[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/VideoSources-VideoFiles.html)
  * [中文](/cn/current/Manual/VideoSources-VideoFiles.html)
  * [日本語](/ja/current/Manual/VideoSources-VideoFiles.html)
  * [한국어](/kr/current/Manual/VideoSources-VideoFiles.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/VideoSources-VideoFiles.html)
  * [中文](/cn/current/Manual/VideoSources-VideoFiles.html)
  * [日本語](/ja/current/Manual/VideoSources-VideoFiles.html)
  * [한국어](/kr/current/Manual/VideoSources-VideoFiles.html)

  * [Video and cutscenes](Video.html)
  * [Video sources](video-sources.html)
  * Understanding video files

[](video-sources-reference.html)

Use video sources

[](VideoSources-FileCompatibility.html)

Video file compatibility

# Understanding video files

Video files are more accurately described as “containers”. This is because
they can contain not only the video itself but also additional tracks
including audio, subtitles, and further video footage. There can also be more
than one of each type of track in a container, for example:

  * Multiple points of view

  * Stereo or 5.1 versions of the audio mix

  * Subtitles in different languages

  * Dialogue in different languages

To save on bandwidth and storage, each track’s content is encoded using a
“codec”, which compresses and decompresses data as required.

A common video codec format is H.264, and a common audio codec format is AAC.

File extensions such as .mp4, .mov, .webm or .avi indicate that the data in
the video file is arranged using a certain container format.

## Hardware and software decoding

Most modern devices have hardware dedicated to decoding videos. This hardware
typically requires less power to do this task than, for example, the CPU, and
means that the resources can be used for tasks other than decoding videos.

This hardware acceleration is made possible by native custom APIs, which vary
from platform to platform. Unity’s video architecture hides these differences
by providing a common **UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More info](UI-
system-compare.html)  
See in [Glossary](Glossary.html#UI) and Scripting API in order to access these
capabilities.

Unity is also capable of software-based video decoding. This uses the VP8
video codec and Vorbis audio codec, and is useful for situations where a
platform’s hardware decoding results in unwanted restrictions in terms of
resolution, the presence of multiple audio tracks, or support of alpha channel
(see documentation on [Transparency](VideoTransparency.html) for more
information).

* * *

  * 2017–06–15 Page published 

  * New feature in Unity 5.6

[](video-sources-reference.html)

Use video sources

[](VideoSources-FileCompatibility.html)

Video file compatibility

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

