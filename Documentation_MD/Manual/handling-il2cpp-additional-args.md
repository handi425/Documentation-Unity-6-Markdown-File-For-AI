[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/handling-il2cpp-additional-args.html)
  * [中文](/cn/current/Manual/handling-il2cpp-additional-args.html)
  * [日本語](/ja/current/Manual/handling-il2cpp-additional-args.html)
  * [한국어](/kr/current/Manual/handling-il2cpp-additional-args.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/handling-il2cpp-additional-args.html)
  * [中文](/cn/current/Manual/handling-il2cpp-additional-args.html)
  * [日本語](/ja/current/Manual/handling-il2cpp-additional-args.html)
  * [한국어](/kr/current/Manual/handling-il2cpp-additional-args.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Scripting backends](scripting-backends.html)
  * [IL2CPP Overview](scripting-backends-il2cpp.html)
  * Handling platform specific settings for IL2CPP additional arguments

[](scripting-backends-il2cpp.html)

IL2CPP Overview

[](linux-il2cpp-crosscompiler.html)

Linux IL2CPP cross-compiler

# Handling platform specific settings for IL2CPP additional arguments

If your project has the additional **IL2CPP** A Unity-developed scripting
back-end which you can use as an alternative to Mono when building projects
for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) arguments set, then compiling for more
than one platform might not work as expected, especially when cross compiling
for Linux.

To find out if any additional IL2CPP arguments are already set, do one of the
following:

  * Check if the environment variable `IL2CPP_ADDITIONAL_ARGS` is set.
  * In `ProjectSettings/ProjectSettings.asset`, check if the editor script has a value called `additionalIl2CppArgs`.

Note that the methods for setting additional IL2CPP arguments are globally
applied to all platforms, which can cause compilation issues if set for a
platform other than the desired platform. Use the `IPreprocessBuildWithReport`
hook (as shown below) to ensure IL2CPP arguments are set only for the platform
that requires them.

## IPreprocessBuildWithReport hook

Use the `IPreprocessBuildWithReport` hook to build **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) or the Build dialog to set the
additional arguments:

    
    
    class MyCustomPreprocessBuild: IPreprocessBuildWithReport
    {
        public int callbackOrder { get { return 0; } }
        public void OnPreprocessBuild(BuildReport report)
        {
            string addlArgs = "";
            if (report.summary.platform == BuildTarget.StandaloneWindows || report.summary.platform == BuildTarget.StandaloneWindows64)
                addlArgs = "--compiler-flags=\"d2ssa-cfg-jt\"";
            UnityEngine.Debug.Log($"Setting Additional IL2CPP Args = \"{addlArgs}\" for platform {report.summary.platform}");
            PlayerSettings.SetAdditionalIl2CppArgs(addlArgs);
        }
    }
    

## Additional resources

  * [Linux IL2CPP cross-compiler](linux-il2cpp-crosscompiler.html)
  * [Windows Runtime Support](il2cpp-windows-runtime-support.html)
  * [Managed stack traces](il2cpp-managed-stack-traces.html)

[](scripting-backends-il2cpp.html)

IL2CPP Overview

[](linux-il2cpp-crosscompiler.html)

Linux IL2CPP cross-compiler

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

