[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPPurchaseReceipts.html)
  * [中文](/cn/current/Manual/UnityIAPPurchaseReceipts.html)
  * [日本語](/ja/current/Manual/UnityIAPPurchaseReceipts.html)
  * [한국어](/kr/current/Manual/UnityIAPPurchaseReceipts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPPurchaseReceipts.html)
  * [中文](/cn/current/Manual/UnityIAPPurchaseReceipts.html)
  * [日本語](/ja/current/Manual/UnityIAPPurchaseReceipts.html)
  * [한국어](/kr/current/Manual/UnityIAPPurchaseReceipts.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Purchase Receipts

[](UnityIAPRestoringTransactions.html)

Restoring Transactions

[](UnityIAPValidatingReceipts.html)

Receipt validation

# Purchase Receipts

Unity IAP provides purchase receipts as a JSON hash containing the following
keys and values:

Key | Value  
---|---  
**Store** | The name of the store in use, such as **GooglePlay** or **AppleAppStore**  
**TransactionID** | This transaction’s unique identifier, provided by the store  
**Payload** | Varies by platform, details below.  
  
## iOS

Payload varies depending upon the device’s iOS version.

iOS version | Payload  
---|---  
**iOS >= 7** | payload is a base 64 encoded [App Receipt](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#/apple_ref/doc/uid/TP40010573-CH106-SW1).  
**iOS < 7** | payload is a [SKPaymentTransaction transactionReceipt](https://developer.apple.com/library/ios/documentation/StoreKit/Reference/SKPaymentTransaction_Class/).  
  
## Mac App Store

Payload is a base 64 encoded [App
Receipt](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#/apple_ref/doc/uid/TP40010573-CH106-SW1).

## Google Play

Payload is a JSON hash with the following keys and values:

Key | Value  
---|---  
**json** | A JSON encoded string provided by Google; [INAPP_PURCHASE_DATA](http://developer.android.com/google/play/billing/billing_reference.html)  
**signature** | A signature for the json parameter, as provided by Google; [INAPP_DATA_SIGNATURE](http://developer.android.com/google/play/billing/billing_reference.html)  
  
## Universal Windows Platform

Payload is an XML string as [specified by
Microsoft](https://msdn.microsoft.com/en-
US/library/windows/apps/windows.applicationmodel.store.currentapp.getappreceiptasync.aspx)

* * *

• 2017–05–16 Page amended  

[](UnityIAPRestoringTransactions.html)

Restoring Transactions

[](UnityIAPValidatingReceipts.html)

Receipt validation

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

