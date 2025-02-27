[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/texture-type-lightmap.html)
  * [中文](/cn/current/Manual/texture-type-lightmap.html)
  * [日本語](/ja/current/Manual/texture-type-lightmap.html)
  * [한국어](/kr/current/Manual/texture-type-lightmap.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/texture-type-lightmap.html)
  * [中文](/cn/current/Manual/texture-type-lightmap.html)
  * [日本語](/ja/current/Manual/texture-type-lightmap.html)
  * [한국어](/kr/current/Manual/texture-type-lightmap.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Textures reference](textures-reference.html)
  * Lightmap texture Import Settings window reference

[](texture-type-cookie.html)

Cookie texture Import Settings window reference

[](texture-type-directional-lightmap.html)

Lightmap texture Import Settings window reference

# Lightmap texture Import Settings window reference

The **Lightmap** texture type formats the texture asset so it’s suitable to
use as a [Lightmap](class-LightmapParameters.html)A pre-rendered texture that
contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap). This option enables encoding into a
specific format (RGBM or dLDR depending on the platform) and a **post-
processing** A process that improves product visuals by applying filters and
effects before the image appears on screen. You can use post-processing
effects to simulate physical camera and film properties, for example Bloom and
Depth of Field. [More info](PostProcessingOverview.html) post processing,
postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) step on texture data (a push-
pull dilation pass). Unity locks **Texture Shape** to **2D** for this texture
type. For more information, see [Texture Shape](class-
TextureImporter.html#textureshape).

## Properties

**Property** | **Description**  
---|---  
**Non Power of 2** | Specifies how Unity scales the dimension size if the texture source file has a non-power of two (NPOT) dimension size. For more information on NPOT dimension sizes, see [Importing Textures](ImportingTextures.html).  
**None** |  Texture dimension size stays the same.  
**To nearest** | Scales the Texture to the nearest power-of-two dimension size at import time. For example, a 257x511 px Texture is scaled to 256x512 px. Note that PVRTC formats require Textures to be square (that is width equal to height), so the final dimension size is upscaled to 512x512 px.  
**To larger** |  Scales the Texture to the power-of-two dimension size of the largest dimension size value at import time. For example, a 257x511 px Texture is scaled to 512x512 px.  
**To smaller** | Scales the Texture to the power-of-two dimension size of the smallest dimension size value at import time. For example, a 257x511 px Texture is scaled to 256x256 px.  
**Read/Write** | Indicates whether to access the texture data from scripts using [Texture2D.SetPixels](../ScriptReference/Texture2D.SetPixels.html), [Texture2D.GetPixels](../ScriptReference/Texture2D.GetPixels.html) and other [Texture](../ScriptReference/Texture.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) methods. Internally, Unity uses a
copy of the Texture data for script access, which doubles the amount of memory
required for the Texture. This property is therefore disabled by default, and
you should enable it only if you require script access. For more information,
see [Texture.isReadable](../ScriptReference/Texture-isReadable.html).  
**Generate Mipmap** | Indicates whether to generate a [mipmap](texture-mipmaps-introduction.html) for this texture.  
**Mipmap Limit** | Disable this option to use all mipmap levels, regardless of the Mipmap Limit settings in the **Quality** menu. This property only appears if you set **Texture Shape** to **2D** or **2D Array**. Other texture shapes always use all mipmap levels.  
**Mipmap Limit Group** | Select the Mipmap Limit group this texture should be part of. The default option is **None (Use Global Mipmap Limit)**. This property only appears if you set **Texture Shape** to **2D** or **2D Array**. Other texture shapes always use all mipmap levels.  
**Mipmap Filtering** | Specifies the method Unity uses to filter mipmap levels and optimize image quality.  
  
This property is visible only when Generate Mipmap is set to true.  
**Box** | Makes mipmap levels smoother as they decrease in dimension size.  
**Kaiser** | Runs a sharpening algorithm on mipmap levels as they decrease in dimension size. Use this option if your textures are too blurry when far away. The algorithm is of the Kaiser Window type. For more information, see [Wikipedia](https://en.wikipedia.org/wiki/Kaiser_window).  
**Preserve Coverage** | Indicates whether the alpha channel in generated mipmaps preserves coverage during the alpha text. For more information, see [TextureImporterSettings.mipMapsPreserveCoverage](../ScriptReference/TextureImporterSettings-mipMapsPreserveCoverage.html).  
  
This property is visible only when Generate Mipmap is set to true.  
**Alpha Cutoff** | The reference value that controls the mipmap coverage during the alpha test.  
  
This property is visible only when Preserve Coverage is set to true.  
**Replicate Border** | Indicates whether to stop colors bleeding out to the edge of the lower mipmap levels. This is useful for light cookies.  
  
This property is visible only when Generate Mipmap is set to true.  
**Fadeout to Gray** | Indicates whether mipmap levels should fade to gray as the mipmap levels progress. This is useful for detail maps. The left-most scroll is the first mipmap level to begin fading out. The right-most scroll defines the mipmap level where the texture is completely grayed out.  
  
This property is visible only when Generate Mipmap is set to true.  
**Ignore PNG Gamma** | Indicates whether to ignore the gamma attribute in PNG files.  
  
This option is only visible if the texture source file is a PNG.  
**Swizzle** | Specifies how to order the texture source file color channel data.  
**Wrap Mode** | Specifies how the texture behaves when it tiles.  
**Repeat** | Repeats the texture in tiles.  
**Clamp** | Stretches the texture’s edges.  
**Mirror** | Mirrors the texture at every integer boundary to create a repeating pattern.  
**Mirror Once** | Mirrors the texture once, then clamps it to edge pixels.  
**Note** : Some mobile devices don’t support Mirror Once. In this case, Unity
uses Mirror instead.  
**Per-axis** | Provides options you can use to individually control how Unity wraps textures on the U and V axis.  
**Filter Mode** | Specifies how Unity filters the texture when the texture stretches during 3D transformations.  
**Point (no filter)** | The texture appears blocky up close.  
**Bilinear** | The texture appears blurry up close.  
**Trilinear** | Like **Bilinear** , but the texture also blurs between the different mipmap levels.  
**Aniso Level** | Controls the texture quality when you view the texture at a steep angle. Anisotropic filtering is good for floor and ground Textures but is resource intensive. For more information, see [Importing textures](ImportingTextures.html).  
  
In addition, you can use the [Platform-specific overrides](class-
TextureImporter.html#platform) panel to set default options and overrides for
specific platforms.

[](texture-type-cookie.html)

Cookie texture Import Settings window reference

[](texture-type-directional-lightmap.html)

Lightmap texture Import Settings window reference

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

