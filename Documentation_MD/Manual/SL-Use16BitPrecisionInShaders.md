[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Use16BitPrecisionInShaders.html)
  * [中文](/cn/current/Manual/SL-Use16BitPrecisionInShaders.html)
  * [日本語](/ja/current/Manual/SL-Use16BitPrecisionInShaders.html)
  * [한국어](/kr/current/Manual/SL-Use16BitPrecisionInShaders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Use16BitPrecisionInShaders.html)
  * [中文](/cn/current/Manual/SL-Use16BitPrecisionInShaders.html)
  * [日本語](/ja/current/Manual/SL-Use16BitPrecisionInShaders.html)
  * [한국어](/kr/current/Manual/SL-Use16BitPrecisionInShaders.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)
  * [Shader input](writing-shader-shader-input.html)
  * Use 16-bit precision in shaders

[](SL-DataTypesAndPrecision.html)

HLSL data types in Unity

[](SL-VertexProgramInputs.html)

Input vertex data into a shader

# Use 16-bit precision in shaders

By default, GPUs use 32-bit precision. You can use 16-bit precision instead in
GPU calculations, which has the following benefits on mobile platforms:

  * **Shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) use less memory, bandwidth, and power.

  * Calculations are faster. Using fewer bits can improve how the GPU allocates registers.

## Create a 16-bit variable

To use 16-bit precision in a shader, use `half` when you declare a scalar, a
vector, or a matrix. For example:

    
    
    half _Glossiness;
    half4 _Color;
    half4x4 _Matrix;
    

To use 16-bit precision in a texture sampler, add `_half` when you declare it.
For example:

    
    
    Texture2D<half4> _MainTex;
    

16-bit precision might not be enough for some shader calculations. This might
cause visible errors such as color banding or stuttering geometry. To check
for errors, run your project on a platform that supports `half`. If there are
errors, use `float` instead.

A `half` variable is stored in buffers with a size and alignment of 32 bits.

## Use 16-bit values on more platforms

By default, `half` has no effect on higher performance platforms in Unity, for
example platforms that use MacOS. A `half` variable becomes a `float`, and the
GPU uses 32-bit values for calculations.

To use 16-bit precision on more platforms, go to **Edit** > **Project
Settings** > **Player** and set **Shader Precision Model** to **Uniform**.
Unity then treats `half` in your HLSL code as the following:

  * `min16float` for scalars
  * `float` for texture samplers

When Unity compiles shaders, `min16float` becomes a platform data type that
allows the GPU to use 16-bit precision for calculations if it supports them.
For example:

  * If you use DirectX 11 or 12, the variable remains a `min16float`.
  * If you use OpenGL, the variable becomes `mediump`.
  * If you use Vulkan, the variable becomes a `RelaxedPrecision` float.
  * If you use Metal, the variable becomes a `float`, but the GPU uses 16-bit values for calculations.

To override the **Shader Precision Model** setting for textures, add `_half`
when you declare a texture sampler. For example `Texture2D<half4> _MainTex`.

## Additional resources

  * [Scalar data types](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-scalar) in the Microsoft HLSL documentation.
  * [HLSL data types](SL-DataTypesAndPrecision.html)
  * [Optimize shader runtime performance](SL-ShaderPerformance.html)
  * [Writing shaders for different graphics APIs](SL-PlatformDifferences.html)

[](SL-DataTypesAndPrecision.html)

HLSL data types in Unity

[](SL-VertexProgramInputs.html)

Input vertex data into a shader

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

