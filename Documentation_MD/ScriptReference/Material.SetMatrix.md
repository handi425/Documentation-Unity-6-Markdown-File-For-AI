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

#  [Material](Material.html).SetMatrix

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

[Switch to Manual](../Manual/class-Material.html "Go to Material Component in
the Manual")

## Declaration

public void SetMatrix(string name, [Matrix4x4](Matrix4x4.html) value);

## Declaration

public void SetMatrix(int nameID, [Matrix4x4](Matrix4x4.html) value);

### Parameters

nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
---|---  
name | Property name, e.g. "_CubemapRotation".  
value | Matrix value to set.  
  
### Description

Sets a named matrix for the shader.

This is mostly used with custom shaders that need extra matrix parameters.
Matrix parameters are not exposed in the material inspector, but can be set
and queried with `SetMatrix` and `GetMatrix` from scripts.  
  
Additional resources: [GetMatrix](Material.GetMatrix.html),
[Materials](../Manual/Materials.html), [ShaderLab
documentation](../Manual/Shaders.html),
[Shader.PropertyToID](Shader.PropertyToID.html), [Properties in Shader
Programs](../Manual/SL-PropertiesInPrograms.html).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Attach to an object that has a [Renderer](Renderer.html) component,
        // and use material with the shader below.
        public float rotateSpeed = 30f;
        public void [Update](PlayerLoop.Update.html)()
        {
            // Construct a rotation matrix and set it for the shader
            [Quaternion](Quaternion.html) rot = [Quaternion.Euler](Quaternion.Euler.html)(0, 0, [Time.time](Time-time.html) * rotateSpeed);
            [Matrix4x4](Matrix4x4.html) m = [Matrix4x4.TRS](Matrix4x4.TRS.html)([Vector3.zero](Vector3-zero.html), rot, [Vector3.one](Vector3-one.html));
            GetComponent<[Renderer](Renderer.html)>().material.SetMatrix("_TextureRotation", m);
        }
    }
    
    
    
    // Use this shader on an object together with the above example script.
    // The shader transforms texture coordinates with a matrix set from a script.
    [Shader](Shader.html) "RotatingTexture"
    {
        Properties
        {
            _MainTex ("Base (RGB)", 2D) = "white" {}
        }
        SubShader
        {
            [Pass](ShaderData.Pass.html)
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag  
      
                struct v2f
                {
                    float2 uv : TEXCOORD0;
                    float4 pos : SV_POSITION;
                };  
      
                float4x4 _TextureRotation;  
      
                v2f vert (float4 pos : POSITION, float2 uv : TEXCOORD0)
                {
                    v2f o;
                    o.pos = UnityObjectToClipPos(pos);
                    o.uv = mul(_TextureRotation, float4(uv,0,1)).xy;
                    return o;
                }  
      
                sampler2D _MainTex;
                fixed4 frag (v2f i) : SV_Target
                {
                    return tex2D(_MainTex, i.uv);
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

