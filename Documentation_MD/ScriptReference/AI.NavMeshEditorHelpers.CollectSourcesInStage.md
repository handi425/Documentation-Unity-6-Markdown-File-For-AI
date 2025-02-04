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

#  [NavMeshEditorHelpers](AI.NavMeshEditorHelpers.html).CollectSourcesInStage

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

### Description

Creates a list of build sources directly from the current geometry in the
specified editor stage.

The collection can be controlled in terms of layers, type of geometry and by
collecting either by hierarchy or volume. The `stageProxy` parameter is used
for picking objects from either the main stage or the stage of a prefab opened
for editing. At runtime that parameter is ignored since objects can only be
part of the main scenes. All main scenes are part of the same main stage while
prefab scenes are each assigned to its own separate prefab stage.

* * *

## Declaration

public static void CollectSourcesInStage([Bounds](Bounds.html)
includedWorldBounds, int includedLayerMask,
[AI.NavMeshCollectGeometry](AI.NavMeshCollectGeometry.html) geometry, int
defaultArea, List<NavMeshBuildMarkup> markups,
[SceneManagement.Scene](SceneManagement.Scene.html) stageProxy,
List<NavMeshBuildSource> results);

### Parameters

includedWorldBounds | The queried objects must overlap these bounds to be included in the results.  
---|---  
includedLayerMask | Specifies which layers are included in the query.  
geometry | Which type of geometry to collect - e.g. physics colliders.  
defaultArea | Area type to assign to results, unless modified by NavMeshMarkup.  
markups | List of markups which allows finer control over how objects are collected.  
stageProxy | Results are selected only from the stage to which this scene belongs.  
results | List where results are stored, the list is cleared at the beginning of the call.  
  
### Description

Collects renderers or physics colliders, and terrains within a volume.

* * *

## Declaration

public static void CollectSourcesInStage([Bounds](Bounds.html)
includedWorldBounds, int includedLayerMask,
[AI.NavMeshCollectGeometry](AI.NavMeshCollectGeometry.html) geometry, int
defaultArea, bool generateLinksByDefault, List<NavMeshBuildMarkup> markups,
bool includeOnlyMarkedObjects,
[SceneManagement.Scene](SceneManagement.Scene.html) stageProxy,
List<NavMeshBuildSource> results);

### Parameters

includedWorldBounds | The queried objects must overlap these bounds to be included in the results.  
---|---  
includedLayerMask | Specifies which layers are included in the query.  
geometry | Which type of geometry to collect - e.g. physics colliders.  
defaultArea | Area type to assign to results, unless modified by NavMeshMarkup.  
generateLinksByDefault | If true, all the source will be considered for generating links. Otherwise, only the marked sources will be considered.  
markups | List of markups which allows finer control over how objects are collected.  
includeOnlyMarkedObjects | Specifies if only objects with markups are collected.  
stageProxy | Results are selected only from the stage to which this scene belongs.  
results | List where results are stored, the list is cleared at the beginning of the call.  
  
### Description

Collects renderers or physics colliders, and terrains within a volume.

* * *

## Declaration

public static void CollectSourcesInStage([Transform](Transform.html) root, int
includedLayerMask, [AI.NavMeshCollectGeometry](AI.NavMeshCollectGeometry.html)
geometry, int defaultArea, List<NavMeshBuildMarkup> markups,
[SceneManagement.Scene](SceneManagement.Scene.html) stageProxy,
List<NavMeshBuildSource> results);

### Parameters

root | If not null, consider only root and its children in the query; if null, includes everything loaded.  
---|---  
includedLayerMask | Specifies which layers are included in the query.  
geometry | Which type of geometry to collect - e.g. physics colliders.  
defaultArea | Area type to assign to results, unless modified by NavMeshMarkup.  
markups | List of markups which allows finer control over how objects are collected.  
stageProxy | Results are selected only from the stage to which this scene belongs.  
results | List where results are stored, the list is cleared at the beginning of the call.  
  
### Description

Collects renderers or physics colliders, and terrains within a transform
hierarchy.

* * *

## Declaration

public static void CollectSourcesInStage([Transform](Transform.html) root, int
includedLayerMask, [AI.NavMeshCollectGeometry](AI.NavMeshCollectGeometry.html)
geometry, int defaultArea, bool generateLinksByDefault,
List<NavMeshBuildMarkup> markups, bool includeOnlyMarkedObjects,
[SceneManagement.Scene](SceneManagement.Scene.html) stageProxy,
List<NavMeshBuildSource> results);

### Parameters

root | If not null, consider only root and its children in the query; if null, includes everything loaded.  
---|---  
includedLayerMask | Specifies which layers are included in the query.  
geometry | Which type of geometry to collect - e.g. physics colliders.  
defaultArea | Area type to assign to results, unless modified by NavMeshMarkup.  
generateLinksByDefault | If true, all the source will be considered for generating links. Otherwise, only the marked sources will be considered.  
markups | List of markups which allows finer control over how objects are collected.  
includeOnlyMarkedObjects | Specifies if only objects with markups are collected.  
stageProxy | Results are selected only from the stage to which this scene belongs.  
results | List where results are stored, the list is cleared at the beginning of the call.  
  
### Description

Collects renderers or physics colliders, and terrains within a transform
hierarchy.

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

