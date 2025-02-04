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

#  [NavMeshBuildSettings](AI.NavMeshBuildSettings.html).buildHeightMesh

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

public bool buildHeightMesh;

### Description

Enables the creation of additional data needed to determine the height at any
position on the NavMesh more accurately.

The NavMesh Agent is constrained to the surface of the NavMesh as it
navigates. Since the NavMesh is an approximation of the walkable space, some
features are evened out when the NavMesh is built. For example, stairs may
appear as a slope in the NavMesh. If you need accurate placement of the agent
for your game, enable height mesh building when you build the NavMesh. Note
that building the height mesh will take up memory and processing at runtime,
and it increases the time needed to bake the NavMesh.  
  
The current implementation of the height mesh has the following limitations:

  * It can construct height data for a Terrain only when its horizontal plane is parallel to the XZ plane of the NavMesh.
  * During a NavMesh update, if the build setting "preserveTilesOutsideBounds" is true the height mesh will not be created and if it already exists, will be removed.

This property is available as of Unity 2022.2. It will be correctly compiled
in scripts when the `UNITY_2022_2_OR_NEWER` symbol is [defined by the
engine](../Manual/platform-dependent-compilation.html).  
  
Additional resources: [NavMeshSurface Advanced
Settings](https://docs.unity3d.com/Packages/com.unity.ai.navigation@1.0/manual/NavMeshSurface.html#advanced-
settings)

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

