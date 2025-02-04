[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightProbeProxyVolume-landing.html)
  * [中文](/cn/current/Manual/LightProbeProxyVolume-landing.html)
  * [日本語](/ja/current/Manual/LightProbeProxyVolume-landing.html)
  * [한국어](/kr/current/Manual/LightProbeProxyVolume-landing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightProbeProxyVolume-landing.html)
  * [中文](/cn/current/Manual/LightProbeProxyVolume-landing.html)
  * [日本語](/ja/current/Manual/LightProbeProxyVolume-landing.html)
  * [한국어](/kr/current/Manual/LightProbeProxyVolume-landing.html)

  * [Lighting](LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline

[](LightingBakedAmbientOcclusion.html)

Add ambient occlusion in the Built-In Render Pipeline

[](class-LightProbeProxyVolume.html)

Introduction to Light Probe Proxy Volumes in the Built-In Render Pipeline

# Configure a GameObject to sample more Light Probes in the Built-In Render
Pipeline

To make lighting more realistic, use a **Light Probe** Light probes store
information about how light passes through space in your scene. A collection
of light probes arranged within a given space can improve lighting on moving
objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) Proxy Volume to configure a
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to sample multiple Light Probes.

**Page** | **Description**  
---|---  
[Light Probe Proxy Volumes](class-LightProbeProxyVolume.html)A component that
allows you to use more lighting information for large dynamic GameObjects that
cannot use baked lightmaps (for example, large Particle Systems or skinned
Meshes). [More info](class-LightProbeProxyVolume.html)  
See in [Glossary](Glossary.html#LightProbeProxyVolume) | Understand how a Light Probe Proxy Volume component generates a 3D grid and texture that Unity uses to create gradients on GameObjects.  
[Set a GameObject to use a Light Probe Proxy Volume](class-LightProbeProxyVolume-add.html) | Use the settings in a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer component to set a GameObject
to sample multiple probes.  
[Configure a Light Probe Proxy Volume](class-LightProbeProxyVolume-configure.html) | Change the size and data format of a Light Probe Proxy Volume.  
[Light Probe Proxy Volume component reference](class-LightProbeProxyVolume-reference.html) | Explore the properties and settings in the Light Probe Proxy Volume component **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to customize how Unity
generates the 3D grid and texture.  
[Add Light Probe Proxy Volume support to a custom shader](class-LightProbeProxyVolume-Shader.html) | An example of a particle **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that uses the `ShadeSHPerPixel`
function to add support for a Light Probe Proxy Volume.  
  
## Additional resources

  * [Precalculating indirect light with Light Probes](LightProbes-landing.html)

[](LightingBakedAmbientOcclusion.html)

Add ambient occlusion in the Built-In Render Pipeline

[](class-LightProbeProxyVolume.html)

Introduction to Light Probe Proxy Volumes in the Built-In Render Pipeline

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

