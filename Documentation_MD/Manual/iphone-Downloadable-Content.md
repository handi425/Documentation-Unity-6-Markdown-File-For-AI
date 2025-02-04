[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/iphone-Downloadable-Content.html)
  * [中文](/cn/current/Manual/iphone-Downloadable-Content.html)
  * [日本語](/ja/current/Manual/iphone-Downloadable-Content.html)
  * [한국어](/kr/current/Manual/iphone-Downloadable-Content.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/iphone-Downloadable-Content.html)
  * [中文](/cn/current/Manual/iphone-Downloadable-Content.html)
  * [日本語](/ja/current/Manual/iphone-Downloadable-Content.html)
  * [한국어](/kr/current/Manual/iphone-Downloadable-Content.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Developing for iOS](ios-developing.html)
  * Prepare your application for in-app purchases

[](ios-authorizations-in-unity.html)

iOS authorizations in Unity

[](net-SocialAPI.html)

Social API

# Prepare your application for in-app purchases

In-app purchases (IAP) allow you to offer additional downloadable content in
your application, such as new levels or character cosmetics. You must
integrate with the StoreKit API within your application using a [native code
plug-in](./plug-ins.html) before you can set up in-app purchases. For more
information, refer to
[StoreKit](https://developer.apple.com/documentation/storekit) (Apple).

**Note** : The [Unity IAP
package](https://docs.unity3d.com/Packages/com.unity.purchasing@latest) can be
used to implement in-app purchases for iOS and other platforms you might want
to develop for.

## Organize your assets

The
[Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/)
package provides a ready-made system to manage and organize
[AssetBundles](AssetBundlesIntro.html) in your project. It’s recommended to
use the Addressables package rather than manage AssetBundles yourself.

## Download your assets

If you are managing AssetBundles yourself, it’s recommended to use
[UnityWebRequest](./web-request.html) to access any remote assets. If using
the
[Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/)
package, this will handle asset downloads for you.

**Note** : Apple might change the folder locations where you’re permitted to
write data. Make sure to check the latest Apple guidelines for the most up-to-
date information.

## Additional resources

  * [StoreKit](https://developer.apple.com/documentation/storekit) (Apple)
  * [Unity IAP package](https://docs.unity3d.com/Packages/com.unity.purchasing@4.11/manual/Overview.html)
  * [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/)
  * [AssetBundles](AssetBundlesIntro.html)

[](ios-authorizations-in-unity.html)

iOS authorizations in Unity

[](net-SocialAPI.html)

Social API

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

