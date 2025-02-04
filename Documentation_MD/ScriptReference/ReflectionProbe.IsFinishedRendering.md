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

#  [ReflectionProbe](ReflectionProbe.html).IsFinishedRendering

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

[Switch to Manual](../Manual/class-ReflectionProbe.html "Go to ReflectionProbe
Component in the Manual")

## Declaration

public bool IsFinishedRendering(int renderId);

### Parameters

renderId | An integer representing the RenderID as returned by the RenderProbe method.  
---|---  
  
### Returns

**bool** True if the render has finished, false otherwise.  
  
Additional resources: [timeSlicingMode](ReflectionProbe-timeSlicingMode.html)

### Description

Checks if a probe has finished a time-sliced render.

    
    
    using UnityEngine;
    using System.Collections;  
      
    
    public class UpdateProbeEvery2Seconds : [MonoBehaviour](MonoBehaviour.html)
    {
        private int RenderId = -1;
        private [ReflectionProbe](ReflectionProbe.html) TheProbe;
        public [RenderTexture](RenderTexture.html) TargetTexture;  
      
        IEnumerator Start()
        {
            TheProbe = GetComponent<[ReflectionProbe](ReflectionProbe.html)>();  
      
            // set the probe to render in time-slicing mode and make sure all faces of the cubemap render the same frame.
            TheProbe.timeSlicingMode = UnityEngine.Rendering.ReflectionProbeTimeSlicingMode.AllFacesAtOnce;
            while (true)
            {
                yield return new [WaitForSeconds](WaitForSeconds.html)(2.0f);  
      
                // render the probe over several frames and blit into TargetTexture once finished.
                RenderId = TheProbe.RenderProbe(TargetTexture);
            }
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (TheProbe.IsFinishedRendering(RenderId))
            {
                // Probe has finished rendering, do something with the render texture
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

