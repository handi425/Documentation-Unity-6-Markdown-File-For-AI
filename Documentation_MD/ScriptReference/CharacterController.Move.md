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

#  [CharacterController](CharacterController.html).Move

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

## Declaration

public [CollisionFlags](CollisionFlags.html) Move([Vector3](Vector3.html)
motion);

### Description

Supplies the movement of a GameObject with an attached CharacterController
component.

The [CharacterController.Move](CharacterController.Move.html) motion moves the
GameObject in the given direction. The given direction requires absolute
movement delta values. A collision constrains the
[Move](CharacterController.Move.html) from taking place. The return,
[CollisionFlags](CollisionFlags.html), indicates the direction of a collision:
None, Sides, Above, and Below.
[CharacterController.Move](CharacterController.Move.html) does not use
gravity.  
  
The example below demonstrates how to use
[CharacterController.Move](CharacterController.Move.html). `Update` causes a
[Move](CharacterController.Move.html) to re-position the player. In addition,
`Jump` changes the player position in a vertical direction.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private [CharacterController](CharacterController.html) controller;
        private [Vector3](Vector3.html) playerVelocity;
        private bool groundedPlayer;
        private float playerSpeed = 2.0f;
        private float jumpHeight = 1.0f;
        private float gravityValue = -9.81f;  
      
        private void Start()
        {
            controller = gameObject.AddComponent<[CharacterController](CharacterController.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            groundedPlayer = controller.isGrounded;
            if (groundedPlayer && playerVelocity.y < 0)
            {
                playerVelocity.y = 0f;
            }  
      
            [Vector3](Vector3.html) move = new [Vector3](Vector3.html)([Input.GetAxis](Input.GetAxis.html)("Horizontal"), 0, [Input.GetAxis](Input.GetAxis.html)("Vertical"));
            controller.Move(move * [Time.deltaTime](Time-deltaTime.html) * playerSpeed);  
      
            if (move != [Vector3.zero](Vector3-zero.html))
            {
                gameObject.transform.forward = move;
            }  
      
            // Makes the player jump
            if ([Input.GetButtonDown](Input.GetButtonDown.html)("Jump") && groundedPlayer)
            {
                playerVelocity.y += [Mathf.Sqrt](Mathf.Sqrt.html)(jumpHeight * -2.0f * gravityValue);
            }  
      
            playerVelocity.y += gravityValue * [Time.deltaTime](Time-deltaTime.html);
            controller.Move(playerVelocity * [Time.deltaTime](Time-deltaTime.html));
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

