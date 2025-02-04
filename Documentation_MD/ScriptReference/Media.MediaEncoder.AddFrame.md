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

#  [MediaEncoder](Media.MediaEncoder.html).AddFrame

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

## Declaration

public bool AddFrame([Texture2D](Texture2D.html) texture);

## Declaration

public bool AddFrame([Texture2D](Texture2D.html) texture,
[Media.MediaTime](Media.MediaTime.html) time);

### Parameters

texture | Texture containing the pixels to be written into the track for the current frame.  
---|---  
time | Timestamp for the new frame.  
  
### Returns

**bool** True if the operation succeeded. False otherwise.

### Description

Appends a frame to the file's video track.

Keep the number of video frames and audio samples aligned so that each track
is syncrhonized as much as possible. For instance, in a file with 30FPS video
and 48KHz audio, each added video frame should be followed by an audio buffer
of 1600 sample frames.  
  
**Note about timestamps**  
  
When adding a frame, a timestamp associated with this frame can optionally be
specified. For the timestamp to be used, it must be valid (see
MediaTime.IsValid).  
  
When no timestamp is provided, the frame is appended using the specified video
frame rate (see [VideoTrackAttributes.frameRate](Media.VideoTrackAttributes-
frameRate.html)) to compute the inter-frame time difference. There are
situations where a timestamp must be specified:  
  
**1.** When the video track is created without a valid rate (see
[VideoTrackAttributes.frameRate](Media.VideoTrackAttributes-frameRate.html).
In this case, **all** added frames must be given a timestamp because there is
no pre-defined inter-frame time difference.  
**2.** When the time difference between the last frame and the appended frame
is not as expected. For example, when recording in Unity and the game loop
lasts longer than expected, the inter-frame time difference is no longer
constant. In this case, you must specify the timestamp associated with the
appended frame. This way, when playing back the recorded movie, it will match
what was seen during recording. The resulting movie will then have a
**Variable Frame Rate** (VFR) because there is not exactly the same time
difference between each frame.  
  
For tracks with a pre-defined rate, it is valid to mix both variants, with and
without timestamps, as long as the time values end up monotonically
increasing. Frames added this way do not have to be equally spaced in time. It
is invalid to add a frame with a timestamp earlier than the timestamp of the
last frame.

* * *

## Declaration

public bool AddFrame(int width, int height, int rowBytes,
[TextureFormat](TextureFormat.html) format, NativeArray<byte> data);

## Declaration

public bool AddFrame(int width, int height, int rowBytes,
[TextureFormat](TextureFormat.html) format, NativeArray<byte> data,
[Media.MediaTime](Media.MediaTime.html) time);

### Parameters

width | Image width.  
---|---  
height | Image height.  
rowBytes | Bytes in one row of pixels. Useful in case lines include padding. Can be set to 0 if there is no padding.  
format | Pixel format. Only TextureFormat.RGBA32 is supported at this time.  
data | Bytes containing the image.  
time | Timestamp for new frame.  
  
### Returns

**bool** True if the operation succeeded. False otherwise.

### Description

Appends a frame from a raw buffer to the file's video track.

This version of AddFrame helps save image copying if the source data is not in
a Texture2D. For example, when pixel data comes from a
[AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html). For more
details, see the note about audio/video alignment in the variant of
[MediaEncoder.AddFrame](Media.MediaEncoder.AddFrame.html) taking a
[Texture2D](Texture2D.html).  
  
For more information about the `time` parameter, see **Note about timestamps**
in the other overloads of this method.

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

