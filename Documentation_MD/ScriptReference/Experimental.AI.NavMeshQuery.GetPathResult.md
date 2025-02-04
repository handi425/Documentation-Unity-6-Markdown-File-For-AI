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

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).GetPathResult

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

public int GetPathResult(NativeSlice<PolygonId> path);

### Parameters

path | Data array to be filled with the sequence of NavMesh nodes that comprises the found path.  
---|---  
  
### Returns

**int** Number of path nodes successfully copied into the provided array.

### Description

Copies into the provided array the list of NavMesh nodes that form the path
found by the NavMeshQuery operation.

Must be called at the end of a successful NavMeshQuery.BeginFindPath -
NavMeshQuery.UpdateFindPath - NavMeshQuery.EndFindPath sequence in order to
obtain the resulting path.  
  
Can be called multiple times as long as NavMeshQuery.BeginFindPath has not
been called for that same query.  
  
If the resulting path, stored in the query, is longer than the length of the
provided array, the nodes are still copied (from the beginning of the path up
to the array's length).  
  
**Important:** If the start NavMesh node of the path has been removed by a
NavMesh modification since the initial `BeginFindPath` call of the pathfinding
operation, the returned path will be empty.

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

