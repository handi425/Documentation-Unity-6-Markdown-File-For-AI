[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ios-requirements-and-compatibility.html)
  * [中文](/cn/current/Manual/ios-requirements-and-compatibility.html)
  * [日本語](/ja/current/Manual/ios-requirements-and-compatibility.html)
  * [한국어](/kr/current/Manual/ios-requirements-and-compatibility.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ios-requirements-and-compatibility.html)
  * [中文](/cn/current/Manual/ios-requirements-and-compatibility.html)
  * [日本語](/ja/current/Manual/ios-requirements-and-compatibility.html)
  * [한국어](/kr/current/Manual/ios-requirements-and-compatibility.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Introducing iOS](ios-introducing.html)
  * iOS requirements and compatibility

[](ios-introducing.html)

Introducing iOS

[](how-unity-builds-ios-applications.html)

How Unity builds iOS applications

# iOS requirements and compatibility

Learn about the system requirements and compatibility information for iOS to
make sure you’re aware of any limitations for developing a Unity application
for this platform.

## iOS version support

Unity supports iOS 13 and above. For more information, see
[`PlayerSettings.iOS-
targetOSVersionString`](../ScriptReference/PlayerSettings.iOS-
targetOSVersionString.html).

## Graphics API support

iOS devices support [Metal](https://developer.apple.com/documentation/metal).
For more information, see [Metal Graphics API](Metal.html).

## Audio compression

Unity supports importing a variety of source format sound files. However, when
importing these files (with the exception of tracker files), they are always
re-encoded to the build target format. By default, this format is Vorbis,
though this can be overridden per platform to other formats (ADPCM, MP3, etc.)
if required. Vorbis playback provides better **compression** A method of
storing data that reduces the amount of storage space it requires. See
[Texture Compression](class-TextureImporterOverride), [Animation
Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) and quality for iOS compared with
MP3 playback.

## ASTC and PVRTC instead of DXT texture compression

Unity iOS does not support DXT textures. Instead, ASTC, PVRTC, ETC2, and ETC
**texture compression** 3D Graphics hardware requires Textures to be
compressed in specialized formats which are optimized for fast Texture
sampling. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) are natively supported by
iPhone/iPad devices. For more information about iOS **texture formats** A file
format for handling textures during real-time rendering by 3D graphics
hardware, such as a graphics card or mobile device. [More info](class-
TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat), see [texture import
settings](class-TextureImporter.html) and [texture compression format](class-
TextureImporterOverride#ios-and-tvos).

[](ios-introducing.html)

Introducing iOS

[](how-unity-builds-ios-applications.html)

How Unity builds iOS applications

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

