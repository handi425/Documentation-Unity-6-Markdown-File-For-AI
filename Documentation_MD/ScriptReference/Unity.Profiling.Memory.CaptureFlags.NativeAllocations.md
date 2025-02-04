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

#  [CaptureFlags](Unity.Profiling.Memory.CaptureFlags.html).NativeAllocations

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

Specifies that the Native Memory used by any Native Allocation made by Unity
should be captured.

This information allows the Memory Profiler to show not just the native size
of Unity Objects, but also their graphics sizes. Additionally, this also
includes information on native memory used by Unity's different subsystems,
allocations made via
[UnsafeUtility.Malloc](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html),
NativeArray_1 or other native collections, as well as how much memory is used
by Unity's different [native allocators](../Manual/performance-native-
allocators.html) and how much is just reserved. Without this flag, there will
be no data recorded for
[CaptureFlags.NativeAllocationSites](Unity.Profiling.Memory.CaptureFlags.NativeAllocationSites.html)
or
[CaptureFlags.NativeStackTraces](Unity.Profiling.Memory.CaptureFlags.NativeStackTraces.html)
either as it is reported in relation to each native alloation.  
  
Corresponds to the NativeAllocations, NativeMemoryRegions,
NativeRootReferences, and NativeMemoryLabels fields in a Memory Snapshot.

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

