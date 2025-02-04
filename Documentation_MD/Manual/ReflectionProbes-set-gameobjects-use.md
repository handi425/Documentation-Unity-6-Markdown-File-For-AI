[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ReflectionProbes-set-gameobjects-use.html)
  * [中文](/cn/current/Manual/ReflectionProbes-set-gameobjects-use.html)
  * [日本語](/ja/current/Manual/ReflectionProbes-set-gameobjects-use.html)
  * [한국어](/kr/current/Manual/ReflectionProbes-set-gameobjects-use.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ReflectionProbes-set-gameobjects-use.html)
  * [中文](/cn/current/Manual/ReflectionProbes-set-gameobjects-use.html)
  * [日本語](/ja/current/Manual/ReflectionProbes-set-gameobjects-use.html)
  * [한국어](/kr/current/Manual/ReflectionProbes-set-gameobjects-use.html)

  * [Lighting](LightingOverview.html)
  * [Reflections](reflections-landing.html)
  * Set GameObjects to use Reflection Probes

[](ReflectionProbes-set-gameobjects.html)

Add GameObjects to reflections

[](ReflectionProbes-EnableReflectionsOfReflections.html)

Enable reflections of reflections

# Set GameObjects to use Reflection Probes

To make use of the reflection **cubemap** A collection of six square textures
that can represent the reflections in an environment or the skybox drawn
behind your geometry. The six squares form the faces of an imaginary cube that
surrounds an object; each face represents the view along the directions of the
world axes (up, down, left, right, forward and back). [More info](class-
Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap), an object must have the **Reflection
Probes** A rendering component that captures a spherical view of its
surroundings in all directions, rather like a camera. The captured image is
then stored as a Cubemap that can be used by objects with reflective
materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) option enabled on its [Mesh
Renderer](class-MeshRenderer.html)A mesh component that takes the geometry
from the Mesh Filter and renders it at the position defined by the object’s
Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) and also be using a **shader** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that supports reflection probes. When
the object passes within the volume set by the probe’s **Size** and **Probe
Origin** properties, the probe’s cubemap will be applied to the object.

You can also manually set which reflection probe to use for a particular
object using the settings on the object’s [Mesh Renderer](class-
MeshRenderer.html). To do this, select one of the options for the **Mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer’s **Reflection Probes**
property (**Simple** , **Blend Probes** or **Blend Probes and Skybox**) and
drag the chosen probe onto its **Anchor Override** property.

See the [Reflection Probes](ReflectionProbes.html) section in the manual for
further details about principles and usage.

[](ReflectionProbes-set-gameobjects.html)

Add GameObjects to reflections

[](ReflectionProbes-EnableReflectionsOfReflections.html)

Enable reflections of reflections

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

