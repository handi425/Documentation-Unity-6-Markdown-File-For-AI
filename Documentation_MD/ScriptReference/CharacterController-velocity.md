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

#  [CharacterController](CharacterController.html).velocity

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

public [Vector3](Vector3.html) velocity;

### Description

The current relative velocity of the Character (see notes).

This allows you to track how fast the character is actually walking, for
example when it is stuck at a wall this value will be the zero vector.  
  
Note: The velocity returned is simply the difference in distance for the
current timestep before and after a call to
[CharacterController.Move](CharacterController.Move.html) or
[CharacterController.SimpleMove](CharacterController.SimpleMove.html). The
velocity is relative because it won't track movements to the transform that
happen outside of the CharacterController (e.g. character parented under
another moving Transform, such as a moving vehicle).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [CharacterController](CharacterController.html) controller;
        void Start()
        {
            controller = GetComponent<[CharacterController](CharacterController.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Vector3](Vector3.html) horizontalVelocity = controller.velocity;
            horizontalVelocity = new [Vector3](Vector3.html)(controller.velocity.x, 0, controller.velocity.z);  
      
            // The speed on the x-z plane ignoring any speed
            float horizontalSpeed = horizontalVelocity.magnitude;
            // The speed from gravity or jumping
            float verticalSpeed  = controller.velocity.y;
            // The overall speed
            float overallSpeed = controller.velocity.magnitude;
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

