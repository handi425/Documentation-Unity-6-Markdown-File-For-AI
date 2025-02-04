[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPImplementingAStore.html)
  * [中文](/cn/current/Manual/UnityIAPImplementingAStore.html)
  * [日本語](/ja/current/Manual/UnityIAPImplementingAStore.html)
  * [한국어](/kr/current/Manual/UnityIAPImplementingAStore.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPImplementingAStore.html)
  * [中文](/cn/current/Manual/UnityIAPImplementingAStore.html)
  * [日本語](/ja/current/Manual/UnityIAPImplementingAStore.html)
  * [한국어](/kr/current/Manual/UnityIAPImplementingAStore.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Implementing a Store

[](UnityIAPAmazonExtendedFunctionality.html)

Amazon Appstore and Amazon Underground Store

[](UnityIAPIStoreInitialization.html)

Initialization

# Implementing a Store

Your store must implement the IStore interface, the methods of which are
detailed in following sections.

    
    
    using UnityEngine.Purchasing.Extension;
    
    public class MyStore : IStore
    {
        private IStoreCallback callback;
        public void Initialize (IStoreCallback callback)
        {
            this.callback = callback;   
        }
    
        public void RetrieveProducts (System.Collections.ObjectModel.ReadOnlyCollection<UnityEngine.Purchasing.ProductDefinition> products)
        {
            // Fetch product information and invoke callback.OnProductsRetrieved();
        }
    
        public void Purchase (UnityEngine.Purchasing.ProductDefinition product, string developerPayload)
        {
            // Start the purchase flow and call either callback.OnPurchaseSucceeded() or callback.OnPurchaseFailed()
        }
    
        public void FinishTransaction (UnityEngine.Purchasing.ProductDefinition product, string transactionId)
        {
            // Perform transaction related housekeeping 
        }
    }
    

[](UnityIAPAmazonExtendedFunctionality.html)

Amazon Appstore and Amazon Underground Store

[](UnityIAPIStoreInitialization.html)

Initialization

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

