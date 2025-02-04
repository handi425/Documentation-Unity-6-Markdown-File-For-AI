[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/texture-formats-reference.html)
  * [中文](/cn/current/Manual/texture-formats-reference.html)
  * [日本語](/ja/current/Manual/texture-formats-reference.html)
  * [한국어](/kr/current/Manual/texture-formats-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/texture-formats-reference.html)
  * [中文](/cn/current/Manual/texture-formats-reference.html)
  * [日本語](/ja/current/Manual/texture-formats-reference.html)
  * [한국어](/kr/current/Manual/texture-formats-reference.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Get started with textures](textures-getting-started.html)
  * [Texture formats in memory](texture-compression-formats.html)
  * GPU texture formats reference

[](texture-choose-format-by-platform.html)

Choose a GPU texture format by platform

[](texture-mipmaps-introduction.html)

Mipmaps

# GPU texture formats reference

## Default texture formats, by platform

The following table shows the default formats used for each platform.

**Platform** | **Color model** | **None** | **Normal quality (default)** | **High quality** | **Low quality (higher performance)**  
---|---|---|---|---|---  
**Windows, Linux, macOS** | RGB | RGB 24 bit | RGB Compressed DXT1 | RGB(A) Compressed BC7 | RGB Compressed DXT1  
| RGBA | RGBA 32 bit | RGBA Compressed DXT5 | RGB(A) Compressed BC7 | RGBA Compressed DXT5  
| **HDR** high dynamic range  
See in [Glossary](Glossary.html#HDR) | RGBA Half | RGB Compressed BC6H | RGB Compressed BC6H | RGB Compressed BC6H  
****WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser.
The Unity Web build option allows Unity to publish content as JavaScript
programs which use HTML5 technologies and the WebGL rendering API to run Unity
content in a web browser. [More info](webgl.html)  
See in [Glossary](Glossary.html#WebGL)** ([configurable](webgl-texture-compression.html)) | RGB | RGB 24 bit | RGB Compressed DXT1 | RGB Compressed DXT1 | RGB Compressed DXT1  
| RGBA | RGBA 32 bit | RGBA Compressed DXT5 | RGBA Compressed DXT5 | RGBA Compressed DXT5  
**Android** ([configurable](android-requirements-and-compatibility.html#texture-compression)) | RGB | RGB 24 bit | RGBA Compressed ASTC 6x6 block  
RGB Compressed ETC2  
RGB Compressed ETC | RGBA Compressed ASTC 4x4 block  
RGB Compressed ETC2  
RGB Compressed ETC | RGBA Compressed ASTC 8x8 block  
RGB Compressed ETC2  
RGB Compressed ETC  
| RGBA | RGBA 32 bit | RGBA Compressed ASTC 6x6 block  
RGBA Compressed ETC2 | RGBA Compressed ASTC 4x4 block  
RGBA Compressed ETC2 | RGBA Compressed ASTC 8x8 block  
RGBA Compressed ETC2  
**iOS** ([configurable](iphone.html)) | RGB | RGB 24 bit | RGBA Compressed ASTC 6x6 block  
RGB Compressed PVRTC 4 bits | RGBA Compressed ASTC 4x4 block  
RGB Compressed PVRTC 4 bits | RGBA Compressed ASTC 8x8 block  
RGB Compressed PVRTC 2 bits  
| RGBA | RGBA 32 bit | RGBA Compressed ASTC 6x6 block  
RGBA Compressed PVRTC 4 bits | RGBA Compressed ASTC 4x4 block  
RGBA Compressed PVRTC 4 bits | RGBA Compressed ASTC 8x8 block  
RGBA Compressed PVRTC 2 bits  
**tvOS** | RGB | RGB 24 bit | RGBA Compressed ASTC 6x6 block | RGBA Compressed ASTC 4x4 block | RGBA Compressed ASTC 8x8 block  
| RGBA | RGBA 32 bit | RGBA Compressed ASTC 6x6 block | RGBA Compressed ASTC 4x4 block | RGBA Compressed ASTC 8x8 block  
**Default** | RGBA | RGBA 32 bit | RGBA 16 bit | RGBA 16 bit | RGBA 16 bit  
  
## Texture formats, by quality

The table below shows each format available in Unity, and their quality
details.

****Texture format** A file format for handling textures during real-time
rendering by 3D graphics hardware, such as a graphics card or mobile device.
[More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat)** | **Description** | **Channels** | **Quality** | **Bits per**pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel)** | **Size of 1024x1024 texture, in MB**  
---|---|---|---|---|---  
**RGB(A) Compressed BC7** | Compressed RGB or RGBA | RGB or RGBA | High | 8 | 1  
**RGBA Crunched DXT5** | Compressed RGBA, with additional on-disk Crunch **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) | RGBA | Low to medium | Variable | Variable  
**RGBA 64 bit** | Uncompressed RGBA, very high precision | RGBA | Very high | 64 | 8  
**RGBA 32 bit** | Uncompressed RGBA | RGBA | High | 32 | 4  
**RGBA 16 bit** | Quantized RGBA | RGBA | Medium | 16 | 2  
**RGB Compressed DXT1** | Compressed RGB (also known as BC1) | RGB | Medium | 4 | 0.5  
**RGB Crunched DXT1** | Compressed RGB, with additional on-disk Crunch compression | RGB | Low to medium | Variable | Variable  
**RGB 48 bit** | Uncompressed RGB, very high precision. Converted to RGBA 64 bit for the GPU | RGB | Very high | 48 disk, 64 GPU | 6 disk, 8 GPU  
**RGB 24 bit** | Uncompressed RGB. Converted to RGBA 32 bit for the GPU | RGB | High | 24 disk, 32 GPU | 3 disk, 4 GPU  
**RGB 16 bit** | Quantized RGB | RGB | Medium | 16 | 2  
**RG Compressed BC5** | Compressed two channel (RG) | RG | High | 8 | 1  
**RG 32 bit** | Uncompressed two channel (RG), very high precision | RG | Very high | 32 | 4  
**R Compressed BC4** | Compressed single channel (R) | R | High | 4 | 0.5  
**R 8** | Uncompressed single channel (R) | R | High | 8 | 1  
**R 16 bit** | Uncompressed single channel (R), very high precision | R | Very high | 16 | 2  
**Alpha 8** | Uncompressed single channel (A) | A | High | 8 | 1  
**RGBA Half** | HDR, half-precision (FP16) RGBA, –64k to +64k range | RGBA | High | 64 | 8  
**RGB Compressed BC6H** | HDR, compressed RGB, 0 to +64k range | RGB | High | 8 | 1  
**RGB9e5 32 Bit Shared Exponent Float** | HDR, quantized RGB, 0 to +64k range | RGB | Medium | 32 | 4  
**RGB(A) Compressed ASTC** | Compressed RGB or RGBA, size & quality dependent on block size | RGB or RGBA | Low to high | 12x12: 0.89, 10x10: 1.28, 8x8: 2, 6x6: 3.56, 5x5: 5.12, 4x4: 8 | 12x12: 0.11, 10x10: 0.16, 8x8: 0.25, 6x6: 0.45, 5x5: 0.64, 4x4: 1.0  
**RGBA Compressed ETC2** | Compressed RGBA | RGBA | Medium | 8 | 1  
**RGBA Crunched ETC2** | Compressed RGBA, with additional on-disk Crunch compression | RGBA | Low to medium | Variable | Variable  
**RGB + 1-bit Alpha Compressed ETC2 4 bits** | Compressed RGBA, with alpha values fully opaque or fully transparent | RGBA | Medium | 4 | 0.5  
**RGBA Compressed PVRTC 4 bits** | Compressed RGBA, texture required to be square | RGBA | Medium | 4 | 0.5  
**RGBA Compressed PVRTC 2 bits** | Compressed RGBA, texture required to be square | RGBA | Low | 2 | 0.25  
**RGB Compressed ETC2** | Compressed RGB | RGB | Medium | 4 | 0.5  
**RGB Compressed ETC** | Compressed RGB | RGB | Low | 4 | 0.5  
**RGB Crunched ETC** | Compressed RGB, with additional on-disk Crunch compression | RGB | Low | Variable | Variable  
**RGB Compressed PVRTC 4 bits** | Compressed RGB, texture required to be square | RGB | Medium | 4 | 0.5  
**RGB Compressed PVRTC 2 bits** | Compressed RGB, texture required to be square | RGB | Low | 2 | 0.25  
**RG Compressed EAC 8 bit** | Compressed two channel (RG) | RG | High | 8 | 1  
**R Compressed EAC 4 bit** | Compressed single channel (R) | R | High | 4 | 0.5  
**RGB(A) Compressed ASTC HDR** | HDR, compressed RGB or RGBA, size & quality dependent on block size | RGB or RGBA | Low to High | 12x12: 0.89, 10x10: 1.28, 8x8: 2, 6x6: 3.56, 5x5: 5.12, 4x4: 8 | 12x12: 0.11, 10x10: 0.16, 8x8: 0.25, 6x6: 0.45, 5x5: 0.64, 4x4: 1.0  
  
## Supported texture formats, by platform

The table below shows each texture format available in Unity, and the
platforms that support them.

**Texture format** | **Windows** | **macOS** | **Linux** | **Android** | **iOS & tvOS** | **Web (Desktop Browsers)** | **Web (iOS and Android browser)**  
---|---|---|---|---|---|---|---  
**RGB(A) Compressed BC7** | yes (1) | yes (1) | yes | no | no | **yes (1)** | no  
**RGBA Compressed DXT5** | yes | yes | yes | no (3) | no | partial (2) | no  
**RGBA Crunched DXT5** | yes | yes | yes | no (3) | no | partial (2) | no  
**RGBA 64 bit** | yes | yes | yes | partial (4) | yes | no | no  
**RGBA 32 bit** | yes | yes | yes | yes | yes | yes | yes  
**RGBA 16 bit** | yes | yes | yes | yes | yes | yes | yes  
**RGB Compressed DXT1** | yes | yes | yes | no (3) | no | partial (2) | no  
**RGB Crunched DXT1** | yes | yes | yes | no (3) | no | partial (2) | no  
**RGB 48 bit** | yes | yes | yes | partial (4) | yes | no | no  
**RGB 24 bit** | yes | yes | yes | yes | yes | yes | yes  
**RGB 16 bit** | yes | yes | yes | yes | yes | yes | yes  
**RG Compressed BC5** | yes | yes | yes | no | no | **yes** | no  
**RG 32 bit** | yes | yes | yes | partial (4) | yes | no | no  
**R Compressed BC4** | yes | yes | yes | no | no | **yes** | no  
**R 8** | yes | yes | yes | yes | yes | yes | yes  
**R 16 bit** | yes | yes | yes | partial (4) | partial (4) | **yes (10)** | yes (10)  
**Alpha 8** | yes | yes | yes | yes | yes | yes | yes  
**RGBA Half** | yes | yes | yes | partial (7) | yes | partial (7) | partial (7)  
**RGB Compressed BC6H** | yes (1) | yes (1) | yes | no | no | **yes (1)** | no  
**RGB9e5 32 Bit Shared Exponent Float** | yes | yes | yes | yes | yes | yes | yes)  
**RGB(A) Compressed ASTC** | no | no | no | partial (5) | yes (6) | no | yes (6 and 9)  
**RGBA Compressed ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGBA Crunched ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGB + 1-bit Alpha Compressed ETC2 4 bits** | no | no | no | partial (9) | yes | no | yes  
**RGBA Compressed PVRTC 4 bits** | no | no | no | no (8) | yes | no | no  
**RGBA Compressed PVRTC 2 bits** | no | no | no | no (8) | yes | no | no  
**RGB Compressed ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGB Compressed ETC** | no | no | no | yes | yes | no | yes  
**RGB Crunched ETC** | no | no | no | yes | yes | no | yes  
**RGB Compressed PVRTC 4 bits** | no | no | no | no (8) | yes | no | no  
**RGB Compressed PVRTC 2 bits** | no | no | no | no (8) | yes | no | no  
**RG Compressed EAC 8 bit** | no | no | no | partial (9) | yes | no | yes  
**R Compressed EAC 4 bit** | no | no | no | partial (9) | yes | no | yes  
**RGB(A) Compressed ASTC HDR** | no | no | no | partial (7) | partial (7) | no | partial (7)  
  
**Notes:**

  1. Except on pre-DX11 level GPUs, or macOS when using WebGL or OpenGL. When not supported, BC6H textures get decompressed to RGBA Half, and BC7 get decompressed to RGBA32 at load time.
  2. With [linear rendering](color-spaces-landing.html) on web browsers that don’t support sRGB DXT, textures are decompressed to RGBA32 at load time.
  3. Except on Android devices with NVIDIA Tegra GPUs; these do support DXT/BC formats.
  4. Requires GL_EXT_texture_norm16 or corresponding Vulkan capability on Android.
  5. Requires Vulkan or [GL_KHR_texture_compression_astc_ldr](https://opengles.gpuinfo.org/listreports.php?extension=GL_KHR_texture_compression_astc_ldr) OpenGL ES extension.
  6. Except on Apple A7 chip devices (2013).
  7. Android: requires [GL_KHR_texture_compression_astc_hdr](https://opengles.gpuinfo.org/listreports.php?extension=GL_KHR_texture_compression_astc_hdr) extension. iOS: requires A13 or later chip (2019). WebGL: requires [WEBGL_compressed_texture_astc](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_compressed_texture_astc) extension and [HDR profile](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_compressed_texture_astc/getSupportedProfiles). When not supported, the texture is decompressed to RGB9E5 format, losing the alpha channel.
  8. Except on Android devices with Imagination PowerVR GPUs; these do support PVRTC formats.
  9. Requires [WEBGL_compressed_texture_astc](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_compressed_texture_astc) extension.
  10. Requires [EXT_texture_norm16](https://developer.mozilla.org/en-US/docs/Web/API/EXT_texture_norm16) extension and WebGL 2.

## Supported texture formats in Web

The following table provides the supported texture formats for the Web
platform.

**Format** | **Description**  
---|---  
**ASTC** | Adaptive Scalable **Texture Compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) (ASTC) is an advanced
lossy texture compression format. Widely used for mobile browsers / devices.  
**DXT** | Also known as S3 Texture Compression (S3TC), DXT is mainly used for desktop browsers and devices.  
**ETC2** | Ericsson Texture Compression (ETC) is an older lossy texture compression format, lower quality than ASTC, used for mobile browsers / devices.  
  
## Additional resources:

  * [Texture compression in Web](webgl-texture-compression.html)
  * [Texture Compression format in Android](android-requirements-and-compatibility.html#texture-compression)

TextureImporterOverride

[](texture-choose-format-by-platform.html)

Choose a GPU texture format by platform

[](texture-mipmaps-introduction.html)

Mipmaps

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

