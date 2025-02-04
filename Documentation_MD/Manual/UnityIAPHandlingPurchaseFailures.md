[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPHandlingPurchaseFailures.html)
  * [中文](/cn/current/Manual/UnityIAPHandlingPurchaseFailures.html)
  * [日本語](/ja/current/Manual/UnityIAPHandlingPurchaseFailures.html)
  * [한국어](/kr/current/Manual/UnityIAPHandlingPurchaseFailures.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPHandlingPurchaseFailures.html)
  * [中文](/cn/current/Manual/UnityIAPHandlingPurchaseFailures.html)
  * [日本語](/ja/current/Manual/UnityIAPHandlingPurchaseFailures.html)
  * [한국어](/kr/current/Manual/UnityIAPHandlingPurchaseFailures.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Handling purchase failures

[](UnityIAPProcessingPurchases.html)

Processing Purchases

[](UnityIAPRestoringTransactions.html)

Restoring Transactions

# Handling purchase failures

Purchases may fail for a number of reasons, including network failure, payment
failure or device settings. You may wish to check the reason for a purchase
failure and prompt the user to take action, though note that not all stores
provide fine-grained failure information.

    
    
    /// <summary>
    /// Called when a purchase fails.
    /// </summary>
    public void OnPurchaseFailed (Product i, PurchaseFailureReason p)
    {
        if (p == PurchaseFailureReason.PurchasingUnavailable) {
            // IAP may be disabled in device settings.
        }
    }
    

[](UnityIAPProcessingPurchases.html)

Processing Purchases

[](UnityIAPRestoringTransactions.html)

Restoring Transactions

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

