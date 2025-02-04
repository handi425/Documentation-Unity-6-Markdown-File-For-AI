[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPWindowsConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPWindowsConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPWindowsConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPWindowsConfiguration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPWindowsConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPWindowsConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPWindowsConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPWindowsConfiguration.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Setting up Unity IAP](UnityIAPSettingUp.html)
  * Configuring for Windows Store

[](UnityIAPGoogleConfiguration.html)

Configuring for Google Play Store

[](UnityIAPAmazonConfiguration.html)

Configuration for the Amazon Appstore

# Configuring for Windows Store

## Introduction

This guide describes the process of establishing the digital records and
relationships necessary for a Unity game to interact with an In-App Purchase
Store. The [Unity IAP](UnityIAP.html)Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) purchasing API is targeted.

In-App Purchase (IAP) is the process of transacting money for digital goods. A
platform’s Store allows purchase of Products representing digital goods. These
Products have an Identifier, typically of string datatype. Products have Types
to represent their durability: _subscription_ , _consumable_ (capable of being
rebought), and _non-consumable_ (capable of being bought once) are the most
common.

## Windows Store

### Introduction

Windows App Development offers both local and remote Windows Store client-
server IAP testing.

This page covers local testing with the emulator and a simulated billing
system, then Windows Store testing which limits app publication visibility to
those with the app’s link.

**Note** : This guide targets Windows 10 Universal SDK. Other Windows targets
are available.

**Note** : Unity versions 5.6+ support **IL2CPP** A Unity-developed scripting
back-end which you can use as an alternative to Mono when building projects
for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) Windows builds. Using Unity IAP for
IL2CPP on Windows with earlier versions of Unity generates a compilation
error.

### Getting started

  1. Write a game implementing Unity IAP. Refer to [Unity IAP Initialization](UnityIAPInitialization.html).

  2. Keep the game’s product identifiers on-hand for use in Microsoft’s Windows Dev Center Dashboard to perform remote Windows Store testing later. 

![](../uploads/Main/IAPWindowsImage0.png)

### Test IAP locally

Microsoft offers a simulated billing system, permitting local testing of IAP.
This removes the need to configure anything on the Windows Dev Center or
communicate with the Windows Store via the app for initial integration
testing.

[Configuring local
testing](http://docs.unity3d.com/Manual/UnityIAPUniversalWindows.html) is far
simpler than for remote Store testing, although it requires temporary code
changes to the app which need to be removed before app publication.

To test IAP locally:

  1. Activate the simulated billing system in code where Unity IAP is initialized with its ConfigurationBuilder instance. 

**Warning** : Remove these code changes after testing, before publishing to
the Store; otherwise the app will not transact any real money via IAP!

![](../uploads/Main/IAPWindowsImage1.png)

  2. Build the application in Unity for **Universal Windows Platform**.

  3. Open the application in Visual Studio and run the Local Machine target for x86.

  4. Test IAP.

  5. Remove the simulated billing system from code.

### Register the App on the Windows Store

Once basic IAP functionality has been tested locally, you can more confidently
begin working with the Windows Store. This test confirms that the app has all
necessary IAPs registered correctly to permit purchasing.

For testing IAP and publication use the [Windows Dev
Center](https://dev.windows.com/en-us/publish) and configure the app with a
limited visibility. This limits the app’s visibility to those who have its
direct link.

**Note** : Testing on the Store also requires Certification, which might serve
as an obstacle to testing. It is therefore important to complete testing
locally before proceeding to testing with Windows Store.

  1. In the Dev Center [create a new app](https://dev.windows.com/en-us/overview).

![](../uploads/Main/IAPWindowsImage2.png)

  2. Reserve the app name. 

![](../uploads/Main/IAPWindowsImage3.png)

  3. To test IAP with the Windows Store, the Windows Dev Center needs the published app. Click **Pricing and availability** and limit the app’s Store visibility so that it is only available to users who have the app’s direct link.

![](../uploads/Main/IAPWindowsImage4.png)

  4. “Distribution and visibility” has a list of the Store’s available [publication behaviors](https://msdn.microsoft.com/en-us/library/windows/apps/mt148548.aspx#dist_vis). Select **Hide this app in the Store**. 

![](../uploads/Main/IAPWindowsImage5.png)

  5. Collect the direct link. This will be used to install the app on a Windows 10 device for [testing](https://msdn.microsoft.com/en-us/library/windows/apps/mt148561.aspx). 

![](../uploads/Main/IAPWindowsImage6.png)

  6. Submit the app for Certification. 

Submissions might take many hours to complete, and blocking issues might be
raised by Microsoft Certification, which you will need to address before the
submission passes successfully.

### Add In-App Products on the Store

Add each IAP, setting the price to be “free” so that no money will be
transacted during testing. After the test is completed, reconfigure the IAP
with the desired price and republish it. Refer to [IAP
Submissions](https://msdn.microsoft.com/en-
us/library/windows/apps/mt148551.aspx).

  1. In the new app’s “App overview” page, click **Create a new IAP** .

![](../uploads/Main/IAPWindowsImage7.png)

  2. Enter the product ID.

![](../uploads/Main/IAPWindowsImage8.png)

  3. Configure the type, price, and language. 

**Note** : For **Pricing and availability** choose **free** for testing
purposes to avoid incurring unnecessary financial charges. When you finish
testing, yo can then update and re-submit each IAP with the desired price in
preparation for release to the public.

![](../uploads/Main/IAPWindowsImage9.png)

Select **Properties** to set the type.

![](../uploads/Main/IAPWindowsImage10.png)

Select **Pricing and availability** to set the price choosing **Free** as
explained above.

![](../uploads/Main/IAPWindowsImage11.png)

Select **Manage languages** and declare the supported languages.

![](../uploads/Main/IAPWindowsImage12.png)

Select the declared language when returned to the IAP overview.

![](../uploads/Main/IAPWindowsImage13.png)

Populate the Title, Description and Icon.

![](../uploads/Main/IAPWindowsImage14.png)

  4. Submit the IAP for Certification. 

Similar to apps, IAP submissions might take many hours to complete, and
blocking issues might be raised by Microsoft Certification, which you will
need to address before the submission passes successfully.

![](../uploads/Main/IAPWindowsImage15.png)

### Test IAP with the Store

These steps follow a branch of the beta test process made possible with
Windows Store. This involves limiting the visibility of the app itself,
negating discovery by the public through the “Search Store” function. For more
information, refer to Windows Dev Center resources on [beta
testing](https://msdn.microsoft.com/en-
us/library/windows/apps/xaml/mt188751.aspx) and [targeted
distribution](https://msdn.microsoft.com/en-
us/library/windows/apps/mt185377.aspx).

  1. Confirm both the app and IAPs have completed Certification.

  2. Install the app on a Windows 10 device via the direct link, generated above.

  3. Test IAP.

  4. After passing test, update the IAP with the desired public pricing, update the app visibility settings to share with the general public, and submit both kinds of changes for final Certification.

* * *

• 2017–05–16 Page amended  

[](UnityIAPGoogleConfiguration.html)

Configuring for Google Play Store

[](UnityIAPAmazonConfiguration.html)

Configuration for the Amazon Appstore

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

