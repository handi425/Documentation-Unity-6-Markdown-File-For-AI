[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPBrowsingMetadata.html)
  * [中文](/cn/current/Manual/UnityIAPBrowsingMetadata.html)
  * [日本語](/ja/current/Manual/UnityIAPBrowsingMetadata.html)
  * [한국어](/kr/current/Manual/UnityIAPBrowsingMetadata.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPBrowsingMetadata.html)
  * [中文](/cn/current/Manual/UnityIAPBrowsingMetadata.html)
  * [日本語](/ja/current/Manual/UnityIAPBrowsingMetadata.html)
  * [한국어](/kr/current/Manual/UnityIAPBrowsingMetadata.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Browsing Product Metadata

[](UnityIAPInitialization.html)

Initialization

[](UnityIAPInitiatingPurchases.html)

Initiating Purchases

# Browsing Product Metadata

Unity IAP retrieves localized product metadata during the initialization
process, which you can access via the `IStoreController`’s products field.

    
    
    foreach (var product in controller.products.all) {
        Debug.Log (product.metadata.localizedTitle);
        Debug.Log (product.metadata.localizedDescription);
        Debug.Log (product.metadata.localizedPriceString);
    }
    

[](UnityIAPInitialization.html)

Initialization

[](UnityIAPInitiatingPurchases.html)

Initiating Purchases

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

