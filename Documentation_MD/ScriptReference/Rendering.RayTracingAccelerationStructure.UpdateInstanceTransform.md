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
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).UpdateInstanceTransform

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

public void UpdateInstanceTransform([Renderer](Renderer.html) renderer);

### Parameters

renderer | The Renderer associated with a ray tracing instance.  
---|---  
  
### Description

Updates the transformation of a ray tracing instance.

For a ray tracing instance associated with a Renderer component, Unity
retrieves the transformation from the Transform component.

* * *

## Declaration

public void UpdateInstanceTransform(int handle, [Matrix4x4](Matrix4x4.html)
matrix);

### Parameters

handle | The handle associated with a AABB or Mesh ray tracing instance.  
---|---  
matrix | The new transformation matrix of the ray tracing instance.  
  
### Description

Updates the transformation of a ray tracing instance.

Pass along a new transformation matrix and the handle
[RayTracingAccelerationStructure.AddInstance](Rendering.RayTracingAccelerationStructure.AddInstance.html)
returns in order to transform a ray tracing instance associated with a axis-
aligned bounding box (AABB) [GraphicsBuffer](GraphicsBuffer.html) or a
[Mesh](Mesh.html).  
  
Access the transformation matrix in shader code using `WorldToObject()` or
`ObjectToWorld()` HLSL functions.  
  
To trigger an acceleration structure build on the GPU, call
[RayTracingAccelerationStructure.Build](Rendering.RayTracingAccelerationStructure.Build.html)
or
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html).  
  
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

