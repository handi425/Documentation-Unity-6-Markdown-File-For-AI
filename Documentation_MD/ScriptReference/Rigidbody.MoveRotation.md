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

#  [Rigidbody](Rigidbody.html).MoveRotation

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

public void MoveRotation([Quaternion](Quaternion.html) rot);

### Parameters

rot | The new rotation for the Rigidbody.  
---|---  
  
### Description

Rotates the rigidbody to `rotation`.

Use [Rigidbody.MoveRotation](Rigidbody.MoveRotation.html) to rotate a
[Rigidbody](Rigidbody.html), complying with the Rigidbody's interpolation
setting.  
  
If Rigidbody interpolation is enabled on the [Rigidbody](Rigidbody.html),
calling [Rigidbody.MoveRotation](Rigidbody.MoveRotation.html) will resulting
in a smooth transition between the two rotations in any intermediate frames
rendered. This should be used if you want to continuously rotate a rigidbody
in each [FixedUpdate](PlayerLoop.FixedUpdate.html).  
  
Set [Rigidbody.rotation](Rigidbody-rotation.html) instead, if you want to
teleport a rigidbody from one rotation to another, with no intermediate
positions being rendered.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) m_Rigidbody;
        [Vector3](Vector3.html) m_EulerAngleVelocity;  
      
        void Start()
        {
            //Fetch the [Rigidbody](Rigidbody.html) from the [GameObject](GameObject.html) with this script attached
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();  
      
            //Set the angular velocity of the [Rigidbody](Rigidbody.html) (rotating around the Y axis, 100 deg/sec)
            m_EulerAngleVelocity = new [Vector3](Vector3.html)(0, 100, 0);
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            [Quaternion](Quaternion.html) deltaRotation = [Quaternion.Euler](Quaternion.Euler.html)(m_EulerAngleVelocity * [Time.fixedDeltaTime](Time-fixedDeltaTime.html));
            m_Rigidbody.MoveRotation(m_Rigidbody.rotation * deltaRotation);
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

