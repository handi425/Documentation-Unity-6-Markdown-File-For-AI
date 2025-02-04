[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-asset-packs-set-up.html)
  * [中文](/cn/current/Manual/android-asset-packs-set-up.html)
  * [日本語](/ja/current/Manual/android-asset-packs-set-up.html)
  * [한국어](/kr/current/Manual/android-asset-packs-set-up.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-asset-packs-set-up.html)
  * [中文](/cn/current/Manual/android-asset-packs-set-up.html)
  * [日本語](/ja/current/Manual/android-asset-packs-set-up.html)
  * [한국어](/kr/current/Manual/android-asset-packs-set-up.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Android application size restrictions](android-application-size-restrictions.html)
  * [Play Asset Delivery](play-asset-delivery.html)
  * Set up Play Asset Delivery

[](android-asset-packs-in-unity.html)

Asset packs in Unity

[](android-asset-packs-create-custom.html)

Create a custom asset pack

# Set up Play Asset Delivery

[Play Asset Delivery](play-asset-delivery.html) is the asset splitting
solution for [Android App Bundles](https://developer.android.com/guide/app-
bundle) (AAB). To use Play Asset Delivery, set up your project to:

  1. Use the AAB publishing format. For information on how to do this, refer to [Publishing format](android-BuildProcess.html#publishing-format).
  2. Split the application binary. For information on how to do this, refer to [Splitting the application binary](android-optimize-distribution-size.html#splitting-the-application-binary). If **Split Application Binary** is grayed out, it means your current Unity Editor version doesn’t support Play Asset Delivery. To resolve this, update the Unity Editor.

When you build your application, Unity creates an AAB that includes your
application split into a [base
module](https://developer.android.com/guide/app-bundle/configure-base) and
asset packs. For more information, refer to [Asset packs in Unity](android-
asset-packs-in-unity.html).

**Important** : Unity uses the `PLAY_ASSET_PACKS` [Gradle template](android-
gradle-template-variables.html) variable to specify which asset packs to
include in the Android App Bundle. If you use a custom **Gradle** An Android
build system that automates several build processes. This automation means
that many common build errors are less likely to occur. [More info](android-
gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) template that was created before Unity
supported Play Asset Delivery, your template won’t contain this variable.
Because Unity automatically generates the values for this variable, it’s best
practice to recreate your Gradle template file from the current Unity version
and reapply your modifications on top.

## Additional resources

  * [Asset packs in Unity](android-asset-packs-in-unity.html)
  * [Create a custom asset pack](android-asset-packs-create-custom.html)
  * [Manage asset packs at runtime](android-asset-packs-manage.html)

[](android-asset-packs-in-unity.html)

Asset packs in Unity

[](android-asset-packs-create-custom.html)

Create a custom asset pack

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

