[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-MultipleProgramVariants-make-conditionals.html)
  * [中文](/cn/current/Manual/SL-MultipleProgramVariants-make-conditionals.html)
  * [日本語](/ja/current/Manual/SL-MultipleProgramVariants-make-conditionals.html)
  * [한국어](/kr/current/Manual/SL-MultipleProgramVariants-make-conditionals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-MultipleProgramVariants-make-conditionals.html)
  * [中文](/cn/current/Manual/SL-MultipleProgramVariants-make-conditionals.html)
  * [日本語](/ja/current/Manual/SL-MultipleProgramVariants-make-conditionals.html)
  * [한국어](/kr/current/Manual/SL-MultipleProgramVariants-make-conditionals.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * Make shader behavior conditional on keywords

[](SL-MultipleProgramVariants-declare.html)

Declare shader keywords

[](shader-keywords-material-inspector.html)

Add shader keywords to the Inspector window

# Make shader behavior conditional on keywords

To mark parts of your **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code conditional based on whether you
enable or disable a shader keyword in a set, use [an HLSL if
statement](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-
graphics-hlsl-if).

For example:

    
    
    #pragma multi_compile QUALITY_LOW QUALITY_MED QUALITY_HIGH
    
    if (QUALITY_LOW)
    {
        // code for low quality setting
    }
    

You can enable and disable keywords [using the Inspector](shader-keywords-
material-inspector.html) or [C# scripting](shader-keywords-scripts.html).

What Unity does with your shader code depends on which shader directive you
use.

If you use `dynamic_branch`, Unity creates a uniform integer variable for each
keyword. When you enable a keyword, Unity sets the integer for that variable
to `1`, and your GPU switches to using the code in the `if` statement for that
keyword. This is dynamic branching.

If you use `shader_feature` or `multi_compile`, Unity creates separate [shader
variants](shader-variants.html)A verion of a shader program that Unity
generates according to a specific combination of shader keywords and their
status. A Shader object can contain multiple shader variants. [More
info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant) for each keyword state. Each
variant contains the code from an `if` branch for that keyword. When you
enable a keyword, Unity sends the matching variant to your GPU. This is static
branching.

Refer to [Conditionals in shaders](shader-conditionals-choose-a-type.html) for
more information about when to use which shader directive.

## Branch if a keyword exists

For each keyword in a set, Unity automatically adds a `_KEYWORD_DECLARED`
keyword. For example, if you declare a `QUALITY_LOW` keyword, Unity adds a
`QUALITY_LOW_KEYWORD_DECLARED` keyword.

You can use this to check if a keyword exists, regardless of whether it’s
enabled or disabled.

For example:

    
    
    #pragma multi_compile QUALITY_LOW QUALITY_MED QUALITY_HIGH
    
    #if defined(QUALITY_LOW_KEYWORD_DECLARED)
    {
        // The QUALITY_LOW keyword exists
    }
    

## Branch when all keywords in a set are disabled

To execute code when all keywords in a set are disabled, Unity must create an
additional shader variant or uniform integer for that state.

If you use `shader_feature` or `dynamic_branch` to create a single keyword,
Unity automatically creates an additional variant or uniform integer. For
example:

    
    
    // Creates a variant for when FEATURE_1_ON is enabled, and another for when FEATURE_1_ON is disabled. 
    #pragma shader_feature FEATURE_1_ON
    
    // Creates a uniform integer for when FEATURE_2_ON is enabled, and another for when FEATURE_2_ON is disabled. 
    #pragma dynamic_branch FEATURE_2_ON
    

If you use `shader_feature` or `dynamic_branch` to create a set of two or more
keywords, or you use `multi_compile`, add `_` when you declare a keyword set
so that Unity creates an additional variant or uniform integer. For example:

    
    
    // Creates 5 shader variants, including one for when RED, GREEN, BLUE, and WHITE are all disabled. 
    #pragma shader_feature _ RED GREEN BLUE WHITE
    
    // Creates 2 shader variants, including one for when FEATURE_3_ON is disabled.
    #pragma multi_compile _ FEATURE_3_ON
    
    // Creates 4 uniform integers, including one for when QUALITY_LOW, QUALITY_MED, and QUALITY_HIGH are all disabled.
    #pragma dynamic_branch _ QUALITY_LOW QUALITY_MED QUALITY_HIGH
    

## Use other statements to make shader behavior conditional

You can also use the following HLSL pre-processor directives to create
conditional code:

  * [`#if, #elif, #else and #endif`](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-appendix-pre-if).
  * [`#ifdef and #ifndef`](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-appendix-pre-ifdef).

Using these instead of `if` makes it more difficult to change the `#pragma`
keyword directive later. For example, if you need to reduce the number of
shader variants, it’s more difficult to change to `dynamic_branch`.

[](SL-MultipleProgramVariants-declare.html)

Declare shader keywords

[](shader-keywords-material-inspector.html)

Add shader keywords to the Inspector window

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

