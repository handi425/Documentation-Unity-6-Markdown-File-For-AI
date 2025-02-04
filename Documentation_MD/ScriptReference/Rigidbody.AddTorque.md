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

#  [Rigidbody](Rigidbody.html).AddTorque

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

public void AddTorque([Vector3](Vector3.html) torque,
[ForceMode](ForceMode.html) mode = ForceMode.Force);

### Parameters

torque | Torque vector in world coordinates.  
---|---  
mode | The type of torque to apply.  
  
### Description

Adds a torque to the rigidbody.

Force can be applied only to an active rigidbody. If a GameObject is inactive,
AddTorque has no effect.  
  
The effects of the torques applied with this function are accumulated at the
time of the call. The physics system applies the effects during the next
simulation run (either after [FixedUpdate](PlayerLoop.FixedUpdate.html), or
when the script explicitly calls the [Physics.Simulate](Physics.Simulate.html)
method). Because this function has different modes, the physics system only
accumulates the resulting angular velocity change, not the passed torque
values. Assuming deltaTime (DT) is equal to the simulation step length
([Time.fixedDeltaTime](Time-fixedDeltaTime.html)), and mass is equal to the
mass of the Rigidbody the torque is being applied to, here is how the angular
velocity change is calculated for all the modes:

  * ForceMode.Force: Interprets the input as torque (measured in Newton-metres), and changes the angular velocity by the value of torque * DT / mass. The effect depends on the simulation step length and the mass of the body.
  * ForceMode.Acceleration: Interprets the parameter as angular acceleration (measured in degrees per second squared), and changes the angular velocity by the value of torque * DT. The effect depends on the simulation step length but does not depend on the mass of the body.
  * ForceMode.Impulse: Interprets the parameter as an angular momentum (measured in kilogram-meters-squared per second), and changes the angular velocity by the value of torque / mass. The effect depends on the mass of the body but doesn't depend on the simulation step length.
  * ForceMode.VelocityChange: Interprets the parameter as a direct angular velocity change (measured in degrees per second), and changes the angular velocity by the value of torque. The effect doesn't depend on the mass of the body and the simulation step length.

Wakes up the Rigidbody by default. If the torque size is zero then the
Rigidbody will not be woken up.  
  
Additional resources: [AddRelativeTorque](Rigidbody.AddRelativeTorque.html),
[AddForce](Rigidbody.AddForce.html).

    
    
    // [Rotate](UIElements.Rotate.html) an object around its Y (upward) axis in response to
    // left/right controls.
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float torque;
        public [Rigidbody](Rigidbody.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            float turn = [Input.GetAxis](Input.GetAxis.html)("Horizontal");
            rb.AddTorque(transform.up * torque * turn);
        }
    }
    

* * *

## Declaration

public void AddTorque(float x, float y, float z, [ForceMode](ForceMode.html)
mode = ForceMode.Force);

### Parameters

x | Size of torque along the world x-axis.  
---|---  
y | Size of torque along the world y-axis.  
z | Size of torque along the world z-axis.  
mode | The type of torque to apply.  
  
### Description

Adds a torque to the rigidbody.

Force can be applied only to an active rigidbody. If a GameObject is inactive,
AddTorque has no effect.  
  
Wakes up the Rigidbody by default. If the torque size is zero then the
Rigidbody will not be woken up.

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

