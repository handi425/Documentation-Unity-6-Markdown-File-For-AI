[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-sandbox-testing.html)
  * [中文](/cn/current/Manual/udp-sandbox-testing.html)
  * [日本語](/ja/current/Manual/udp-sandbox-testing.html)
  * [한국어](/kr/current/Manual/udp-sandbox-testing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-sandbox-testing.html)
  * [中文](/cn/current/Manual/udp-sandbox-testing.html)
  * [日本語](/ja/current/Manual/udp-sandbox-testing.html)
  * [한국어](/kr/current/Manual/udp-sandbox-testing.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * Testing your game in the UDP sandbox

[](udp-implementing-iap.html)

Implementing IAP products

[](udp-managing-and-publishing.html)

Managing and publishing your game on the UDP console

# Testing your game in the UDP sandbox

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
Before you can release your game for the first time and repack for the app
stores, test your game in the sandbox environment. You must:

  * Initialize UDP in the sandbox at least once (for all games) 
    * Call the Initialize() method
  * Complete an IAP purchase in the sandbox at least once (if your game has IAPs) 
    * Call the Purchase() method

This is to ensure that the UDP implementation works for a simple and nominal
case. Unity recommends you test your UDP methods more extensively. After your
first release, you don’t need to retest in the sandbox to release new
revisions of your game on UDP.

**Note** : If you test your game in the Unity Editor Play mode, all IAP
transactions are successful and are automatically consumed. This is not
connected to the UDP console and is not sufficient to clear sandbox testing.

To test your game in the sandbox:

  1. In the Unity Distribution Portal tab of the Project Settings window, go to the UDP Sandbox Test accounts section and create login credentials for the sandbox environment.  
If you have already added credentials in the UDP console, you can use those.

  2. Run your game on an Android device or emulator.  
When your game launches it should call the Initialize method, which displays
the login screen automatically in the sandbox environment. If you didn’t call
Initialize on game launch, trigger the necessary step to call Initialize.

    1. Enter your login credentials for the sandbox test account.  
This is all that’s required to check that the game initializes.

    2. For IAP games, make a purchase to test your IAP purchases.  
No real transaction is made in the sandbox environment.

When each test is successful:

  * The sandbox environment displays a toast notification
  * The UDP sandbox updates the [Sandbox Testing](udp-reference.html#sandbox) section of the UDP console to display a green **Tested** status for the corresponding test

When all required tests are successful, the left panel of the Game Info page
displays a green tick to confirm you’ve cleared sandbox testing. You can now
complete any remaining steps on your Game Info page to release your first
revision and submit it to stores.

The sandbox login credentials only work with the generic UDP build for the
sandbox environment. When UDP repacks your build for the real app stores, UDP
removes the sandbox environment and login page, and patches in the store-
specific SDK. The store-specific SDK in the build ensures IAP transactions
work with that store’s payment system.

**Note** : Sandbox mode also supports server-side validation.

## Troubleshooting

Check your UDP and/or IAP implementation if any IAP-related issues arise, such
as:

  * No login screen appearing
  * No IAP products retrieved
  * Unresponsive purchase buttons
  * Inability to complete a purchase

For further troubleshooting information, check the [UDP Package
documentation](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest)
or contact the UDP support team via the “Contact Support” link on the UDP
Console.

[](udp-implementing-iap.html)

Implementing IAP products

[](udp-managing-and-publishing.html)

Managing and publishing your game on the UDP console

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

