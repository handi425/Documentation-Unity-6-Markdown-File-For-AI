[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Lightmaps-TechnicalInformation.html)
  * [中文](/cn/current/Manual/Lightmaps-TechnicalInformation.html)
  * [日本語](/ja/current/Manual/Lightmaps-TechnicalInformation.html)
  * [한국어](/kr/current/Manual/Lightmaps-TechnicalInformation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Lightmaps-TechnicalInformation.html)
  * [中文](/cn/current/Manual/Lightmaps-TechnicalInformation.html)
  * [日本語](/ja/current/Manual/Lightmaps-TechnicalInformation.html)
  * [한국어](/kr/current/Manual/Lightmaps-TechnicalInformation.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Lighting data](Lightmap-data-landing.html)
  * Lightmap data format

[](GICache.html)

Global Illumination (GI) cache

[](LightProbes-TechnicalInformation.html)

Light Probe data format

# Lightmap data format

Unity stores **lightmaps** A pre-rendered texture that contains the effects of
light sources on static objects in the scene. Lightmaps are overlaid on top of
scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) with different compressions and
encoding schemes, depending on the target platform and the compression setting
in the Lighting Window.

## Encoding schemes

Unity projects can use two techniques to encode baked light intensity ranges
into low dynamic range textures when this is needed:

  * **RGBM encoding**. RGBM encoding stores a color in the **RGB** channels and a multiplier (**M**) in the alpha channel. The range of RGBM lightmaps goes from 0 to 34.49(52.2) in linear space, and from 0 to 5 in gamma space.

  * **Double Low Dynamic Range (dLDR) encoding**. dLDR encoding is used on mobile platforms by simply mapping a range of [0, 2] to [0, 1]. Baked light intensities that are above a value of 2 will be clamped. The decoding value is computed by multiplying the value from the lightmap texture by 2 when gamma space is used, or 4.59482(22.2) when linear space is used. Some platforms store lightmaps as dLDR because their hardware compression produces poor-looking artifacts when using RGBM.

When Linear Color Space is used, the lightmap texture is marked as sRGB and
the final value used by the **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) (after sampling and decoding) will be
in Linear Color Space. When Gamma Color Space is used, the final value will be
in Gamma Color Space.

**Note** : When encoding is used, the values stored in the lightmaps (GPU
texture memory) are always in Gamma Color Space.

The **Decode Lightmap** shader function from the _UnityCG.cginc_ shader
include file handles the decoding of lightmap values after the value is read
from the lightmap texture in a shader.

## HDR lightmap support

You can use HDR lightmaps on Windows, Mac, Linux, iOS, tvOS, and Android. To
control the encoding/compression of the lightmaps for these platforms, go to
**Edit** > **Project Settings** > **Player** > **Other Settings** > **Lightmap
Encoding**.

Choosing **High Quality** will enable **HDR** high dynamic range  
See in [Glossary](Glossary.html#HDR) lightmap support, whereas **Normal
Quality** will switch to using **RGBM** encoding. **Low Quality** will switch
to **dLDR** encoding on mobile platforms, on other platforms it’s equivalent
to **Normal Quality**.

When lightmap **Compression** A method of storing data that reduces the amount
of storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) is enabled in the Lighting
Window, the lightmaps will be compressed using the **BC6H** compression format
on desktop and console platforms. For mobile platforms, Unity selects the HDR
format according to the table below.

## Advantages of High Quality (BC6H) lightmaps

  * HDR lightmaps don’t use any encoding scheme to encode lightmap values, so the supported range is only limited by the 16-bit floating point **texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat) that goes from 0 to 65504.

  * BC6H format quality is superior to DXT5 + RGBM format encoding, and it doesn’t produce any of the color banding artifacts that RGBM encoding has. 

  * Shaders that need to sample HDR lightmaps are a few ALU instructions shorter because there is no need to decode the sampled values. 

  * BC6H format has the same GPU memory requirements as DXT5.

Here is the list of encoding schemes and their **texture compression** 3D
Graphics hardware requires Textures to be compressed in specialized formats
which are optimized for fast Texture sampling. [More info](class-
TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) formats per target
platform:

**Target platform** | **Encoding** | **Compression - size (bits per pixel)**  
---|---|---  
Standalone(PC, Mac, Linux) | RGBM / HDR | DXT5 / BC6H - 8 bpp  
**WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser.
The Unity Web build option allows Unity to publish content as JavaScript
programs which use HTML5 technologies and the WebGL rendering API to run Unity
content in a web browser. [More info](webgl.html)  
See in [Glossary](Glossary.html#WebGL) 2.0 | RGBM / RGBM / HDR | DXT5 - 8 bpp  
iOS ASTC (1) | dLDR / RGBM / HDR | ASTC - 3.56 bpp / ASTC - 3.56 bpp / RGB9E5 - 32 bpp  
iOS PVRTC | dLDR / RGBM / HDR | PVRTC RGB - 4 bpp / ETC2 RGBA - 8 bpp / RGB9E5 - 32 bpp  
tvOS | dLDR / RGBM / HDR | ASTC - 3.56 bpp / ASTC - 3.56 bpp / RGB9E5 - 32 bpp  
Android ASTC (2) | dLDR / RGBM / HDR | ASTC - 3.56 bpp / ASTC - 3.56 bpp / ASTC HDR - 3.56 bpp  
Android ETC2 | dLDR / RGBM / HDR | ETC2 RGB - 4 bpp / ETC2 RGBA - 8 bpp / ASTC HDR - 3.56 bpp  
Android ETC | dLDR / RGBM / HDR | ETC1 RGB - 4 bpp / ETC2 RGBA - 8 bpp / ASTC HDR - 3.56 bpp  
  
[1] The texture compression format used for lightmaps on **iOS** depends on
the _Texture compression format_ setting in the [Player
Settings](iphone.html).

[2] The texture compression format used for lightmaps on **Android** depends
on [Player Settings](class-PlayerSettingsAndroid.html#Rendering) and [Build
Settings](android-build-settings.html). See [Texture compression
settings](android-requirements-and-compatibility.html#texture-compression) for
more details on how these settings interact.

## Precomputed real-time Global Illumination (GI)

The inputs to the GI system have a different range and encoding to the output.
Surface albedo is 8-bit unsigned integer RGB in gamma space and emission is
16-bit floating point RGB in linear space. For advice on providing custom
inputs using a meta pass, see documentation on [Lightmapping and
shaders](MetaPass.html).

The irradiance output texture is stored using the RGB9E5 shared exponent
floating point format if the graphics hardware supports it, or RGBM with a
range of 5 as fallback. The range of RGB9E5 lightmaps is [0, 65408]. For
details on the RGB9E5 format, see [Khronos.org:
EXT_texture_shared_exponent](https://www.khronos.org/registry/OpenGL/extensions/EXT/EXT_texture_shared_exponent.txt).

See also:

  * [Texture Importer Override](class-TextureImporterOverride)
  * [Texture Types](class-TextureImporter.html)
  * [Global Illumination](lighting-window.html)A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination)

* * *

  * 2019–04–26 Page amended 

  * Baked lightmaps added in Unity [2017.2](https://docs.unity3d.com/2017.2/Documentation/Manual/30_search.html?q=newin20172) NewIn20172

  * HDR lightmap support added in Unity [2017.3](https://docs.unity3d.com/2017.3/Documentation/Manual/30_search.html?q=newin20173) NewIn20173

  * Lightmap encoding settings for mobile platform added in Unity [2019.1](https://docs.unity3d.com/2019.1/Documentation/Manual/30_search.html?q=newin20191) NewIn20191

  * Update lightmap texture compression formats for Android and iOS

[](GICache.html)

Global Illumination (GI) cache

[](LightProbes-TechnicalInformation.html)

Light Probe data format

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

