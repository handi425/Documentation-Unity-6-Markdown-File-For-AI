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

# GarbageCollector

class in UnityEngine.Scripting

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

API to control the garbage collector on the Mono and IL2CPP scripting
backends.

See [GarbageCollector.GCMode](Scripting.GarbageCollector.GCMode.html) for how
to change the global garbage collector operation mode.

### Static Properties

[GCMode](Scripting.GarbageCollector.GCMode.html)| Set and get global garbage
collector operation mode.  
---|---  
[incrementalTimeSliceNanoseconds](Scripting.GarbageCollector-
incrementalTimeSliceNanoseconds.html)| The target duration of a collection
step when performing incremental garbage collection.  
[isIncremental](Scripting.GarbageCollector-isIncremental.html)| Reports
whether incremental garbage collection is enabled.  
  
### Static Methods

[CollectIncremental](Scripting.GarbageCollector.CollectIncremental.html)|
Perform an on-demand incremental garbage collection for a maximum duration
specified by the nanoseconds parameter.  
---|---  
  
### Events

[GCModeChanged](Scripting.GarbageCollector.GCModeChanged.html)| Subscribe to
this event to get notified when GarbageCollector.GCMode changes.  
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

