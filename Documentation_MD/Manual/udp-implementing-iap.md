[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-implementing-iap.html)
  * [中文](/cn/current/Manual/udp-implementing-iap.html)
  * [日本語](/ja/current/Manual/udp-implementing-iap.html)
  * [한국어](/kr/current/Manual/udp-implementing-iap.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-implementing-iap.html)
  * [中文](/cn/current/Manual/udp-implementing-iap.html)
  * [日本語](/ja/current/Manual/udp-implementing-iap.html)
  * [한국어](/kr/current/Manual/udp-implementing-iap.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * Implementing IAP products

[](udp-distribution.html)

Distributing your game with UDP

[](udp-sandbox-testing.html)

Testing your game in the UDP sandbox

# Implementing IAP products

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
The recommended best practice is to add and manage your IAP products in the
UDP console. The [IAP Catalog](udp.html#iap-catalog) in the UDP console is the
source of truth for what’s submitted to the store’s back-end systems.
Additionally, the UDP console lets you:

  * Manage multiple IAP prices and currencies
  * Add descriptions in multiple languages
  * Upload items in bulk via CSV file (multiple currencies and languages supported)

**Note** : If you are using the UDP package only, you should still create at
least one IAP item in the Unity Editor to test that it can sync with the UDP
console correctly. If you are using the **Unity IAP** Abbreviation of Unity
**In App Purchase**  
See in [Glossary](Glossary.html#UnityIAP) package (codeless implementation),
you must add each IAP item in the Unity Editor and upload them all to the UDP
console. If you are using the Unity IAP package and have implemented IAP in
code, create the IAP items in the UDP console.

If you maintain an IAP Catalog in your game client, UDP keeps it synchronized
between the Unity Editor and the UDP console.

## Managing in-app purchases on the UDP console

In the [UDP console](https://distribute.dashboard.unity.com/), access your
game through the My Games page. In the Game Info page, select the **EDIT
INFO** button to enter edit mode. To save changes select **SAVE**. To discard
your changes, select **CANCEL**. This section covers how to edit, create and
delete IAP products from the UDP console.

![](../uploads/Main/UDPManagingGame_07.png)

### Creating new IAP items

To create new IAP items in the UDP console:

  1. Select **EDIT INFO** on the Game Information page.
  2. Select **Add Item** to create a new item.
  3. Specify and save your [product information](udp-reference.html#iap). 
    1. Follow the requirements for Product IDs to make sure they’re valid for app stores.
    2. Make sure the IAP products you define in your game use the same **Product ID** that is set in the IAP Catalog.
  4. Select **Manage amounts and currencies** to: 
    1. Convert the IAP price from USD to foreign currencies.
    2. Adjust pricing in these currencies.
  5. Select **SAVE** to save your changes.

**Note** : If you have many IAP items to create, consider using the Bulk IAP
Import feature to create all your IAP items at once, including localized
description and pricing in multiple currencies.

If using the UDP package, any new IAP items you add in the Console are synced
to your Unity project. You don’t need to rebuild your game to include them.

### Editing IAP descriptions

To edit IAP descriptions, proceed as follows.

  1. Select **EDIT INFO** on the Game Information page.
  2. Choose the language for which you want to edit your description via the drop-down language selector.
  3. In the In-App Purchases section, select the pencil icon to edit an existing IAP item.
  4. Edit your IAP item information: 
    1. **Product Name** , the name of the IAP item
    2. **Description** , to succinctly describe the IAP item
  5. Select **SAVE** to save your changes.

**Note** : The above steps only edit your IAP item information for the
language selected. If you have a large number of IAP items and languages to
support, consider using Bulk IAP Import to import this information.

### Editing IAP prices and currencies

  1. Select **EDIT INFO** on the Game Information page.
  2. Select **Manage amounts and currencies** for an IAP item to: 
    1. Change the IAP price.
    2. Convert it from USD to foreign currencies.
    3. Adjust pricing in these currencies.
  3. Select **SAVE** to save your changes.

**Hint** : To set currencies as favourite currencies, select the star icon
next to their currency code. This pins the currency to the top of the list.
Deselect the star to unpin.

**Note** : If you have many IAP items and currencies to support, you can use
the **Convert** function to automatically convert all your IAP prices into
global currencies, based on the USD amount set for each IAP item. This
overrides any local prices you have previously set.

Alternatively, use Bulk IAP Import to import all this information at once.

### Deleting IAP items

  1. Select **EDIT INFO** on the Game Information page.
  2. Select the trash can icon to delete an IAP item.
  3. Select **SAVE** to save your changes.

### Importing IAP items in bulk

  1. Select **EDIT INFO** on the Game Information page.
  2. Select **IMPORT CATALOG** in the top-right corner of the In-App Purchases panel.  
See Bulk IAP Import for full coverage of this function.

  3. Select **SAVE** to save your changes.

### Importing game information from Google Play

If you have already published your game on Google Play, you can import the
basic information using your game’s Google Play URL:

  1. Select **Import from Google Play**.
  2. Paste your game’s Google Play URL into the input box.
  3. To specify which language to specifically import, use a Google Play URL that contains the language suffix, for example for Italian use `&hl=it`.  
If your Google Play URL doesn’t contain the language suffix, UDP fetches the
information for the language that you’re currently editing in the UDP console
(if it is set on Google Play).

  4. Select **Import**.
  5. Double-check the outcome as in some instances your computer’s IP address may ultimately determine which language you are served.

## Bulk IAP Import

The Bulk IAP Import feature makes it easier to manage your IAP Catalog if you
have a lot of IAP items. This lets you upload CSV files in the regular UDP
format and in Google Play format to the UDP Console with all your IAP product
details, including prices in multiple currencies and descriptions in multiple
languages.

Unity recommends that you still add an IAP item in the Unity Editor for
testing purposes to ensure you can purchase an IAP item in the sandbox
environment.

**Note** : If your CSV file contains multiple languages, [add the supported
languages](udp-distribution.html#languages) before you import the CSV file.

This section describes how to import your IAP items in bulk via CSV.

### Implementation requirements

#### To add new IAP products

You should only use the Bulk IAP Import function to add new IAP products if
you implemented UDP:

  * With the UDP package
  * With Unity IAP (code implementation)

Unity recommends that you still add an IAP item in the Unity Editor for
testing purposes to ensure you can purchase an IAP item in the sandbox
environment.

#### To add localized descriptions and prices

For all implementations, you can use Bulk IAP Import to assign descriptions in
more languages and prices in more currencies to your existing IAP products.

#### With the UDP Package

You can use Bulk IAP Import to entirely redefine your game’s IAP Catalog
without having to rebuild your game.

You only need to have a UDP implementation in good working order.

#### With Unity IAP (code implementation)

With Unity IAP, you can only sync your IAP Catalog from the Editor to the UDP
Console.

If you will upload your game’s IAP Catalog to the UDP Console via Bulk IAP
Upload, you should prepare your game to fetch IAP product information from the
UDP Console, rather than from the game client’s default IAP Catalog.

To allow your game to fetch the IAP Catalog from the UDP console, do not
invoke any IAP product retrieval method in your code.

For more information, see [Querying IAP
inventory](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/games-
with-iap.html%23query-iap).

### Download the CSV Template

UDP provides a CSV template you can use for bulk import of IAP products. The
template is in the regular UDP format for CSV files.

  1. Select **EDIT INFO** on the **Game Information** page.
  2. Go to the **In-App Purchases** panel.
  3. Select **IMPORT CATALOG**.
  4. Select **Download Template**.

### Fill in the CSV file

CSV files use commas (,) and semicolons (;) to separate data values. Commas
separate primary data values, and semicolons separate subvalues.

Each IAP item must appear entirely on a single line within the CSV file.

You must enter data in the exact [format](udp-reference.html#csv) of the
template provided. The UDP console displays an error message if you upload a
file that contains errors, such as invalid price syntax or missing languages.

### Upload your CSV file

  1. Select **EDIT INFO** on the **Game Information** page.
  2. Go to the **In-App Purchases** section.
  3. Select **IMPORT CATALOG**.
  4. Select **Upload CSV** or drag and drop your CSV file in the designated box.
  5. Select **IMPORT** to upload your IAP Catalog to the UDP console.

**Note:** Uploading a CSV file entirely overwrites this revision’s IAP
catalog. The UDP console only uses the information contained in your CSV file;
any other IAP information you previously entered via the UDP console is lost.

### Export a CSV file

To re-use or modify an existing IAP Catalog:

  1. Select **EDIT INFO** on the Game Information page.
  2. Go to the In-App Purchases section.
  3. Select **EXPORT CATALOG**.  
This exports your existing IAP Catalog as a CSV file in the regular UDP
format.

  4. Modify the CSV file.
  5. Upload your CSV file.

The **EXPORT CATALOG** button is only shown if you have IAP products in your
IAP Catalog, and is only visible in edit mode. The image below shows this
button in the In-App Purchases section.

![](../uploads/Main/UDPBulkImport_06.png)

## Import IAP products from Google Play format

UDP also supports CSV files in Google Play format.

To import IAP products using a Google Play CSV file:

  1. Select **EDIT INFO** on the **Game Information** page.
  2. Go to the **In-App Purchases** section.
  3. Click **IMPORT CATALOG**.
  4. Select the **CSV file in Google Play format** checkbox.
  5. Select Upload CSV or drag and drop your CSV file in the designated box. 
    1. In the **Google Play default currency** field, select the default currency for your game.
  6. Select **Import** to upload your IAP Catalog to the UDP console.

### Pricing

Google Play sets pricing by country, UDP sets pricing by currency. Therefore
the import maps countries to currencies. If for an IAP product you’ve set
different prices across countries using the same currency (for example, EUR in
European countries) UDP uses the first country in the list for the currency.
If there are several countries with USD listed, the US locale is used.

UDP does not support Google Play’s pricing templates. This setting is ignored.
UDP only uses the local prices provided in the CSV file.

### Default currency

UDP uses USD as its default currency. If you don’t have USD pricing on Google
Play, UDP converts your Google Play default pricing and currency into USD and
uses this as the UDP default pricing.

Local prices that are set in your CSV file are maintained in their respective
currencies.

For countries that aren’t explicitly set in the CSV file, UDP converts your
Google Play default pricing and currency into their respective currencies.

### IAP products

The type of IAP products (consumable / non-consumable) cannot be determined
from your CSV file; you need to tell UDP the type of each IAP product.

UDP does not support Auto-Translate. This setting is ignored. UDP only uses
the localized descriptions provided in the CSV file.

[](udp-distribution.html)

Distributing your game with UDP

[](udp-sandbox-testing.html)

Testing your game in the UDP sandbox

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

