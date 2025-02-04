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

#  [Camera](Camera.html).rect

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

public [Rect](Rect.html) rect;

### Description

Where on the screen is the camera rendered in normalized coordinates.

In `rect`, the bottom-left of the screen is (0,0) and the top-right of the
screen is (1,1).

    
    
    using UnityEngine;  
      
    // Change the width of the viewport each time space key is pressed  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = [Camera.main](Camera-main.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKey](Input.GetKey.html)("space"))
            {
                // choose the margin randomly
                float margin = [Random.Range](Random.Range.html)(0.0f, 0.3f);
                // setup the rectangle
                cam.rect = new [Rect](Rect.html)(margin, 0.0f, 1.0f - margin * 2.0f, 1.0f);
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

