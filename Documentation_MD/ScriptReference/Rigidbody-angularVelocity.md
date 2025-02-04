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

#  [Rigidbody](Rigidbody.html).angularVelocity

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

public [Vector3](Vector3.html) angularVelocity;

### Description

The angular velocity vector of the rigidbody measured in radians per second.

In most cases you should not modify it directly, as this can result in
unrealistic behaviour. Note that if the Rigidbody has rotational constraints
set, the corresponding angular velocity components are set to zero in the mass
space (ie relative to the inertia tensor rotation) at the time of the call.
Additionally, setting the angular velocity of a kinematic rigidbody is not
allowed and will have no effect.

    
    
    // Change the material depending on the speed of rotation
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Material](Material.html) fastWheelMaterial;
        public [Material](Material.html) slowWheelMaterial;
        public [Rigidbody](Rigidbody.html) rb;
        public [MeshRenderer](MeshRenderer.html) rend;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody](Rigidbody.html)>();
            rend = GetComponent<[MeshRenderer](MeshRenderer.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (rb.angularVelocity.magnitude < 5)
                rend.sharedMaterial = slowWheelMaterial;
            else
                rend.sharedMaterial = fastWheelMaterial;
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

