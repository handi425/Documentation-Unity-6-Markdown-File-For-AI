[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/low-level-native-plugin-rendering-extensions.html)
  * [中文](/cn/current/Manual/low-level-native-plugin-rendering-extensions.html)
  * [日本語](/ja/current/Manual/low-level-native-plugin-rendering-extensions.html)
  * [한국어](/kr/current/Manual/low-level-native-plugin-rendering-extensions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/low-level-native-plugin-rendering-extensions.html)
  * [中文](/cn/current/Manual/low-level-native-plugin-rendering-extensions.html)
  * [日本語](/ja/current/Manual/low-level-native-plugin-rendering-extensions.html)
  * [한국어](/kr/current/Manual/low-level-native-plugin-rendering-extensions.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Integrating third-party code libraries (plug-ins)](plug-ins.html)
  * [Low-level native plug-in interface](native-plugin-interface.html)
  * Low-level native plug-in rendering extensions

[](native-plugin-interface.html)

Low-level native plug-in interface

[](low-level-native-plugin-shader-compiler-access.html)

Low-level native plug-in Shader compiler access

# Low-level native plug-in rendering extensions

On top of the [low-level native plug-in interface](native-plugin-
interface.html), Unity also supports low level rendering extensions that can
receive callbacks when certain events happen. This is mostly used to implement
and control low-level rendering in your **plug-in** A set of code created
outside of Unity that creates functionality in Unity. There are two kinds of
plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies
created with tools like Visual Studio) and Native plug-ins (platform-specific
native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) and enable it to work with Unity’s
multithreaded rendering.

Due to the low-level nature of this extension the plug-in might need to be
preloaded before the devices get created. Currently the convention is name-
based; the plug-in name must begin _GfxPlugin_ (for example:
_GfxPluginMyNativePlugin_).

The rendering extension definition exposed by Unity is in the file
_IUnityRenderingExtensions.h_ , provided with the Editor (see file path
_Unity\Editor\Data\PluginAPI_).

All platforms supporting **native plug-ins** A platform-specific native code
library that is created outside of Unity for use in Unity. Allows you can
access features like OS calls and third-party code libraries that would
otherwise not be available to Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Nativeplug-in) support these extensions.

## Rendering extensions API

To take advantage of the rendering extension, a plug-in should export
_UnityRenderingExtEvent_ and optionally _UnityRenderingExtQuery_. There is a
lot of documentation provided inside the include file.

## plug-in callbacks on the rendering thread

A plug-in gets called via _UnityRenderingExtEvent_ whenever Unity triggers one
of the built-in events. The callbacks can also be added to CommandBuffers via
[CommandBuffer.IssuePluginEventAndData](../ScriptReference/Rendering.CommandBuffer.IssuePluginEventAndData.html)
or
[CommandBuffer.IssuePluginCustomBlit](../ScriptReference/Rendering.CommandBuffer.IssuePluginCustomBlit.html)
from **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

## Additional resources

  * [Low-level native plug-in shader compiler access](low-level-native-plugin-shader-compiler-access.html)
  * [Low-level native plug-in memory manager API](low-level-native-plugin-memory-manager-api.html)
  * [Low-level native plug-in memory manager API reference](low-level-native-plugin-memory-manager-api-reference.html)

[](native-plugin-interface.html)

Low-level native plug-in interface

[](low-level-native-plugin-shader-compiler-access.html)

Low-level native plug-in Shader compiler access

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

