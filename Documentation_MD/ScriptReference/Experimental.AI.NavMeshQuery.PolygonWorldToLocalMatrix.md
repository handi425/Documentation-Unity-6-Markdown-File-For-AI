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

**Method group is Obsolete**  

**Experimental** : this API is experimental and might be changed or removed in
the future.

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).PolygonWorldToLocalMatrix

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

**Obsolete** The experimental NavMeshQuery struct has been deprecated without
replacement.

## Declaration

public [Matrix4x4](Matrix4x4.html) PolygonWorldToLocalMatrix(PolygonId
polygon);

### Parameters

polygon | NavMesh node for which its owner's inverse transform must be determined.  
---|---  
  
### Returns

**Matrix4x4** Inverse transformation matrix of the surface owning the
specified polygon.  
[Matrix4x4.identity](Matrix4x4-identity.html) when the NavMesh node is a
[NavMeshLink](../Manual/class-NavMeshLink.html) or an [Off-mesh
Link](../Manual/nav-CreateOffMeshLink.html). Additional resources:
NavMeshQuery.GetPolygonType.

### Description

Returns the inverse transformation matrix of the NavMesh surface that contains
the specified NavMesh node (Read Only).

In contrast to NavMeshQuery.PolygonLocalToWorldMatrix the returned matrix can
be used for transforming a world-coordinates position into the local
coordinate system of the NavMesh surface owning the specified polygon.  
  
**Important:** This method does not return the inverse position and
orientation of a single NavMesh polygon. It returns the inverse position and
orientation of the surface that owns the polygon.  
  
**Known issue:** Identity matrix is returned instead of the actual inverse
transform for NavMeshLinks that have been instantiated with a call to
[NavMesh.AddLink](AI.NavMesh.AddLink.html)(linkData, position, rotation).

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

