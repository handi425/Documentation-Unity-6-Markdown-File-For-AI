[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/WindowsLowIntegrity.html)
  * [中文](/cn/current/Manual/WindowsLowIntegrity.html)
  * [日本語](/ja/current/Manual/WindowsLowIntegrity.html)
  * [한국어](/kr/current/Manual/WindowsLowIntegrity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/WindowsLowIntegrity.html)
  * [中文](/cn/current/Manual/WindowsLowIntegrity.html)
  * [日本語](/ja/current/Manual/WindowsLowIntegrity.html)
  * [한국어](/kr/current/Manual/WindowsLowIntegrity.html)

  * [Platform development ](PlatformSpecific.html)
  * [Windows](Windows.html)
  * [Develop for Windows](windows-develop.html)
  * Windows integrity control

[](WindowsDebugging.html)

Windows debugging

[](WindowsPlayerIL2CPPScriptingBackend.html)

Windows Player: IL2CPP Scripting Backend

# Windows integrity control

The **Mandatory Integrity Control** security feature on Windows devices
allocates an integrity level (IL) to all applications and processes. The
device’s operating system or database constrains a user’s or initiator’s
ability to access or perform other operations on an_ object/target_ (such as
files, memory, or directories). Both the initiator and the object are
allocated an IL, with low as the most restricted access. When the initiator
attempts to access the object, their ILs are compared. The initiator can’t
access the object if it has a lower IL than the object.

For more information about integrity levels, see Microsoft’s [Mandatory
Integrity Control](https://docs.microsoft.com/en-
us/windows/win32/secauthz/mandatory-integrity-control) documentation.

Windows Standalone player can detect if it’s running at low integrity ievel.
For more information, see Microsoft’s documentation on [Designing Applications
to Run at a Low Integrity Level](https://msdn.microsoft.com/en-
us/library/bb625960.aspx). In this case, one of the following things might
happen:

  * The log file is written to `%USERPROFILE%\AppData\LocalLow\CompanyName\ProductName`
  * PlayerPrefs is saved to `HKCU\Software\AppDataLow\Software\CompanyName\ProductName`

[](WindowsDebugging.html)

Windows debugging

[](WindowsPlayerIL2CPPScriptingBackend.html)

Windows Player: IL2CPP Scripting Backend

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

