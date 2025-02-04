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
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).AddInstance

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

public int AddInstance([Renderer](Renderer.html) targetRenderer,
RayTracingSubMeshFlags[] subMeshFlags, bool enableTriangleCulling, bool
frontTriangleCounterClockwise, uint mask, uint id);

### Parameters

targetRenderer | The Renderer to add to the RayTracingAccelerationStructure.  
---|---  
enableTriangleCulling | A bool that indicates whether front/back face culling for this ray tracing instance is enabled. The culling takes place when the GPU performs a ray-triangle intersection test. Culling is enabled (true) by default.  
frontTriangleCounterClockwise | A bool that indicates whether to flip the way triangles face in this ray tracing instance. If this is set to true, front-facing triangles will become back-facing and vice versa. Set to false by default.  
mask | An 8-bit mask you can use to selectively intersect the ray tracing instance associated with the target Renderer with rays that only pass the mask. All rays are enabled (0xff) by default.  
subMeshFlags | A list of flags that control the shader execution behaviour when a ray intersects a sub-mesh geometry. See [RayTracingSubMeshFlags](Rendering.RayTracingSubMeshFlags.html) for additional information.  
id | An optional instance ID value accessed with `InstanceID()` HLSL function.  
  
### Returns

**int** A value representing a handle that you can use to perform later
actions (e.g. RemoveInstance).

### Description

Adds a ray tracing instance to the RayTracingAccelerationStructure.

Ray tracing instances in the acceleration structure contain an 8-bit user
defined instance mask. The `TraceRay()` HLSL function has an 8-bit input
parameter, `InstanceInclusionMask` which gets ANDed with the instance mask
from any ray tracing instance that is a candidate for intersection during
acceleration structure traversal on the GPU. If the result of the AND
operation is zero, the intersection is ignored.  
  
When you have added all required instances, use
[RayTracingAccelerationStructure.Build](Rendering.RayTracingAccelerationStructure.Build.html)
or
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)
to build the acceleration structure on the GPU.  
  
Additional resources:
[RayTracingAccelerationStructure.RemoveInstance](Rendering.RayTracingAccelerationStructure.RemoveInstance.html),
[RayTracingSubMeshFlags](Rendering.RayTracingSubMeshFlags.html).

* * *

## Declaration

public int AddInstance(ref
[Rendering.RayTracingMeshInstanceConfig](Rendering.RayTracingMeshInstanceConfig.html)
config, [Matrix4x4](Matrix4x4.html) matrix, Nullable<Matrix4x4> prevMatrix =
null, uint id);

### Parameters

config | The common parameters that this Mesh ray tracing instance uses.  
---|---  
matrix | The transformation matrix of the ray tracing instance.  
prevMatrix | The previous frame transformation matrix of the ray tracing instance that you can use to compute motion vectors in shader code.  
id | An optional instance ID value that you can access with `InstanceID()` HLSL function.  
  
### Returns

**int** A value representing a handle that you can use to perform later
actions (e.g. RemoveInstance, UpdateInstancePropertyBlock or
UpdateInstanceTransform).

### Description

Adds a ray tracing instance associated with a [Mesh](Mesh.html) to the
RayTracingAccelerationStructure.

The config function argument specifies the relevant [Mesh](Mesh.html) and
associated parameters.  
  
When you have added all required instances, use
[RayTracingAccelerationStructure.Build](Rendering.RayTracingAccelerationStructure.Build.html)
or
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)
to build the acceleration structure on the GPU.  
  
Additional resources:
[RayTracingAccelerationStructure.RemoveInstance](Rendering.RayTracingAccelerationStructure.RemoveInstance.html),
[RayTracingShader.Dispatch](Rendering.RayTracingShader.Dispatch.html).

* * *

## Declaration

public int AddInstance(ref
[Rendering.RayTracingGeometryInstanceConfig](Rendering.RayTracingGeometryInstanceConfig.html)
config, [Matrix4x4](Matrix4x4.html) matrix, Nullable<Matrix4x4> prevMatrix =
null, uint id);

### Parameters

config | The common parameters that this geometry ray tracing instance uses.  
---|---  
matrix | The transformation matrix of the ray tracing instance.  
prevMatrix | The previous frame transformation matrix of the ray tracing instance that you can use to compute motion vectors in shader code.  
id | An optional instance ID value that you can access with `InstanceID()` HLSL function.  
  
### Returns

**int** A value representing a handle that you can use to perform later
actions (e.g. RemoveInstance, UpdateInstancePropertyBlock or
UpdateInstanceTransform).

### Description

Adds a ray tracing instance to the RayTracingAccelerationStructure.

The config function argument specifies the relevant triangle geometry data
(vertex and index buffers) and associated parameters.  
  
When you have added all required instances, use
[RayTracingAccelerationStructure.Build](Rendering.RayTracingAccelerationStructure.Build.html)
or
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)
to build the acceleration structure on the GPU.  
  
Additional resources:
[RayTracingAccelerationStructure.RemoveInstance](Rendering.RayTracingAccelerationStructure.RemoveInstance.html),
[RayTracingShader.Dispatch](Rendering.RayTracingShader.Dispatch.html).

* * *

## Declaration

public int
AddInstance([Rendering.RayTracingAABBsInstanceConfig](Rendering.RayTracingAABBsInstanceConfig.html)
config, [Matrix4x4](Matrix4x4.html) matrix, uint id);

### Parameters

config | The common parameters that this AABBs ray tracing instance uses.  
---|---  
matrix | The transformation matrix of the ray tracing instance.  
id | An optional instance ID value that you can access with `InstanceID()` HLSL function.  
  
### Returns

**int** A value representing a handle that can be used to perform later
actions (e.g. RemoveInstance, UpdateInstancePropertyBlock or
UpdateInstanceTransform).

### Description

Adds a ray tracing instance associated with a list of axis-aligned bounding
boxes (AABBs) to the RayTracingAccelerationStructure for procedural geometry
generation using intersection shaders.

Define the AABB list in the [GraphicsBuffer](GraphicsBuffer.html) you set the
[config.aabbBuffer](Rendering.RayTracingAABBsInstanceConfig-aabbBuffer.html)
parameter to. Unity uses the AABBs to build an acceleration structure for this
ray tracing instance.  
  
The AABBs are defined in local space and can be transformed using the matrix
argument. Use
[RayTracingAccelerationStructure.UpdateInstanceTransform](Rendering.RayTracingAccelerationStructure.UpdateInstanceTransform.html)
to update the transformation of the ray tracing instance at a later time.  
  
Unity copies the contents of the
[MaterialPropertyBlock](MaterialPropertyBlock.html) in the
[config.materialProperties](Rendering.RayTracingAABBsInstanceConfig-
materialProperties.html) parameter into the ray tracing instance when this
function is called. Any subsequent changes to the
[MaterialPropertyBlock](MaterialPropertyBlock.html) object that was passed as
argument are not taken into account. Use
[RayTracingAccelerationStructure.UpdateInstancePropertyBlock](Rendering.RayTracingAccelerationStructure.UpdateInstancePropertyBlock.html)
to updated the properties again at a later time.  
  
When a ray intersects one of the AABBs in the list during a ray tracing
dispatch, the GPU invokes an intersection shader. You can retrieve the index
of a discrete AABB in the acceleration structure with the `PrimitiveIndex()`
HLSL function.  
  
When you have added all required instances, use
[RayTracingAccelerationStructure.Build](Rendering.RayTracingAccelerationStructure.Build.html)
or
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)
to build the acceleration structure on the GPU.  
  
Additional resources:
[RayTracingAccelerationStructure.RemoveInstance](Rendering.RayTracingAccelerationStructure.RemoveInstance.html),
[RayTracingShader.Dispatch](Rendering.RayTracingShader.Dispatch.html).

* * *

**Obsolete** This AddInstance method is deprecated and will be removed and it
will be removed in Unity 2024.1. Please use the alternative AddInstance method
for adding Renderers to the acceleration structure.

## Declaration

public void AddInstance([Renderer](Renderer.html) targetRenderer, bool[]
subMeshMask, bool[] subMeshTransparencyFlags, bool enableTriangleCulling, bool
frontTriangleCounterClockwise, uint mask, uint id);

### Description

Deprecated. Please use the alternate method for adding Renderers to the
acceleration structure.

* * *

**Obsolete** This AddInstance method is deprecated and it will be removed in
Unity 2024.1. Please use the alternative AddInstance method for adding
procedural geometry (AABBs) to the acceleration structure.

## Declaration

public void AddInstance([GraphicsBuffer](GraphicsBuffer.html) aabbBuffer, uint
numElements, [Material](Material.html) material, bool isCutOff, bool
enableTriangleCulling, bool frontTriangleCounterClockwise, uint mask, bool
reuseBounds, uint id);

### Description

Deprecated. Please use the alternate method for adding procedural geometry
(AABBs) to the acceleration structure.

* * *

**Obsolete** This AddInstance method is deprecated and it will be removed in
Unity 2024.1. Please use the alternative AddInstance method for adding
procedural geometry (AABBs) to the acceleration structure.

## Declaration

public int AddInstance([GraphicsBuffer](GraphicsBuffer.html) aabbBuffer, uint
aabbCount, bool dynamicData, [Matrix4x4](Matrix4x4.html) matrix,
[Material](Material.html) material, bool opaqueMaterial,
[MaterialPropertyBlock](MaterialPropertyBlock.html) properties, uint mask,
uint id);

### Description

Deprecated. Please use the alternate method for adding procedural geometry
(AABBs) to the acceleration structure.

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

