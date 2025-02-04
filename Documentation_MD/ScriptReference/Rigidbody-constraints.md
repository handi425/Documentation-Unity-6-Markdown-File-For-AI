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

#  [Rigidbody](Rigidbody.html).constraints

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

public [RigidbodyConstraints](RigidbodyConstraints.html) constraints;

### Description

Controls which degrees of freedom are allowed for the simulation of this
Rigidbody.

By default this is set to
[RigidbodyConstraints.None](RigidbodyConstraints.None.html), allowing rotation
and movement along all axes. In some cases, you may want to constrain a
[Rigidbody](Rigidbody.html) to only move or rotate along some axes, for
example when developing 2D games. You can use the bitwise OR operator to
combine multiple constraints.  
  
Note that position constraints are applied in World space, and rotation
constraints are applied in the inertia space (relative to
[Rigidbody.inertiaTensorRotation](Rigidbody-inertiaTensorRotation.html)).

    
    
    //Attach this script to a [GameObject](GameObject.html).
    //Attach a [Rigidbody](Rigidbody.html) to the [GameObject](GameObject.html) by clicking the [GameObject](GameObject.html) in the [Hierarchy](UIElements.VisualElement.Hierarchy.html) and
    //clicking the **Add Component** button. Search for [Rigidbody](Rigidbody.html) in the field and select
    //it when shown.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) m_Rigidbody;  
      
        void Start()
        {
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();
            //This locks the RigidBody so that it does not move or rotate in the Z axis.
            m_Rigidbody.constraints = [RigidbodyConstraints.FreezePositionZ](RigidbodyConstraints.FreezePositionZ.html) | [RigidbodyConstraints.FreezeRotationZ](RigidbodyConstraints.FreezeRotationZ.html);
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

