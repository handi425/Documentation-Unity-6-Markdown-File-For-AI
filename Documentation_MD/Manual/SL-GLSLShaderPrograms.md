[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-GLSLShaderPrograms.html)
  * [中文](/cn/current/Manual/SL-GLSLShaderPrograms.html)
  * [日本語](/ja/current/Manual/SL-GLSLShaderPrograms.html)
  * [한국어](/kr/current/Manual/SL-GLSLShaderPrograms.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-GLSLShaderPrograms.html)
  * [中文](/cn/current/Manual/SL-GLSLShaderPrograms.html)
  * [日本語](/ja/current/Manual/SL-GLSLShaderPrograms.html)
  * [한국어](/kr/current/Manual/SL-GLSLShaderPrograms.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)
  * GLSL in Unity

[](SL-PlatformDifferences.html)

Writing shaders for different graphics APIs

[](writing-shader-render-state-commands.html)

Setting the render state on the GPU

# GLSL in Unity

As well as writing [HLSL shader programs](writing-shader-writing-shader-
programs-hlsl.html), you can also write raw OpenGL Shading Language (GLSL)
**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) programs in Unity. This is only
supported on OpenGL Core and OpenGL ES platforms.

**Note:** This is not recommended or needed as part of a normal workflow;
Unity cross-compiles your HLSL into optimized GLSL when needed. The use of raw
GLSL is only recommended for testing, or for some special use cases.

## GLSL snippets

GLSL program snippets are written between `GLSLPROGRAM` and `ENDGLSL`
keywords.

In GLSL, all shader function entry points have to be called `main()`. When
Unity loads the GLSL shader, it loads the source once for the vertex program,
with the `VERTEX` preprocessor define, and once more for the fragment program,
with the `FRAGMENT` preprocessor define. So the way to separate vertex and
fragment program parts in GLSL snippet is to surround them with `#ifdef VERTEX
.. #endif` and `#ifdef FRAGMENT .. #endif`. Each GLSL snippet must contain
both a vertex program and a fragment program.

Standard include files match those provided for Cg/HLSL shaders; they just
have a `.glslinc` extension:

    
    
    UnityCG.glslinc
    

Vertex shader inputs come from predefined GLSL variables (`gl_Vertex`,
`gl_MultiTexCoord0`, …) or are user defined attributes. Usually only the
tangent vector needs a user defined attribute:

    
    
    attribute vec4 Tangent;
    

Data from vertex to fragment programs is passed through _varying_ variables,
for example:

    
    
    varying vec3 lightDir; // vertex shader computes this, fragment shader uses this
    

### External OES textures

Unity does some preprocessing during Shader compilation; for example,
`texture2D/texture2DProj` functions may be replaced to `texture/textureProj`,
based on graphics API (GlES3, GLCore). Some extensions don’t support new
convention, most notably
[`GL_OES_EGL_image_external`](https://www.khronos.org/registry/gles/extensions/OES/OES_EGL_image_external.txt).

If you want to sample external textures in GLSL shaders, use
`textureExternal/textureProjExternal` calls instead of
`texture2D/texture2DProj`.

Example:

    
    
    gl_FragData[0] = textureExternal(_MainTex, uv);
    

[](SL-PlatformDifferences.html)

Writing shaders for different graphics APIs

[](writing-shader-render-state-commands.html)

Setting the render state on the GPU

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

