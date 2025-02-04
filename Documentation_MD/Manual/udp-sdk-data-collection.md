[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-sdk-data-collection.html)
  * [中文](/cn/current/Manual/udp-sdk-data-collection.html)
  * [日本語](/ja/current/Manual/udp-sdk-data-collection.html)
  * [한국어](/kr/current/Manual/udp-sdk-data-collection.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-sdk-data-collection.html)
  * [中文](/cn/current/Manual/udp-sdk-data-collection.html)
  * [日本語](/ja/current/Manual/udp-sdk-data-collection.html)
  * [한국어](/kr/current/Manual/udp-sdk-data-collection.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * [UDP reference](udp-reference.html)
  * UDP SDK data collection

[](udp-api.html)

UDP API

[](udp-troubleshooting.html)

UDP troubleshooting

# UDP SDK data collection

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
For various app stores, app publishers must define what data their apps
collect, including the data collected by integrated third-party SDKs such as
UDP. For your convenience, UDP provides information on its data collection
practices below.

**Important** : The data disclosures below are for the UDP SDK only. You are
also responsible for providing any additional disclosures for your app,
including other third-party SDKs used in your app.

**Contact info data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Name**  
For example, first or last name. | No | Not applicable | Not applicable  
**Email Address**  
Including, but not limited to a hashed email address. | No | Not applicable | Not applicable  
**Phone Number**  
Including, but not limited to a hashed phone number. | No | Not applicable | Not applicable  
**Physical Address**  
Such as home address, physical address, or mailing address. | No | Not applicable | Not applicable  
**Other User Contact Info**  
Any other information that can be used to contact the user outside the app. | No | Not applicable | Not applicable  
**Health and Fitness data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Health**  
Health and medical data, including but not limited to from the Clinical Health Records API, HealthKit API, MovementDisorderAPIs, or health-related human subject research or any other user-provided health or medical data. | No | Not applicable | Not applicable  
**Fitness**  
Fitness and exercise data, including but not limited to the Motion and Fitness API. | No | Not applicable | Not applicable  
**Financial data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Payment Info**  
Such as form of payment, payment card number, or bank account number. | No | Not applicable | Not applicable  
**Credit Info**  
Such as a credit score. | No | Not applicable | Not applicable  
**Other Financial Info**  
Such as salary, income, assets, debts, or any other financial information. | No | Not applicable | Not applicable  
**Location data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Precise Location**  
Information that describes the location of a user or device with the same or greater resolution as a latitude and longitude with three or more decimal places. | No | Not applicable | Not applicable  
**Coarse Location**  
Information that describes the location of a user or device with lower resolution than a latitude and longitude with three or more decimal places, such as approximate location services. | Yes | Not applicable | Analytics  
**Note** : For example, Unity collects country-level information for
analytics.  
**Sensitive data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Sensitive Info**  
Such as racial or ethnic data, sexual orientation, pregnancy or childbirth information, disability, religious or philosophical beliefs, trade union membership, political opinion, genetic information, or biometric data. | No | Not applicable | Not applicable  
**Contact data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Contacts**  
Such as a list of contacts in the user’s phone, address book, or social graph. | No | Not applicable | Not applicable  
**User content** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Emails or Text Messages**  
Including subject line, sender, recipients, and contents of the email or message. | No | Not applicable | Not applicable  
**Photos or Videos**  
The user’s photos or videos. | No | Not applicable | Not applicable  
**Audio Data**  
The user’s voice or sound recordings. | No | Not applicable | Not applicable  
**Customer Support**  
Data generated by the user during a customer support request. | No | Not applicable | Not applicable.  
(Players do not make CS requests to UDP)  
**Other User Content**  
Any other user-generated content. | No | Not applicable | Not applicable  
**Browsing data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Browsing History**  
Information about the content the user has viewed that is not part of the app, such as websites. | No | Not applicable | Not applicable  
**Search data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Search History**  
Information about searches performed in the app. | No | Not applicable | Not applicable  
**Identifier data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**User ID**  
Such as screen name, handle, account ID, assigned user ID, customer number, or other user- or account-level ID that can be used to identify a particular user or account. | Yes (depends on which store the game is repacked for) | Linked to user | App Functionality  
For certain UDP stores, UDP will collect the User ID (returned by login method
of the store’s SDK) and keep it for further App Functionality. For other
stores the login method is not required and UDP doesn’t collect such data.  
**Device ID**  
Such as the device’s advertising identifier, or other device-level ID. | Yes | Linked to user | Analytics  
**Purchase data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Purchase History**  
An account’s or individual’s purchases or purchase tendencies. | Yes | Linked to user | Tracking and analytics  
**Note** : For example, Unity collects in-app purchase information to verify
purchases. But does not use it to analyze any specific user’s purchase
tendencies  
**Usage data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Product Interaction**  
Such as app launches, taps, clicks, scrolling information, music listening data, video views, saved place in a game, video, or song, or other information about how the user interacts with the app. | Yes | Not applicable | Analytics  
**Advertising Data**  
Such as information about the advertisements the user has seen. | No | Not applicable | Not applicable  
**Other Usage Data**  
Any other data about user activity in the app. | No | Not applicable | Not applicable  
**Diagnostic data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Crash Data**  
Such as crash logs. | No | Not applicable | Not applicable  
**Performance Data**  
Such as launch time, hang rate, or energy use. | No | Not applicable | Not applicable  
**Other Diagnostic Data**  
Any other data collected for the purposes of measuring technical diagnostics related to the app. | No | Not applicable | Not applicable  
**Other data** | **Collected?** | **Linked to user?** | **Purpose**  
---|---|---|---  
**Other Data Types**  
Any other data types not mentioned. | Yes | Not applicable | Analytics  
**Note** : For example, Unity collects data like device language, make, model,
screen size, and connection type, to be able to understand the overall
distribution of devices within a store channel  
  
[](udp-api.html)

UDP API

[](udp-troubleshooting.html)

UDP troubleshooting

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

