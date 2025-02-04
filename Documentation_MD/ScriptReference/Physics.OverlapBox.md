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

#  [Physics](Physics.html).OverlapBox

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

public static Collider[] OverlapBox([Vector3](Vector3.html) center,
[Vector3](Vector3.html) halfExtents, [Quaternion](Quaternion.html) orientation
= Quaternion.identity, int layerMask = AllLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

center | Center of the box.  
---|---  
halfExtents | Half of the size of the box in each dimension.  
orientation | Rotation of the box.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**Collider[]** Colliders that overlap with the given box.

### Description

Find all colliders touching or inside of the given box.

Creates an invisible box you define that tests collisions by outputting any
colliders that come into contact with the box.

    
    
    //Attach this script to your [GameObject](GameObject.html). This [GameObject](GameObject.html) doesn’t need to have a [Collider](Collider.html) component
    //Set the [Layer](Experimental.GraphView.GraphView.Layer.html) Mask field in the Inspector to the layer you would like to see collisions in (set to **Everything** if you are unsure).
    //Create a second Gameobject for testing collisions. Make sure your [GameObject](GameObject.html) has a [Collider](Collider.html) component (if it doesn’t, click on the **Add Component** button in the [GameObject](GameObject.html)’s Inspector, and go to **Physics** >**Box Collider**).
    //Place it so it is overlapping your other [GameObject](GameObject.html).
    //Press Play to see the console output the name of your second [GameObject](GameObject.html)  
      
    //This script uses the OverlapBox that creates an invisible [Box](UIElements.Box.html) [Collider](Collider.html) that detects multiple collisions with other colliders. The OverlapBox in this case is the same size and position as the [GameObject](GameObject.html) you attach it to (acting as a replacement for the [BoxCollider](BoxCollider.html) component).  
      
    using UnityEngine;  
      
    public class OverlapBoxExample : [MonoBehaviour](MonoBehaviour.html)
    {
        bool m_Started;
        public [LayerMask](LayerMask.html) m_LayerMask;  
      
        void Start()
        {
            //Use this to ensure that the [Gizmos](Gizmos.html) are being drawn when in Play [Mode](Scripting.GarbageCollector.Mode.html).
            m_Started = true;
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            MyCollisions();
        }  
      
        void MyCollisions()
        {
            //Use the OverlapBox to detect if there are any other colliders within this box area.
            //Use the [GameObject](GameObject.html)'s centre, half the size (as a radius) and rotation. This creates an invisible box around your [GameObject](GameObject.html).
            [Collider](Collider.html)[] hitColliders = [Physics.OverlapBox](Physics.OverlapBox.html)(gameObject.transform.position, transform.localScale / 2, [Quaternion.identity](Quaternion-identity.html), m_LayerMask);
            int i = 0;
            //Check when there is a new collider coming into contact with the box
            while (i < hitColliders.Length)
            {
                //Output all of the collider names
                [Debug.Log](Debug.Log.html)("Hit : " + hitColliders[i].name + i);
                //Increase the number of Colliders in the array
                i++;
            }
        }  
      
        //Draw the [Box](UIElements.Box.html) Overlap as a gizmo to show where it currently is testing. Click the [Gizmos](Gizmos.html) button to see this
        void OnDrawGizmos()
        {
            [Gizmos.color](Gizmos-color.html) = [Color.red](Color-red.html);
            //Check that it is being run in Play [Mode](Scripting.GarbageCollector.Mode.html), so it doesn't try to draw this in [Editor](Editor.html) mode
            if (m_Started)
                //Draw a cube where the OverlapBox is (positioned where your [GameObject](GameObject.html) is as well as a size)
                [Gizmos.DrawWireCube](Gizmos.DrawWireCube.html)(transform.position, transform.localScale);
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

