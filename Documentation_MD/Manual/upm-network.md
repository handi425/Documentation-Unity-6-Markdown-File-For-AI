[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-network.html)
  * [中文](/cn/current/Manual/upm-network.html)
  * [日本語](/ja/current/Manual/upm-network.html)
  * [한국어](/kr/current/Manual/upm-network.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-network.html)
  * [中文](/cn/current/Manual/upm-network.html)
  * [日本語](/ja/current/Manual/upm-network.html)
  * [한국어](/kr/current/Manual/upm-network.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Troubleshooting](upm-errors.html)
  * Diagnose network issues

[](upm-errors.html)

Troubleshooting

[](Packages-all.html)

Packages

# Diagnose network issues

Use the Unity Package Manager Diagnostics tool to help diagnose common network
issues associated with Unity Package Manager. The Diagnostics tool runs some
basic network tests and creates files that the Unity support team needs to
diagnose common network problems. After you run the tool, you can share the
results with the Unity support team who can better guide you in resolving
those issues.

To diagnose network issues:

  1. Run the Unity Package Manager Diagnostics tool by using either the Unity Package Manager Error dialog or by Manually running the script. 

  2. View the test results in the shell window. The tool output also lists the location of the `upm-diagnostic-report.txt` report and the `upm-diag.log` file that it created. 

  3. If you need help from the Unity support team, include `upm-diagnostic-report.txt` and `upm-diag.log` when you [submit a bug](https://unity3d.com/unity/qa/bug-reporting).

## Method 1: Use the Unity Package Manager Error dialog

When Unity tries to launch, it starts the Package Manager process before it
loads the project. If it encounters a critical error with Package Manager,
Unity displays the following error message:

![Critical error dialog appears prompting you for action](../uploads/Main/upm-
network.png) Critical error dialog appears prompting you for action

To run the Diagnostics tool, click **Diagnose**. Unity closes and launches the
Diagnostics tool in a new window.

## Method 2: Manually run the script

Locate the `RunUnityPackageManagerDiagnostics` script in the `Diagnostics`
folder within the [installation folder for your Unity
Editor](https://docs.unity3d.com/hub/manual/AddEditor.html#locate-the-editor-
program-file):

**Operating system:** |  **Path to Diagnostics command line tool** :  
---|---  
Windows |  `<path-to-unity-installation-folder>`  
`\Unity`  
`\Data`  
`\Resources`  
`\PackageManager`  
`\Diagnostics`  
`\RunUnityPackageManagerDiagnostics.bat`  
macOS  
Linux |  `<path-to-unity-installation-folder>`  
`\Unity.app`  
`\Contents`  
`\Resources`  
`\PackageManager`  
`\Diagnostics`  
`\RunUnityPackageManagerDiagnostics`  
  
To launch the tool, either:

  * Run the script file from the command line.
  * Double-click the script file in your file browser. **Note:** On macOS, you must right-click `Unity.app` and select **Show Package Contents** to access the contents of `Unity.app`.

## Sample output

![Diagnostic report on top of the tool results in the shell
window](../uploads/Main/upm-network-diagnostics.png) Diagnostic report on top
of the tool results in the shell window

## Additional resources

  * [Configuring your firewall](upm-config-network.html#Firewall)
  * [Configuring your proxy server](upm-config-network.html#Proxy)

[](upm-errors.html)

Troubleshooting

[](Packages-all.html)

Packages

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

