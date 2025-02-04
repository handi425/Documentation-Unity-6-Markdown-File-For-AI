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

# Texture2D

class in UnityEngine

/

Inherits from:[Texture](Texture.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Class that represents textures in C# code.

Use this class to create textures, or to modify existing [texture
assets](../Manual/Textures.html).  
  
The [ImageConversion](ImageConversion.html) class provides extension methods
to this class that handle image encoding functionality. For details on those
methods, see the [ImageConversion](ImageConversion.html) documentation.  
  
Do not assume that the texture will be created and available in
[Awake](MonoBehaviour.Awake.html). All texture uploads are synchronized on the
Main thread at [Start](MonoBehaviour.Start.html). Perform texture operations
in [Start](MonoBehaviour.Start.html).

### Static Properties

[blackTexture](Texture2D-blackTexture.html)| Gets a small Texture with all
black pixels.  
---|---  
[grayTexture](Texture2D-grayTexture.html)| Gets a small Texture with all gray
pixels.  
[linearGrayTexture](Texture2D-linearGrayTexture.html)| Gets a small Texture
with all gray pixels.  
[normalTexture](Texture2D-normalTexture.html)| Gets a small Texture with
pixels that represent surface normal vectors at a neutral position.  
[redTexture](Texture2D-redTexture.html)| Gets a small Texture with all red
pixels.  
[whiteTexture](Texture2D-whiteTexture.html)| Gets a small Texture with all
white pixels.  
  
### Properties

[activeMipmapLimit](Texture2D-activeMipmapLimit.html)| The number of high
resolution mipmap levels from the texture that Unity doesn't upload to the
GPU. (Read Only)  
---|---  
[alphaIsTransparency](Texture2D-alphaIsTransparency.html)| Indicates whether
this texture was imported with TextureImporter.alphaIsTransparency enabled.
This setting is available only in the Editor scripts. Note that changing this
setting will have no effect; it must be enabled in TextureImporter instead.  
[calculatedMipmapLevel](Texture2D-calculatedMipmapLevel.html)| The mipmap
level calculated by the streaming system, which takes into account the
streaming Cameras and the location of the objects containing this Texture.
This is unaffected by requestedMipmapLevel or minimumMipmapLevel.  
[desiredMipmapLevel](Texture2D-desiredMipmapLevel.html)| The mipmap level that
the streaming system would load before memory budgets are applied.  
[format](Texture2D-format.html)| The format of the pixel data in the texture
(Read Only).  
[ignoreMipmapLimit](Texture2D-ignoreMipmapLimit.html)| This property causes a
texture to ignore all texture mipmap limit settings.  
[loadedMipmapLevel](Texture2D-loadedMipmapLevel.html)| The mipmap level that
is currently loaded by the streaming system.  
[loadingMipmapLevel](Texture2D-loadingMipmapLevel.html)| The mipmap level that
the mipmap streaming system is in the process of loading.  
[minimumMipmapLevel](Texture2D-minimumMipmapLevel.html)| Restricts the mipmap
streaming system to a minimum mip level for this Texture.  
[mipmapLimitGroup](Texture2D-mipmapLimitGroup.html)| The name of the texture
mipmap limit group that this texture is associated with. (Read Only)  
[requestedMipmapLevel](Texture2D-requestedMipmapLevel.html)| The mipmap level
to load.  
[streamingMipmaps](Texture2D-streamingMipmaps.html)| Determines whether mipmap
streaming is enabled for this Texture.  
[streamingMipmapsPriority](Texture2D-streamingMipmapsPriority.html)| Sets the
relative priority for this Texture when reducing memory size to fit within the
memory budget.  
[vtOnly](Texture2D-vtOnly.html)| Returns true if the VTOnly checkbox was
checked when the texture was imported; otherwise returns false. For additional
information, see TextureImporter.vtOnly.  
  
### Constructors

[Texture2D](Texture2D-ctor.html)| Create a new empty texture.  
---|---  
  
### Public Methods

[Apply](Texture2D.Apply.html)| Copies changes you've made in a CPU texture to
the GPU.  
---|---  
[ClearMinimumMipmapLevel](Texture2D.ClearMinimumMipmapLevel.html)| Resets the
minimumMipmapLevel field.  
[ClearRequestedMipmapLevel](Texture2D.ClearRequestedMipmapLevel.html)| Resets
the requestedMipmapLevel field.  
[Compress](Texture2D.Compress.html)| Compress texture at runtime to DXT/BCn or
ETC formats.  
[CopyPixels](Texture2D.CopyPixels.html)| Copies pixel data from another
texture on the CPU.  
[GetPixel](Texture2D.GetPixel.html)| Gets the pixel color at coordinates (x,
y).  
[GetPixelBilinear](Texture2D.GetPixelBilinear.html)| Gets the filtered pixel
color at the normalized coordinates (u, v).  
[GetPixelData](Texture2D.GetPixelData.html)| Gets the raw data from a texture.  
[GetPixels](Texture2D.GetPixels.html)| Gets the pixel color data for a mipmap
level as Color structs.  
[GetPixels32](Texture2D.GetPixels32.html)| Gets the pixel color data for a
mipmap level as Color32 structs.  
[GetRawTextureData](Texture2D.GetRawTextureData.html)| Gets the raw data from
a texture, as an array that points to memory.  
[IsRequestedMipmapLevelLoaded](Texture2D.IsRequestedMipmapLevelLoaded.html)|
Checks to see whether the mipmap level set by requestedMipmapLevel has
finished loading.  
[LoadRawTextureData](Texture2D.LoadRawTextureData.html)| Sets the raw data of
an entire texture in CPU memory.  
[PackTextures](Texture2D.PackTextures.html)| Packs multiple Textures into a
texture atlas.  
[ReadPixels](Texture2D.ReadPixels.html)| Reads pixels from the current render
target and writes them to a texture.  
[Reinitialize](Texture2D.Reinitialize.html)| Reinitializes a Texture2D, making
it possible for you to replace width, height, textureformat, and
graphicsformat data for that texture.  
[SetPixel](Texture2D.SetPixel.html)| Sets the pixel color at coordinates
(x,y).  
[SetPixelData](Texture2D.SetPixelData.html)| Sets the raw data of an entire
mipmap level directly in CPU memory.  
[SetPixels](Texture2D.SetPixels.html)| Sets the pixel colors of an entire
mipmap level.  
[SetPixels32](Texture2D.SetPixels32.html)| Sets the pixel colors of an entire
mipmap level.  
[UpdateExternalTexture](Texture2D.UpdateExternalTexture.html)| Updates Unity
texture to use different native texture object.  
  
### Static Methods

[CreateExternalTexture](Texture2D.CreateExternalTexture.html)| Creates a Unity
Texture out of an externally created native texture object.  
---|---  
[GenerateAtlas](Texture2D.GenerateAtlas.html)| Packs a set of rectangles into
a square atlas, with optional padding between rectangles.  
  
### Inherited Members

### Static Properties

[allowThreadedTextureCreation](Texture-allowThreadedTextureCreation.html)|
Allow Unity internals to perform Texture creation on any thread (rather than
the dedicated render thread).  
---|---  
[currentTextureMemory](Texture-currentTextureMemory.html)| The amount of
memory that all Textures in the scene use.  
[desiredTextureMemory](Texture-desiredTextureMemory.html)| The total size of
the Textures, in bytes, that Unity loads if there were no other constraints.
Before Unity loads any Textures, it applies the memory budget which reduces
the loaded Texture resolution if the Texture sizes exceed its value. The
desiredTextureMemory value takes into account the mipmap levels that Unity has
requested or that you have set manually.For example, if Unity does not load a
Texture at full resolution because it is far away or its requested mipmap
level is greater than 0, Unity reduces the desiredTextureMemory value to match
the total memory needed.The desiredTextureMemory value can be greater than the
Texture.targetTextureMemory value.  
[GenerateAllMips](Texture.GenerateAllMips.html)| Can be used with Texture
constructors that take a mip count to indicate that all mips should be
generated. The value of this field is -1.  
[nonStreamingTextureCount](Texture-nonStreamingTextureCount.html)| The number
of non-streaming Textures in the scene. This includes instances of Texture2D
and CubeMap Textures. This does not include any other Texture types, or 2D and
CubeMap Textures that Unity creates internally.  
[nonStreamingTextureMemory](Texture-nonStreamingTextureMemory.html)| The
amount of memory Unity allocates for non-streaming Textures in the scene. This
only includes instances of Texture2D and CubeMap Textures. This does not
include any other Texture types, or 2D and CubeMap Textures that Unity creates
internally.  
[streamingMipmapUploadCount](Texture-streamingMipmapUploadCount.html)| How
many times has a Texture been uploaded due to Texture mipmap streaming.  
[streamingRendererCount](Texture-streamingRendererCount.html)| Number of
renderers registered with the Texture streaming system.  
[streamingTextureCount](Texture-streamingTextureCount.html)| Number of
streaming Textures.  
[streamingTextureDiscardUnusedMips](Texture-
streamingTextureDiscardUnusedMips.html)| This property forces the streaming
Texture system to discard all unused mipmaps instead of caching them until the
Texture memory budget is exceeded. This is useful when you profile or write
tests to keep a predictable set of Textures in memory.  
[streamingTextureForceLoadAll](Texture-streamingTextureForceLoadAll.html)|
Force streaming Textures to load all mipmap levels.  
[streamingTextureLoadingCount](Texture-streamingTextureLoadingCount.html)|
Number of streaming Textures with mipmaps currently loading.  
[streamingTexturePendingLoadCount](Texture-
streamingTexturePendingLoadCount.html)| Number of streaming Textures with
outstanding mipmaps to be loaded.  
[targetTextureMemory](Texture-targetTextureMemory.html)| The total amount of
Texture memory that Unity allocates to the Textures in the scene after it
applies the memory budget and finishes loading Textures.
`targetTextureMemory`also takes mipmap streaming settings into account. This
value only includes instances of Texture2D and CubeMap Textures. This value
does not include any other Texture types, or 2D and CubeMap Textures that
Unity creates internally.  
[totalTextureMemory](Texture-totalTextureMemory.html)| The total amount of
Texture memory that Unity would use if it loads all Textures at mipmap level
0.This is a theoretical value that does not take into account any input from
the streaming system or any other input, for example when you set
the`Texture2D.requestedMipmapLevel` manually.To see a Texture memory value
that takes inputs into account, use
`desiredTextureMemory`.`totalTextureMemory` only includes instances of
Texture2D and CubeMap Textures. This value does not include any other Texture
types, or 2D and CubeMap Textures that Unity creates internally.  
  
### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
[anisoLevel](Texture-anisoLevel.html)| Defines the anisotropic filtering level
of the Texture.  
[dimension](Texture-dimension.html)| Dimensionality (type) of the Texture
(Read Only).  
[filterMode](Texture-filterMode.html)| Filtering mode of the Texture.  
[graphicsFormat](Texture-graphicsFormat.html)| Returns the GraphicsFormat
format or color format of a Texture object.  
[graphicsTexture](Texture-graphicsTexture.html)|  GraphicsTexture that
represents the texture resource uploaded to the graphics device (Read Only).  
[height](Texture-height.html)| Height of the Texture in pixels (Read Only).  
[imageContentsHash](Texture-imageContentsHash.html)| The hash value of the
Texture.  
[isDataSRGB](Texture-isDataSRGB.html)| Returns true if the texture pixel data
is in sRGB color space (Read Only).  
[isReadable](Texture-isReadable.html)| Whether Unity stores an additional copy
of this texture's pixel data in CPU-addressable memory.  
[mipMapBias](Texture-mipMapBias.html)| The mipmap bias of the Texture.  
[mipmapCount](Texture-mipmapCount.html)| How many mipmap levels are in this
Texture (Read Only).  
[updateCount](Texture-updateCount.html)| This counter is incremented when the
Texture is updated.  
[width](Texture-width.html)| Width of the Texture in pixels (Read Only).  
[wrapMode](Texture-wrapMode.html)| Texture coordinate wrapping mode.  
[wrapModeU](Texture-wrapModeU.html)| Texture U coordinate wrapping mode.  
[wrapModeV](Texture-wrapModeV.html)| Texture V coordinate wrapping mode.  
[wrapModeW](Texture-wrapModeW.html)| Texture W coordinate wrapping mode for
Texture3D.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
[GetNativeTexturePtr](Texture.GetNativeTexturePtr.html)| Retrieve a native
(underlying graphics API) pointer to the Texture resource.  
[IncrementUpdateCount](Texture.IncrementUpdateCount.html)| Increment the
update counter.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
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
[SetGlobalAnisotropicFilteringLimits](Texture.SetGlobalAnisotropicFilteringLimits.html)|
Sets Anisotropic limits.  
[SetStreamingTextureMaterialDebugProperties](Texture.SetStreamingTextureMaterialDebugProperties.html)|
This function sets mipmap streaming debug properties on all materials known by
the mipmap streaming system.  
  
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

