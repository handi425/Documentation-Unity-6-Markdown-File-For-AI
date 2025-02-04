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
[CharacterController](CharacterController.html).OnControllerColliderHit(ControllerColliderHit)

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

[Switch to Manual](../Manual/class-CharacterController.html "Go to
CharacterController Component in the Manual")

### Description

OnControllerColliderHit is called when the controller hits a collider while
performing a Move.

This can be used to push objects when they collide with the character.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // this script pushes all rigidbodies that the character touches
        float pushPower = 2.0f;
        void OnControllerColliderHit([ControllerColliderHit](ControllerColliderHit.html) hit)
        {
            [Rigidbody](Rigidbody.html) body = hit.collider.attachedRigidbody;  
      
            // no rigidbody
            if (body == null || body.isKinematic)
            {
                return;
            }  
      
            // We dont want to push objects below us
            if (hit.moveDirection.y < -0.3)
            {
                return;
            }  
      
            // Calculate push direction from move direction,
            // we only push objects to the sides never up and down
            [Vector3](Vector3.html) pushDir = new [Vector3](Vector3.html)(hit.moveDirection.x, 0, hit.moveDirection.z);  
      
            // If you know how fast your character is trying to move,
            // then you can also multiply the push velocity by that.  
      
            // Apply the push
            body.velocity = pushDir * pushPower;
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

