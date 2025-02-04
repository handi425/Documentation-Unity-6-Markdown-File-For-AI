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

#  [RigidbodyConstraints](RigidbodyConstraints.html).FreezePositionX

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

Freeze motion along the X-axis.

    
    
    //This example shows how [RigidbodyConstraints](RigidbodyConstraints.html) is used to freeze the position and rotation of a [Rigidbody](Rigidbody.html) in the x axis at start-up.
    //It also shows what happens when these constraints are removed, when you press the space key
    //Attach this to a [GameObject](GameObject.html) with a [Rigidbody](Rigidbody.html) to see it in action  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) m_Rigidbody;
        [Vector3](Vector3.html) m_XAxis;  
      
        void Start()
        {
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();
            //This locks the RigidBody so that it does not move or rotate in the x axis (can be seen in Inspector).
            m_Rigidbody.constraints = [RigidbodyConstraints.FreezePositionX](RigidbodyConstraints.FreezePositionX.html) | [RigidbodyConstraints.FreezeRotationX](RigidbodyConstraints.FreezeRotationX.html);
            //Set up vector for moving the [Rigidbody](Rigidbody.html) in the x axis
            m_XAxis = new [Vector3](Vector3.html)(5, 0, 0);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press space to remove the constraints on the RigidBody
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //Remove all constraints
                m_Rigidbody.constraints = [RigidbodyConstraints.None](RigidbodyConstraints.None.html);
            }  
      
            //Press the right arrow key to move positively in the x axis if the constraints are removed
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.RightArrow](KeyCode.RightArrow.html)))
            {
                //If the constraints are removed, the [Rigidbody](Rigidbody.html) moves along the x axis
                //If the constraints are there, no movement occurs
                m_Rigidbody.velocity = m_XAxis;
            }  
      
            //Press the left arrow key to move negatively in the x axis if the constraints are removed
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.LeftArrow](KeyCode.LeftArrow.html)))
            {
                m_Rigidbody.velocity = -m_XAxis;
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

