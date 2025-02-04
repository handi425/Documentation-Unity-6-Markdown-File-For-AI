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

# PlayerLoopSystem

struct in UnityEngine.LowLevel

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

The representation of a single system being updated by the player loop in
Unity.

This struct represents a single system in the player loop. A system can be one
of Unity's built-in native systems, or you can add new custom systems to the
player loop using C#. Native systems can only be retrieved by calling
[PlayerLoop.GetDefaultPlayerLoop](LowLevel.PlayerLoop.GetDefaultPlayerLoop.html),
and the parameters of them should not be modified.

### Properties

[loopConditionFunction](LowLevel.PlayerLoopSystem-loopConditionFunction.html)|
The loop condition for a native engine system. To get a valid value for this,
you must copy it from one of the PlayerLoopSystems returned by
PlayerLoop.GetDefaultPlayerLoop.  
---|---  
[subSystemList](LowLevel.PlayerLoopSystem-subSystemList.html)| A list of sub
systems which run as part of this item in the player loop.  
[type](LowLevel.PlayerLoopSystem-type.html)| This property is used to identify
which native system this belongs to, or to get the name of the managed system
to show in the profiler.  
[updateDelegate](LowLevel.PlayerLoopSystem-updateDelegate.html)| A managed
delegate. You can set this to create a new C# entrypoint in the player loop.  
[updateFunction](LowLevel.PlayerLoopSystem-updateFunction.html)| A native
engine system. To get a valid value for this, you must copy it from one of the
PlayerLoopSystems returned by PlayerLoop.GetDefaultPlayerLoop.  
  
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

