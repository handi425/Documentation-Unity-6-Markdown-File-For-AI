[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityIAPAmazonExtendedFunctionality.html)
  * [中文](/cn/current/Manual/UnityIAPAmazonExtendedFunctionality.html)
  * [日本語](/ja/current/Manual/UnityIAPAmazonExtendedFunctionality.html)
  * [한국어](/kr/current/Manual/UnityIAPAmazonExtendedFunctionality.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityIAPAmazonExtendedFunctionality.html)
  * [中文](/cn/current/Manual/UnityIAPAmazonExtendedFunctionality.html)
  * [日本語](/ja/current/Manual/UnityIAPAmazonExtendedFunctionality.html)
  * [한국어](/kr/current/Manual/UnityIAPAmazonExtendedFunctionality.html)

  * [Unity Services](UnityServices.html)
  * [Unity IAP](UnityIAP.html)
  * [Store Guides](UnityIAPStoreGuides.html)
  * Amazon Appstore and Amazon Underground Store 

[](UnityIAPGooglePlay.html)

Google Play

[](UnityIAPImplementingAStore.html)

Implementing a Store

# Amazon Appstore and Amazon Underground Store

## Extended functionality

### Amazon User ID

To fetch the current Amazon User ID for other Amazon services, use the
`IAmazonExtensions`:

    
    
    public void OnInitialized
        (IStoreController controller, IExtensionProvider extensions)
    {
        string amazonUserId = 
            extensions.GetExtension<IAmazonExtensions>().amazonUserId;
        // ...
    }
    

### Sandbox testing in Amazon

To use Amazon’s local Sandbox testing app, generate a JSON description of your
product catalog on the device’s SD card using the `IAmazonConfiguration`
extended configuration:

    
    
    var builder = ConfigurationBuilder.Instance(
    StandardPurchasingModule.Instance());
    // Define your products.
    builder.AddProduct("someConsumable", ProductType.Consumable);
    // Write a product description to the SD card 
    // in the appropriate location.
    builder.Configure<IAmazonConfiguration>()
        .WriteSandboxJSON(builder.products);
    

When using this method to write product descriptions to the SD card, declare
the Android permission to write to external storage in the test app’s
manifest:

    
    
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" /> 
    

Remove this extra permission before publishing, if appropriate.

Amazon Sandbox is now set up for local testing. For more information, please
see Amazon’s [App Tester
documentation](https://developer.amazon.com/public/apis/earn/in-app-
purchasing/docs-v2/installing-and-configuring-app-tester).

[](UnityIAPGooglePlay.html)

Google Play

[](UnityIAPImplementingAStore.html)

Implementing a Store

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

