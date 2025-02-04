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

#  [SkinnedMeshRenderer](SkinnedMeshRenderer.html).BakeMesh

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

[Switch to Manual](../Manual/class-SkinnedMeshRenderer.html "Go to
SkinnedMeshRenderer Component in the Manual")

## Declaration

public void BakeMesh([Mesh](Mesh.html) mesh);

## Declaration

public void BakeMesh([Mesh](Mesh.html) mesh, bool useScale);

### Parameters

mesh | A static mesh that will receive the snapshot of the skinned mesh.  
---|---  
useScale | Whether to compensate for the SkinnedMeshRenderer's Transform scale. If true, the baked Mesh is the same size as the original. If false, the baked Mesh matches the scaling of the SkinnedMeshRenderer's Transform component. The default value is false.  
  
### Description

Creates a snapshot of SkinnedMeshRenderer and stores it in `mesh`.

The vertices are relative to the SkinnedMeshRenderer Transform component.  
This function always compensates for the position and rotation values of the
Transform component with the origin of the baked mesh always the same as the
origin of the original mesh.  
  
**Notes** :  
The snapshot is still computed even when
[updateWhenOffscreen](SkinnedMeshRenderer-updateWhenOffscreen.html) is set to
false and the skinned mesh object is currently offscreen.  
When this function is called the skinning process will always take place on
the CPU, regardless of the [GPU Skinning](PlayerSettings-gpuSkinning.html)
setting.

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

