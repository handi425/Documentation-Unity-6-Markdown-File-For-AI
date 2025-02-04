[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPAmazonConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPAmazonConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPAmazonConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPAmazonConfiguration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPAmazonConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPAmazonConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPAmazonConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPAmazonConfiguration.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Setting up Unity IAP](UnityIAPSettingUp.html)
  * Configuration for the Amazon Appstore

[](UnityIAPWindowsConfiguration.html)

Configuring for Windows Store

[](UnityIAPCodelessIAP.html)

Codeless IAP

# Configuration for the Amazon Appstore

## Introduction

This guide describes the process of setting up the Amazon Appstore for use
with the Unity in-app purchasing (IAP) system. This includes establishing the
digital records and relationships that are required to interact with the
**Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) API, setting up an Amazon developer
account, and testing and publishing a Unity IAP application.

As with other platforms, the Amazon store allows for the purchase of virtual
goods and managed products. These digital products are identified using a
string identifier and an additional type to define durability, with choices
including subscription (capable of being subscribed to), consumable (capable
of being rebought), and non-consumable (capable of being bought once).

## Cross-store implementation of in-app purchases

There are cross-store installation issues with publishing to multiple Android
IAP stores (for example, Amazon and Google) simultaneously and shared Android
bundle identifiers. For more information, refer to [Cross-store installation
issues with Android in-app purchase
stores](UnityIAPCrossStoreInstallationIssues.html).

## Amazon Appstore

### Getting started

  1. Set up an Amazon developer account at the [Amazon developer portal](https://developer.amazon.com/).
  2. Write a game implementing the Unity IAP API. Refer to the guides on [Unity IAP initialization](UnityIAPInitialization.html). Use the Amazon Appstore for apps with no restrictions on IAP items.

### Device setup

  1. For Android devices, download and install the [Amazon Appstore](https://www.amazon.com/appstore_android_app).

  2. For FireOS devices, the Amazon Appstore should come pre-installed.

**Note** : Although you can freely target FireOS devices, FireOS is not a
Unity-supported platform.

  3. After you have installed the Amazon Appstore, install the [Amazon App Tester](http://www.amazon.com/Amazon-App-Tester/dp/B00BN3YZM2/).

![](../uploads/Main/AmazonConfiguration-AmazonAppTester.jpg)

  4. Set up the Android SDK 
    1. To install and watch the Android debug log, ensure you have the [Android SDK](https://developer.android.com/studio/install.html) installed. Download the relevant command line tools package from the Android SDK install page and extract them to your computer.
    2. Confirm that the SDK recognizes the attached Android device through the command-line **adb** An Android Debug Bridge (ADB). You can use an ADB to deploy an Android package (APK) manually after building. [More info](https://developer.android.com/studio/command-line/adb.html)  
See in [Glossary](Glossary.html#ADB) tool. For example:

    
    
    |[11:07:01] user@laptop:/Applications | $ adb devices
    List of devices attached
    00DA0807526300W5    device
    

### Unity app setup

Setting up to use Unity’s IAP takes a few steps.

  1. Import the Unity IAP **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in). For more information, refer to
[Setting up Unity IAP](UnityIAPSettingUp.html) (Unity 5.3 or later).

  2. Set the IAP target store. You should already have an Android app set up. Set the target store using **Unity IAP’s Window > Unity IAP > Android > Target Amazon** menu item. This is used to toggle between Google, Amazon, and other Android stores.

![](../uploads/Main/AmazonConfiguration-TargetAmazonMenu.jpg)

Alternatively, call the API:

    
    
    UnityPurchasingEditor.TargetAndroidStore(AndroidStore.AmazonAppStore)
    

### Amazon Appstore setup

You do not have to download Amazon’s native IAP plug-in when preparing to use
the Amazon stores, because all of the functionality that it provides is
already included in Unity’s IAP service.

  1. Add your app. From the Amazon Developer Portal select **Add a New App**.

![](../uploads/Main/AmazonConfiguration-AddNewApp.png)

  2. Set up your catalog. Using the product descriptions you prepared earlier, add the items to the Amazon catalog using the Amazon Developer Portal. Navigate to your app’s page, and find the **In-App Items section**. Use the **Add a Consumable** , **Add an Entitlement** , or **Add a Subscription** buttons to set up your catalog.

![](../uploads/Main/AmazonConfiguration-SetUpCatalog.png)

[](UnityIAPWindowsConfiguration.html)

Configuring for Windows Store

[](UnityIAPCodelessIAP.html)

Codeless IAP

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

