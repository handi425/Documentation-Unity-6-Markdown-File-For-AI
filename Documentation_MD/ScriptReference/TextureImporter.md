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

# TextureImporter

class in UnityEditor

/

Inherits from:[AssetImporter](AssetImporter.html)

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

[Switch to Manual](../Manual/class-TextureImporter.html "Go to TextureImporter
Component in the Manual")

### Description

Texture importer lets you modify [Texture2D](Texture2D.html) import settings
from editor scripts.

Settings of this class cover most of the settings exposed in [Texture Import
Settings](../Manual/class-TextureImporter.html). Some settings require you to
use [TextureImporterSettings](TextureImporterSettings.html). Refer to
[TextureImporter.SetTextureSettings](TextureImporter.SetTextureSettings.html)).

### Properties

[allowAlphaSplitting](TextureImporter-allowAlphaSplitting.html)| Allows alpha
splitting on relevant platforms for this texture.  
---|---  
[alphaIsTransparency](TextureImporter-alphaIsTransparency.html)| If the alpha
channel of your texture represents transparency, enable this property to
dilate the color channels of visible texels into fully transparent areas. This
effectively adds padding around transparent areas that prevents filtering
artifacts from forming on their edges. Unity does not support this property
for HDR textures.This property makes the color data of invisible texels
undefined. Disable this property to preserve invisible texels' original color
data.  
[alphaSource](TextureImporter-alphaSource.html)| Select how the alpha of the
imported texture is generated.  
[alphaTestReferenceValue](TextureImporter-alphaTestReferenceValue.html)|
Returns or assigns the alpha test reference value.  
[androidETC2FallbackOverride](TextureImporter-
androidETC2FallbackOverride.html)| ETC2 texture decompression fallback
override on Android devices that don't support ETC2.  
[anisoLevel](TextureImporter-anisoLevel.html)| Anisotropic filtering level of
the texture.  
[borderMipmap](TextureImporter-borderMipmap.html)| Keeps texture borders the
same when generating mipmaps.  
[compressionQuality](TextureImporter-compressionQuality.html)| The quality of
the texture after Crunch compresses it. The range is 0 through 100. A higher
value means a larger, better-quality texture, but a longer compression time
because Crunch needs more time to try different texture encodings.  
[convertToNormalmap](TextureImporter-convertToNormalmap.html)| Convert
heightmap to normal map  
[crunchedCompression](TextureImporter-crunchedCompression.html)| Use crunched
compression when available.  
[fadeout](TextureImporter-fadeout.html)| Fade out mip levels to gray color.  
[filterMode](TextureImporter-filterMode.html)| Filtering mode of the texture.  
[flipGreenChannel](TextureImporter-flipGreenChannel.html)| Indicates whether
to invert the green channel values of a normal map.  
[generateCubemap](TextureImporter-generateCubemap.html)| Cubemap generation
mode.  
[heightmapScale](TextureImporter-heightmapScale.html)| Amount of bumpyness in
the heightmap.  
[ignoreMipmapLimit](TextureImporter-ignoreMipmapLimit.html)| Enable this flag
for textures that should ignore mipmap limit settings.  
[ignorePngGamma](TextureImporter-ignorePngGamma.html)| Ignore the Gamma
attribute in PNG files. This property does not effect other file formats.  
[isReadable](TextureImporter-isReadable.html)| Whether Unity stores an
additional copy of the imported texture's pixel data in CPU-addressable
memory.  
[maxTextureSize](TextureImporter-maxTextureSize.html)| Maximum texture size.  
[mipMapBias](TextureImporter-mipMapBias.html)| Mip map bias of the texture.  
[mipmapEnabled](TextureImporter-mipmapEnabled.html)| Generate Mip Maps.  
[mipmapFadeDistanceEnd](TextureImporter-mipmapFadeDistanceEnd.html)| Mip level
where texture is faded out completely.  
[mipmapFadeDistanceStart](TextureImporter-mipmapFadeDistanceStart.html)| Mip
level where texture begins to fade out.  
[mipmapFilter](TextureImporter-mipmapFilter.html)| Mipmap filtering mode.  
[mipmapLimitGroupName](TextureImporter-mipmapLimitGroupName.html)| Name of the
texture mipmap limit group to which this texture belongs.  
[mipMapsPreserveCoverage](TextureImporter-mipMapsPreserveCoverage.html)|
Enables or disables coverage-preserving alpha mipmapping.  
[normalmapFilter](TextureImporter-normalmapFilter.html)| Normal map filtering
mode.  
[npotScale](TextureImporter-npotScale.html)| Scaling mode for non power of two
textures.  
[qualifiesForSpritePacking](TextureImporter-qualifiesForSpritePacking.html)|
Returns true if this TextureImporter is setup for Sprite packing.  
[secondarySpriteTextures](TextureImporter-secondarySpriteTextures.html)|
Secondary textures for the imported Sprites.  
[spriteBorder](TextureImporter-spriteBorder.html)| Border sizes of the
generated sprites.  
[spriteImportMode](TextureImporter-spriteImportMode.html)| Selects Single or
Manual import mode for Sprite textures.  
[spritePivot](TextureImporter-spritePivot.html)| The point in the Sprite
object's coordinate space where the graphic is located.  
[spritePixelsPerUnit](TextureImporter-spritePixelsPerUnit.html)| The number of
pixels in the sprite that correspond to one unit in world space.  
[sRGBTexture](TextureImporter-sRGBTexture.html)| Whether this texture stores
data in sRGB (also called gamma) color space.  
[streamingMipmaps](TextureImporter-streamingMipmaps.html)| Enable mipmap
streaming for this texture.  
[streamingMipmapsPriority](TextureImporter-streamingMipmapsPriority.html)|
Relative priority for this texture when reducing memory size in order to hit
the memory budget.  
[swizzleA](TextureImporter-swizzleA.html)| Specifies the source for the
texture's alpha color channel data.  
[swizzleB](TextureImporter-swizzleB.html)| Specifies the source for the
texture's blue color channel data.  
[swizzleG](TextureImporter-swizzleG.html)| Specifies the source for the
texture's green color channel data.  
[swizzleR](TextureImporter-swizzleR.html)| Specifies the source for the
texture's red color channel data.  
[textureCompression](TextureImporter-textureCompression.html)| Compression of
imported texture.  
[textureShape](TextureImporter-textureShape.html)| The shape of the imported
texture.  
[textureType](TextureImporter-textureType.html)| Which type of texture are we
dealing with here.  
[vtOnly](TextureImporter-vtOnly.html)| When enabled, this texture can solely
be used in combination with a Texture Stack for Virtual Texturing. When
enabled the texture is not guaranteed to be available as a Texture2D in the
Player (e.g., not accessible from a script). When disabled, the Player
includes the texture both as a Texture2D (e.g., accessible from script) and as
a streamable texture in a Texture Stack.  
[wrapMode](TextureImporter-wrapMode.html)| Texture coordinate wrapping mode.  
[wrapModeU](TextureImporter-wrapModeU.html)| Texture U coordinate wrapping
mode.  
[wrapModeV](TextureImporter-wrapModeV.html)| Texture V coordinate wrapping
mode.  
[wrapModeW](TextureImporter-wrapModeW.html)| Texture W coordinate wrapping
mode for Texture3D.  
  
### Public Methods

[ClearPlatformTextureSettings](TextureImporter.ClearPlatformTextureSettings.html)|
Clears specific target platform settings.  
---|---  
[DoesSourceTextureHaveAlpha](TextureImporter.DoesSourceTextureHaveAlpha.html)|
Allows you to check whether the texture source image has an alpha channel.  
[GetAutomaticFormat](TextureImporter.GetAutomaticFormat.html)| Returns the
TextureImporterFormat that would be automatically chosen for this platform.  
[GetDefaultPlatformTextureSettings](TextureImporter.GetDefaultPlatformTextureSettings.html)|
Gets the default platform specific texture settings.  
[GetPlatformTextureSettings](TextureImporter.GetPlatformTextureSettings.html)|
Gets platform specific texture settings.  
[GetSourceTextureWidthAndHeight](TextureImporter.GetSourceTextureWidthAndHeight.html)|
Gets the source texture's width and height.  
[ReadTextureImportInstructions](TextureImporter.ReadTextureImportInstructions.html)|
Reads the active texture output instructions of this TextureImporter.  
[ReadTextureSettings](TextureImporter.ReadTextureSettings.html)| Read texture
settings into TextureImporterSettings class.  
[SetPlatformTextureSettings](TextureImporter.SetPlatformTextureSettings.html)|
Sets specific target platform settings.  
[SetTextureSettings](TextureImporter.SetTextureSettings.html)| Sets texture
importers settings from TextureImporterSettings class.  
  
### Static Methods

[IsDefaultPlatformTextureFormatValid](TextureImporter.IsDefaultPlatformTextureFormatValid.html)|
Validates TextureImporterFormat based on the type of the current format
(TextureImporterType) and the default platform.  
---|---  
[IsPlatformTextureFormatValid](TextureImporter.IsPlatformTextureFormatValid.html)|
Validates TextureImporterFormat based on a specified import type
(TextureImporterType) and a specified build target (BuildTarget.).  
  
### Inherited Members

### Properties

[assetBundleName](AssetImporter-assetBundleName.html)| Get or set the
AssetBundle name.  
---|---  
[assetBundleVariant](AssetImporter-assetBundleVariant.html)| Get or set the
AssetBundle variant.  
[assetPath](AssetImporter-assetPath.html)| The path name of the asset for this
importer. (Read Only)  
[importSettingsMissing](AssetImporter-importSettingsMissing.html)| The value
is true when no meta file is provided with the imported asset.  
[userData](AssetImporter-userData.html)| Get or set any user data.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[AddRemap](AssetImporter.AddRemap.html)| Map a sub-asset from an imported
asset (such as an FBX file) to an external Asset of the same type.  
---|---  
[GetExternalObjectMap](AssetImporter.GetExternalObjectMap.html)| Gets a copy
of the external object map used by the AssetImporter.  
[RemoveRemap](AssetImporter.RemoveRemap.html)| Removes an item from the map of
external objects.  
[SaveAndReimport](AssetImporter.SaveAndReimport.html)| Save asset importer
settings if asset importer is dirty.  
[SetAssetBundleNameAndVariant](AssetImporter.SetAssetBundleNameAndVariant.html)|
Set the AssetBundle name and variant.  
[SupportsRemappedAssetType](AssetImporter.SupportsRemappedAssetType.html)|
Checks if the AssetImporter supports remapping the given asset type.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[GetAtPath](AssetImporter.GetAtPath.html)| Retrieves the asset importer for
the asset at path.  
---|---  
[GetImportLog](AssetImporter.GetImportLog.html)| Retrieves logs generated
during the import of the asset at path.  
[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

