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

#  [HingeJoint](HingeJoint.html).motor

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

[Switch to Manual](../Manual/class-HingeJoint.html "Go to HingeJoint Component
in the Manual")

public [JointMotor](JointMotor.html) motor;

### Description

The motor will apply a force up to a maximum force to achieve the target
velocity in degrees per second.

The motor tries to reach [JointMotor.targetVelocity](JointMotor-
targetVelocity.html) angular velocity in degrees per second. The motor will
only be able to reach `targetVelocity`, if [JointMotor.force](JointMotor-
force.html) is sufficiently large. If the joint is spinning faster than
`targetVelocity` the motor will brake. A negative `targetVelocity` will make
the motor spin in the opposite direction.  
  
The `force` is the maximum torque the motor can exert. If it is zero the motor
is disabled.  
  
The motor will brake when it is spinning faster than `targetVelocity` only, if
[JointMotor.freeSpin](JointMotor-freeSpin.html) is false. If `freeSpin` is
true the motor will not brake.  
  
Additional resources: [useMotor](HingeJoint-useMotor.html),
[JointMotor](JointMotor.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var hinge = GetComponent<[HingeJoint](HingeJoint.html)>();  
      
            // Make the hinge motor rotate with 90 degrees per second and a strong force.
            var motor = hinge.motor;
            motor.force = 100;
            motor.targetVelocity = 90;
            motor.freeSpin = false;
            hinge.motor = motor;
            hinge.useMotor = true;
        }
    }
    

Modifying the motor does **not** automatically enable the motor.  
  
Enabling the motor **overrides** the [spring](HingeJoint-spring.html), given
the spring was enabled. If the motor is again disabled the spring will be
restored.

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

