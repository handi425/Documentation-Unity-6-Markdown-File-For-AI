[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-getting-started.html)
  * [中文](/cn/current/Manual/udp-getting-started.html)
  * [日本語](/ja/current/Manual/udp-getting-started.html)
  * [한국어](/kr/current/Manual/udp-getting-started.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-getting-started.html)
  * [中文](/cn/current/Manual/udp-getting-started.html)
  * [日本語](/ja/current/Manual/udp-getting-started.html)
  * [한국어](/kr/current/Manual/udp-getting-started.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * Getting started with UDP

[](udp.html)

Unity Distribution Portal

[](udp-distribution.html)

Distributing your game with UDP

# Getting started with UDP

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
## UDP implementation

Unity recommends implementing UDP in your game development cycle towards the
end of the development cycle, for example when you have decided what your
game’s purchasable in-app products will be. This makes it easier to implement
UDP in your back-catalog games to give them a new lease of life on new app
stores.

You can implement UDP in your game in one of the following ways.

  * Using the UDP Package only
  * Using the UDP package and **Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) package (for Unity IAP package
versions 2.0.0+)

  * Using Unity IAP only (for Unity IAP package versions 1.22.0–1.23.5)

The implementation you choose does not affect the UDP console.

### Using the UDP Package

This implementation is similar to the Google Play In-App Billing
implementation. If you have previously configured your game for Google Play
then Unity recommends using the UDP package.

The UDP package is available from Unity Package Manager or from the Unity
Asset Store.

For standalone UDP package installations, see [Installing the UDP
package](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/getting-
started.html).

### Using the UDP package and Unity IAP

The Unity IAP package version 2.0.0 and above does not contain the UDP DLL.
This requires the UDP package version 2.0.0 and above. From these versions on,
[install the UDP
package](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/getting-
started.html) and install the Unity IAP package from the Asset Store.

### Using Unity IAP

If your game already uses Unity IAP, you can continue to use the Unity IAP
package.

**Note** : Unity recommends using the UDP package along with the Unity IAP
package version 2.0.0+, available from the [Asset
Store](https://assetstore.unity.com/packages/add-ons/services/billing/unity-
iap-68207)A growing library of free and commercial assets created by Unity and
members of the community. Offers a wide variety of assets, from textures,
models and animations to whole project examples, tutorials and Editor
extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore)..

UDP is included in Unity IAP from version 1.22.0 - 1.23.5. If you use the
Unity IAP package (1.22.0 - 1.23.5) do not install the UDP package separately.
To check which Unity IAP version is installed, go to **Services** > **Unity
IAP** > **IAP Updates**. Follow the general implementation guidance of [Unity
IAP’s documentation](https://docs.unity3d.com/Manual/UnityIAP.html) before you
[implement your IAP items with Unity IAP](udp-service-
interoperability.html#iap).

If using the Unity IAP package, you can implement IAP items in your game using
code, or a codeless implementation. For better integration with UDP, implement
IAP using code.

## System requirements

UDP is supported in Unity 5.6.1 or higher. Unity recommends to use 2018.4 or
above.

From the following package versions and above, you can use the UDP and Unity
IAP packages together:

  * UDP - 2.0.0
  * Unity IAP - 2.0.0 (Asset Store version)

## Accessing the UDP console

To access the UDP console, go to the [Unity
Dashboard](https://distribute.dashboard.unity.com) and select Distribution
Portal.

To access the UDP console from the Unity Editor, select **Services** > **Unity
Distribution Portal** > **Configure**. In the Unity Distribution Portal
settings, select **Go to UDP console**.

[](udp.html)

Unity Distribution Portal

[](udp-distribution.html)

Distributing your game with UDP

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

