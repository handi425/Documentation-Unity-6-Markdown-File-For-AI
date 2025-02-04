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

#  [Mesh.MeshData](Mesh.MeshData.html).indexFormat

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

public [Rendering.IndexFormat](Rendering.IndexFormat.html) indexFormat;

### Description

Gets the format of the index buffer data in the `MeshData`. (Read Only)

A Mesh's index buffer format can be either 16 bit (which supports up to 65535
vertices), or 32 bit (which supports up to 4 billion vertices). The default
index format is 16 bit, which requires less memory and bandwidth and is more
widely supported than 32 bit. Note that GPU support for 32 bit indices is not
guaranteed on all platforms; for example Android devices with Mali-400 GPUs do
not support them. When using 32 bit indices on such a platform, Unity logs a
warning message and does not render the Mesh. Additional resources:
[IndexFormat](Rendering.IndexFormat.html), [Mesh.indexFormat](Mesh-
indexFormat.html), [GetIndices](Mesh.MeshData.GetIndices.html),
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html).

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

