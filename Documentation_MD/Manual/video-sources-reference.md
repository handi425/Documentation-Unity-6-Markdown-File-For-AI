[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/video-sources-reference.html)
  * [中文](/cn/current/Manual/video-sources-reference.html)
  * [日本語](/ja/current/Manual/video-sources-reference.html)
  * [한국어](/kr/current/Manual/video-sources-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/video-sources-reference.html)
  * [中文](/cn/current/Manual/video-sources-reference.html)
  * [日本語](/ja/current/Manual/video-sources-reference.html)
  * [한국어](/kr/current/Manual/video-sources-reference.html)

  * [Video and cutscenes](Video.html)
  * [Video sources](video-sources.html)
  * Use video sources

[](video-clips-use.html)

Import and preview video clips

[](VideoSources-VideoFiles.html)

Understanding video files

# Use video sources

Reference your video sources in the Video Player to use video in Unity.

To use video in Unity, you must reference your files in the Video Player
through the **Source** dropdown. The Video Player can play video sources from
video clips or URLs.

This information covers referencing video files only. To configure the Video
Player, refer to [Video Player component](class-VideoPlayer.html). To
configure video clips, refer to [Video Clip Importer](class-VideoClip.html).

## Prerequisites

  * Add a [Video Player component](class-VideoPlayer.html) to your **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

## Reference your file as a video clip

To reference a file as a video clip in the Video Player:

  1. [Import your file as a video clip](video-clips-use.html#import).
  2. Select your **Video Player** component.
  3. In the **Video Player**Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window, go to **Source**.

  4. Set **Source** to **Video Clip**.
  5. Click and drag the video clip asset into the **Video Clip** parameter or click the **Video Clip** picker to select your video clip.

**Note:** As video files are often large, you can also assign video clips as
an [addressable video
asset](https://docs.unity3d.com/Packages/com.unity.addressables@2.2/manual/index.html)
or from [AssetBundles](AssetBundlesIntro.html) to help reduce your initial
game install size.

## Reference your file as a URL

Reference your file as a URL to play files that aren’t bundled with your
application. This can be helpful for user-generated content, if your content
isn’t under Unity’s direct control, or if you want to avoid storing large
video files locally.

URLs can point to files on a local file system, a web server, or your
StreamingAssets folder. As the URL option bypasses asset management, you must
manually ensure that Unity is able to locate the source video. For example, a
local file must be in a file location that Unity can access, indicated with
scripting, while a web URL needs a web server to host the source video.

To reference a file as a URL in the Video Player:

  1. Select your **Video Player** component.
  2. In the **Video Player Inspector** window, go to **Source**.
  3. Set **Source** to **URL**.
  4. Set the URL as your chosen URL.

**Note:** On the [Web](webgl.html) platform, the URL must point to a web URL
because playback from the local file system and
`Application.persistentDataPath` aren’t supported.

### File system

On native build platforms, you can set the URL to any file path to directly
use files in your file system. You can use a `file://` prefix but it’s not
necessary.

**Note:** Some web browsers allow you to manually disable browser Cross-Origin
Resource Sharing (CORS) security for `file://` URL access for local
development and testing purposes. For security reasons, this isn’t a
recommended approach.

### Web server

You can set the URL to read videos from a web server using the `http://` and
`https://` prefixes. In these cases, Unity performs the necessary pre-
buffering and error management processes.

### StreamingAssets folder

You can set the URL to use files placed in Unity’s
[StreamingAssets](StreamingAssets.html) folder, or by using the platform-
specific path `Application.streamingAssetsPath`. Refer to
[Application.streamingAssetsPath](../ScriptReference/Application-
streamingAssetsPath.html) for more information.

## Additional resources

  * [Video Player component](class-VideoPlayer.html)
  * [Video Clip Importer](class-VideoClip.html)
  * [Asset Bundles](AssetBundlesIntro.html)
  * [StreamingAssets](StreamingAssets.html)

[](video-clips-use.html)

Import and preview video clips

[](VideoSources-VideoFiles.html)

Understanding video files

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

