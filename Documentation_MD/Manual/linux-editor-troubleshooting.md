[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/linux-editor-troubleshooting.html)
  * [中文](/cn/current/Manual/linux-editor-troubleshooting.html)
  * [日本語](/ja/current/Manual/linux-editor-troubleshooting.html)
  * [한국어](/kr/current/Manual/linux-editor-troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/linux-editor-troubleshooting.html)
  * [中文](/cn/current/Manual/linux-editor-troubleshooting.html)
  * [日本語](/ja/current/Manual/linux-editor-troubleshooting.html)
  * [한국어](/kr/current/Manual/linux-editor-troubleshooting.html)

  * [Platform development ](PlatformSpecific.html)
  * [Linux](linux.html)
  * Troubleshooting the Linux Editor issues

[](build-for-linux.html)

Build a Linux application

[](AppleMac.html)

macOS

# Troubleshooting the Linux Editor issues

This page lists the known issues for the Linux Unity Editor and provides
tested solutions.

## Unity Editor crashes with Pipe error ! message

Opening projects with large number of assets crashes the Editor and logs a
`Pipe error !` message. The error message appears in the terminal if you
opened the Editor via the terminal, otherwise it’s logged in the `Editor.log`
file located in `~/.config/unity3d` directory.

### Cause

The error message is logged when the project reaches the maximum number of
open files limit.

### Solution

Increase the maximum open file limit in the Unity Editor session in one of the
following ways:

  * Increasing the maximum open file limit in the current Editor session
  * Increasing the maximum open file limit system wide

#### Increase the maximum open file limit current Editor session

If you’re using a terminal to open the Editor, then you can increase the
maximum open file limit in the current Editor session by following these
steps:

  1. In the terminal window, check the current maximum open file limit by using following command:
    
        ulimit -a
    

This increases the soft limit of the maximum number of open files and the
value of the soft limit can’t exceed the hard limit.

  2. Check the hard limit to make sure you’re not exceeding the hard limit by using the following command: 
    
        ulimit -Hn
    

  3. Once you know the hard limit, increase the soft limit using following command such that it doesn’t exceed the hard limit:
    
        ulimit -n <desired maximum open files value>
    

For example, to increase the soft limit to 4096, use the following command:

    
        ulimt -n 4096
    

  4. Confirm the soft limit change by using either `ulimit -a` or `ulimit -Sn` command, and then use the same terminal to launch the Unity Editor.

### Increase the maximum open file limit system wide

To increase the maximum open file limit system wide, follow these steps:

  1. Locate the limits configuration file in the following location: `/etc/security/limits.conf`.

  2. Modify the following line: ` [UserName] soft nofile [Desired soft open file limit] ` where `[UserName]` can be the username of the desired user, root, or * to include all the users excluding root. You can also increase the hard limit in this file, but make sure that you don’t exceed the hard limit set by the system.

  
Following is an example of how the `limits.conf` file located in
`/etc/security/limits.conf` looks after adding the soft and hard limit values
to increase the open file count.

    
        * soft nofile 4096
    * hard nofile 4096
    

  3. Reboot the system.

  4. Confirm that the values have actually changed by running the following commands.

     * Soft open file limit:
    
        ulimit -Sn
    

     * Hard open file limit:
    
        ulimit -Hn
    

  5. Launch the Unity Editor.

## Additional resources:

  * [System Requirements](system-requirements.html)

[](build-for-linux.html)

Build a Linux application

[](AppleMac.html)

macOS

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

