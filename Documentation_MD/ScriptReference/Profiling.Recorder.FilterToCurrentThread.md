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

#  [Recorder](Profiling.Recorder.html).FilterToCurrentThread

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

public void FilterToCurrentThread();

### Description

Configures the recorder to only collect data from the current thread.

By default, a Recorder collects samples from its corresponding Sampler
regardless of which thread those samples occur on. Call this function to limit
sample collection to the current thread only.  
  
Limiting sample collection to the current thread is particularly useful when
performing tests with very commonly-used samplers (such as GC.Alloc), as
ensuring that background threads are not active during the test can be
difficult.  
  
Reset the Recorder to collect samples from all threads by calling
[Recorder.CollectFromAllThreads](Profiling.Recorder.CollectFromAllThreads.html).  
  
Note that when you have more than one Recorder object for the same Sampler,
this filter setting affects all of them. If all of these Recorder instances
are destroyed, any new Recorder instances obtained for the Sampler revert to
the default behavior and collect samples from all threads. However, because it
is difficult to predict the timing of object destruction, always call
[Recorder.CollectFromAllThreads](Profiling.Recorder.CollectFromAllThreads.html)
to reset sample collection.

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

