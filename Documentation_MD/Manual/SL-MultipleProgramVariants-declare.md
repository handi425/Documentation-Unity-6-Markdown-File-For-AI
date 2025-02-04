[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-MultipleProgramVariants-declare.html)
  * [中文](/cn/current/Manual/SL-MultipleProgramVariants-declare.html)
  * [日本語](/ja/current/Manual/SL-MultipleProgramVariants-declare.html)
  * [한국어](/kr/current/Manual/SL-MultipleProgramVariants-declare.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-MultipleProgramVariants-declare.html)
  * [中文](/cn/current/Manual/SL-MultipleProgramVariants-declare.html)
  * [日本語](/ja/current/Manual/SL-MultipleProgramVariants-declare.html)
  * [한국어](/kr/current/Manual/SL-MultipleProgramVariants-declare.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * Declare shader keywords

[](shader-conditionals-choose-a-type.html)

Choose which type of keyword to use in shaders

[](SL-MultipleProgramVariants-make-conditionals.html)

Make shader behavior conditional on keywords

# Declare shader keywords

To declare **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) keywords, use a `#pragma` directive in
the HLSL code. For example:

    
    
    #pragma shader_feature REFLECTION_TYPE1 REFLECTION_TYPE2 REFLECTION_TYPE3
    

Use one of the following shader directives:

**Shader directive** | **Branching type** | **Shader variants Unity creates**  
---|---|---  
`shader_feature` | [Static branching](shader-branching-use.html#static-branching) | Variants for keyword combinations you enable at build time with material properties  
`multi_compile` | [Static branching](shader-branching-use.html#static-branching) | Variants for every possible combination of keywords  
`dynamic_branch` | [Dynamic branching](shader-branching-use.html#dynamic-branching) | No additional variants  
  
Refer to the following:

  * [Conditionals in shaders](shader-conditionals-choose-a-type.html) for information about when to use which shader directive.
  * [Shader keyword limits](shader-keywords.html#keyword-limits) for information about how many keywords you can declare in a shader.

In Shader Graph, see [Shader Graph: Keyword
Node](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?subfolder=/manual/Keyword-
Node.html) instead.

## Declare sets of keywords

The keywords in a single `#pragma` statement are together called a ‘set’.

For example, to declare a set of three keywords:

    
    
    #pragma shader_feature REFLECTION_TYPE1 REFLECTION_TYPE2 REFLECTION_TYPE3
    

You can declare multiple sets of keywords in a single shader. For example, to
create 2 sets:

    
    
    #pragma shader_feature REFLECTION_TYPE1 REFLECTION_TYPE2 REFLECTION_TYPE3
    #pragma shader_feature RED GREEN BLUE WHITE
    

You can’t do the following:

  * You cannot include two keywords with the same name in one set.
  * You cannot include duplicate keyword sets in one shader.
  * You cannot declare a keyword as both `dynamic_branch` and `shader_feature` or `multi_compile` \- Unity uses `dynamic_branch` if you do this.

## Make keywords local

Keywords are affected by global keyword state by default.

Add `_local` to the shader directive to make the keywords local. If you enable
or disable a global keyword, you don’t affect the state of local keywords with
the same name.

For example:

    
    
    #pragma shader_feature_local REFLECTION_TYPE1 REFLECTION_TYPE2 REFLECTION_TYPE3
    

## Additional resources

  * [Targeting shader models and GPU features in HLSL](SL-ShaderCompileTargets.html)

[](shader-conditionals-choose-a-type.html)

Choose which type of keyword to use in shaders

[](SL-MultipleProgramVariants-make-conditionals.html)

Make shader behavior conditional on keywords

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

