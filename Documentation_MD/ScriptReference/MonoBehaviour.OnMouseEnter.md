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

#  [MonoBehaviour](MonoBehaviour.html).OnMouseEnter()

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

Called when the mouse enters the [Collider](Collider.html).

The corresponding [OnMouseOver](MonoBehaviour.OnMouseOver.html) function is
called while the mouse stays over the object and
[OnMouseExit](MonoBehaviour.OnMouseExit.html) is called when it moves away.

    
    
    // Change the mesh color in response to mouse actions.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Renderer](Renderer.html) rend;  
      
        void Start()
        {
            rend = GetComponent<[Renderer](Renderer.html)>();
        }  
      
        // The mesh goes red when the mouse is over it...
        void OnMouseEnter()
        {
            rend.material.color = [Color.red](Color-red.html);
        }  
      
        // ...the red fades out to cyan as the mouse is held over...
        void OnMouseOver()
        {
            rend.material.color -= new [Color](Color.html)(0.1F, 0, 0) * [Time.deltaTime](Time-deltaTime.html);
        }  
      
        // ...and the mesh finally turns white when the mouse moves away.
        void OnMouseExit()
        {
            rend.material.color = [Color.white](Color-white.html);
        }
    }
    

This function is not called on objects that belong to Ignore Raycast layer.  
  
This function is called on Colliders and 2D Colliders marked as trigger when
the following properties are set to true:  
  
\- For 3D physics: [Physics.queriesHitTriggers](Physics-
queriesHitTriggers.html)  
  
\- For 2D physics:
[Physics2D.queriesHitTriggers](Physics2D-queriesHitTriggers.html)  
  
OnMouseEnter can be a co-routine, simply use the yield statement in the
function. This event is sent to all scripts attached to the
[Collider](Collider.html).  
  
Additional resources: [OnMouseOver](MonoBehaviour.OnMouseOver.html),
[OnMouseExit](MonoBehaviour.OnMouseExit.html).

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

