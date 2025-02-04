[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/il2cpp-managed-stack-traces.html)
  * [中文](/cn/current/Manual/il2cpp-managed-stack-traces.html)
  * [日本語](/ja/current/Manual/il2cpp-managed-stack-traces.html)
  * [한국어](/kr/current/Manual/il2cpp-managed-stack-traces.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/il2cpp-managed-stack-traces.html)
  * [中文](/cn/current/Manual/il2cpp-managed-stack-traces.html)
  * [日本語](/ja/current/Manual/il2cpp-managed-stack-traces.html)
  * [한국어](/kr/current/Manual/il2cpp-managed-stack-traces.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Scripting backends](scripting-backends.html)
  * [IL2CPP Overview](scripting-backends-il2cpp.html)
  * Managed stack traces with IL2CPP

[](il2cpp-windows-runtime-support.html)

Windows Runtime support

[](scripting-restrictions.html)

Scripting restrictions

# Managed stack traces with IL2CPP

When an exception happens in managed code, the stack trace for the exception
can help you understand the cause of the exception. However, the managed stack
trace might not appear as expected in some cases. The stack trace varies
depending on the build configuration.​

## C++ Compiler Configuration options

### Debug

When you set the [C++ Compiler
Configuration](../ScriptReference/Il2CppCompilerConfiguration.html) property
to **Debug** , **IL2CPP** A Unity-developed scripting back-end which you can
use as an alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) reports a reliable managed stack
trace, and includes each managed method in the call stack. The stack trace
doesn’t include line numbers from the original C# source code.​

### Release and master

When you set the [C++ Compiler
Configuration](../ScriptReference/Il2CppCompilerConfiguration.html) property
to either the **Release** or **Master** setting, IL2CPP might produce a call
stack that’s missing one or more managed methods. This happens when the C++
compiler inlines the missing methods. Method inlining usually improves runtime
performance, but it can make call stacks more difficult to understand.

IL2CPP always provides at least one managed method on the call stack. For
stack traces created from managed exceptions, this is the method where the
exception occurred. It also includes other methods if they aren’t inlined.​

## Source code line numbers

To include file and line number information in the managed stack traces, go to
**Edit** > **Project Settings** > **Player** > **Other Settings**. Then, under
the **Configuration** heading, set the **IL2CPP Stacktrace Information**
property to the **Method Name, File Name, and Line Number** setting.

![The IL2CPP Stacktrace Information property, set to Method Name, File Name,
and Line Number](../uploads/Main/IL2CPP-source-code-line-numbers.png) The
IL2CPP Stacktrace Information property, set to Method Name, File Name, and
Line Number

This setting instructs IL2CPP to include all managed stack frames in the call
stack. Each stack frame also includes the proper C# line number, as long as a
managed symbol file (.pdb) is available for the managed assembly (.dll) where
that code exists.

When you enable this feature, it slightly increases both the build time and
final size of the built program. The player build process includes an
additional step that processes debug symbol files and generates a new data
file which includes the necessary symbol formation. Unity ships this data file
with the built player and uses it at runtime to determine C# line information
in call stacks.

When you enable this feature, Unity generates correct call stacks in either
the **Release** or **Master** configurations, even in the presence of
inlining.

## Script Debugging enabled

To enable **Script Debugging** , go to **File** > **Build Profiles** and then
enable the **Script Debugging** checkbox. When script debugging is enabled,
IL2CPP reports the correct managed stack trace with the method, file, and line
number. This comes at the expense of a larger program size and decreased
performance.

If you only want to improve stack traces, you shouldn’t enable script
debugging. Instead, enable Source code line numbers as described above.

## Additional resources

  * [C++ Compiler Configuration](../ScriptReference/Il2CppCompilerConfiguration.html)

[](il2cpp-windows-runtime-support.html)

Windows Runtime support

[](scripting-restrictions.html)

Scripting restrictions

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

