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

#  [CollisionDetectionMode](CollisionDetectionMode.html).ContinuousSpeculative

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

Speculative continuous collision detection is on for static and dynamic
geometries

This is a collision detection mode that can be used on both dyanmic and
kinematic objects. It is generally cheaper than other CCD mode. It also
handles angular motion much better. However, in some cases, high speed objects
may still tunneling through other geometries.

    
    
    //This script allows you to switch collision detection mode at the press of the space key, and move your [GameObject](GameObject.html). It also outputs collisions that occur to the console.
    //Attach this script to a [GameObject](GameObject.html) and make sure it has a [Rigidbody](Rigidbody.html) component
    //If it doesn't have a [Rigidbody](Rigidbody.html) component, click the [GameObject](GameObject.html), go to its Inspector and click the **Add Component** button. Then, go to **Physics** >**Rigidbody**.
    //Create another [GameObject](GameObject.html). Make sure it has a [Collider](Collider.html), so you can test collisions between them.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) m_Rigidbody;  
      
        void Start()
        {
            //Attach this script to a [GameObject](GameObject.html). Ensure that it has a [Rigidbody](Rigidbody.html) component.
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the space key to switch the collision detection mode
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
                SwitchCollisionDetectionMode();
        }  
      
        //[Switch](PlayerSettings.Switch.html) between the different [Collision](Collision.html) Detection Modes
        void SwitchCollisionDetectionMode()
        {
            switch (m_Rigidbody.collisionDetectionMode)
            {
                //If the current mode is continuous, switch it to continuous dynamic mode
                case [CollisionDetectionMode.Continuous](CollisionDetectionMode.Continuous.html):
                    m_Rigidbody.collisionDetectionMode = [CollisionDetectionMode.ContinuousDynamic](CollisionDetectionMode.ContinuousDynamic.html);
                    break;
                //If the current mode is continuous dynamic, switch it to continuous speculative
                case [CollisionDetectionMode.ContinuousDynamic](CollisionDetectionMode.ContinuousDynamic.html):
                    m_Rigidbody.collisionDetectionMode = [CollisionDetectionMode.ContinuousSpeculative](CollisionDetectionMode.ContinuousSpeculative.html);
                    break;  
      
                // If the curren mode is continuous speculative, switch it to discrete mode
                case [CollisionDetectionMode.ContinuousSpeculative](CollisionDetectionMode.ContinuousSpeculative.html):
                    m_Rigidbody.collisionDetectionMode = [CollisionDetectionMode.Discrete](CollisionDetectionMode.Discrete.html);
                    break;  
      
                //If the current mode is discrete, switch it to continuous mode
                case [CollisionDetectionMode.Discrete](CollisionDetectionMode.Discrete.html):
                    m_Rigidbody.collisionDetectionMode = [CollisionDetectionMode.Continuous](CollisionDetectionMode.Continuous.html);
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

