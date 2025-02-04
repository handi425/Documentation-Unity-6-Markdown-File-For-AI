[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityasaLibrary-Windows.html)
  * [中文](/cn/current/Manual/UnityasaLibrary-Windows.html)
  * [日本語](/ja/current/Manual/UnityasaLibrary-Windows.html)
  * [한국어](/kr/current/Manual/UnityasaLibrary-Windows.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityasaLibrary-Windows.html)
  * [中文](/cn/current/Manual/UnityasaLibrary-Windows.html)
  * [日本語](/ja/current/Manual/UnityasaLibrary-Windows.html)
  * [한국어](/kr/current/Manual/UnityasaLibrary-Windows.html)

  * [Platform development ](PlatformSpecific.html)
  * [Windows](Windows.html)
  * Integrating Unity into Windows applications

[](Windows.html)

Windows

[](playersettings-windows.html)

Windows Player settings

# Integrating Unity into Windows applications

You can use the Unity as a Library feature to integrate the Unity Runtime
Library in Windows applications.

This feature enables you to include Unity-powered features in your
application, such as:

  * 3D/2D Real-Time Rendering
  * **AR** Augmented Reality [More info](AROverview.html)  
See in [Glossary](Glossary.html#AR) Experience

  * 3D model interaction
  * 2D mini-games

The Unity Runtime Library exposes controls to manage when and how to load,
activate, and unload content within the application.

On Windows, you can embed a Unity build into your application in the following
ways:

  * Launch Unity as an external build from your application and specify a window in which Unity will initialize and render with the `-parentHWND` [command line argument](PlayerCommandLineArguments.html). This is the easier option.

  * Embed Unity within your existing operating system process. To do this, call into `UnityPlayer.dll`, which any Win32 application can load directly. The entry point signature is:

`extern "C" UNITY_API int UnityMain(HINSTANCE hInstance, HINSTANCE
hPrevInstance, LPWSTR lpCmdLine, int nShowCmd);`

Use `lpCmdLine` to pass any command line arguments to Unity, for example, to
control resolution, job threads or parent HWND. This enables you to run Unity
within your process. For other valid Unity player command line arguments you
can use, see [Unity Standalone Player command line
arguments](PlayerCommandLineArguments.html).

## Additional resources:

  * [Using Unity as a Library in other applications](UnityasaLibrary.html)
  * [Unity Standalone Player command line arguments](PlayerCommandLineArguments.html)

* * *

  * Unity as a Library added in [2019.3](https://docs.unity3d.com/Manual/30_search.html?q=newin20193).

[](Windows.html)

Windows

[](playersettings-windows.html)

Windows Player settings

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

