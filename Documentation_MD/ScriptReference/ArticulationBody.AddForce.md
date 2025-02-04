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

#  [ArticulationBody](ArticulationBody.html).AddForce

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

[Switch to Manual](../Manual/class-ArticulationBody.html "Go to
ArticulationBody Component in the Manual")

## Declaration

public void AddForce([Vector3](Vector3.html) force,
[ForceMode](ForceMode.html) mode = ForceMode.Force);

### Parameters

force | The force vector to apply.  
---|---  
mode | The type of force to apply.  
  
### Description

Applies a force to the [ArticulationBody](ArticulationBody.html).

Note that the force accumulates over the duration of a simulation frame. It is
only physically applied to the articulation body during the simulation step,
after [FixedUpdate](PlayerLoop.FixedUpdate.html) has been called to scripts.
Specifying the [ForceMode](ForceMode.html) `mode` allows the type of force to
be changed to an Acceleration, Impulse or Velocity Change.  
  
You can only apply a force to an active ArticulationBody. If a GameObject is
inactive, AddForce has no effect. Also, the ArticulationBody must be movable
(cannot be immovable).  
  
[ForceMode.Force](ForceMode.Force.html) and
[ForceMode.Acceleration](ForceMode.Acceleration.html) modes modify the Linear
Velocity Per Second accumulator and
[ForceMode.Impulse](ForceMode.Impulse.html) and
[ForceMode.VelocityChange](ForceMode.VelocityChange.html) modify the Linear
Velocity Per Step accumulator. Mixing these 2 groups of ForceModes doesn't
work for Articulation Bodies and will result in only the Linear Velocity Per
Second accumulator being applied.  
  
For more information on how ForceMode affects velocity, see
[Rigidbody.AddForce](Rigidbody.AddForce.html).  
  
By default the ArticulationBody's state is set to awake when a force is
applied, unless the force is [Vector3.zero](Vector3-zero.html).  
Unit of measurement - N (newtons).  
  
Additional resources:
[AddForceAtPosition](ArticulationBody.AddForceAtPosition.html),
[AddRelativeForce](ArticulationBody.AddRelativeForce.html),
[AddTorque](ArticulationBody.AddTorque.html).  
  
This example applies a forward force to the GameObject's ArticulationBody.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [ArticulationBody](ArticulationBody.html) m_ArticulationBody;
        public float m_Thrust = 20f;  
      
        void Start()
        {
            //Fetch the [ArticulationBody](ArticulationBody.html) from the [GameObject](GameObject.html) with this script attached
            m_ArticulationBody = GetComponent<[ArticulationBody](ArticulationBody.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            if ([Input.GetButton](Input.GetButton.html)("Jump"))
            {
                //Apply a force to this [ArticulationBody](ArticulationBody.html) in the direction of this [GameObject](GameObject.html)'s up-axis
                m_ArticulationBody.AddForce(transform.up * m_Thrust);
            }
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

