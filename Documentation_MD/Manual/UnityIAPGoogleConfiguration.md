[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPGoogleConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPGoogleConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPGoogleConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPGoogleConfiguration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPGoogleConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPGoogleConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPGoogleConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPGoogleConfiguration.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Setting up Unity IAP](UnityIAPSettingUp.html)
  * Configuring for Google Play Store

[](UnityIAPAppleConfiguration.html)

Configuring for Apple App Store and Mac App Store

[](UnityIAPWindowsConfiguration.html)

Configuring for Windows Store

# Configuring for Google Play Store

## Introduction

This guide describes the process of establishing the digital records and
relationships necessary for a Unity game to interact with an In-App Purchase
Store. The [Unity IAP](UnityIAP.html)Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) purchasing API is targeted.

In-App Purchase (IAP) is the process of transacting money for digital goods. A
platform’s Store allows the purchase of Products, representing digital goods.
These Products have an Identifier, typically of string datatype. Products have
Types to represent their durability: _subscription_ , _consumable_ (capable of
being rebought), and _non-consumable_ (capable of being bought once) are the
most common.

## Google Play Store

### Getting Started

  1. Write a game implementing Unity IAP. See [Unity IAP Initialization](UnityIAPInitialization.html) and [the Sample IAP Project](https://forum.unity.com/threads/sample-iap-project.529555/).

  2. Keep the game’s product identifiers on-hand for [Google Play](UnityIAPGooglePlay.html) Developer Console use later. 

![gold50](../uploads/Main/IAPGoogleImage0.png) gold50

  3. Build a [signed non-Development Build Android APK](android.html) from your game. 

**TIP:** Make sure you safely store your keystore file. The original keystore
is always required to update a published Google Play application.

**TIP:** Reuse the Bundle Version Code from your last uploaded **APK** The
Android Package format output by Unity. An APK is automatically deployed to
your device when you select File > Build & Run. [More info](android-
BuildProcess.html)  
See in [Glossary](Glossary.html#APK) during local testing to permit side-
loading without first being required to upload the changed APK to the
Developer Console. See the settings for the [Android platform Player](class-
PlayerSettingsAndroid.html).

### Register the Application

From the Google Account that will publish the game, register the Android
application with the [Google Play Developer
Console](https://play.google.com/apps/publish).

**NOTE:** This guide uses the [Google Play License Testing
approach](http://developer.android.com/google/play/billing/billing_testing.html)
for testing in-app purchase integration.

  1. Choose **Create app**.

![All apps](../uploads/Main/IAPGoogleImage1.png) All apps

  2. Give the application an App name and select the appropriate options for your game. 

![Create app](../uploads/Main/IAPGoogleImage2.png) Create app

  3. Navigate to **Testing/Closed testing** in the left nav and choose **Create track**. Select your APK and upload it. Also complete the basic Dashboard requirements, upload screenshots and add a Short and Full description. You can also create an Internal test track.

![Closed testing](../uploads/Main/IAPGoogleImage3.png) Closed testing

### Add In-App Purchases

Now that you have uploaded our first binary, you can add the IAP products.

  1. Navigate to **In-app Products** and choose **Create product**.

![In-app products](../uploads/Main/IAPGoogleImage4.png) In-app products

  2. Define the **Product ID** , product details and price. Remember to activate the product after saving. 

You can specify a consumable or non-consumable Product Type in **Managed
product**. **Subscription** is also supported by Unity IAP.

**NOTE** : The “Product ID” here is the same identifier used in the game
source code, added to the [Unity IAP ConfigurationBuilder] instance via
`AddProduct()` or `AddProducts()`, like “gold50”.

![50goldcoins](../uploads/Main/IAPGoogleImage5.png) 50goldcoins

### Test IAP

Add your testers to License Testing.

  1. Navigate to All Apps on your Google Developer dashboard. 

  2. Select **Settings/License Testing**. Add each Google Account email address. Save changes. 

![License testing](../uploads/Main/IAPGoogleImage6.png)

    
    
    NOTE: There may be a delay of several hours from the time you publish the APK. 
    

  1. When available, share the **Join on Android** link with testers. Ensure that testers can install the application from the store.

**Note:** To test updates retaining permission to purchase IAPS’s for free,
you may side-load applications, updating the existing store-downladed APK
install.

![My closed Track](../uploads/Main/IAPGoogleImage7.png) My closed Track

  1. To test the IAP, make a purchase on a device logged in with a Tester Google Account. A modified purchase dialog box appears to confirm the fact this product is under test and is free.

**WARNING** : If this dialog box does not appear, then the Tester Google
Account will be charged real money for the product.

![](../uploads/Main/IAPGoogleImage8.png)

[](UnityIAPAppleConfiguration.html)

Configuring for Apple App Store and Mac App Store

[](UnityIAPWindowsConfiguration.html)

Configuring for Windows Store

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

