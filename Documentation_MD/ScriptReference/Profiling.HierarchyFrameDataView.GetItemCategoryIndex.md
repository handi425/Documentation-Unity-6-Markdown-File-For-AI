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
[HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html).GetItemCategoryIndex

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

public ushort GetItemCategoryIndex(int id);

### Parameters

id | Hierarchy item identifier.  
---|---  
  
### Returns

**ushort** Returns Profiler category index.

### Description

Gets Profiler marker category for the specific marker identifier.

Use Profiler category to filter samples produced by a specific subsystem, e.g.
Rendering, Audio.  
The category index is represented by _ushort_ value and refers to one of the
following constants in
[ProfilerUnsafeUtility](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html)
class:

  * [ProfilerUnsafeUtility.CategoryRender](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryRender.html),
  * [ProfilerUnsafeUtility.CategoryScripts](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html),
  * [ProfilerUnsafeUtility.CategoryGUI](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryGUI.html),
  * [ProfilerUnsafeUtility.CategoryPhysics](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryPhysics.html),
  * [ProfilerUnsafeUtility.CategoryAnimation](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAnimation.html),
  * [ProfilerUnsafeUtility.CategoryAi](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAi.html),
  * [ProfilerUnsafeUtility.CategoryAudio](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAudio.html),
  * [ProfilerUnsafeUtility.CategoryVideo](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVideo.html),
  * [ProfilerUnsafeUtility.CategoryParticles](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryParticles.html),
  * ProfilerUnsafeUtility.CategoryLightning,
  * [ProfilerUnsafeUtility.CategoryNetwork](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryNetwork.html),
  * [ProfilerUnsafeUtility.CategoryLoading](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryLoading.html),
  * [ProfilerUnsafeUtility.CategoryOther](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryOther.html),
  * [ProfilerUnsafeUtility.CategoryVr](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVr.html),
  * [ProfilerUnsafeUtility.CategoryAllocation](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAllocation.html),
  * [ProfilerUnsafeUtility.CategoryVr](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVr.html),
  * [ProfilerUnsafeUtility.CategoryInput](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryInput.html).

Additional resources:
[FrameDataView.GetMarkerId](Profiling.FrameDataView.GetMarkerId.html),
[ProfilerUnsafeUtility](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html).

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

