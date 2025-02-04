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

#  [GarbageCollector](Scripting.GarbageCollector.html).CollectIncremental

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

public static bool CollectIncremental(ulong nanoseconds);

### Parameters

nanoseconds | The maximum time in nanoseconds to perform the garbage collection for.  
---|---  
  
### Returns

**bool** Returns true if additional garbage collection work remains when the
method returns and false if garbage collection is complete. Also returns false
if incremental garbage collection is not enabled or is not supported on the
current platform.

### Description

Perform an on-demand incremental garbage collection for a maximum duration
specified by the `nanoseconds` parameter.

If incremental garbage collection is enabled, then `CollectIncremental` runs
the incremental garbage collector for up to the specified number of
nanoseconds. The method returns when either the specified amount of time has
elapsed, or there is no more garbage collection work to be done. Note that the
garbage collector uses the underlying platform timer, which can have a
resolution as low as a few microseconds. In other words, changing the value by
a few nanoseconds might have no effect.  
  
Use this method when you know you have a certain amount of time to wait for
something to happen, and want to use this time to let the garbage collector
run.  
  
If incremental garbage collection is not enabled, this method does nothing and
returns `false`. Enable incremental garbage collection in the
[PlayerSettings](PlayerSettings.html) for a project. You can check whether
incremental garbage collection is enabled with
[GarbageCollector.isIncremental](Scripting.GarbageCollector-
isIncremental.html).  
  
If no value is specified for the `nanoseconds` parameter, the value defaults
to `0` and no incremental garbage collection is performed.  
  
**Note** : The `nanoseconds` parameter specifies the maximum total time for
which to perform an on-demand incremental garbage collection and should not be
confused with
[GarbageCollector.incrementalTimeSliceNanoseconds](Scripting.GarbageCollector-
incrementalTimeSliceNanoseconds.html) which specifies the target duration of
the individual collection steps that incremental garbage collection is split
across. For example, if
[GarbageCollector.incrementalTimeSliceNanoseconds](Scripting.GarbageCollector-
incrementalTimeSliceNanoseconds.html) has its default value of 3000000
nanoseconds (3 ms) and you call
`GarbageCollector.CollectIncremental(10000000)`, the garbage collector can run
for a maximum of 10 ms and therefore can perform a maximum of three (but
likely no more than two) 3 ms long incremental collection steps in the time
available.  
  
Additional resources:
[incrementalTimeSliceNanoseconds](Scripting.GarbageCollector-
incrementalTimeSliceNanoseconds.html).

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

