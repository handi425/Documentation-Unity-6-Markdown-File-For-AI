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

#  [Physics2D](Physics2D.html).gravity

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

public static [Vector2](Vector2.html) gravity;

### Description

Acceleration due to gravity.

Set this vector to change all 2D gravity in your Scene. The default is (0,
-9.8).

    
    
    //Attach this script to a 2D [GameObject](GameObject.html) (for example a [Sprite](Sprite.html)).
    //Attach a [Rigidbody](Rigidbody.html) component to the [GameObject](GameObject.html) (Click the **Add Component** button and go to **Physics 2D** >**Rigidbody 2D**)  
      
    //This script allows you to change the direction of gravity in your [Scene](SceneManagement.Scene.html) by pressing the space key in Play [Mode](Scripting.GarbageCollector.Mode.html).  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        enum GravityDirection { Down, Left, Up, Right };
        GravityDirection m_GravityDirection;  
      
        void Start()
        {
            m_GravityDirection = GravityDirection.Down;
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            switch (m_GravityDirection)
            {
                case GravityDirection.Down:
                    //Change the gravity to be in a downward direction (default)
                    [Physics2D.gravity](Physics2D-gravity.html) = new [Vector2](Vector2.html)(0, -9.8f);
                    //Press the space key to switch to the left direction
                    if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
                    {
                        m_GravityDirection = GravityDirection.Left;
                        [Debug.Log](Debug.Log.html)("Left");
                    }
                    break;  
      
                case GravityDirection.Left:
                    //Change the gravity to go to the left
                    [Physics2D.gravity](Physics2D-gravity.html) = new [Vector2](Vector2.html)(-9.8f, 0);
                    //Press the space key to change the direction of gravity
                    if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
                    {
                        m_GravityDirection = GravityDirection.Up;
                        [Debug.Log](Debug.Log.html)("Up");
                    }
                    break;  
      
                case GravityDirection.Up:
                    //Change the gravity to be in a upward direction
                    [Physics2D.gravity](Physics2D-gravity.html) = new [Vector2](Vector2.html)(0, 9.8f);
                    //Press the space key to change the direction
                    if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
                    {
                        m_GravityDirection = GravityDirection.Right;
                        [Debug.Log](Debug.Log.html)("Right");
                    }
                    break;  
      
                case GravityDirection.Right:
                    //Change the gravity to go in the right direction
                    [Physics2D.gravity](Physics2D-gravity.html) = new [Vector2](Vector2.html)(9.8f, 0);
                    //Press the space key to change the direction
                    if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
                    {
                        m_GravityDirection = GravityDirection.Down;
                        [Debug.Log](Debug.Log.html)("Down");
                    }  
      
                    break;
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

