[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-reference.html)
  * [中文](/cn/current/Manual/udp-reference.html)
  * [日本語](/ja/current/Manual/udp-reference.html)
  * [한국어](/kr/current/Manual/udp-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-reference.html)
  * [中文](/cn/current/Manual/udp-reference.html)
  * [日本語](/ja/current/Manual/udp-reference.html)
  * [한국어](/kr/current/Manual/udp-reference.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * UDP reference

[](udp-firebase.html)

Using Firebase with UDP builds

[](udp-api.html)

UDP API

# UDP reference

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
## UDP console reference

This section provides a high-level overview of the UDP console’s information
architecture.

The UDP console contains a navigation bar that lets you navigate between the
following sections of the UDP console:

  * Overview
  * My Games
  * Store Sign-Ups
  * Reporting
  * Documentation
  * Resources
  * Settings
  * Developer API

### Overview

The Overview tab of the UDP console contains useful information on how to use
the UDP console, including:

  * Tutorial videos
  * A walkthrough guide to help you track your progress
  * Store-specific information
  * FAQ

### My Games

The My Games tab displays your UDP projects. From here you can switch between
UDP projects, [create a new game](udp-distribution.html#create), and
[archive](udp-managing-and-publishing.html#archive) and [restore](udp-
managing-and-publishing.html#restore) games.

You can filter the list of games by status, for example:

  * **All Games**
  * **Published to UDP**
  * **Submitted to stores**
  * **Live on stores**

If you select **Submitted to stores** or **Live on stores** , you can also
filter the list of games by store.

When you select a game, the following tabs are available:

  * Game Info
  * Publish
  * Status

Each game card displays the status of the game. The Published status indicates
the game has completed the available steps to be repacked and submitted to the
store.

#### Game Info

Use the Game Info page to view and edit your game information. See [Entering
game information on the UDP console](udp-distribution.html#edit) To view the
Game Info page for a game, select the card in the My Games tab.

The Game Info page contains the following sections:

  * Game Description
  * Binary
  * Ads
  * Premium Price
  * In-App Purchases
  * Sandbox Testing
  * App Signature
  * Integration Information

![](../uploads/Main/UDPManagingGame_01.png)

The Game Info page contains a progress bar to display how close you are to
being able to release your game. Each section displays a **Completed** status
when you have added the necessary info for that section.

#### Game description

Use the Game Description section to enter information that the app stores will
display for your game.

The table below describes a superset of all the participating stores’
requirements. Not all stores use all the properties described. The UDP console
flags which fields are mandatory and which are optional. The UDP console also
indicates any store-specific syntax requirements.

Property | Description  
---|---  
**Import from Google Play** | If you have already published your game on Google Play, you can import the basic information using your game’s Google Play URL.  
**Game Title** | The title of your game (this field is synced with the Editor).  
**Genre** | Indicates the category that your game belongs to. You can choose from Action, Adventure, Arcade, Board, Card, Casino, Casual, Educational, Music, Puzzle, Racing, Role Playing, Simulation, Sports, Strategy, Trivia, and Word.  
**Device** | Choose between Smartphone, Tablet, or Universal.  
**Game Icon** | The game icon to display on the app stores.  
**Short Description** | Short description (max 60 char) of your game to display on the app stores.  
**Description** | Full-length description (4,000 char) of your game to display on the app stores.  
**Game Banners** | An image used by stores to feature your game. For example, it can be a placement in a carousel. The landscape banner is mandatory, the portrait banner is optional.  
**Keywords** | Define up to 4 keywords (30 char each). These are used for search purposes in the app stores.  
**Feature Video** | Add a video trailer for your game.  
**Note** : For videos, some stores only accept MP4 files while others only
accept a Youtube link. Unity recommends you upload both.  
**Screenshots** | Add screenshots of your game, including the cover image (thumbnail) to lay over the MP4 video when it’s not playing.  
Add at least four images per orientation that you use.  
Some app stores only accept either portrait or landscape images, but not both.
If you upload both portrait and landscape images to UDP, select your preferred
orientation in the **Preference** field. UDP will inform you if the
screenshots don’t meet the stores’ requirements.  
**Use these screenshots for all languages** | Enable this toggle to use the same screenshots for all languages. Disable this toggle if you want to add language-specific screenshots.  
**Preference** | Certain stores only accept portrait or landscape images. For such stores, specify which orientation of image to use.  
**Ratings** | Select the audience which the game is suitable for.  
  
You can specify metadata for each of your supported languages. To add new
languages, select the language dropdown while in edit mode and select Manage
Languages.

![](../uploads/Main/UDPManagingGame_02.png)

#### Binary

Use the Binary section to upload your **APK** The Android Package format
output by Unity. An APK is automatically deployed to your device when you
select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) file and OBB files, or AAB files:

Property | Description  
---|---  
**APK Files (or AAB)** | Your UDP game build. If you pushed your UDP build via Build Automation, you don’t need to upload it again.  
For UDP to accept your APK file, the APK file:  
\- Must contain a `versionName`  
\- Must have an `Initialize()` method  
\- Must have a `Purchase()` method (for games with IAP)  
If you upload a new APK version which contains a different package name, you
will receive an error. This also prevents publishing the new APK version.  
To upload an Android App Bundle (AAB) file, select the **Convert from AAB
file** option. UDP converts AAB files to APK for publishing to stores.  
**Version code** | This field is only displayed once you’ve uploaded your game to UDP.  
**Minimum Android Version Support** | Minimum supported Android version for your game. This field is only displayed once you’ve uploaded your game to UDP.  
**What’s New** | Describe what’s changed with this version of your game. UDP publishes this information in the stores.  
This field is only displayed once you’ve uploaded your game to UDP.  
**OBB File (Main)** | The main extension file for additional resources that your game or app might need.  
**OBB File (Patch)** | Optional file to make small updates to the main expansion file.  
**Does your game use Google Play Services?** | Knowing about your Google Play Services usage helps UDP better guide you during the submission stage.  
  
OBB files aren’t pushed during a **Build Automation** A continuous integration
service for Unity projects that automates the process of creating builds on
Unity’s servers. [More info](https://docs.unity.com/devops/en/manual/unity-
build-automation)  
See in [Glossary](Glossary.html#BuildAutomation) deployment, so if your game
uses them you must upload them manually to the UDP console.

**Note** : You can only change the APK files and OBB files in the default
language view (English).

#### Ads

The table below describes the Ads section.

Property | Description  
---|---  
**Does your game contain ads** | Select whether or not your game contains ads. This information is useful for UDP to better guide you during submission.  
**What ad mediation solutions does your game use?** (Optional) | If your game contains ads, select which mediation solutions your game uses.  
**What ad networks does your game use?** (Optional) | If your game contains ads, select which ad networks your game uses.  
  
Certain stores expect you to implement their proprietary ad network in games
you submit to them.

UDP asks if your game contains ads to better inform your submissions to the
stores, especially if UDP can ascertain that your submission will be rejected
from a store because of this.

Stores which might reject your game display a warning icon in the Publish
section, and a tooltip to explain the issue that might occur. UDP otherwise
doesn’t modify your game’s ad implementation in any way.

**Note** : Tests of the most common mediation layers and ad networks indicate
that games repacked for the UDP stores generally have no problem receiving ad
campaigns. Feel free to contact [UDP Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692) about your ad setup and its
suitability for distribution via UDP. Make sure you mention which mediation
SDK and ad networks your game uses, to get a better-informed answer faster.

#### Premium price

The Premium price is the price it costs players to download your game.

Property | Description  
---|---  
**Manage amounts and currencies** | Set the price of the game in USD.  
Select **Convert** to automatically convert the USD price into the other
listed currencies. You can also edit prices manually for specific currencies.  
  
**Note** : You can only submit premium games to stores which support premium
games.

#### In-App Purchases

Use the In-App Purchases section to add and manage IAP items.

If using the UDP package, UDP automatically keeps your game’s IAP Catalog
synchronized between the Unity Editor and the UDP console.

Property | Description  
---|---  
Search box | Filter the list of IAP items by text.  
Type dropdown | Filter the list of IAPs by type, that is, consumable or non-consumable.  
Sort dropdown | Choose how to sort the list of IAP items.  
**Add Item** | Click to add a new IAP item. This opens a window to enter the IAP details.  
**Manage amounts and currencies** | Click to set prices for additional currencies.  
**Convert** | Converts the USD price of your IAP item into global currencies. This overwrites any manually set prices for other currencies.  
**Favourite Currencies** | Select to open the Favourite currencies window. To set currencies as favourite currencies, select the star icon next to their currency code. This pins the currency to the top of the list. Deselect the star to unpin.  
  
##### IAP Item window

Use the IAP Item window to add and edit details for IAP products. To open this
window select **Add Item**. The table below describes the windows of the **Add
IAP Item** window.

Field | Description  
---|---  
**Product ID** | The unique ID used to identify the IAP product.  
Product IDs must follow these requirements:  
\- Start with a letter or a digit  
\- Contain only letters, digits, dots (.) and underscores (_)  
\- Must not use capitalized letters  
**Product Name** | The name of the IAP product.  
Currency | Displays the currency the price is shown in.  
Price | The price of the IAP product in USD.  
You must specify a price to enable players to purchase products in your game.  
**Consumable** | Select this option for consumable IAP items.  
**Description** | A short description of the IAP product.  
  
#### Sandbox Testing

The Sandbox Testing section displays the test status for your game. Use this
section to create user credentials for testing in the sandbox environment and
view the status of the tests. The table below describes the fields of this
section.

Field | Description  
---|---  
**Test status** | Displays the test status for the game.  
**UDP Initialization** | Displays the test status for the Initialization check. This checks to ensure the Initialize() method is called (for all games).  
**IAP Transaction** | Displays the test status for the IAP transactions check. Purchase() method is called (for IAP games only)  
**Sandbox Test Account** | The email address for the sandbox test account. This is used as the login name for the UDP sandbox environment only.  
**Password** | The password for the test account.  
  
#### App Signature

UDP uses an App-signing private key to sign the repacked APK files that are
submitted to the stores.

Unity recommends that you select **Export and upload the key and certificate**
and use your own App signing private key. If your game is released on Google
Play, use the same key as on Google Play. This significantly decreases the
chance of Google Play Protect flagging your game when users install it.

**Note** : If your game is flagged, you can appeal to Google
[here](https://support.google.com/googleplay/android-
developer/answer/2992033?hl=en).

The table below describes the App Signature section of the Game Info tab.

Property | Description  
---|---  
**Export and upload the key and certificate (recommended)** | UDP uses the App signing private key you upload to sign the repacked builds. If you select this option, it applies to all stores you submit your game to.  
**Let UDP create and manage App signing private key** | UDP generates a different App signing private key for each store the game is repacked for.  
This option leaves your game more vulnerable to Google Play Protect warnings.  
  
**Note** : App signature generation is only supported for Android SDK Version
18 and above. If your game uses a lower SDK version than this, use the RSA
algorithm signature or increase the game’s Minimum API Level.

##### Changing keys

You can switch from using the UDP key to your own key at any time. This change
only applies for stores that the game hasn’t been repacked for (and therefore
signed). If you have previously repacked for a store using the UDP key, that
store will always use the UDP key.

You can only switch from using your own key to the UDP key if you haven’t
repacked your game (and your own key) for any store.

##### UDP-generated keys

UDP uses company information to generate a keystore for the repacked APK files
when the following conditions are met:

  * The APK file uploaded by the developer doesn’t contain the keystore file.
  * The game hasn’t been repacked in the partner store.

If these conditions aren’t met, UDP uses an existing UDP keystore if
available, or it uses the developer information to generate a new signature
file.

#### Integration Information

This information is synced with the Editor. The following fields are editable:

Field | Description  
---|---  
**Unity Project ID** | The Unity project ID linked to the UDP client.  
To unlink a Unity project from the UDP client, delete the ID in this field and
select **Save**.  
**Note** : Only owners and managers can edit this field.  
**Callback URL** | URL of the game server. UDP uses this to send notifications for payment results.  
  
#### Release window

The Release window lets you release versions of your game. This is displayed
when you select Release in the Game Info page.

The Release window contains fields to specify the version’s:

  * Tag
  * Release notes

The tag and release notes of all your revisions are visible in:

  * The Game Info section, when expanding the Revision drop-down
  * The Status section, which is organized by Release

**Note** : You can only publish the latest revision to the stores.

Learn more about:

  * [Editing revisions](udp-managing-and-publishing.html#release)
  * [Submitting different revisions to different stores](udp-managing-and-publishing.html#select-target)

### Publish Panel

Use the Publish panel to sign up to stores and publish your games. Each store
has its own section in the page.

![](../uploads/Main/UDPManagingGame_11.png)

The table below describes the Publish page.

Field | Description  
---|---  
**Publish** | Publishes the selected games.  
**Only show stores that accept the game’s pricing model** | Hides stores that don’t support your game’s pricing model from the Publish page.  
**All Stores** | Selects all visible stores for publishing.  
Store checkbox | Select the checkbox for a store to only publish to selected stores.  
**Premium** | The Premium label is displayed for stores which support premium games.  
**IAP** | The IAP label is displayed for stores which support IAP.  
Info icon | The info icon states whether the store is fully or partially integrated with UDP.  
**Sign up** | Sign up to the selected store.  
**Countries** | Select Countries to choose which countries you want to publish your game to.  
This opens a window containing a list of countries which the store supports.
Select the checkboxes to enable your game for a country and select Save.  
This option is only displayed when you’ve signed up for the store.  
**Advanced** | Select to configure advanced properties for a specific store.  
This option is only displayed when you’ve signed up for the store.  
  
#### Target steps

In the Publish tab, each store contains a dropdown to let you select the
target step for the given store. The following options are available:

Target step | Description  
---|---  
**Repack Game** | UDP unpacks the generic UDP build and repacks your game with the SDK from the selected store. This uses the IAP catalog from the last build you submitted to the store.  
**Submit to Store** | UDP repacks and submits your game, its metadata and its IAP catalog to the production environment of the selected stores.  
The first time you publish your game, you must submit it to create an IAP
catalog on the stores’ servers.  
  
### Advanced settings

To configure store-specific settings before you submit your game, select
Advanced for the store in the Publish tab. You can configure the following
properties specifically for a store:

Property | Function | Affected store  
---|---|---  
**Target SDK** | The version of the store SDK that you publish your game to. By default, UDP repacks for the latest version of the store SDK. | All  
**CP ID** | Merchant ID on the Huawei AppGallery Connect console. | Huawei  
**Product ID** | Product ID on the Huawei AppGallery Connect console. | Huawei  
**App ID** | Application ID on the Huawei AppGallery Connect console. | Huawei  
**Configuration version on the Huawei AppGallery Connect console.** | Version of the game | Huawei  
**PubKey** | Public key on the Huawei AppGallery Connect console. | Huawei  
**App Secret** | App secret on the Huawei AppGallery Connect console. | Huawei  
**privacyPolicy** | Privacy statement address on the Huawei AppGallery Connect console. | Huawei  
**Premium Price** | The price players will pay to download your game. | All stores which support premium games  
**In-App Purchases** | The name of your IAP items. | All  
**Approval Number from SAPPRFT (aka ISBN)** | Enter the SAPPRFT approval number for games you publish in China. If you don’t have a publishing licence for this, deselect China from the country list. | Xiaomi  
Huawei  
**Registration Number from MCPRC** | Ministry of Culture Record number for games you publish in China. | Huawei  
**Launch Manually** | Set to launch the game manually on the store. | Huawei  
**Launch on** | Specify a date and time to launch your game on the store. | Huawei  
**Renew authentication** | Select to renew your authentication token for the selected store. | Huawei  
**Package Name** | Displays the name of the package. This can’t be edited once it’s been registered. | QooApp  
Viveport  
**URL for Privacy Policy** | Enter the URL of your game’s privacy policy. | Viveport  
**URL for EULA/Terms of Use** | Enter the URL of your game’s EULA/Terms of use. | Viveport  
  
#### Detail

If your submission is missing anything, the UDP console displays error or
warning messages. Select **Detail** to expand for more information on the
problem.

Errors are displayed in a red panel. You must fix errors before you can submit
your game. Select **Modify** to go to the erroneous area to fix the issue.

You can also choose to only submit to stores where there are no errors.

Warnings are displayed in a yellow panel. You can dismiss the warnings you
decide to ignore.

### Status panel

When UDP starts processing your game, visit the **Status** panel to monitor
progress and check the submission history of your game.

The **Status** panel displays an overview of your game’s history.

Field | Description  
---|---  
**Revisions repacked** | Total number of repacked APK builds created with UDP.  
**Note** : If a game has been repacked three times for the same stores, this
counts as three.  
**Revisions submitted** | Total number of submissions made via UDP.  
**Note** : If a game was submitted five times to a store, this counts as five.  
**Submissions accepted** | Number of submissions that have been accepted to app stores.  
**Submissions rejected** | Number of revisions that have been rejected by app stores.  
  
For each game revision, the **Status** panel displays the following details:

Field | Description  
---|---  
**Store** | The store(s) that the game was submitted to.  
**Status** | The status of the revision.  
Not all stores can provide visibility until ‘Live’. The Status section only
provides the information it can get from the store.  
**Countries** | The number of countries which your game is enabled for, for each store. Select the number in this column to view the countries.  
**Action** | Perform additional actions, such as **download** revisions of your game or **go to store** to complete publishing steps.  
  
Your game can have the following statuses:

  * **Repacked** : your game was successfully repacked with the SDK of the selected store
  * **Published** : your game has passed all the steps required for the store when repacking and submitting to that store
  * **Pending** : your game is being repacked with the SDK of the selected store
  * **Failed** : your game couldn’t be repacked with the SDK of the selected store
  * **Canceled** : your game submission was cancelled by you or someone from your Organization

### Store Sign-Ups

The Store Sign-Ups tab displays information about the stores you can
distribute your game to using UDP.

![](../uploads/Main/UDPSettingUp_07.png)

Select the More link for more information on a store, such as overview, FAQs,
and other useful links specific to each store.

For an overview of information for all stores, select **Compare stores** to
open the Partner Stores cheatsheet. This compares details for all stores,
including data such as number of users, countries in which the store is
available, and whether or not the store supports premium games.

### Reporting dashboard

The Reporting tab displays performance information for your published games.
Monitor the performance of your published games from the Reporting dashboard,
which is accessible from the top navigation bar.

![](../uploads/Main/UDPReportingDashboard_01.png)

You can filter the information presented on the Reporting dashboard by game
and store.

![](../uploads/Main/UDPReportingDashboard_02.png)

If you don’t select anything in the **All Games** and **All Stores** filters
for the whole Reporting dashboard, you can view breakdowns on an individual
chart level (where applicable). On supported charts, select the **by store**
or **by game** filters to view performance on specific stores or for
individual games.

The Reporting dashboard is divided into five panels, all subject to the Games
and Stores filters. For the panels which are subject to the date filter, you
can export chart data as CSV files and images. To download the data as a CSV
file or image, select the corresponding icon for the chart.

**Note** : The Huawei AppGallery only returns revenue information to UDP if
you’ve set up server-side validation using QueryOrder. If you used callback
notifications, no revenue-related charts or information is available for
Huawei.

#### Metrics and definitions

The **Reporting** dashboard tracks the following data from the UDP stores
where your games are published:

Metric | Description  
---|---  
**Gross revenue** | Amount collected from players in USD (for example, if IAP price= 0.99 then= $0.99)  
**Players** | The number of unique users who downloaded and started the game. This is calculated by unique devices.  
**Spenders** | The number of paying players. That is, the number of unique users who have made at least one successful payment.  
**Days since 1st activity** | The number of days since a game reached 10 players on an app store.  
**New Players** | Number of players who started the game for the first time during the selected time period.  
****DAU**(Daily Active Users) The number of different players who started a
session on a given day. DAU includes both new and returning players. [More
info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#DAU)** | Daily active users. The number of unique users who launched the game at least once on that day.  
****MAU**(Monthly Active Users) The number of players who started a session
within the last 30 days. [More info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#MAU)** | Monthly Active Users. The number of unique users who launched the game at least once during the last 30 days.  
**IAP Revenue** | Gross revenue from IAP, in USD.  
**Average Revenue per Transaction** | This is defined as Revenue / Number of Transactions, in USD.  
****ARPPU**(Average Revenue Per Paying User) Average verified IAP revenue per
user who completed a verified IAP transaction. [More
info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#ARPPU)** | Average revenue per paying user, in USD. This is defined as Gross Revenue / Number of Paying Players.  
**ARPU** | Average revenue per user, in USD. This is defined as Gross Revenue / Number of Players.  
**Spender Conversion Rate** | This is defined as Number of Paying Players / Number of Players.  
**Transactions** | Number of successful transactions which resulted in a payment (OrderID was successful and verified by the UDP server).  
**Revenue by IAP** | Breakdown of gross revenue by IAP, in USD.  
**Transaction Volume by IAP** | Breakdown of transactions by IAP.  
**Premium Revenue** | Gross revenue generated by premium games, in USD.  
**Sessions** | Number of times the game was launched, on any device.  
****Day 1 Retention** The percentage of players who returned to your game one
day after playing the first time. [More info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#Day1Retention) (%)** | This is defined as Percentage of Players that are still active 1 day after their first game launch.  
****Day 7 Retention** The percentage of players who returned to your game
seven days after playing the first time. [More
info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#Day7Retention) (%)** | This is defined as Percentage of Players that are still active 7 days after their first game launch.  
****Day 30 Retention** The percentage of players who returned to your game
thirty days after playing the first time. [More
info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#Day30Retention) (%)** | This is defined as Percentage of Players that are still active 30 days after their first game launch.  
  
**Note:** The Reporting dashboard contains estimated data; you can get exact
numbers directly from the stores. The data shown is in UTC time and is until
the previous day to display the most accurate, complete data.

#### All Time

This panel displays the following lifetime metrics:

  * Gross revenue (in USD)
  * Players
  * Spenders
  * Days since 1st activity

#### Yesterday

This panel displays the following metrics from the last full 24h day (basis
UTC):

  * Gross revenue (in USD) _with $ or % comparison to the previous day_
  * New players
  * DAU _with % comparison with average DAU value of last 7 days_
  * MAU _with % comparison with average MAU value of last 7 days_

#### IAP Performance

This panel displays the following metrics for the selected date range:

  * IAP Revenue
  * Average Revenue per Transaction
  * ARPPU
  * ARPU
  * Spender Conversion Rate
  * Transactions
  * Revenue by IAP. You can view up to 5 IAPs in the chart, and select which ones to view via the drop-down selector. This chart contains presets for: 
    * Most revenue
    * Most transactions
    * Highest price points
    * Lowest price points
  * Transaction Volume by IAP. You can view up to 5 IAPs in the chart, and select which ones to view via the drop-down selector. This chart contains presets for: 
    * Most revenue
    * Most transactions
    * Highest price points
    * Lowest price points

#### Premium Revenue

This panel displays, for the selected date range:

  * Premium Revenue (revenue from paid downloads)

#### Game Health

This panel displays the following metrics for the selected date range:

  * DAU - per day and average over the period
  * MAU - per day and average over the period
  * New Players - per day and total over the period
  * Sessions - per day and total over the period
  * Day 1 Retention Rate - per day and average over the period
  * Day 7 Retention Rate - per day and average over the period
  * Day 30 Retention Rate - per day and average over the period

### Documentation

The Documentation tab displays useful information to help you get started,
including:

  * Links to the UDP documentation
  * Guides to different app stores
  * Video tutorials

### Resources

The Resources tab provides useful information to help you get started,
including:

  * Getting Started Guide
  * Tutorial videos
  * Store Guides
  * Knowledge base
  * Release notes

### Settings

#### Company Information

Use the Company Information window to add information to display for your
company in the app stores. On the UDP console, choose your organization and
select the pencil icon to edit the profile.

Field | Description  
---|---  
**Company Name** | The name of your company as you want players to see it.  
**Company Icon** | Upload an image to display for your company.  
**Location** | The location you want to define as your studio’s headquarters.  
**Company Size** | Use the drop-down to specify the number of people in your company.  
**Official Website** | The official website of your company.  
**Support Email Address** | The support email that players can use to contact your company.  
**Introduction** | Any additional information about your company / studio.  
  
#### Developer API

The Developer API page lets you generate and manage authentication tokens for
use with the [UDP API](udp-api.html). You can use the UDP API to upload binary
files to the UDP console. See [Managing and publishing your game on the UDP
console](udp-managing-and-publishing.html#api-upload)

The table below describes the Developer API page.

Field | Description  
---|---  
**Token** | The authentication token to use to let the UDP API access the UDP console. Select COPY to copy the token to your clipboard.  
**Expiry date** | The expiry date of the authentication token, if specified.  
**Operations** | Edit or delete existing tokens.  
**NEW TOKEN** | Select to create a new token.  
  
## CSV reference

### Data values for CSV files

Each row in a CSV file of In-App Purchases can contain the following values.
Don’t pass empty values.

Field | Description  
---|---  
`product_id` | Represents the ID of a unique IAP product. product_id needs to start with a lowercase letter or a digit and must be composed of only lowercase letters (a-z), digits (0–9), underscores (_), and periods (.)  
`language; product_name; description` | When setting the language value, use the language code listed in TABLE A.  
UDP uses en-US as the default language.  
Use semicolon(;) to separate language, product_name and description.  
To include localized versions of the item’s product name and description, list
the default language, product_name, and description, followed by the
languages, product_names, and descriptions for each locale. In the following
example, the product has en-US (ENGLISH) as the default language and zh-CN
(CHINESE) as a localization:  
en-US;Product 1;This is my first product; zh-CN; 产品1; 产品描述1.  
Note: UDP only imports the fields for languages you’ve defined in the **Game
Info** section of the UDP Console. To support multiple languages, define them
on the UDP Console before you import your IAP catalog.  
`consumable` | Set to TRUE or FALSE (case insensitive) to define whether or not the IAP product is consumable.  
`auto_convert_prices` | If true, UDP automatically converts the price to other currencies. To exclude a currency from conversion, specify the currency and its price in the `currency;price` field.  
`currency; price` | When setting the currency value, use the currency code listed in TABLE B. The price must be positive. The default currency is USD. The price of each IAP product must immediately follow its corresponding currency. For example: USD;0.99;CNY;6  
  
#### **TABLE A - Language codes**

Language | Code  
---|---  
AFRIKAANS | af  
AMHARIC | am  
BULGARIAN | bg  
CATALAN | ca  
CHINESE | zh-CN  
CHINESE (HONG KONG) | zh-HK  
CHINESE (TAIWAN) | zh-TW  
CROATIAN | hr  
CZECH | cs  
DANISH | da  
DUTCH | nl  
ENGLISH (UK) | en-GB  
ENGLISH | en-US  
ESTONIAN | et  
FILIPINO | fil  
FINNISH | fi  
FRENCH (CANADA) | fr-CA  
FRENCH | fr-FR  
GERMAN | de  
GREEK | el  
HINDI | hi  
HUNGARIAN | hu  
INDONESIAN | id  
ITALIAN | it  
JAPANESE | ja  
KOREAN | ko  
LATVIAN | lv  
LITHUANIAN | lt  
MALAY | ms  
NORWEGIAN | no  
POLISH | pl  
PORTUGUESE (BRAZIL) | pt-BR  
PORTUGUESE (PORTUGAL) | pt-PT  
ROMANIAN | ro  
RUSSIAN | ru  
SERBIAN | sr  
SLOVAK | sk  
SLOVENIAN | sl  
SPANISH (LATIN AMERICA) | es  
SPANISH | es-ES  
SWAHILI | sw  
SWEDISH | sv  
THAI | th  
TURKISH | tr  
UKRAINIAN | uk  
VIETNAMESE | vi  
ZULU | zu  
  
#### **TABLE B - Currency codes**

Code | Code | Code  
---|---|---  
AED | IDR | PEN  
**ARS** Augmented Reality [More info](AROverview.html)  
See in [Glossary](Glossary.html#AR) | ILS | PHP  
AUD | INR | PKR  
BGN | IQD | PLN  
BHD | ISK | QAR  
BND | JOD | RON  
BIF | JPY | RUB  
BRL | KES | SAR  
CAD | KHR | SDG  
CHF | KRW | SEK  
CNY | KWD | SGD  
CZK | LAK | THB  
DKK | LKR | TND  
DZD | LYD | TRY  
EGP | MAD | TWD  
EUR | MMK | TZS  
GBP | MXN | USD  
GHS | MYR | UYU  
HKD | NOK | VND  
HRK | NZD | ZAR  
HUF | OMR  
  
### Example 1

    
    
    product_id,language; product_name; description,consumable,auto_convert_prices,currency; price
    com.mystudio.mygame.product1,en-US;Product 1;This is my first product; zh-CN; 产品1; 产品描述1,TRUE,TRUE,USD;0.99;CNY;6;EUR;0.79
    com.mystudio.mygame.product2,en-US;Product 2;This is my second product; zh-CN; 产品2; 产品描述2,FALSE,FALSE,USD;1.99;CNY;12;EUR;1.59
    com.mystudio.mygame.product3,en-US;Product 3;This is my third product; zh-CN; 产品3; 产品描述3,TRUE,TRUE,USD;4.99;CNY;30;EUR;3.99
    

[](udp-firebase.html)

Using Firebase with UDP builds

[](udp-api.html)

UDP API

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

