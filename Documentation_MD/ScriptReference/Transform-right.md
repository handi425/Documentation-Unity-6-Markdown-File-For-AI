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

#  [Transform](Transform.html).right

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

public [Vector3](Vector3.html) right;

### Description

The red axis of the transform in world space.

Manipulate a GameObject’s position on the X axis (red axis) of the transform
in world space. Unlike [Vector3.right](Vector3-right.html),
[Transform.right](Transform-right.html) moves the GameObject while also
considering its rotation.  
  
When a GameObject is rotated, the red arrow representing the X axis of the
GameObject also changes direction. [Transform.right](Transform-right.html)
moves the GameObject in the red arrow’s axis (X).  
  
For moving the GameObject on the X axis while ignoring rotation, see
[Vector3.right](Vector3-right.html).

    
    
    //Attach this script to a [GameObject](GameObject.html) with a [Rigidbody2D](Rigidbody2D.html) component. Use the left and right arrow keys to see the transform in action.
    //Use the up and down keys to change the rotation, and see how using [Transform.right](Transform-right.html) differs from using [Vector3.right](Vector3-right.html)  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody2D](Rigidbody2D.html) m_Rigidbody;
        float m_Speed;  
      
        void Start()
        {
            //Fetch the [Rigidbody](Rigidbody.html) component you attach from your [GameObject](GameObject.html)
            m_Rigidbody = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();
            //Set the speed of the [GameObject](GameObject.html)
            m_Speed = 10.0f;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.RightArrow](KeyCode.RightArrow.html)))
            {
                //Move the [Rigidbody](Rigidbody.html) to the right constantly at speed you define (the red arrow axis in [Scene](SceneManagement.Scene.html) view)
                m_Rigidbody.velocity = transform.right * m_Speed;
            }  
      
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.LeftArrow](KeyCode.LeftArrow.html)))
            {
                //Move the [Rigidbody](Rigidbody.html) to the left constantly at the speed you define (the red arrow axis in [Scene](SceneManagement.Scene.html) view)
                m_Rigidbody.velocity = -transform.right * m_Speed;
            }  
      
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.UpArrow](KeyCode.UpArrow.html)))
            {
                //rotate the sprite about the Z axis in the positive direction
                transform.Rotate(new [Vector3](Vector3.html)(0, 0, 1) * [Time.deltaTime](Time-deltaTime.html) * m_Speed, [Space.World](Space.World.html));
            }  
      
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.DownArrow](KeyCode.DownArrow.html)))
            {
                //rotate the sprite about the Z axis in the negative direction
                transform.Rotate(new [Vector3](Vector3.html)(0, 0, -1) * [Time.deltaTime](Time-deltaTime.html) * m_Speed, [Space.World](Space.World.html));
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

