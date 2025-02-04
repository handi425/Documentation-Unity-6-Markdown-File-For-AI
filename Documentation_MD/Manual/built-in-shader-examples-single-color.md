[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-shader-examples-single-color.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-single-color.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-single-color.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-single-color.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-shader-examples-single-color.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-single-color.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-single-color.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-single-color.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
  * Single color shader example in the Built-In Render Pipeline

[](built-in-shader-examples.html)

HLSL shader examples in the Built-in Render Pipeline

[](built-in-shader-examples-checkerboard.html)

Checkerboard pattern shader example in the Built-In Render Pipeline

# Single color shader example in the Built-In Render Pipeline

![](../uploads/SL/ExampleSingleColor.png)

    
    
    Shader "Unlit/SingleColor"
    {
        Properties
        {
            // Color property for material inspector, default to white
            _Color ("Main Color", Color) = (1,1,1,1)
        }
        SubShader
        {
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                
                // vertex shader
                // this time instead of using "appdata" struct, just spell inputs manually,
                // and instead of returning v2f struct, also just return a single output
                // float4 clip position
                float4 vert (float4 vertex : POSITION) : SV_POSITION
                {
                    return mul(UNITY_MATRIX_MVP, vertex);
                }
                
                // color from the material
                fixed4 _Color;
    
                // pixel shader, no inputs needed
                fixed4 frag () : SV_Target
                {
                    return _Color; // just return it
                }
                ENDCG
            }
        }
    }
    

[](built-in-shader-examples.html)

HLSL shader examples in the Built-in Render Pipeline

[](built-in-shader-examples-checkerboard.html)

Checkerboard pattern shader example in the Built-In Render Pipeline

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

