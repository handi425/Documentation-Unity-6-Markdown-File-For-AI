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

# Vector3 Constructor

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

## Declaration

public Vector3(float x, float y, float z);

### Description

Creates a new vector with given x, y, z components.

    
    
    //Attach this script to a [GameObject](GameObject.html).
    //Attach a [Rigidbody](Rigidbody.html) component to the [GameObject](GameObject.html) (Click **Add Component** button in the Inspector window and go to **Physics** <**Rigidbody**)
    //This script moves a [GameObject](GameObject.html) upwards using a [Vector3](Vector3.html)
    using UnityEngine;  
      
    public class Vector3CtorExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [Vector3](Vector3.html) myVector;
        [Rigidbody](Rigidbody.html) m_Rigidbody;
        float m_Speed = 2.0f;  
      
        void Start()
        {
            //Set the vector, which you use to move the RigidBody upwards straight away
            myVector = new [Vector3](Vector3.html)(0.0f, 1.0f, 0.0f);
            //Fetch the RigidBody you attach to the [GameObject](GameObject.html)
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Move the RigidBody upwards at the speed you define
            m_Rigidbody.velocity = myVector * m_Speed;
        }
    }
    

* * *

## Declaration

public Vector3(float x, float y);

### Description

Creates a new vector with given x, y components and sets `z` to zero.

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

