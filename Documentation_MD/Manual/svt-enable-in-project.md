[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/svt-enable-in-project.html)
  * [中文](/cn/current/Manual/svt-enable-in-project.html)
  * [日本語](/ja/current/Manual/svt-enable-in-project.html)
  * [한국어](/kr/current/Manual/svt-enable-in-project.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/svt-enable-in-project.html)
  * [中文](/cn/current/Manual/svt-enable-in-project.html)
  * [日本語](/ja/current/Manual/svt-enable-in-project.html)
  * [한국어](/kr/current/Manual/svt-enable-in-project.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Streaming Virtual Texturing](svt-streaming-virtual-texturing.html)
  * Enabling Streaming Virtual Texturing in your project

[](svt-how-it-works.html)

How Streaming Virtual Texturing works

[](svt-use-in-shader-graph.html)

Using Streaming Virtual Texturing in Shader Graph

# Enabling Streaming Virtual Texturing in your project

This feature is experimental and not ready for production use. The feature and
documentation might be changed or removed in the future.

To enable Streaming Virtual Texturing, you need to enable **Virtual
Texturing** in your project. To do this, go to **Edit > Project Settings >
Player** and enable the **Virtual Texturing** setting.

![](../uploads/Main/svt-enable-in-project01.png)

Virtual Texturing is a project-wide setting that is shared for all platforms.
You cannot build a player for platforms and graphics APIs that don’t support
Virtual Texturing. Virtual Texturing can allocate resources such as buffers,
even if you don’t use the feature in your project, so don’t enable **Virtual
Texturing** if you don’t plan to use it.

When you enable **Virtual Texturing** in your project, Unity adds the
following compiler directives:

  * `ENABLE_VIRTUALTEXTURES`: C# define that evaluates to `True` if your project supports Virtual Texturing.
  * `ENABLE_VIRTUALTEXTURING`: C++ and C# editor define that evaluates to `True` if Virtual Texturing is possible on the current build target.
  * `UNITY_VIRTUAL_TEXTURING`: **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) version of `ENABLE_VIRTUALTEXTURES`.

Note that these might be renamed in future versions of Unity.

[](svt-how-it-works.html)

How Streaming Virtual Texturing works

[](svt-use-in-shader-graph.html)

Using Streaming Virtual Texturing in Shader Graph

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

