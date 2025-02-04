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

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).IsValid

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

public bool IsValid(PolygonId polygon);

### Parameters

polygon | Identifier of the NavMesh node to be checked.  
---|---  
  
### Description

Returns true if the node referenced by the specified PolygonId is active in
the NavMesh.

NavMesh nodes become invalid when the NavMesh surface or the links they belong
are removed or when they have been replaced due to modification of the NavMesh
in their region. The NavMesh surface and links may be removed by calls to
[NavMesh.RemoveNavMeshData](AI.NavMesh.RemoveNavMeshData.html),
[NavMesh.RemoveLink](AI.NavMesh.RemoveLink.html). The NavMesh is modified by
calling
[NavMeshBuilder.UpdateNavMeshData](AI.NavMeshBuilder.UpdateNavMeshData.html)
or carving the NavMesh using a [NavMeshObstacle](../Manual/class-
NavMeshObstacle.html).

* * *

**Obsolete** The experimental NavMeshQuery struct has been deprecated without
replacement.

## Declaration

public bool IsValid(NavMeshLocation location);

### Parameters

location | Location on the NavMesh to be checked. Same as checking `location.polygon` directly.  
---|---  
  
### Description

Returns `true` if the node referenced by the PolygonId contained in the
NavMeshLocation is active in the NavMesh.

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

