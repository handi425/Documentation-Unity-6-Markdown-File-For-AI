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
[RayTracingInstanceCullingConfig](Rendering.RayTracingInstanceCullingConfig.html).instanceTests

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

public RayTracingInstanceCullingTest[] instanceTests;

### Description

An array of
[RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html)
objects used add Renderers to the acceleration structure based on their layer,
[ShadowCastingMode](Rendering.ShadowCastingMode.html) and Material type.

Typically, each ray tracing effect can use a dedicated
[RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html)
configuration. If the array is empty then
[RayTracingAccelerationStructure.CullInstances](Rendering.RayTracingAccelerationStructure.CullInstances.html)
doesn't have any effect.  
  
For each test that passes, its instanceMask value will be ORed into a final
8-bit ray tracing instance mask. When casting rays on the GPU using _TraceRay_
HLSL function, the _instanceInclusionMask_ argument of _TraceRay_ is ANDed
with the final 8-bit instance mask to include or reject ray tracing instances
during acceleration structure traversal. This way, an acceleration structure
can be used by multiple ray tracing effects, each effect potentially affecting
different Materials types or layers.  
  
Additional resources:
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).

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

