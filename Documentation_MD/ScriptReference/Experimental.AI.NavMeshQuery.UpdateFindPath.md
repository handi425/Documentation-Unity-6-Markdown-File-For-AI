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

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).UpdateFindPath

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

public PathQueryStatus UpdateFindPath(int iterations, out int
iterationsPerformed);

### Parameters

iterations | Maximum number of nodes to be traversed by the search algorithm during this call.  
---|---  
iterationsPerformed | Outputs the actual number of nodes that have been traversed during this call.  
  
### Returns

**PathQueryStatus** `InProgress` if the search needs to continue further by
calling `UpdateFindPath` again.  
`Success` if the search is completed and a path has been found or not.  
`Failure` if the search for the desired position could not be completed
because the NavMesh has changed significantly since the search was initiated.  
Additionally the returned value can contain the `OutOfNodes` flag when the
`pathNodePoolSize` parameter for the NavMeshQuery initialization was not large
enough to accommodate the search space.

### Description

Continues a path search that is in progress.

The operation needs to have been initialized previously with
NavMeshQuery.BeginFindPath and it will run until the entire route is found or
the specified number of iterations have been executed.  
  
As long as the previous call returned a state of `InProgress` this method can
be called repeatedly, across different frames, until the operation is
successful. Use NavMeshQuery.EndFindPath afterwards to prepare the path data
for retrieval, along with the number of contained nodes.  
  
Additional resources: PathQueryStatus.

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

