[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/deep-linking-ios.html)
  * [中文](/cn/current/Manual/deep-linking-ios.html)
  * [日本語](/ja/current/Manual/deep-linking-ios.html)
  * [한국어](/kr/current/Manual/deep-linking-ios.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/deep-linking-ios.html)
  * [中文](/cn/current/Manual/deep-linking-ios.html)
  * [日本語](/ja/current/Manual/deep-linking-ios.html)
  * [한국어](/kr/current/Manual/deep-linking-ios.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Developing for iOS](ios-developing.html)
  * Deep linking on iOS

[](UnityasaLibrary-iOS.html)

Integrating Unity into native iOS applications

[](ios-authorizations-in-unity.html)

iOS authorizations in Unity

# Deep linking on iOS

Deep links are hyperlinks outside of your application that take a user to a
specific location within the application rather than a website. When a user
clicks a deep link, the application opens from the designated location, such
as a specific **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) in a Unity application. For more
information about deep links and how to use them, refer to [Deep
linking](deep-linking.html).

There are two ways to enable deep links for iOS applications: URL schemes and
universal links.

For information on how to use deep links and handle them when your application
opens, refer to [Using deep links](deep-linking.html#using-deep-links).

## URL schemes

A URL scheme specifies a link structure that your iOS application refers to.
The device opens the application when the user clicks a deep link that matches
the URL scheme structure. To add a URL scheme, use the following steps:

  1. Go to **Edit** > **Project Settings** > **Player** > **Other Settings** > **Configuration**.
  2. Expand **Supported URL schemes** to set the following properties: 
     * **Size** property to `1`.
     * **Element 0** property to the URL scheme to use with your application. For example, use `unitydl` to open your application when the device processes a link that starts with `unitydl://`.

![Supported URL schemes settings for iOS.](../uploads/Main/ios-supported-
url.png) Supported URL schemes settings for iOS.

Your iOS application now opens when the device processes any link that starts
with `unitydl://`.

**Note** : To use multiple URL schemes in your project, increase the value of
the **Size** property.

## Universal links

Universal links are similar to deep links because they open a specific
location within an application. However, if the application isn’t installed, a
universal link opens a URL in Safari. To enable universal links, refer to
Apple’s documentation on [Allowing Apps and Websites to Link to Your
Content](https://developer.apple.com/documentation/xcode/allowing-apps-and-
websites-to-link-to-your-content).

## Additional resources

  * [Deep linking](deep-linking.html)

[](UnityasaLibrary-iOS.html)

Integrating Unity into native iOS applications

[](ios-authorizations-in-unity.html)

iOS authorizations in Unity

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

