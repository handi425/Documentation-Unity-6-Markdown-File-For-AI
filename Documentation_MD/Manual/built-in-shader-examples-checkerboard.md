[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-shader-examples-checkerboard.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-checkerboard.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-checkerboard.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-checkerboard.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-shader-examples-checkerboard.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-checkerboard.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-checkerboard.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-checkerboard.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
  * Checkerboard pattern shader example in the Built-In Render Pipeline

[](built-in-shader-examples-single-color.html)

Single color shader example in the Built-In Render Pipeline

[](built-in-shader-examples-unlit.html)

Simple unlit shader example in the Built-In Render Pipeline

# Checkerboard pattern shader example in the Built-In Render Pipeline

![](../uploads/SL/ExampleCheckerboard.png)

Here’s a **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that outputs a checkerboard pattern
based on texture coordinates of a **mesh** The main graphics primitive of
Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh):

    
    
    Shader "Unlit/Checkerboard"
    {
        Properties
        {
            _Density ("Density", Range(2,50)) = 30
        }
        SubShader
        {
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #include "UnityCG.cginc"
    
                struct v2f
                {
                    float2 uv : TEXCOORD0;
                    float4 vertex : SV_POSITION;
                };
    
                float _Density;
    
                v2f vert (float4 pos : POSITION, float2 uv : TEXCOORD0)
                {
                    v2f o;
                    o.vertex = UnityObjectToClipPos(pos);
                    o.uv = uv * _Density;
                    return o;
                }
                
                fixed4 frag (v2f i) : SV_Target
                {
                    float2 c = i.uv;
                    c = floor(c) / 2;
                    float checker = frac(c.x + c.y) * 2;
                    return checker;
                }
                ENDCG
            }
        }
    }
    

The density slider in the [Properties](SL-Properties.html) block controls how
dense the checkerboard is. In the **vertex shader** A program that runs on
each vertex of a 3D model when the model is being rendered. [More
info](writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader), the mesh UVs are multiplied by
the density value to take them from a range of 0 to 1 to a range of 0 to
density. Let’s say the density was set to 30 - this will make **i.uv** input
into the fragment shader contain floating point values from zero to 30 for
various places of the mesh being rendered.

Then the fragment shader code takes only the integer part of the input
coordinate using HLSL’s built-in **floor** function, and divides it by two.
Recall that the input coordinates were numbers from 0 to 30; this makes them
all be “quantized” to values of 0, 0.5, 1, 1.5, 2, 2.5, and so on. This was
done on both the x and y components of the input coordinate.

Next up, we add these x and y coordinates together (each of them only having
possible values of 0, 0.5, 1, 1.5, …) and only take the fractional part using
another built-in HLSL function, **frac**. Result of this can only be either
0.0 or 0.5. We then multiply it by two to make it either 0.0 or 1.0, and
output as a color (this results in black or white color respectively).

[](built-in-shader-examples-single-color.html)

Single color shader example in the Built-In Render Pipeline

[](built-in-shader-examples-unlit.html)

Simple unlit shader example in the Built-In Render Pipeline

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

