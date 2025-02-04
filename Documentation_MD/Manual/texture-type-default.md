[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/texture-type-default.html)
  * [中文](/cn/current/Manual/texture-type-default.html)
  * [日本語](/ja/current/Manual/texture-type-default.html)
  * [한국어](/kr/current/Manual/texture-type-default.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/texture-type-default.html)
  * [中文](/cn/current/Manual/texture-type-default.html)
  * [日本語](/ja/current/Manual/texture-type-default.html)
  * [한국어](/kr/current/Manual/texture-type-default.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Textures reference](textures-reference.html)
  * Default texture Import Settings window reference

[](class-TextureImporter.html)

Texture Import Settings window reference

[](texture-type-normal-map.html)

Normal Map texture Import Settings window reference

# Default texture Import Settings window reference

The **Default** texture type is the most common texture type and provides
access to most of the properties for texture importing. With this texture
type, you can also change the [Texture Shape](class-
TextureImporter.html#textureshape).

For more information about the Texture Importer window, see [texture
type](class-TextureImporter.html).

## Properties

**Property** | **Description**  
---|---  
**sRGB (Color Texture)** | Indicates whether the texture is in gamma space. Enable this property for non-HDR color textures such as albedo and specular color. If the texture stores information that you need the exact value for, like smoothness or metalness values, disable this property.  
**Alpha Source** | Specifies how Unity generates the alpha value for the texture asset from the texture source file.  
**None** | The texture asset doesn’t have an alpha channel, whether or not the texture source file has one.  
**Input Texture Alpha** | Unity applies the alpha channel from the texture source file to the texture asset, if the texture source file has an alpha channel.  
**From Gray Scale** | Unity generates the alpha channel for the texture asset from the average values the texture source files RGB channels.  
**Alpha is Transparency** | Indicates whether to dilate the color channels. This helps to avoid filtering artifacts on the edges of the alpha channel if the alpha channel represents transparency.  
**Remove PSD Matte** | Indicates whether to apply special processing for Photoshop files that use transparency (blending color pixels with white).  
**Note** : This is only available for PSD files.  
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
**Virtual Texture Only** | Indicates whether to use the texture solely in combination with a Texture Stack for Virtual Texturing. When enabled, the texture is not guaranteed to be available as a Texture2D in the Player (that is, not accessible from a script). When disabled, the Player includes the texture both as a Texture2D (accessible from script) and as a streamable texture in a Texture Stack.  
**Generate Mipmap** | Indicates whether to generate a [mipmap](texture-mipmaps-introduction.html) for this texture.  
**Mipmap Limit** | Disable this option to use all mipmap levels, regardless of the Mipmap Limit settings in the **Quality** menu. This property only appears if you set **Texture Shape** to **2D** or **2D Array**. Other texture shapes always use all mipmap levels.  
**Mipmap Limit Group** | Select the Mipmap Limit group this texture should be part of. The default option is **None (Use Global Mipmap Limit)**. This property only appears if you set **Texture Shape** to **2D** or **2D Array**. Other texture shapes always use all mipmap levels.  
**Stream Mipmap Levels** | Indicates whether to use [Mipmap Streaming](TextureStreaming.html) for this texture.  
  
This property is visible only when Generate Mipmap is set to true.  
**Priority** | The priority of the textures in the [Mipmap Streaming system](TextureStreaming.html). Unity uses this setting in two ways:  
  
• To determine which textures to prioritize when assigning resources.  
• As a mipmap bias value when choosing a mipmap level that fits in the memory
budget. For example, with a priority of 2, the mipmap streaming system tries
to use a mipmap two levels higher than textures with a priority of 0.  
  
Positive numbers give higher priority. Valid values range from –128 to 127.  
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

[](class-TextureImporter.html)

Texture Import Settings window reference

[](texture-type-normal-map.html)

Normal Map texture Import Settings window reference

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

