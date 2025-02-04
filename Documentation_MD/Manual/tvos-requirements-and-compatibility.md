[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tvos-requirements-and-compatibility.html)
  * [中文](/cn/current/Manual/tvos-requirements-and-compatibility.html)
  * [日本語](/ja/current/Manual/tvos-requirements-and-compatibility.html)
  * [한국어](/kr/current/Manual/tvos-requirements-and-compatibility.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tvos-requirements-and-compatibility.html)
  * [中文](/cn/current/Manual/tvos-requirements-and-compatibility.html)
  * [日本語](/ja/current/Manual/tvos-requirements-and-compatibility.html)
  * [한국어](/kr/current/Manual/tvos-requirements-and-compatibility.html)

  * [Platform development ](PlatformSpecific.html)
  * [tvOS](tvOS-introducing.html)
  * Requirements and compatibility

[](tvOS-introducing.html)

tvOS

[](tvos-player-settings.html)

tvOS Player Settings

# Requirements and compatibility

Although the Apple TV platform (tvOS) is similar to the iOS platform, there
are some differences between the two. Before developing your application for
tvOS, review the requirements, compatibility notes, and known limitations.

## Requirements

To develop for tvOS, you need the following:

  * Xcode 7.1 or later.

## Compatibility

It’s best practice to create a separate branch or copy of your application and
port that to Apple TV. tvOS only supports a subset of the iOS framework. This
means that **plug-ins** A set of code created outside of Unity that creates
functionality in Unity. There are two kinds of plug-ins you can use in Unity:
Managed plug-ins (managed .NET assemblies created with tools like Visual
Studio) and Native plug-ins (platform-specific native code libraries). [More
info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) that are compatible with iOS might
not be compatible with tvOS.

If your app uses more than 4 GB on disk, break it into smaller parts and use
On Demand Resources.

**Note:** Bitcode is included with tvOS builds, which adds around 130 MB to
your executables. App Store servers strip this code, so it doesn’t affect your
distribution size. To estimate Bitcode size, analyze the
[LLVM](https://en.wikipedia.org/wiki/LLVM) sections in your executable from
the command line with `otool -1`.

## Implementing support for On Demand Resources

tvOS limits how much disk space your application can reserve. The main
application installation bundle size can’t be larger than 4 GB. The limits for
additional downloadable content are up to 2 GB for in-use assets, and up to 20
GB of total downloadable content. Apple recommends the use of On Demand
Resources (ODR) for tvOS downloadable content, which is the best disk space
management for tvOS. Unity supports ****ODR** On-demand resources (ODR) is a
feature available for the iOS and tvOS platforms, from version 9.0 of iOS and
tvOS onwards. It allows you to reduce the size of your application by
separating the core assets (those that are needed from application startup)
from assets which may be optional, or which appear in later levels of your
game. [More info](AppThinning.html)  
See in [Glossary](Glossary.html#ODR)** via **Asset Bundles**.

## Known limitations

  * The on-screen keyboard is limited to single line entries.
  * [tvOS Simulator](https://developer.apple.com/documentation/xcode/running-your-app-in-the-simulator-or-on-a-device/) doesn’t emulate the Apple TV Remote as an app controller, which means apps can’t access its input.

[](tvOS-introducing.html)

tvOS

[](tvos-player-settings.html)

tvOS Player Settings

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

