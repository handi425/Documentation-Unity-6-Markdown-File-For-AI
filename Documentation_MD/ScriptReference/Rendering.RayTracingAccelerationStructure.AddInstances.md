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
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).AddInstances

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

public int AddInstances(ref
[Rendering.RayTracingMeshInstanceConfig](Rendering.RayTracingMeshInstanceConfig.html)
config, T[] instanceData, int instanceCount = -1, int startInstance = 0, uint
id);

## Declaration

public int AddInstances(ref
[Rendering.RayTracingMeshInstanceConfig](Rendering.RayTracingMeshInstanceConfig.html)
config, List<T> instanceData, int instanceCount = -1, int startInstance = 0,
uint id);

## Declaration

public int AddInstances(ref
[Rendering.RayTracingMeshInstanceConfig](Rendering.RayTracingMeshInstanceConfig.html)
config, NativeArray<T> instanceData, int instanceCount = -1, int startInstance
= 0, uint id);

## Declaration

public int AddInstances(ref
[Rendering.RayTracingMeshInstanceConfig](Rendering.RayTracingMeshInstanceConfig.html)
config, NativeSlice<T> instanceData, uint id);

### Parameters

config | The common parameters this array of ray tracing Mesh instance uses.  
---|---  
instanceData | An array of instance data used by the ray tracing Mesh instances.  
instanceCount | The number of instances to add to the acceleration structure. When this argument is -1 (default), Unity adds all the instances from the startInstance to the end of the instanceData array.  
startInstance | The first instance in the instanceData to add to the acceleration structure.  
id | An optional instance ID value that you can access in HLSL with the `InstanceID()` function. Unity assigns consecutive instance IDs to each mesh instance, starting with the value of `id`.  
  
### Returns

**int** A value which represents a handle you can use to perform later actions
(e.g. RemoveInstance, UpdateInstancePropertyBlock).

### Description

Adds an array of ray tracing Mesh instances to the
RayTracingAccelerationStructure.

The passed instanceData can either be an array of [Matrix4x4](Matrix4x4.html)
(object-to-world transformation per instance) or a custom data structure. When
the instanceData is a custom data structure, the structure can contain the
following members:

  * **Matrix4x4 objectToWorld** (mandatory) - specifies per-instance object-to-world transformation matrix
  * **uint renderingLayerMask** (optional) - specifies per-instance rendering layer mask
  * **Matrix4x4 prevObjectToWorld** (optional) - specifies per-instance previous frame object-to-world transformation matrix (used for motion vector calculation)

These members can appear in any order in the structure, but they must have the
above name and type. AddInstances ignores any other members you include in the
structure for your own use. The following example of a custom structure
defines the mandatory objectToWorld member, an optional renderingLayerMask
member, and a custom weight member (the AddInstances function ignores this
member).

    
    
    struct MyInstanceData
    {
        public [Matrix4x4](Matrix4x4.html) objectToWorld; // We must specify object-to-world transformation for each instance
        public uint renderingLayerMask; // Optional per-instance rendering layer mask.
        public float weight; // Additional per-instance data unrelated to rendering.
    };

For optimal CPU performance, MyInstanceData should contain objectToWorld
member only, otherwise Unity must deinterleave the data.  
  
When AddInstances is in use, Unity enables `INSTANCING_ON` shader keyword. To
declare the shader keyword in HLSL, add `#pragma multi_compile _
INSTANCING_ON` in the Shader Pass specified in
[RayTracingShader.SetShaderPass](Rendering.RayTracingShader.SetShaderPass.html)
or
[CommandBuffer.SetRayTracingShaderPass](Rendering.CommandBuffer.SetRayTracingShaderPass.html).
To access per-instance data relative to this array of ray tracing instances,
use `InstanceIndex() - unity_BaseInstanceID` as an instance index in HLSL. For
example, if prevObjectToWorld member is present in MyInstanceData structure,
Unity copies the values into `unity_PrevObjectToWorldArray` buffer which you
can define in HLSL as `StructuredBuffer<float4x4>
unity_PrevObjectToWorldArray;` You can then index the buffer using
`InstanceIndex() - unity_BaseInstanceID` difference. The following HLSL code
snippet demonstrates how to compute a world-space velocity vector which is
output in the ray payload:

    
    
    #pragma multi_compile _ INSTANCING_ON  
      
    struct AttributeData
    {
        float2 barycentrics;
    };  
      
    struct RayPayload
    {
        float3 velocity;
    };  
      
    // Built-in shader variables:
    StructuredBuffer<float4x4> unity_PrevObjectToWorldArray;
    float4x4 unity_MatrixPreviousM;
    uint unity_BaseInstanceID;  
      
    static uint unity_InstanceID;  
      
    [shader("closesthit")]
    void ClosestHitMain(inout RayPayload payload, AttributeData attribs)
    {
       float3 localPos = ObjectRayOrigin() + RayTCurrent() * ObjectRayDirection();  
      
    #if INSTANCING_ON
        unity_InstanceID = InstanceIndex() - unity_BaseInstanceID;
     
        float3 prevWorldPos = mul(unity_PrevObjectToWorldArray[unity_InstanceID], float4(localPos, 1)).xyz;
    #else
        float3 prevWorldPos = mul(unity_MatrixPreviousM, float4(localPos, 1)).xyz;
    #endif
        float3 worldPos = WorldRayOrigin() + RayTCurrent() * WorldRayDirection();  
      
        payload.velocity = worldPos - prevWorldPos;
    }

Depending on the parameters in config argument and the instanceData custom
structure, AddInstances will set up and bind the following built-in
StructuredBuffers to hit shaders:

  * `unity_PrevObjectToWorldArray` (float4x4) - when prevObjectToWorld member is present in instanceData custom structure.
  * `unity_RenderingLayerArray` (float) - when renderingLayerMask member is present in instanceData custom structure.
  * `unity_SHArArray`, `unity_SHAgArray`, `unity_SHAbArray`, `unity_SHBrArray`, `unity_SHBgArray`, `unity_SHBbArray`, `unity_SHCArray` (float4) - spherical harmonics coefficients (used by ambient and light probes) when config.lightProbeUsage is [LightProbeUsage.Off](Rendering.LightProbeUsage.Off.html) (ambient probe only), [LightProbeUsage.BlendProbes](Rendering.LightProbeUsage.BlendProbes.html) or [LightProbeUsage.UseProxyVolume](Rendering.LightProbeUsage.UseProxyVolume.html) (when config.lightProbeProxyVolume.qualityMode is set to [LightProbeProxyVolume.QualityMode.Normal](LightProbeProxyVolume.QualityMode.Normal.html)).

Note that AddInstances doesn't set up and bind `unity_ObjectToWorldArray` or
`unity_WorldToObjectArray` buffers since you can access the ray tracing
instance transformation matrices in hit shaders using `ObjectToWorld()` or
`WorldToObject()` HLSL intrinsics.  
  
You can use this function to add a maximum of 1048575 ray tracing Mesh
instances. The final instance count depends on both startInstance and
instanceCount arguments. You can access the instance count in HLSL using
`unity_InstanceCount` built-in uniform.  
  
AddInstances throws InvalidOperationException if the Material specified in the
config argument doesn't have [Material.enableInstancing](Material-
enableInstancing.html) set to true. When you have added all required
instances, use
[RayTracingAccelerationStructure.Build](Rendering.RayTracingAccelerationStructure.Build.html)
or
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)
to build the acceleration structure on the GPU.  
  
This functionality doesn't have any special hardware requirements in addition
to ray tracing support ([SystemInfo.supportsRayTracing](SystemInfo-
supportsRayTracing.html) must be true). In DirectX Raytracing (DXR), this
function causes all ray tracing instances in the array to use only one shader
record from the shader table, thus reducing the CPU overhead on the render
thread for binding GPU resources to hit shaders.  
  
Additional resources:
[RayTracingAccelerationStructure.AddInstance](Rendering.RayTracingAccelerationStructure.AddInstance.html),
[RayTracingAccelerationStructure.RemoveInstance](Rendering.RayTracingAccelerationStructure.RemoveInstance.html).

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

