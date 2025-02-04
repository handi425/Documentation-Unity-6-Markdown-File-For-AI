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

# RayTracingAABBsInstanceConfig

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

The parameters you use to add an instance of ray tracing axis-aligned bounding
boxes (AABBs) to a
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).

Use this structure to share parameters across different ray tracing AABBs
instances.  
  
Additional resources:
[RayTracingAccelerationStructure.AddInstance](Rendering.RayTracingAccelerationStructure.AddInstance.html),
[RayTracingAccelerationStructure.RemoveInstance](Rendering.RayTracingAccelerationStructure.RemoveInstance.html).

### Properties

[aabbBuffer](Rendering.RayTracingAABBsInstanceConfig-aabbBuffer.html)| The
GraphicsBuffer that defines a list of axis-aligned bounding boxes (AABBs).  
---|---  
[aabbCount](Rendering.RayTracingAABBsInstanceConfig-aabbCount.html)| The
number of AABBs Unity uses when you build the acceleration structure for this
ray tracing instance.  
[aabbOffset](Rendering.RayTracingAABBsInstanceConfig-aabbOffset.html)| The
index of the first AABB Unity uses from
RayTracingAABBsInstanceConfig.aabbBuffer.  
[accelerationStructureBuildFlags](Rendering.RayTracingAABBsInstanceConfig-
accelerationStructureBuildFlags.html)| The flags Unity uses when it builds the
acceleration structure for the geometry referenced by this ray tracing
instance configuration.  
[accelerationStructureBuildFlagsOverride](Rendering.RayTracingAABBsInstanceConfig-
accelerationStructureBuildFlagsOverride.html)| Whether to override the build
flags specified when creating a RayTracingAccelerationStructure.  
[dynamicGeometry](Rendering.RayTracingAABBsInstanceConfig-
dynamicGeometry.html)| Whether the data in
RayTracingAABBsInstanceConfig.aabbBuffer is dynamic.  
[layer](Rendering.RayTracingAABBsInstanceConfig-layer.html)| The Layer used by
the ray tracing instance.  
[mask](Rendering.RayTracingAABBsInstanceConfig-mask.html)| The ray tracing
instance mask.  
[material](Rendering.RayTracingAABBsInstanceConfig-material.html)| The
Material the ray tracing instance uses.  
[materialProperties](Rendering.RayTracingAABBsInstanceConfig-
materialProperties.html)| Additional MaterialPropertyBlock properties to apply
to the Material.  
[opaqueMaterial](Rendering.RayTracingAABBsInstanceConfig-opaqueMaterial.html)|
Determines whether Unity considers the material opaque.  
  
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

