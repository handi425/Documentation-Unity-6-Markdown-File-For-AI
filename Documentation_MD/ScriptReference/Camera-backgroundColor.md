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

#  [Camera](Camera.html).backgroundColor

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

public [Color](Color.html) backgroundColor;

### Description

The color with which the screen will be cleared.

Only used if [clearFlags](Camera-clearFlags.html) are set to
[CameraClearFlags.SolidColor](CameraClearFlags.SolidColor.html) (or
[CameraClearFlags.Skybox](CameraClearFlags.Skybox.html) but the skybox is not
set up).

    
    
    // ping-pong animate background color
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Color](Color.html) color1 = [Color.red](Color-red.html);
        public [Color](Color.html) color2 = [Color.blue](Color-blue.html);
        public float duration = 3.0F;  
      
        public [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
            cam.clearFlags = [CameraClearFlags.SolidColor](CameraClearFlags.SolidColor.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            float t = [Mathf.PingPong](Mathf.PingPong.html)([Time.time](Time-time.html), duration) / duration;
            cam.backgroundColor = [Color.Lerp](Color.Lerp.html)(color1, color2, t);
        }
    }
    

Additional resources: [camera component](../Manual/class-Camera.html),
[Camera.clearFlags](Camera-clearFlags.html)

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

