[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPIStoreHandlingPurchases.html)
  * [中文](/cn/current/Manual/UnityIAPIStoreHandlingPurchases.html)
  * [日本語](/ja/current/Manual/UnityIAPIStoreHandlingPurchases.html)
  * [한국어](/kr/current/Manual/UnityIAPIStoreHandlingPurchases.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPIStoreHandlingPurchases.html)
  * [中文](/cn/current/Manual/UnityIAPIStoreHandlingPurchases.html)
  * [日本語](/ja/current/Manual/UnityIAPIStoreHandlingPurchases.html)
  * [한국어](/kr/current/Manual/UnityIAPIStoreHandlingPurchases.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Implementing a Store](UnityIAPImplementingAStore.html)
  * Handling purchases

[](UnityIAPIStoreRetrievingProducts.html)

Retrieving products

[](UnityIAPModules.html)

Store Modules

# Handling purchases

Your Store’s Purchase method is called when the user opts to make a purchase.
Your store should take the user through the checkout process and call either
the `OnPurchaseSucceeded` or `OnPurchaseFailed` method of the
`IStoreCallback`.

Your store should supply a receipt and unique transaction ID; if the
application has not already processed a purchase with the supplied
tranasaction ID, **Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) will invoke the application’s
`ProcessPurchase` method.

## Finishing Transactions

When the application acknowledges that a transaction has been processed, or if
the transaction has already been processed, Unity IAP invokes your store’s
FinishTransaction method.

Stores should use FinishTransaction to perform any housekeeping following a
purchase, such as closing transactions or consuming consumable products.

[](UnityIAPIStoreRetrievingProducts.html)

Retrieving products

[](UnityIAPModules.html)

Store Modules

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

