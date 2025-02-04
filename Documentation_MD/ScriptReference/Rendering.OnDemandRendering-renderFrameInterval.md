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

#  [OnDemandRendering](Rendering.OnDemandRendering.html).renderFrameInterval

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

public static int renderFrameInterval;

### Description

Get or set the current frame rate interval. To restore rendering back to the
value of [Application.targetFrameRate](Application-targetFrameRate.html) or
[QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) set this to 0 or
1.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    // This example shows how to get and set the current frame rate interval and what you can do with that information.
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) = 0;
            [Application.targetFrameRate](Application-targetFrameRate.html) = 60;
            [OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html) = 6;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetMouseButton](Input.GetMouseButton.html)(0) || ([Input.touchCount](Input-touchCount.html) > 0))
            {
                // If the mouse button or a finger is down render at 60 FPS (every frame).
                [OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html) = 1;
            }
            else
            {
                // If there isn't any input then we can go back to 10 FPS (every 6 frames).
                [OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html) = 6;
            }  
      
            // We've decided to lower the frame rate by increasing the frame interval. Perhaps in a pause menu.
            // There may be some other systems that we don't need at that time.
            if ([OnDemandRendering.renderFrameInterval](Rendering.OnDemandRendering-renderFrameInterval.html) > 1)
            {
                // Disable physics
                Physics.autoSimulation = false;  
      
                // Disable other systems or turn down audio volume for example.
            }
            else
            {
                // If we are back to the normal framerate turn physics back on.
                Physics.autoSimulation = true;
            }
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

