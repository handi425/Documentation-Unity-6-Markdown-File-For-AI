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

#  [Mesh](Mesh.html).GetNativeIndexBufferPtr

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

## Declaration

public IntPtr GetNativeIndexBufferPtr();

### Returns

**IntPtr** Pointer to the underlying graphics API index buffer.

### Description

Retrieves a native (underlying graphics API) pointer to the index buffer.

Use this function to retrieve a pointer/handle corresponding to the Mesh index
buffer, as it is represented in the native graphics API. This can be used to
enable Mesh manipulation from [native code plugins](../Manual/native-plugin-
interface.html).  
  
Index buffer data is either 16 or 32 bit per index, depending on
[indexFormat](Mesh-indexFormat.html). The layout of the index buffer otherwise
depends on the [MeshTopology](MeshTopology.html) that is used (see
[SetIndices](Mesh.SetIndices.html)). The most common case is Meshes composed
of triangle lists, which have index buffers with three indices per triangle.  
  
The type of data returned depends on the underlying graphics API:

  * ID3D11Buffer on D3D11
  * ID3D12Resource on D3D12
  * id<MTLBuffer> on Metal
  * buffer "name" (as GLuint) on OpenGL/ES
  * internal representation on Vulkan, that should be accessed via IUnityGraphicsVulkan interface

For most use cases (when writing Mesh data from native code), you need to mark
the Mesh as "dynamic" (see [MarkDynamic](Mesh.MarkDynamic.html)) before
getting the native buffer pointer. Generally this switches the buffers to be
CPU-writable.  
  
Note that calling this function when using multi-threaded rendering will
synchronize with the rendering thread (a slow operation), so best practice is
to set up necessary buffer pointers only at initialization time.  
  
Additional resources: [Native code plugins](../Manual/native-plugin-
interface.html),
[GetNativeVertexBufferPtr](Mesh.GetNativeVertexBufferPtr.html),
[SetIndices](Mesh.SetIndices.html).

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

