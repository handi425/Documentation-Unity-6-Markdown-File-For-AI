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

#  [NavMeshBuilder](AI.NavMeshBuilder.html).UpdateNavMeshData

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

public static bool UpdateNavMeshData([AI.NavMeshData](AI.NavMeshData.html)
data, [AI.NavMeshBuildSettings](AI.NavMeshBuildSettings.html) buildSettings,
List<NavMeshBuildSource> sources, [Bounds](Bounds.html) localBounds);

### Parameters

data | The NavMeshData to update.  
---|---  
buildSettings | The build settings which is used to update the NavMeshData. The build settings is also hashed along with the data, so changing settings will cause a full rebuild.  
sources | List of input geometry used for baking, they describe the surfaces to walk on or obstacles to avoid.  
localBounds | Bounding box relative to position and rotation which describes the volume where the NavMesh should be built.  
  
### Returns

**bool** Returns true if the update was successful.

### Description

Incrementally updates the NavMeshData based on the sources.

Each time NavMeshData is built or updated, the source data is hashed, and the
hashes are stored along with the [NavMeshData](AI.NavMeshData.html).  
  
When called, first the hashes are recomputed and compared and only changed
portions are rebuilt. For this reason, the list of sources should always
contain all the input geometry, even if they haven't moved or changed. If the
list of sources is modified between calls to UpdateNavMeshData the
missing/added sources are considered changes. Try to provide the sources that
have not changed since the last update in the same relative order as before
because their sequence can affect the values of the hashes. This measure
ensures that unchanged portions don't get rebuilt unnecessarily.  
  
You must supply a [Bounds](Bounds-ctor.html) struct for the `localBounds`
parameter.  
  
Additional resources:
[NavMeshBuilder.UpdateNavMeshDataAsync](AI.NavMeshBuilder.UpdateNavMeshDataAsync.html).

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

