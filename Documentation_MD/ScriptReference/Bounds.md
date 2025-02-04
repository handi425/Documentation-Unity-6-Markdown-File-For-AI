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

# Bounds

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Represents an axis aligned bounding box.

An axis-aligned bounding box, or AABB for short, is a box aligned with
coordinate axes and fully enclosing some object. Because the box is never
rotated with respect to the axes, it can be defined by just its
[center](Bounds-center.html) and [extents](Bounds-extents.html), or
alternatively by [min](Bounds-min.html) and [max](Bounds-max.html) points.  
  
`Bounds` is used by [Collider.bounds](Collider-bounds.html),
[Mesh.bounds](Mesh-bounds.html) and [Renderer.bounds](Renderer-bounds.html).

### Properties

[center](Bounds-center.html)| The center of the bounding box.  
---|---  
[extents](Bounds-extents.html)| The extents of the Bounding Box. This is
always half of the size of the Bounds.  
[max](Bounds-max.html)| The maximal point of the box. This is always equal to
center+extents.  
[min](Bounds-min.html)| The minimal point of the box. This is always equal to
center-extents.  
[size](Bounds-size.html)| The total size of the box. This is always twice as
large as the extents.  
  
### Constructors

[Bounds](Bounds-ctor.html)| Creates a new Bounds.  
---|---  
  
### Public Methods

[ClosestPoint](Bounds.ClosestPoint.html)| The closest point on the bounding
box.  
---|---  
[Contains](Bounds.Contains.html)| Is point contained in the bounding box?  
[Encapsulate](Bounds.Encapsulate.html)| Grows the Bounds to include the point.  
[Expand](Bounds.Expand.html)| Expand the bounds by increasing its size by
amount along each side.  
[IntersectRay](Bounds.IntersectRay.html)| Does ray intersect this bounding
box?  
[Intersects](Bounds.Intersects.html)| Does another bounding box intersect with
this bounding box?  
[SetMinMax](Bounds.SetMinMax.html)| Sets the bounds to the min and max value
of the box.  
[SqrDistance](Bounds.SqrDistance.html)| The smallest squared distance between
the point and this bounding box.  
[ToString](Bounds.ToString.html)| Returns a formatted string for the bounds.  
  
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

