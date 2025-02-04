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

#  [CommandBuffer](Rendering.CommandBuffer.html).DrawProcedural

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

public void DrawProcedural([Matrix4x4](Matrix4x4.html) matrix,
[Material](Material.html) material, int shaderPass,
[MeshTopology](MeshTopology.html) topology, int vertexCount, int instanceCount
= 1, [MaterialPropertyBlock](MaterialPropertyBlock.html) properties = null);

### Parameters

matrix | Transformation matrix to use.  
---|---  
material | Material to use.  
shaderPass | Which pass of the shader to use (or -1 for all passes).  
topology | Topology of the procedural geometry.  
vertexCount | Vertex count to render.  
instanceCount | Instance count to render.  
properties | Additional material properties to apply just before rendering. See [MaterialPropertyBlock](MaterialPropertyBlock.html).  
  
### Description

Add a "draw procedural geometry" command.

When the command buffer executes, this will do a draw call on the GPU, without
any vertex or index buffers. This is mainly useful on [Shader Model
4.5](../Manual/SL-ShaderCompileTargets.html) level hardware where shaders can
read arbitrary data from [ComputeBuffer](ComputeBuffer.html) buffers.  
  
In the vertex shader, you'd typically use the SV_VertexID and SV_InstanceID
input variables to fetch data from some buffers.  
  
Note that the draw call will not have any lighting related shader data (light
colors, directions, shadows, light and reflection probes etc.) set up. If the
shader used by the material uses any lighting related variables, the results
are undefined.  
  
Additional resources:
[DrawProceduralIndirect](Rendering.CommandBuffer.DrawProceduralIndirect.html),
[MaterialPropertyBlock](MaterialPropertyBlock.html),
[Graphics.DrawProcedural](Graphics.DrawProcedural.html).

* * *

## Declaration

public void DrawProcedural([GraphicsBuffer](GraphicsBuffer.html) indexBuffer,
[Matrix4x4](Matrix4x4.html) matrix, [Material](Material.html) material, int
shaderPass, [MeshTopology](MeshTopology.html) topology, int indexCount, int
instanceCount, [MaterialPropertyBlock](MaterialPropertyBlock.html)
properties);

## Declaration

public void DrawProcedural([GraphicsBuffer](GraphicsBuffer.html) indexBuffer,
[Matrix4x4](Matrix4x4.html) matrix, [Material](Material.html) material, int
shaderPass, [MeshTopology](MeshTopology.html) topology, int indexCount, int
instanceCount);

## Declaration

public void DrawProcedural([GraphicsBuffer](GraphicsBuffer.html) indexBuffer,
[Matrix4x4](Matrix4x4.html) matrix, [Material](Material.html) material, int
shaderPass, [MeshTopology](MeshTopology.html) topology, int indexCount);

### Parameters

matrix | Transformation matrix to use.  
---|---  
material | Material to use.  
shaderPass | Which pass of the shader to use (or -1 for all passes).  
topology | Topology of the procedural geometry.  
indexCount | Index count to render.  
instanceCount | Instance count to render.  
indexBuffer | The index buffer used to submit vertices to the GPU.  
properties | Additional material properties to apply just before rendering. See [MaterialPropertyBlock](MaterialPropertyBlock.html).  
  
### Description

Add a "draw procedural geometry" command.

When the command buffer executes, this will do a draw call on the GPU, without
a vertex buffer. This is mainly useful on [Shader Model 4.5](../Manual/SL-
ShaderCompileTargets.html) level hardware where shaders can read arbitrary
data from [ComputeBuffer](ComputeBuffer.html) buffers.  
  
In the vertex shader, you'd typically use the SV_VertexID and SV_InstanceID
input variables to fetch data from some buffers.  
  
Additional resources:
[DrawProceduralIndirect](Rendering.CommandBuffer.DrawProceduralIndirect.html),
[MaterialPropertyBlock](MaterialPropertyBlock.html),
[Graphics.DrawProcedural](Graphics.DrawProcedural.html).

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

