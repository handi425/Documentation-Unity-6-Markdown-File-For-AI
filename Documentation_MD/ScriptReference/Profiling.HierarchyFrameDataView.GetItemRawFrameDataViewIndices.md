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
[HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html).GetItemRawFrameDataViewIndices

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

public void GetItemRawFrameDataViewIndices(int id, List<int>
outSampleIndices);

### Parameters

id | Hierarchy item identifier.  
---|---  
outSampleIndices | List filled with all profiler sample indices represented by the hierarchy item.  
  
### Description

Retrieves the raw indices of all samples associated with this Hierarchy item
identifier.

When HierarchyFrameDataView.ViewMode.MergeSamplesWithTheSameName is active,
Unity merges multiple samples with the same name at the same hierarchy level
together in a single item.  
  
As a result of this behavior, and the hierarchical structure of the samples in
_HierarchyFrameDataView_ , the **Hierarchy item identifiers** that
_HierarchyFrameDataView_ uses, do not correspond to the **sample indices**
that [RawFrameDataView](Profiling.RawFrameDataView.html) uses. Use
_GetItemRawFrameDataViewIndices_ to get the sample indices in a format that
works with [RawFrameDataView](Profiling.RawFrameDataView.html)  
  
The result is written to _outSampleIndices_ list which is resized if
necessary.  
  
If you you only want to confirm that an item in the _HierarchyFrameDataView_
corresponds to a particular **sample index** you can use
[HierarchyFrameDataView.ItemContainsRawFrameDataViewIndex](Profiling.HierarchyFrameDataView.ItemContainsRawFrameDataViewIndex.html)
instead.  
  
**Throws:**  
_System.ArgumentException_ if _id_ is invalid. _System.ArgumentNullException_
if _outSampleIndices_ is null.  
  
Additional resources:
[HierarchyFrameDataView.GetItemMergedSamplesCount](Profiling.HierarchyFrameDataView.GetItemMergedSamplesCount.html),
[HierarchyFrameDataView.ItemContainsRawFrameDataViewIndex](Profiling.HierarchyFrameDataView.ItemContainsRawFrameDataViewIndex.html)
[RawFrameDataView](Profiling.RawFrameDataView.html).

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

