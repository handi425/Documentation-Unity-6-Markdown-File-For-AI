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

# ProfilerTimeSampleSelection

class in UnityEditor.Profiling

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

An object describing a selection made in a frame time sample based [Profiler
module](../Manual/ProfilerWindow#modules.html).

Use
[ProfilerWindow.GetFrameTimeViewSampleSelectionController](ProfilerWindow.GetFrameTimeViewSampleSelectionController.html)
to get a frame time sample based Profiler module, then use
[IProfilerFrameTimeViewSampleSelectionController.selection](Profiling.IProfilerFrameTimeViewSampleSelectionController-
selection.html) to get an object describing the current selection. You can
create a selection object and set the current selection in a frame time sample
based Profiler module via
[IProfilerFrameTimeViewSampleSelectionController.SetSelection](Profiling.IProfilerFrameTimeViewSampleSelectionController.SetSelection.html).

### Properties

[frameIndex](Profiling.ProfilerTimeSampleSelection-frameIndex.html)| The 0
based frame index. Note that the Profiler Window UI shows the frame index as
n+1.  
---|---  
[markerNamePath](Profiling.ProfilerTimeSampleSelection-markerNamePath.html)| A
list of the names of all ProfilerMarkers that make up the Sample Stack of this
selection. Unity populates this list on a selection object if it was passed to
IProfilerFrameTimeViewSampleSelectionController.SetSelection and was accepted
as a valid selection.  
[markerPathDepth](Profiling.ProfilerTimeSampleSelection-markerPathDepth.html)|
A shorthand for _markerNamePath.Count. When _markerNamePath is null, this
value is 0.  
[rawSampleIndex](Profiling.ProfilerTimeSampleSelection-rawSampleIndex.html)|
The raw index of a sample, i.e. the index as if would be used with
RawFrameDataView and NOT an Item ID as it would be used with
HierarchyFrameDataView.  
[rawSampleIndices](Profiling.ProfilerTimeSampleSelection-
rawSampleIndices.html)| A sample selected in Hierarchy view might correspond
to multiple samples in RawFrameDataView. This is a list of all of these sample
indices.  
[sampleDisplayName](Profiling.ProfilerTimeSampleSelection-
sampleDisplayName.html)| The name of the Sample as it is displayed in the
Profiler Window. This might be a shorter version than the last item in
_markerNamePath.  
[threadGroupName](Profiling.ProfilerTimeSampleSelection-threadGroupName.html)|
The name of the group of the thread this sample resides in. When the thread is
not part of a thread group, this value is string.empty.  
[threadId](Profiling.ProfilerTimeSampleSelection-threadId.html)| The ID of the
thread this sample resides in.  
[threadName](Profiling.ProfilerTimeSampleSelection-threadName.html)| The name
of the thread this sample resides in.  
  
### Constructors

[ProfilerTimeSampleSelection](Profiling.ProfilerTimeSampleSelection-
ctor.html)| Constructs a selection object that can be passed to
IProfilerFrameTimeViewSampleSelectionController.SetSelection to change the
selection.  
---|---  
  
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

