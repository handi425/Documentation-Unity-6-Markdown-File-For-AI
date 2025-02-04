[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPIStoreRetrievingProducts.html)
  * [中文](/cn/current/Manual/UnityIAPIStoreRetrievingProducts.html)
  * [日本語](/ja/current/Manual/UnityIAPIStoreRetrievingProducts.html)
  * [한국어](/kr/current/Manual/UnityIAPIStoreRetrievingProducts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPIStoreRetrievingProducts.html)
  * [中文](/cn/current/Manual/UnityIAPIStoreRetrievingProducts.html)
  * [日本語](/ja/current/Manual/UnityIAPIStoreRetrievingProducts.html)
  * [한국어](/kr/current/Manual/UnityIAPIStoreRetrievingProducts.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Implementing a Store](UnityIAPImplementingAStore.html)
  * Retrieving products

[](UnityIAPIStoreInitialization.html)

Initialization

[](UnityIAPIStoreHandlingPurchases.html)

Handling purchases

# Retrieving products

When your store’s `RetrieveProducts` method is called it should fetch the
latest product metadata and, optionally, ownership status for the current
user.

When this process completes your store should call the `OnProductsRetrieved`
method of the `IStoreCallback` supplied to your store upon initialisation,
supplying a collection of `ProductDescription` that represent the items
available for purchase.

Where products are owned by the user, your store may fill in the receipt and
transaction ID fields of `ProductDescription`; **Unity IAP** Abbreviation of
Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) will invoke the application’s
`ProcessPurchase` method for any transactions the application has not already
processed.

Note that if the user is offline your store should retry until the user
regains connectivity, taking care to avoid impacting game performance through
aggressive polling.

## Handling errors

If products cannot be retrieved due to an unrecoverable error, such as the
developer making an error with their store configuration, you should call the
`OnSetupFailed` method of the `IStoreCallback`, indicating the
`InitializationFailureReason` responsible.

[](UnityIAPIStoreInitialization.html)

Initialization

[](UnityIAPIStoreHandlingPurchases.html)

Handling purchases

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

