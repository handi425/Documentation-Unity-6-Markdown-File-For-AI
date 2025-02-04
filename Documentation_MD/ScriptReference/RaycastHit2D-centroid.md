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

#  [RaycastHit2D](RaycastHit2D.html).centroid

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

public [Vector2](Vector2.html) centroid;

### Description

The world space centroid (center) of the physics query shape when it
intersects.

When the [RaycastHit2D](RaycastHit2D.html) result is returned from a linecast
or raycast query, the `centroid` is identical to the returned
[point](RaycastHit2D-point.html) property because a line or ray uses a very
small point with no area, so its position is the same as the position it
intersects a [Collider2D](Collider2D.html).  
  
However, when using other physics queries that cast shapes that do have an
area such as circles, capsules or boxes, the `centroid` is the center of the
respective shape used when it is in contact with the returned
[point](RaycastHit2D-point.html). For example, a circle will always have its
`centroid` be its radius away from the returned
[point](RaycastHit2D-point.html).  
  
The `centroid` helps identify the position the shape would be at for it to
come into contact at the returned
[RaycastHit2D.point](RaycastHit2D-point.html).  
  
Additional resources: [RaycastHit2D.point](RaycastHit2D-point.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // A stationary planet
        public [Transform](Transform.html) planet;  
      
        // A satellite moving around the planet
        public [Transform](Transform.html) satellite;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Cast a circle with a radius of 10 in from the satellite position to the planet position.
            [RaycastHit2D](RaycastHit2D.html) hit = [Physics2D.CircleCast](Physics2D.CircleCast.html)(satellite.position, 10.0f, planet.position);  
      
            // If something was hit, draw a line from the planet to the position the satellite would be if it were to hit the planet.
            if (hit)
                [Debug.DrawLine](Debug.DrawLine.html)(planet.position, hit.centroid, [Color.yellow](Color-yellow.html));
        }
    }

Additional resources: [RaycastHit2D.point](RaycastHit2D-point.html).

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

