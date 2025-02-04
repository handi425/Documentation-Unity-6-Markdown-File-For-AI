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

# IProfilerFrameTimeViewSampleSelectionController

interface in UnityEditor.Profiling

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

This Interface defines an
[IProfilerFrameTimeViewSampleSelectionController](Profiling.IProfilerFrameTimeViewSampleSelectionController.html)
object that you can use to control the selection in [Profiler
modules](../Manual/ProfilerWindow#modules.html) that display timing
information of Profiler samples, such as the [CPU Usage
module](../Manual/ProfilerCPU.html) and the [GPU Usage Profiler
module](../Manual/ProfilerGPU.html).

Use
[ProfilerWindow.GetFrameTimeViewSampleSelectionController](ProfilerWindow.GetFrameTimeViewSampleSelectionController.html)
to retrieve such an object.

### Properties

[focusedThreadIndex](Profiling.IProfilerFrameTimeViewSampleSelectionController-
focusedThreadIndex.html)| The index of the the thread selected to be displayed
in the Profiler module.  
---|---  
[sampleNameSearchFilter](Profiling.IProfilerFrameTimeViewSampleSelectionController-
sampleNameSearchFilter.html)| This filters the samples displayed in Hierarchy
view to only include the names that include this string.  
[selection](Profiling.IProfilerFrameTimeViewSampleSelectionController-
selection.html)| Get the current selection in a frame time sample based
Profiler modules, such as the CPU Usage module and the GPU Usage Profiler
module.  
  
### Public Methods

[ClearSelection](Profiling.IProfilerFrameTimeViewSampleSelectionController.ClearSelection.html)|
Call this method to clear the current selection in this frame time view based
Profiler module.  
---|---  
[SetSelection](Profiling.IProfilerFrameTimeViewSampleSelectionController.SetSelection.html)|
Set the current selection in a frame time sample based Profiler Module, such
as the CPU Usage module and the GPU Usage Profiler module.  
  
### Events

[selectionChanged](Profiling.IProfilerFrameTimeViewSampleSelectionController-
selectionChanged.html)| Calls the methods in its invocation list when the
selection in this Profiler module changes. The first parameter contains the
Profiler module the selection change occurred in, the second parameter is the
new selection.  
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

