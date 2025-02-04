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

# Vector2 Constructor

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

public Vector2(float x, float y);

### Description

Constructs a new vector with given x, y components.

    
    
    //This script moves a [GameObject](GameObject.html) to a new x position using a [Vector2](Vector2.html).
    //Attach this script to a [GameObject](GameObject.html)
    //Set your x position in the Inspector  
      
    using UnityEngine;  
      
    public class Examples : [MonoBehaviour](MonoBehaviour.html)
    {
        [Vector2](Vector2.html) m_NewPosition;
        //This is the new X position. Set it in the Inspector.
        public float m_XPosition;  
      
        // Use this for initialization
        void Start()
        {
            //Initialise the vector
            m_NewPosition = new [Vector2](Vector2.html)(0.0f, 0.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the space key to change the x component of the vector
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                m_NewPosition.x = m_XPosition;
            }
            //Change the position depending on the vector
            transform.position = m_NewPosition;
        }
    }
    
    
    
    //This script shows how a [GameObject](GameObject.html) can be moved to new positions using vectors.  
      
    //Attach this script to a [GameObject](GameObject.html). Click on the [GameObject](GameObject.html) and the Inspector window appears. Change the “Second Vector” in the Inspector
    //Attach a [GameObject](GameObject.html) in the MyTransform field
    //Also create 3 UI Buttons (**Create** >**UI** >**Button**) and go to each of their Inspectors to change their OnClick method (click the **+** button)
    //Put your [GameObject](GameObject.html) in each field. Use the **No function** dropdown to assign one [Button](UIElements.Button.html) with the  ZeroButton method, one with PositiveButton method and the other with the GameObjectButton method.  
      
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //Use these to set the [GameObject](GameObject.html)'s position
        [Vector2](Vector2.html) m_MyFirstVector;
        //Set this Vector in the Inspector (the position you would like the [GameObject](GameObject.html) to move to)
        public [Vector2](Vector2.html) m_MySecondVector;
        [Vector2](Vector2.html) m_MyThirdVector;  
      
        //You must assign to this [Transform](Transform.html) in the Inspector (could be another [GameObject](GameObject.html))
        public [Transform](Transform.html) m_MyTransform;  
      
        void Start()
        {
            //Set the first vector to be at (0, 0, 0)
            m_MyFirstVector = [Vector2.zero](Vector2-zero.html);
            //Set the third vector to the [GameObject](GameObject.html) you set in the Inspector's position
            m_MyThirdVector = m_MyTransform.position;
        }  
      
        public void ZeroButton()
        {
            //Press this [Button](UIElements.Button.html) to move your [GameObject](GameObject.html) to the first vector position (0, 0)
            //Use this to move your [GameObject](GameObject.html) to the origin (be wary of parent GameObjects)
            transform.position = m_MyFirstVector;
        }  
      
        //Press this [Button](UIElements.Button.html) to move your [GameObject](GameObject.html) to the second vector position (100, 200)
        public void PositionButton()
        {
            //Use this to move your [GameObject](GameObject.html) to a specified position
            transform.position = m_MySecondVector;
        }  
      
        //Press this [Button](UIElements.Button.html) to move your [GameObject](GameObject.html) to the third vector position (The m_MyTransform's position)
        public void GameObjectButton()
        {
            //Use this to move your [GameObject](GameObject.html) to another [GameObject](GameObject.html)'s position
            transform.position = m_MyThirdVector;
        }
    }
    

A script that converts degrees into radians. The radians are used to rotate
around the origin.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class ExampleScene : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            float degrees = 45.0f;
            float radians = degrees * [Mathf.Deg2Rad](Mathf.Deg2Rad.html);  
      
            [Vector2](Vector2.html) vec2 = new [Vector2](Vector2.html)([Mathf.Cos](Mathf.Cos.html)(radians), [Mathf.Sin](Mathf.Sin.html)(radians));
            [Debug.Log](Debug.Log.html)(vec2);
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

