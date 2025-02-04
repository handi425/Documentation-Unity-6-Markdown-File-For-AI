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
[HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html).ItemContainsRawFrameDataViewIndex

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

public bool ItemContainsRawFrameDataViewIndex(int id, int sampleIndex);

### Parameters

id | Hierarchy item identifier.  
---|---  
sampleIndex | The particular profiler sample index that should be checked if it is represented by this hierarchy item.  
  
### Returns

**bool** True if the sample index is represented by this hierarchy item, false
if it is not.

### Description

Checks if the provided raw sample index matches any of the raw sample indices
associated with this Hierarchy item identifier.

When HierarchyFrameDataView.ViewMode.MergeSamplesWithTheSameName is active,
Unity merges multiple samples with the same name at the same hierarchy level
together in a single item.  
  
As a result of this behavior, and the hierarchical structure of the samples in
_HierarchyFrameDataView_ , the **Hierarchy item identifiers** that
_HierarchyFrameDataView_ uses, do not correspond to the **sample indices**
that [RawFrameDataView](Profiling.RawFrameDataView.html) uses. To get these
indices to use with [RawFrameDataView](Profiling.RawFrameDataView.html), use
_GetItemRawFrameDataViewIndices_.  
  
However, if you only want to confirm that an item in the
_HierarchyFrameDataView_ corresponds to a particular **sample index** you can
use _ItemContainsRawFrameDataViewIndex_ to confirm that without the need to
retrieve the entire list of **sample indices**.  
  
**Throws:**  
_System.ArgumentException_ if _id_ is invalid.  
  
Additional resources:
[HierarchyFrameDataView.GetItemMergedSamplesCount](Profiling.HierarchyFrameDataView.GetItemMergedSamplesCount.html),
[HierarchyFrameDataView.GetItemRawFrameDataViewIndices](Profiling.HierarchyFrameDataView.GetItemRawFrameDataViewIndices.html),
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

