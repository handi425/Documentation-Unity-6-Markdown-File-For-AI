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

#  [RaycastHit2D](RaycastHit2D.html).normal

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

public [Vector2](Vector2.html) normal;

### Description

The surface normal of the detected [Collider2D](Collider2D.html).

When the physics query detects an intersection of a
[Collider2D](Collider2D.html) at a specific
[RaycastHit2D.point](RaycastHit2D-point.html) the `normal` is the surface
normal of the [Collider2D](Collider2D.html) at that position. A surface normal
is a vector perpendicular to the collider surface edge in a direction pointing
away from the collider.  
  
Additional resources: [RaycastHit2D.point](RaycastHit2D-point.html).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector2](Vector2.html) direction;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Cast a ray in the direction specified in the inspector.
            [RaycastHit2D](RaycastHit2D.html) hit = [Physics2D.Raycast](Physics2D.Raycast.html)(transform.position, direction);  
      
            // If something was hit, draw a line from the hit position in the direction of the surface normal.
            if (hit)
                [Debug.DrawLine](Debug.DrawLine.html)(hit.point, hit.point + hit.normal, [Color.yellow](Color-yellow.html));
        }
    }

**Note:** If a hit starts occuring inside a collider, the collision normal is
the opposite direction of the line/ray query.

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

