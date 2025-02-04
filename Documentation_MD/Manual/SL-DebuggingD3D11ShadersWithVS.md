[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-DebuggingD3D11ShadersWithVS.html)
  * [中文](/cn/current/Manual/SL-DebuggingD3D11ShadersWithVS.html)
  * [日本語](/ja/current/Manual/SL-DebuggingD3D11ShadersWithVS.html)
  * [한국어](/kr/current/Manual/SL-DebuggingD3D11ShadersWithVS.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-DebuggingD3D11ShadersWithVS.html)
  * [中文](/cn/current/Manual/SL-DebuggingD3D11ShadersWithVS.html)
  * [日本語](/ja/current/Manual/SL-DebuggingD3D11ShadersWithVS.html)
  * [한국어](/kr/current/Manual/SL-DebuggingD3D11ShadersWithVS.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Troubleshooting shaders](shader-troubleshooting.html)
  * [Debugging shaders](shader-debugging.html)
  * Debug shaders with Visual Studio

[](shader-debugging.html)

Debugging shaders

[](DebuggingShadersWithPIX.html)

Debug shaders with PIX

# Debug shaders with Visual Studio

You can use Visual Studio to debug **shaders** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) in a Unity application on Windows
platforms using DirectX 11 or 12. This page contains information on how to do
this.

**Note:** If you are using DirectX 12, Microsoft recommends that you use PIX
to debug shaders instead of Visual Studio. For information on using PIX on
Windows with Unity, see [Debugging shaders using
PIX](DebuggingShadersWithPIX.html).

## Preparing your shaders

To debug shaders, you must compile them with debug symbols included. To do
that, insert the `#pragma enable_d3d11_debug_symbols` directive into the
source code of each shader that you want to debug.

**Warning:** This pragma directive can negatively affect performance. Remove
it from your shader code before you make a final build. For more information
on this pragma directive, see [Shader compilation: pragma directives](SL-
PragmaDirectives.html).

## Creating a placeholder Visual Studio project for Windows Standalone

If you build your application for Windows Standalone, you must create a
placeholder Visual Studio project. If you build your application for Universal
Windows Platform, Unity generates a Visual Studio project for you.

  1. Launch Visual Studio.
  2. Go to **File** > **New** > **Project** In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) > **Visual C++** > **Empty Project**.

  3. Go to **Project** > **Properties** > **Configuration Properties** > **Debugging**
  4. In the **Command** field, replace $(TargetPath) with the path to your Windows Standalone application (for example, _C:\MyApp\MyApp.exe_)
  5. If you want to force the project to run under DirectX 11, select **Command Arguments** and type **-force-d3d11**.

## Using Visual Studio to debug shaders

For instructions on setting up Visual Studio, see the Microsoft documentation:
[Install Visual Studio](https://docs.microsoft.com/en-
us/visualstudio/install/install-visual-studio?view=vs-2019).

For instructions on setting up and using Visual Studio’s graphics debugging
tools, see the Microsoft documentation: [Visual Studio Graphics
Diagnostics](https://docs.microsoft.com/en-
us/visualstudio/debugger/graphics/visual-studio-graphics-
diagnostics?view=vs-2019).

[](shader-debugging.html)

Debugging shaders

[](DebuggingShadersWithPIX.html)

Debug shaders with PIX

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

