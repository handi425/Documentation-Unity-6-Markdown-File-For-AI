[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/svt-cache-management.html)
  * [中文](/cn/current/Manual/svt-cache-management.html)
  * [日本語](/ja/current/Manual/svt-cache-management.html)
  * [한국어](/kr/current/Manual/svt-cache-management.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/svt-cache-management.html)
  * [中文](/cn/current/Manual/svt-cache-management.html)
  * [日本語](/ja/current/Manual/svt-cache-management.html)
  * [한국어](/kr/current/Manual/svt-cache-management.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Streaming Virtual Texturing](svt-streaming-virtual-texturing.html)
  * Cache Management for Virtual Texturing

[](svt-use-in-shader-graph.html)

Using Streaming Virtual Texturing in Shader Graph

[](svt-marking-textures.html)

Marking textures as "Virtual Texturing Only"

# Cache Management for Virtual Texturing

This feature is experimental and not ready for production use. The feature and
documentation might be changed or removed in the future.

Virtual Texturing uses fixed-size texture caches in GPU memory. There is one
cache per graphics format. You can configure the default size of a cache and
overwrite its default size.

The Streaming Virtual Texturing (SVT) system also uses one CPU cache in main
memory to store tile pages. A tile page contains multiple tiles that the SVT
system reads all together from disk into the CPU cache. This increases the
speed of the read throughput from disk on slower drives. When the Virtual
Texturing system requests a tile, it reads the page that contains that tile.
It’s likely that the system will request other tiles in that page in the
following frames, so the CPU cache retains that page to avoid another read
from disk. The larger the CPU cache size, the longer Virtual Texturing can
keep the page in main memory.

Virtual Texturing allocates the GPU cache of a given graphics format when it
renders a Material that has a Texture Stack with a texture that uses that
format. You can configure the cache size (in MB) on the [HDRP
Asset](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-
definition@latest/index.html?subfolder=/manual/HDRP-Asset.html), which allows
you to have different configurations for each quality level.

![](../uploads/Main/svt-cache-management01.png)

You can also use the
[`VirtualTexturing.Streaming.SetGPUCacheSettings`](../ScriptReference/Rendering.VirtualTexturing.Streaming.SetGPUCacheSettings.html)
method to set the cache size in a script.

You can change the cache size, but this results in resource-heavy CPU and GPU
operations, and blocks both the main thread and the render thread. The length
of time it takes to change the cache size depends on the size and number of
caches. To avoid noticeable freezes or stuttering, you should change the cache
size at a time when frame rate is less important (such as when loading a
level).

The main factors that influence the optimal size of a given cache are the
output screen resolution, and the number of layers in each Texture Stack that
use that graphics format. The number of Materials in the **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and the resolution of the textures
don’t influence the optimal size as much. For a full HD screen resolution on
the highest quality setting, the combined total GPU cache size is typically
700MB.

An issue called “cache thrashing” occurs when the size of a cache is too low
to accommodate its contents, and it must load and unload tiles in the same
frame. To prevent cache thrashing, the Virtual Texturing system automatically
reduces texture quality as needed. It monitors cache usage, and automatically
manages a mipmap bias for the Texture Stack sampling in **pixel** The smallest
unit in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) **shaders** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). If the cache fills up, the mipmap
bias increases. This ensures that the Virtual Texturing system requests lower
resolution tiles, which saves space in the cache, allowing it to contain all
of the requested tiles.

If your textures look blurry, try increasing the size of your caches. If the
caches are already large enough to render frames at the highest quality,
further increasing the cache size means that the cache can retain tiles for
longer before evicting them. This can reduce unwanted effects such as texture
popping when you move or turn the **Camera** A component which creates an
image of a particular viewpoint in your scene. The output is either drawn to
the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), because tiles that were recently
visible are more likely to still be in the cache.

[](svt-use-in-shader-graph.html)

Using Streaming Virtual Texturing in Shader Graph

[](svt-marking-textures.html)

Marking textures as "Virtual Texturing Only"

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

