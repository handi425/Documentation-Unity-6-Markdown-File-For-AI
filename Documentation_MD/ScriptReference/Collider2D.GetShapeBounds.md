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

#  [Collider2D](Collider2D.html).GetShapeBounds

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

public [Bounds](Bounds.html) GetShapeBounds(List<Bounds> bounds, bool
useRadii, bool useWorldSpace);

### Parameters

bounds | The list used to store the returned [Bounds](Bounds.html).  
---|---  
useRadii | Whether the radius of each [PhysicsShape2D](PhysicsShape2D.html) should be used to calculate the [Bounds](Bounds.html) or not.  
useWorldSpace | Whether to transform all the returned [Bounds](Bounds.html) to world space or leave them in their default local space.  
  
### Returns

**Bounds** Returns the combined [Bounds](Bounds.html) of the retrieved list.

### Description

Retrieves a list of [Bounds](Bounds.html) for all
[PhysicsShape2D](PhysicsShape2D.html) created by this
[Collider2D](Collider2D.html), and returns the combined [Bounds](Bounds.html)
of the retrieved list.

Additional resources: [Bounds](Bounds.html),
[Collider2D.GetShapes](Collider2D.GetShapes.html) and
[Collider2D.GetShapeHash](Collider2D.GetShapeHash.html).

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

