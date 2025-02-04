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

#  [Shader](Shader.html).SetGlobalRayTracingAccelerationStructure

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

[Switch to Manual](../Manual/class-Shader.html "Go to Shader Component in the
Manual")

## Declaration

public static void SetGlobalRayTracingAccelerationStructure(string name,
[Rendering.RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)
value);

## Declaration

public static void SetGlobalRayTracingAccelerationStructure(int nameID,
[Rendering.RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)
value);

### Parameters

name | The name of the acceleration structure in shader code.  
---|---  
nameID | The name ID of the acceleration structure in shader code. Use [Shader.PropertyToID](Shader.PropertyToID.html) to get this value.  
value | The acceleration structure to set.  
  
### Description

Sets a global
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)
property for all shaders.

This command binds a
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)
object to all shader stages. You can use the acceleration structure for inline
ray tracing (ray queries) or as an argument in `TraceRay` calls in ray tracing
shaders. The
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)
object must be built using the
[RayTracingAccelerationStructure.Build](Rendering.RayTracingAccelerationStructure.Build.html)
method before calling this command.  
  
Ray queries can be used to perform acceleration structure traversal and
geometry intersection tests. To access this functionality, the HLSL code must
be compiled using the `#pragma require inlineraytracing` directive or by using
the built-in shader keyword `UNITY_DEVICE_SUPPORTS_INLINE_RAY_TRACING` (for
example, #pragma multi_compile _ UNITY_DEVICE_SUPPORTS_INLINE_RAY_TRACING).  
  
Additional resources:
[CommandBuffer.SetGlobalRayTracingAccelerationStructure](Rendering.CommandBuffer.SetGlobalRayTracingAccelerationStructure.html),
[SystemInfo.supportsRayTracingShaders](SystemInfo-
supportsRayTracingShaders.html),
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

