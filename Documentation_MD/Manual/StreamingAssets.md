[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StreamingAssets.html)
  * [中文](/cn/current/Manual/StreamingAssets.html)
  * [日本語](/ja/current/Manual/StreamingAssets.html)
  * [한국어](/kr/current/Manual/StreamingAssets.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StreamingAssets.html)
  * [中文](/cn/current/Manual/StreamingAssets.html)
  * [日本語](/ja/current/Manual/StreamingAssets.html)
  * [한국어](/kr/current/Manual/StreamingAssets.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Scripting with Assets](ScriptingAssets.html)
  * Streaming Assets

[](LoadingResourcesatRuntime.html)

Loading Resources at Runtime

[](ModifyingSourceAssetsThroughScripting.html)

Modifying Source Assets Through Scripting

# Streaming Assets

Unity combines **Scenes** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and Assets into binary files inside the
generated Player when it builds the Project. However, you can place files into
the normal filesystem on the target machine to make them available using a
pathname. For example, for deploying a movie file on iOS devices, the original
movie file must be available from a location in the filesystem to play using
the `PlayMovie` function. This folder can also include `AssetBundles` that you
intend to distribute directly in the Player installation, rather than
downloading them on-demand.

Unity copies any files placed in the folder called **StreamingAssets** (case-
sensitive) in a Unity Project verbatim to a particular folder on the target
machine. To retrieve the folder, use the
[Application.streamingAssetsPath](../ScriptReference/Application-
streamingAssetsPath.html) property. It’s always best to use
`Application.streamingAssetsPath` to get the location of the
**StreamingAssets** folder, because it always points to the correct location
on the platform where the application is running.

The location returned by `Application.streamingAssetsPath` varies per
platform:

  * Most platforms (Unity Editor, Windows, Linux players) use `Application.dataPath + "/StreamingAssets"`.
  * macOS player uses `Application.dataPath + "/Resources/Data/StreamingAssets"`.
  * iOS uses `Application.dataPath + "/Raw"`.
  * Android uses files inside a compressed **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK)/JAR file, `"jar:file://" +
Application.dataPath + "!/assets"`.

  * On Web, `Application.streamingAssetsPath` returns a HTTP URL that points to the `StreamingAssets/` path on the web server. For example, `http://localhost:8000/unity_webgl_build/StreamingAssets/` is returned when your application is running against a local development server.

## Accessing streaming assets

On Android and the Web platform, it’s not possible to access the streaming
asset files directly via file system APIs and [`streamingAssets`
path](../ScriptReference/Application-streamingAssetsPath.html) because these
platforms return a URL. Use the
[UnityWebRequest](../ScriptReference/Networking.UnityWebRequest.html) class to
access the content instead.

**Notes:**

  * The `streamingAssets` path is read-only. Don’t modify or write new files to the `streamingAssets` directory at runtime.
  * .dll and script files located in the StreamingAssets folder aren’t included during script compilation.
  * [Asset Bundles](AssetBundlesIntro.html) and [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html?preview=1) are alternative ways of accessing content that’s not part of regular game build data, and preferred over Streaming Assets folder.

[](LoadingResourcesatRuntime.html)

Loading Resources at Runtime

[](ModifyingSourceAssetsThroughScripting.html)

Modifying Source Assets Through Scripting

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

