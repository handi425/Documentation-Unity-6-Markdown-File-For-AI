[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ent-proxy-cert-trust.html)
  * [中文](/cn/current/Manual/ent-proxy-cert-trust.html)
  * [日本語](/ja/current/Manual/ent-proxy-cert-trust.html)
  * [한국어](/kr/current/Manual/ent-proxy-cert-trust.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ent-proxy-cert-trust.html)
  * [中文](/cn/current/Manual/ent-proxy-cert-trust.html)
  * [日本語](/ja/current/Manual/ent-proxy-cert-trust.html)
  * [한국어](/kr/current/Manual/ent-proxy-cert-trust.html)

  * [Install and upgrade](install-and-upgrade.html)
  * [Deploy Unity across your enterprise](ent-deployment.html)
  * [Use Unity through web proxies](ent-proxy-autoconfig.html)
  * Trusting the web proxy security certificate

[](ent-proxy-autoconfig-store-mac.html)

Store credentials for automatic proxy configuration (macOS)

[](ent-proxy-env-vars.html)

Use environment variables to identify your web proxy

# Trusting the web proxy security certificate

Some enterprises use SSL inspection as part of their networking environment,
to inspect, track, and control network traffic.

With SSL inspection, the web proxy acts as the server to the actual client,
and then acts as the client to the actual server. To prevent the client from
seeing a security warning, the web proxy must present a valid SSL/TLS
certificate to the client on behalf of the server. Without a valid SSL/TLS
certificate, the client might not trust the web proxy, and might block or warn
the user that their connection isn’t secure.

SSL inspection is sometimes associated with a machine-in-the-middle (MITM).

It’s assumed that your web proxy that uses SSL inspection is already set up.
It’s also assumed that client computers are configured at the operating system
level to accept the SSL/TLS certificate so they can communicate with the web
proxy.

Even with certificates trusted at the operating system level, client computers
must be configured to:

  * [Enable automatic proxy configuration](ent-proxy-autoconfig-enable.html) to make the Unity Hub trust the certificates.
  * Set the NODE_EXTRA_CA_CERTS environment variable or set a global configuration file to make the Unity Package Manager trust certificates.

As an alternative, you can [define exceptions on your web proxy](ent-proxy-
exception-list.html) so that Unity URLs aren’t subject to SSL inspection.

## Set certificates with the NODE_EXTRA_CA_CERTS environment variable

To enable Unity Package Manager operations with a web proxy that uses SSL
inspection, you must set the `NODE_EXTRA_CA_CERTS` environment variable or set
certificates with a configuration file.

The certificate file must be distributed to each computer running Unity. Then,
the `NODE_EXTRA_CA_CERTS` environment variable must be set so its value points
the absolute path of the certificate file. Whether you do this manually or use
a more scalable method, the certificate and environment variable must be set
on each device that communicates with the web proxy. Follow these general
steps:

  1. Create a text file with one or more certificates for custom certificate authorities. The file must consist of one or more trusted certificates in the Privacy-Enhanced Mail (PEM) format. Refer to the help for your web proxy software for details.
  2. Distribute the `.pem` file to each computer that has an instance of Unity.
  3. Define the `NODE_EXTRA_CA_CERTS` environment variable in a command file. Refer to [Create a command file to set environment variables and open applications](ent-proxy-cmd-file.html).

### Examples

In the following examples, `mycert.pem` is the name of the certificate, and it
exists in the user’s home directory.

#### Windows

    
    
    set NODE_EXTRA_CA_CERTS=C:\Users\username\mycert.pem
    

#### macOS and Linux

    
    
    export NODE_EXTRA_CA_CERTS=/Users/username/mycert.pem
    

You can find more information about the `NODE_EXTRA_CA_CERTS` environment
variable in the [Node.js documentation](https://nodejs.org/api/cli.html).

## Set certificates with a configuration file

Follow this process if you’re unable to set certificates with the
`NODE_EXTRA_CA_CERTS` environment variable to enable Unity Package Manager
operations.

**Note** : Whether you add or update the configuration file manually or by
using a more scalable method, you must apply the addition or update to each
client computer.

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

[](ent-proxy-autoconfig-store-mac.html)

Store credentials for automatic proxy configuration (macOS)

[](ent-proxy-env-vars.html)

Use environment variables to identify your web proxy

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

