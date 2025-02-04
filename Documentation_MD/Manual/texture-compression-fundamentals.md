[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/texture-compression-fundamentals.html)
  * [中文](/cn/current/Manual/texture-compression-fundamentals.html)
  * [日本語](/ja/current/Manual/texture-compression-fundamentals.html)
  * [한국어](/kr/current/Manual/texture-compression-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/texture-compression-fundamentals.html)
  * [中文](/cn/current/Manual/texture-compression-fundamentals.html)
  * [日本語](/ja/current/Manual/texture-compression-fundamentals.html)
  * [한국어](/kr/current/Manual/texture-compression-fundamentals.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Get started with textures](textures-getting-started.html)
  * [Texture formats in memory](texture-compression-formats.html)
  * GPU texture format fundamentals

[](texture-compression-formats.html)

Texture formats in memory

[](texture-choose-format-by-platform.html)

Choose a GPU texture format by platform

# GPU texture format fundamentals

The Unity Editor can import texture source files with a number of common
formats, such as JPEG or PNG. However, GPUs do not use these formats at
runtime; instead, they use different, specialized formats that are optimized
for memory usage and speed of sampling operations.

You can configure the texture **compression** A method of storing data that
reduces the amount of storage space it requires. See [Texture
Compression](class-TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) format for a texture asset in its
import settings. When you add a texture asset to your project, the Unity
Editor automatically chooses an appropriate compression format for each build
target; however, most platforms support several **texture compression** 3D
Graphics hardware requires Textures to be compressed in specialized formats
which are optimized for fast Texture sampling. [More info](class-
TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) formats.

Texture compression format can affect load times, GPU frame times, memory
usage, visual quality, build size, and compression times; it is therefore
important to understand this subject before you make changes to this setting.

This page contains the following information:

  * Texture compression overview
  * Crunch compression
  * Applying texture compression formats to texture assets

For general information on texture asset import settings, see [Texture import
settings](class-TextureImporter.html). For information on the recommended,
default, and supported texture compression formats for each platform, see
[Recommended, default, and supported texture compression formats, by
platform](class-TextureImporterOverride).

## Texture compression overview

Bits per **pixel** The smallest unit in a computer image. Pixel size depends
on your screen resolution. Pixel lighting is calculated at every screen pixel.
[More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) (bpp) is the amount of storage required
for a single texture pixel. Textures with a lower bpp value have a smaller
size on disk and in memory. A lower bpp value also means that the GPU uses
less memory bandwidth to read the texture pixels. GPU memory bandwidth can
often be a frame rate bottleneck, and thus texture compression helps to avoid
it.

The higher the visual quality of a texture asset, the higher the bits per
pixel; which, consequently, leads to greater build size, loading time, and
runtime memory usage. All texture compression formats are lossy, to some
extent. Uncompressed textures offer the highest quality, but they also have
the highest bits per pixel. Different texture compression formats offer
different trade-offs.

In general, for the best runtime performance and size on disk, for most of
your texture assets, you should choose a texture compression format that is
supported by your target device, and has the fewest bits per pixel for the
visual quality you want.

When you use a texture for a specific purpose, you can change its individual
settings. For example, if you are using a texture with only one channel as a
mask, you might choose the BC4 format to reduce file size but preserve
quality. If you are using some textures for pixel-perfect **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI), you might choose not to compress them.

Choose a format that your target platforms and devices support. When Unity
loads a texture with a compression format that the device does not support, it
decompresses the texture to the default uncompressed format for that platform
and stores the uncompressed copy in memory alongside the original compressed
texture. This increases texture loading time and uses additional memory. When
Unity loads a texture with a compression format that the device supports, the
GPU can use the data without any need for conversion.

## Crunch compression

Crunch is a compression format that works on top of DXT or ETC compression, by
providing additional variable bit rate compression. When Unity loads a Crunch-
compressed texture, it decompresses the texture to DXT or ETC on the CPU, and
then uploads the DXT or ETC compressed texture data to the GPU.

Crunch compression helps the texture use the lowest possible amount of disk
space, but has no effect on runtime memory usage. Crunch textures can take a
long time to compress, but decompression at runtime is fairly fast. You can
adjust how lossy Crunch compression is, to strike a balance between file size
and quality.

If you are particularly concerned about the size of your build and Crunch is
supported on your target platform, consider adding Crunch compression.

## Applying texture compression formats to texture assets

For information about texture import settings and how to set up platform-
specific overrides, see [Texture Import Settings](class-TextureImporter.html).

[](texture-compression-formats.html)

Texture formats in memory

[](texture-choose-format-by-platform.html)

Choose a GPU texture format by platform

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

