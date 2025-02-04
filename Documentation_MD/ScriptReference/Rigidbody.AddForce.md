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

#  [Rigidbody](Rigidbody.html).AddForce

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

public void AddForce([Vector3](Vector3.html) force,
[ForceMode](ForceMode.html) mode = ForceMode.Force);

### Parameters

force | Force vector in world coordinates.  
---|---  
mode | Type of force to apply.  
  
### Description

Adds a force to the [Rigidbody](Rigidbody.html).

Force is applied continuously along the direction of the `force` vector.
Specifying the [ForceMode](ForceMode.html) `mode` allows the type of force to
be changed to an Acceleration, Impulse or Velocity Change.  
  
The effects of the forces applied with this function are accumulated at the
time of the call. The physics system applies the effects during the next
simulation run (either after [FixedUpdate](PlayerLoop.FixedUpdate.html), or
when the script explicitly calls the [Physics.Simulate](Physics.Simulate.html)
method). Because this function has different modes, the physics system only
accumulates the resulting velocity change, not the passed force values.
Assuming deltaTime (DT) is equal to the simulation step length
([Time.fixedDeltaTime](Time-fixedDeltaTime.html)), and mass is equal to the
mass of the Rigidbody the force is being applied to, here is how the velocity
change is calculated for all the modes:

  * [ForceMode.Force](ForceMode.Force.html): Interprets the input as force (measured in Newtons), and changes the velocity by the value of force * DT / mass. The effect depends on the simulation step length and the mass of the body.
  * [ForceMode.Acceleration](ForceMode.Acceleration.html): Interprets the parameter as acceleration (measured in meters per second squared), and changes the velocity by the value of force * DT. The effect depends on the simulation step length but doesn't depend on the mass of the body.
  * [ForceMode.Impulse](ForceMode.Impulse.html): Interprets the parameter as an impulse (measured in newton-seconds), and changes the velocity by the value of force / mass. The effect depends on the mass of the body but doesn't depend on the simulation step length.
  * [ForceMode.VelocityChange](ForceMode.VelocityChange.html): Interprets the parameter as a direct velocity change (measured in meters per second), and changes the velocity by the value of force. The effect doesn't depend on the mass of the body or the simulation step length.

Force can only be applied to an active Rigidbody. If a GameObject is inactive,
AddForce has no effect. Also, the Rigidbody cannot be kinematic.  
  
By default the Rigidbody's state is set to awake once a force is applied,
unless the force is [Vector3.zero](Vector3-zero.html).  
  
Additional resources: [AddForceAtPosition](Rigidbody.AddForceAtPosition.html),
[AddRelativeForce](Rigidbody.AddRelativeForce.html),
[AddTorque](Rigidbody.AddTorque.html).  
  
This example applies a forward force to the GameObject's Rigidbody.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) m_Rigidbody;
        public float m_Thrust = 20f;  
      
        void Start()
        {
            //Fetch the [Rigidbody](Rigidbody.html) from the [GameObject](GameObject.html) with this script attached
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            if ([Input.GetButton](Input.GetButton.html)("Jump"))
            {
                //Apply a force to this [Rigidbody](Rigidbody.html) in direction of this GameObjects up axis
                m_Rigidbody.AddForce(transform.up * m_Thrust);
            }
        }
    }
    

* * *

## Declaration

public void AddForce(float x, float y, float z, [ForceMode](ForceMode.html)
mode = ForceMode.Force);

### Parameters

x | Size of force along the world x-axis.  
---|---  
y | Size of force along the world y-axis.  
z | Size of force along the world z-axis.  
mode | Type of force to apply.  
  
### Description

Adds a force to the [Rigidbody](Rigidbody.html).

This example applies an Impulse force along the Z axis to the GameObject's
Rigidbody.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public float thrust = 1.0f;
        public [Rigidbody](Rigidbody.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody](Rigidbody.html)>();
            rb.AddForce(0, 0, thrust, [ForceMode.Impulse](ForceMode.Impulse.html));
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

