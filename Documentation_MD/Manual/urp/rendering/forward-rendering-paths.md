[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/rendering/forward-rendering-paths.html)
  * [中文](/cn/current/Manual/urp/rendering/forward-rendering-paths.html)
  * [日本語](/ja/current/Manual/urp/rendering/forward-rendering-paths.html)
  * [한국어](/kr/current/Manual/urp/rendering/forward-rendering-paths.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/rendering/forward-rendering-paths.html)
  * [中文](/cn/current/Manual/urp/rendering/forward-rendering-paths.html)
  * [日本語](/ja/current/Manual/urp/rendering/forward-rendering-paths.html)
  * [한국어](/kr/current/Manual/urp/rendering/forward-rendering-paths.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Get started with URP](../../urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](../../urp/urp-concepts.html)
  * [Rendering paths in URP](../../urp/rendering-paths-landing.html)
  * Forward and Forward+ rendering paths in URP

[](../../urp/rendering-paths-set.html)

Set the rendering path in URP

[](../../urp/rendering/deferred-rendering-path-landing.html)

Deferred rendering path in URP

# Forward and Forward+ rendering paths in URP

The Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../../render-
pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (URP) has the following
forward **rendering paths** The technique that a render pipeline uses to
render graphics. Choosing a different rendering path affects how lighting and
shading are calculated. Some rendering paths are more suited to different
platforms and hardware than others. [More info](../../RenderingPaths.html)  
See in [Glossary](../../Glossary.html#RenderingPath):

  * Forward
  * Forward+

## Forward rendering path

The **Forward rendering** A rendering path that renders each object in one or
more passes, depending on lights that affect the object. Lights themselves are
also treated differently by Forward Rendering, depending on their settings and
intensity. [More info](../../RenderTech-ForwardRendering.html)  
See in [Glossary](../../Glossary.html#ForwardRendering) path is the default
rendering path in URP. Unity lights each **GameObject** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) in turn, and there’s a limit
to the number of lights that can affect each GameObject.

## Forward+ rendering path

The Forward+ rendering path is similar to the Forward rendering path, but
there’s no limit to the number of lights that can affect each GameObject.
There’s still a limit on the number of lights visible per-camera.

Using the Forward+ rendering path reduces the number of lights Unity
calculates for each GameObject. Unity divides the screen into tiles, then
identifies which lights affect which tiles. When Unity calculates the lighting
for a GameObject, it uses only the lights that affect the tile the GameObject
is in.

![An example of the Lighting Complexity Debug Draw Mode using the Forward+
rendering path. Each grid square is a tile, and each value represents the
number of lights affecting the tile.](../../../uploads/urp/lighting-
complexity.png) An example of the Lighting Complexity [Debug Draw
Mode](../../GIVis.html) using the Forward+ rendering path. Each grid square is
a tile, and each value represents the number of lights affecting the tile.

Unity ignores the following settings if you select the Forward+ rendering
path:

  * **Additional Lights** in the URP Asset.
  * **Main Light** in the URP Asset.
  * **Additional Lights** > **Per Object Limit** in the URP Asset.
  * **Reflection Probes** > **Probe Blending** in the Lighting window.

## Additional resources

  * [Light limits in URP](../lighting/light-limits-in-urp.html)
  * [Introduction to rendering paths in URP](../rendering-paths-introduction-urp.html)

[](../../urp/rendering-paths-set.html)

Set the rendering path in URP

[](../../urp/rendering/deferred-rendering-path-landing.html)

Deferred rendering path in URP

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

