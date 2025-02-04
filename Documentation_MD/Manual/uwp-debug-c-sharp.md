[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/uwp-debug-c-sharp.html)
  * [中文](/cn/current/Manual/uwp-debug-c-sharp.html)
  * [日本語](/ja/current/Manual/uwp-debug-c-sharp.html)
  * [한국어](/kr/current/Manual/uwp-debug-c-sharp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/uwp-debug-c-sharp.html)
  * [中文](/cn/current/Manual/uwp-debug-c-sharp.html)
  * [日本語](/ja/current/Manual/uwp-debug-c-sharp.html)
  * [한국어](/kr/current/Manual/uwp-debug-c-sharp.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Develop for Universal Windows Platform](uwp-developing.html)
  * [IL2CPP scripting backend for UWP](uwp-il2cpp-scripting.html)
  * [Debug UWP applications with IL2CPP](uwp-il2cpp-debugging.html)
  * Debug C# code

[](uwp-il2cpp-debugging.html)

Debug UWP applications with IL2CPP

[](uwp-debug-generated-cpp.html)

Debug generated C++ code

# Debug C# code

Before you can debug C# code with **IL2CPP** A Unity-developed scripting back-
end which you can use as an alternative to Mono when building projects for
some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) for your Universal Windows Platform
(UWP) application, you need to do the following:

  1. In **File** > **Build Settings** , enable **Script Debugging**.
  2. In **Player** settings, enable the **InternetClient** , **InternetClientServer** , and **PrivateNetworkClientServer** capabilities.   
**Note:** You can also enable these capabilities in the manifest. You will
need to change these capabilities from the Visual Studio manifest editor
because the manifest isn’t overwritten when you build on top of an earlier
build.

The debugging procedure for UWP applications is the same as for other
platforms. For more information on how to debug C# code, refer to [Debug C#
code in Unity](managed-code-debugging.html).

## Additional resources

  * [Debug C# code in Unity](managed-code-debugging.html)
  * [Microsoft documentation on how to Debug C# code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/get-started/csharp/tutorial-debugger?toc=%2Fvisualstudio%2Fdebugger%2Ftoc.json&view=vs-2022)
  * [Microsoft documentation on Unity debugging with Visual Studio](https://learn.microsoft.com/en-us/visualstudio/gamedev/unity/get-started/using-visual-studio-tools-for-unity?pivots=windows#unity-debugging)
  * [IL2CPP overview](./scripting-backends-il2cpp.html)
  * [IL2CPP scripting backend for UWP](uwp-il2cpp-scripting.html)

[](uwp-il2cpp-debugging.html)

Debug UWP applications with IL2CPP

[](uwp-debug-generated-cpp.html)

Debug generated C++ code

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

