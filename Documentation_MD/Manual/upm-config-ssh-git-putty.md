[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-config-ssh-git-putty.html)
  * [中文](/cn/current/Manual/upm-config-ssh-git-putty.html)
  * [日本語](/ja/current/Manual/upm-config-ssh-git-putty.html)
  * [한국어](/kr/current/Manual/upm-config-ssh-git-putty.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-config-ssh-git-putty.html)
  * [中文](/cn/current/Manual/upm-config-ssh-git-putty.html)
  * [日本語](/ja/current/Manual/upm-config-ssh-git-putty.html)
  * [한국어](/kr/current/Manual/upm-config-ssh-git-putty.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Configuration](upm-config.html)
  * [Using passphrase-protected SSH keys with SSH Git URLs](upm-config-ssh-git.html)
  * Loading SSH keys automatically on Windows (PuTTY)

[](upm-config-ssh-git-win.html)

Loading SSH keys automatically on Windows (OpenSSH)

[](upm-config-ssh-git-mac.html)

Loading SSH keys automatically on macOS

# Loading SSH keys automatically on Windows (PuTTY)

Follow these steps if you use PuTTY and its authentication agent (Pageant)
instead of Windows’ built-in OpenSSH client. For example, if you use
SourceTree as your Git client, it comes with PuTTY (and Pageant) to use
instead of OpenSSH.

## Before you begin

Make sure you’ve installed the PuTTY suite, which includes Pageant. If it’s
not installed, its download link is available at <https://www.putty.org/>.

Check if you have any existing SSH keys. Refer to the GitHub Docs article,
[Checking for existing SSH keys](https://docs.github.com/en/enterprise-
server@3.8/authentication/connecting-to-github-with-ssh/checking-for-existing-
ssh-keys).

If you don’t have an SSH key:

  1. Use the **PuTTYgen** application to generate a private/public key pair, saving it as private key. Refer to [Using PuTTYgen, the PuTTY key generator](https://the.earth.li/~sgtatham/putty/0.78/htmldoc/Chapter8.html#pubkey-puttygen) in the PuTTY User Manual.
  2. Add the new SSH key to your GitHub account, by following the GitHub Docs article, [Adding a new SSH key to your GitHub account](https://docs.github.com/en/enterprise-server@3.8/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

## Procedure

Follow these steps to load keys and passphrases automatically on Windows:

  1. Start Pageant from the PuTTY folder: **Start-Menu** > **All Programs** > **PuTTY** > **Pageant**
  2. Find the Pageant icon in the system tray. ![](../uploads/Main/upm-pageant.png)
  3. Right-click the Pageant icon in the system tray and select **View Keys**. The **Pageant Key List** window opens.
  4. Click **Add Key**.
  5. Use the **File Explorer** window to select your SSH key file to load. Make sure you select a file with a `.ppk` extension, then click **Open**.
  6. If the key is passphrase-protected, enter your passphrase.
  7. Make sure the key you selected is now listed in the **Pageant Key List** window. This key is now available to connect to any server during your PuTTY sessions.

You might have configured Git already to use PuTTY’s `plink.exe` program. To
check if Git uses Pageant when using SSH keys:

  1. Check if you have a `GIT_SSH_COMMAND` environment variable. If not, create it.
  2. Set its value to the fully qualified path of PuTTY’s `plink.exe` file. By default, this location is `"C:\Program Files\PuTTY\plink.exe"`. **Important** : If the path includes spaces, make sure you enclose the value in quotation marks.

To load private keys automatically on Startup:

  1. Open the Start Menu and right-click **Pageant**.

  2. Select **More** > **Open file location**. A **File Explorer** window opens.

  3. Right-click **Pageant** and select **Properties**. The **Pageant Properties** window opens.

  4. Update the **Target** field by appending the full paths of the private keys you want to load on startup. Separate each key with a space. Example:
    
          "C:\Program Files\PuTTY\pageant.exe" "C:\Users\user1\myKeys\privatekey.ppk"
    

  5. Select **Apply** then select **OK**. 

  6. Test your configuration by opening a command line and running a `git` command in your repository, to make sure you can complete the operation without prompts for your passphrase.

When Pageant is running and you enter your passphrase, you can use the Unity
Package Manager to fetch packages from that Git repository over SSH using your
passphrase-protected SSH key.

The next time Pageant starts, it prompts you for the passphrase, if it’s
passphrase-protected.

To load Pageant automatically when Windows starts, refer to the Microsoft
Support article, [Add an app to run automatically at startup in Windows
10](https://support.microsoft.com/en-us/windows/add-an-app-to-run-
automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd).

## Additional resources

  * [Loading SSH keys automatically on Windows (OpenSSH)](upm-config-ssh-git-win.html)
  * [Using passphrase-protected SSH keys with SSH Git URLs](upm-config-ssh-git.html)
  * [PuTTY User Manual](https://the.earth.li/~sgtatham/putty/0.78/htmldoc/index.html)

[](upm-config-ssh-git-win.html)

Loading SSH keys automatically on Windows (OpenSSH)

[](upm-config-ssh-git-mac.html)

Loading SSH keys automatically on macOS

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

