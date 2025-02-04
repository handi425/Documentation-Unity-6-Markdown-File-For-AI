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

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).MapLocation

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

public NavMeshLocation MapLocation([Vector3](Vector3.html) position,
[Vector3](Vector3.html) extents, int agentTypeID, int areaMask);

### Parameters

position | World position for which the closest point on the NavMesh needs to be found.  
---|---  
extents | Maximum distance, from the specified `position`, expanding along all three axes, within which NavMesh surfaces are searched.  
agentTypeID | Identifier for the agent type whose NavMesh surfaces should be selected for this operation. The _Humanoid_ agent type exists for all NavMeshes and has an ID of 0. Other agent types can be defined manually through the Editor. A separate NavMesh surface needs to be baked for each agent type.  
areaMask | Bitmask used to represent areas of the NavMesh that should (value of 1) or shouldn't (values of 0) be sampled. This parameter is optional and defaults to [NavMesh.AllAreas](AI.NavMesh.AllAreas.html) if unspecified. Additional resources: [Areas and Costs](../Manual/nav-AreasAndCosts.html).  
  
### Returns

**NavMeshLocation** An object with position and valid PolygonId - when a point
on the NavMesh has been found.  
An invalid object - when no NavMesh surface with the desired features has been
found within the search area. Additional resources: NavMeshQuery.IsValid.

### Description

Finds the closest point and PolygonId on the NavMesh for a given world
position.

The search only applies to the specified type of NavMesh surface, for one or
more desired area types and is limited to within the specified search area. It
does not search for positions on [NavMeshLinks](../Manual/class-
NavMeshLink.html) or [Off-mesh Links](../Manual/nav-CreateOffMeshLink.html).  
  
Nearby NavMesh surfaces directly above or below the specified position are
preferred. When there are none up or down within the specified search extents
the surfaces closest sideways are sampled.  
  
Additional resources:
[NavMesh.SamplePosition](AI.NavMesh.SamplePosition.html).

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

