[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-managing-and-publishing.html)
  * [中文](/cn/current/Manual/udp-managing-and-publishing.html)
  * [日本語](/ja/current/Manual/udp-managing-and-publishing.html)
  * [한국어](/kr/current/Manual/udp-managing-and-publishing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-managing-and-publishing.html)
  * [中文](/cn/current/Manual/udp-managing-and-publishing.html)
  * [日本語](/ja/current/Manual/udp-managing-and-publishing.html)
  * [한국어](/kr/current/Manual/udp-managing-and-publishing.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * Managing and publishing your game on the UDP console

[](udp-sandbox-testing.html)

Testing your game in the UDP sandbox

[](udp-service-interoperability.html)

Using UDP with other services

# Managing and publishing your game on the UDP console

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
## Uploading your game to the UDP console

Once you’ve built your game in the Unity Editor, the UDP console needs to
repack it with each store’s SDK before you can publish your game to the
supported stores. To upload your build to the UDP Console, follow these steps.
**Note** : The UDP console only accepts **APKs** The Android Package format
output by Unity. An APK is automatically deployed to your device when you
select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) or AABs that have a UDP implementation.

  1. On the UDP Console, select your project in **My Games**.
  2. In the Game Info tab, go to the **Binary** section. 
     * Select **Upload APK** and upload the APK file (and OBB files, if any) of your game.
     * To upload AAB files, select **Convert from AAB file** and upload the file.

You can also deploy your game to the UDP console in the following ways:

  * Using the UDP API
  * [Upload your APK to Build Automation](udp-service-interoperability.html#upload), and deploy it to UDP from there
  * [Build your game with Build Automation](udp-service-interoperability.html#build), and deploy it to UDP from there

### Uploading your game to the UDP console using the UDP API

You can only use the [UDP API](udp-api.html) to upload binary files for the
draft version of your game. If there is no draft version of your game, UDP
creates one based on the latest version of your game. If the upload process is
successful, UDP returns the “upload success” message with status code 200. If
the upload process is unsuccessful, UDP returns an error message with a
non–2xx status code.

You can upload either:

  * An APK file, a main OBB file (optional) and a patch OBB file (optional).  
This overwrites any existing AAB file in the UDP console.

  * An AAB file.  
This overwrites any existing APK or OBB file in the UDP console.

You can only upload one binary file at a time; you can’t specify multiple
binary files for a command. If you upload the same type of binary file
multiple times, the most recent file overrides the previous one.

#### Prerequisites

To use the UDP API, you need:

  * A valid authentication token from the UDP console.  
To generate an authentication token in the UDP console, go to the Developer
API page and select **New Token**.

  * A tool to send HTTPS POST messages. Unity recommends using [curl](https://curl.se/).

#### Uploading binary files

To upload binary files to the UDP console using the UDP API, use the HTTP POST
method, and set the `Content-Type` to `multipart/form-data`. For information
on the supported API parameters, see [UDP API](udp-api.html).

#### Uploading APK files

To upload an APK file, specify the path to your APK file in the POST method
with the form key `uploadFile`.

Example:

    
    
    $ curl -XPOST -F 'whatsNew="example"' -F 'useGoogleService=false'  -F 'uploadFile=@/path/to/your/APK/example.apk'
    https://distribute.dashboard.unity.com/developer/api/upload/12369536319506/1d1a4cxq774MzPKwsiHgXA?token=NWQxMWIzZmYyNjk0Njc2NGYwMDU0ZTA3ZTk3YjA2ZDA=
    

#### Uploading AAB files

To upload an AAB file, specify the path to your AAB file with the form key
`uploadFile`.

Example:

    
    
    $ curl -XPOST -F 'whatsNew="example"' -F 'useGoogleService=true  -F 'uploadFile=@/path/to/your/AAB/example.aab'
    https://distribute.dashboard.unity.com/developer/api/upload/12369536319506/1d1a4cxq774MzPKwsiHgXA?token=NWQxMWIzZmYyNjk0Njc2NGYwMDU0ZTA3ZTk3YjA2ZDA=
    

#### Uploading OBB files

To upload an OBB file:

  1. Specify the path to your OBB file with the form key `uploadFile`.
  2. Specify the OBB type. Set the query parameter key `obbType` to `mainObb` or `patchObb`.

Example main OBB file upload:

    
    
    $ curl -XPOST -F 'uploadFile=@/path/to/your/OBB/exampleMain.obb'
    https://distribute.dashboard.unity.com/developer/api/upload/12369536319506/1d1a4cxq774MzPKwsiHgXA?token=NWQxMWIzZmYyNjk0Njc2NGYwMDU0ZTA3ZTk3YjA2ZDA=&obbType=mainObb
    

Example patch OBB file upload:

    
    
    $ curl -XPOST -F 'uploadFile=@/path/to/your/OBB/examplePatch.obb'
    https://distribute.dashboard.unity.com/developer/api/upload/12369536319506/1d1a4cxq774MzPKwsiHgXA?token=NWQxMWIzZmYyNjk0Njc2NGYwMDU0ZTA3ZTk3YjA2ZDA=&obbType=patchObb
    

## Finalizing game info

Before you can publish your game to a store on the UDP console, follow these
steps:

  1. [Edit your game information](udp-distribution.html#edit), including: 
    1. Check the Sandbox Testing section to ensure testing was successful.
    2. Upload your app signing private key
    3. Indicate your use of ads.
    4. Set a premium price (if applicable).
    5. Localize your game information for additional languages (if applicable).
    6. Finalize your IAP products.
  2. Release your game revision.

You can then proceed to publish your game.

### Release your revision

To be able to publish your game to stores, you need to release it. When you
have saved your revision draft and are ready to publish it:

  1. In the Game Info page, select **RELEASE**.  
A window opens to enter release information.

  2. Enter **Release notes** and a **Release label** to keep track of your revision.
  3. Select **RELEASE**.

Revisions are released versions of your game. This lets you store a record of
changes to your app store submissions throughout time.

A revision’s key components are:

  * your game build (APK file)
  * your IAP catalog
  * your game metadata

If you change one of these elements, your store submission changes, and you
must create a new revision. The revision system is incremental (+1 each time)
and is managed by UDP. You cannot create custom revision numbers. Use revision
notes and labels when you release a new revision to help you keep track of
revisions.

**Note** : If a draft revision has been saved on the UDP console but not
released, you can’t push changes from the Editor that would increment the
revision number.

### Editing a revision

To overwrite an existing revision draft.

  1. Choose the existing revision that you want to edit. Your new draft will inherit all the Game Information data of this revision.
  2. Select **Edit** to make your changes.
  3. Save your changes to create a revision draft.
  4. To make this draft the latest revision, select **RELEASE**. 
    1. Enter release notes and a release label to keep track of your revisions.  
The revision number increments by one from the highest released revision. This
becomes the latest Revision Draft

## Publishing your game to stores

Use the **Publish** panel to publish your game to stores. You can only publish
released revisions to stores.

Follow these steps for each of the stores you want to submit your game to:

  1. Sign up with the store.
  2. Register your game with the store.
  3. Submitting your game to the store.
  4. [Set Advanced settings](udp-reference.html#advanced).
  5. Add company information.
  6. When your setup is complete for all stores, select **Publish**.

For help publishing to specific stores, see **Documentation** > **Partner
Store Guides** in the UDP console.

When you’ve published your game, you can monitor its performance in the
[Reporting Dashboard](udp-reference.html#reporting).

### Sign up with the store

To be able to publish your game to stores, you need to have an account with
them.

To create an account with a store:

  1. In the Publish page, select Sign up to <store name>.  
For some stores, you might be redirected outside the UDP console to complete
your sign-up process with the store.

  2. Follow the onboarding process for the store.

Once you’ve signed up with the store, you can register your game with it.

**Note:** Only the Organization Owner and Manager can sign up with a store.
See [Organization-related permissions](udp.html#permissions) for more details.

Store accounts are per Unity Organization. Any games you publish via UDP are
attached to the Organization from which you published. If you access the UDP
console under a different Organization, you need to sign up again and create a
different account. For more information on how to sign up to individual
stores, see **Documentation** > **Partner Store Guides** in the UDP console.

### Register your game with the store

When you have signed up to a store, you can register your game with the store.

  1. In the Publish page, select Register your game with <store name>.
  2. Confirm the package name you want to register with the store and select **REGISTER**. Some stores ask for additional information when registering the game.

When your game is registered with the store, you can no longer change the
package name for that store.

If you use UDP to generate the [App signing](udp-reference.html#app-sign)
private key, UDP generates a store-specific key to sign the repacked build.
This may also affect third-party services integrated in your game. The store-
specific certificate is available in the **Advanced** section when your game
has been repacked.

Signing your repacked build in this way makes your game more vulnerable to
Google Play Protect warnings.

### Submitting your game to the store

In the Publish tab, select the [target step](udp-reference.html#target) for
the given store.

  1. To publish your game to a store for the first time, select the checkbox for the store.
  2. Select **Submit to Store**.  
UDP repacks and submits your game to the store.

UDP creates a separate build for each store that you publish to, containing
only the store-specific SDK that’s required. Each store-specific build is
signed with a UDP certificate that is specific to your game and to each store.
You can find and retrieve the certificate from the Advanced section of each
store.

Additionally, UDP adds a store-specific suffix to the package name, if
applicable. If this is required, the UDP console will display this information
during the Register step.

**Note** : If required, in the Publish page, you can configure:

  * The countries you want to publish your game to
  * Advanced settings for your game

#### Submitting different revisions to different stores

You can only submit the latest released revision to a store. If you intend to
submit different revisions to different stores, Unity recommends you use the
release labels and notes to identify your revisions.

Example: You want to submit one revision for StoreA and another revision for
StoresBCD.

  1. Create your revision (for example, revision 1) for StoreA. When releasing revision 1, write clear release notes and label your release **StoreA**. 
    1. Submit revision 1 to StoreA.
  2. Create a new revision for StoresBCD. This revision draft will ultimately become revision 2. When releasing revision 2, write clear release notes and label your release **StoresBCD**.
  3. Submit revision 2 to StoresBCD.
  4. When you need to submit a new release to StoreA, you can do so based on your previous submission to that store. Your release labels will show that revision 1 was the last revision labelled **StoreA**.
  5. Select revision 1, and edit it. This will create a revision draft based on revision 1. When you release it, it will become revision 3 (as revision 2 has already been released ).
  6. When releasing revision 3, continue to use the StoreA label. Submit revision 3 to StoreA.

#### Repacking your game

If you’ve previously submitted your game to a store, you can repack the game
without uploading a new IAP catalog. This uses the most recently submitted IAP
catalog.

  1. To repack without uploading a new IAP catalog, select the checkbox for the store.
  2. Select **Repack Game**.

Before you submit your repacked build to stores, download the APK from the
Status tab and test it to ensure your in-app purchases work as expected in the
store’s commercial environment.

**Note** : Changes you’ve made in the Advanced settings for a store are not
overridden if you submit a new version of your game.

### Adding company information

To publish your game to the UDP stores, you need to create a company
information profile. Stores display this information in the “About the
developer” section of your game’s listing on their app store. You only need to
do this once.

  1. On the UDP console, select **Settings** > **Company Info**.
  2. Enter and save your company information.

### Publishing your game

Once you have completed all the above steps, publish your game.

  1. In the Publish tab, select each store you want to submit this game revision to.
  2. Select **PUBLISH**.

Only the latest released revision of your game is taken through the target
steps selected for each store.

If there are any problems with your submission, these are displayed in the
[Detail](udp-reference.html#detail) section.

For stores that are only partially integrated with UDP, you must complete the
submission on the store’s own developer console. To do this, select **Go to
Store** next to the submitted revision. A tooltip explains which steps are
still required. Follow the links and complete your submission on the store’s
console.

## Archiving games

When you no longer need a game on the UDP console, you can archive it.

To archive your game:

  1. Go to the **My Games** panel.
  2. Select your filters for the game. By default, you can see all active games.
  3. Hover over the game to display the **More** menu (⋮).
  4. Select **Archive**.

When you have archived a game, you can then restore it or delete it from the
UDP console.

## Deleting games

To delete games you no longer need on the UDP console:

  1. Follow the steps to archive the game.
  2. Hover over the game to display the **More** menu (⋮). 
    1. Select **Delete**.

**Note** : This permanently removes the game from the My Games tab of the UDP
console, and all of the game’s data from the Reporting Dashboard.

### Restoring archived games

To restore archived games:

  1. Go to the **My Games** panel.
  2. Select the **archived** filter in the selection criteria.
  3. On the game you want to restore, select the **More** menu (⋮).
  4. Select **Restore**.

[](udp-sandbox-testing.html)

Testing your game in the UDP sandbox

[](udp-service-interoperability.html)

Using UDP with other services

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

