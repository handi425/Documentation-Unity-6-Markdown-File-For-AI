[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/metal-requirements-and-compatibility.html)
  * [中文](/cn/current/Manual/metal-requirements-and-compatibility.html)
  * [日本語](/ja/current/Manual/metal-requirements-and-compatibility.html)
  * [한국어](/kr/current/Manual/metal-requirements-and-compatibility.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/metal-requirements-and-compatibility.html)
  * [中文](/cn/current/Manual/metal-requirements-and-compatibility.html)
  * [日本語](/ja/current/Manual/metal-requirements-and-compatibility.html)
  * [한국어](/kr/current/Manual/metal-requirements-and-compatibility.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * [Graphics API support](GraphicsAPIs.html)
  * [Metal](Metal.html)
  * Metal requirements and compatibility

[](Metal.html)

Metal

[](metal-debug.html)

Debug Metal graphics

# Metal requirements and compatibility

This page lists the requirements for using Metal as well as the features that
Metal is compatible with.

## Platform compatibility

Unity supports Metal for the Unity Player on iOS, tvOS, and macOS. Unity also
supports Metal for the Unity Editor on macOS.

## Hardware compatibility

Unity supports Metal for all Apple devices that Unity supports.

## Render pipeline compatibility

**Feature** | **Built-in**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline)** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)**  
---|---|---|---|---  
**Metal** | Yes | Yes | Yes (macOS only) | Yes  
  
## Shader compatibility

  * Metal supports **shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that have a minimum [shader
compilation target](SL-ShaderCompileTargets.html) of 3.5.

  * Metal doesn’t support geometry shaders.

## Additional resources

  * [Use 16-bit precision in shaders](SL-Use16BitPrecisionInShaders.html)
  * [Writing shaders for different graphics APIs](SL-PlatformDifferences.html)

[](Metal.html)

Metal

[](metal-debug.html)

Debug Metal graphics

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

