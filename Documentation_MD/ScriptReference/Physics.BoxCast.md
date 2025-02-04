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

#  [Physics](Physics.html).BoxCast

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

public static bool BoxCast([Vector3](Vector3.html) center,
[Vector3](Vector3.html) halfExtents, [Vector3](Vector3.html) direction,
[Quaternion](Quaternion.html) orientation = Quaternion.identity, float
maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

center | Center of the box.  
---|---  
halfExtents | Half the size of the box in each dimension.  
direction | The direction in which to cast the box.  
orientation | Rotation of the box.  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**bool** True, if any intersections were found.

### Description

Casts the box along a ray and returns detailed information on what was hit.

* * *

## Declaration

public static bool BoxCast([Vector3](Vector3.html) center,
[Vector3](Vector3.html) halfExtents, [Vector3](Vector3.html) direction, out
[RaycastHit](RaycastHit.html) hitInfo, [Quaternion](Quaternion.html)
orientation = Quaternion.identity, float maxDistance = Mathf.Infinity, int
layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

center | Center of the box.  
---|---  
halfExtents | Half the size of the box in each dimension.  
direction | The direction in which to cast the box.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](RaycastHit.html)).  
orientation | Rotation of the box.  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**bool** True, if any intersections were found.

### Description

Casts the box along a ray and returns detailed information on what was hit.

    
    
    //Attach this script to a [GameObject](GameObject.html). Make sure it has a [Collider](Collider.html) component by clicking the **Add Component** button. Then click **Physics** >**Box Collider** to attach a [Box](UIElements.Box.html) [Collider](Collider.html) component.
    //This script creates a BoxCast in front of the [GameObject](GameObject.html) and outputs a message if another [Collider](Collider.html) is hit with the [Collider](Collider.html)’s name.
    //It also draws where the ray and BoxCast extends to. Just press the [Gizmos](Gizmos.html) button to see it in Play [Mode](Scripting.GarbageCollector.Mode.html).
    //Make sure to have another [GameObject](GameObject.html) with a [Collider](Collider.html) component for the BoxCast to collide with.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        float m_MaxDistance;
        float m_Speed;
        bool m_HitDetect;  
      
        [Collider](Collider.html) m_Collider;
        [RaycastHit](RaycastHit.html) m_Hit;  
      
        void Start()
        {
            //Choose the distance the [Box](UIElements.Box.html) can reach to
            m_MaxDistance = 300.0f;
            m_Speed = 20.0f;
            m_Collider = GetComponent<[Collider](Collider.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Simple movement in x and z axes
            float xAxis = [Input.GetAxis](Input.GetAxis.html)("Horizontal") * m_Speed;
            float zAxis = [Input.GetAxis](Input.GetAxis.html)("Vertical") * m_Speed;
            transform.Translate(new [Vector3](Vector3.html)(xAxis, 0, zAxis));
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            //Test to see if there is a hit using a BoxCast
            //Calculate using the center of the [GameObject](GameObject.html)'s [Collider](Collider.html)(could also just use the [GameObject](GameObject.html)'s position), half the [GameObject](GameObject.html)'s size, the direction, the [GameObject](GameObject.html)'s rotation, and the maximum distance as variables.
            //Also fetch the hit data
            m_HitDetect = [Physics.BoxCast](Physics.BoxCast.html)(m_Collider.bounds.center, transform.localScale*0.5f, transform.forward, out m_Hit, transform.rotation, m_MaxDistance);
            if (m_HitDetect)
            {
                //Output the name of the [Collider](Collider.html) your [Box](UIElements.Box.html) hit
                [Debug.Log](Debug.Log.html)("Hit : " + m_Hit.collider.name);
            }
        }  
      
        //Draw the BoxCast as a gizmo to show where it currently is testing. Click the [Gizmos](Gizmos.html) button to see this
        void OnDrawGizmos()
        {
            [Gizmos.color](Gizmos-color.html) = [Color.red](Color-red.html);  
      
            //Check if there has been a hit yet
            if (m_HitDetect)
            {
                //Draw a [Ray](Ray.html) forward from [GameObject](GameObject.html) toward the hit
                [Gizmos.DrawRay](Gizmos.DrawRay.html)(transform.position, transform.forward * m_Hit.distance);
                //Draw a cube that extends to where the hit exists
                [Gizmos.DrawWireCube](Gizmos.DrawWireCube.html)(transform.position + transform.forward * m_Hit.distance, transform.localScale);
            }
            //If there hasn't been a hit yet, draw the ray at the maximum distance
            else
            {
                //Draw a [Ray](Ray.html) forward from [GameObject](GameObject.html) toward the maximum distance
                [Gizmos.DrawRay](Gizmos.DrawRay.html)(transform.position, transform.forward * m_MaxDistance);
                //Draw a cube at the maximum distance
                [Gizmos.DrawWireCube](Gizmos.DrawWireCube.html)(transform.position + transform.forward * m_MaxDistance, transform.localScale);
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

