[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysInstancing.html)
  * [中文](/cn/current/Manual/PartSysInstancing.html)
  * [日本語](/ja/current/Manual/PartSysInstancing.html)
  * [한국어](/kr/current/Manual/PartSysInstancing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysInstancing.html)
  * [中文](/cn/current/Manual/PartSysInstancing.html)
  * [日本語](/ja/current/Manual/PartSysInstancing.html)
  * [한국어](/kr/current/Manual/PartSysInstancing.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System optimization](particle-system-optimization.html)
  * [GPU instancing for Particle Systems](gpu-instancing-particle-systems.html)
  * Apply GPU instancing for a Particle System

[](gpu-instancing-particle-systems.html)

GPU instancing for Particle Systems

[](example-particle-system-gpu-instancing-surface-shader.html)

Example of Particle System GPU instancing in a Surface Shader

# Apply GPU instancing for a Particle System

GPU instancing offers a large performance boost compared with CPU rendering.
You can use it if you want your **particle system** A component that simulates
fluid entities such as liquids, clouds and flames by generating and animating
large numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) to render **Mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) particles (as opposed to the default
[rendering mode](PartSysRendererModule.html) of rendering **billboard** A
textured 2D object that rotates so that it always faces the Camera. [More
info](class-BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) particles).

To be able to use GPU instancing with your particle systems:

  * Set your Particle System’s [renderer](PartSysRendererModule.html) mode to **Mesh**

  * Use a **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) for the
[renderer](PartSysRendererModule.html) material that supports GPU Instancing

  * Run your project on a platform that supports GPU instancing

To enable GPU instancing for a particle system, you must enable the **Enable
GPU Instancing** checkbox in the **Renderer** module of your particle system.

![The option to enable Particle System GPU instancing in the Renderer
module](../uploads/Main/PartSysInstancingEnable.png) The option to enable
Particle System GPU instancing in the Renderer module

Unity comes with a built-in particle shader that supports GPU instancing, but
the default particle material does not use it, so you must change this to use
GPU instancing. The particle shader that supports GPU instancing is called
**Particles/Standard Surface**. To use it, you must create your own new
**material** An asset that defines how a surface should be rendered. [More
info](class-Material.html)  
See in [Glossary](Glossary.html#Material), and set the material’s shader to
**Particles/Standard Surface**. You must then assign this new material to the
material field in the Particle System [renderer](PartSysRendererModule.html)
module.

![The built-in shader that is compatible with Particle System GPU
Instancing](../uploads/Main/PartSysInstancingShader.png) The built-in shader
that is compatible with Particle System GPU Instancing

If you are using a different shader for your particles, it must use ‘#pragma
target 4.5’ or higher. See [Shader Compile Targets](SL-
ShaderCompileTargets.html) for more details. This requirement is higher than
regular GPU Instancing in Unity because the Particle System writes all its
instance data to a single large buffer, rather than breaking up the instancing
into multiple draw calls.

## Custom shader examples

You can also write custom shaders that make use of GPU Instancing. See the
following sections for more information:

  * [Particle system GPU Instancing in a Surface Shader](example-particle-system-gpu-instancing-surface-shader.html)
  * [Particle system GPU Instancing in a Custom Shader](example-particle-system-gpu-instancing-custom-shader.html)
  * [Customising instance data used by the Particle System](example-particle-system-gpu-instancing-custom-vertex-streams.html) (to work alongside Custom Vertex Streams)

[](gpu-instancing-particle-systems.html)

GPU instancing for Particle Systems

[](example-particle-system-gpu-instancing-surface-shader.html)

Example of Particle System GPU instancing in a Surface Shader

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

