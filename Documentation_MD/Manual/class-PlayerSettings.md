[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-PlayerSettings.html)
  * [中文](/cn/current/Manual/class-PlayerSettings.html)
  * [日本語](/ja/current/Manual/class-PlayerSettings.html)
  * [한국어](/kr/current/Manual/class-PlayerSettings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-PlayerSettings.html)
  * [中文](/cn/current/Manual/class-PlayerSettings.html)
  * [日本語](/ja/current/Manual/class-PlayerSettings.html)
  * [한국어](/kr/current/Manual/class-PlayerSettings.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Project Settings](comp-ManagerGroup.html)
  * Player

[](class-Physics2DManager.html)

Physics 2D reference

[](class-PlayerSettingsSplashScreen.html)

Splash Image Player settings

# Player

[Switch to Scripting](../ScriptReference/PlayerSettings.html "Go to
PlayerSettings page in the Scripting Reference")

The **Player** settings window (menu: **Edit > Project Settings > Player**)
contain settings that determine how Unity builds and displays your final
application. You can use the
[PlayerSettings](../ScriptReference/PlayerSettings.html) API to control most
of the settings available in this window.

## General settings

The **Player settings** differ between the [platform
modules](https://docs.unity3d.com/hub/manual/AddModules.html) that you’ve
installed. Each [platform](PlatformSpecific.html) has its own Player settings
which you’ll need to set for each version of your application you want to
build. To navigate between them, click on the tabs with the platform operating
system icon on.

![Player settings window](../uploads/Main/player-settings-window.png) Player
settings window

However, there are some general settings that all platforms share, that you
only need to set once:

**Property** | **Function**  
---|---  
**Company Name** | Enter the name of your company. Unity uses this to locate the preferences file.  
**Product Name** | Enter the name that appears on the menu bar when your application is running. Unity also uses this to locate the preferences file.  
**Version** | Enter the version number of your application.  
**Default Icon** | Pick the Texture 2D file that you want to use as a default icon for the application on every platform. You can override this for specific platforms.  
**Default Cursor** | Pick the Texture 2D file that you want to use as a default cursor for the application on every supported platform.  
**Cursor Hotspot** | Set the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) offset value from the top left of the
default cursor to the location of the cursor hotspot. The cursor hotspot is
the point in the cursor image that Unity uses to trigger events based on
cursor position.  
  
## Platform-specific settings

The platform-specific settings are divided into the following sections:

  * **Icon** : the game icon(s) as shown on the desktop. You can choose icons from 2D image assets in the Project, such as **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) or imported images.

  * **Resolution and Presentation** : settings for screen resolution and other presentation details such as whether the game should default to fullscreen mode.
  * **Splash Image** : the image shown while the game is launching. This section also includes common settings for creating a Splash Screen. For more information, refer to the [Splash Image](class-PlayerSettingsSplashScreen.html) documentation.
  * **Other Settings** : any remaining settings specific to the platform.
  * **Publishing Settings** : details of how the built application is prepared for delivery from the app store or host webpage.
  * ****XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) Settings**: settings specific to [Virtual
Reality, Augmented Reality, and Mixed Reality](XR.html) applications.

You can find information about the settings specific to individual platforms
in the [platform’s own manual section](PlatformSpecific.html):

  * **Android:** [Android Player settings](class-PlayerSettingsAndroid.html)
  * **Dedicated Server:** [Dedicated Server Player settings](dedicated-server-player-settings.html)
  * **iOS:** [iOS Player settings](class-PlayerSettingsiOS.html)
  * **Linux:** [Linux Player settings](PlayerSettings-linux.html)
  * **macOS:** [macOS Player settings](PlayerSettings-macOS.html)
  * **tvOS:** [tvOS Player settings](tvos-player-settings.html)
  * **Web:** [Web Player settings](class-PlayerSettingsWebGL.html)
  * **Windows:** [Windows Player settings](playersettings-windows.html)

You can find details of **closed platform** Includes platforms that require
confidentiality and legal agreements with the platform provider for using
their developer tools and hardware. These platforms aren’t open to development
unless you have an established relationship with the provider. For example
PlayStation®, Game Core for Xbox®, and Nintendo®.  
See in [Glossary](Glossary.html#Closedplatform) Player settings in their
respective documentation.

PlayerSettings

[](class-Physics2DManager.html)

Physics 2D reference

[](class-PlayerSettingsSplashScreen.html)

Splash Image Player settings

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

