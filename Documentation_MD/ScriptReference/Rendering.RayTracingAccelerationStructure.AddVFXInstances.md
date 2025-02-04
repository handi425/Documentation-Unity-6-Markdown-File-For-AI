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
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).AddVFXInstances

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

public void AddVFXInstances([Renderer](Renderer.html) targetRenderer, uint[]
vfxSystemMasks);

### Parameters

targetRenderer | The Renderer to add to the RayTracingAccelerationStructure.  
---|---  
vfxSystemMasks | An array of 8-bit masks you can use to selectively intersect ray-traced VFX systems associated with the target Renderer with rays that only pass the mask. All rays are enabled (0xff) by default.  
  
### Description

Adds the ray tracing instances associated with a VFXRenderer to the
RayTracingAccelerationStructure.

Ray tracing instances in the acceleration structure contain an 8-bit user
defined instance mask. The `TraceRay()` HLSL function has an 8-bit input
parameter, `InstanceInclusionMask` which gets ANDed with the instance mask
from any ray tracing instance that is a candidate for intersection during
acceleration structure traversal on the GPU. If the result of the AND
operation is zero, the intersection is ignored.  
  
One VFXRenderer can have more than one ray tracing instance if it contains
multiple output contexts. This method adds all the instances of outputs which
enable ray tracing, with the masks specified in vfxSystemMasks.

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

