[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-grabpass.html)
  * [中文](/cn/current/Manual/writing-shader-grabpass.html)
  * [日本語](/ja/current/Manual/writing-shader-grabpass.html)
  * [한국어](/kr/current/Manual/writing-shader-grabpass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-grabpass.html)
  * [中文](/cn/current/Manual/writing-shader-grabpass.html)
  * [日本語](/ja/current/Manual/writing-shader-grabpass.html)
  * [한국어](/kr/current/Manual/writing-shader-grabpass.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * Get the current framebuffer with the GrabPass command

[](SL-BuiltinFunctions.html)

Use built-in shader functions in the Built-In Render Pipeline

[](built-in-shader-examples.html)

HLSL shader examples in the Built-in Render Pipeline

# Get the current framebuffer with the GrabPass command

GrabPass is a command that creates a special type of Pass that grabs the
contents of the frame buffer into a texture. This texture can be used in
subsequent Passes to do advanced image based effects.

This command can significantly increase both CPU and GPU frame times. You
should generally avoid using this command other than for quick prototyping,
and attempt to achieve your effect in other ways. If you do use this command,
try to reduce the number of screen grabbing operations as much as possible;
either by reducing your usage of this command, or by using the signature that
grabs the screen to a named texture if applicable.

GrabPass works only on the frame buffer. You cannot use this command to grab
the contents of other render targets, the **depth buffer** A memory store that
holds the z-value depth of each pixel in an image, where the z-value is the
depth for each rendered pixel from the projection plane. [More info](class-
RenderTexture.html)  
See in [Glossary](Glossary.html#depthbuffer), and so on.

## Examples

This example for the Built-in **Render Pipeline** A series of operations that
take the contents of a Scene, and displays them on a screen. Unity lets you
choose from pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) demonstrates using `GrabPass`
to invert the colors of the render target. Note that this is not an efficient
way to achieve this effect, and is intended only to demonstrate the use of
GrabPass; the same effect could be achieved more efficiently using an invert
blend mode.

    
    
    Shader "GrabPassInvert"
    {
        SubShader
        {
            // Draw after all opaque geometry
            Tags { "Queue" = "Transparent" }
    
            // Grab the screen behind the object into _BackgroundTexture
            GrabPass
            {
                "_BackgroundTexture"
            }
    
            // Render the object with the texture generated above, and invert the colors
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #include "UnityCG.cginc"
    
                struct v2f
                {
                    float4 grabPos : TEXCOORD0;
                    float4 pos : SV_POSITION;
                };
    
                v2f vert(appdata_base v) {
                    v2f o;
                    // use UnityObjectToClipPos from UnityCG.cginc to calculate 
                    // the clip-space of the vertex
                    o.pos = UnityObjectToClipPos(v.vertex);
    
                    // use ComputeGrabScreenPos function from UnityCG.cginc
                    // to get the correct texture coordinate
                    o.grabPos = ComputeGrabScreenPos(o.pos);
                    return o;
                }
    
                sampler2D _BackgroundTexture;
    
                half4 frag(v2f i) : SV_Target
                {
                    half4 bgcolor = tex2Dproj(_BackgroundTexture, i.grabPos);
                    return 1 - bgcolor;
                }
                ENDCG
            }
    
        }
    }
    
    

## Additional resources

  * [GrabPass directive in ShaderLab reference](SL-GrabPass.html)
  * [Writing shaders in code](shader-writing.html)

[](SL-BuiltinFunctions.html)

Use built-in shader functions in the Built-In Render Pipeline

[](built-in-shader-examples.html)

HLSL shader examples in the Built-in Render Pipeline

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

