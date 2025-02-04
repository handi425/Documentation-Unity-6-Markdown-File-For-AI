[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/macos-distribution-mac-app-store.html)
  * [中文](/cn/current/Manual/macos-distribution-mac-app-store.html)
  * [日本語](/ja/current/Manual/macos-distribution-mac-app-store.html)
  * [한국어](/kr/current/Manual/macos-distribution-mac-app-store.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/macos-distribution-mac-app-store.html)
  * [中文](/cn/current/Manual/macos-distribution-mac-app-store.html)
  * [日本語](/ja/current/Manual/macos-distribution-mac-app-store.html)
  * [한국어](/kr/current/Manual/macos-distribution-mac-app-store.html)

  * [Platform development ](PlatformSpecific.html)
  * [macOS](AppleMac.html)
  * [Building and delivering for macOS](macos-delivery.html)
  * Deliver applications to the Mac App Store

[](macosnotarizealtool.html)

Notarize with altool

[](tvOS-introducing.html)

tvOS

# Deliver applications to the Mac App Store

This page has information about Mac App Store delivery requirements.

## Delivery requirements

If you want to distribute your application to the Mac App Store, then the
upload process includes a similar content validation to [notarization](macos-
building-notarization.html), which means that you don’t have to notarize your
application. However, when you [build your macOS application](macos-
building.html), the Mac App Store has additional requirements.

### Validation

Before you build your application, enable the **Mac App Store Validation**
property. To do this:

  1. Open Project Settings (menu: **Edit** > **Project Settings**).
  2. Go to **Player** > **Other Settings** > **Mac App Store Options**.
  3. Enable **Mac App Store Validation**.

Enabling the **Mac App Store Validation** option means that your application
only runs when it holds a valid receipt from the Mac App Store. It prevents
people from running the application on a different computer than the one they
purchased.

### Signing identity

To distribute your application via the Mac App Store, Apple requires you to
use one of the following signing identities when you [code sign](macos-
building.html#code-signing) your application:

**Signing Identity** | **Format**  
---|---  
Mac App Distribution | `3rd Party Mac Developer Application: TTT`  
Apple Distribution | `Apple Distribution: TTT`  
  
**Note** : Replace `TTT` with your team identity.

### Submit a macOS application

For information on how to submit your application to the Mac App Store, refer
to the Submit and promote section in [Submitting apps to the Mac App
Store](https://developer.apple.com/macos/submit/).

## Additional resources

  * [Build a macOS application](macos-building.html)

[](macosnotarizealtool.html)

Notarize with altool

[](tvOS-introducing.html)

tvOS

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

