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

# Graphics

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Raw interface to Unity's drawing functions.

This is the high-level shortcut into the optimized mesh drawing functionality
of Unity.

### Static Properties

[activeColorBuffer](Graphics-activeColorBuffer.html)| Currently active color
buffer (Read Only).  
---|---  
[activeColorGamut](Graphics-activeColorGamut.html)| Returns the currently
active color gamut.  
[activeDepthBuffer](Graphics-activeDepthBuffer.html)| Currently active
depth/stencil buffer (Read Only).  
[activeTier](Graphics-activeTier.html)| The GraphicsTier for the current
device.  
[minOpenGLESVersion](Graphics-minOpenGLESVersion.html)| The minimum OpenGL ES
version. The value is specified in PlayerSettings.  
[preserveFramebufferAlpha](Graphics-preserveFramebufferAlpha.html)| True when
rendering over native UI is enabled in Player Settings (readonly).  
  
### Static Methods

[Blit](Graphics.Blit.html)| Uses a shader to copy the pixel data from a
texture into a render target.  
---|---  
[BlitMultiTap](Graphics.BlitMultiTap.html)| Copies source texture into
destination, for multi-tap shader.  
[ClearRandomWriteTargets](Graphics.ClearRandomWriteTargets.html)| Unset random
write targets for Shader Model 4.5 level pixel shaders.  
[ConvertTexture](Graphics.ConvertTexture.html)| Copies the pixel data from one
texture, converts the data into a different format, and copies it into another
texture.  
[CopyBuffer](Graphics.CopyBuffer.html)| Copies the contents of one
GraphicsBuffer into another.  
[CopyTexture](Graphics.CopyTexture.html)| Copies pixel data from one texture
to another.  
[CreateAsyncGraphicsFence](Graphics.CreateAsyncGraphicsFence.html)| Shortcut
for calling Graphics.CreateGraphicsFence with
GraphicsFenceType.AsyncQueueSynchronisation as the first parameter.  
[CreateGraphicsFence](Graphics.CreateGraphicsFence.html)| Creates a
GraphicsFence.  
[DrawMesh](Graphics.DrawMesh.html)| Draw a mesh.  
[DrawMeshInstanced](Graphics.DrawMeshInstanced.html)| Draws the same mesh
multiple times using GPU instancing.  
[DrawMeshInstancedIndirect](Graphics.DrawMeshInstancedIndirect.html)| This
function is now obsolete. Use Graphics.RenderMeshIndirect instead. Draws the
same mesh multiple times using GPU instancing.  
[DrawMeshInstancedProcedural](Graphics.DrawMeshInstancedProcedural.html)| This
function is now obsolete. Use Graphics.RenderMeshPrimitives instead. Draws the
same mesh multiple times using GPU instancing. This is similar to
Graphics.DrawMeshInstancedIndirect, except that when the instance count is
known from script, it can be supplied directly using this method, rather than
via a ComputeBuffer.  
[DrawMeshNow](Graphics.DrawMeshNow.html)| Draw a mesh immediately.  
[DrawProcedural](Graphics.DrawProcedural.html)| This function is now obsolete.
For non-indexed rendering, use Graphics.RenderPrimitives instead. For indexed
rendering, use Graphics.RenderPrimitivesIndexed. Draws procedural geometry on
the GPU.  
[DrawProceduralIndirect](Graphics.DrawProceduralIndirect.html)| Draws
procedural geometry on the GPU.  
[DrawProceduralIndirectNow](Graphics.DrawProceduralIndirectNow.html)| Draws
procedural geometry on the GPU.  
[DrawProceduralNow](Graphics.DrawProceduralNow.html)| Draws procedural
geometry on the GPU.  
[DrawTexture](Graphics.DrawTexture.html)| Draw a texture in screen
coordinates.  
[ExecuteCommandBuffer](Graphics.ExecuteCommandBuffer.html)| Execute a command
buffer.  
[ExecuteCommandBufferAsync](Graphics.ExecuteCommandBufferAsync.html)| Executes
a command buffer on an async compute queue with the queue selected based on
the ComputeQueueType parameter passed.  
[RenderMesh](Graphics.RenderMesh.html)| Renders a mesh with given rendering
parameters.  
[RenderMeshIndirect](Graphics.RenderMeshIndirect.html)| Renders multiple
instances of a mesh using GPU instancing and rendering command arguments from
commandBuffer.  
[RenderMeshInstanced](Graphics.RenderMeshInstanced.html)| Renders multiple
instances of a mesh using GPU instancing.  
[RenderMeshPrimitives](Graphics.RenderMeshPrimitives.html)| Renders multiple
instances of a Mesh using GPU instancing and a custom shader.  
[RenderPrimitives](Graphics.RenderPrimitives.html)| Renders non-indexed
primitives with GPU instancing and a custom shader.  
[RenderPrimitivesIndexed](Graphics.RenderPrimitivesIndexed.html)| Renders
indexed primitives with GPU instancing and a custom shader.  
[RenderPrimitivesIndexedIndirect](Graphics.RenderPrimitivesIndexedIndirect.html)|
Renders indexed primitives with GPU instancing and a custom shader with
rendering command arguments from commandBuffer.  
[RenderPrimitivesIndirect](Graphics.RenderPrimitivesIndirect.html)| Renders
primitives with GPU instancing and a custom shader using rendering command
arguments from commandBuffer.  
[SetRandomWriteTarget](Graphics.SetRandomWriteTarget.html)| Set random write
target for Shader Model 4.5 level pixel shaders.  
[SetRenderTarget](Graphics.SetRenderTarget.html)| Sets current render target.  
[WaitOnAsyncGraphicsFence](Graphics.WaitOnAsyncGraphicsFence.html)| Instructs
the GPU to pause processing of the queue until it passes through the
GraphicsFence fence.  
  
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

