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

#  [NavMeshBuildSettings](AI.NavMeshBuildSettings.html).voxelSize

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

public float voxelSize;

### Description

Sets the voxel size in world length units.

The NavMesh is built by first voxelizing the Scene, and then figuring out
walkable spaces from the voxelized representation of the Scene. The voxel size
controls how closely the NavMesh fits the geometry of your Scene, and is
defined in world units.  
  
If you require a more detail so that the NavMesh more closely fits your
Scene’s geometry, you can reduce the voxel size. An increase in detail will
also cause your game to consume more memory and take more time to calculate
the NavMesh data. The scaling is roughly quadratic, so doubling the resolution
will result in an approximate quadrupling of the build time.  
  
In general you should aim to have 4-6 voxels per character diameter. For
example, if you have a Scene with characters that have a radius of 0.3, a good
voxel size is 0.1. The default value is set to a third of the agentRadius.  
  
Note: If you want to use this setting, you must also set
[overrideVoxelSize](AI.NavMeshBuildSettings-overrideVoxelSize.html) to true.

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

