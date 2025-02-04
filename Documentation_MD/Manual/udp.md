[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp.html)
  * [中文](/cn/current/Manual/udp.html)
  * [日本語](/ja/current/Manual/udp.html)
  * [한국어](/kr/current/Manual/udp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp.html)
  * [中文](/cn/current/Manual/udp.html)
  * [日本語](/ja/current/Manual/udp.html)
  * [한국어](/kr/current/Manual/udp.html)

  * [Unity Services](UnityServices.html)
  * Unity Distribution Portal

[](UnityIAPModuleExtension.html)

Store Extensions

[](udp-getting-started.html)

Getting started with UDP

# Unity Distribution Portal

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
## Overview

Unity Distribution Portal (UDP) lets you distribute your games to multiple app
stores through a single hub. UDP repacks your Android build with each store’s
dedicated In-App Purchase SDK to make your game compatible with the separate
app stores. You can manage all your store submissions from the UDP console.

![](../uploads/Main/UDPOverview_01.png)  
UDP overview

You can use UDP to distribute premium games and games with IAP.

## UDP console

The [UDP console](https://distribute.dashboard.unity.com) is a web-based
portal where you can prepare your games for submission to multiple app stores.
The UDP console lets you:

  * [Manage your game’s information](udp-distribution.html#edit)
  * [Edit your game’s in-app purchases](udp-implementing-iap.html#edit)
  * [Publish your game to multiple app stores](udp-managing-and-publishing.html#publish)
  * [View your games’ performance across all UDP stores](udp-reference.html#reporting)

Learn more about the [UDP console interface](udp-reference.html).

## UDP package

The [UDP
package](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/)
contains an SDK for working with UDP. It also enables the Unity Distribution
Portal settings in the **Project Settings** A broad collection of settings
which allow you to configure how Physics, Audio, Networking, Graphics, Input
and many other areas of your project behave. [More info](comp-
ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) window of the Unity Editor.

## UDP client

To use UDP, your game must have a UDP client, including UDP client ID. This
identifies your game on the UDP service. The ID is generated when you [create
a game on UDP](udp-distribution.html#create) and you must [link it to your
Unity
project](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/getting-
started.html%23linking). To unlink a Unity project from a UDP client, remove
the Unity project ID from the [Integration Information](udp-
reference.html#integrate) section in the UDP console.

## UDP sandbox

The UDP package contains a sandbox environment that acts as a test store for
your UDP games. When you implement the UDP SDK in your game, your UDP build
can then use the sandbox as a test environment. Before you can submit your
game to the real stores, you must [test your game in the sandbox](udp-sandbox-
testing.html) to verify that your UDP and IAP (if applicable) implementation
works properly.

Sandbox testing helps you to identify any issues that arise during your
initial UDP implementation. Unresolved problems could prevent UDP repacking
your game for stores, or cause UDP to repack the game with the existing
problems. This could result in stores rejecting your game or players being
unable to complete transactions.

## Games with in-app purchases

In-app purchases (IAP) let you sell content to players from inside your game.
You only need to implement your in-app purchases via UDP. UDP then
automatically repacks your game into store-specific builds.

You can implement UDP on both the game client and server sides. For offline
games, you only need to implement UDP in the game client. For online games,
you can also implement UDP on the server side.

  * Implementing UDP in-app purchases in the game client  
The implementation in the game client includes initializing the UDP SDK and
integrating with the in-app purchase flow of UDP.

  * Implementing UDP in-app purchases on the server side  
The implementation on the server side lets you query the UDP server about
orders, receive callback notifications, and return the acknowledgements.

Learn how to:

  * [Manage in-app purchases on the UDP console](udp-implementing-iap.html#manage)
  * Implement in-app purchases on the Editor 
    * [with the UDP package](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/games-with-iap.html)
    * [with Unity IAP](udp-service-interoperability.html#iap)
  * [Implement in-app purchases on the server side](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/games-with-iap.html%23server-side)

### IAP product types

UDP only supports consumable and non-consumable IAP products. Subscription
products are not supported.

#### Non-consumable IAP products

Non-consumable products provide permanent effects. Players can only purchase
them once.

#### Consumable IAP products

Consumable products provide temporary effects, such as game currency and extra
experience points. Players can purchase these multiple times.

When a user has purchased a consumable product, they must consume it before
they can repurchase it. You can use the consumption to ensure the purchased
product is successfully delivered.

To [consume a
product](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/games-
with-iap.html%23consume), your game needs to send a Consume request to the UDP
SDK. Your game should deliver a product when it is consumed. This prevents the
product being delivered repeatedly.

### IAP Catalog

The IAP Catalog is an inventory of the IAP items implemented in your game. For
each IAP item, you define a:

  * description
  * price
  * consumable type
  * Product ID

When your game is repacked and submitted to a store, UDP syncs your IAP
Catalog with the store’s back-end. Your game can then query the IAP inventory
from the store’s back-end.

When players purchase IAP products, your game asks the store to confirm the
IAP Catalog. UDP must be properly implemented in your game for this step to
work smoothly.

The IAP Catalog on the UDP console is the source of truth for what is
submitted to the store’s back-end systems.

For a successful implementation, follow the [UDP implementation
guidance](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/games-
with-iap.html). To ensure your IAPs behave properly, [test your game in the
UDP Sandbox
environment](https://docs.unity3d.com/Packages/com.unity.purchasing.udp@latest/index.html?subfolder=/manual/building-
your-game.html%23testing).

## Premium Games

You can distribute Premium games (aka pay-to-download games) via UDP to stores
which support premium games. You can then view your premium game revenue in
the UDP console’s [Reporting dashboard](udp-reference.html#reporting).

Learn how to distribute your premium game via UDP.

## Ownership

UDP games belong to a [Unity
Organization](https://docs.unity3d.com/Manual/OrgsManagingyourOrganization.html)
and not to any individual user. All users of an Organization have access to
its UDP games. Permissions vary depending on the role of a given user within
the Organization.

You can also add users who aren’t in the Organization to specific projects.
Add users in the Unity Dashboard under **Project** > **Settings** > **Users**.

You can divide tasks within a Unity Organization between users and non-users
of the Unity Editor; for example:

  * **Publishing Manager** (not an Editor user) 
    * Creates a new game on the UDP console
    * Passes **Developer** the parameters needed to carry out the UDP implementation
    * Consolidates the material required for distribution
    * Begins signing up with the stores the Organization wants to distribute its games to
  * **Developer** (Editor user) 
    * Implements UDP in the project
    * Builds and tests the game’s **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) or AAB

    * Deploys the game build to the UDP console
  * **Publishing Manager**
    * Creates game releases
    * Finalizes the submissions to the stores

### Project-related permissions

Members of an organization and individuals granted access to a project can
both work on Unity projects.

Project-related permissions relate to what UDP features you have access to on
a specific Unity project, both in the Unity Editor and in the UDP console.
This applies to:

  * Members of the organization that the project belongs to (with organization-level permissions)
  * Individuals granted access to the project only (with project-level permissions)

The table below lists the project-related UDP permissions for Users, Managers
and Owners in the Unity Editor. These are the same for both project-level and
organization-level permissions.

| User | Manager | Owner  
---|---|---|---  
Generate a new UDP client | Yes | Yes | Yes  
Link a Unity project to the UDP client | Yes | Yes | Yes  
Modify UDP settings | Yes | Yes | Yes  
Create or modify IAPs | Yes | Yes | Yes  
  
The table below lists the project-related UDP permissions for Users, Managers
and Owners in the UDP console. These are the same for both project-level and
organization-level permissions.

| User | Manager | Owner  
---|---|---|---  
Generate a new UDP client | Yes | Yes | Yes  
Archive a game in game list | No | Yes | Yes  
Delete a game in game list | No | Yes | Yes  
Edit a game revision | Yes | Yes | Yes  
Link a Unity project with a UDP client | Yes | Yes | Yes  
Unlink a Unity project from a UDP client | No | Yes | Yes  
Release a game revision | No | Yes | Yes  
Register a game to a store | No | Yes | Yes  
Publish a game to a store | No | Yes | Yes  
Advanced page operation | No | Yes | Yes  
Status page access and operation | No | Yes | Yes  
Generate an authentication token | No | Yes | Yes  
  
### Organization-related permissions

Organization-related permissions relate to what UDP features you have access
to in the Organization. These features are generally restricted to
Organization members only, that is, individuals granted access only to
specific projects do not have organization-level permissions. The exceptions
to this are:

  * the project Owner can view the Reporting dashboard
  * any project role can view the projects they have access to in the game list

The table below lists additional Organization-related permissions for Users,
Managers and Owners.

| Project-level | Org-level  
---|---|---  
| User | Manager | Owner | User | Manager | Owner  
View the Reporting dashboard | No | No | Yes | No | Yes | Yes  
Access the game list | Yes* | Yes* | Yes* | Yes | Yes | Yes  
Edit the Company profile | No | No | No | No | Yes | Yes  
Sign up the Organization to a store | No | Yes | Yes | No | Yes | Yes  
  
**Note** : Project-level users can assess the games within the host
organization that owns the project, and any other projects they have access to
within their own Organizations.

[](UnityIAPModuleExtension.html)

Store Extensions

[](udp-getting-started.html)

Getting started with UDP

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

