[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-CustomRenderTexture-write-shader.html)
  * [中文](/cn/current/Manual/class-CustomRenderTexture-write-shader.html)
  * [日本語](/ja/current/Manual/class-CustomRenderTexture-write-shader.html)
  * [한국어](/kr/current/Manual/class-CustomRenderTexture-write-shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-CustomRenderTexture-write-shader.html)
  * [中文](/cn/current/Manual/class-CustomRenderTexture-write-shader.html)
  * [日本語](/ja/current/Manual/class-CustomRenderTexture-write-shader.html)
  * [한국어](/kr/current/Manual/class-CustomRenderTexture-write-shader.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Rendering to a texture](render-texture-landing.html)
  * [Drawing to textures with shaders via Custom Render Textures](class-CustomRenderTexture-landing.html)
  * Write a shader for a Custom Render Texture

[](class-CustomRenderTexture-create.html)

Create a Custom Render Texture

[](class-CustomRenderTexture-configure.html)

Control when a Custom Render Texture updates

# Write a shader for a Custom Render Texture

To update a Custom **Render Texture** A special type of Texture that is
created and updated at runtime. To use them, first create a new Render Texture
and designate one of your Cameras to render into it. Then you can use the
Render Texture in a Material just like a regular Texture. [More info](class-
RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) manually, you can write a
specialized Custom Render Texture **shader** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

To help you write your Custom Render Texture shaders, here are two example
frameworks that contain utility functions and built-in helper variables.

The following shader example fills the texture with a color multiplied by a
color. When you write a shader for a Custom Render Texture, you must do the
following:

  * `#include "UnityCustomRenderTexture.cginc"`.
  * Use the provided **Vertex Shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader)
`CustomRenderTextureVertexShader`.

  * Use the provided input structure `v2f_customrendertexture` for the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) shader.

    
    
    Shader "CustomRenderTexture/Simple"
    {
        Properties
        {
            _Color ("Color", Color) = (1,1,1,1)
            _Tex("InputTex", 2D) = "white" {}
         }
    
         SubShader
         {
            Lighting Off
            Blend One Zero
    
            Pass
            {
                CGPROGRAM
                #include "UnityCustomRenderTexture.cginc"
                #pragma vertex CustomRenderTextureVertexShader
                #pragma fragment frag
                #pragma target 3.0
    
                float4      _Color;
                sampler2D   _Tex;
    
                float4 frag(v2f_customrendertexture IN) : COLOR
                {
                    return _Color * tex2D(_Tex, IN.localTexcoord.xy);
                }
                ENDCG
                }
        }
    }
    

The following example is a shader for a material you can use to initialize a
Custom Render Texture. When you write a shader for an initialization Material,
the following steps are mandatory:

  * `#include "UnityCustomRenderTexture.cginc"`

  * Use the provided Vertex Shader `CustomRenderTextureVertexShader`

  * Use the provided input structure `v2f_customrendertexture` for the pixel shader.

    
    
    Shader "CustomRenderTexture/CustomTextureInit"
    {
        Properties
        {
            _Color ("Color", Color) = (1,1,1,1)
            _Tex("InputTex", 2D) = "white" {}
        }
    
        SubShader
        {
            Lighting Off
            Blend One Zero
    
            Pass
            {
                CGPROGRAM
                #include "UnityCustomRenderTexture.cginc"
    
                #pragma vertex InitCustomRenderTextureVertexShader
                #pragma fragment frag
                #pragma target 3.0
    
                float4      _Color;
                sampler2D   _Tex;
    
                float4 frag(v2f_init_customrendertexture IN) : COLOR
                {
                    return _Color * tex2D(_Tex, IN.texcoord.xy);
                }
                ENDCG
            }
        }
    }
    

[](class-CustomRenderTexture-create.html)

Create a Custom Render Texture

[](class-CustomRenderTexture-configure.html)

Control when a Custom Render Texture updates

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

