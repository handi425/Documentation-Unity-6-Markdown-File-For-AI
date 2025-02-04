[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPIStoreInitialization.html)
  * [中文](/cn/current/Manual/UnityIAPIStoreInitialization.html)
  * [日本語](/ja/current/Manual/UnityIAPIStoreInitialization.html)
  * [한국어](/kr/current/Manual/UnityIAPIStoreInitialization.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPIStoreInitialization.html)
  * [中文](/cn/current/Manual/UnityIAPIStoreInitialization.html)
  * [日本語](/ja/current/Manual/UnityIAPIStoreInitialization.html)
  * [한국어](/kr/current/Manual/UnityIAPIStoreInitialization.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Implementing a Store](UnityIAPImplementingAStore.html)
  * Initialization

[](UnityIAPImplementingAStore.html)

Implementing a Store

[](UnityIAPIStoreRetrievingProducts.html)

Retrieving products

# Initialization

Your store’s `Initialize` method is called by **Unity IAP** Abbreviation of
Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) with an `IStoreCallback` that your
store uses to communicate back to Unity IAP asynchronously.

    
    
    void Initialize(IStoreCallback callback) {
        // Keep a reference to the callback for communicating with Unity IAP.
        this.callback = callback;
    }
    

[](UnityIAPImplementingAStore.html)

Implementing a Store

[](UnityIAPIStoreRetrievingProducts.html)

Retrieving products

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

