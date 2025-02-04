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

#  [Profiler](Profiling.Profiler.html).SetAreaEnabled

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

public static void
SetAreaEnabled([Profiling.ProfilerArea](Profiling.ProfilerArea.html) area,
bool enabled);

### Parameters

area | The area you want to enable or disable.  
---|---  
enabled | Enable or disable the collection of data for this area.  
  
### Description

Enable or disable a given [ProfilerArea](Profiling.ProfilerArea.html).

Disable an area to stop it emitting stats and samples. Disabling areas that
you are not interested in is a way to reduce profiler overhead. If you turn an
area back on after you profile a frame with a disabled
[ProfilerArea](Profiling.ProfilerArea.html), this only turns on collection for
subsequent frames.  
  
To disable or enable an area, close or open the corresponding chart in the
[ProfilerWindow](ProfilerWindow.html), or call this method.  
  
**Note** : If the [ProfilerWindow](ProfilerWindow.html) is open when starting
to profile, it will override the enabled/disabled areas to reflect which
charts are open at the time.  
  
To query the current state of an area, use
[Profiler.GetAreaEnabled](Profiling.Profiler.GetAreaEnabled.html).  
  
Setting [ProfilerArea.CPU](Profiling.ProfilerArea.CPU.html) is essentially the
same as setting [Profiler.enabled](Profiling.Profiler-enabled.html), since
some other areas depend on CPU sample collection and it is also handling the
frame ticks.

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

