[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-shader-examples-fog.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-fog.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-fog.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-fog.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-shader-examples-fog.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-fog.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-fog.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-fog.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
  * Fog shader example in the Built-In Render Pipeline

[](built-in-shader-examples-receive-shadows.html)

Receiving shadows shader example in the Built-In Render Pipeline

[](built-in-shader-examples-vertex-data.html)

Visualizing vertex data shader examples in the Built-In Render Pipeline

# Fog shader example in the Built-In Render Pipeline

    
    
    Shader "Custom/TextureCoordinates/Fog" {
        SubShader {
            Pass {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                
                //Needed for fog variation to be compiled.
                #pragma multi_compile_fog
    
                #include "UnityCG.cginc"
    
                struct vertexInput {
                    float4 vertex : POSITION;
                    float4 texcoord0 : TEXCOORD0;
                };
    
                struct fragmentInput{
                    float4 position : SV_POSITION;
                    float4 texcoord0 : TEXCOORD0;
                    
                    //Creates a variable that contains fog coordinates. The parameter must be a free TEXCOORD, for example 1 if TEXCOORD1 is free.
                    UNITY_FOG_COORDS(1)
                };
    
                fragmentInput vert(vertexInput i){
                    fragmentInput o;
                    o.position = UnityObjectToClipPos(i.vertex);
                    o.texcoord0 = i.texcoord0;
                    
                    //Compute fog amount from clip space position.
                    UNITY_TRANSFER_FOG(o,o.position);
                    return o;
                }
    
                fixed4 frag(fragmentInput i) : SV_Target {
                    fixed4 color = fixed4(i.texcoord0.xy,0,0);
                    
                    //Apply fog (additive pass are automatically handled)
                    UNITY_APPLY_FOG(i.fogCoord, color); 
                    
                    //to handle custom fog color another option would have been 
                    //#ifdef UNITY_PASS_FORWARDADD
                    //  UNITY_APPLY_FOG_COLOR(i.fogCoord, color, float4(0,0,0,0));
                    //#else
                    //  fixed4 myCustomColor = fixed4(0,0,1,0);
                    //  UNITY_APPLY_FOG_COLOR(i.fogCoord, color, myCustomColor);
                    //#endif
                    
                    return color;
                }
                ENDCG
            }
        }
    }
    

[](built-in-shader-examples-receive-shadows.html)

Receiving shadows shader example in the Built-In Render Pipeline

[](built-in-shader-examples-vertex-data.html)

Visualizing vertex data shader examples in the Built-In Render Pipeline

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

