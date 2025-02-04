[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPValidatingReceipts.html)
  * [中文](/cn/current/Manual/UnityIAPValidatingReceipts.html)
  * [日本語](/ja/current/Manual/UnityIAPValidatingReceipts.html)
  * [한국어](/kr/current/Manual/UnityIAPValidatingReceipts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPValidatingReceipts.html)
  * [中文](/cn/current/Manual/UnityIAPValidatingReceipts.html)
  * [日本語](/ja/current/Manual/UnityIAPValidatingReceipts.html)
  * [한국어](/kr/current/Manual/UnityIAPValidatingReceipts.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Receipt validation

[](UnityIAPPurchaseReceipts.html)

Purchase Receipts

[](UnityIAPStoreExtensions.html)

Store Extensions

# Receipt validation

Receipt validation helps you prevent users from accessing content they have
not purchased.

## Point of validation

It is best practice to validate the receipt at the point where your
application’s content is distributed.

  * **Local validation:** For client-side content, where all content is contained in the application and is enabled once purchased, the validation should take place on the target device, without the need to connect to a remote server. Unity IAP is designed to support local validation within your application. See **Local validation** below for more information.
  * **Remote validation:** For server-side content, where content is downloaded once purchased, the validation should take place on the server before the content is released. Unity does not offer support for server-side validation; however, third-party solutions are available, such as Nobuyori Takahashi’s [IAP project](https://github.com/voltrue2/in-app-purchase).

## Local validation

**Important** : While Unity IAP provides a local validation method, local
validation is more vulnerable to fraud. Validating sensitive transactions
server-side where possible is considered best practice. For more information,
please see [Apple](https://developer.apple.com/documentation/storekit/in-
app_purchase/choosing_a_receipt_validation_technique) and
[Android](https://developer.android.com/google/play/billing/security)’s
documentation on fraud prevention.

If the content that the user is purchasing already exists on the device, the
application simply needs to make a decision about whether to unlock it.

Unity IAP provides tools to help you hide content and to validate and parse
receipts through Google Play and Apple stores.

### Obfuscating encryption keys

Receipt validation is performed using known encryption keys. For your
application, this is an encrypted Google Play public key, and/or Apple’s root
certificate.

If a user can replace these, they can defeat your receipt validation checks,
so it is important to make it difficult for a user to easily find and modify
these keys.

Unity IAP provides a tool that can help you obfuscate your encryption keys
within your Application. This confuses or jumbles the keys so that it is much
harder for a user to acces them. In the Unity menu bar, go to **Window** >
**Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) > **IAP Receipt Validation
Obfuscator**.

![The Obfuscator window](../uploads/Main/IAPObfuscator.png) The Obfuscator
window

This window encodes both Apple’s root certificate (which is bundled with Unity
IAP) and your Google Play public key (from the application’s [Google Play
Developer Console’s Services &
APIs](https://developer.android.com/google/play/licensing/setting-up.html)
page) into two different C# files: **AppleTangle** and **GooglePlayTangle**.
These are added to your project for use in the next section.

Note that you do not have to provide a Google Play public key if you are only
targeting Apple’s stores, and vice versa.

### Validating receipts

Use the `CrossPlatformValidator` class for validation across both Google Play
and Apple stores.

You must supply this class with either your Google Play public key or Apple’s
root certificate, or both if you wish to validate across both platforms.

The `CrossPlatformValidator` performs two checks:

  * Receipt authenticity is checked via signature validation.
  * The application bundle identifier on the receipt is compared to the one in your application. An **InvalidBundleId** exception is thrown if they do not match.

Note that the validator only validates receipts generated on Google Play and
Apple platforms. Receipts generated on any other platform, including fakes
generated in the Editor, throw an **IAPSecurityException**.

If you try to validate a receipt for a platform that you haven’t supplied a
secret key for, a **MissingStoreSecretException** is thrown.

    
    
    public PurchaseProcessingResult ProcessPurchase (PurchaseEventArgs e)
    {
        bool validPurchase = true; // Presume valid for platforms with no R.V.
    
        // Unity IAP's validation logic is only included on these platforms.
    #if UNITY_ANDROID || UNITY_IOS || UNITY_STANDALONE_OSX
        // Prepare the validator with the secrets we prepared in the Editor
        // obfuscation window.
        var validator = new CrossPlatformValidator(GooglePlayTangle.Data(),
            AppleTangle.Data(), Application.bundleIdentifier);
    
        try {
            // On Google Play, result has a single product ID.
            // On Apple stores, receipts contain multiple products.
            var result = validator.Validate(e.purchasedProduct.receipt);
            // For informational purposes, we list the receipt(s)
            Debug.Log("Receipt is valid. Contents:");
            foreach (IPurchaseReceipt productReceipt in result) {
                Debug.Log(productReceipt.productID);
                Debug.Log(productReceipt.purchaseDate);
                Debug.Log(productReceipt.transactionID);
            }
        } catch (IAPSecurityException) {
            Debug.Log("Invalid receipt, not unlocking content");
            validPurchase = false;
        }
    #endif
    
        if (validPurchase) {
            // Unlock the appropriate content here.
        }
    
        return PurchaseProcessingResult.Complete;
    }
    
    

It is important you check not just that the receipt is valid, but also what
information it contains. A common technique by users attempting to access
content without purchase is to supply receipts from other products or
applications. These receipts are genuine and do pass validation, so you should
make decisions based on the product IDs parsed by the
**CrossPlatformValidator**.

### Store-specific details

Different stores have different fields in their purchase receipts. To access
store-specific fields, `IPurchaseReceipt` can be downcast to two different
subtypes: `GooglePlayReceipt` and `AppleInAppPurchaseReceipt`.

    
    
    var result = validator.Validate(e.purchasedProduct.receipt);
    Debug.Log("Receipt is valid. Contents:");
    foreach (IPurchaseReceipt productReceipt in result) {
        Debug.Log(productReceipt.productID);
        Debug.Log(productReceipt.purchaseDate);
        Debug.Log(productReceipt.transactionID);
    
        GooglePlayReceipt google = productReceipt as GooglePlayReceipt;
        if (null != google) {
            // This is Google's Order ID.
            // Note that it is null when testing in the sandbox
            // because Google's sandbox does not provide Order IDs.
            Debug.Log(google.transactionID);
            Debug.Log(google.purchaseState);
            Debug.Log(google.purchaseToken);
        }
    
        AppleInAppPurchaseReceipt apple = productReceipt as AppleInAppPurchaseReceipt;
        if (null != apple) {
            Debug.Log(apple.originalTransactionIdentifier);
            Debug.Log(apple.subscriptionExpirationDate);
            Debug.Log(apple.cancellationDate);
            Debug.Log(apple.quantity);
        }
    }
    

### Parsing raw Apple receipts

Use the `AppleValidator` class to extract detailed information about an Apple
receipt. Note that this class only works with iOS App receipts from version
7.0 onwards, not Apple’s deprecated transaction receipts.

    
    
    #if UNITY_ANDROID || UNITY_IOS || UNITY_STANDALONE_OSX
    var builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
    // Get a reference to IAppleConfiguration during IAP initialization.
    var appleConfig = builder.Configure<IAppleConfiguration>();
    var receiptData = System.Convert.FromBase64String(appleConfig.appReceipt);
    AppleReceipt receipt = new AppleValidator(AppleTangle.Data()).Validate(receiptData);
    
    Debug.Log(receipt.bundleID);
    Debug.Log(receipt.receiptCreationDate);
    foreach (AppleInAppPurchaseReceipt productReceipt in receipt.inAppPurchaseReceipts) {
        Debug.Log(productReceipt.transactionIdentifier);
        Debug.Log(productReceipt.productIdentifier);
    }
    #endif
    

The `AppleReceipt` type models Apple’s ASN1 receipt format. See [Apple’s
documentation](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#/apple_ref/doc/uid/TP40010573-CH106-SW1)
for an explanation of its fields.

[](UnityIAPPurchaseReceipts.html)

Purchase Receipts

[](UnityIAPStoreExtensions.html)

Store Extensions

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

