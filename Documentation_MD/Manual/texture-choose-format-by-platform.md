[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/texture-choose-format-by-platform.html)
  * [中文](/cn/current/Manual/texture-choose-format-by-platform.html)
  * [日本語](/ja/current/Manual/texture-choose-format-by-platform.html)
  * [한국어](/kr/current/Manual/texture-choose-format-by-platform.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/texture-choose-format-by-platform.html)
  * [中文](/cn/current/Manual/texture-choose-format-by-platform.html)
  * [日本語](/ja/current/Manual/texture-choose-format-by-platform.html)
  * [한국어](/kr/current/Manual/texture-choose-format-by-platform.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Get started with textures](textures-getting-started.html)
  * [Texture formats in memory](texture-compression-formats.html)
  * Choose a GPU texture format by platform

[](texture-compression-fundamentals.html)

GPU texture format fundamentals

[](texture-formats-reference.html)

GPU texture formats reference

# Choose a GPU texture format by platform

## Desktop

For devices with DirectX 11 or better class GPUs, where support for BC7 and
BC6H formats is guaranteed to be available, the recommended choice of
**compression** A method of storing data that reduces the amount of storage
space it requires. See [Texture Compression](class-TextureImporterOverride),
[Animation Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) formats is: RGB textures - DXT1
at four bits/**pixel** The smallest unit in a computer image. Pixel size
depends on your screen resolution. Pixel lighting is calculated at every
screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel). RGBA textures - BC7 (higher quality,
slower to compress) or DXT5 (faster to compress), both at eight bits/pixel.
HDR textures - BC6H at eight bits/pixel. If you need to support DirectX 10
class GPUs on PC (NVIDIA GPUs before 2010, AMD before 2009, Intel before
2012), then DXT5 instead of BC7 would be preferred, since these GPUs do not
support BC7 nor BC6H.

See the [Supported texture formats reference table](texture-formats-
reference.html) for detailed information about all supported formats.

## iOS and tvOS

For Apple devices that use the A8 chip (2014) or above, ASTC is the
recommended **texture format** A file format for handling textures during
real-time rendering by 3D graphics hardware, such as a graphics card or mobile
device. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat) for RGB and RGBA textures. This
format allows you to choose between texture quality and size on a granular
level: all the way from eight bits/pixel (4x4 block size) down to 0.89
bits/pixel (12x12 block size). If support for older devices is needed, or you
want additional Crunch compression, then Apple devices support ETC/ETC2
formats starting with A7 chip (2013). For even older devices, PVRTC is the
format to use. On iOS you can configure the default texture format in the
[Player Settings](iphone.html)Settings that let you set various player-
specific options for the final game built by Unity. [More info](class-
PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings). PVRTC gives you the broadest
possible compatibility. ASTC is preferred, but is not supported on A7 devices
(the very first Metal-enabled devices) and will be unpacked at runtime.

See the [Supported texture formats reference table](texture-formats-
reference.html) for detailed information about all supported formats.

## Android

Texture format support on Android is complicated. You might need to build
several application versions with different [sub-targets](android-
BuildProcess.html).

You can select the default format in [Player Settings](class-
PlayerSettingsAndroid.html#Rendering). Your options are ASTC, ETC2 and ETC
(ETC1 for RGB, ETC2 for RGBA). See [Texture compression settings](android-
requirements-and-compatibility.html#texture-compression) for more details on
how the different settings interact.

For LDR RGB and RGBA textures, most modern Android GPUs that support OpenGL ES
3.1 or Vulkan also support ASTC format, including: Qualcomm GPUs since Adreno
4xx / Snapdragon 415 (2015), ARM GPUs since Mali T624 (2012), NVIDIA GPUs
since Tegra K1 (2014), PowerVR GPUs since GX6250 (2014).

If you need support for older devices, or you want additional Crunch
compression, then all GPUs that run Vulkan or OpenGL ES 3.0 support the ETC2
format. The resulting image quality is quite high, and it supports one- to
four-component texture data. For even older devices, usually only ETC format
is available. The drawback is that there is no direct alpha channel support.
For **Sprites** A 2D graphic objects. If you are used to working in 3D,
Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite), Unity offers an option to use ETC1
compression by splitting a texture into two ETC1 textures: one for RGB, one
for alpha. To enable this, enable the Android-specific [Split Alpha
Channel](class-TextureImporter.html#splitalpha) option for the Texture when
importing a [Sprite Atlas](sprite/atlas/atlas-landing.html)A utility that
packs several sprite textures tightly together within a single texture known
as an atlas. [More info](sprite/atlas/v2/v2-landing.html)  
See in [Glossary](Glossary.html#SpriteAtlas). The sprite **shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) samples both textures and combines
them into the final result.

For older Android devices that don’t support the ASTC format, the texture is
decompressed into an uncompressed RGBA 32-bit format. This increases memory
usage and can slow down the decompression performed on the CPU.

For **HDR** high dynamic range  
See in [Glossary](Glossary.html#HDR) textures, ASTC HDR is the only compressed
format available on Android devices. ASTC HDR requires Vulkan or
[GL_KHR_texture_compression_astc_hdr](https://opengles.gpuinfo.org/listreports.php?extension=GL_KHR_texture_compression_astc_hdr)
support. ASTC is the most flexible format. If a device doesn’t support ASTC
HDR the texture is decompressed at runtime to RGB9e5 or RGBA Half, depending
on alpha channel usage.

For devices that don’t support ASTC HDR, all devices running Vulkan, Metal, or
OpenGL ES 3.0 support RGB9e5, which is suitable for textures without an alpha
channel. If an alpha channel or even wider support is needed, use RGBA Half.
This takes twice as much memory as RGB9e5.

If you want to distribute your application to Google Play, it’s best practice
to use [texture compression targeting](android-distribution-google-
play.html#texture-compression-targeting).

See the [Supported texture formats reference table](texture-formats-
reference.html) for detailed information about all supported formats.

[](texture-compression-fundamentals.html)

GPU texture format fundamentals

[](texture-formats-reference.html)

GPU texture formats reference

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

