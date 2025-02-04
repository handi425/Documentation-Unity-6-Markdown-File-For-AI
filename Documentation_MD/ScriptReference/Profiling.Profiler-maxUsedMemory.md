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

#  [Profiler](Profiling.Profiler.html).maxUsedMemory

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

public static int maxUsedMemory;

### Description

Sets the maximum amount of memory that Profiler uses for buffering data. This
property is expressed in bytes.

When Profiler is enabled, it collects data continuously and either saves the
data to a file or sends it to the Editor.  
  
Depending on disk write speed or network bandwidth, Profiler may collect more
data than it is able to write. If this happens, Profiler accumulates data in a
ring buffer chain and stops collecting data when the total size of the buffer
chain reaches the _maxUsedMemory_ limit. Profiler data collection resumes when
it is able to write data.  
  
By default, _maxUsedMemory_ is 128MB for Players and 512MB for the Editor. You
can use the **-profiler-maxusedmemory** command line argument to set the
_maxUsedMemory_ parameter at startup. For example, _-profiler-maxusedmemory
16777216_ ,  
  
Additional resources: [Profiler.enabled](Profiling.Profiler-enabled.html).

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

