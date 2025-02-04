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

#  [QueryTriggerInteraction](QueryTriggerInteraction.html).Ignore

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

Queries never report Trigger hits.

    
    
    //Create two GameObjects (e.g. a Cube) and place them near each other. Attach this script to one of them.
    //Click on the [GameObject](GameObject.html) with the script. Attach the other [GameObject](GameObject.html) to the “My Game Object” field in the Inspector.
    //Make sure both have [Collider](Collider.html) components
    //Choose your own “Max Distance” in the Inspector (e.g. 600).  
      
    //This script casts a ray that ignores Trigger Colliders.
    //Press space to switch the second [GameObject](GameObject.html) between a Trigger and non-Trigger [GameObject](GameObject.html). When the Trigger is off, the ray detects a collision. When it is on, no collisions occur.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //The maximum distance from your [GameObject](GameObject.html). Make sure to set this in the Inspector
        public float m_MaxDistance;
        public [LayerMask](LayerMask.html) m_Mask = -1;  
      
        //Assign a [GameObject](GameObject.html) in the Inspector that you want to test collisions with
        public [GameObject](GameObject.html) m_MyGameObject;
        //This is the [Collider](Collider.html) of the [GameObject](GameObject.html) you assign in the Inspector
        [Collider](Collider.html) m_OtherGameObjectCollider;  
      
        void Start()
        {
            //Fetch the [Collider](Collider.html) from the [GameObject](GameObject.html) you assign in the Inspector
            m_OtherGameObjectCollider = m_MyGameObject.GetComponent<[Collider](Collider.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            //Set the direction as forward
            [Vector3](Vector3.html) direction = transform.TransformDirection([Vector3.forward](Vector3-forward.html));  
      
            //Use [Physics](Physics.html) to calculate the raycast
            //Uses your [GameObject](GameObject.html)'s original position, the direction (above), the max distance from your [GameObject](GameObject.html), and the [LayerMask](LayerMask.html) value to calculate raycast.
            //Also tells it to ignore trigger colliders using [QueryTriggerInteraction](QueryTriggerInteraction.html)
            if ([Physics.Raycast](Physics.Raycast.html)(transform.position, direction, m_MaxDistance, m_Mask.value, [QueryTriggerInteraction.Ignore](QueryTriggerInteraction.Ignore.html)))
                print("There is something in front of the object!");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press space to turn the other [GameObject](GameObject.html)'s trigger status on and off
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //Test if the trigger collisions are ignored by turning the [GameObject](GameObject.html)'s trigger collider on and off
                m_OtherGameObjectCollider.isTrigger = !m_OtherGameObjectCollider.isTrigger;
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

