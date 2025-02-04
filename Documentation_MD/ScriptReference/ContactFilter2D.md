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

# ContactFilter2D

struct in UnityEngine

/

Implemented in:[UnityEngine.Physics2DModule](UnityEngine.Physics2DModule.html)

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

A set of parameters for filtering contact results. Define the angle by
referring to their position in world space, where 0 degrees is parallel to the
positive x-axis, 90 degrees is parallel to the positive y-axis, 180 degrees is
parallel to the negative x-axis, and 270 degrees is parallel to the negative
y-axis.

Use a contact filter to precisely control which contact results get returned.
This removes the need to filter the results later, is faster, and more
convenient.  
  
If you are using a function that requires a
[ContactFilter2D](ContactFilter2D.html), but you don't want to perform any
filtering, then use [ContactFilter2D.NoFilter](ContactFilter2D.NoFilter.html).  
  
For more information on using [ContactFilter2D](ContactFilter2D.html) with
casting, see: [Physics2D.CircleCast](Physics2D.CircleCast.html),
[Physics2D.BoxCast](Physics2D.BoxCast.html),
[Physics2D.CapsuleCast](Physics2D.CapsuleCast.html),
[Physics2D.Linecast](Physics2D.Linecast.html),
[Physics2D.Raycast](Physics2D.Raycast.html),
[Collider2D.Raycast](Collider2D.Raycast.html),
[Collider2D.Cast](Collider2D.Cast.html) and
[Rigidbody2D.Cast](Rigidbody2D.Cast.html).  
  
For more information on using [ContactFilter2D](ContactFilter2D.html) with
overlapping areas, see: [Physics2D.OverlapPoint](Physics2D.OverlapPoint.html),
[Physics2D.OverlapCircle](Physics2D.OverlapCircle.html),
[Physics2D.OverlapBox](Physics2D.OverlapBox.html),
[Physics2D.OverlapArea](Physics2D.OverlapArea.html),
[Physics2D.OverlapCapsule](Physics2D.OverlapCapsule.html),
[Physics2D.OverlapCollider](Physics2D.OverlapCollider.html),
Rigidbody2D.OverlapCollider and Collider2D.OverlapCollider.  
  
For more information on using [ContactFilter2D](ContactFilter2D.html) with
contacts, see: [Physics2D.GetContacts](Physics2D.GetContacts.html),
[Collider2D.GetContacts](Collider2D.GetContacts.html),
[Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html),
[Physics2D.IsTouching](Physics2D.IsTouching.html),
[Rigidbody2D.IsTouching](Rigidbody2D.IsTouching.html) and
[Collider2D.IsTouching](Collider2D.IsTouching.html).

### Properties

[isFiltering](ContactFilter2D-isFiltering.html)| Given the current state of
the contact filter, determine whether it would filter anything.  
---|---  
[layerMask](ContactFilter2D-layerMask.html)| Sets the contact filter to filter
the results that only include Collider2D on the layers defined by the layer
mask.  
[maxDepth](ContactFilter2D-maxDepth.html)| Sets the contact filter to filter
the results to only include Collider2D with a Z coordinate (depth) less than
this value.  
[maxNormalAngle](ContactFilter2D-maxNormalAngle.html)| Sets the contact filter
to filter the results to only include contacts with collision normal angles
that are less than this angle.  
[minDepth](ContactFilter2D-minDepth.html)| Sets the contact filter to filter
the results to only include Collider2D with a Z coordinate (depth) greater
than this value.  
[minNormalAngle](ContactFilter2D-minNormalAngle.html)| Sets the contact filter
to filter the results to only include contacts with collision normal angles
that are greater than this angle.  
[useDepth](ContactFilter2D-useDepth.html)| Sets the contact filter to filter
the results by depth using minDepth and maxDepth.  
[useLayerMask](ContactFilter2D-useLayerMask.html)| Sets the contact filter to
filter results by layer mask.  
[useNormalAngle](ContactFilter2D-useNormalAngle.html)| Sets the contact filter
to filter the results by the collision's normal angle using minNormalAngle and
maxNormalAngle.  
[useOutsideDepth](ContactFilter2D-useOutsideDepth.html)| Sets the contact
filter to filter within the minDepth and maxDepth range, or outside that
range.  
[useOutsideNormalAngle](ContactFilter2D-useOutsideNormalAngle.html)| Sets the
contact filter to filter within the minNormalAngle and maxNormalAngle range,
or outside that range.  
[useTriggers](ContactFilter2D-useTriggers.html)| Sets to filter contact
results based on trigger collider involvement.  
  
### Public Methods

[ClearDepth](ContactFilter2D.ClearDepth.html)| Turns off depth filtering by
setting useDepth to false. The associated values of minDepth and maxDepth are
not changed.  
---|---  
[ClearLayerMask](ContactFilter2D.ClearLayerMask.html)| Turns off layer mask
filtering by setting useLayerMask to false. The associated value of layerMask
is not changed.  
[ClearNormalAngle](ContactFilter2D.ClearNormalAngle.html)| Turns off normal
angle filtering by setting useNormalAngle to false. The associated values of
minNormalAngle and maxNormalAngle are not changed.  
[IsFilteringDepth](ContactFilter2D.IsFilteringDepth.html)| Checks if the
Transform for obj is within the depth range to be filtered.  
[IsFilteringLayerMask](ContactFilter2D.IsFilteringLayerMask.html)| Checks if
the GameObject.layer for obj is included in the layerMask to be filtered.  
[IsFilteringNormalAngle](ContactFilter2D.IsFilteringNormalAngle.html)| Checks
if the angle of normal is within the normal angle range to be filtered.  
[IsFilteringTrigger](ContactFilter2D.IsFilteringTrigger.html)| Checks if the
collider is a trigger and should be filtered by the useTriggers to be
filtered.  
[NoFilter](ContactFilter2D.NoFilter.html)| Sets the contact filter to not
filter any ContactPoint2D.  
[SetDepth](ContactFilter2D.SetDepth.html)| Sets the minDepth and maxDepth
filter properties and turns on depth filtering by setting useDepth to true.  
[SetLayerMask](ContactFilter2D.SetLayerMask.html)| Sets the layerMask filter
property using the layerMask parameter provided and also enables layer mask
filtering by setting useLayerMask to true.  
[SetNormalAngle](ContactFilter2D.SetNormalAngle.html)| Sets the minNormalAngle
and maxNormalAngle filter properties and turns on normal angle filtering by
setting useNormalAngle to true.  
  
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

