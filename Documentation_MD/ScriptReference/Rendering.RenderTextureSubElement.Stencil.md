[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [RenderTextureSubElement](Rendering.RenderTextureSubElement.html).Stencil

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

The stencil element of a RenderTexture.

Use this to access the stencil data of the underlying surface from a Render
Texture and then bind it in a Shader. Before you create the RenderTexture,
make sure to set the stencil format to one that the target platform supports.  
  
To access the stencil information in a Shader, you must read it from the
correct channel. The stencil data is stored in the red channel for all
graphics APIs that support it except for DirectX 11, in which case it is
stored in the green channel.  
  
If the stencilFormat is set to `R8_UInt`, you need to use the function Load to
read from the Texture. Otherwise, if the format is `R8_UNorm` you can use
sampling.  
  
When using MSAA RenderTextures, you need to define the Stencil Texture using
the equivalent MS Texture types.  
  
You cannot bind the stencil buffer as a RWTexture.  
  
Below is an example Unlit shader that reads the stencil information from a
RenderTexture with stencilFormat `R8_UInt` and writes it as color information
on the green channel.  
  
Additional resources:
[GraphicsFormat](Experimental.Rendering.GraphicsFormat.html).

    
    
    [Shader](Shader.html) "Unlit/ExampleShader"
    {
        Properties
        {
            _ExampleTex("[Texture](Texture.html)", 2D) = "" {}
        }
        SubShader
        {
            Tags { "RenderType" = "Opaque" }
            [LOD](LOD.html) 100  
      
            [Pass](ShaderData.Pass.html)
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #pragma target 4.0  
      
                #include "UnityCG.cginc"  
      
    
                struct appdata
                {
                    float4 vertex : POSITION;
                    float2 uv : TEXCOORD0;
                };  
      
                struct v2f
                {
                    float2 uv : TEXCOORD0;
                    float4 vertex : SV_POSITION;
                };  
      
    
                        #if SHADER_API_D3D11
                        #define STENCIL_CHANNEL g
                        #else
                        #define STENCIL_CHANNEL r
                        #endif  
      
                [Texture2D](Texture2D.html)<uint2> _ExampleTex;  
      
                v2f vert(appdata v)
                {
                    v2f o;
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    o.uv = v.uv;
                    return o;
                }  
      
                fixed4 frag(v2f i) : SV_Target
                {
                    int xRes = 1024;
                    int yRes = 768;  
      
                    uint stencil = _ExampleTex.Load(int3(floor(i.uv.x * xRes), floor(i.uv.y * yRes), 0)).STENCIL_CHANNEL;
                    fixed4 col = float4(0.0, float(stencil) / 255.0f, 0.0, 1.0);  
      
                    return col;
                }  
      
                ENDCG
            }
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

