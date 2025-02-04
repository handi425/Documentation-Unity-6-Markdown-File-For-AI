[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightProbes-MeshRenderer.html)
  * [中文](/cn/current/Manual/LightProbes-MeshRenderer.html)
  * [日本語](/ja/current/Manual/LightProbes-MeshRenderer.html)
  * [한국어](/kr/current/Manual/LightProbes-MeshRenderer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightProbes-MeshRenderer.html)
  * [中文](/cn/current/Manual/LightProbes-MeshRenderer.html)
  * [日本語](/ja/current/Manual/LightProbes-MeshRenderer.html)
  * [한국어](/kr/current/Manual/LightProbes-MeshRenderer.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating indirect light with Light Probes](LightProbes-landing.html)
  * Set a GameObject to use light from Light Probes

[](LightProbes-Placing-Scripting.html)

Place Light Probes with a script

[](light-probes-and-scene-loading.html)

Load Light Probes in multiple scenes

# Set a GameObject to use light from Light Probes

To use **Light Probes** Light probes store information about how light passes
through space in your scene. A collection of light probes arranged within a
given space can improve lighting on moving objects and static LOD scenery
within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) on your moving GameObjects, the
**Mesh Renderer** A mesh component that takes the geometry from the Mesh
Filter and renders it at the position defined by the object’s Transform
component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) component on the moving
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) must be set correctly. The
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer component has a **Light
Probes** setting which is set to **Blend Probes** by default. This means that
by default, all GameObjects will use light probes and will blend between the
nearest probes as it changes position in your **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

You can change this setting to either “off” or “use proxy volume”. Switching
the light probes setting to off will disable the light probe’s effect on this
GameObject.

Light Probe Proxy Volumes are a special setting which you can use for
situations where a **large moving object** might be too big to be sensibly lit
by the results of a single tetrahedron from the **light probe group** A
component that enables you to add Light Probes to GameObjects in your scene.
[More info](class-LightProbeGroup.html)  
See in [Glossary](Glossary.html#LightProbeGroup), and instead needs to be lit
by multiple groups of light probes across the length of the model. See **Light
Probe Proxy Volumes** A component that allows you to use more lighting
information for large dynamic GameObjects that cannot use baked lightmaps (for
example, large Particle Systems or skinned Meshes). [More info](class-
LightProbeProxyVolume.html)  
See in [Glossary](Glossary.html#LightProbeProxyVolume) for more information.

The other setting in the Mesh Renderer **inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) which relates to light probes is
the **Anchor Override** setting. As described previously, when a GameObject
moves through your scene, Unity calculates which tetrahedron the GameObject
falls within from the volume defined by the light probe groups. By default
this is calculated from the centre point of the Mesh’s bounding box, however
you can override the point that is used by assigning a different GameObject to
the **Anchor Override** field.

If you assign a different GameObject to this field, it is up to you to move
that GameObject in a way that suits the lighting you want on your mesh.

The anchor override may be useful when a GameObject contains two separate
adjoining meshes; if both meshes are lit individually according to their
bounding box positions then the lighting will be discontinuous at the place
where they join. This can be prevented by using the same Transform (for
example the parent or a child object) as the interpolation point for both Mesh
Renderers or by using a Light Probe Proxy Volume.

[](LightProbes-Placing-Scripting.html)

Place Light Probes with a script

[](light-probes-and-scene-loading.html)

Load Light Probes in multiple scenes

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

