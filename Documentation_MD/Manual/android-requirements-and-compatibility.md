[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-requirements-and-compatibility.html)
  * [中文](/cn/current/Manual/android-requirements-and-compatibility.html)
  * [日本語](/ja/current/Manual/android-requirements-and-compatibility.html)
  * [한국어](/kr/current/Manual/android-requirements-and-compatibility.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-requirements-and-compatibility.html)
  * [中文](/cn/current/Manual/android-requirements-and-compatibility.html)
  * [日本語](/ja/current/Manual/android-requirements-and-compatibility.html)
  * [한국어](/kr/current/Manual/android-requirements-and-compatibility.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Introducing Android](android-introducing.html)
  * Android requirements and compatibility

[](android-introducing.html)

Introducing Android

[](android-gradle-overview.html)

Gradle for Android

# Android requirements and compatibility

Before you begin to develop an Android application in Unity, check Unity’s
requirements and compatibility information for Android to make sure you’re
aware of any limitations for developing a Unity application for this platform.

## Android support

Unity supports Android 6.0 “Marshmallow” (API level 23) and above. For more
information, refer to
[AndroidSdkVersions](../ScriptReference/AndroidSdkVersions.html).

## Graphics API support

Android devices support
[Vulkan](https://developer.android.com/ndk/guides/graphics) and [OpenGL
ES](https://developer.android.com/guide/topics/graphics/opengl). This section
contains information about the graphics APIs Unity supports for Android.

**Graphics API** | **Support**  
---|---  
**Vulkan** | Yes  
**OpenGL ES 1.0** | No  
**OpenGL ES 1.1** | No  
**OpenGL ES 2.0** | No  
**OpenGL ES 3.0** | Yes  
**OpenGL ES 3.1** | Yes  
**OpenGL ES 3.2** | Yes  
  
## Render pipeline compatibility

Not every [render pipeline](render-pipelines.html)A series of operations that
take the contents of a Scene, and displays them on a screen. Unity lets you
choose from pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) is compatible with Android due
to hardware and graphics API limitations.

**Feature** | **Built-in Render Pipeline** | **Universal Render Pipeline** | **High Definition Render Pipeline** | **Custom Scriptable Render Pipeline**  
---|---|---|---|---  
**Android** | Yes | Yes | No | Yes  
  
## Manifest element attributes

This section contains compatibility information on [Android App Manifest
element](https://developer.android.com/guide/topics/manifest/manifest-
intro#reference) attributes.

  * For the [<Activity>](https://developer.android.com/guide/topics/manifest/activity-element.html) element, Unity only supports the `singleTask` [launchMode](https://developer.android.com/guide/topics/manifest/activity-element.html#lmode).

## Emulator compatibility

Unity doesn’t support Android emulators. To test your application, you can:

  * [Test on an Android device](android-debugging-on-an-android-device.html).
  * If you only need to test mobile input for your application, use [Unity Remote](UnityRemote5.html)A downloadable app designed to help with Android, iOS and tvOS development. The app connects with Unity while you are running your project in Play Mode from the Unity Editor. [More info](UnityRemote5.html)  
See in [Glossary](Glossary.html#UnityRemote).

  * If you only need to test the appearance of an Android device, use the [Device Simulator](android-device-simulator.html).

## Texture compression

The standard texture **compression** A method of storing data that reduces the
amount of storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) formats on Android are [Ericsson
Texture Compression
(ETC)](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression) and
[Adaptable Scalable Texture Compression
(ASTC)](https://www.khronos.org/opengl/wiki/ASTC_Texture_Compression). To
target the widest range of Android devices, use one of these **texture
compression** 3D Graphics hardware requires Textures to be compressed in
specialized formats which are optimized for fast Texture sampling. [More
info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) formats. Unity’s default
texture compression format is ASTC. If an Android device doesn’t support the
texture compression format you use for a texture, Unity decompresses the
texture at runtime. This increases memory usage and decreases rendering speed.

A subset of Android devices support the DXT and PVRTC texture compression
formats. These formats support textures with an alpha channel as well as high
compression rates or high image quality. For digital distribution services
that filter content based on texture compression format, it is best practice
to create separate builds of your application for each texture compression
format.

There are two ways to change the default texture compression format for your
application:

  * In [Android Player Settings](class-PlayerSettingsAndroid.html) with the **Texture compression formats** setting. For more information, refer to [texture compression targeting](android-distribution-google-play.html#texture-compression-targeting).
  * In [Android Build Settings](android-build-settings.html) with the **Texture Compression** setting. The default value for this is **Use**Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings)**.

The value you set in Build Settings has priority over the one you set in
Player Settings. Use it to change the texture compression format for a
particular build.

You can also customize the texture compression format for individual textures.
The value you set for an individual **texture overrides** Platform-specific
settings that allow you to set the resolution, file size with associated
memory size requirements, pixel dimensions, and quality of your Textures for
each target platform. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureOverrides) the default texture
compression format value. For information on how to change the **texture
format** A file format for handling textures during real-time rendering by 3D
graphics hardware, such as a graphics card or mobile device. [More
info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat) of individual textures, see
[Texture Importer](class-TextureImporter.html).

## Playing video files

This section provides additional information for playing video files on
Android:

  * To play video files on Android, use the [Video Player](VideoPlayer.html) component. If your application tries to play a video file that the device doesn’t support, Unity doesn’t play the video.

  * You can use any resolution or number of audio channels so long as the target device supports them. **Note** : Not all devices support resolutions greater than 640 × 360.

  * Unity supports playback from uncompressed asset bundles. For [Android Pie](https://en.wikipedia.org/wiki/Android_Pie) and above, Unity supports playback from compressed asset bundles.

  * Unity doesn’t support native webM/VP8 transparency. To play VP8-encoded webM clips with transparency, transcode the clips to a supported format.

  * In Android versions prior to `6.0.1`, videos with transparency that have a higher resolution than the device support render **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) outside the supported resolution as
white.

  * Unity reports format compatibility issues in the `adb logcat` output and prefixes them with `AndroidVideoMedia`. This file might display other device-specific error messages near the video format issues Unity reports. These device-specific errors aren’t visible to Unity and often explain what the compatibility issue is.

[](android-introducing.html)

Introducing Android

[](android-gradle-overview.html)

Gradle for Android

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

