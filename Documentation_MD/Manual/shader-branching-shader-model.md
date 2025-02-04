[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-branching-shader-model.html)
  * [中文](/cn/current/Manual/shader-branching-shader-model.html)
  * [日本語](/ja/current/Manual/shader-branching-shader-model.html)
  * [한국어](/kr/current/Manual/shader-branching-shader-model.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-branching-shader-model.html)
  * [中文](/cn/current/Manual/shader-branching-shader-model.html)
  * [日本語](/ja/current/Manual/shader-branching-shader-model.html)
  * [한국어](/kr/current/Manual/shader-branching-shader-model.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Branching in shaders](shader-branching.html)
  * [Branch in a shader via built-in macros](shader-branching-built-in-macros.html)
  * Branch based on shader model 

[](shader-branching-api.html)

Branch based on platform or graphics API

[](shader-branching-platform.html)

Branch based on platform features

# Branch based on shader model

`SHADER_TARGET` is defined to a numeric value that matches the **Shader** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) target compilation model (that is,
matching `#pragma target` directive). For example, `SHADER_TARGET` is `30`
when compiling into Shader model 3.0. You can use it in Shader code to do
conditional checks. For example:

    
    
    #if SHADER_TARGET < 30
        // less than Shader model 3.0:
        // very limited Shader capabilities, do some approximation
    #else
        // decent capabilities, do a better thing
    #endif
    

## Additional resources

  * [HLSL pragma directives reference](SL-PragmaDirectives.html)
  * [HLSL pragma target command reference](SL-Pragma-target.html)
  * [HLSL pragma require command reference](SL-Pragma-require.html)

[](shader-branching-api.html)

Branch based on platform or graphics API

[](shader-branching-platform.html)

Branch based on platform features

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

