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

#  [MonoBehaviour](MonoBehaviour.html).OnMouseUp()

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

OnMouseUp is called when the user has released the mouse button.

Note that OnMouseUp is called even if the mouse is not over the same
[Collider](Collider.html) as the mouse has been pressed down on. For button-
like behavior see: [OnMouseUpAsButton](MonoBehaviour.OnMouseUpAsButton.html).

    
    
    // Register when mouse dragging has ended. OnMouseUp is called
    // when the mouse button is released.  
      
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnMouseUp()
        {
            // If the user releases the mouse button while over the [GameObject](GameObject.html) with this script attached, output this message
            [Debug.Log](Debug.Log.html)("Drag ended!");
        }
    }
    

**Note:** This function is not called on objects that belong to Ignore Raycast
layer.  
  
This function is called on Colliders and 2D Colliders marked as trigger when
the following properties are set to true:  
  
\- For 3D physics: [Physics.queriesHitTriggers](Physics-
queriesHitTriggers.html)  
  
\- For 2D physics:
[Physics2D.queriesHitTriggers](Physics2D-queriesHitTriggers.html)  
  
[OnMouseUp](MonoBehaviour.OnMouseUp.html) can be a co-routine. Simply use the
yield statement in the function. This event is sent to all scripts attached to
the [Collider](Collider.html).  
  
Additional resources: [OnMouseDown](MonoBehaviour.OnMouseDown.html),
[OnMouseDrag](MonoBehaviour.OnMouseDrag.html).

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

