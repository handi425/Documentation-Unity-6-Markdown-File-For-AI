[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPModuleRegistration.html)
  * [中文](/cn/current/Manual/UnityIAPModuleRegistration.html)
  * [日本語](/ja/current/Manual/UnityIAPModuleRegistration.html)
  * [한국어](/kr/current/Manual/UnityIAPModuleRegistration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPModuleRegistration.html)
  * [中文](/cn/current/Manual/UnityIAPModuleRegistration.html)
  * [日本語](/ja/current/Manual/UnityIAPModuleRegistration.html)
  * [한국어](/kr/current/Manual/UnityIAPModuleRegistration.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Implementing a Store](UnityIAPImplementingAStore.html)
  * [Store Modules](UnityIAPModules.html)
  * Registering your store

[](UnityIAPModules.html)

Store Modules

[](UnityIAPModuleConfiguration.html)

Store Configuration

# Registering your store

Call the `RegisterStore` method supplying a name for your store and your
implementation, which must implement the IStore interface.

    
    
    public override void Configure() {
        RegisterStore(“GooglePlay”, InstantiateMyStore());
    }
    
    private void InstantiateMyStore() {
        if (Application.platform == RuntimePlatform.Android) {
            return new MyAlternativeGooglePlayImplementation ();
        }
        return null;
    }
    

The store name must match the name developers use when defining products for
your store so **Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) uses the correct product identifiers
when addressing your store.

[](UnityIAPModules.html)

Store Modules

[](UnityIAPModuleConfiguration.html)

Store Configuration

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

