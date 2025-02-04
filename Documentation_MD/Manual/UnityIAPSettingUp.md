[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPSettingUp.html)
  * [中文](/cn/current/Manual/UnityIAPSettingUp.html)
  * [日本語](/ja/current/Manual/UnityIAPSettingUp.html)
  * [한국어](/kr/current/Manual/UnityIAPSettingUp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPSettingUp.html)
  * [中文](/cn/current/Manual/UnityIAPSettingUp.html)
  * [日本語](/ja/current/Manual/UnityIAPSettingUp.html)
  * [한국어](/kr/current/Manual/UnityIAPSettingUp.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Setting up Unity IAP

[](UnityIAP.html)

Unity IAP

[](UnityIAPAppleConfiguration.html)

Configuring for Apple App Store and Mac App Store

# Setting up Unity IAP

**Note** : Screenshots and menu choices might differ between release versions.

## Overview

This document explains how to activate **In-App Purchasing** (IAP).

The **Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) package provides coded and codeless
approaches that you set up to: \- Allow users to buy items in your games. \-
Connect to stores so that you can obtain revenue from these purchases.

Here is an overview of the steps:

  * Define your In-app purchase strategy for this game.

  * Setup your project as a Unity service.

  * Activate IAP to automatically install the package.

  * Configure settings.

  * Create and catalog your the in-game items that you want to sell.

  * Use the Codeless IAP button to give users a way to buy items. Then, once you have the logic working, consider customizing the button look and feel. Or use the scripted IAP for a rich API to enhance this process. 

![](../uploads/Main/IAP-DemoButtons.png)

  * Connect your app to the relevant app-stores, such as Google, Apple, or Android. 

  * Add items to the stores.

Put it all together:

  * Configure your IAP using guidance from this doc, support, and the IAP forum.
  * Test everything.
  * Make it live.

You can also do many of these steps, or fine-tune what you create, with the
In-App Purchasing API.

**Note** : Versions of Unity IAP between 4.2.0 and 4.6.0 automatically install
Unity **Analytics** Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics). **Unity Analytics** A data
platform that provides analytics for your Unity game. [More
info](https://docs.unity.com/ugs/en-us/manual/analytics/manual/overview)  
See in [Glossary](Glossary.html#UnityAnalytics) is a paid service, and if your
usage exceeds the free tier limits, you will be responsible for paying for
your usage. To avoid using Unity Analytics, install Unity IAP 4.7.0 or later,
and/or remove Unity Analytics from your project (which you can learn more
about [here](https://forum.unity.com/threads/important-iap-sdk-usage-of-
analytics-changed-as-of-version-4-7-0.1301283/)).

## Getting Started

**Note** : The Samsung Galaxy store is now obsolete and is no longer supported
in the Unity In-App Purchasing package 4.0.0 and later. This guide to
configure the Samsung Galaxy store only applies to the IAP package version
3.1.0 and earlier. If you are using the Unity IAP package 4.0.0 and later and
you want to implement a Samsung Galaxy store, use the [Unity Distribution
Platform](https://docs.unity3d.com/Manual/udp.html) instead.

  1. Open your Unity project in the Unity Editor.

  2. Choose **Window\General\Services**. The services window will appear.

  3. Create a Project ID, then connect the project to an organization.

  4. Answer the **COPPA**(Children’s Online Privacy Protection Act) COPPA is a US law that applies to apps that collect personal information and are targeted to children under the age of 14. [More info](UnityAnalyticsCOPPA)  
See in [Glossary](Glossary.html#COPPA) compliance questions.

  5. The services window will display a list of services. Click **In-App Purchasing**.

![](../uploads/Main/IAP-ServicesList.png)

  6. The **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) window appears.

![](../uploads/Main/IAP-ProjectSettings.png)

  7. Activate the toggle next to **In-App Purchasing Settings** to **ON**.

This automatically installs the IAP package from the package manager,
providing you with new features and menu items to help you manage IAP.

## Next Steps

### Define your In-App Purchase strategy

Your task will be to create items for players to buy and obtain their
identifiers.

You must tie product identifiers (strings) to each item you are selling by
using a specified format. Some stores require that you customize the **Product
ID** for their stores.

#### Planning:

  * Define your strategy to determine when/how users can buy things
  * Define your pricing strategy
  * Define the types of products (subscriber, consumable, non consumable)

## Where to learn more

#### IAP Samples

  1. From the **IAP Project Settings Page** , select **Open Package Manager** from **Options**.
  2. Navigate to **In App Purchasing**. On the right information panel, find **Samples**.
  3. Expand **Samples** , then select **Import**.

![](../uploads/Main/IAP-Samples.png)

#### Forum tutorials

[Visit the Unity forum](https://forum.unity.com/threads/sample-iap-
project.529555/).

#### Unity Learn IAP classes

[Refer to the Unity Learn IAP classes](https://learn.unity.com/tutorial/unity-
iap).

## Troubleshooting

#### How to resolve compilation errors during upgrades

**Important notes if you are upgrading from Unity IAP version 2.x to future
versions.**

If you are updating from Unity IAP (com.unity.purchasing + the Asset Store
plugin) versions 2.x to future versions, to resolve compilation errors,
complete the following actions:

  * Move `IAPProductCatalog.json` and `BillingMode.json`from `Assets/Plugins/UnityPurchasing/Resources/` to `Assets/Resources/`
  * Move `AppleTangle.cs` and `GooglePlayTangle.cs` FROM: ‘Assets/Plugins/UnityPurchasing/generated’ TO: `Assets/Scripts/UnityPurchasing/generated`.
  * Remove all remaining **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) plugin folders and files in
`Assets/Plugins/UnityPurchasing` from your project.

#### Common Unity IAP integration compiler errors

The following error messages might indicate that Unity IAP is deactivated in
the Unity Cloud Services window, or that Unity is disconnected from the
Internet: * `CS0246` * `System.Reflection.ReflectionTypeLoadException` *
`UnityPurchasing/Bin/Stores.dll` * `UnityEngine.Purchasing`

To resolve these errors:

Reload the Services window by closing, then reopening it. After reloading,
ensure that the Unity IAP service is active. If this doesn’t work, try to
disconnect and reconnect to the Internet, then sign back into Unity Services
and re-activate Unity IAP.

**Note** : You must have an **Owner** or **Manager** role for the project.

[](UnityIAP.html)

Unity IAP

[](UnityIAPAppleConfiguration.html)

Configuring for Apple App Store and Mac App Store

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

