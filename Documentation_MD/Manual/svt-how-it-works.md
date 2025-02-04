[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/svt-how-it-works.html)
  * [中文](/cn/current/Manual/svt-how-it-works.html)
  * [日本語](/ja/current/Manual/svt-how-it-works.html)
  * [한국어](/kr/current/Manual/svt-how-it-works.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/svt-how-it-works.html)
  * [中文](/cn/current/Manual/svt-how-it-works.html)
  * [日本語](/ja/current/Manual/svt-how-it-works.html)
  * [한국어](/kr/current/Manual/svt-how-it-works.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Streaming Virtual Texturing](svt-streaming-virtual-texturing.html)
  * How Streaming Virtual Texturing works

[](svt-requirements-compatibility.html)

Streaming Virtual Texturing requirements and compatibility

[](svt-enable-in-project.html)

Enabling Streaming Virtual Texturing in your project

# How Streaming Virtual Texturing works

This feature is experimental and not ready for production use. The feature and
documentation might be changed or removed in the future.

The Streaming Virtual Texturing system (SVT) divides textures into tiles.

At runtime, when SVT samples a texture, it does the following:

  * It samples an indirection texture, calculates the non-virtual UVs, and samples a cache texture with these UVs.
  * It translates the virtual UVs to a tile ID, and binds an additional render target that receives these tile IDs. The CPU copies this render target back to main memory asynchronously, and processes it on a separate thread, to create requests for the asynchronous read manager to load these tiles from disk into a cache of GPU memory (if they are not already present).

The cost of these runtime operations means that it’s more efficient to group
textures together, and to sample them all at the same time. This process is
called stacking textures. A group of textures that are sampled at the same
time with the same UV coordinates is called a Texture Stack.

SVT issues requests for tiles during frame rendering, so it can take from
milliseconds to seconds until the requested tiles load into the GPU cache, and
in some cases they might not load into the GPU cache at all. If the requested
tile does not load into the cache, SVT has an automatic fallback mechanism: it
samples tiles from a higher mipmap level until the requested tile is in the
cache. This results in a lower **level of detail** The _Level Of Detail_ (LOD)
technique is an optimization that reduces the number of triangles that Unity
has to render for a GameObject when its distance from the Camera increases.
[More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#levelofdetail) until the tile fully loads.

## SVT in the High Definition Render Pipeline debug view

The High Definition **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (HDRP) debug view shows how
many neighboring screen **pixels** The smallest unit in a computer image.
Pixel size depends on your screen resolution. Pixel lighting is calculated at
every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) request the same tile.

To open the HDRP debug view, navigate to the Unity top menu and select
**Window > Analysis > Rendering Debugger > Rendering**. To view the debug data
for SVT, set **Fullscreen Debug Mode** to **RequestedVirtualTextureTiles**.

![The debug view uses distinct colors for every tile ID.](../uploads/Main/svt-
how-it-works02.png) The debug view uses distinct colors for every tile ID.

Pixels that sample the same texture tile have the same colour. The color hue
(green, red, and so on) represents the mipmap level to which a tile belongs.
For example, all yellowish tiles belong to mipmap 1 of the texture.

[](svt-requirements-compatibility.html)

Streaming Virtual Texturing requirements and compatibility

[](svt-enable-in-project.html)

Enabling Streaming Virtual Texturing in your project

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

