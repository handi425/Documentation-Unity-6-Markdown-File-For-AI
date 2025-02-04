[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPInitiatingPurchases.html)
  * [中文](/cn/current/Manual/UnityIAPInitiatingPurchases.html)
  * [日本語](/ja/current/Manual/UnityIAPInitiatingPurchases.html)
  * [한국어](/kr/current/Manual/UnityIAPInitiatingPurchases.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPInitiatingPurchases.html)
  * [中文](/cn/current/Manual/UnityIAPInitiatingPurchases.html)
  * [日本語](/ja/current/Manual/UnityIAPInitiatingPurchases.html)
  * [한국어](/kr/current/Manual/UnityIAPInitiatingPurchases.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Initiating Purchases

[](UnityIAPBrowsingMetadata.html)

Browsing Product Metadata

[](UnityIAPProcessingPurchases.html)

Processing Purchases

# Initiating Purchases

When the user wants to buy a product call the `InitiatePurchase` method of the
`IStoreController`, identifying the product the user wants to buy.

    
    
    // Example method called when the user presses a 'buy' button
    // to start the purchase process.
    public void OnPurchaseClicked(string productId) {
        controller.InitiatePurchase(productId);
    }
    

Your application will be notified asynchronously of the result, either with an
invocation of `ProcessPurchase` for successful purchases or `OnPurchaseFailed`
for failures.

[](UnityIAPBrowsingMetadata.html)

Browsing Product Metadata

[](UnityIAPProcessingPurchases.html)

Processing Purchases

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

