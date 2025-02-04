[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPProcessingPurchases.html)
  * [中文](/cn/current/Manual/UnityIAPProcessingPurchases.html)
  * [日本語](/ja/current/Manual/UnityIAPProcessingPurchases.html)
  * [한국어](/kr/current/Manual/UnityIAPProcessingPurchases.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPProcessingPurchases.html)
  * [中文](/cn/current/Manual/UnityIAPProcessingPurchases.html)
  * [日本語](/ja/current/Manual/UnityIAPProcessingPurchases.html)
  * [한국어](/kr/current/Manual/UnityIAPProcessingPurchases.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * Cross Platform Guide
  * Processing Purchases

[](UnityIAPInitiatingPurchases.html)

Initiating Purchases

[](UnityIAPHandlingPurchaseFailures.html)

Handling purchase failures

# Processing Purchases

The `ProcessPurchase` function of your store listener is called when a
purchase completes. Your application should fulfil whatever the user has
bought; for example, unlocking local content or sending purchase receipts to a
server to update a server-side game model.

A result is returned to indicate whether or not your Application has finished
processing the purchase:

Result | Description  
---|---  
**PurchaseProcessingResult.Complete** | The application has finished processing the purchase and should not be informed of it again.  
**PurchaseProcessingResult.Pending** | The application is still processing the purchase and ProcessPurchase will be called again the next time the Application starts, unless the `ConfirmPendingPurchase` function of `IStoreController` is called.  
  
Note that ProcessPurchase may be called at any point following a successful
initialization. If your application crashes during execution of the
`ProcessPurchase` handler, then it is invoked again the next time **Unity
IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) initializes, so you may wish to
implement your own additional de-duplication.

## Reliability

Unity IAP requires explicit acknowledgement of purchases to ensure that
purchases are reliably fulfilled in the event of network outages or
application crashes. Any purchases that complete while the application is
offline will be sent to the application on next initialization.

### Completing purchases immediately

When `PurchaseProcessingResult.Complete` is returned, Unity IAP finishes the
transaction immediately (as shown in the diagram below).

You **must not** return `PurchaseProcessingResult.Complete` if you are selling
consumable products and fulfilling them from a server (for example, providing
currency in an online game).

If you do, there is a risk that consumable purchases will be lost if your
Application is uninstalled before the cloud save takes place.

![Completing
immediately](../uploads/Main/PurchaseProcessingResult.Complete.png) Completing
immediately

### Saving purchases to the cloud

If you are saving consumable purchases to the cloud, you **must** return
`PurchaseProcessingResult.Pending` and call `ConfirmPendingPurchase` only when
you have successfully persisted the purchase.

When returning `Pending`, Unity IAP keeps transactions open on the underlying
store until confirmed as processed, ensuring consumable purchases are not lost
even if a user reinstalls your application while a consumable is in this
state.

![Pending Purchases](../uploads/Main/PurchaseProcessingResult.Pending.png)
Pending Purchases

[](UnityIAPInitiatingPurchases.html)

Initiating Purchases

[](UnityIAPHandlingPurchaseFailures.html)

Handling purchase failures

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

