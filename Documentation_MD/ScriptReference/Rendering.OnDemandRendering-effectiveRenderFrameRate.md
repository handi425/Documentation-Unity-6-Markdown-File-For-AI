[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#
[OnDemandRendering](Rendering.OnDemandRendering.html).effectiveRenderFrameRate

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

public static int effectiveRenderFrameRate;

### Description

The current estimated rate of rendering in frames per second rounded to the
nearest integer.

This is an estimate and may not be achieved depending upon the application.  
If [QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) is greater
than 0 it is calculated by:  
  
FPS = Resolution.refreshRate / [QualitySettings.vSyncCount](QualitySettings-
vSyncCount.html) /
[OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-
renderFrameInterval.html)  
  
If [QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) is 0 and
[Application.targetFrameRate](Application-targetFrameRate.html) is also
greater than 0:  
  
FPS = [Application.targetFrameRate](Application-targetFrameRate.html) /
[OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-
renderFrameInterval.html)  
  
Android, iOS and tvOS use 30 FPS as the default framerate when no other value
has been specified. In that case 30 /
[OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-
renderFrameInterval.html) is returned. All other platforms return the value of
[Application.targetFrameRate](Application-targetFrameRate.html).

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using System.Collections;  
      
    // This example shows how to use effectiveRenderFrameRate to ensure your application renders at a given frame rate regardless of
    // settings that could be changed by the user. Also demonstrates use of setting renderFrameInterval from a coroutine.
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            const int myTargetFrameRate = 10;  
      
            // Start off assuming that [Application.targetFrameRate](Application-targetFrameRate.html) is 60 and [QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) is 0
            [OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html) = 6;  
      
            // Some applications may allow the user to modify the quality level. So we may not be able to rely on
            // the framerate always being a specific value. For this example we want the effective framerate to be 10.
            // If it is not then check the values and adjust the frame interval accordingly to achieve the framerate that we desire.
            if ([OnDemandRendering.effectiveRenderFrameRate](Rendering.OnDemandRendering-effectiveRenderFrameRate.html) != 10)
            {
                if ([QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) > 0)
                {
                    [OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html) = (Screen.currentResolution.refreshRate / [QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) / myTargetFrameRate);
                }
                else
                {
                    [OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html) = ([Application.targetFrameRate](Application-targetFrameRate.html) / myTargetFrameRate);
                }
            }  
      
            StartCoroutine(SlowRenderingFor5Seconds());
        }  
      
        IEnumerator SlowRenderingFor5Seconds()
        {
            // After 5 seconds go back to rendering every frame
            yield return new [WaitForSeconds](WaitForSeconds.html)(5);
            [OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html) = 1;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // For 5 seconds this will report that the effective framerate is 10. Afterward it will log what the framerate is given the current
            // quality and target framerate settings.
            [Debug.Log](Debug.Log.html)("FrameRate: " + [OnDemandRendering.effectiveRenderFrameRate](Rendering.OnDemandRendering-effectiveRenderFrameRate.html));
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

