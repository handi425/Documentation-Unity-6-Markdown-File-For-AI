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

# NavMeshQuery

struct in UnityEngine.Experimental.AI

/

Implemented in:[UnityEngine.AIModule](UnityEngine.AIModule.html)

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

### Description

Object used for doing navigation operations in a NavMeshWorld.

NavMeshQuery operations can be executed inside jobs
([IJob](Unity.Jobs.IJob.html),
[IJobParallelFor](Unity.Jobs.IJobParallelFor.html)), as opposed to the
operations in the [NavMesh](AI.NavMesh.html)-related structures.  
  
To obtain a path between two locations on the NavMesh, you must create a
NavMeshQuery with a `pathNodePoolSize` value in the range from 1 to 65,535.
After creating a NavMeshQuery, you must call the following methods in this
order: `BeginFindPath`, `UpdateFindPath` (can be repeated), `EndFindPath`,
`GetPathResult`. These methods store state data within the NavMeshQuery. Other
methods can be called in any order since they do not change state data.  
  
All methods throw exceptions if any of their parameters are not valid when
executed in the Editor.  
  
**Note:** The intended feature set for NavMeshQuery is not yet fully complete.

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

