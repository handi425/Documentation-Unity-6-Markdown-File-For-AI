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

#  [Rigidbody](Rigidbody.html).AddForceAtPosition

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

[Switch to Manual](../Manual/class-Rigidbody.html "Go to Rigidbody Component
in the Manual")

## Declaration

public void AddForceAtPosition([Vector3](Vector3.html) force,
[Vector3](Vector3.html) position, [ForceMode](ForceMode.html) mode =
ForceMode.Force);

### Parameters

force | Force vector in world coordinates.  
---|---  
position | Position in world coordinates.  
  
### Description

Applies `force` at `position`. As a result this will apply a torque and force
on the object.

For realistic effects `position` should be approximately in the range of the
surface of the rigidbody. This is most commonly used for explosions. When
applying explosions it is best to apply forces over several frames instead of
just one. Note that when `position` is far away from the center of the
rigidbody the applied torque will be unrealistically large.  
  
Force can be applied only to an active rigidbody. If a GameObject is inactive,
AddForceAtPosition has no effect.  
  
Wakes up the Rigidbody by default. If the force size is zero then the
Rigidbody will not be woken up.  
  
For more information on how ForceMode affects velocity, see
[Rigidbody.AddForce](Rigidbody.AddForce.html).  
  
Additional resources: [AddForce](Rigidbody.AddForce.html),
[AddRelativeForce](Rigidbody.AddRelativeForce.html),
[AddTorque](Rigidbody.AddTorque.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void ApplyForce([Rigidbody](Rigidbody.html) body)
        {
            [Vector3](Vector3.html) direction = body.transform.position - transform.position;
            body.AddForceAtPosition(direction.normalized, transform.position);
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

