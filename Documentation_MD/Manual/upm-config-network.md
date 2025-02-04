[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-config-network.html)
  * [中文](/cn/current/Manual/upm-config-network.html)
  * [日本語](/ja/current/Manual/upm-config-network.html)
  * [한국어](/kr/current/Manual/upm-config-network.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-config-network.html)
  * [中文](/cn/current/Manual/upm-config-network.html)
  * [日本語](/ja/current/Manual/upm-config-network.html)
  * [한국어](/kr/current/Manual/upm-config-network.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Configuration](upm-config.html)
  * Solving network issues

[](upm-config.html)

Configuration

[](upm-config-scoped.html)

Scoped registry authentication

# Solving network issues

Use these procedures to:

  * Configure your firewall settings so that Unity has access to the Package Manager registry server.
  * Configure your proxy server, either by setting environment variables or adding custom certificate authority (CA) certificates.

## Configuring your firewall

To ensure that the Unity Package Manager can access the domains it uses, you
must add the domains to your firewall’s safe list.

For a complete list of these domains, and all domains that the Unity Editor
requires, refer to [Endpoints that Unity applications access](ent-proxy-
exception-list.html#endpoints-unity). You can either use the list to add
entire domains, or use the table to selectively add subdomains.

Refer to your operating system’s help to learn how to add a domain name to the
firewall’s safe list.

## Configuring your proxy server

When using a proxy server, configure the `HTTP_PROXY` and `HTTPS_PROXY`
environment variables for the Unity Package Manager to use when performing
requests against the Unity package registry. For more information, refer to
[Use environment variables to identify your proxy server](ent-proxy-env-
vars.html).

You can set these variables globally (either system or user variables)
according to your operating system. Alternatively, you can [create a command
file to set these environment variables and launch the Hub](ent-proxy-cmd-
file.html).

For environments where you are behind a proxy server using a certificate that
Package Manager doesn’t recognize, you can configure a custom certificate
authority.

### Custom certificate authority

In some organizations, users can only access the internet through a proxy
server. Some proxies unpack the HTTPS content and repack it with their own SSL
certificate. Unity Package Manager’s underlying HTTPS layer sometimes rejects
these certificates because it doesn’t recognize the certificate authority that
emitted them. When this happens, the Package Manager treats the connection as
a possible machine-in-the-middle attack (MITM). This means that you can’t use
many features in Unity, including the Package Manager, unless you configure
additional SSL certificate authorities to allow these certificates.

To configure additional SSL certificate authorities:

  1. Locate the [`upmconfig.toml` global configuration file](upm-config.html#upmconfig). If the file doesn’t already exist, create an empty text file.

  2. Create a text file with one or more certificates for custom certificate authorities. The file must consist of one or more trusted certificates in the Privacy-Enhanced Mail (PEM) format. For example:
    
        -----BEGIN CERTIFICATE-----
    MIIC+zCCAeOgAwIBAgIJAO0U6hVJnbvjMA0GCSqGSIb3DQEBBQUAMBQxEjAQBgNV
    BAMMCWxvY2FsaG9zdDAeFw0xOTAzMTIwMTIxMzRaFw0yOTAzMDkwMTIxMzRaMBQx
    (additional lines omitted for conciseness)
    LFwHSUdqk0lJK4b0mCwyTHNvYO1IDziE5EKwfuaKVgOa62iCHVahgIVa+een4EfS
    hCCr3M3cq11Mi+mnRi1scxxrOno4OEEChWg2szZLlxBrkVJllrrq620XJ6RLB/8=
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    MIIDtzCCAp+gAwIBAgIQDOfg5RfYRv6P5WD8G/AwOTANBgkqhkiG9w0BAQUFADBl
    MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
    (additional lines omitted for conciseness)
    H2sMNgcWfzd8qVttevESRmCD1ycEvkvOl77DZypoEd+A5wwzZr8TDRRu838fYxAe
    +o0bJW1sj6W3YQGx0qMmoRBxna3iw/nDmVG3KwcIzi7mULKn+gpFL6Lw8g==
    -----END CERTIFICATE-----
    

  3. Save this file to the same folder as the global configuration file if possible, although Unity supports any location on the file system.

  4. In the global configuration file, add the **caFile** key and set its value as an absolute file path to your PEM file. **Important** : When setting Windows paths in TOML files, use forward slashes (`/`) or double backslashes (`\\`). Don’t use single backslashes (`\`) because they’re special characters which mark escape sequences and can cause TOML parsing errors.

**Windows example**

    
        caFile = "C:\\ProgramData\\Unity\\config\\cert.pem"
    

**macOS and Linux example**

    
        caFile = "/etc/cert.pem"
    

## Additional resources

  * [Using Unity through web proxies](ent-proxy-autoconfig.html)

[](upm-config.html)

Configuration

[](upm-config-scoped.html)

Scoped registry authentication

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

