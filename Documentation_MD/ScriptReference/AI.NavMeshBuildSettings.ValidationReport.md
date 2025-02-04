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

#  [NavMeshBuildSettings](AI.NavMeshBuildSettings.html).ValidationReport

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

## Declaration

public string[] ValidationReport([Bounds](Bounds.html) buildBounds);

### Parameters

buildBounds | Describes the volume to build NavMesh for.  
---|---  
  
### Returns

**string[]** The list of violated constraints.

### Description

Validates the properties of NavMeshBuildSettings.

Returns a string of violated constraints. - and suggestions for changes for
the current values in the build settings and the provided bounds for building
the NavMesh.  
  
An empty array is returned if all internal constraints are satisfied.  
  
Some of the settings which you can specify in the
[NavMeshBuildSettings](AI.NavMeshBuildSettings.html) struct are coupled to
each other, meaning there are constraints on the values based on other values.
For example, it’s not valid for [agentClimb](AI.NavMeshBuildSettings-
agentClimb.html) to be larger than [agentHeight](AI.NavMeshBuildSettings-
agentHeight.html). Another invalid case is when the vertical size of the
buildBounds exceeds the height of 65535 voxel units.  
  
You can use this function to check if the values in
[NavMeshBuildSettings](AI.NavMeshBuildSettings.html) violate any of the
constraints, before starting the NavMesh building process.  
  
Ignoring the violated constraints might give unexpected results when building
a NavMesh, but will still produce a NavMesh.

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

