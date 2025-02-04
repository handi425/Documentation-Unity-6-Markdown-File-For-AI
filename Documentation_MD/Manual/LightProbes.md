[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightProbes.html)
  * [中文](/cn/current/Manual/LightProbes.html)
  * [日本語](/ja/current/Manual/LightProbes.html)
  * [한국어](/kr/current/Manual/LightProbes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightProbes.html)
  * [中文](/cn/current/Manual/LightProbes.html)
  * [日本語](/ja/current/Manual/LightProbes.html)
  * [한국어](/kr/current/Manual/LightProbes.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating indirect light with Light Probes](LightProbes-landing.html)
  * Light Probes

[](LightProbes-landing.html)

Precalculating indirect light with Light Probes

[](LightProbes-MovingObjects.html)

Light Probes and moving GameObjects

# Light Probes

**Light Probes** provide a way to capture and use information about light that
is passing through the empty space in your **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

Similar to **lightmaps** A pre-rendered texture that contains the effects of
light sources on static objects in the scene. Lightmaps are overlaid on top of
scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), light probes store “baked”
information about lighting in your scene. The difference is that while
lightmaps store lighting information about light hitting the _surfaces_ in
your scene, light probes store information about light passing through _empty
space_ in your scene.

Light Probes are positions in the scene where the light is measured (probed)
during the bake. At runtime, the indirect light that hits dynamic
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) is approximated using the values
from the nearest Light Probes to that object.

![An extremely simple scene showing light probes placed around two
cubes](../uploads/Main/LightProbes-0.png) An extremely simple scene showing
light probes placed around two cubes

Light Probes have two main uses:

The primary use of light probes is to provide high quality lighting (including
indirect bounced light) on moving objects in your scene.

The secondary use of light probes is to provide the lighting information for
static scenery when that scenery is using Unity’s **LOD system**.

When using light probes for either of these two distinct purposes, many of the
techniques you need to use are the same. It’s important to understand how
light probes work so that you can choose where to place your probes in the
scene.

## Additional resources

  * [Adaptive Probe Volumes (APV) in URP](urp/probevolumes.html)

[](LightProbes-landing.html)

Precalculating indirect light with Light Probes

[](LightProbes-MovingObjects.html)

Light Probes and moving GameObjects

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

