[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-config-ssh-git.html)
  * [中文](/cn/current/Manual/upm-config-ssh-git.html)
  * [日本語](/ja/current/Manual/upm-config-ssh-git.html)
  * [한국어](/kr/current/Manual/upm-config-ssh-git.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-config-ssh-git.html)
  * [中文](/cn/current/Manual/upm-config-ssh-git.html)
  * [日本語](/ja/current/Manual/upm-config-ssh-git.html)
  * [한국어](/kr/current/Manual/upm-config-ssh-git.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Configuration](upm-config.html)
  * Using passphrase-protected SSH keys with SSH Git URLs

[](upm-config-https-git.html)

Using private repositories with HTTPS Git URLs

[](upm-config-ssh-git-win.html)

Loading SSH keys automatically on Windows (OpenSSH)

# Using passphrase-protected SSH keys with SSH Git URLs

When you use Git to access a private repository over SSH, Git uses an SSH
client to establish a secure connection with the server. While establishing
the connection, Git uses your configured SSH key during the SSH handshaking
phase. During this phase, the SSH client needs to be able to read your key.
However, if you encrypted your key with a passphrase, the SSH client can’t use
the key directly. In this case, you’re prompted to type in the passphrase in
the terminal. After you enter the correct passphrase, the SSH connection
completes and the Git command runs using that connection.

When the Unity Package Manager fetches packages using Git URLs, there’s no
interface for you to enter credentials requested by the SSH client. As a
result, if you protected your SSH key file with a passphrase, the SSH client
fails to establish the connection and Git reports an error. To solve this, an
authentication agent for SSH must be running and loaded with the SSH key, so
that the SSH client can use it without requiring its passphrase.

The method varies, depending on your operating system and the SSH client that
you use:

  * If you use Windows 10 or later and its built-in OpenSSH client, refer to [Loading SSH keys automatically on Windows (OpenSSH)](upm-config-ssh-git-win.html).
  * If you use Windows and PuTTY and its authentication agent (Pageant), refer to [Loading SSH keys automatically on Windows (PuTTY)](upm-config-ssh-git-putty.html).
  * If you use macOS, refer to [Loading SSH keys automatically on macOS](upm-config-ssh-git-mac.html).

## Additional resources

  * [Using private repositories with HTTPS Git URLs](upm-config-https-git.html)
  * [Troubleshooting Git issues](upm-errors.html#git-not-found)

[](upm-config-https-git.html)

Using private repositories with HTTPS Git URLs

[](upm-config-ssh-git-win.html)

Loading SSH keys automatically on Windows (OpenSSH)

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

