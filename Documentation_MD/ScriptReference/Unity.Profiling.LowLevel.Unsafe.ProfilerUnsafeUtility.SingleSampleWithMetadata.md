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
[ProfilerUnsafeUtility](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html).SingleSampleWithMetadata

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

public static void SingleSampleWithMetadata(IntPtr markerPtr, int
metadataCount, void* metadata);

### Parameters

markerPtr | Profiler marker handle.  
---|---  
metadataCount | Metadata parameters count.  
metadata | Unsafe pointer to the ProfilerMarkerData array.  
  
### Description

Creates profiling sample with a custom name that the _markerPtr_ handle and
metadata parameters has defined.

Sample created with
[SingleSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.SingleSampleWithMetadata.html)
shows up as a sample with zero duration in the Profiler hierarchy. In the
Timeline view of the Profiler Window the provided _metadata_ is available in
the tooltip message. Use
[HierarchyFrameDataView.GetItemMetadata](Profiling.HierarchyFrameDataView.GetItemMetadata.html)
to retrieve metadata programmatically.  
  
If _markerPtr_ points to a marker with
[MarkerFlags.Counter](Unity.Profiling.LowLevel.MarkerFlags.Counter.html)
defined, the metadata value can be retrieved with
[FrameDataView.GetCounterValueAsInt](Profiling.FrameDataView.GetCounterValueAsInt.html)
methods.  
  
**Note:**
[SingleSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.SingleSampleWithMetadata.html)
is thread safe and can be used in jobified code.  
The low level Profiler API is included in a Release Build.

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

