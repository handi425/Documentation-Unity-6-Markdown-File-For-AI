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

#  [ParticleSystemRenderer](ParticleSystemRenderer.html).BakeMesh

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

public void BakeMesh([Mesh](Mesh.html) mesh,
[ParticleSystemBakeMeshOptions](ParticleSystemBakeMeshOptions.html) options);

## Declaration

public void BakeMesh([Mesh](Mesh.html) mesh, [Camera](Camera.html) camera,
[ParticleSystemBakeMeshOptions](ParticleSystemBakeMeshOptions.html) options);

**Obsolete** BakeMesh with useTransform is deprecated. Use BakeMesh with
ParticleSystemBakeMeshOptions instead.

## Declaration

public void BakeMesh([Mesh](Mesh.html) mesh, bool useTransform);

**Obsolete** BakeMesh with useTransform is deprecated. Use BakeMesh with
ParticleSystemBakeMeshOptions instead.

## Declaration

public void BakeMesh([Mesh](Mesh.html) mesh, [Camera](Camera.html) camera,
bool useTransform);

### Parameters

mesh | A static Mesh to receive the snapshot of the particles.  
---|---  
camera | The Camera used to determine which way camera-space particles face.  
options | Specifies whether to include the rotation and scale of the Transform in the baked Mesh.  
useTransform | Specifies whether to include the rotation and scale of the Transform in the baked Mesh.  
  
### Description

Creates a snapshot of ParticleSystemRenderer and stores it in a `mesh`.

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

