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

# NavMeshBuildSettings

struct in UnityEngine.AI

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

### Description

The NavMeshBuildSettings struct allows you to specify a collection of settings
which describe the dimensions and limitations of a particular agent type.

You might want to define multiple NavMeshBuildSettings if your game involves
characters with large differences in height, width or climbing ability.  
  
You can also use this struct to control the precision and granularity of the
build process, by setting the voxel and tile sizes. Some of the values are
coupled, meaning there are constraints on the values based on other values.
For example, it’s not valid for [agentClimb](AI.NavMeshBuildSettings-
agentClimb.html) to be larger than [agentHeight](AI.NavMeshBuildSettings-
agentHeight.html). To help diagnose violations of these rules, a special
method [ValidationReport](AI.NavMeshBuildSettings.ValidationReport.html) can
be evaluated.

### Properties

[agentClimb](AI.NavMeshBuildSettings-agentClimb.html)| The maximum vertical
step size an agent can take.  
---|---  
[agentHeight](AI.NavMeshBuildSettings-agentHeight.html)| The height of the
agent for baking in world units.  
[agentRadius](AI.NavMeshBuildSettings-agentRadius.html)| The radius of the
agent for baking in world units.  
[agentSlope](AI.NavMeshBuildSettings-agentSlope.html)| The maximum slope angle
which is walkable (angle in degrees).  
[agentTypeID](AI.NavMeshBuildSettings-agentTypeID.html)| The agent type ID the
NavMesh will be baked for.  
[buildHeightMesh](AI.NavMeshBuildSettings-buildHeightMesh.html)| Enables the
creation of additional data needed to determine the height at any position on
the NavMesh more accurately.  
[debug](AI.NavMeshBuildSettings-debug.html)| Options for collecting debug data
during the build process.  
[ledgeDropHeight](AI.NavMeshBuildSettings-ledgeDropHeight.html)| Maximum agent
drop height.  
[maxJobWorkers](AI.NavMeshBuildSettings-maxJobWorkers.html)| The maximum
number of worker threads that the build process can utilize when building a
NavMesh with these settings.  
[maxJumpAcrossDistance](AI.NavMeshBuildSettings-maxJumpAcrossDistance.html)|
Maximum agent jump distance.  
[minRegionArea](AI.NavMeshBuildSettings-minRegionArea.html)| The approximate
minimum area of individual NavMesh regions.  
[overrideTileSize](AI.NavMeshBuildSettings-overrideTileSize.html)| Enables
overriding the default tile size. Additional resources: tileSize.  
[overrideVoxelSize](AI.NavMeshBuildSettings-overrideVoxelSize.html)| Enables
overriding the default voxel size. Additional resources: voxelSize.  
[tileSize](AI.NavMeshBuildSettings-tileSize.html)| Sets the tile size in voxel
units.  
[voxelSize](AI.NavMeshBuildSettings-voxelSize.html)| Sets the voxel size in
world length units.  
  
### Public Methods

[ValidationReport](AI.NavMeshBuildSettings.ValidationReport.html)| Validates
the properties of NavMeshBuildSettings.  
---|---  
  
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

