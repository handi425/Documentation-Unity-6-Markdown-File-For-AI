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

#  [Mesh](Mesh.html).indexFormat

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

Format of the mesh index buffer data.

Index buffer can either be 16 bit (supports up to 65535 vertices in a mesh),
or 32 bit (supports up to 4 billion vertices). Default index format is 16 bit,
since that takes less memory and bandwidth.  
  
Note that GPU support for 32 bit indices is not guaranteed on all platforms;
for example Android devices with Mali-400 GPU do not support them. When using
32 bit indices on such a platform, a warning message will be logged and mesh
will not render.  
  
**Note:** the maximum possible vertex index (for example, 0xFFFF for a 16 bit
index format) might not be usable. Some graphics APIs and GPUs skip rendering
triangles with maximum vertex indices.  
  
Changing `indexFormat` sets [subMeshCount](Mesh-subMeshCount.html) to one and
clears the index buffer.  
  
Refer to [Mesh.MeshData.GetIndexData](Mesh.MeshData.GetIndexData.html) for an
example.  
  
Additional resources: [IndexFormat](Rendering.IndexFormat.html),
[ModelImporter.indexFormat](ModelImporter-indexFormat.html),
[SetIndices](Mesh.SetIndices.html), [SetTriangles](Mesh.SetTriangles.html),
[SetIndexBufferParams](Mesh.SetIndexBufferParams.html),
[SetIndexBufferData](Mesh.SetIndexBufferData.html),
[MeshData](Mesh.MeshData.html).

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

