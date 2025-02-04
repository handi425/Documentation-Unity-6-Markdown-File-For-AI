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

#  [RigidbodyConstraints](RigidbodyConstraints.html).FreezeRotation

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

[ ]()

### Description

Freeze rotation along all axes.

    
    
    //Attach this script to a [GameObject](GameObject.html) with a [Rigidbody](Rigidbody.html). Press the up and down keys to move the [Rigidbody](Rigidbody.html) up and down.
    //Press the space key to freeze all rotations, but notice the positions still change.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) m_Rigidbody;
        [Vector3](Vector3.html) m_YAxis;
        float m_Speed;  
      
        void Start()
        {
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();
            //Set up vector for moving the [Rigidbody](Rigidbody.html) in the y axis
            m_YAxis = new [Vector3](Vector3.html)(0, 5, 0);
            m_Speed = 20.0f;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press space to add constraints on the RigidBody (freeze all rotations)
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //Freeze all rotations
                m_Rigidbody.constraints = [RigidbodyConstraints.FreezeRotation](RigidbodyConstraints.FreezeRotation.html);
            }  
      
            //Press the up arrow key to move positively in the y axis
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.UpArrow](KeyCode.UpArrow.html)))
            {
                //The [Rigidbody](Rigidbody.html) moves along the y axis
                m_Rigidbody.velocity = m_YAxis;
            }  
      
            //Press the down arrow key to move negatively in the y axis
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.DownArrow](KeyCode.DownArrow.html)))
            {
                m_Rigidbody.velocity = -m_YAxis;
            }  
      
            //Press the A key to rotate the [GameObject](GameObject.html) (if there are no rotation constraints)
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.A](KeyCode.A.html)))
            {
                m_Rigidbody.angularVelocity = [Vector3.right](Vector3-right.html) * m_Speed * [Time.deltaTime](Time-deltaTime.html);
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

