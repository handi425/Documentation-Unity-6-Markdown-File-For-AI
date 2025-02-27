[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPAppleConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPAppleConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPAppleConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPAppleConfiguration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPAppleConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPAppleConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPAppleConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPAppleConfiguration.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Setting up Unity IAP](UnityIAPSettingUp.html)
  * Configuring for Apple App Store and Mac App Store

[](UnityIAPSettingUp.html)

Setting up Unity IAP

[](UnityIAPGoogleConfiguration.html)

Configuring for Google Play Store

# Configuring for Apple App Store and Mac App Store

## Introduction

This guide describes the process of establishing the digital records and
relationships necessary for a Unity game to interact with an In-App Purchase
Store. The [Unity IAP](UnityIAP.html)Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) purchasing API is targeted.

In-App Purchase (IAP) is the process of transacting money for digital goods. A
platform’s Store allows purchase of Products, representing digital goods.
These Products have an Identifier, typically of string datatype. Products have
Types to represent their durability: _subscription_ , _consumable_ (capable of
being rebought), and _non-consumable_ (capable of being bought only once) are
the most common.

## Apple App Store

### Getting Started

  1. Write a game implementing Unity IAP. Refer to [Unity IAP Initialization](UnityIAPInitialization.html).

  2. Keep the game’s product identifiers on-hand for use in iTunes Connect later.

![](../uploads/Main/IAPAppleImage0.png)

### Register the Application

  1. In the [Apple Developer Center](https://developer.apple.com/account), navigate to the appropriate Identifiers section. 

  2. Add a new App ID to create a fundamental application entity with Apple. 

**NOTE:** Use an Explicit App ID. You cannot use Wildcard App IDs
(com.example.*) for applications that use In-App Purchases.

**NOTE:** The App ID is available to use in iTunes Connect after you create it
in the Developer Center.

![](../uploads/Main/IAPAppleImage1.png)

  3. Navigate to [iTunes Connect](https://itunesconnect.apple.com) and create an App, to establish a Store relationship with your game. 

![](../uploads/Main/IAPAppleImage2.png)

  4. Use the newly created App ID for the app’s Bundle ID. 

![](../uploads/Main/IAPAppleImage3.png)

### Add In-App Purchases

  1. Choose **Features** and add a new In-App Purchase with the plus (“+”) button. 

![](../uploads/Main/IAPAppleImage4.png)

  2. Choose a [Product Type](UnityIAPDefiningProducts.html). 

![](../uploads/Main/IAPAppleImage5.jpg)

  3. Specify the Product Identifier, and complete other fields as requested.

**Note** : The “Product ID” here is the same identifier used in the game
source code, added to the Unity IAP ConfigurationBuilder instance by using
**AddProduct()** or **AddProducts()**.

**Note** : When targeting multiple Apple device groups (for example, shipping
on both iOS and Mac) Apple requires usage of different, unique product
identifiers for each distinct device group. Use Unity IAP’s Purchasing.IDs
class and define a one-to-many mapping Product IDs to the store-specific
identifiers, and pass that mapping in when initializing IAP.

![](../uploads/Main/IAPAppleImage6.jpg)

  4. Result:

![](../uploads/Main/IAPAppleImage7.png)

### Test IAP

  1. Create **Sandbox Testers** using iTunes Connect for use on your test device’s iTunes Account. To do this, go to **iTunes Connect > Users and Roles**, and choose the plus (“+”) button. You must review [Apple’s Sandbox Tester documentation](https://developer.apple.com/library/ios/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/SettingUpUserAccounts.html#/apple_ref/doc/uid/TP40011225-CH25-SW9) as there are several additional important usage notes, and you must use a real email address to create Testers. 

**Note** : For more information, refer to the [iOS and Mac App Store
guides](UnityIAPiOSMAS.html).

**Tip** : To simplify managing the email address, use an email service capable
of sub-addressing (emailaccount+subaddress@example.com) such as Gmail, iCloud,
and Outlook.com. This allows one email account to receive email for multiple
sub-addresses.

![](../uploads/Main/IAPAppleImage8.png)

  2. Complete the user creation wizard. 

![](../uploads/Main/IAPAppleImage9.png)

  3. Build the Xcode project for your game by using Unity.

**Note** : Ensure the Bundle Identifier in Unity (**Edit** > **Project
Settings** , then select the **Other Settings** category, and navigate to the
**Bundle Identifier** section) matches that used in iTunes Connect.

  4. In your game’s Xcode project, ensure the Team (Project Navigator > your game Target > General > Identity > Team) is set to that of your Apple Developer account.

![](../uploads/Main/IAPAppleImage10.png)

#### For iOS

  1. Using the target iOS device, sign out of any existing Apple ID accounts. Only sign in as the Sandbox Tester when prompted by the app, later. Any subsequent purchases are routed through the Apple Sandbox instead of the Production Store.

![](../uploads/Main/IAPAppleImage11.png)

  2. Build and run the game on your iOS device. `UnityPurchasing.Initialize()` succeeds if everything has been correctly configured. 

  3. Test the IAP by making a purchase in the game on the device. A modified purchase dialog displays, explaining that this purchase is being performed in the Sandbox Environment. Use the Sandbox User Tester password when prompted for purchase. 

**Warning** : If the indicator is not present, then an account is charged real
money for the product.

![](../uploads/Main/IAPAppleImage12.png)

#### For Mac

  1. When building a desktop Mac build, select **Mac App Store Validation** within Unity’s Mac **Player** settings.

  2. After you have built your App, update its `info.plist` file with your bundle identifier and version strings. Right-click the .app file and select **Show Package Contents** , locate the `info.plist` file and update the `CFBundleIdentifier` string to your application’s bundle identifier.

  3. Sign, package, and install your application. Run the following commands from an OSX terminal, filling in “your.app” and “your.pkg” appropriately.

**Tip** : To sign the bundle, you might first need to remove the Contents.meta
file if it exists:
`your.app/Contents/Plugins/unitypurchasing.bundle/Contents.meta`

    1. `codesign -f --deep -s "3rd Party Mac Developer Application: " your.app/Contents/Plugins/unitypurchasing.bundle`

    2. `codesign -f --deep -s "3rd Party Mac Developer Application: " your.app`

    3. `productbuild --component your.app /Applications --sign "3rd Party Mac Developer Installer: " your.pkg`

  4. To install the package correctly, delete the unpackaged .app file before you run the newly created package and install it.

  5. Launch the app from the _Applications_ folder. The first time you do so, you are prompted to enter your iTunes account details, for which you can then make test purchases against the sandbox environment.

For more information on Apple App Store testing and signing, refer to [iOS and
Mac Extended Functionality](UnityIAPiOSMAS.html) and [Building your macOS
application](macos-building.html).

[](UnityIAPSettingUp.html)

Setting up Unity IAP

[](UnityIAPGoogleConfiguration.html)

Configuring for Google Play Store

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

