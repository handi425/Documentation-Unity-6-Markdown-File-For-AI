[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPModuleConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPModuleConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPModuleConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPModuleConfiguration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPModuleConfiguration.html)
  * [中文](/cn/current/Manual/UnityIAPModuleConfiguration.html)
  * [日本語](/ja/current/Manual/UnityIAPModuleConfiguration.html)
  * [한국어](/kr/current/Manual/UnityIAPModuleConfiguration.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Implementing a Store](UnityIAPImplementingAStore.html)
  * [Store Modules](UnityIAPModules.html)
  * Store Configuration

[](UnityIAPModuleRegistration.html)

Registering your store

[](UnityIAPModuleExtension.html)

Store Extensions

# Store Configuration

Your store may require developers to supply additional configuration
information during initialization, for which your module can register a
configuration instance that implements the `IStoreConfiguration` interface:

    
    
    var config = new MyConfiguration(); // Implements IStoreConfiguration
    BindConfiguration<MyConfiguration>(new MyConfiguration());
    

When developers request an instance of your configuration type, **Unity IAP**
Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) first tries to cast your store
implementation to the configuration type. Only if that cast fails will any
instance bound via `BindConfiguration` will be used.

[](UnityIAPModuleRegistration.html)

Registering your store

[](UnityIAPModuleExtension.html)

Store Extensions

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

