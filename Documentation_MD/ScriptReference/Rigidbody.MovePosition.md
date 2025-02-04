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

#  [Rigidbody](Rigidbody.html).MovePosition

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

public void MovePosition([Vector3](Vector3.html) position);

### Parameters

position | Provides the new position for the [Rigidbody](Rigidbody.html) object.  
---|---  
  
### Description

Moves the kinematic [Rigidbody](Rigidbody.html) towards `position`.

[Rigidbody.MovePosition](Rigidbody.MovePosition.html) moves a Rigidbody and
complies with the interpolation settings. When Rigidbody interpolation is
enabled, [Rigidbody.MovePosition](Rigidbody.MovePosition.html) creates a
smooth transition between frames. Unity moves a [Rigidbody](Rigidbody.html) in
each `FixedUpdate` call. The `position` occurs in world space. To teleport a
[Rigidbody](Rigidbody.html) from one position to another, use
[Rigidbody.position](Rigidbody-position.html) instead of
[MovePosition](Rigidbody.MovePosition.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) m_Rigidbody;
        public float m_Speed = 5f;  
      
        void Start()
        {
            //Fetch the [Rigidbody](Rigidbody.html) from the [GameObject](GameObject.html) with this script attached
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            //Store user input as a movement vector
            [Vector3](Vector3.html) m_Input = new [Vector3](Vector3.html)([Input.GetAxis](Input.GetAxis.html)("Horizontal"), 0, [Input.GetAxis](Input.GetAxis.html)("Vertical"));  
      
            //Apply the movement vector to the current position, which is
            //multiplied by deltaTime and speed for a smooth MovePosition
            m_Rigidbody.MovePosition(transform.position + m_Input * [Time.fixedDeltaTime](Time-fixedDeltaTime.html) * m_Speed);
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

