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

#  [Rigidbody](Rigidbody.html).AddRelativeForce

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

public void AddRelativeForce([Vector3](Vector3.html) force,
[ForceMode](ForceMode.html) mode = ForceMode.Force);

### Parameters

force | Force vector in local coordinates.  
---|---  
  
### Description

Adds a force to the rigidbody relative to its coordinate system.

Force can be applied only to an active rigidbody. If a GameObject is inactive,
AddRelativeForce has no effect.  
  
Wakes up the Rigidbody by default. If the force size is zero then the
Rigidbody will not be woken up.  
  
For more information on how ForceMode affects velocity, see
[Rigidbody.AddForce](Rigidbody.AddForce.html).  
  
Additional resources: [AddForce](Rigidbody.AddForce.html),
[AddForceAtPosition](Rigidbody.AddForceAtPosition.html),
[AddRelativeTorque](Rigidbody.AddRelativeTorque.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Add a thrust force to push an object in its current forward
    // direction (to simulate a rocket motor, say).
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float thrust;
        public [Rigidbody](Rigidbody.html) rb;
        void Start()
        {
            rb = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            rb.AddRelativeForce([Vector3.forward](Vector3-forward.html) * thrust);
        }
    }
    

* * *

## Declaration

public void AddRelativeForce(float x, float y, float z,
[ForceMode](ForceMode.html) mode = ForceMode.Force);

### Parameters

x | Size of force along the local x-axis.  
---|---  
y | Size of force along the local y-axis.  
z | Size of force along the local z-axis.  
  
### Description

Adds a force to the rigidbody relative to its coordinate system.

Force can be applied only to an active rigidbody. If a GameObject is inactive,
AddRelativeForce has no effect.  
  
Wakes up the Rigidbody by default. If the force size is zero then the
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

