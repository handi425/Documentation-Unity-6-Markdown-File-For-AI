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

#  [Collider](Collider.html).ClosestPoint

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

public [Vector3](Vector3.html) ClosestPoint([Vector3](Vector3.html) position);

### Parameters

position | Location you want to find the closest point to.  
---|---  
  
### Returns

**Vector3** The point on the collider that is closest to the specified
location.

### Description

Returns a point on the collider that is closest to a given location.

This method computes the point on the Collider that is closest to a 3D
location in the world. In the example below `closestPoint` is the point on the
Collider and `location` is the point in 3D space. If `location` is in the
Collider the `closestPoint` is inside. If the Collider is disabled, the method
returns the input `position`.  
  
**Note:** The difference from
[ClosestPointOnBounds](Collider.ClosestPointOnBounds.html) is that the
returned point is actually on the collider instead of on the bounds of the
collider. ([bounds](Collider-bounds.html) is a box that surrounds the
collider.)

    
    
    using UnityEngine;  
      
    // Note that closestPoint is based on the surface of the collider
    // and location represents a point in 3d space.
    // The gizmos work in the editor.
    //
    // Create an origin-based cube and give it a scale of (1, 0.5, 3).
    // Change the [BoxCollider](BoxCollider.html) size to (0.8, 1.2, 0.8).  This means that
    // collisions will happen when a [GameObject](GameObject.html) gets close to the [BoxCollider](BoxCollider.html).
    // The ShowClosestPoint.cs script shows spheres that display the location
    // and closestPoint.  Try changing the [BoxCollider](BoxCollider.html) size and the location
    // values.  
      
    // Attach this to a [GameObject](GameObject.html) that has a [Collider](Collider.html) component attached
    public class ShowClosestPoint : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) location;  
      
        public void OnDrawGizmos()
        {
            var collider = GetComponent<[Collider](Collider.html)>();  
      
            if (!collider)
            {
                return; // nothing to do without a collider
            }  
      
            [Vector3](Vector3.html) closestPoint = collider.ClosestPoint(location);  
      
            [Gizmos.DrawSphere](Gizmos.DrawSphere.html)(location, 0.1f);
            [Gizmos.DrawWireSphere](Gizmos.DrawWireSphere.html)(closestPoint, 0.1f);
        }
    }
    

**Note:** Same as [Physics.ClosestPoint](Physics.ClosestPoint.html) but
doesn't allow passing a custom position and rotation. Instead, it uses the
position of the collider.

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

