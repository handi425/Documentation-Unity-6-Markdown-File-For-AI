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

# RayTracingGeometryInstanceConfig

struct in UnityEngine.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Parameters you can use to configure ray tracing triangle geometry instances
that are part of a
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).

The triangle geometry is specified using
[GraphicsBuffers](GraphicsBuffer.html) containing vertex and index data and
additional parameters.

### Properties

[accelerationStructureBuildFlags](Rendering.RayTracingGeometryInstanceConfig-
accelerationStructureBuildFlags.html)| The flags Unity uses when it builds the
acceleration structure for the geometry referenced by this ray tracing
instance configuration.  
---|---  
[accelerationStructureBuildFlagsOverride](Rendering.RayTracingGeometryInstanceConfig-
accelerationStructureBuildFlagsOverride.html)| Whether to override the build
flags specified when creating a RayTracingAccelerationStructure.  
[dynamicGeometry](Rendering.RayTracingGeometryInstanceConfig-
dynamicGeometry.html)| Whether Unity considers the geometry animated or not.  
[enableTriangleCulling](Rendering.RayTracingGeometryInstanceConfig-
enableTriangleCulling.html)| Whether front/back face culling for this ray
tracing instance is enabled.  
[frontTriangleCounterClockwise](Rendering.RayTracingGeometryInstanceConfig-
frontTriangleCounterClockwise.html)| Whether to flip the way triangles face in
this ray tracing instance.  
[indexBuffer](Rendering.RayTracingGeometryInstanceConfig-indexBuffer.html)|
The index buffer that Unity uses to define the ray tracing geometry instance.  
[indexCount](Rendering.RayTracingGeometryInstanceConfig-indexCount.html)| The
amount of indices from indexBuffer that defines this ray tracing geometry
instance.  
[indexStart](Rendering.RayTracingGeometryInstanceConfig-indexStart.html)| The
first index from indexBuffer that defines this ray tracing geometry instance.  
[layer](Rendering.RayTracingGeometryInstanceConfig-layer.html)| The Layer used
by the ray tracing instance.  
[lightProbeProxyVolume](Rendering.RayTracingGeometryInstanceConfig-
lightProbeProxyVolume.html)| The LightProbeProxyVolume the ray tracing
instance uses.  
[lightProbeUsage](Rendering.RayTracingGeometryInstanceConfig-
lightProbeUsage.html)| The Light probe interpolation type for this instance.  
[mask](Rendering.RayTracingGeometryInstanceConfig-mask.html)| The ray tracing
instance mask.  
[material](Rendering.RayTracingGeometryInstanceConfig-material.html)| The
Material the ray tracing instance uses.  
[materialProperties](Rendering.RayTracingGeometryInstanceConfig-
materialProperties.html)| Additional Material properties to apply onto
Material.  
[motionVectorMode](Rendering.RayTracingGeometryInstanceConfig-
motionVectorMode.html)| Motion vector mode.  
[renderingLayerMask](Rendering.RayTracingGeometryInstanceConfig-
renderingLayerMask.html)| A mask that you can access in HLSL with
unity_RenderingLayer built-in shader uniform.  
[subMeshFlags](Rendering.RayTracingGeometryInstanceConfig-subMeshFlags.html)|
Flags that determine the ray-geometry intersection behavior relative to
Material type during ray tracing.  
[vertexAttributes](Rendering.RayTracingGeometryInstanceConfig-
vertexAttributes.html)| An array of vertex attributes that define the vertex
format of vertexBuffer.  
[vertexBuffer](Rendering.RayTracingGeometryInstanceConfig-vertexBuffer.html)|
The vertex buffer that Unity uses to define the ray tracing geometry instance.  
[vertexCount](Rendering.RayTracingGeometryInstanceConfig-vertexCount.html)|
The amount of vertices from vertexBuffer that defines this ray tracing
geometry instance.  
[vertexStart](Rendering.RayTracingGeometryInstanceConfig-vertexStart.html)|
The index of the first vertex from vertexBuffer that defines this ray tracing
geometry instance.  
  
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

