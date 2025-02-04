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
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html).SetNestedContainer

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
SetNestedContainer([Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)
handle, bool isNestedContainer);

### Parameters

handle | The AtomicSafetyHandle to flag.  
---|---  
isNestedContainer | Set to `true` to flag the container protected by this AtomicSafetyHandle as nested; `false` otherwise.  
  
### Description

Sets the nested container flag on an AtomicSafetyHandle.

The job system doesn't support nested containers which are containers where
the individual elements inside the container are themselves containers),
because it can't configure the AtomicSafetyHandle instances stored inside the
container's elements independently for each job using the container. This
means that attempting to use a nested container in a job doesn't work
correctly.  
  
To protect against using nested containers in jobs and prevent subtle and
hard-to-diagnose errors from arising, you should set the nested container flag
on any container's AtomicSafetyHandle that detects that it is being used to
store containers. This makes the Job Debugger throw an explicit error when
scheduling a job which tries to use a nested container.  
  
Additional resources:
[AtomicSafetyHandle.GetNestedContainer](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetNestedContainer.html).

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

