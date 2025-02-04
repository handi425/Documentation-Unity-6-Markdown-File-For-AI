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

#  [Rigidbody2D](Rigidbody2D.html).totalForce

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

public [Vector2](Vector2.html) totalForce;

### Description

The total amount of force that has been explicitly applied to this
[Rigidbody2D](Rigidbody2D.html) since the last physics simulation step.

When adding force to the [Rigidbody2D](Rigidbody2D.html) using
[Rigidbody2D.AddForce](Rigidbody2D.AddForce.html),
[Rigidbody2D.AddForceAtPosition](Rigidbody2D.AddForceAtPosition.html) or
[Rigidbody2D.AddRelativeForce](Rigidbody2D.AddRelativeForce.html) the force
total is summed. This only applies when using
[ForceMode2D.Force](ForceMode2D.Force.html) and not when using
[ForceMode2D.Impulse](ForceMode2D.Impulse.html).  
  
During the next simulation step, the total force will be time-integrated into
the [Rigidbody2D.linearVelocity](Rigidbody2D-linearVelocity.html) then
automatically reset to [zero](Vector2-zero.html).  
  
**NOTE** : Only a [Rigidbody2D](Rigidbody2D.html) with a [Dynamic Body
Type](RigidbodyType2D.Dynamic.html) will respond to force or torque. Setting
this property on a [Kinematic Body Type](RigidbodyType2D.Kinematic.html) or
[Static Body Type](RigidbodyType2D.Static.html) will have no effect.

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Fetch the rigidbody.
            var body = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();  
      
            // Make the assumption the body has no previous force applied.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.zero](Vector2-zero.html), body.totalForce);  
      
            // Initialize a force.
            var force = new [Vector2](Vector2.html)(3f, 2f);  
      
            // Add the force.
            body.AddForce(force);  
      
            // The total force should be what we just added.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(force, body.totalForce);  
      
            // Add the same force again.
            body.AddForce(force);  
      
            // The total force should still be what we've added.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(force * 2f, body.totalForce);  
      
            // We can reset any force that has been applied since the last simulation step.
            body.totalForce = [Vector2.zero](Vector2-zero.html);
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

