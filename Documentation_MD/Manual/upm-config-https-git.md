[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-config-https-git.html)
  * [中文](/cn/current/Manual/upm-config-https-git.html)
  * [日本語](/ja/current/Manual/upm-config-https-git.html)
  * [한국어](/kr/current/Manual/upm-config-https-git.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-config-https-git.html)
  * [中文](/cn/current/Manual/upm-config-https-git.html)
  * [日本語](/ja/current/Manual/upm-config-https-git.html)
  * [한국어](/kr/current/Manual/upm-config-https-git.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Configuration](upm-config.html)
  * Using private repositories with HTTPS Git URLs

[](upm-config-cache-as.html)

Customize the asset package cache location

[](upm-config-ssh-git.html)

Using passphrase-protected SSH keys with SSH Git URLs

# Using private repositories with HTTPS Git URLs

When you use Git in a terminal to access a private repository over HTTPS, Git
prompts you to enter a username and password. Then, Git submits these
credentials to the server and proceeds with the command if the server accepts
those credentials and allows access to the repository.

When the Unity Package Manager fetches packages using Git URLs, there’s no
terminal for users to enter credentials. As a result, when the server requests
credentials from Git, Git doesn’t issue a prompt. Instead, it reports an error
to the Unity Package Manager. To solve this problem, you must configure Git
with a Git credential helper, and that helper must already have the required
credentials loaded for that repository. If the credentials are valid, Git can
successfully run the commands issued by the Unity Package Manager.

**Note** : A Git credential helper has no effect when using Git URLs with the
SSH protocol, including the SCP-like syntax. For information about accessing a
private Git repository over SSH, refer to [Using passphrase-protected SSH keys
with SSH Git URLs](upm-config-ssh-git.html).

## Git Credential Manager

Although Git supports several [credential helpers to store
credentials](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage), the
[Git Credential Manager](https://github.com/git-ecosystem/git-credential-
manager) (GCM) is the recommended credential helper. GCM is flexible, easy to
install, and is actively supported. It’s built on .NET, which means it can run
on Windows, macOS, and Linux distributions that support .NET.

By default, GCM uses Windows Credential Manager (on Windows) and macOS
Keychain (on macOS) as the configured credential store. GCM doesn’t have a
default store configured for Linux. Refer to the [GCM credential stores
documentation](https://github.com/git-ecosystem/git-credential-
manager/blob/release/docs/credstores.md) for more information on the different
credential store configurations supported by GCM.

## Prerequisites

Before you can fetch packages from private Git repositories using HTTPS URLs,
make sure you install GCM.

The [Git for Windows](https://gitforwindows.org/) installer includes a step to
install and configure GCM automatically. You can also install GCM separately
if you:

  * Used a different method to install Git on Windows.
  * Use macOS or Linux.

Refer to the [GCM install instructions](https://github.com/git-ecosystem/git-
credential-manager/blob/release/docs/install.md) for more information about
installing GCM.

## Procedure

Follow these steps to access packages in private repositories that use HTTPS
Git URLs:

  1. Configure Git to use GCM by running the following command in a terminal:
    
        git config --global credential.helper manager
    

  2. Access the repository one time by using a terminal. For example, run the following command:
    
        git ls-remote --heads https://<url-to-repository> HEAD
    

  3. When Git prompts you, enter your credentials. If your user account has access to the remote Git server and the server accepts your credentials, then the Git credential helper will securely store your credentials.

  4. Use the Unity Package Manager. It will use your stored credentials, when necessary, to fetch packages from HTTPS-based repositories that you have permissions to access.

## Additional resources

  * [Troubleshooting Git issues](upm-errors.html#git-not-found)
  * [Using passphrase-protected SSH keys with SSH Git URLs](upm-config-ssh-git.html)

[](upm-config-cache-as.html)

Customize the asset package cache location

[](upm-config-ssh-git.html)

Using passphrase-protected SSH keys with SSH Git URLs

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

