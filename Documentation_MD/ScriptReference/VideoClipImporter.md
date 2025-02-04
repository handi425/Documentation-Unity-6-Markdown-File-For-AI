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

# VideoClipImporter

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

[ ]()

### Description

VideoClipImporter lets you modify [VideoClip](Video.VideoClip.html) import
settings from Editor scripts.

See the **Movie File Format Support Notes** section in the
[VideoPlayer](Video.VideoPlayer.html) class documentation for supported movie
file formats and encoding guidelines.

### Properties

[defaultTargetSettings](VideoClipImporter-defaultTargetSettings.html)| Default
values for the platform-specific import settings.  
---|---  
[deinterlaceMode](VideoClipImporter-deinterlaceMode.html)| Images are
deinterlaced during transcode. This tells the importer how to interpret fields
in the source, if any.  
[flipHorizontal](VideoClipImporter-flipHorizontal.html)| Apply a horizontal
flip during import.  
[flipVertical](VideoClipImporter-flipVertical.html)| Apply a vertical flip
during import.  
[frameCount](VideoClipImporter-frameCount.html)| Number of frames in the clip.  
[frameRate](VideoClipImporter-frameRate.html)| Frame rate of the clip.  
[importAudio](VideoClipImporter-importAudio.html)| Import audio tracks from
source file.  
[isPlayingPreview](VideoClipImporter-isPlayingPreview.html)| Whether the
preview is currently playing.  
[keepAlpha](VideoClipImporter-keepAlpha.html)| Whether to keep the alpha from
the source into the transcoded clip.  
[outputFileSize](VideoClipImporter-outputFileSize.html)| Size in bytes of the
file once imported.  
[pixelAspectRatioDenominator](VideoClipImporter-
pixelAspectRatioDenominator.html)| Denominator of the pixel aspect ratio
(num:den).  
[pixelAspectRatioNumerator](VideoClipImporter-pixelAspectRatioNumerator.html)|
Numerator of the pixel aspect ratio (num:den).  
[sourceAudioTrackCount](VideoClipImporter-sourceAudioTrackCount.html)| Number
of audio tracks in the source file.  
[sourceFileSize](VideoClipImporter-sourceFileSize.html)| Size in bytes of the
file before importing.  
[sourceHasAlpha](VideoClipImporter-sourceHasAlpha.html)| True if the source
file has a channel for per-pixel transparency.  
[sRGBClip](VideoClipImporter-sRGBClip.html)| Whether the imported clip
contains sRGB color data.  
[transcodeSkipped](VideoClipImporter-transcodeSkipped.html)| Returns true if
transcoding was skipped during import, false otherwise. (Read Only)When
VideoImporterTargetSettings.enableTranscoding is set to true, the resulting
transcoding operation done at import time may be quite long, up to many hours
depending on source resolution and content duration. An option to skip this
process is offered in the asset import progress bar. When skipped, the
transcoding instead provides a non-transcoded verision of the asset. However,
the importer settings stay intact so this property can be inspected to detect
the incoherence with the generated artifact.Re-importing without stopping the
transcode process, or with transcode turned off, causes this property to
become false.  
  
### Public Methods

[ClearTargetSettings](VideoClipImporter.ClearTargetSettings.html)| Clear the
platform-specific import settings for the specified platform, causing them to
go back to the default settings.  
---|---  
[Equals](VideoClipImporter.Equals.html)| Performs a value comparison with
another VideoClipImporter.  
[GetPreviewTexture](VideoClipImporter.GetPreviewTexture.html)| Returns a
texture with the transcoded clip's current frame. Returns frame 0 when not
playing, and frame at current time when playing.  
[GetResizeHeight](VideoClipImporter.GetResizeHeight.html)| Get the resulting
height of the resize operation for the specified resize mode.  
[GetResizeModeName](VideoClipImporter.GetResizeModeName.html)| Get the full
name of the resize operation for the specified resize mode.  
[GetResizeWidth](VideoClipImporter.GetResizeWidth.html)| Get the resulting
width of the resize operation for the specified resize mode.  
[GetSourceAudioChannelCount](VideoClipImporter.GetSourceAudioChannelCount.html)|
Number of audio channels in the specified source track.  
[GetSourceAudioSampleRate](VideoClipImporter.GetSourceAudioSampleRate.html)|
Sample rate of the specified audio track.  
[GetTargetSettings](VideoClipImporter.GetTargetSettings.html)| Returns the
platform-specific import settings for the specified platform.  
[PlayPreview](VideoClipImporter.PlayPreview.html)| Starts preview playback.  
[SetTargetSettings](VideoClipImporter.SetTargetSettings.html)| Sets the
platform-specific import settings for the specified platform.  
[StopPreview](VideoClipImporter.StopPreview.html)| Stops preview playback.  
  
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

