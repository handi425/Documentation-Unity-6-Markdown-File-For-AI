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

#  [ArticulationBody](ArticulationBody.html).AddTorque

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

public void AddTorque([Vector3](Vector3.html) torque,
[ForceMode](ForceMode.html) mode = ForceMode.Force);

### Parameters

torque | The torque to apply.  
---|---  
mode | The type of torque to apply.  
  
### Description

Add torque to the articulation body.

You can only apply a torque to an active ArticulationBody. If a GameObject is
inactive, AddTorque has no effect.  
  
[ForceMode.Force](ForceMode.Force.html) and
[ForceMode.Acceleration](ForceMode.Acceleration.html) modes modify the Angular
Velocity Per Second accumulator and
[ForceMode.Impulse](ForceMode.Impulse.html) and
[ForceMode.VelocityChange](ForceMode.VelocityChange.html) modify the Angular
Velocity Per Step accumulator. Mixing these 2 groups of ForceModes doesn't
work for Articulation Bodies and will result in only the Angular Velocity Per
Second accumulator being applied.  
  
For more information on how ForceMode affects angular velocity, see
[Rigidbody.AddTorque](Rigidbody.AddTorque.html).  
  
Applying a torque to an ArticulationBody wakes up that body. If the torque
size is zero then the ArticulationBody does not wake up.  
Unit of measurement - Nm (Newtonmeters).  
  
Additional resources:
[AddRelativeTorque](ArticulationBody.AddRelativeTorque.html),
[AddForce](ArticulationBody.AddForce.html).

    
    
    // [Rotate](UIElements.Rotate.html) an object around its Y (upward) axis in response to
    // left/right controls.
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float torque;
        public [ArticulationBody](ArticulationBody.html) ab;  
      
        void Start()
        {
            ab = GetComponent<[ArticulationBody](ArticulationBody.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            float turn = [Input.GetAxis](Input.GetAxis.html)("Horizontal");
            ab.AddTorque(transform.up * torque * turn);
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

