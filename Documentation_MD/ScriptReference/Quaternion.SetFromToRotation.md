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

#  [Quaternion](Quaternion.html).SetFromToRotation

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

[Switch to Manual](../Manual/class-Quaternion.html "Go to Quaternion Component
in the Manual")

## Declaration

public void SetFromToRotation([Vector3](Vector3.html) fromDirection,
[Vector3](Vector3.html) toDirection);

### Description

Creates a rotation which rotates from `fromDirection` to `toDirection`.

Use this to create a rotation which starts at the first Vector (fromDirection)
and rotates to the second Vector (toDirection). These Vectors must be set up
in a script.

    
    
    //This example shows how the rotation works between two GameObjects. Attach this to a [GameObject](GameObject.html).
    //Make sure to assign the [GameObject](GameObject.html) you would like your [GameObject](GameObject.html) to rotate towards in the Inspector  
      
    using UnityEngine;  
      
    public class SetFromToRotationExample : [MonoBehaviour](MonoBehaviour.html)
    {
        //This is the [Transform](Transform.html) of the second [GameObject](GameObject.html)
        public [Transform](Transform.html) m_NextPoint;
        [Quaternion](Quaternion.html) m_MyQuaternion;
        float m_Speed = 1.0f;  
      
        void Start()
        {
            m_MyQuaternion = new [Quaternion](Quaternion.html)();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Set the [Quaternion](Quaternion.html) rotation from the [GameObject](GameObject.html)'s position to the next [GameObject](GameObject.html)'s position
            m_MyQuaternion.SetFromToRotation(transform.position, m_NextPoint.position);
            //Move the [GameObject](GameObject.html) towards the second [GameObject](GameObject.html)
            transform.position = [Vector3.Lerp](Vector3.Lerp.html)(transform.position, m_NextPoint.position, m_Speed * [Time.deltaTime](Time-deltaTime.html));
            //[Rotate](UIElements.Rotate.html) the [GameObject](GameObject.html) towards the second [GameObject](GameObject.html)
            transform.rotation = m_MyQuaternion * transform.rotation;
        }
    }
    
    
    
    //In this example your [GameObject](GameObject.html) rotates towards the position of the mouse  
      
    using UnityEngine;  
      
    public class Example2 : [MonoBehaviour](MonoBehaviour.html)
    {
        [Quaternion](Quaternion.html) m_MyQuaternion;
        float m_Speed = 1.0f;
        [Vector3](Vector3.html) m_MousePosition;  
      
        void Start()
        {
            m_MyQuaternion = new [Quaternion](Quaternion.html)();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Fetch the mouse's position
            m_MousePosition = [Input.mousePosition](Input-mousePosition.html);
            //Fix how far into the [Scene](SceneManagement.Scene.html) the mouse should be
            m_MousePosition.z = 50.0f;
            //[Transform](Transform.html) the mouse position into world space
            m_MousePosition = Camera.main.ScreenToWorldPoint(m_MousePosition);  
      
            //Set the [Quaternion](Quaternion.html) rotation from the [GameObject](GameObject.html)'s position to the mouse position
            m_MyQuaternion.SetFromToRotation(transform.position, m_MousePosition);
            //Move the [GameObject](GameObject.html) towards the mouse position
            transform.position = [Vector3.Lerp](Vector3.Lerp.html)(transform.position, m_MousePosition, m_Speed * [Time.deltaTime](Time-deltaTime.html));
            //[Rotate](UIElements.Rotate.html) the [GameObject](GameObject.html) towards the mouse position
            transform.rotation = m_MyQuaternion * transform.rotation;
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

