[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# TextureImporterSettings

class in UnityEditor

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Stores settings of a [TextureImporter](TextureImporter.html).

Additional resources: [TextureImporter](TextureImporter.html).

### Properties

[alphaIsTransparency](TextureImporterSettings-alphaIsTransparency.html)| If
the alpha channel of your texture represents transparency, enable this
property to dilate the color channels of visible texels into fully transparent
areas. This effectively adds padding around transparent areas that prevents
filtering artifacts from forming on their edges. Unity does not support this
property for HDR textures.This property makes the color data of invisible
texels undefined. Disable this property to preserve invisible texels' original
color data.  
---|---  
[alphaSource](TextureImporterSettings-alphaSource.html)| Select how the alpha
of the imported texture is generated.  
[alphaTestReferenceValue](TextureImporterSettings-
alphaTestReferenceValue.html)| Returns or assigns the alpha test reference
value.  
[aniso](TextureImporterSettings-aniso.html)| Anisotropic filtering level of
the texture.  
[borderMipmap](TextureImporterSettings-borderMipmap.html)| Enable this to
avoid colors seeping out to the edge of the lower Mip levels. Used for light
cookies.  
[convertToNormalMap](TextureImporterSettings-convertToNormalMap.html)| Convert
heightmap to normal map?  
[cubemapConvolution](TextureImporterSettings-cubemapConvolution.html)|
Convolution mode.  
[fadeOut](TextureImporterSettings-fadeOut.html)| Fade out mip levels to gray
color?  
[filterMode](TextureImporterSettings-filterMode.html)| Filtering mode of the
texture.  
[flipbookColumns](TextureImporterSettings-flipbookColumns.html)| The number of
columns in the source image for a Texture2DArray or Texture3D.  
[flipbookRows](TextureImporterSettings-flipbookRows.html)| The number of rows
in the source image for a Texture2DArray or Texture3D.  
[flipGreenChannel](TextureImporterSettings-flipGreenChannel.html)| Indicates
whether to invert the green channel values of a normal map.  
[generateCubemap](TextureImporterSettings-generateCubemap.html)| Cubemap
generation mode.  
[heightmapScale](TextureImporterSettings-heightmapScale.html)| Amount of
bumpyness in the heightmap.  
[ignoreMipmapLimit](TextureImporterSettings-ignoreMipmapLimit.html)| Enable
this flag for textures that should ignore mipmap limit settings.  
[ignorePngGamma](TextureImporterSettings-ignorePngGamma.html)| Ignore the
Gamma attribute in PNG files. This property does not effect other file
formats.  
[mipmapBias](TextureImporterSettings-mipmapBias.html)| Mipmap bias of the
texture.  
[mipmapEnabled](TextureImporterSettings-mipmapEnabled.html)| Generate mipmaps
for the texture?  
[mipmapFadeDistanceEnd](TextureImporterSettings-mipmapFadeDistanceEnd.html)|
Mip level where texture is faded out to gray completely.  
[mipmapFadeDistanceStart](TextureImporterSettings-
mipmapFadeDistanceStart.html)| Mip level where texture begins to fade out to
gray.  
[mipmapFilter](TextureImporterSettings-mipmapFilter.html)| Mipmap filtering
mode.  
[mipMapsPreserveCoverage](TextureImporterSettings-
mipMapsPreserveCoverage.html)| Enables or disables coverage-preserving alpha
mipmapping.  
[normalMapFilter](TextureImporterSettings-normalMapFilter.html)| Normal map
filtering mode.  
[npotScale](TextureImporterSettings-npotScale.html)| Scaling mode for non
power of two textures.  
[readable](TextureImporterSettings-readable.html)| Is texture data readable
from scripts.  
[singleChannelComponent](TextureImporterSettings-singleChannelComponent.html)|
Color or Alpha component Single Channel Textures uses.  
[spriteAlignment](TextureImporterSettings-spriteAlignment.html)| Edge-relative
alignment of the sprite graphic.  
[spriteBorder](TextureImporterSettings-spriteBorder.html)| Border sizes of the
generated sprites.  
[spriteExtrude](TextureImporterSettings-spriteExtrude.html)| The number of
blank pixels to leave between the edge of the graphic and the mesh.  
[spriteGenerateFallbackPhysicsShape](TextureImporterSettings-
spriteGenerateFallbackPhysicsShape.html)| Generates a default physics shape
for a Sprite if a physics shape has not been set by the user.  
[spriteMeshType](TextureImporterSettings-spriteMeshType.html)|  SpriteMeshType
defines the type of Mesh that TextureImporter generates for a Sprite.  
[spriteMode](TextureImporterSettings-spriteMode.html)| Sprite texture import
mode.  
[spritePivot](TextureImporterSettings-spritePivot.html)| Pivot point of the
Sprite relative to its graphic's rectangle.  
[spritePixelsPerUnit](TextureImporterSettings-spritePixelsPerUnit.html)| The
number of pixels in the sprite that correspond to one unit in world space.  
[spriteTessellationDetail](TextureImporterSettings-
spriteTessellationDetail.html)| The tessellation detail to be used for
generating the mesh for the associated sprite if the SpriteMode is set to
Single. For Multiple sprites, use the SpriteEditor to specify the value per
sprite. Valid values are in the range [0-1], with higher values generating a
tighter mesh. A default of -1 will allow Unity to determine the value
automatically.  
[sRGBTexture](TextureImporterSettings-sRGBTexture.html)| Whether this texture
stores data in sRGB (also called gamma) color space.  
[streamingMipmaps](TextureImporterSettings-streamingMipmaps.html)| Enable
mipmap streaming for this texture.  
[streamingMipmapsPriority](TextureImporterSettings-
streamingMipmapsPriority.html)| Relative priority for this texture when
reducing memory size in order to hit the memory budget.  
[swizzleA](TextureImporterSettings-swizzleA.html)| Specifies the source for
the texture's alpha color channel data.  
[swizzleB](TextureImporterSettings-swizzleB.html)| Specifies the source for
the texture's blue color channel data.  
[swizzleG](TextureImporterSettings-swizzleG.html)| Specifies the source for
the texture's green color channel data.  
[swizzleR](TextureImporterSettings-swizzleR.html)| Specifies the source for
the texture's red color channel data.  
[textureShape](TextureImporterSettings-textureShape.html)| The shape of the
imported texture.  
[textureType](TextureImporterSettings-textureType.html)| Which type of texture
are we dealing with here.  
[vtOnly](TextureImporterSettings-vtOnly.html)| Enable if the texture is
purposed solely for use with a Texture Stack for Virtual Texturing.  
[wrapMode](TextureImporterSettings-wrapMode.html)| Texture coordinate wrapping
mode.  
[wrapModeU](TextureImporterSettings-wrapModeU.html)| Texture U coordinate
wrapping mode.  
[wrapModeV](TextureImporterSettings-wrapModeV.html)| Texture V coordinate
wrapping mode.  
[wrapModeW](TextureImporterSettings-wrapModeW.html)| Texture W coordinate
wrapping mode for Texture3D.  
  
### Public Methods

[ApplyTextureType](TextureImporterSettings.ApplyTextureType.html)| Configure
parameters to import a texture for a purpose of type, as described here.  
---|---  
[CopyTo](TextureImporterSettings.CopyTo.html)| Copy parameters into another
TextureImporterSettings object.  
  
### Static Methods

[Equal](TextureImporterSettings.Equal.html)| Test texture importer settings
for equality.  
---|---  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

