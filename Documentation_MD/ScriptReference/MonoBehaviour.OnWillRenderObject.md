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

#  [MonoBehaviour](MonoBehaviour.html).OnWillRenderObject()

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

OnWillRenderObject is called for each camera if the object is visible and not
a UI element.

The function is not called if the MonoBehaviour is disabled.  
  
The function is called during the culling process just before rendering each
culled object.  
  
Note that [Camera.current](Camera-current.html) will be set to the camera that
will render the object.  
  
**Note:** This has no effect when called from a UI element.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Renderer](Renderer.html) rend;  
      
        private float timePass = 0.0f;  
      
        void Start()
        {
            rend = GetComponent<[Renderer](Renderer.html)>();
        }  
      
        void OnWillRenderObject()
        {
            timePass += [Time.deltaTime](Time-deltaTime.html);  
      
            if (timePass > 1.0f)
            {
                timePass = 0.0f;
                print(gameObject.name + " is being rendered by " + Camera.current.name + " at " + [Time.time](Time-time.html));
            }
        }
    }
    

This is called multiple times per frame.

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

