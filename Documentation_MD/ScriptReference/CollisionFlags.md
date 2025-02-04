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

# CollisionFlags

enumeration

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

### Description

CollisionFlags is a bitmask returned by CharacterController.Move.

It gives you a broad overview of where your character collided with any other
objects.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            [CharacterController](CharacterController.html) controller = GetComponent<[CharacterController](CharacterController.html)>();  
      
            if (controller.collisionFlags == [CollisionFlags.None](CollisionFlags.None.html))
            {
                print("Free floating!");
            }  
      
            if ((controller.collisionFlags & [CollisionFlags.Sides](CollisionFlags.Sides.html)) != 0)
            {
                print("Touching sides!");
            }  
      
            if (controller.collisionFlags == [CollisionFlags.Sides](CollisionFlags.Sides.html))
            {
                print("Only touching sides, nothing else!");
            }  
      
            if ((controller.collisionFlags & [CollisionFlags.Above](CollisionFlags.Above.html)) != 0)
            {
                print("Touching Ceiling!");
            }  
      
            if (controller.collisionFlags == [CollisionFlags.Above](CollisionFlags.Above.html))
            {
                print("Only touching Ceiling, nothing else!");
            }  
      
            if ((controller.collisionFlags & [CollisionFlags.Below](CollisionFlags.Below.html)) != 0)
            {
                print("Touching ground!");
            }  
      
            if (controller.collisionFlags == [CollisionFlags.Below](CollisionFlags.Below.html))
            {
                print("Only touching ground, nothing else!");
            }
        }
    }
    

### Properties

[None](CollisionFlags.None.html)| CollisionFlags is a bitmask returned by
CharacterController.Move.  
---|---  
[Sides](CollisionFlags.Sides.html)| CollisionFlags is a bitmask returned by
CharacterController.Move.  
[Above](CollisionFlags.Above.html)| CollisionFlags is a bitmask returned by
CharacterController.Move.  
[Below](CollisionFlags.Below.html)| CollisionFlags is a bitmask returned by
CharacterController.Move.  
  
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

