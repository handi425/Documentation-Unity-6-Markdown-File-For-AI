[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-service-interoperability.html)
  * [中文](/cn/current/Manual/udp-service-interoperability.html)
  * [日本語](/ja/current/Manual/udp-service-interoperability.html)
  * [한국어](/kr/current/Manual/udp-service-interoperability.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-service-interoperability.html)
  * [中文](/cn/current/Manual/udp-service-interoperability.html)
  * [日本語](/ja/current/Manual/udp-service-interoperability.html)
  * [한국어](/kr/current/Manual/udp-service-interoperability.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * Using UDP with other services

[](udp-managing-and-publishing.html)

Managing and publishing your game on the UDP console

[](udp-firebase.html)

Using Firebase with UDP builds

# Using UDP with other services

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
## Google Play games services in UDP builds

### Overview

Implementing [Google Play games
services](https://developers.google.com/games/services/console/enabling) in
your Android games lets you leverage Google’s service layer for features such
as achievements and leaderboards. If your game implements Google Play game
services, additional configuration is required to support the builds that
[UDP](https://unity.com/products/unity-distribution-portal) creates for
different stores.

When your game invokes Google Play games services, Google Play games services
checks that the following details match the information registered on the
Google Play Console:

  * The application’s **package name**
  * The **certificate** the application was signed with

If they don’t match, the player can’t log into the application with Google
Play games services.

For certain stores that you publish your game to via UDP, UDP adds a store-
specific suffix to the package name. Additionally, if you don’t use your own
private key to generate the certificate, UDP generates a certificate for each
repacked build. These events would cause your certificate and/or package name
to no longer match the information on the Google Play Console. This would
prevent users from logging into the game with Google Play game services.

The following section explains how to resolve this issue.

### Configuring Google Play games services for UDP builds

This section explains how to link your UDP versions to a Google Play
application so that Google Play game services can work on all of them.

  1. In the Google Play Console, go to the target app.
  2. Go to **Play Games Services** > **Setup and management** > **Configuration**. 
     * If your Google Play game has Google Play games services implemented, your game will already be linked to a Google Play games services project. In this case: 
       1. Select **Use an existing Play Games Services project**.
       2. Select your game project and select **Use**.
       3. Follow the steps in Link the UDP apps to your game service.
     * If your Google Play game doesn’t have Google Play games services implemented: 
       1. In the Play Games Services setup page, select **Yes, my game already uses Google APIs** or **No, my game doesn’t use Google APIs**.
       2. Follow the steps in Creating and linking a Google Play games services project.

#### Creating and linking a Google Play games services project

This section explains how to create a Google Play games services project and
link it to a new or existing cloud project.

If you selected **Yes, my game already uses Google APIs** in the Play Games
Services setup page:

  1. Select a cloud project.
  2. Select Use to create a new Play Games Services project and link it to your existing cloud project.

If you selected **No, my game doesn’t use Google APIs** in the Play Games
Services setup page:

  1. Enter a game name.
  2. Select Create to create a new Play Games Services project and link it to a new cloud project.

When you create a new Play Games Services project, the **Add credential** link
is disabled.

  1. Select **Configure OAuth consent screen**.
  2. In the Play Games Services configuration screen, select Refresh.  
The Add credential option is now enabled.

  3. Select **Add credential**.  
This opens the Add credential page.

  4. In the Add credential page: 
    1. Select **Android** as the **Type**.
    2. Set **Enable anti-piracy** to **Off**. This lets users access your game if they have installed it from a different app store than Google Play.
    3. In the Authorization section, select **Create OAuth client**. This opens a popup.
    4. Select **Create OAuth Client ID** and use the details from the popup to complete the form.

When you’ve completed the above steps, your Google Play game is linked to its
Google Play games services. The next step is to link your UDP builds to the
games services.

#### Linking UDP apps to your games services

When you have linked your app to Google Play games services you can link the
other (UDP) apps to the games services.

  1. In the Google Play Console, select **Play Games Services** > **Setup and management** > **Configuration**. 
    1. In the Play Games Services configuration page, select **Add credential**.
  2. In the Add credential page: 
    1. Select **Android**.
    2. Set **Enable anti-piracy to off**. This lets users access your game if they have installed it from a different app store than Google Play.
    3. In the **Authorization** section, select **Create OAuth client**. This opens a popup.
    4. Select **Create OAuth Client ID** and use the details from the popup to complete the form.
  3. In the Create OAuth client ID form, enter the required details to create an entry for one of your UDP builds. 
    1. In the **Name** field, name the build after the corresponding store, for example “Samsung version”.
    2. In the **Package name** field, specify the package name for the build registered with the corresponding store via the UDP console.  
The store-specific package name is displayed in the UDP console:

      1. Go to My Games > Publish tab.
      2. Select **Advanced** for the corresponding store.  
The package name is displayed in the Basic Information section.

    3. In the certificate field, use the certificate used for the corresponding UDP store. UDP signs the app with the new certificate after the Repack operation.  
The store-specific certificate is displayed in the UDP console:

      1. Go to My Games > Publish tab.
      2. Select **Advanced** for the corresponding store.  
The certificate is displayed in the Basic Information section.  
**Note** : You can also download the APK Certificate and get the fingerprint
information via the command:  
`openssl x509 -in [downloaded-pem-filepath] -fingerprint -noout`

      3. Copy the SHA–1 from the UDP console into the certificate field.
  4. When you’ve completed the form, select **Create** and return to Google Play Console.
  5. Select **Refresh OAuth clients**.
  6. Select your new OAuth client. 
    1. Select **Save changes** to save the credential.
  7. Repeat the above steps for each store-specific UDP build that you want to link to your Google Play application.

You can view the UDP builds you’ve linked to your Google Play application in
the Google Cloud Platform > Google API & Services dashboard, under
Credentials.

These steps enable Google Play games services to work successfully on all the
UDP store versions that are linked that way, excluding Mi GetApps (whose SDK
integrates an old version of Google Mobile Services, which creates conflicts).

**Note** : Any changes to Google’s systems could impact the solution described
above. For more information on Google’s troubleshooting information, see the
[Google
documentation](https://www.google.com/url?q=https://developers.google.com/games/services/android/troubleshooting&sa=D&ust=1611571996561000&usg=AOvVaw00u3uXWmm9qmGpqo4yuFQX).

## Using Build Automation with UDP

You can use [Build Automation](https://docs.unity.com/ugs/en-
us/manual/devops/manual/unity-build-automation)A continuous integration
service for Unity projects that automates the process of creating builds on
Unity’s servers. [More info](https://docs.unity.com/devops/en/manual/unity-
build-automation)  
See in [Glossary](Glossary.html#BuildAutomation) to deploy your game to the
UDP console in the following ways:

  * Upload your APK to Build Automation, and deploy it to UDP from there
  * Build your game with Build Automation, and deploy it to UDP from there

## Pushing the build to the UDP console via Build Automation

This section explains how to use Build Automation to push your game to UDP. In
the Unity Editor, enable Build Automation in the **Project Settings** A broad
collection of settings which allow you to configure how Physics, Audio,
Networking, Graphics, Input and many other areas of your project behave. [More
info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) window.

### Using Build Automation in the Editor to deploy your game to UDP

To deploy your game to UDP via the Build Automation feature in the Unity
Editor, you need to upload your UDP build and push it to UDP.

  1. In the **Build Automation** tab of the Project Settings window, if you haven’t uploaded any build before, select **Upload Build**.  

  2. In **FILE** :  

     * Choose the **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) of your UDP build

     * Enter a useful **LABEL**
     * Set the **PLATFORM** field to Android.  

  3. Select **UPLOAD** , and let it complete the upload process.
  4. In the **Build Automation** tab of the Project Settings window, locate the desired build from the build **History** timeline and select **Push to Unity Distribution Portal**. 
    1. Verify that you want to push, and that the action completes.  

### Using the Unity Dashboard to deploy your game to UDP

To deploy your game to UDP via the Build Automation feature in the Unity
Dashboard, you need to upload your UDP build to the Unity Dashboard and push
it from there to UDP.

  1. In the [Unity Developer Dashboard](https://developer.cloud.unity3d.com/build), navigate to your Project’s **Build Automation** > **History**.
  2. Select **Upload** , then select your APK file.
  3. In the **Platform** field, select **Android**.
  4. Select **Upload**.
  5. Select the More menu next to your build to expand the drop-down menu.
  6. Select **Push to Unity Distribution Portal**.

## Building and deploying via Build Automation

If you use Unity Teams Advanced, you can [generate builds
automatically](https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-
build-automation#continuous-integration).

In the Build Automation tab of the Project Settings window:

  1. Select **Manage Build Targets** > **Add new build target**
  2. In the **TARGET SETUP** window, set the **PLATFORM** field to Android and enter a useful **TARGET LABEL**.
  3. Select **Next: Save**.
  4. Select **Start Build Automation** , then select the target build you just created.

Push your build to UDP directly via the Unity Build Automation Developer
Dashboard (as shown above).

## Service interoperability

UDP can tell other services used by your game which store was the game
downloaded from.

This information can be used in many ways, by Unity services as well as by
third-party or your own services.

For example, [Unity Remote Config](https://unity.com/remote-config) lets you
tune your game settings based on rules that you define, such as which store
the game was downloaded from.

This section explains how to let other services gain access to this
information, and includes an example.

### How does it work?

When your game first launches on a player’s device, UDP creates and drops the
`udp.json` file in the game’s Persistent Data Path. This file contains the
field `udpStore`, which shows which store the game was downloaded from.
Retrieve that information to use it the way you intend to.

**Note:** This doesn’t add any new permission into your game manifest.

### Locating udp.json

The file `udp.json` is saved in:

`Application.PersistentDataPath + '/Unity' + /Application.CloudProjectID +
/udp/udp.json`

Where:

  * `Application.PersistentDataPath` is your game’s persistent data path
  * `Application.CloudProjectID` is your game’s Unity project ID

Here is an example of a path to the `udp.json` file:

`path/storage/emulated/0/Android/data/com.mystudio.mygame/files/Unity/c83d2de2-de74-4b75-83fc-
ade948bda064/udp/udp.json`

Where:

  * `Application.PersistentDataPath`= `path/storage/emulated/0/Android/data/com.mystudio.mygame`
  * `Application.CloudProjectID`= `c83d2de2-de74-4b75-83fc-ade948bda064`

### Reading udp.json

The file `udp.json` contains the following information:

    
    
    {"key":"UDP","udpStore":"StoreName","udpClientId":"value_of_udpClientId","CloudProjectId":"value_of_CloudProjectId"}
    

The field `udpStore` contains the value of the UDP store your game was
downloaded from.

Here is an example of a `udp.json` file:

    
    
    {"key":"UDP","udpStore":"Huawei","udpClientId":"icjaB7wmu_q7AOjrSLH8yw","cloudProjectId":"bc2be074-09f3-450f-8e98-a0f79c9746f7"}
    

In this example, the game was downloaded from the HUAWEI AppGallery.

**Tip:** use `JSONUtility.FromJsonOverwrite` to read the contents of the file
as a text asset.

### udpStore values

The table below lists the `udpStore` values you can expect for stores
available on UDP.

These are case-sensitive.

Store (channel name on UDP) | Value for udpStore  
---|---  
UDP Sandbox (for the generic UDP builds) | UdpSandbox  
ONE store | OneStore  
APPTUTTi | Apptutti  
Mi GetApps (Xiaomi) | XiaomiStore  
HUAWEI AppGallery | Huawei  
QooApp Game Store | QooApp  
Uptodown | Uptodown  
SHAREit | ShareIt  
JioGames | JioGames  
Legion Store | Legion  
  
### Using udpStore with Remote Config

[Unity Remote Config](https://unity.com/remote-config) lets you tune your game
settings without deploying new versions of your application. When a player
launches your game, Remote Config detects contextual attributes used as Rule
conditions (based on Unity, the application, the user, or custom criteria that
you define). The service then returns customized settings for each player
according to the Rules that apply to them.

Use `udpStore` as an attribute in your Rule conditions, so you can determine
game settings that depend on which UDP store the game was downloaded from.

To implement udpStore with Remote Config, follow these steps.

  1. Download and install the UDP package.
  2. Download and install the **Unity Remote** A downloadable app designed to help with Android, iOS and tvOS development. The app connects with Unity while you are running your project in Play Mode from the Unity Editor. [More info](UnityRemote5.html)  
See in [Glossary](Glossary.html#UnityRemote) Config package. See the [Remote
Config documentation](https://docs.unity3d.com/Packages/com.unity.remote-
config@latest/index.html).

  3. Create an AppAttributes struct, which at least has a parameter, “udpStore”:  
` public struct AppAttributes { public string udpStore; } `

  4. In the game code, implement the Remote Config ConfigManager.FetchConfigs call.
  5. When calling FetchConfigs, create a new instance of the AppAttributes struct, read the UDP store data file from: Application.PersistentDataPath + ‘/Unity’ + /Application.CloudProjectId + /udp/udp.json Use JSONUtility.FromJsonOverwrite to read the contents of the file as a text asset.  
` { string udpFilePath =
System.IO.Path.Combine(Application.persistentDataPath, "Unity",
Application.cloudProjectId, "udp", "udp.json"); string udpFileContents =
System.IO.File.ReadAllText(udpFilePath); var appAttr =
JsonUtility.FromJson&lt;AppAttributes&gt;(udpFileContents);
Unity.RemoteConfig.ConfigManager.FetchCompleted +=
ConfigManager_FetchCompleted;
Unity.RemoteConfig.ConfigManager.FetchConfigs(null, appAttr); } `

  6. Ensure the AppAttributes struct is used in ConfigManager.FetchConfigs.
  7. Open the **Remote Config** settings (**Services** > **Remote Config** > **Configure**), and create the parameters that you’d want to change based on the UDP store.
  8. When the parameters are set up, and instrumented in the game code, create a rule for each store in the Remote Config window.
  9. In each rule’s condition, put: app.udpStore == “[storeName]”  

     * See the values for udpStore  
![](../uploads/Main/UDPServiceInteroperability_01.png)

  10. To enable the setting, select the checkbox next to the name of the rule on the left panel in the Remote Config settings.
  11. Build the app to a device and ensure the rules are properly applied, and ship it.

## Implementing IAP items for UDP with Unity IAP

If you want to implement UDP using **Unity IAP** Abbreviation of Unity **In
App Purchase**  
See in [Glossary](Glossary.html#UnityIAP), first [set up Unity
IAP](https://docs.unity3d.com/Manual/UnityIAPSettingUp.html).

**Note** : If you choose to implement UDP with Unity IAP version 1.22.0–1.23.5
(instead of using the UDP package) then implement via Unity IAP only.

Unity IAP automatically handles the following:

  * Initializing UDP
  * Querying the store’s IAP product inventory
  * Requesting to purchase a product
  * Consuming the purchased item

However, your game must properly use Unity IAP’s similar functions (such as
initialization and purchase) according to the [Unity IAP
Documentation](https://docs.unity3d.com/Manual/UnityIAP.html).

When you’ve implemented your game’s in-app purchases with Unity IAP, take the
following steps to set up UDP with Unity IAP.

### Querying IAP inventory

#### With Unity IAP (code implementation)

##### Fetching IAP products defined in the Editor

When fetching the IAP products to pass to the `queryInventory` method, invoke
`ProductCatalog.LoadDefaultCatalog()`. This returns the IAP products defined
in the Editor’s **IAP Catalog** (**Services** > **Unity IAP** > **IAP
Catalog**).

For instance:

    
    
    var catalog = ProductCatalog.LoadDefaultCatalog();
    
    foreach (var product in catalog.allValidProducts)
    {
       if (product.allStoreIDs.Count > 0)
       {
           var ids = new IDs();
           foreach (var storeID in product.allStoreIDs)
           {
               ids.Add(storeID.id, storeID.store);
           }
           builder.AddProduct(product.id, product.type, ids);
       }
       else
       {
           builder.AddProduct(product.id, product.type);
       }
    }
    

##### Fetching IAP product information from the UDP console

If you plan to modify your game’s IAP Catalog on the UDP Console, prepare your
game to fetch IAP product information from the UDP Console.

When fetching the IAP products to pass to the `queryInventory` method, invoke
builder.AddProduct to retrieve specific IAP products defined from the UDP
console:

`builder.AddProduct(product.id, product.type, new IDs{})`

To display the product price, formatted with currency, use
`productInfo.Value.Price`.

##### Fetching the IAP Catalog from the UDP console

To retrieve all the IAP products defined on the UDP Console, don’t invoke any
IAP product retrieval method. Your game will then fetch the entire IAP Catalog
from the UDP Console.

Note: Uploading a CSV file of IAP products on the UDP Console entirely
overwrites your IAP Catalog.

#### Filling in the IAP Catalog with the Unity IAP package

Add and configure your [IAP Catalog](udp.html#iap-catalog) all your in-app
purchases for UDP.

**Note** : If you don’t use an IAP Catalog in your game client (for instance,
you maintain your IAP items solely on your game server) you must still [create
your IAP Catalog on the UDP console](udp-implementing-iap.html#create).

  1. In the Unity Editor, select **Services** > **Unity IAP** > **IAP Catalog**.
  2. Select **Add Product** and enter the details for each IAP product. 
    1. Add the price for the IAP item under Unity Distribution Portal Configuration. ![](../uploads/Main/UDPGamesWithIAP_09.png)
  3. To save your IAP product to the UDP console, select **Sync to UDP**. Do this for each IAP product you create.

To make sure the IAP Catalog is properly saved, check that the items you added
are displayed in the UDP console.

[](udp-managing-and-publishing.html)

Managing and publishing your game on the UDP console

[](udp-firebase.html)

Using Firebase with UDP builds

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

