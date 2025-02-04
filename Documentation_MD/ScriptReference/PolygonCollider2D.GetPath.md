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

#  [PolygonCollider2D](PolygonCollider2D.html).GetPath

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

public Vector2[] GetPath(int index);

### Parameters

index | The index of the path to retrieve.  
---|---  
  
### Returns

**Vector2[]** An ordered array of the vertices (points) in the selected path.

### Description

Gets a path from the Collider by its index.

A _path_ is a cyclic sequence of line segments between points that define the
outline of the Collider. Because the Collider can have holes and discontinuous
parts, its shape is not necessarily defined by a single path.  
  
Returns an ordered array of the points in the path.  
  
Additional resources: [pathCount](PolygonCollider2D-pathCount.html),
[SetPath](PolygonCollider2D.SetPath.html).

* * *

## Declaration

public int GetPath(int index, List<Vector2> points);

### Parameters

index | The index of the path to retrieve.  
---|---  
points | An ordered list of the vertices (points) in the selected path.  
  
### Returns

**int** Returns the number of results placed in the `points` list.

### Description

Gets a path from the Collider by its index.

A _path_ is a cyclic sequence of line segments between points that define the
outline of the Collider. Because the Collider can have holes and discontinuous
parts, its shape is not necessarily defined by a single path.  
  
Returns an ordered list of the points in the path.  
  
The integer return value is the number of results written into the `points`
list. The points list will be resized if it doesn't contain enough elements to
report all the points.This prevents memory from being allocated for results
when the `points` list does not need to be resized, and improves garbage
collection performance when the query is performed frequently.  
  
Additional resources: [pathCount](PolygonCollider2D-pathCount.html),
[SetPath](PolygonCollider2D.SetPath.html).

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

