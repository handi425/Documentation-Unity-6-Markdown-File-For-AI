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

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).BeginFindPath

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

public PathQueryStatus BeginFindPath(NavMeshLocation start, NavMeshLocation
end, int areaMask, NativeArray<float> costs);

### Parameters

costs | Array of custom cost values for all of the 32 possible area types. Each value must be at least `1.0f`. This parameter is optional and defaults to the area costs configured in the project settings. Additional resources: [NavMesh.GetAreaCost](AI.NavMesh.GetAreaCost.html).  
---|---  
areaMask | Bitmask with values of 1 set at the indices for areas that can be traversed, and values of 0 for areas that are not traversable. This parameter is optional and defaults to [NavMesh.AllAreas](AI.NavMesh.AllAreas.html), if omitted. Additional resources: [Areas and Costs](../Manual/nav-AreasAndCosts.html).  
start | The start location on the NavMesh for the path.  
end | The location on the NavMesh where the path ends.  
  
### Returns

**PathQueryStatus** `InProgress` if the operation was successful and the query
is ready to search for a path.  
`Failure` if the query's NavMeshWorld or any of the received parameters are no
longer valid.

### Description

Initiates a pathfinding operation between two locations on the NavMesh.

The path always begins at the specified location. If the desired end location
is not directly accessible, the search algorithm tries to find a valid
location nearby.  
Calling this method overrides the progress made by this NavMeshQuery in the
previous pathfinding operation.  
  
NavMeshQuery.UpdateFindPath should be called after this method to process the
path search.  
  
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

