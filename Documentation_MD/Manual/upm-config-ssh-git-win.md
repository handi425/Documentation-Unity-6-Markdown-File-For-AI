[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-config-ssh-git-win.html)
  * [中文](/cn/current/Manual/upm-config-ssh-git-win.html)
  * [日本語](/ja/current/Manual/upm-config-ssh-git-win.html)
  * [한국어](/kr/current/Manual/upm-config-ssh-git-win.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-config-ssh-git-win.html)
  * [中文](/cn/current/Manual/upm-config-ssh-git-win.html)
  * [日本語](/ja/current/Manual/upm-config-ssh-git-win.html)
  * [한국어](/kr/current/Manual/upm-config-ssh-git-win.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Configuration](upm-config.html)
  * [Using passphrase-protected SSH keys with SSH Git URLs](upm-config-ssh-git.html)
  * Loading SSH keys automatically on Windows (OpenSSH)

[](upm-config-ssh-git.html)

Using passphrase-protected SSH keys with SSH Git URLs

[](upm-config-ssh-git-putty.html)

Loading SSH keys automatically on Windows (PuTTY)

# Loading SSH keys automatically on Windows (OpenSSH)

If you use Windows and its built-in OpenSSH client, follow these steps to
configure the OpenSSH client so you can use your passphrase-protected SSH key
without prompts.

## Prerequisites

  * Windows 10 or later.

## Before you begin

Check if you have any existing SSH keys. Refer to the GitHub Docs article,
[Checking for existing SSH keys](https://docs.github.com/en/enterprise-
server@3.8/authentication/connecting-to-github-with-ssh/checking-for-existing-
ssh-keys).

If you don’t have an SSH key:

  1. Create one by following the GitHub Docs article, [Generating a new SSH key](https://docs.github.com/en/enterprise-server@3.8/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
  2. Add the new SSH key to your GitHub account, by following the GitHub Docs article, [Adding a new SSH key to your GitHub account](https://docs.github.com/en/enterprise-server@3.8/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

## Procedure

  1. Check if `C:\Users\<YourUserName>\.ssh\config` exists. **Note** : In some applications, such as Git Bash, `.ssh` is a hidden subdirectory.

  2. Create `C:\Users\<YourUserName>\.ssh\config` if it doesn’t exist.

  3. Add the following content to `C:\Users\<YourUserName>\.ssh\config` to set the key to load in the authentication agent and specify its use by the target server. Make sure you add this entry before any global settings marked as `Host *`.
    
        Host SERVER_NAME
        IdentitiesOnly yes
        IdentityFile FILE_PATH
    

     * `SERVER_NAME` is the server that uses the file specified by `IdentityFile`. A sample value is `github.com`.
     * `FILE_PATH` is the fully qualified path to the SSH file you created. A sample value is `C:\Users\<YourUserName>\.ssh\<FILE>`, where `<FILE>` might be `id_rsa`, `id_ecdsa`, `id_ed25519`, or a custom name.

Example:

    
        Host github.com
        IdentitiesOnly yes
        IdentityFile C:/Users/user1/.ssh/id_ed25519
    

  4. Open the Windows PowerShell, making sure you open it by selecting **Run as Administrator**.

  5. Configure the SSH Authentication Agent service so it starts each time you reboot your computer, by running the following command:
    
        Get-Service ssh-agent | Set-Service -StartupType Automatic
    

  6. Start the service, by running the following command:
    
        Start-Service ssh-agent
    

  7. Check that the service is running, by running the following command and confirming that the `Status` value is `Running`:
    
        Get-Service ssh-agent
    

  8. Load your key file into the `ssh-agent`, replacing `<FILE>` with the actual file name of your key, then type your passphrase, if prompted.
    
        ssh-add $env:USERPROFILE\.ssh\<FILE>
    

Example:

    
        ssh-add $env:USERPROFILE\.ssh\id_ed25519
    

  9. Make sure Git uses the Windows OpenSSH client instead of the SSH client included with Git, by using either of the following methods:

     * For system-wide configuration, create an environment variable named `GIT_SSH_COMMAND` with a value of `C:/Windows/System32/OpenSSH/ssh.exe`. **Important** : Make sure you use forward slashes in the path.

     * To set the configuration for a specific scope, run the following `git config` command in a terminal. Refer to the [git config documentation](https://git-scm.com/docs/git-config) for details. For example:
        
                git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe
        

**Important** : Make sure you use forward slashes in the path.

You can now use the Unity Package Manager to fetch packages from that Git
repository over SSH using your passphrase-protected SSH key.

## Additional resources

  * [Loading SSH keys and passphrases automatically on Windows (PuTTY)](upm-config-ssh-git-putty.html)
  * [Using passphrase-protected SSH keys with SSH Git URLs](upm-config-ssh-git.html)

[](upm-config-ssh-git.html)

Using passphrase-protected SSH keys with SSH Git URLs

[](upm-config-ssh-git-putty.html)

Loading SSH keys automatically on Windows (PuTTY)

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

