[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-VideoClip.html)
  * [中文](/cn/current/Manual/class-VideoClip.html)
  * [日本語](/ja/current/Manual/class-VideoClip.html)
  * [한국어](/kr/current/Manual/class-VideoClip.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-VideoClip.html)
  * [中文](/cn/current/Manual/class-VideoClip.html)
  * [日本語](/ja/current/Manual/class-VideoClip.html)
  * [한국어](/kr/current/Manual/class-VideoClip.html)

  * [Video and cutscenes](Video.html)
  * [Video sources](video-sources.html)
  * Video Clip Importer

[](VideoSources-FileCompatibility.html)

Video file compatibility

[](VideoTransparency.html)

Video transparency support

# Video Clip Importer

A Video Clip is an imported video file, which the [Video Player
component](class-VideoPlayer.html) uses to play video content (and
accompanying audio content, if the video also has sound). Typical file
extensions for video files include .mp4, .mov, .webm, and .wmv.

Platform-specific options adapt the transcode process for each target
platform, allowing the selection of default options for each platform.

![The Transcode section of the Video Clip
Importer](../uploads/Main/Video-6.png) The Transcode section of the Video Clip
Importer

If transcode is disabled, the video file is used as is, meaning compatibility
with the target platform must be verified manually (see documentation on video
file compatibility for more information). However, choosing not to transcode
can save time as well as avoid transformation-related quality loss.

## Video Clip Importer Properties

**_Property_** |  |  | **_Function_**  
---|---|---|---  
**Keep Alpha** | Keeps the [alpha channel](VideoTransparency.html) and encodes it during transcode so it can be used even if the target platform does not natively support videos with alpha.  
  
This property is only visible for sources that have an alpha channel.  
**Deinterlace** | Controls how interlaced sources are deinterlaced during transcode. For example, you can choose to change interlacing settings due to how a video is encoded or for aesthetic reasons. Interlaced videos have two time samples in each frame: one in odd-numbered lines, and one in even-numbered lines.  
| **Off** | The source is not interlaced, and there is no processing to do (this is the default setting).  
| **Even** | Takes the even lines of each frame and interpolates them to create missing content. Odd lines are dropped.  
| **Odd** | Takes the odd lines of each frame and interpolates them to create missing content. Even lines are dropped.  
**Flip Horizontally** | If this tickbox is checked, the source content is flipped along a horizontal axis during transcode to make it upside-down.  
**Flip Vertically** | If this tickbox is checked, the source content is flipped along a vertical axis during transcode to swap left and right.  
**Import Audio** | If this tickbox is checked, audio tracks are imported during transcode.  
  
This property is only visible for sources that have audio tracks.  
**Transcode** | When enabled by ticking the checkbox, the source is transcoded into a format that is compatible with the target platform.  
  
If disabled, the original content is used, bypassing the potentially lengthy
transcoding process.  
  
**Note:** Verify that the source format is compatible with each target
platform (see documentation on video file compatibility for more information).  
| **Dimensions** | Controls how the source content is resized.  
| **Original** | Keeps the original size.  
| **Three Quarter Res** | Resizes the source to three quarters of its original width and height.  
| **Half Res** | Resizes the source to half of its original width and height.  
| **Quarter Res** | Resizes the source to a quarter of its original width and height.  
| **Square (1024 X 1024)** | Resizes the source to 1024 x 1024 square images. Aspect ratio is controllable.  
| **Square (512 X 512)** | Resizes the source to 512 x 512 square images. Aspect ratio is controllable.  
| **Square (256 X 256)** | Resizes the source to to 256 x 256 square images. Aspect ratio is controllable.  
| **Custom** | Resizes the source to a custom resolution. Aspect ratio is controllable.  
| **Width** | Width of the resulting images.  
  
This property is only visible when the Dimensions field is set to Custom.  
| **Height** | Height of the resulting images.  
  
This property is only visible when the Dimensions field is set to Custom.  
| **Aspect Ratio** The relationship of an image’s proportional dimensions,
such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio) | Aspect ratio control used when resizing images.  
  
This property is only visible when the Dimensions field is set to an option
other than Original.  
| **No Scaling** | Black areas added as needed to preserve the aspect ratio of the original content.  
| **Stretch** | Stretches the original content to fill the destination resolution without leaving black areas.  
| **Codec** | Codec used for encoding the video track.   
  
For information about codec support, see the documentation on [Video file
compatibility](VideoSources-FileCompatibility.html).  
| **Auto** | Chooses the most suitable video codec for the target platform.  
| **H264** | The MPEG–4 Advanced Video Coding (AVC) video codec, supported by hardware on most platforms.  
| **H265** | The MPEG-H Part 2, or High Efficiency Video Coding (HEVC) video codec, supported by hardware on some platforms.  
| **VP8** | The VP8 video codec, supported by software on most platforms, and by hardware on a few platforms such as Android and Web.  
| **Bitrate Mode** | Low, Medium, or High bitrate, relative to the chosen codec’s baseline profile.  
| **Spatial Quality** | This setting dictates whether video images are reduced in size during transcoding, which means they take up less storage space. However, resizing images also results in blurriness during playback.  
| **Low Spatial Quality** | The image is significantly reduced in size during transcode (typically to a quarter of its original dimensions), and then expanded back to its original size upon playback. This is the highest amount of resizing, meaning it saves the most storage space but results in the largest amount of blurriness upon playback.  
| **Medium Spatial Quality** | The image is moderately reduced in size during transcode (typically to half of its original dimensions), and then expanded back to its original size upon playback. Although there is some resizing, images will be less blurry than those that use the Low Spatial Quality option, and there is some reduction in required storage space.  
| **High Spatial Quality** | No resizing takes place if this option is selected. This means the image is not reduced in size during transcode, and therefore the video’s original level of visual clarity is maintained.  
  
* * *

  * 2019–05–07 Page amended 

  * New feature in Unity 5.6

VideoClip

[](VideoSources-FileCompatibility.html)

Video file compatibility

[](VideoTransparency.html)

Video transparency support

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

