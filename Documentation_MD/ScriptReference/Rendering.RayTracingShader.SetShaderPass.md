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

#  [RayTracingShader](Rendering.RayTracingShader.html).SetShaderPass

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

public void SetShaderPass(string passName);

### Parameters

passName | The Shader Pass to use when executing ray tracing shaders.  
---|---  
  
### Description

Selects which Shader Pass to use when executing ray/geometry intersection
shaders.

This name is specified in the ShaderLab shaders used by Materials applied to
Renderers used in ray tracing. If a shader doesn't have a Shader Pass with the
specified name, then no ray/geometry intersection code is executed. This
method must be called before calling RayTracingShader.DispatchRays.  
  
The Shader Pass code can include optional closest hit or any hit shaders.  
  
For procedural ray-traced geometries, an intersection shader must be authored.
The engine code will automatically enable a keywork named
`RAY_TRACING_PROCEDURAL_GEOMETRY` if the geometry is proceduraly ray-traced.  
  
The following example shader code returns the color red.

    
    
    SubShader
    {
        [Pass](ShaderData.Pass.html)
        {
            // [RayTracingShader.SetShaderPass](Rendering.RayTracingShader.SetShaderPass.html) must use this name in order to execute the ray tracing shaders from this [Pass](ShaderData.Pass.html).
            Name "Test"  
      
            // Add tags to identify the shaders to use for ray tracing.
            Tags{ "[LightMode](Experimental.GlobalIllumination.LightMode.html)" = "RayTracing" }  
      
            HLSLPROGRAM  
      
            #pragma multi_compile_local RAY_TRACING_PROCEDURAL_GEOMETRY  
      
            // Specify this shader is a raytracing shader.
            #pragma raytracing test  
      
            struct AttributeData
            {
                float2 barycentrics;
            };  
      
            struct RayPayload
            {
                float4 color;
            };  
      
    #if RAY_TRACING_PROCEDURAL_GEOMETRY
            [shader("intersection")]
            void IntersectionMain()
            {
                AttributeData attr;
                attr.barycentrics = float2(0, 0);
                ReportHit(0, 0, attr);
            }
    #endif  
      
            [shader("closesthit")]
            void ClosestHitMain(inout RayPayload payload : SV_RayPayload, AttributeData attribs : SV_IntersectionAttributes)
            {
                payload.color = float4(1, 0, 0, 1);
            }  
      
            ENDHLSL
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

