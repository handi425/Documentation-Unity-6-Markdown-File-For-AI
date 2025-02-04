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

#  [Physics](Physics.html).IgnoreLayerCollision

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

public static void IgnoreLayerCollision(int layer1, int layer2, bool ignore =
true);

### Description

Makes the collision detection system ignore all collisions between any
collider in `layer1` and any collider in `layer2`.  
  
Note that IgnoreLayerCollision will reset the trigger state of affected
colliders, so you might receive OnTriggerExit and OnTriggerEnter messages in
response to calling this.

You can set the default values for your project for any layer combinations in
the Physics inspector.  
  
Additional resources:
[Physics.GetIgnoreLayerCollision](Physics.GetIgnoreLayerCollision.html),[Physics.IgnoreCollision](Physics.IgnoreCollision.html).

    
    
    //Attach this script to a [GameObject](GameObject.html) and make sure it has a [Rigidbody](Rigidbody.html) component
    //Make a second [GameObject](GameObject.html) with a [Collider](Collider.html) to test collisions on. Make sure both GameObjects are the same on the y and z axes  
      
    //This script stops collisions between two layers (in this case layers 0 and 8). Set up a new layer in the Inspector window by clicking the [Layer](Experimental.GraphView.GraphView.Layer.html) option.
    //Next click “Add [Layer](Experimental.GraphView.GraphView.Layer.html)”. Then, assign this layer to the second [GameObject](GameObject.html).  
      
    //In Play [Mode](Scripting.GarbageCollector.Mode.html), press the left and right keys to move the [Rigidbody](Rigidbody.html) to the left and right. If your first [GameObject](GameObject.html) is in layer 0 and your second [GameObject](GameObject.html) is in layer 8, the collision is ignored.  
      
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //Set the speed number in the Inspector window
        public float m_Speed;
        [Rigidbody](Rigidbody.html) m_Rigidbody;  
      
        void Start()
        {
            //Fetch the [Rigidbody](Rigidbody.html) component from the [GameObject](GameObject.html)
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();
            //Ignore the collisions between layer 0 (default) and layer 8 (custom layer you set in Inspector window)
            [Physics.IgnoreLayerCollision](Physics.IgnoreLayerCollision.html)(0, 8);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press right to move the [GameObject](GameObject.html) to the right. Make sure you set the speed high in the Inspector window.
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.RightArrow](KeyCode.RightArrow.html)))
            {
                m_Rigidbody.AddForce([Vector3.right](Vector3-right.html) * m_Speed);
            }  
      
            //Press the left arrow key to move the [GameObject](GameObject.html) to the left
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.LeftArrow](KeyCode.LeftArrow.html)))
            {
                m_Rigidbody.AddForce([Vector3.left](Vector3-left.html) * m_Speed);
            }
        }  
      
        //Detect when there is a collision
        void OnCollisionStay([Collision](Collision.html) collide)
        {
            //Output the name of the [GameObject](GameObject.html) you collide with
            [Debug.Log](Debug.Log.html)("I hit the [GameObject](GameObject.html) : " + collide.gameObject.name);
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

