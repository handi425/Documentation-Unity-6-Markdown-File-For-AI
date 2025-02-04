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

#  [CharacterController](CharacterController.html).enableOverlapRecovery

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

[Switch to Manual](../Manual/class-CharacterController.html "Go to
CharacterController Component in the Manual")

public bool enableOverlapRecovery;

### Description

Enables or disables overlap recovery. Enables or disables overlap recovery.
Used to depenetrate character controllers from static objects when an overlap
is detected.

Overlap recovery can be used to depenetrate character controllers (CCTs) from
static objects when an overlap is detected. This can happen in three main
cases:  
  
\- when the CCT is directly spawned or teleported in another object  
  
\- when the CCT algorithm fails due to limited FPU accuracy  
  
\- when the "up vector" is modified, making the rotated CCT shape overlap
surrounding objects  
  
When activated, the CCT module will automatically try to resolve the
penetration, and move the CCT to a safe place where it does  
  
not overlap other objects anymore. This only concerns static objects, dynamic
objects are ignored by overlap recovery.  
  
When overlap recovery is not activated, it is possible for the CCTs to go
through static objects. By default, overlap recovery is enabled.  
  
Overlap recovery currently works with all geometries except heightfields.

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

