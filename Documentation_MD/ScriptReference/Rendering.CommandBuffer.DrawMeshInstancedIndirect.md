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

#  [CommandBuffer](Rendering.CommandBuffer.html).DrawMeshInstancedIndirect

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

public void DrawMeshInstancedIndirect([Mesh](Mesh.html) mesh, int
submeshIndex, [Material](Material.html) material, int shaderPass,
[ComputeBuffer](ComputeBuffer.html) bufferWithArgs, int argsOffset,
[MaterialPropertyBlock](MaterialPropertyBlock.html) properties);

## Declaration

public void DrawMeshInstancedIndirect([Mesh](Mesh.html) mesh, int
submeshIndex, [Material](Material.html) material, int shaderPass,
[ComputeBuffer](ComputeBuffer.html) bufferWithArgs, int argsOffset);

## Declaration

public void DrawMeshInstancedIndirect([Mesh](Mesh.html) mesh, int
submeshIndex, [Material](Material.html) material, int shaderPass,
[ComputeBuffer](ComputeBuffer.html) bufferWithArgs);

## Declaration

public void DrawMeshInstancedIndirect([Mesh](Mesh.html) mesh, int
submeshIndex, [Material](Material.html) material, int shaderPass,
[GraphicsBuffer](GraphicsBuffer.html) bufferWithArgs, int argsOffset,
[MaterialPropertyBlock](MaterialPropertyBlock.html) properties);

## Declaration

public void DrawMeshInstancedIndirect([Mesh](Mesh.html) mesh, int
submeshIndex, [Material](Material.html) material, int shaderPass,
[GraphicsBuffer](GraphicsBuffer.html) bufferWithArgs, int argsOffset);

## Declaration

public void DrawMeshInstancedIndirect([Mesh](Mesh.html) mesh, int
submeshIndex, [Material](Material.html) material, int shaderPass,
[GraphicsBuffer](GraphicsBuffer.html) bufferWithArgs);

### Parameters

mesh | The [Mesh](Mesh.html) to draw.  
---|---  
submeshIndex | Which subset of the mesh to draw. This only applies to meshes that are composed of several materials.  
material |  [Material](Material.html) to use.  
shaderPass | Which pass of the shader to use, or -1 which renders all passes.  
properties | Additional Material properties to apply onto the Material just before this Mesh is drawn. See [MaterialPropertyBlock](MaterialPropertyBlock.html).  
bufferWithArgs | The GPU buffer containing the arguments for how many instances of this mesh to draw.  
argsOffset | The byte offset into the buffer, where the draw arguments start.  
  
### Description

Add a "draw mesh with indirect instancing" command.

Additional resources: [DrawMesh](Rendering.CommandBuffer.DrawMesh.html),
[Graphics.DrawMeshInstancedIndirect](Graphics.DrawMeshInstancedIndirect.html),
[MaterialPropertyBlock](MaterialPropertyBlock.html).

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

