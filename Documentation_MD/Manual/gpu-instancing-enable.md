[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gpu-instancing-enable.html)
  * [中文](/cn/current/Manual/gpu-instancing-enable.html)
  * [日本語](/ja/current/Manual/gpu-instancing-enable.html)
  * [한국어](/kr/current/Manual/gpu-instancing-enable.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gpu-instancing-enable.html)
  * [中文](/cn/current/Manual/gpu-instancing-enable.html)
  * [日本語](/ja/current/Manual/gpu-instancing-enable.html)
  * [한국어](/kr/current/Manual/gpu-instancing-enable.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [GPU instancing](GPUInstancing-landing.html)
  * Enable GPU instancing

[](GPUInstancing.html)

Introduction to GPU instancing

[](gpu-instancing-troubleshoot.html)

Troubleshooting GPU instancing

# Enable GPU instancing

Unity uses GPU instancing for **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that share the same **mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) and material. To instance a mesh and
material:

  * The material’s [shader](Shaders.html)A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) must support GPU instancing. Unity’s
[Standard Shader](shader-StandardShader.html) supports GPU instancing, as do
all [surface shaders](SL-SurfaceShaders.html)A streamlined way of writing
shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader). To add GPU instancing support
to any other shader, see [Creating shaders that support GPU instancing](gpu-
instancing-shader.html).

  * The mesh must come from one of the following sources, grouped by behavior: 
    * A [MeshRenderer](class-MeshRenderer.html) component or a [Graphics.RenderMesh](../ScriptReference/Graphics.RenderMesh.html) call.   
Behavior: Unity adds these meshes to a list and then checks to see which
meshes it can instance.  
Unity does not support GPU instancing for [SkinnedMeshRenderers](class-
SkinnedMeshRenderer.html) or MeshRenderer components attached to GameObjects
that are SRP Batcher compatible. For more information, see [SRP Batcher
compatibility](SRPBatcher.html).

    * A [Graphics.RenderMeshInstanced](../ScriptReference/Graphics.RenderMeshInstanced.html) or [Graphics.RenderMeshIndirect](../ScriptReference/Graphics.RenderMeshIndirect.html) call. These methods render the same mesh multiple times using the same shader. Each call to these methods issues a separate draw call. Unity does not merge these draw calls.

To use GPU instancing for a material, select the **Enable GPU Instancing**
option in the **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

To enable **Light Probe** Light probes store information about how light
passes through space in your scene. A collection of light probes arranged
within a given space can improve lighting on moving objects and static LOD
scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) rendering for
`Graphics.RenderMeshInstanced`, provide a
[MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html) that
includes the Probe data. For more information and code examples, see
[LightProbes.CalculateInterpolatedLightAndOcclusionProbes](../ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html).

Alternatively, if your project uses the Built-In **Render Pipeline** A series
of operations that take the contents of a Scene, and displays them on a
screen. Unity lets you choose from pre-built render pipelines, or write your
own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), you can pass an LPPV
component reference and
[LightProbeUsage.UseProxyVolume](../ScriptReference/Rendering.LightProbeUsage.UseProxyVolume.html)
to `Graphics.RenderMeshInstanced`. When you do this, all instances sample the
volume for the [L0 and L1 bands](LightProbes-TechnicalInformation.html) of the
Light Probe data. If you want to supplement L2 data and occlusion data, use a
`MaterialPropertyBlock`. For more information, see [Light Probes: Technical
Information](LightProbes-TechnicalInformation.html).

## Additional resources

  * [Make materials incompatible with the SRP Batcher in URP](SRPBatcher-Incompatible.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)

[](GPUInstancing.html)

Introduction to GPU instancing

[](gpu-instancing-troubleshoot.html)

Troubleshooting GPU instancing

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

