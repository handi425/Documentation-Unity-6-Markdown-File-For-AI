[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-troubleshooting.html)
  * [中文](/cn/current/Manual/udp-troubleshooting.html)
  * [日本語](/ja/current/Manual/udp-troubleshooting.html)
  * [한국어](/kr/current/Manual/udp-troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-troubleshooting.html)
  * [中文](/cn/current/Manual/udp-troubleshooting.html)
  * [日本語](/ja/current/Manual/udp-troubleshooting.html)
  * [한국어](/kr/current/Manual/udp-troubleshooting.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * UDP troubleshooting

[](udp-sdk-data-collection.html)

UDP SDK data collection

[](Glossary.html)

Glossary

# UDP troubleshooting

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
## Incorrect UDP implementation

An incorrect implementation of UDP in your game client could prevent users
from purchasing IAP products. Typical symptoms of such a problem in your game
include:

  * The wallet doesn’t appear when invoked

  * In-app purchases are unresponsive If these symptoms occur in your generic UDP build, resolve them before you repack your game.

## No IAPs are displayed in the UDP console

Make sure you push your IAP Catalog information in the Editor.

## Error: Packing Failed: No UDP SDK detected

This can happen with an implementation via **Unity IAP** Abbreviation of Unity
**In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP), if you forget to set UDP as the
build target.

It can also happen if you use the Minify option while building your **APK**
The Android Package format output by Unity. An APK is automatically deployed
to your device when you select File > Build & Run. [More info](android-
BuildProcess.html)  
See in [Glossary](Glossary.html#APK); UDP may not be able to find
files/directories that it needs because of it. Keep UDP-related packages in a
customized proguard file (or disable Minify option) and rebuild your game.

## UDP Sandbox: login screen doesn’t appear

The login screen in the Sandbox can fail to appear if the Init() method has
not been implemented properly. The login screen is displayed when Init() is
called. Init() is successful only when the login is successful. Unity
recommends to implement Init() when your game launches.

[](udp-sdk-data-collection.html)

UDP SDK data collection

[](Glossary.html)

Glossary

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

