[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ManualActivationCmdMac.html)
  * [中文](/cn/current/Manual/ManualActivationCmdMac.html)
  * [日本語](/ja/current/Manual/ManualActivationCmdMac.html)
  * [한국어](/kr/current/Manual/ManualActivationCmdMac.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ManualActivationCmdMac.html)
  * [中文](/cn/current/Manual/ManualActivationCmdMac.html)
  * [日本語](/ja/current/Manual/ManualActivationCmdMac.html)
  * [한국어](/kr/current/Manual/ManualActivationCmdMac.html)

  * [Install and upgrade](install-and-upgrade.html)
  * [Licenses and activation](LicensesAndActivation.html)
  * [Manual license activation](ManualActivationGuide.html)
  * Submit a license request from a command line and browser (macOS, Linux)

[](ManualActivationCmdWin.html)

Submit a license request from a command line and browser (Windows)

[](ActivationFAQ.html)

License troubleshooting

# Submit a license request from a command line and browser (macOS, Linux)

Submit a license request from the command line to manually activate your
license if you’re unable to use the [other activation
methods](LicenseActivationMethods.html).

Note: The manual activation method works only with plans other than Unity
Personal.  
---  
  
## Before you begin

  * See [Manual license activation](ManualActivationGuide.html) to make sure you understand the scenario for using this procedure, its limitations, and its internet connectivity requirements.
  * Make sure you know the path where you installed the Unity Editor. Use the Unity Hub to determine the path. Open the Unity Hub and select **Installs** from the side menu. The list shows the path for each installed Editor. For more information, see [Locate the Editor](https://docs.unity3d.com/hub/manual/AddEditor.html#locate-the-editor-program-file).

The default installation paths for the Unity Editor are:

  * macOS: `/Applications/Unity/Hub/Editor/<version>/Unity.app`
  * Linux: `/Applications/Unity/Hub/Editor/<version>/Unity.app`

## Procedure

To manually activate your Unity license, follow these steps:

  1. Create a license request file (`.alf`) from the command line. You must do this step from the computer where you installed Unity.
  2. Use that `.alf` file to generate a Unity license file (`.ulf`) from Unity. You must do this step from any computer that has internet access.
  3. Use that `.ulf` file to activate your license from the command line. You must do this step from the computer where you installed Unity.

### 1) Create a license request file from the command line

**Important** : You must run this command from the computer where you
installed Unity, but the computer doesn’t need internet access for this step
to work.

  1. Make sure you know the installation location of your Unity Editor (ending with `Unity.app`), described earlier. On macOS, you’ll add `/Contents/MacOS/Unity` to this path for this procedure.

**Note** : On macOS, although you don’t need Finder for this step, this latter
subdirectory structure isn’t visible in Finder, unless you right-click the
Unity application (`Unity.app`) and select **Show Package Contents**.

For example, for a `2022.2.0b4` Editor, the complete path to the `Unity`
command on macOS is:

    
        /Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app/Contents/MacOS/Unity
    

  2. Open a Terminal session (macOS) or the command line (Linux), and make sure you’re aware which directory you’re in. The directory you run the command from is the same directory where the `.alf` file is output. You can use the `pwd` command to determine your directory.

  3. Run the following command, replacing `<editor-command-location>` with the complete path to the `Unity` command from Step 1:
    
        <editor-command-location> -batchmode -createManualActivationFile -logfile
    

**Note:** This command doesn’t return output to the Terminal or command line
window. When the command completes, it returns control to the command prompt.

  4. When the command completes, check the directory where you ran the command to make sure it created an activation license file, such as `Unity_v2022.2.0b4.alf`. If you experience issues, see Troubleshooting.

Now you are ready to generate a Unity license file.

##### Example (macOS)

Assuming you installed a `2022.2.0b4` Editor at
`/Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app`, the command for this
step is:

    
    
    /Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app/Contents/MacOS/Unity -batchmode -createManualActivationFile -logfile
    

  

### 2) Generate a Unity license file

The next step is to use the license activation file (`.alf`) that you just
created to request a Unity license file (`.ulf`).

**Important** : You can generate a Unity license file from any computer; it
doesn’t necessarily need to be the same computer where you installed Unity.
However, the computer you use in this step must have an internet connection.

  1. Go to [id.unity.com](https://id.unity.com/) and make sure you’re signed in to your Unity ID. You need a valid login to request a Unity license file.

  2. Use the same browser session to go to [license.unity3d.com/manual](https://license.unity3d.com/manual). The **Manual activation** page appears.

**Note:** If you experience issues accessing this page, try pasting
`https://license.unity3d.com/manual` into your browser’s address bar.

![](../uploads/Main/license-request-ulf.png)

  3. Select the **Browse** button and use your computer’s file browser to select the license activation (`.alf`) file from the create a license request file step.

If the upload was successful and Unity detected that the file you chose was a
license activation file, the filename appears in the text box with a green
check mark. If you see a red **X** instead, try again.

  4. Select the **Next** button. The **Activate your license** page appears.

![](../uploads/Main/license-request-activate.png)

  5. Enter the serial key you received in an email when you purchased a single license. You need to enter the key in the exact format that it appears in the email. For example, `PS/SC/E3-XXXX-XXXX-XXXX-XXXX`.

  6. Select the **Next** button. The **Download license file** page appears.

![](../uploads/Main/license-request-download.png)

  7. Select the **Download license file** button. If prompted, allow downloads for the [license.unity3d.com/manual](https://license.unity3d.com/manual) page.

  8. Open your browser’s downloads location and confirm the new Unity license file, which has a `.ulf` extension. For example, `Unity_v2017.x.ulf`.

Now you are ready to activate your Unity license from the command line.

### 3) Activate your license from the command line

**Important** : You must run this command from the computer where you
installed Unity, but the computer doesn’t need internet access for this step
to work.

  1. Make sure you know the following paths:

     * `<editor-command-location>` is the same value as the path described in the create a license request file step.
     * `<yourUlfFile>` is the full path of the `.ulf` file you generated in the generate a Unity license file step.
  2. Open a Terminal session (macOS) or the command line (Linux), and run the following command, replacing `<editor-command-location>` and `<yourUlfFile>` with the actual full paths:
    
        <editor-command-location> -batchmode -manualLicenseFile <yourUlfFile> -logfile
    

**Note:** This command doesn’t return output to the Terminal or command line
window. When the command completes, it returns control to the command prompt.

  3. When the command completes, you can view your active license in the Hub by opening the Preferences menu (![](../uploads/Main/hubPref.png)) and selecting **Licenses**. If you experience issues, see Troubleshooting.

##### Example (macOS)

This example assumes that you:

  * Installed a `2022.2.0b4` Editor at `/Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app`
  * Generated a `.ulf` file and stored it at `/Users/myAccount/Downloads/Unity_v2017.x.ulf`

    
    
    /Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app/Contents/MacOS/Unity -batchmode -manualLicenseFile /Users/myAccount/Downloads/Unity_v2017.x.ulf -logfile
    

  

## Troubleshooting

If the command line operations don’t yield the expected results, view the
`Editor.log` file. Check the location of this file in [Log Files](LogFiles).

## Additional resources

  * For troubleshooting activation issues, see [Activation issues](ActivationFAQ.html)
  * For documentation for the Unity Hub, see [Hub documentation](https://docs.unity3d.com/hub/manual/index.html)

[](ManualActivationCmdWin.html)

Submit a license request from a command line and browser (Windows)

[](ActivationFAQ.html)

License troubleshooting

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

