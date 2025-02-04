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

#  [Graphics](Graphics.html).RenderPrimitives

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

public static void RenderPrimitives(ref [RenderParams](RenderParams.html)
rparams, [MeshTopology](MeshTopology.html) topology, int vertexCount, int
instanceCount = 1);

### Parameters

rparams | The parameters Unity uses to render the primitives.  
---|---  
topology | Primitive topology (for example, triangles or lines).  
vertexCount | The number of vertices per instance.  
instanceCount | The number of instances to render.  
  
### Description

Renders non-indexed primitives with GPU instancing and a custom shader.

Renders a given number of instances and primitives that have specific
topology. This method requires custom shaders to fetch or calculate vertex
data using the `SV_VertexID` semantic. To access instance ID use
`SV_InstanceID` semantic.  
  
Additional resources:
[RenderPrimitivesIndexed](Graphics.RenderPrimitivesIndexed.html).  
  
The following example renders 10 instances of a Mesh using the function. The
associated Material must use the below custom shader:

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Material](Material.html) material;
        public [Mesh](Mesh.html) mesh;  
      
        [GraphicsBuffer](GraphicsBuffer.html) meshTriangles;
        [GraphicsBuffer](GraphicsBuffer.html) meshPositions;  
      
        void Start()
        {
            // note: remember to check "Read/Write" on the mesh asset to get access to the geometry data
            meshTriangles = new [GraphicsBuffer](GraphicsBuffer.html)([GraphicsBuffer.Target.Structured](GraphicsBuffer.Target.Structured.html), mesh.triangles.Length, sizeof(int));
            meshTriangles.SetData(mesh.triangles);
            meshPositions = new [GraphicsBuffer](GraphicsBuffer.html)([GraphicsBuffer.Target.Structured](GraphicsBuffer.Target.Structured.html), mesh.vertices.Length, 3 * sizeof(float));
            meshPositions.SetData(mesh.vertices);
        }  
      
        void OnDestroy()
        {
            meshTriangles?.Dispose();
            meshTriangles = null;
            meshPositions?.Dispose();
            meshPositions = null;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [RenderParams](RenderParams.html) rp = new [RenderParams](RenderParams.html)(material);
            rp.worldBounds = new [Bounds](Bounds.html)([Vector3.zero](Vector3-zero.html), 10000*[Vector3.one](Vector3-one.html)); // use tighter bounds
            rp.matProps = new [MaterialPropertyBlock](MaterialPropertyBlock.html)();
            rp.matProps.SetBuffer("_Triangles", meshTriangles);
            rp.matProps.SetBuffer("_Positions", meshPositions);
            rp.matProps.SetInt("_StartIndex", (int)mesh.GetIndexStart(0));
            rp.matProps.SetInt("_BaseVertexIndex", (int)mesh.GetBaseVertex(0));
            rp.matProps.SetMatrix("_ObjectToWorld", [Matrix4x4.Translate](Matrix4x4.Translate.html)(new [Vector3](Vector3.html)(-4.5f, 0, 0)));
            rp.matProps.SetFloat("_NumInstances", 10.0f);
            [Graphics.RenderPrimitives](Graphics.RenderPrimitives.html)(rp, [MeshTopology.Triangles](MeshTopology.Triangles.html), (int)mesh.GetIndexCount(0), 10);
        }
    }

Use the following example shader with the above C# example code:

    
    
              [Shader](Shader.html) "ExampleShader"
    {
        SubShader
        {
            [Pass](ShaderData.Pass.html)
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag  
      
                #include "UnityCG.cginc"  
      
                struct v2f
                {
                    float4 pos : SV_POSITION;
                    float4 color : COLOR0;
                };  
      
                StructuredBuffer<int> _Triangles;
                StructuredBuffer<float3> _Positions;
                uniform uint _StartIndex;
                uniform uint _BaseVertexIndex;
                uniform float4x4 _ObjectToWorld;
                uniform float _NumInstances;  
      
                v2f vert(uint vertexID: SV_VertexID, uint instanceID : SV_InstanceID)
                {
                    v2f o;
                    float3 pos = _Positions[_Triangles[vertexID + _StartIndex] + _BaseVertexIndex];
                    float4 wpos = mul(_ObjectToWorld, float4(pos + float3(instanceID, 0, 0), 1.0f));
                    o.pos = mul(UNITY_MATRIX_VP, wpos);
                    o.color = float4(instanceID / _NumInstances, 0.0f, 0.0f, 0.0f);
                    return o;
                }  
      
                float4 frag(v2f i) : SV_Target
                {
                    return i.color;
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

