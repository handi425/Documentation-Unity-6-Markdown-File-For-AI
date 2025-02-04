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

# NavMeshLocation

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

**Obsolete** The experimental NavMeshLocation struct has been deprecated
without replacement.

### Description

A world position that is guaranteed to be on the surface of the NavMesh.

The NavMeshLocation stores the position on the NavMesh surface together with
the PolygonId of the NavMesh node containing that position. Using
NavMeshLocations with NavMeshQuery operations remove the need to project the
desired world position onto the NavMesh at the beginning of each and every
operation.  
  
A NavMeshLocation can be invalid in two situations: 1\. When it has been
created empty, instead of being the result of a NavMeshQuery operation. 2\.
When the NavMesh has been removed or modified at the indicated position or in
its close vicinity.  
  
If a NavMeshLocation is made invalid by a
[NavMeshObstacle](AI.NavMeshObstacle.html) carving the NavMesh in its vicinity
the NavMeshLocation returns to a valid state if the
[NavMeshObstacle](AI.NavMeshObstacle.html) is removed. This is because
removing a [NavMeshObstacle](AI.NavMeshObstacle.html) restores the NavMesh to
its original form without regenerating it.  
  
Additional resources: NavMeshQuery.MapLocation, NavMeshQuery.IsValid,
PolygonId.

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

