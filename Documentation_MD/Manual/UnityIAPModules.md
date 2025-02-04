[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPModules.html)
  * [中文](/cn/current/Manual/UnityIAPModules.html)
  * [日本語](/ja/current/Manual/UnityIAPModules.html)
  * [한국어](/kr/current/Manual/UnityIAPModules.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPModules.html)
  * [中文](/cn/current/Manual/UnityIAPModules.html)
  * [日本語](/ja/current/Manual/UnityIAPModules.html)
  * [한국어](/kr/current/Manual/UnityIAPModules.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Implementing a Store](UnityIAPImplementingAStore.html)
  * Store Modules

[](UnityIAPIStoreHandlingPurchases.html)

Handling purchases

[](UnityIAPModuleRegistration.html)

Registering your store

# Store Modules

Store modules extend the `AbstractPurchasingModule` class, acting as factories
**Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) can use to obtain an instance of
your store along with any configuration and extensions.

Developers can supply multiple modules to Unity IAP, allowing them to use your
custom store implementation alongside the default Unity-provided stores:

    
    
    ConfigurationBuilder.Instance (MyCustomModule.Instance(), StandardPurchasingModule.Instance ());
    

Where two or more modules have implementations available for a given platform,
precedence is given in order the modules were supplied to the
`ConfigurationBuilder`; any implementation provided by `MyCustomModule` will
be used in preference to `StandardPurchasingModule`.

Note that a module can support multiple stores; the `StandardPurchasingModule`
handles all of Unity IAPs default store implementations.

[](UnityIAPIStoreHandlingPurchases.html)

Handling purchases

[](UnityIAPModuleRegistration.html)

Registering your store

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

