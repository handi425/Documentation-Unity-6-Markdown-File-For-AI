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
[IProfilerFrameTimeViewSampleSelectionController](Profiling.IProfilerFrameTimeViewSampleSelectionController.html).focusedThreadIndex

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

public int focusedThreadIndex;

### Description

The index of the the thread selected to be displayed in the [Profiler
module](../Manual/ProfilerWindow#modules.html).

If the [Profiler module](../Manual/ProfilerWindow#modules.html) is in (Raw)
Hierarchy view and is showing data for a specific thread, this property's
value corresponds to that thread's index. When you set this to a thread index,
when the Profiler module is in (Raw) Hierarchy view, it switches the display
to show the data of the specified thread. If you set the value, when the
Profiler module is in Timeline view, the specified thread is framed vertically
and on the next change to (Raw) Hierarchy view, it will be set there.  
  
Apart from this one-off effect, the Timeline view's behavior of showing all
threads means it does not track any specific thread that is focused. Because
the Timeline view focuses on the thread that a selection belongs to, this
property returns the thread index of any active selection, when Timeline view
is shown. If there is no active selection, or (Raw) Hierarchy view is shown,
the returned value corresponds to the thread index that is currently showing
in (Raw) Hierarchy or is shown when the view next changes to (Raw) Hierarchy.  
  
The effect of setting this value only happens when you set it, and any
subsequent action or API call to set a selection or change the thread shown in
(Raw) Hierarchy overrides its effect.  
  
This property is especially useful when used in conjunction with
[IProfilerFrameTimeViewSampleSelectionController.sampleNameSearchFilter](Profiling.IProfilerFrameTimeViewSampleSelectionController-
sampleNameSearchFilter.html) and in the Hierarchy view, because you can select
a specific thread and then filter the samples listed in the Hierarchy view.  
  
Additional resources:
[IProfilerFrameTimeViewSampleSelectionController.sampleNameSearchFilter](Profiling.IProfilerFrameTimeViewSampleSelectionController-
sampleNameSearchFilter.html),
[IProfilerFrameTimeViewSampleSelectionController.selection](Profiling.IProfilerFrameTimeViewSampleSelectionController-
selection.html).

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

