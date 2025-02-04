[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-config.html)
  * [中文](/cn/current/Manual/upm-config.html)
  * [日本語](/ja/current/Manual/upm-config.html)
  * [한국어](/kr/current/Manual/upm-config.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-config.html)
  * [中文](/cn/current/Manual/upm-config.html)
  * [日本語](/ja/current/Manual/upm-config.html)
  * [한국어](/kr/current/Manual/upm-config.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * Configuration

[](upm-cache.html)

Global cache

[](upm-config-network.html)

Solving network issues

# Configuration

This section shows you how to configure the following for the Package Manager:

  * [Network configuration](upm-config-network.html): get around a firewall and set up a proxy server.
  * [Scoped registry authentication](upm-config-scoped.html): create and provide Package Manager with an authentication token for any scoped package registry servers that require it.
  * [Customize the global cache](upm-config-cache.html): override the location of the global cache folders and the maximum size of the registry data cache.
  * [Customize the asset package cache location](upm-config-cache-as.html): override the location of the **asset package** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage) cache folder.

  * [Using private repositories with HTTPS Git URLs](upm-config-https-git.html): use a Git credential helper to access private repositories over HTTPS.
  * [Using passphrase-protected SSH keys with SSH Git URLs](upm-config-ssh-git.html): use an authentication agent to access private repositories over SSH.

In addition, you can find the location of the Package Manager configuration
files under Configuration files.

## Configuration files

Package Manager supports two configuration files: a global configuration file
and a user configuration file. Both of these files use the
[TOML](https://en.wikipedia.org/wiki/TOML) format and they appear in different
locations:

  * **Global** configuration files apply to all users on the machine. For example, you can define additional [SSL certificate authorities](upm-config-network.html#SSL) when setting up a proxy server for the entire machine.
  * **User** configuration files apply to a single user. For example, you can set up [authentication tokens](upm-config-scoped.html) to use for custom package registry servers that you access with scoped registries. These tokens authenticate a specific user account.

### Global configuration file location

Package Manager uses a global configuration file named `upmconfig.toml`. This
file isn’t created when you install the Unity Hub or Editor, but you can
create it in the following location if you need to customize your
configuration:

**Environment:** | **Location:**  
---|---  
Windows |  `%ALLUSERSPROFILE%\Unity\config\upmconfig.toml` (for example, `C:\ProgramData\Unity\config\upmconfig.toml`)  
macOS and Linux | `/etc/upmconfig.toml`  
  
You can define a custom location that overrides the default location for your
configuration file. To do this, create a `UPM_GLOBAL_CONFIG_FILE` environment
variable and set its value to the absolute path of your configuration file,
including the file name.

### User configuration file location

Package Manager uses a user configuration file named `.upmconfig.toml`. This
file isn’t created when you install the Unity Hub or Editor, but you can
create it in the following location if you need to customize your
configuration:

**Environment:** | **Location:**  
---|---  
Windows (user account) |  `%USERPROFILE%\.upmconfig.toml` (for example, `C:\Users\myusername\.upmconfig.toml`)  
Windows ([system user account](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts#default-local-system-accounts)) |  `%ALLUSERSPROFILE%\Unity\config\ServiceAccounts\.upmconfig.toml` (for example, `C:\Users\Public\Unity\config\ServiceAccounts\.upmconfig.toml`)  
macOS and Linux |  `~/.upmconfig.toml` (for example, `/Users/myusername/.upmconfig.toml`)  
  
You can define a custom location that overrides the default location for your
configuration file. To do this, create a `UPM_USER_CONFIG_FILE` environment
variable and set its value to the absolute path of your configuration file,
including the file name.

[](upm-cache.html)

Global cache

[](upm-config-network.html)

Solving network issues

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

