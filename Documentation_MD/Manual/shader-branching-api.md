[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-branching-api.html)
  * [中文](/cn/current/Manual/shader-branching-api.html)
  * [日本語](/ja/current/Manual/shader-branching-api.html)
  * [한국어](/kr/current/Manual/shader-branching-api.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-branching-api.html)
  * [中文](/cn/current/Manual/shader-branching-api.html)
  * [日本語](/ja/current/Manual/shader-branching-api.html)
  * [한국어](/kr/current/Manual/shader-branching-api.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Branching in shaders](shader-branching.html)
  * [Branch in a shader via built-in macros](shader-branching-built-in-macros.html)
  * Branch based on platform or graphics API

[](shader-branching-built-in-macros.html)

Branch in a shader via built-in macros

[](shader-branching-shader-model.html)

Branch based on shader model

# Branch based on platform or graphics API

**Macro:** | **Target platform:**  
---|---  
`SHADER_API_D3D11` | Direct3D 11  
`SHADER_API_GLCORE` | Desktop OpenGL “core” (GL 3/4)  
`SHADER_API_GLES3` | OpenGL ES 3.0/3.1  
`SHADER_API_METAL` | iOS/Mac Metal  
`SHADER_API_VULKAN` | Vulkan  
`SHADER_API_D3D11_9X` | Direct3D 11 “feature level 9.x” target for Universal Windows Platform  
`SHADER_API_DESKTOP` | Windows, Mac and Linux desktop platforms, Web  
`SHADER_API_MOBILE` | iOS and Android mobile platforms, tvOS  
  
Additionally, `SHADER_TARGET_GLSL` is defined when the target shading language
is GLSL (always true for OpenGL/GLES platforms).

## Additional resources

  * [HLSL pragma directives reference](SL-PragmaDirectives.html)
  * [HLSL pragma target command reference](SL-Pragma-target.html)
  * [HLSL pragma require command reference](SL-Pragma-require.html)

[](shader-branching-built-in-macros.html)

Branch in a shader via built-in macros

[](shader-branching-shader-model.html)

Branch based on shader model

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

