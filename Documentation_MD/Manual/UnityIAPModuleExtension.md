[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPModuleExtension.html)
  * [中文](/cn/current/Manual/UnityIAPModuleExtension.html)
  * [日本語](/ja/current/Manual/UnityIAPModuleExtension.html)
  * [한국어](/kr/current/Manual/UnityIAPModuleExtension.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPModuleExtension.html)
  * [中文](/cn/current/Manual/UnityIAPModuleExtension.html)
  * [日本語](/ja/current/Manual/UnityIAPModuleExtension.html)
  * [한국어](/kr/current/Manual/UnityIAPModuleExtension.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Implementing a Store](UnityIAPImplementingAStore.html)
  * [Store Modules](UnityIAPModules.html)
  * Store Extensions

[](UnityIAPModuleConfiguration.html)

Store Configuration

[](udp.html)

Unity Distribution Portal

# Store Extensions

Your store may offer additional functionality that does not fit into the cross
platform purchase flow, for example the ability to refresh app receipts on
Apple’s stores.

You should create an interface that defines the extended functionality, itself
implementing the `IStoreExtension` interface:

    
    
    /// <summary>
    /// Functionality specific to my store.
    /// </summary>
    public interface IMyExtensions : IStoreExtension
    {
        // Hypothetical method for a store that provides User IDs.
        String GetUserStoreId();
    }
    

Applications request extended functionality via the `IExtensionProvider`. When
they do so **Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) first tries to cast the active store
implementation to the requested type.

If that cast fails, Unity IAP will provide any instance registered via a call
your store module has provided via `RegisterExtension`, or null if no instance
has been provided.

Modules should provide instances for the extension interfaces they define even
when running on unsupported platforms, so as to avoid forcing application
developers to use platform dependent compilation.

[](UnityIAPModuleConfiguration.html)

Store Configuration

[](udp.html)

Unity Distribution Portal

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

