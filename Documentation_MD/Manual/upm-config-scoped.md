[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-config-scoped.html)
  * [中文](/cn/current/Manual/upm-config-scoped.html)
  * [日本語](/ja/current/Manual/upm-config-scoped.html)
  * [한국어](/kr/current/Manual/upm-config-scoped.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-config-scoped.html)
  * [中文](/cn/current/Manual/upm-config-scoped.html)
  * [日本語](/ja/current/Manual/upm-config-scoped.html)
  * [한국어](/kr/current/Manual/upm-config-scoped.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Configuration](upm-config.html)
  * Scoped registry authentication

[](upm-config-network.html)

Solving network issues

[](upm-config-cache.html)

Customize the global cache

# Scoped registry authentication

Some organizations host their own packages on private package registries that
require authentication to access. If you are an employee or customer of one of
those organizations, you must configure a scoped registry with npm
authentication. To set this up, get an npm authentication token and then add
that token to your user configuration file.

## 1) Fetch the npm authentication token

The process of creating and accessing an npm authentication token is different
for each registry provider. For example, JFrog’s
[Artifactory](https://www.jfrog.com/confluence/display/JFROG/JFrog+Artifactory)
repository manager uses a different procedure to generate the authentication
token from npm. This is an example of a typical procedure, but you need to
follow the process recommended by the specific package registry provider for
your scoped registry.

To fetch an authentication token from npm:

  1. Install [npm](https://www.npmjs.com/get-npm) locally on your computer.

  2. From a terminal, enter the following command to log in to the registry:

`$ npm login --registry <registry url>`

  3. Locate and open the generated [.npmrc](https://docs.npmjs.com/files/npmrc) file. 

  4. Locate either the `_authToken` or the `_auth` entry and copy its value (refer to the example below).

Depending on the registry, the token string can be either a globally unique
identifier (GUID), a token, or a proprietary-formatted string.

### Examples of .npmrc files

This is an example of an `.npmrc` file containing an `_authToken` attribute:

    
    
    registry=https://example.com:1234/mylocation/
    //example.com:1234/mylocation/:_authToken=<AUTH TOKEN>
    

This is an example of an `.npmrc` file containing an`_auth` attribute:

    
    
    registry=https://example.com:1234/mylocation
    _auth=<AUTH TOKEN>
    email=<EMAIL>
    always-auth=true
    

## 2) Configure authentication information

Store your token information for each scoped registry that requires
authentication in the `.upmconfig.toml` [user configuration file](upm-
config.html#upmconfigUser) using the `npmAuth` configuration schema. After you
save this information to the configuration file, Package Manager will provide
your authentication information on every request made to each registry in the
file.

Follow these instructions to add your authentication information to the user
configuration file:

  1. Locate the `.upmconfig.toml` [user configuration file](upm-config.html#upmconfigUser). If the file doesn’t exist, create an empty text file.

  2. Format your authentication information using a schema, depending on whether you are using a Bearer (token-based) or Basic (Base64-encrypted) authentication mechanism.

    
    
    [npmAuth."<REGISTRY URL>"]
    <TOKEN-PROPERTY> = "<TOKEN-VALUE>"
    email = "<EMAIL>"
    alwaysAuth = <BOOLEAN>
    

The information in the following table explains how to specify the
configuration file values:

**Entry** | **Description**  
---|---  
`[npmAuth."<REGISTRY-URL>"]` | Required. URL for the registry. For example, `[npmAuth."https://example.com:8081/mylocation"]`.  
`<TOKEN-PROPERTY> = "<TOKEN-VALUE>"` | Required. The authentication token generated from the npm registry. This can be a GUID, a token, or a proprietary-formatted string. For example, this can be either `token = "<AUTH TOKEN>"` (Bearer) or `_auth = "<BASE64 TOKEN>"` (Basic).  
**email** | Optional. Email address for the user matching the user’s email on the registry.  
**alwaysAuth** | Optional. Set to `true` if the package metadata and tarballs aren’t located on the same server. Typically, you can copy the value from the .npmrc file you generated.  
  
#### Example using bearer authentication

    
    
    [npmAuth."http://localhost:8081/myrepository/mylocation"]
    token = "NpmToken.2348c7ea-6f86-3dbe-86b6-f257e86569a8"
    alwaysAuth = true
    
    [npmAuth."http://localhost:4873"]
    token = "eaJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsX2dyb3VwcyI6WyJwYXNjYWxsIl0sIm5hbWUiOiJwYXNjYWxsIiwiZ3JvdXBzIjpbIn"
    
    [npmAuth."https://api.bintray.example/npm/mycompany/myregistry"]
    token = "aGFzY2FsbDo4ZWIwNTM5NzBjNTI3OTIwYjQ4MDVkYzY2YWEzNmQxOTkyNDYzZjky"
    email = "username@example.com"
    alwaysAuth = true
    

### Configure basic authentication information

These steps use Azure DevOps as an example, but the process is similar for any
platform that uses a personal access token (PAT).

Before you begin, install Node.js if it’s not already installed.

  1. Get your Azure DevOps personal access token (PAT), and have it ready for a later step. If you need to regenerate your PAT, log in to Azure DevOps (<https://dev.azure.com>) and go to **User settings** > **Personal access tokens**. For information about using PATs, refer to the Microsoft article, [Use personal access tokens](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate).

  2. From a command line, run the following command:
    
        node -e "require('readline').createInterface({input:process.stdin,output:process.stdout,historySize:0}).question('Enter PAT> ',p => {b64=Buffer.from(p.trim()).toString('base64');console.log(b64);process.exit();})"
    

  3. At the `Enter PAT` prompt, type `email:PAT`, replacing:

     * `email` with the email associated with your Azure DevOps account and the email specified in the `.upmconfig.toml` file
     * `PAT` with your PAT from the earlier step
  4. The command returns a Base64-encrypted string. Copy that string and assign it as the value for the `_auth` key in the `.upmconfig.toml` file.

#### Example using basic authentication

    
    
    [npmAuth."http://localhost:8081/myrepository/mylocation"]
    _auth = "c19kaW5pcm9AaG90bWFpbC4jb206d3FzdzVhemU9Q=="
    email = "username@example.com"
    alwaysAuth = true
    

## Additional resources

  * [Scoped registries](upm-scoped.html)

[](upm-config-network.html)

Solving network issues

[](upm-config-cache.html)

Customize the global cache

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

