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

# JointMotor

struct in UnityEngine

/

Implemented in:[UnityEngine.PhysicsModule](UnityEngine.PhysicsModule.html)

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

The JointMotor is used to motorize a joint.

For example the [HingeJoint](HingeJoint.html) can be told to rotate at a given
speed and force. The joint will then attempt to reach the velocity with the
given maximum force.  
Additional resources: [HingeJoint](HingeJoint.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [HingeJoint](HingeJoint.html) hinge = GetComponent<[HingeJoint](HingeJoint.html)>();  
      
            // Make the hinge motor rotate with 90 degrees per second and a strong force.
            [JointMotor](JointMotor.html) motor = hinge.motor;
            motor.force = 100;
            motor.targetVelocity = 90;
            motor.freeSpin = false;
            hinge.motor = motor;
        }
    }
    

### Properties

[force](JointMotor-force.html)| The motor will apply a force.  
---|---  
[freeSpin](JointMotor-freeSpin.html)| If freeSpin is enabled the motor will
only accelerate but never slow down.  
[targetVelocity](JointMotor-targetVelocity.html)| The motor will apply a force
up to force to achieve targetVelocity.  
  
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

