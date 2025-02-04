[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-LightProbeProxyVolume-add.html)
  * [中文](/cn/current/Manual/class-LightProbeProxyVolume-add.html)
  * [日本語](/ja/current/Manual/class-LightProbeProxyVolume-add.html)
  * [한국어](/kr/current/Manual/class-LightProbeProxyVolume-add.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-LightProbeProxyVolume-add.html)
  * [中文](/cn/current/Manual/class-LightProbeProxyVolume-add.html)
  * [日本語](/ja/current/Manual/class-LightProbeProxyVolume-add.html)
  * [한국어](/kr/current/Manual/class-LightProbeProxyVolume-add.html)

  * [Lighting](LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * [Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline](LightProbeProxyVolume-landing.html)
  * Set a GameObject to use a Light Probe Proxy Volume in the Built-In Render Pipeline

[](class-LightProbeProxyVolume.html)

Introduction to Light Probe Proxy Volumes in the Built-In Render Pipeline

[](class-LightProbeProxyVolume-configure.html)

Configure a Light Probe Proxy Volume in the Built-In Render Pipeline

# Set a GameObject to use a Light Probe Proxy Volume in the Built-In Render
Pipeline

Most of the Renderer components in Unity contain Light Probes. There are three
options for Light Probes:

  * **Off** : the Renderer doesn’t use any interpolated Light Probes.

  * **Blend Probes** (default value): the Renderer uses one interpolated Light Probe.

  * **Use Proxy Volume** : the Renderer uses a 3D grid of interpolated Light Probes.

When you set the **Light Probes** Light probes store information about how
light passes through space in your scene. A collection of light probes
arranged within a given space can improve lighting on moving objects and
static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) property in the ****Mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer** component to **Use Proxy
Volume** , the **GameObject** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) must have a **Light Probe Proxy
Volume** A component that allows you to use more lighting information for
large dynamic GameObjects that cannot use baked lightmaps (for example, large
Particle Systems or skinned Meshes). [More info](class-
LightProbeProxyVolume.html)  
See in [Glossary](Glossary.html#LightProbeProxyVolume) (LPPV) component
attached. You can add a LPPV component on the same GameObject, or you can use
(borrow) a LPPV component from another GameObject using the **Proxy Volume
Override** property. If Unity cannot find a LPPV component in the current
GameObject or in the Proxy Volume Override GameObject, a warning message is
displayed at the bottom of the Renderer.

## Example

![An example of a simple Mesh Renderer using a Light Probe Proxy Volume
component](../uploads/Main/LightProbeProxyVolumeExample.png) An example of a
simple Mesh Renderer using a Light Probe Proxy Volume component

In the **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) above, there are two planes on the
floor using Materials that emit a lot of light. Note that:

  * The **ambient light** Light that doesn’t come from any specific direction, and contributes equal light in all directions to the Scene. [More info](lighting-window.html)  
See in [Glossary](Glossary.html#Ambientlight) changes across the geometry when
using a LPPV component. Use one interpolated Light Probe to create a constant
color on each side of the geometry.

  * The geometry doesn’t use static **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), and the spheres represent
interpolated Light Probes. They are part of the **Gizmo Renderer**.

[](class-LightProbeProxyVolume.html)

Introduction to Light Probe Proxy Volumes in the Built-In Render Pipeline

[](class-LightProbeProxyVolume-configure.html)

Configure a Light Probe Proxy Volume in the Built-In Render Pipeline

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

