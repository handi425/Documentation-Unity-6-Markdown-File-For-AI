[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPStoreExtensions.html)
  * [中文](/cn/current/Manual/UnityIAPStoreExtensions.html)
  * [日本語](/ja/current/Manual/UnityIAPStoreExtensions.html)
  * [한국어](/kr/current/Manual/UnityIAPStoreExtensions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPStoreExtensions.html)
  * [中文](/cn/current/Manual/UnityIAPStoreExtensions.html)
  * [日本語](/ja/current/Manual/UnityIAPStoreExtensions.html)
  * [한국어](/kr/current/Manual/UnityIAPStoreExtensions.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Store Extensions

[](UnityIAPValidatingReceipts.html)

Receipt validation

[](UnityIAPCrossStoreInstallationIssues.html)

Cross-store installation issues with Android in-app purchase stores

# Store Extensions

Stores may offer unique functionality that does not fit into the normal cross-
platform purchase flow. This extended functionality is accessed via the
`IExtensionProvider` which is provided to your application when **Unity IAP**
Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) initializes successfully.

It is not necessary to use platform-dependent compilation when using
extensions; each extension comes with a fake no-op implementation which is
used when running on a platform that does not offer the extended
functionality.

For example, the following snippet accesses the `RefreshReceipt` mechanism
Apple offers to fetch a refreshed App Receipt from Apple’s servers. It can be
compiled on any Unity IAP platform, and if you were to run it on a non Apple
platform such as Android it would have no effect; the supplied lambda would
never be invoked.

    
    
    /// <summary>
    /// Called when Unity IAP is ready to make purchases.
    /// </summary>
    public void OnInitialized (IStoreController controller, IExtensionProvider extensions)
    {
        extensions.GetExtension<IAppleExtensions> ().RefreshAppReceipt (result => {
            if (result) {
                // Refresh finished successfully.
            } else {
                // Refresh failed.
            }
        });
    }
    

[](UnityIAPValidatingReceipts.html)

Receipt validation

[](UnityIAPCrossStoreInstallationIssues.html)

Cross-store installation issues with Android in-app purchase stores

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

