[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPRestoringTransactions.html)
  * [中文](/cn/current/Manual/UnityIAPRestoringTransactions.html)
  * [日本語](/ja/current/Manual/UnityIAPRestoringTransactions.html)
  * [한국어](/kr/current/Manual/UnityIAPRestoringTransactions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPRestoringTransactions.html)
  * [中文](/cn/current/Manual/UnityIAPRestoringTransactions.html)
  * [日本語](/ja/current/Manual/UnityIAPRestoringTransactions.html)
  * [한국어](/kr/current/Manual/UnityIAPRestoringTransactions.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Restoring Transactions

[](UnityIAPHandlingPurchaseFailures.html)

Handling purchase failures

[](UnityIAPPurchaseReceipts.html)

Purchase Receipts

# Restoring Transactions

When a user reinstalls your application they should be granted any Non-
Consumable or renewable Subscription products they already own. App stores
maintain a permanent record of each user’s Non-Consumable and renewable
Subscription products which **Unity IAP** Abbreviation of Unity **In App
Purchase**  
See in [Glossary](Glossary.html#UnityIAP) can retrieve. Non-renewing
subscriptions on Apple platforms cannot be restored. If you use non-renewing
subscription products on Apple platforms, it is up to you to keep a record of
the active subscriptions and sync the subscription between devices.

On platforms that support it (e.g. Google Play and Universal Windows
Applications) Unity IAP automatically restores any products the user owns
during the first initialization following reinstallation; the
`ProcessPurchase` method of your `IStoreListener` will be called for each
owned item.

On Apple platforms users must enter their password to retrieve previous
transactions so your application must provide users with a button letting them
do so. During this process the `ProcessPurchase` method of your
`IStoreListener` will be invoked for any items the user already owns.

    
    
    /// <summary>
    /// Your IStoreListener implementation of OnInitialized.
    /// </summary>
    public void OnInitialized(IStoreController controller, IExtensionProvider extensions)
    {
        extensions.GetExtension<IAppleExtensions> ().RestoreTransactions (result => {
            if (result) {
                // This does not mean anything was restored,
                // merely that the restoration process succeeded.
            } else {
                // Restoration failed.
            }
        });
    }
    

[](UnityIAPHandlingPurchaseFailures.html)

Handling purchase failures

[](UnityIAPPurchaseReceipts.html)

Purchase Receipts

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

