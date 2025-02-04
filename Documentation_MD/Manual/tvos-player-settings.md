[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tvos-player-settings.html)
  * [中文](/cn/current/Manual/tvos-player-settings.html)
  * [日本語](/ja/current/Manual/tvos-player-settings.html)
  * [한국어](/kr/current/Manual/tvos-player-settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tvos-player-settings.html)
  * [中文](/cn/current/Manual/tvos-player-settings.html)
  * [日本語](/ja/current/Manual/tvos-player-settings.html)
  * [한국어](/kr/current/Manual/tvos-player-settings.html)

  * [Platform development ](PlatformSpecific.html)
  * [tvOS](tvOS-introducing.html)
  * tvOS Player Settings

[](tvos-requirements-and-compatibility.html)

Requirements and compatibility

[](tvOS-developing.html)

Developing for tvOS

# tvOS Player Settings

tvOS shares many **Player Settings** Settings that let you set various player-
specific options for the final game built by Unity. [More info](class-
PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) with [iOS](class-
PlayerSettingsiOS.html) but there are certain settings that are specific only
to tvOS.

![tvOS Player Settings](../uploads/Main/tvos-player-settings.png) tvOS Player
Settings

## Icon

Use the **Icon** settings to customize the branding for your Apple TV app.

Apple TV images consist of between two and five layers. Unity only provides
two layers for Apple TV icons. For more information on layering images for
Apple TV, see the Apple Developer documentation on [Layered
Images](https://developer.apple.com/design/human-interface-
guidelines/tvos/icons-and-images/layered-images/).

**Setting** | **Function**  
---|---  
**App icons** | Build the custom icon that you would like to appear on your [AppleTV home screen](https://developer.apple.com/design/human-interface-guidelines/tvos/overview/home-screen/) for each resolution (1280x768, 800x480, and 400x240).  
**Top Shelf icons** | Build the custom icon that you would like to appear on the [Apple Top Shelf](https://developer.apple.com/design/human-interface-guidelines/tvos/overview/top-shelf/) for each aspect and resolution (4640x1440, 2320x720, 3840x1440, and 1920x720).  
  
## Splash Image

In addition to the [common Splash Screen settings](class-
PlayerSettingsSplashScreen.html), there are two additional settings for the
tvOS platform:

![tvOS Splash Settings](../uploads/Main/tvos-splash-settings.png) tvOS Splash
Settings

Use the **AppleTV (1x)** and **AppleTV (2x)** properties to set [Apple TV
static splash screens](https://developer.apple.com/design/human-interface-
guidelines/tvos/app-architecture/loading/).

## Configuration

tvOS has the same Configuration settings as iOS, except for one - the
**Require Extended Game Controller** setting.

If your application requires a game controller, enable the **Require Extended
Game Controller** setting. For more information, see the Apple Developer
documentation on [Game Controllers](https://developer.apple.com/design/human-
interface-guidelines/tvos/remote-and-controllers/game-controllers/)A device to
control objects and characters in a game.  
See in [Glossary](Glossary.html#gamecontroller).

[](tvos-requirements-and-compatibility.html)

Requirements and compatibility

[](tvOS-developing.html)

Developing for tvOS

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

