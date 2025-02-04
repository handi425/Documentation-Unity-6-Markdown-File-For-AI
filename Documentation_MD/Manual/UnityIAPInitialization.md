[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPInitialization.html)
  * [中文](/cn/current/Manual/UnityIAPInitialization.html)
  * [日本語](/ja/current/Manual/UnityIAPInitialization.html)
  * [한국어](/kr/current/Manual/UnityIAPInitialization.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPInitialization.html)
  * [中文](/cn/current/Manual/UnityIAPInitialization.html)
  * [日本語](/ja/current/Manual/UnityIAPInitialization.html)
  * [한국어](/kr/current/Manual/UnityIAPInitialization.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Initialization

[](UnityIAPSubscriptionProducts.html)

Subscription Product support

[](UnityIAPBrowsingMetadata.html)

Browsing Product Metadata

# Initialization

You must provide an implementation of the `IStoreListener` interface which
**Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) uses to inform your application of
purchase-related events.

Call the `UnityPurchasing.Initialize` method to start the initialization
process, supplying your listener implementation and configuration.

Note that initialization will not fail if the network is unavailable; Unity
IAP will continue attempting to initialize in the background. Initialization
will only fail if Unity IAP encounters an unrecoverable problem such as a
misconfiguration or IAP being disabled in device settings.

Consequently Unity IAP may take an arbitrary period of time to initialize;
indefinitely if the user is in airplane mode. You should design your store
accordingly by preventing users from attempting to make purchases if
initialization has not completed successfully.

    
    
    using UnityEngine;
    using UnityEngine.Purchasing;
    
    public class MyIAPManager : IStoreListener {
    
        private IStoreController controller;
        private IExtensionProvider extensions;
    
        public MyIAPManager () {
            var builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
            builder.AddProduct("100_gold_coins", ProductType.Consumable, new IDs
            {
                {"100_gold_coins_google", GooglePlay.Name},
                {"100_gold_coins_mac", MacAppStore.Name}
            });
    
            UnityPurchasing.Initialize (this, builder);
        }
    
        /// <summary>
        /// Called when Unity IAP is ready to make purchases.
        /// </summary>
        public void OnInitialized (IStoreController controller, IExtensionProvider extensions)
        {
            this.controller = controller;
            this.extensions = extensions;
        }
    
        /// <summary>
        /// Called when Unity IAP encounters an unrecoverable initialization error.
        ///
        /// Note that this will not be called if Internet is unavailable; Unity IAP
        /// will attempt initialization until it becomes available.
        /// </summary>
        public void OnInitializeFailed (InitializationFailureReason error)
        {
        }
    
        /// <summary>
        /// Called when a purchase completes.
        ///
        /// May be called at any time after OnInitialized().
        /// </summary>
        public PurchaseProcessingResult ProcessPurchase (PurchaseEventArgs e)
        {
            return PurchaseProcessingResult.Complete;
        }
    
        /// <summary>
        /// Called when a purchase fails.
        /// </summary>
        public void OnPurchaseFailed (Product i, PurchaseFailureReason p)
        {
        }
    }
    

[](UnityIAPSubscriptionProducts.html)

Subscription Product support

[](UnityIAPBrowsingMetadata.html)

Browsing Product Metadata

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

