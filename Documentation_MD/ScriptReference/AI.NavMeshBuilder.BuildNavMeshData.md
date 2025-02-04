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

#  [NavMeshBuilder](AI.NavMeshBuilder.html).BuildNavMeshData

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

public static [AI.NavMeshData](AI.NavMeshData.html)
BuildNavMeshData([AI.NavMeshBuildSettings](AI.NavMeshBuildSettings.html)
buildSettings, List<NavMeshBuildSource> sources, [Bounds](Bounds.html)
localBounds, [Vector3](Vector3.html) position, [Quaternion](Quaternion.html)
rotation);

### Parameters

buildSettings | Settings for the bake process, see [NavMeshBuildSettings](AI.NavMeshBuildSettings.html).  
---|---  
sources | List of input geometry used for baking, they describe the surfaces to walk on or obstacles to avoid.  
localBounds | Bounding box relative to position and rotation which describes the volume where the NavMesh should be built. Empty bounds is treated as no bounds, i.e. the NavMesh will cover all the inputs.  
position | Center of the NavMeshData. This specifies the origin for the NavMesh tiles (Additional resources: [NavMeshBuildSettings.tileSize](AI.NavMeshBuildSettings-tileSize.html)).  
rotation | Orientation of the NavMeshData, you can use this to generate NavMesh with an arbitrary up-vector – e.g. for walkable vertical surfaces.  
  
### Returns

**NavMeshData** Returns a newly built NavMeshData, or null if the NavMeshData
was empty or an error occurred. The newly built NavMeshData, or null if the
NavMeshData was empty or an error occurred.

### Description

Builds a NavMesh data object from the provided input sources.

Note: that
[NavMeshBuilder.BuildNavMeshData](AI.NavMeshBuilder.BuildNavMeshData.html) has
same effect as creating a new empty [NavMeshData](AI.NavMeshData.html) and
calling
[NavMeshBuilder.UpdateNavMeshData](AI.NavMeshBuilder.UpdateNavMeshData.html).

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

