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

#  [HingeJoint](HingeJoint.html).spring

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

public [JointSpring](JointSpring.html) spring;

### Description

The spring attempts to reach a target angle by adding spring and damping
forces.

The [JointSpring.spring](JointSpring-spring.html) force attempts to reach the
target angle. A larger value makes the spring reach the target position
faster.  
  
The [JointSpring.damper](JointSpring-damper.html) force dampens the angular
velocity. A larger value makes the spring reach the goal slower.  
  
The spring reaches for the [JointSpring.targetPosition](JointSpring-
targetPosition.html) angle in degrees relative to the rest angle. The rest
angle between the bodies is always zero at the beginning of the simulation.  
  
Additional resources: [useSpring](HingeJoint-useSpring.html),
[JointSpring](JointSpring.html), [useAcceleration](HingeJoint-
useAcceleration.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    
    public class HingeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [HingeJoint](HingeJoint.html) hinge = GetComponent<[HingeJoint](HingeJoint.html)>();  
      
            // Make the spring reach shoot for a 70 degree angle.
            // This could be used to fire off a catapult.  
      
            [JointSpring](JointSpring.html) hingeSpring = hinge.spring;
            hingeSpring.spring = 10;
            hingeSpring.damper = 3;
            hingeSpring.targetPosition = 70;
            hinge.spring = hingeSpring;
            hinge.useSpring = true;
        }
    }
    

Modifying the spring does **not** automatically enable it.  
  
Enabling the [motor](HingeJoint-motor.html) **overrides** the spring, given
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

