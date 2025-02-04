[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPCrossStoreInstallationIssues.html)
  * [中文](/cn/current/Manual/UnityIAPCrossStoreInstallationIssues.html)
  * [日本語](/ja/current/Manual/UnityIAPCrossStoreInstallationIssues.html)
  * [한국어](/kr/current/Manual/UnityIAPCrossStoreInstallationIssues.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPCrossStoreInstallationIssues.html)
  * [中文](/cn/current/Manual/UnityIAPCrossStoreInstallationIssues.html)
  * [日本語](/ja/current/Manual/UnityIAPCrossStoreInstallationIssues.html)
  * [한국어](/kr/current/Manual/UnityIAPCrossStoreInstallationIssues.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Cross-store installation issues with Android in-app purchase stores

[](UnityIAPStoreExtensions.html)

Store Extensions

[](UnityIAPStoreGuides.html)

Store Guides

# Cross-store installation issues with Android in-app purchase stores

There are cross-store installation issues when using shared Android bundle
identifiers to publish to multiple Android in-app purchase stores (such as
Google) simultaneously. This page describes the results of these conflicts,
and how to resolve the issue.

The cross-store install scenario is one where a user installs an application
from one store (store A), and then upgrades the installation with an
application from another store (store B). The opportunity to upgrade a user’s
installation belongs to the store hosting the newest application version. This
scenario can arise when both builds of the application use the same Android
bundle identifier and signing key.

For example, `com.foo.bar` is published to Google Play and Amazon Appstore. A
user who has both App stores installed could install `com.foo.bar` from Amazon
Apps and receive an updated version from Google Play. This could result in
them losing IAP digital product transactions, and being unable to restore
previously made transactions.

## Impact of cross-store installation issues

Cross-store conflict can cause intractable end-user problems with applications
using IAP. Users may find they lose purchases upon
uninstallation/reinstallation and lose any in-flight purchases interrupted by
a cross-store upgrade.

The resulting IAP problems are:

  * **Losing incomplete purchases.** This occurs if the user upgrades after a purchase has been approved but before the application has acknowledged receiving the purchase from the store’s billing system. This can arise when an application fails to synchronize with a cloud inventory service in a timely fashion, or the app crashes before saving this new IAP to the local inventory database.

  * **Withholding purchases from store A.** This occurs if a user reinstalls an application from store B after completing IAP transactions on store A. They will not be able to restore those transactions. Many stores explicitly disallow applications from accessing other stores’ IAP systems. To workaround this utilize a cloud inventory system along with its dependent user identity service.

  * **Divergent IAP product lists.** This occurs if the upgraded product list in store B’s application diverges from the list in store A’s version. You may provide divergent IAP cataloges. This may result in an application error when an inconsistent local inventory is read by the store B version, or the user may lose the inventory they previously purchased which is unavailable through the store B version.

## Resolving cross-store installation issues

There are two ways to resolve cross-store conflicts:

  * use unique signing keys for each store (This results in upgrade error messages from the conflicting store), or
  * use unique bundle identifiers for each store (This may result in duplicate installed apps for the user).

[](UnityIAPStoreExtensions.html)

Store Extensions

[](UnityIAPStoreGuides.html)

Store Guides

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

