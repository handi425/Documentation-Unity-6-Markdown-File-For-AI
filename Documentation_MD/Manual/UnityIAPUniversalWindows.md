[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPUniversalWindows.html)
  * [中文](/cn/current/Manual/UnityIAPUniversalWindows.html)
  * [日本語](/ja/current/Manual/UnityIAPUniversalWindows.html)
  * [한국어](/kr/current/Manual/UnityIAPUniversalWindows.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPUniversalWindows.html)
  * [中文](/cn/current/Manual/UnityIAPUniversalWindows.html)
  * [日本語](/ja/current/Manual/UnityIAPUniversalWindows.html)
  * [한국어](/kr/current/Manual/UnityIAPUniversalWindows.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Store Guides](UnityIAPStoreGuides.html)
  * Universal Windows Platform

[](UnityIAPiOSMAS.html)

iOS & Mac App Stores

[](UnityIAPGooglePlay.html)

Google Play

# Universal Windows Platform

## Simulator

Unity IAP features support for Microsoft’s **In App Purchase** Revenue from
“micro-transactions” within a game. [More info](UnityIAP.html)  
See in [Glossary](Glossary.html#InAppPurchase) simulator, which allows you to
test IAP purchase flows on devices before publishing your application.

The simulator can be enabled when configuring **Unity IAP** Abbreviation of
Unity **In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) before initialization, as follows:

    
    
    var builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
    builder.Configure<IMicrosoftConfiguration>().useMockBillingSystem = true;
    

Make sure you disable the mock billing system before publishing your
application.

* * *

• 2017–05–16 Page amended  

[](UnityIAPiOSMAS.html)

iOS & Mac App Stores

[](UnityIAPGooglePlay.html)

Google Play

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

