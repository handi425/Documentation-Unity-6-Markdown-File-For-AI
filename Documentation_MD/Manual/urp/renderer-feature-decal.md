[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-feature-decal.html)
  * [中文](/cn/current/Manual/urp/renderer-feature-decal.html)
  * [日本語](/ja/current/Manual/urp/renderer-feature-decal.html)
  * [한국어](/kr/current/Manual/urp/renderer-feature-decal.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-feature-decal.html)
  * [中文](/cn/current/Manual/urp/renderer-feature-decal.html)
  * [日本語](/ja/current/Manual/urp/renderer-feature-decal.html)
  * [한국어](/kr/current/Manual/urp/renderer-feature-decal.html)

  * [Visual effects](../visual-effects.html)
  * [Decals and projectors](../visual-effects-decals.html)
  * [Decals in URP](../urp/renderer-feature-decal-landing.html)
  * Introduction to decals in URP

[](../urp/renderer-feature-decal-landing.html)

Decals in URP

[](../urp/renderer-feature-decal-create.html)

Create a decal via a Decal Renderer Feature in URP

# Introduction to decals in URP

## Decal Renderer Feature

With the Decal Renderer Feature, Unity can project specific Materials (decals)
onto other objects in the **scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene). The decals interact with the
scene’s lighting and wrap around Meshes.

![Sample scene without decals](../../uploads/urp/decal/decal-sample-
without.png)  
_Sample scene without decals_

![Sample scene with decals](../../uploads/urp/decal/decal-sample-with.png)  
_Sample scene with decals. The decals hide the seams between materials and add
artistic details._

For examples of how to use Decals, refer to the [Decals samples in URP Package
Samples](package-sample-urp-package-samples.html#decals).

### Limitations

This feature has the following limitations:

  * The decal projection does not work on transparent surfaces.

## Decal Projector

The Decal Projector component lets Unity project decals onto other objects in
the scene. A Decal Projector component must use a Material with the [Decal
Shader Graph](decal-shader.html) assigned (`Shader Graphs/Decal`).

## Performance

Decals do not support the **SRP Batcher** by design because they use Material
property blocks. To reduce the number of draw calls, decals can be batched
together using GPU instancing. If the decals in your scene use the same
Material, and if the Material has the **Enable GPU Instancing** property
turned on, Unity instances the Materials and reduces the number of draw calls.

To reduce the number of Materials necessary for decals, put multiple decal
textures into one texture (atlas). Use the UV offset properties on the decal
projector to determine which part of the atlas to display.

The following image shows an example of a decal atlas.

![Decal Atlas](../../uploads/urp/decal/decal-atlas.png)  
_left: decal atlas with four decals. Right: a decal projector is projecting
one of them. If the decal Material has GPU instancing enabled, any instance of
the four decals is rendered in a single instanced draw call._

[](../urp/renderer-feature-decal-landing.html)

Decals in URP

[](../urp/renderer-feature-decal-create.html)

Create a decal via a Decal Renderer Feature in URP

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

