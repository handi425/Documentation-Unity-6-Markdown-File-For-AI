[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-video.html)
  * [中文](/cn/current/Manual/webgl-video.html)
  * [日本語](/ja/current/Manual/webgl-video.html)
  * [한국어](/kr/current/Manual/webgl-video.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-video.html)
  * [中文](/cn/current/Manual/webgl-video.html)
  * [日本語](/ja/current/Manual/webgl-video.html)
  * [한국어](/kr/current/Manual/webgl-video.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Video playback in Web

[](webgl-audio.html)

Audio in Web

[](webgl-texture-compression.html)

Texture compression in Web

# Video playback in Web

Unity Web supports video playback using the
[VideoPlayer](../ScriptReference/Video.VideoPlayer.html) API. This page
provides information only about the video playback capabilities that Web
supports. To learn how to use video with your Unity application, refer to the
[Video Player](class-VideoPlayer.html).

## Video player

You can use the Video Player component to control how to time video playback
relative to other interactive behaviors in Web. For more information, refer to
the [Clock management with the Video Player component](video-clock.html).

The only exceptions are:

  * Web doesn’t support frame accuracy.
  * The `VideoPlayer` component doesn’t support synchronous playback with `captureFramerate`. By default, it uses the normal asynchronous playback that’s described with the Game time update mode.
  * The `VideoPlayer` component corrects drift between video playback and Unity time by temporarily speeding the playback controls to up or down. However, because the video support in Safari browser has limitations that prevent this mechanism from operating with precision, the drift correction is disabled.

## Supported video playback features and formats

Unity Web supports the following video playback audio output modes:

**Class** | **Use**  
---|---  
**[VideoAudioOutputMode.None](../ScriptReference/Video.VideoAudioOutputMode.None.html)** | Disables the embedded audio.  
**[VideoAudioOutputMode.Direct](../ScriptReference/Video.VideoAudioOutputMode.Direct.html)** | Sends the embedded audio directly to the platform’s audio hardware.  
**[VideoAudioOutputMode.AudioSource](../ScriptReference/Video.VideoAudioOutputMode.AudioSource.html)** | Sends the embedded audio into a specified [AudioSource](../ScriptReference/AudioSource.html). If you set the output mode to `VideoAudioOutputMode.AudioSource`, Unity ignores all AudioSource fields except mute. This is because 3D spatialization of video playback isn’t available on the web.  
  
### Video formats

Unity supports the following common video file formats:

**_Format_** | **_Extensions_**  
---|---  
MPEG–4 Part 14 | .mp4  
MPEG–4 file used for video downloaded from the Apple iTunes store | .m4v  
Apple’s QuickTime movie format | .mov  
Moving Picture Experts Group (MPEG) | .mpg  
MPEG video | .mpeg  
WebM video | .webm  
Ogg video file | .ogv  
  
The only exception to this restriction is if the video URL has no file name
extension, in which case, the browser plays the video without any
restrictions.

### Video clips

[`VideoClips`](class-VideoClip.html) aren’t supported on Web. Typically, when
creating a **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), you import a [VideoClip](class-
VideoClip.html) to your Unity project using `VideoClipImporter`, which is
convenient if you want to reuse the same `VideoClip` across several platforms.
When building a Web game that has `VideoClip` attached however, the Unity
console logs the following warning for each `VideoClip` found in the game:

`Embedded video clips are not supported by the Web player: %s. \nUse the Video
Player component's URL option instead`. Where `%s` is replaced by the video
clip name. At runtime, if your game has `VideoClips` assigned, then Unity logs
a warning message in the developer console of your web browser.

## Additional resources:

  * [Video Player](VideoPlayer.html)
  * [Video Clip](class-VideoClip.html)
  * [Video Player component](class-VideoPlayer.html)

[](webgl-audio.html)

Audio in Web

[](webgl-texture-compression.html)

Texture compression in Web

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

