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

#  [GeometryHolder](LowLevelPhysics.GeometryHolder.html).As

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

public T As();

### Returns

**T** Returns the basic geometric shape which is stored in the GeometryHolder.

### Description

Return the specified geometric shape stored inside this Geometry Holder
object.

This function throws an InvalidOperationException if you try to request a
geometric shape that is not stored in the GeometryHolder.  
  
In the case of [CapsuleGeometry](LowLevelPhysics.CapsuleGeometry.html), when
Unity retrieves the shape from a [CapsuleCollider](CapsuleCollider.html)
component, the [CapsuleCollider.direction](CapsuleCollider-direction.html) is
not included. For this reason, you should assume the direction is always along
the X axis.  
  
Additional resources: [BoxGeometry](LowLevelPhysics.BoxGeometry.html),
[SphereGeometry](LowLevelPhysics.SphereGeometry.html),
[CapsuleGeometry](LowLevelPhysics.CapsuleGeometry.html),
[ConvexMeshGeometry](LowLevelPhysics.ConvexMeshGeometry.html),
[TriangleMeshGeometry](LowLevelPhysics.TriangleMeshGeometry.html),
[TerrainGeometry](LowLevelPhysics.TerrainGeometry.html).

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

