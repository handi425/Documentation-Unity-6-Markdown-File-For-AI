[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-DataTypesAndPrecision.html)
  * [中文](/cn/current/Manual/SL-DataTypesAndPrecision.html)
  * [日本語](/ja/current/Manual/SL-DataTypesAndPrecision.html)
  * [한국어](/kr/current/Manual/SL-DataTypesAndPrecision.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-DataTypesAndPrecision.html)
  * [中文](/cn/current/Manual/SL-DataTypesAndPrecision.html)
  * [日本語](/ja/current/Manual/SL-DataTypesAndPrecision.html)
  * [한국어](/kr/current/Manual/SL-DataTypesAndPrecision.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)
  * [Shader input](writing-shader-shader-input.html)
  * HLSL data types in Unity

[](writing-shader-shader-input.html)

Shader input

[](SL-Use16BitPrecisionInShaders.html)

Use 16-bit precision in shaders

# HLSL data types in Unity

Unity supports HLSL data types, but handles some differently to provide better
support on mobile platforms.

## Floating point suffixes

Unity doesn’t support [HLSL floating point
suffixes](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-
graphics-hlsl-appendix-grammar#floating-point-numbers).

For example if you use `2.0h` to create a half precision float, Unity treats
it as a high precision float instead.

## Floating point exception handling

Test your **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) on the target platform to know how it
handles floating point exceptions (for example, division by zero).

Desktop GPUs that support Direct3D 10 support the IEEE 754 floating point
standard. This means that float numbers behave exactly as they do in regular
programming languages on the CPU.

Mobile GPUs might not support that standard and handle floating point
exceptions differently. For example, division by zero might result in `NaN`,
zero or another value.

## Additional resources

  * [Use 16-bit precision in shaders](SL-Use16BitPrecisionInShaders.html)
  * [Data Types (HLSL)](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-data-types) in the Microsoft HLSL documentation.
  * [Writing shaders for different graphics APIs](SL-PlatformDifferences.html)
  * [Optimizing Shader Runtime Performance](SL-ShaderPerformance.html)

[](writing-shader-shader-input.html)

Shader input

[](SL-Use16BitPrecisionInShaders.html)

Use 16-bit precision in shaders

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

