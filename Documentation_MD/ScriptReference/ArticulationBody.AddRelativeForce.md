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

#  [ArticulationBody](ArticulationBody.html).AddRelativeForce

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

public void AddRelativeForce([Vector3](Vector3.html) force,
[ForceMode](ForceMode.html) mode = ForceMode.Force);

### Parameters

force | The force vector in local coordinates.  
---|---  
mode | The type of force to apply.  
  
### Description

Applies a `force` to the Articulation Body, relative to its local coordinate
system.

You can only apply a force to an active ArticulationBody. If a GameObject is
inactive, AddRelativeForce has no effect.  
  
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
  
Applying a force to an ArticulationBody wakes up that body. If the force size
is zero then the ArticulationBody does not wake up.  
Unit of measurement - N (newtons).  
  
Additional resources: [AddForce](ArticulationBody.AddForce.html),
[AddForceAtPosition](ArticulationBody.AddForceAtPosition.html),
[AddRelativeTorque](ArticulationBody.AddRelativeTorque.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Add a thrust force to push an object in its current forward
    // direction (to simulate a rocket motor, say).
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float thrust;
        public [ArticulationBody](ArticulationBody.html) ab;
        void Start()
        {
            ab = GetComponent<[ArticulationBody](ArticulationBody.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            ab.AddRelativeForce([Vector3.forward](Vector3-forward.html) * thrust);
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

