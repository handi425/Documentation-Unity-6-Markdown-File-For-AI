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

#
[ParticleSystemRenderer](ParticleSystemRenderer.html).SetActiveVertexStreams

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

## Declaration

public void SetActiveVertexStreams(List<ParticleSystemVertexStream> streams);

### Parameters

streams | The new array of enabled vertex streams.  
---|---  
  
### Description

Enables a set of Vertex Shader streams on the
[ParticleSystemRenderer](ParticleSystemRenderer.html).

Additional resources:
[ParticleSystemRenderer.GetActiveVertexStreams](ParticleSystemRenderer.GetActiveVertexStreams.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections.Generic;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {  
      
        private [ParticleSystem](ParticleSystem.html) ps;
        private [ParticleSystemRenderer](ParticleSystemRenderer.html) psr;
        private List<[Vector4](Vector4.html)> customData = new List<[Vector4](Vector4.html)>();
        public float minDist = 30.0f;  
      
        void Start() {  
      
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();  
      
            // emit in a sphere with no speed
            var main = ps.main;
            main.startSpeedMultiplier = 0.0f;
            main.simulationSpace = [ParticleSystemSimulationSpace.World](ParticleSystemSimulationSpace.World.html); // so our particle positions don't require any extra transformation, to compare with the mouse position
            var emission = ps.emission;
            emission.rateOverTimeMultiplier = 200.0f;
            var shape = ps.shape;
            shape.shapeType = [ParticleSystemShapeType.Sphere](ParticleSystemShapeType.Sphere.html);
            shape.radius = 4.0f;
            psr.sortMode = [ParticleSystemSortMode.YoungestInFront](ParticleSystemSortMode.YoungestInFront.html);  
      
            // send custom data to the shader
            psr.SetActiveVertexStreams(new List<[ParticleSystemVertexStream](ParticleSystemVertexStream.html)>(new [ParticleSystemVertexStream](ParticleSystemVertexStream.html)[] { [ParticleSystemVertexStream.Position](ParticleSystemVertexStream.Position.html), [ParticleSystemVertexStream.Normal](ParticleSystemVertexStream.Normal.html), [ParticleSystemVertexStream.Color](ParticleSystemVertexStream.Color.html), [ParticleSystemVertexStream.UV](ParticleSystemVertexStream.UV.html), [ParticleSystemVertexStream.Custom1X](ParticleSystemVertexStream.Custom1X.html) }));
        }  
      
        void [Update](PlayerLoop.Update.html)() {  
      
            [Camera](Camera.html) mainCam = [Camera.main](Camera-main.html);  
      
            ps.GetCustomParticleData(customData, [ParticleSystemCustomData.Custom1](ParticleSystemCustomData.Custom1.html));  
      
            // If you know the particle count, or have a reasonable maxParticles threshold, consider caching
            // this array instead of reallocating it on every frame, to avoid per-frame garbage.
            int particleCount = ps.particleCount;
            [ParticleSystem.Particle](ParticleSystem.Particle.html)[] particles = new [ParticleSystem.Particle](ParticleSystem.Particle.html)[particleCount];  
      
            ps.GetParticles(particles);  
      
            for (int i = 0; i < particles.Length; i++)
            {
                [Vector3](Vector3.html) sPos = mainCam.WorldToScreenPoint(particles[i].position);  
      
                // set custom data to 1, if close enough to the mouse
                if ([Vector2.Distance](Vector2.Distance.html)(sPos, [Input.mousePosition](Input-mousePosition.html)) < minDist)
                {
                    customData[i] = new [Vector4](Vector4.html)(1, 0, 0, 0);
                }
                // otherwise, fade the custom data back to 0
                else
                {
                    float particleLife = particles[i].remainingLifetime / ps.main.startLifetimeMultiplier;  
      
                    if (customData[i].x > 0)
                    {
                        float x = customData[i].x;
                        x = [Mathf.Max](Mathf.Max.html)(x - [Time.deltaTime](Time-deltaTime.html), 0.0f);
                        customData[i] = new [Vector4](Vector4.html)(x, 0, 0, 0);
                    }
                }
            }  
      
            ps.SetCustomParticleData(customData, [ParticleSystemCustomData.Custom1](ParticleSystemCustomData.Custom1.html));
        }  
      
        void OnGUI() {  
      
            minDist = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 40, 100, 30), minDist, 0.0f, 100.0f);
        }
    }
    

Here is an example of a custom Shader that you can use with the above script:

    
    
              [Shader](Shader.html) "Particles/CustomVertexStream" {
    Properties {
        _TintColor ("Tint [Color](Color.html)", [Color](Color.html)) = (0.5,0.5,0.5,0.5)
        _MainTex ("[Particle](ParticleSystem.Particle.html) [Texture](Texture.html)", 2D) = "white" {}
        _OffsetValue("Offset Value", Range(0,1)) = 0.4
    }  
      
    [Category](Unity.Android.Gradle.Manifest.Category.html) {
        Tags { "Queue"="Transparent" "IgnoreProjector"="True" "RenderType"="Transparent" }
        Blend SrcAlpha OneMinusSrcAlpha
        ColorMask RGB
        Cull Off Lighting Off ZWrite Off  
      
        SubShader {
            [Pass](ShaderData.Pass.html) {  
      
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #pragma multi_compile_particles
                #pragma multi_compile_fog  
      
                #include "UnityCG.cginc"  
      
                sampler2D _MainTex;
                fixed4 _TintColor;
                float _OffsetValue;  
      
                struct appdata_t {
                    float4 vertex : POSITION;
                    float3 normal : NORMAL;
                    fixed4 color : COLOR;
                    float3 texcoordAndCustom : TEXCOORD0;
                };  
      
                struct v2f {
                    float4 vertex : SV_POSITION;
                    fixed4 color : COLOR;
                    float2 texcoord : TEXCOORD0;
                    float customData : TEXCOORD1;
                    UNITY_FOG_COORDS(2)
                };  
      
                float4 _MainTex_ST;  
      
                v2f vert (appdata_t v)
                {
                    v.vertex.y = lerp(v.vertex.y, v.vertex.y + _OffsetValue, v.texcoordAndCustom.z);  
      
                    v2f o;
                    o.vertex = mul(UNITY_MATRIX_MVP, v.vertex);  
      
                    float4 offsetX = float4(-1, 1, 1, -1);
                    float4 offsetY = float4(1, 1, -1, -1);  
      
                    o.color = v.color;
                    o.texcoord = TRANSFORM_TEX(v.texcoordAndCustom.xy,_MainTex);
                    o.customData = v.texcoordAndCustom.z;
                    UNITY_TRANSFER_FOG(o,o.vertex);  
      
                    return o;
                }  
      
                fixed4 frag (v2f i) : SV_Target
                {
                    fixed4 col = 2.0f * i.color * _TintColor * tex2D(_MainTex, i.texcoord);
                    fixed4 col2 = fixed4(i.customData, 0, 0, col.a);
                    fixed4 final = lerp(col, col*col2, i.customData.x);  
      
                    UNITY_APPLY_FOG(i.fogCoord, final);
                    return final;
                }
                ENDCG
            }
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

