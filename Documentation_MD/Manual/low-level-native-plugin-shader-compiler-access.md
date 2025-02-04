[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/low-level-native-plugin-shader-compiler-access.html)
  * [中文](/cn/current/Manual/low-level-native-plugin-shader-compiler-access.html)
  * [日本語](/ja/current/Manual/low-level-native-plugin-shader-compiler-access.html)
  * [한국어](/kr/current/Manual/low-level-native-plugin-shader-compiler-access.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/low-level-native-plugin-shader-compiler-access.html)
  * [中文](/cn/current/Manual/low-level-native-plugin-shader-compiler-access.html)
  * [日本語](/ja/current/Manual/low-level-native-plugin-shader-compiler-access.html)
  * [한국어](/kr/current/Manual/low-level-native-plugin-shader-compiler-access.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Integrating third-party code libraries (plug-ins)](plug-ins.html)
  * [Low-level native plug-in interface](native-plugin-interface.html)
  * Low-level native plug-in Shader compiler access

[](low-level-native-plugin-rendering-extensions.html)

Low-level native plug-in rendering extensions

[](low-level-native-plugin-memory-manager-api.html)

Memory Manager API for low-level native plug-ins

# Low-level native plug-in Shader compiler access

On top of the [low-level native plug-in interface](native-plugin-
interface.html), Unity also supports low level access to the **shader** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) compiler, allowing the user to inject
different variants into a shader. It is also an event driven approach in which
the **plug-in** A set of code created outside of Unity that creates
functionality in Unity. There are two kinds of plug-ins you can use in Unity:
Managed plug-ins (managed .NET assemblies created with tools like Visual
Studio) and Native plug-ins (platform-specific native code libraries). [More
info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) will receive callbacks when certain
builtin events happen.

The shader compiler access extension definition exposed by Unity is to be
found in IUnityShaderCompilerAccess.h and it’s provided with the editor.

These extensions are supported for now only on D3D11. Support for more
platforms will follow.

## Shader compiler access extension API

In order to take advantage of the rendering extension, a plug-in should export
UnityShaderCompilerExtEvent. There is a lot of documentation provided inside
the include file.

A plug-in will get called via UnityShaderCompilerExtEvent whenever one of the
builtin events is triggered by Unity. The callbacks can also be added to
CommandBuffers via CommandBuffer.IssuePluginEventAndData or
CommandBuffer.IssuePluginCustomBlit command from **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

In addition to the basic script interface, [Native Code plug-ins](./plug-
ins.html) in Unity can receive callbacks when certain events happen. This is
mostly used to implement low-level rendering in your plug-in and enable it to
work with Unity’s multithreaded rendering.

Headers defining interfaces exposed by Unity are provided with the editor.

## Shader compiler access configuration interface

Unity provides an interface (IUnityShaderCompilerExtPluginConfigure) to which
the shader compiler access is configured. This interface is used by the plug-
in to reserve its own keyword(s) and configure shader program and gpu program
compiler masks ( For what types for shader or GPU programs the plug-in should
be invoked )

## Additional resources

  * [Low-level native plug-in rendering extensions](low-level-native-plugin-rendering-extensions.html)
  * [Low-level native plug-in memory manager API](low-level-native-plugin-memory-manager-api.html)
  * [Low-level native plug-in memory manager API reference](low-level-native-plugin-memory-manager-api-reference.html)

[](low-level-native-plugin-rendering-extensions.html)

Low-level native plug-in rendering extensions

[](low-level-native-plugin-memory-manager-api.html)

Memory Manager API for low-level native plug-ins

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

