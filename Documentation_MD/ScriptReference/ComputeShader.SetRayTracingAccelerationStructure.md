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

#  [ComputeShader](ComputeShader.html).SetRayTracingAccelerationStructure

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

[Switch to Manual](../Manual/class-ComputeShader.html "Go to ComputeShader
Component in the Manual")

## Declaration

public void SetRayTracingAccelerationStructure(int kernelIndex, int nameID,
[Rendering.RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)
accelerationStructure);

## Declaration

public void SetRayTracingAccelerationStructure(int kernelIndex, string name,
[Rendering.RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)
accelerationStructure);

### Parameters

kernelIndex | For which kernel the [RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html) is being set. See [FindKernel](ComputeShader.FindKernel.html).  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
accelerationStructure | The [RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html) object to bind.  
name | Resource name in shader code.  
  
### Description

Sets a
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)
to be used for Inline Ray Tracing (Ray Queries).

Use [SystemInfo.supportsInlineRayTracing](SystemInfo-
supportsInlineRayTracing.html) to check at runtime if Inline Ray Tracing is
supported by the system.  
  
In compute shaders, ray queries can be used to perform acceleration structure
traversal and geometry intersection tests. To access this functionality, the
HLSL code needs to be compiled using `#pragma require inlineraytracing`.

    
    
    #include "UnityRayQuery.cginc"  
      
    #pragma require inlineraytracing
    #pragma kernel CSRayQueryTest  
      
    RaytracingAccelerationStructure g_AccelStruct;
    RWTexture2D<float> g_Output;  
      
    [numthreads(8,4,1)]
    void CSRayQueryTest (uint3 id : SV_DispatchThreadID)
    {
        const uint rayFlags = RAY_FLAG_ACCEPT_FIRST_HIT_AND_END_SEARCH;
        UnityRayQuery<rayFlags> rayQuery;  
      
        RayDesc ray;
        ray.Origin = float3(0, 0, 0);
        ray.Direction = float3(0, 1, 0);
        ray.TMin = 0;
        ray.TMax = 10000;  
      
        rayQuery.TraceRayInline(g_AccelStruct, rayFlags, 0xff, ray);
        rayQuery.Proceed();  
      
        g_Output[id.xy] = (rayQuery.CommittedStatus() == COMMITTED_TRIANGLE_HIT) ? 1.0 : 0.0;
    }

This is a simple compute shader that checks if a ray with the origin at (0, 0,
0) and direction (0, 1, 0) intersects any geometry consisting of triangles.
The `g_AccelStruct` shader object can be bound using the
SetRayTracingAccelerationStructure function. The compute shader can be
dispatched if [SystemInfo.supportsInlineRayTracing](SystemInfo-
supportsInlineRayTracing.html) is true.  
  
Additional resources:
[CommandBuffer.SetGlobalRayTracingAccelerationStructure](Rendering.CommandBuffer.SetGlobalRayTracingAccelerationStructure.html),
[SystemInfo.supportsInlineRayTracing](SystemInfo-
supportsInlineRayTracing.html).

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

