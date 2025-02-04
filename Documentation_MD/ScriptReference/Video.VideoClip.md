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

# VideoClip

class in UnityEngine.Video

/

Inherits from:[Object](Object.html)

/

Implemented in:[UnityEngine.VideoModule](UnityEngine.VideoModule.html)

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

A container for video data.

A VideoClip stores the video portion of a movie file using a codec that is
appropriate for the target platform. VideoClips are referenced by
[VideoPlayer](Video.VideoPlayer.html)s to play videos.

### Properties

[audioTrackCount](Video.VideoClip-audioTrackCount.html)| Number of audio
tracks in the clip.  
---|---  
[frameCount](Video.VideoClip-frameCount.html)| The length of the VideoClip in
frames. (Read Only).  
[frameRate](Video.VideoClip-frameRate.html)| The frame rate of the clip in
frames/second. (Read Only).  
[height](Video.VideoClip-height.html)| The height of the images in the video
clip in pixels. (Read Only).  
[length](Video.VideoClip-length.html)| The length of the video clip in
seconds. (Read Only).  
[originalPath](Video.VideoClip-originalPath.html)| The video clip path in the
project's assets. (Read Only).  
[pixelAspectRatioDenominator](Video.VideoClip-
pixelAspectRatioDenominator.html)| Denominator of the pixel aspect ratio
(num:den). (Read Only).  
[pixelAspectRatioNumerator](Video.VideoClip-pixelAspectRatioNumerator.html)|
Numerator of the pixel aspect ratio (num:den). (Read Only).  
[sRGB](Video.VideoClip-sRGB.html)| Whether the imported clip contains sRGB
color data (Read Only).  
[width](Video.VideoClip-width.html)| The width of the images in the video clip
in pixels. (Read Only).  
  
### Public Methods

[GetAudioChannelCount](Video.VideoClip.GetAudioChannelCount.html)| The number
of channels in the audio track. E.g. 2 for a stereo track.  
---|---  
[GetAudioLanguage](Video.VideoClip.GetAudioLanguage.html)| Get the audio track
language. Can be unknown.  
[GetAudioSampleRate](Video.VideoClip.GetAudioSampleRate.html)| Get the audio
track sampling rate in Hertz.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
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

