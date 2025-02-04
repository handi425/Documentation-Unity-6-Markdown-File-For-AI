[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/play-asset-delivery.html)
  * [中文](/cn/current/Manual/play-asset-delivery.html)
  * [日本語](/ja/current/Manual/play-asset-delivery.html)
  * [한국어](/kr/current/Manual/play-asset-delivery.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/play-asset-delivery.html)
  * [中文](/cn/current/Manual/play-asset-delivery.html)
  * [日本語](/ja/current/Manual/play-asset-delivery.html)
  * [한국어](/kr/current/Manual/play-asset-delivery.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Android application size restrictions](android-application-size-restrictions.html)
  * Play Asset Delivery

[](android-apk-expansion-files-host.html)

Host APK expansion files

[](android-asset-packs-in-unity.html)

Asset packs in Unity

# Play Asset Delivery

Play Asset Delivery (PAD) is the asset splitting solution for the [Android App
Bundle](https://developer.android.com/guide/app-bundle) (AAB) publishing
format. PAD uses asset packs to store additional assets such as textures,
sounds, and meshes. Google hosts and serves asset packs on Google Play, which
means you don’t need to create a content delivery network to send application
resources to users. For more information about PAD, refer to Android
documentation on [Play Asset
Delivery](https://developer.android.com/guide/playcore/asset-delivery).

PAD is only available for Google Play and enables applications to be larger
than the Google Play application size limit of 200MB.

**Important** : If you have a large application and want to publish it to
[digital distribution services](android-distribution.html) that don’t support
the AAB publishing format, you must use the **APK** The Android Package format
output by Unity. An APK is automatically deployed to your device when you
select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) publishing format and [APK expansion
files](android-OBBsupport.html).

**Topic** | **Description**  
---|---  
[Asset packs in Unity](android-asset-packs-in-unity.html) | Learn how asset packs work in Unity.  
[Set up Play Asset Delivery](android-asset-packs-set-up.html) | Configure your Unity project to produce an AAB that contains asset packs.  
[Create a custom asset pack](android-asset-packs-create-custom.html) | Create a custom asset pack to store additional assets for an application.  
[Manage asset packs at runtime](android-asset-packs-manage.html) | Download and access asset packs at runtime.  
  
**Notes:**

  * All versions of Unity from 2021.3 support Play Asset Delivery.
  * Unity doesn’t support [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery).

## Additional resources

  * [Android application publishing format](android-BuildProcess.html#publishing-format)

[](android-apk-expansion-files-host.html)

Host APK expansion files

[](android-asset-packs-in-unity.html)

Asset packs in Unity

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

