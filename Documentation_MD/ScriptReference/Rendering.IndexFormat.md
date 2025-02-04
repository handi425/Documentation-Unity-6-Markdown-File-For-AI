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

# IndexFormat

enumeration

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
  
Additional resources: [Mesh.indexFormat](Mesh-indexFormat.html),
[ModelImporter.indexFormat](ModelImporter-indexFormat.html),
[Mesh.SetIndices](Mesh.SetIndices.html).

### Properties

[UInt16](Rendering.IndexFormat.UInt16.html)| 16 bit mesh index buffer format.  
---|---  
[UInt32](Rendering.IndexFormat.UInt32.html)| 32 bit mesh index buffer format.  
  
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

