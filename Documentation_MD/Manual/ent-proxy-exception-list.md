[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ent-proxy-exception-list.html)
  * [中文](/cn/current/Manual/ent-proxy-exception-list.html)
  * [日本語](/ja/current/Manual/ent-proxy-exception-list.html)
  * [한국어](/kr/current/Manual/ent-proxy-exception-list.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ent-proxy-exception-list.html)
  * [中文](/cn/current/Manual/ent-proxy-exception-list.html)
  * [日本語](/ja/current/Manual/ent-proxy-exception-list.html)
  * [한국어](/kr/current/Manual/ent-proxy-exception-list.html)

  * [Install and upgrade](install-and-upgrade.html)
  * [Deploy Unity across your enterprise](ent-deployment.html)
  * [Use Unity through web proxies](ent-proxy-autoconfig.html)
  * Define exceptions on your web proxy

[](ent-proxy-cmd-file.html)

Create a command file to set environment variables and open applications

[](LicensesAndActivation.html)

Licenses and activation

# Define exceptions on your web proxy

One of the uses for a web proxy is to filter and block certain websites.
However, there are situations where an administrator needs to allow certain
websites or URLs through the web proxy without authentication.

Administrators define these exceptions in an exception list, which identifies
approved or allowed websites that users can access through the web proxy.

Unity users in your environment need access to several URLs, and an exception
list enables them to access those resources in the following scenarios:

  * Your environment supports automatic proxy configuration but it doesn’t support basic authentication. Refer to Endpoints that Unity applications access to allow Unity applications to communicate through the web proxy without authentication.
  * Your web proxy uses SSL inspection and you’re unable to make Unity applications trust the web proxy certificates. Refer to Endpoints that Unity applications access to allow Unity applications to communicate through the web proxy without SSL inspection.
  * Your web proxy prevents downloading of executable files, or requires user confirmation before downloading executable files. Refer to Endpoints that download executable files to allow Unity applications to download executable files without user confirmation.

Define your exception list so you can bypass any or all of these situations.

The process of adding exceptions varies depending on your proxy software, but
you can typically do it in the web proxy configuration settings or through a
web-based management interface. Refer to the help for your web proxy software
for details.

## Endpoints that Unity applications access

The simplest solution is to add entire domains for the following resources in
your exception list:

  * `unity.com`
  * `unity3d.com`
  * `plasticscm.com`
  * `google.com`
  * `googleapis.com`
  * `microsoft.com`
  * `aka.ms`

If you want to selectively control which subdomains users can access, add
items from the following table to your exception list. **Notes** :

  * Unless specified otherwise, the protocol type for these endpoints is `TCP`, and the port numbers are `80` and `443`.
  * This table was last updated on July 10, 2024. Refer to changelog.

Endpoint or URL | Feature or service that uses the endpoint | Additional information  
---|---|---  
live-platform-api.prd.ld.unity3d.com | Unity Hub | API for retrieving Hub content, such as Unity Releases, Templates, Learn content, and more.  
api.hub-proxy.unity3d.com  
core.hub-proxy.unity3d.com  
config.hub-proxy.unity3d.com | Unity Hub | Proxies for various services that manage data.  
config.uca.cloud.unity3d.com | Unity Hub | Opt-in status for analytics, by using remote configuration.  
learn.unity.com | Unity Hub | Hub links to Unity Learn content on the internet. Required only if users want to access training content from within in the Hub.  
aka.ms | Unity Hub | Download address for Visual Studio Tools for Unity.  
analytics.cloud.unity3d.com | Unity Hub |   
api2.amplitude.com | Unity Hub | Analytics for Unity Hub.  
id.unity.com | Unity ID portal | Portal to manage your Unity ID, seat-based subscriptions, organizations, and more.  
api.unity.com | Identity | API for identity and authentication.  
accounts.unity3d.com | Web authentication |   
license.unity3d.com | License | API for license operations including activation, update, and return.  
activation.unity3d.com | Activation | API for license operations including activation.  
packages.unity.com | Unity Package Registry | Main registry service endpoints for searching packages and retrieving package information.  
download.packages.unity.com | Unity Package Registry | Alias for packages.unity.com  
packages-v2.unity.com | Unity Package Registry | Previously used by Asset Store integration in the Package Manager. Alias for packages.unity.com.  
cdn.packages.unity.com | Unity Package Files | Geo-localized content delivery network to download publicly available Unity packages.  
upm-cdn-china.unitychina.cn | Unity Package Files | Content delivery network to download Unity packages from locations in China.  
private.download.packages.unity.com | Unity Package Files | Signed URLs provided by requests for packages that are available only with entitlements.  
storage.googleapis.com | Unity Package Files | Signed URLs provided by requests for packages that are available only with entitlements.  
assetstore.unity.com | Unity Asset Store | Core URL for Unity Asset Store.  
kharma.unity3d.com | Unity Asset Store | Endpoints for Asset Store operations.  
core.cloud.unity3d.com | Core Cloud services |   
developer.cloud.unity3d.com | Unity Gaming Services | Dashboard for Unity Gaming Services.  
perf.cloud.unity3d.com | Performance | Service for performance and crash reporting.  
perf-events.cloud.unity3d.com | Performance events |   
euwest4–00-cloud.plasticscm.com | PlasticSCM | Unity DevOps for Western Europe.  
useast4–00-cloud.plasticscm.com | PlasticSCM | Unity DevOps for Eastern United States.  
asiaeast1–00-cloud.plasticscm.com | PlasticSCM | Unity DevOps for East Asia.  
asianortheast1–00-cloud.plasticscm.com | PlasticSCM | Unity DevOps for Northeast Asia.  
cdp.cloud.unity3d.com | Analytics | Common Data Platform for collecting data for analytics.  
prd-lender.cdp.internal.unity3d.com | Analytics | Relays data to Unity for internal analytics.  
google-analytics.com | Google Analytics |   
dashboard.unityads.unity3d.com | Ads Dashboard | Dashboard for ads and monetization.  
**Important** : Proceed to [Endpoints that download executable files](ent-
proxy-exception-list.html#endpoints-exe) and add the URLs from that list.  
  
## Endpoints that download executable files

Even if you don’t need to add exceptions from the earlier table based on your
environment, add exceptions to your web proxy if either of the following
conditions are true:

  * Your web proxy prevents downloading of executable files.
  * Your web proxy requires user confirmation before downloading executable files.

Without adding these exceptions, any operations that require Unity
applications to download executable files will fail.

Endpoint or URL | Executable files downloaded | Additional information  
---|---|---  
public-cdn.cloud.unity3d.com | Unity Hub | Content delivery network to store configurations, such as automatic update, and binaries like the Hub installers.  
download.unity3d.com | Unity Editor installers | Downloaded while using the Unity Hub.  
dl.google.com | Unity Hub | Enables Unity Hub to download Android modules.  
go.microsoft.com | Unity Hub | Visual Studio installers by Microsoft.  
  
## Changelog

  * July 10, 2024: Changed the endpoint (URL) value from `upm-cdn.unity.com` to `cdn.packages.unity.com`.

## Additional resources

  * [Using Unity through web proxies](ent-proxy-autoconfig.html)

[](ent-proxy-cmd-file.html)

Create a command file to set environment variables and open applications

[](LicensesAndActivation.html)

Licenses and activation

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

