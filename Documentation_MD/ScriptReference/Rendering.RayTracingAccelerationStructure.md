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

# RayTracingAccelerationStructure

class in UnityEngine.Rendering

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

A data structure used to represent the geometry in the Scene for GPU ray
tracing.

Additional resources:
[CommandBuffer.SetRayTracingAccelerationStructure](Rendering.CommandBuffer.SetRayTracingAccelerationStructure.html),
[RayTracingShader.SetAccelerationStructure](Rendering.RayTracingShader.SetAccelerationStructure.html).

### Constructors

[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure-
ctor.html)| Creates a RayTracingAccelerationStructure with the given
RayTracingAccelerationStructure.Settings.  
---|---  
  
### Public Methods

[AddInstance](Rendering.RayTracingAccelerationStructure.AddInstance.html)|
Adds a ray tracing instance to the RayTracingAccelerationStructure.  
---|---  
[AddInstances](Rendering.RayTracingAccelerationStructure.AddInstances.html)|
Adds an array of ray tracing Mesh instances to the
RayTracingAccelerationStructure.  
[AddVFXInstances](Rendering.RayTracingAccelerationStructure.AddVFXInstances.html)|
Adds the ray tracing instances associated with a VFXRenderer to the
RayTracingAccelerationStructure.  
[Build](Rendering.RayTracingAccelerationStructure.Build.html)| Builds
acceleration structures on the GPU. Allocates any GPU memory required for
storing acceleration structure data.  
[ClearInstances](Rendering.RayTracingAccelerationStructure.ClearInstances.html)|
Removes all ray tracing instances from the RayTracingAccelerationStructure.  
[CullInstances](Rendering.RayTracingAccelerationStructure.CullInstances.html)|
Populates the RayTracingAccelerationStructure with ray tracing instances that
Unity associates with Renderers in the Scene by using filtering and culling
parameters.  
[Dispose](Rendering.RayTracingAccelerationStructure.Dispose.html)| Destroys
this RayTracingAccelerationStructure and frees the GPU memory used for storing
acceleration structure data.  
[GetInstanceCount](Rendering.RayTracingAccelerationStructure.GetInstanceCount.html)|
Returns the number of ray tracing instances in the
RayTracingAccelerationStructure.  
[GetSize](Rendering.RayTracingAccelerationStructure.GetSize.html)| Returns the
total size of this RayTracingAccelerationStructure in GPU memory in bytes.  
[Release](Rendering.RayTracingAccelerationStructure.Release.html)| Destroys
this RayTracingAccelerationStructure and frees the GPU memory used for storing
acceleration structure data.  
[RemoveInstance](Rendering.RayTracingAccelerationStructure.RemoveInstance.html)|
Removes a ray tracing instance associated with a Renderer from this
RayTracingAccelerationStructure.  
[RemoveVFXInstances](Rendering.RayTracingAccelerationStructure.RemoveVFXInstances.html)|
Remove the ray tracing instances associated with a VFXRenderer from the
RayTracingAccelerationStructure.  
[UpdateInstanceID](Rendering.RayTracingAccelerationStructure.UpdateInstanceID.html)|
Updates the instance ID of a ray tracing instance.  
[UpdateInstanceMask](Rendering.RayTracingAccelerationStructure.UpdateInstanceMask.html)|
Updates the instance mask of a ray tracing instance.  
[UpdateInstancePropertyBlock](Rendering.RayTracingAccelerationStructure.UpdateInstancePropertyBlock.html)|
Updates per ray tracing instance Material properties.  
[UpdateInstanceTransform](Rendering.RayTracingAccelerationStructure.UpdateInstanceTransform.html)|
Updates the transformation of a ray tracing instance.  
  
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

