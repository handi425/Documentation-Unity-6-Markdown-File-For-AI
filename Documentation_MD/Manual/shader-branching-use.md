[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-branching-use.html)
  * [中文](/cn/current/Manual/shader-branching-use.html)
  * [日本語](/ja/current/Manual/shader-branching-use.html)
  * [한국어](/kr/current/Manual/shader-branching-use.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-branching-use.html)
  * [中文](/cn/current/Manual/shader-branching-use.html)
  * [日本語](/ja/current/Manual/shader-branching-use.html)
  * [한국어](/kr/current/Manual/shader-branching-use.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Branching in shaders](shader-branching.html)
  * Static and dynamic branching in a shader

[](shader-branching-introduction.html)

Introduction to static and dynamic branching

[](shader-branching-built-in-macros.html)

Branch in a shader via built-in macros

# Static and dynamic branching in a shader

For more information, refer to [Introduction to static and dynamic branching
in shaders](shader-branching-introduction.html).

## Static branching

You can use static branching in your **shaders** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) in the following ways:

  * In hand-coded shaders: 
    * Use [`#if`, `#elif`, `#else`, and `#endif`](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-appendix-pre-if) preprocessor directives, or [`#ifdef` and `#ifndef`](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-appendix-pre-ifdef) preprocessor directives to create static branches.
    * Use an [if statement](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-if) that evaluates a compile-time constant value. Although `if` statements can also be used for dynamic branches, the compiler detects the compile-time constant value and creates a static branch instead.
    * Unity provides [built-in macros](shader-branching-built-in-macros.html) for some compile-time constants that you can use with static branches.

**Note:** Static branching is available only in hand-coded shaders. You cannot
create static branches in Shader Graph.

## Dynamic branching

You can use dynamic branching in your shaders in the following ways:

  * In hand-coded shaders: 
    * **Optional** : Set up [shader keywords](shader-keywords.html) for use with with dynamic branching. You can use dynamic branching without shader keywords, but this provides simple set up and per-material configuration.
    * Use an [if statement](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-if) that evaluates the shader keywords (if used) or any other runtime state. You can use attributes to force the GPU to execute both branches, or to execute only one branch.
  * In Shader Graph, use a [Branch Node](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?subfolder=/manual/Branch-Node.html). This always executes both branches.

[](shader-branching-introduction.html)

Introduction to static and dynamic branching

[](shader-branching-built-in-macros.html)

Branch in a shader via built-in macros

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

