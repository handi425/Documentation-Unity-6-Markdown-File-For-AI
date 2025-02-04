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
[GarbageCollector](Scripting.GarbageCollector.html).incrementalTimeSliceNanoseconds

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

public static ulong incrementalTimeSliceNanoseconds;

### Description

The target duration of a collection step when performing incremental garbage
collection.

When you enable incremental garbage collection, the garbage collector spreads
the amount of work required to free unused memory across a number of steps. In
any single step, the garbage collector limits itself to the length of time
specified by `incrementalTimeSliceNanoseconds`. By spreading out the workload,
incremental garbage collection can help your game achieve a smoother frame
rate (when garbage-collection hiccups are a problem). Use the
[Profiler](Profiling.Profiler.html) to help identify whether garbage
collection has an effect on frame rate smoothness.  
  
The garbage collector might still choose to perform a regular, non-incremental
collection cycle if your application runs low on memory or if the incremental
steps cannot keep up with the garbage collection workload. Setting too short a
time slice can be counterproductive in this regard and because each garbage
collection step has a small amount of overhead. The default value of 3 ms
(3000000 nanoseconds) is a good starting point and the selected duration
should be always be significantly shorter than your target frame rate.  
  
If you turn on Vsync by setting [QualitySettings.vSyncCount](QualitySettings-
vSyncCount.html) greater than 0 or specify a frame rate with
[Application.targetFrameRate](Application-targetFrameRate.html), Unity
automatically uses any extra time remaining at the end of each frame for
incremental garbage collection, regardless of the value of
[incrementalTimeSliceNanoseconds](Scripting.GarbageCollector-
incrementalTimeSliceNanoseconds.html).  
  
**Note** : The garbage collector uses the underlying platform timer, which can
have a resolution as low as a whole millisecond. In other words, changing the
value by a few nanoseconds might have no effect.  
  
Enable incremental garbage collection in the
[PlayerSettings](PlayerSettings.html) for a project. You can check whether
incremental garbage collection is enabled with
[IsIncremental](Scripting.GarbageCollector.IsIncremental.html).  
  
You can manually trigger an incremental garbage collection step with
[CollectIncremental](Scripting.GarbageCollector.CollectIncremental.html).

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

