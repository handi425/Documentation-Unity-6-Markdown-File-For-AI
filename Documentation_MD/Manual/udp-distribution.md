[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-distribution.html)
  * [中文](/cn/current/Manual/udp-distribution.html)
  * [日本語](/ja/current/Manual/udp-distribution.html)
  * [한국어](/kr/current/Manual/udp-distribution.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-distribution.html)
  * [中文](/cn/current/Manual/udp-distribution.html)
  * [日本語](/ja/current/Manual/udp-distribution.html)
  * [한국어](/kr/current/Manual/udp-distribution.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * Distributing your game with UDP

[](udp-getting-started.html)

Getting started with UDP

[](udp-implementing-iap.html)

Implementing IAP products

# Distributing your game with UDP

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
The steps below describe the overall process to publish a game to app stores
via UDP.

  1. [Creating a game in the UDP console](udp-distribution.html#create). 
    1. Entering your game info on the UDP console.
    2. Defining supported languages.
  2. [Implement UDP in your Unity project](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/getting-started.html). 
    1. Install the package.
    2. Link your project to the UDP client.
    3. Initialize the UDP SDK.
    4. Implement IAP (if applicable).
    5. Implement LicenceCheck for premium games (optional).
  3. [Build and test your game](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/building-your-game.html)
    1. Build your game **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK).

    2. Ensure all your IAP products are listed in the UDP console (if applicable).
    3. Test your game in the Sandbox.
  4. [Upload your game APK to the UDP console](udp-managing-and-publishing.html).
  5. Finalize the game information page in the UDP console. 
    1. Verify testing was successful.
    2. Upload your app signing private key.
    3. Set a premium price (if applicable).
    4. Localize your game information for additional languages (if applicable).
  6. [Release your game on UDP](udp-managing-and-publishing.html#release).
  7. [Publish your game to stores](udp-managing-and-publishing.html#publish).

The image below illustrates the overall workflow.

![The workflow.](../uploads/Main//UDPWorkflow.png) The workflow.

## Creating a game in the UDP console

To create a new game in the UDP console:

  1. In the My Games tab, select **Add Game**.
  2. Add a title for your game and select **Create New Game**.  
The Game Info page opens.

  3. Select **Save**.

This is the minimum required to create a new game in the UDP console. The next
step is to enter your game information.

When you create a new game in the UDP console it generates a UDP client and
UDP client ID. You must [link the UDP client to your
game](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/getting-
started.html%23linking) in the Unity Editor.

## Entering game information on the UDP console

To edit your game information on the UDP console:

  1. In the My games tab, select your game’s card.
  2. In the Game Info page, select **EDIT INFO** to enter edit mode. 
    1. Update your game information. Learn more about the requirements for the Game Info page.  
To help complete this information, you can also import metadata from Google
Play.

  3. To save changes select **SAVE**. To discard your changes, select **CANCEL**.

If you intend to provide descriptions for your game in multiple languages, add
your supported languages in the UDP console. Otherwise, implement UDP in your
project.

## Adding supported languages

When you add a language in the Game Info page, it copies the information from
the default version. Therefore, to reduce duplication of work, add as much
information as possible in the default version before you add more languages.
To add languages:

  1. In the Game Info page, select **EDIT INFO**.
  2. In the language dropdown, select **Manage languages**. 
    1. Select the languages you wish to support and select **Save**.
  3. In the Game Info page, select **Save**.

If you will use the bulk import feature to import IAP products, including
descriptions in multiple languages, you should first add the languages in the
UDP Console. Otherwise, the IAP descriptions would not be imported for those
languages.

## Implementing UDP in your project

Follow the steps to [get started with the UDP
package](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/getting-
started.html). This includes:

  1. Install the UDP package.
  2. Link your project to an existing UDP client ID.
  3. Initialize the SDK.
  4. If applicable, implement code in your game for: 
     * IAP
     * Premium games

[](udp-getting-started.html)

Getting started with UDP

[](udp-implementing-iap.html)

Implementing IAP products

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

