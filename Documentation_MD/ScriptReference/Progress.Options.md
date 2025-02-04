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

# Options

enumeration

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

Options that define how a progress indicator behaves.

### Properties

[None](Progress.Options.None.html)| A progress indicator that starts with no
other options activated. This is the default.  
---|---  
[Sticky](Progress.Options.Sticky.html)| A sticky progress indicator displays
progress information even after the task is complete. The system does not
remove it automatically. You must remove it using a remove operation.  
[Indefinite](Progress.Options.Indefinite.html)| An indefinite progress
indicator shows that the associated task is in progress, but does not show how
close it is to completion.  
[Synchronous](Progress.Options.Synchronous.html)| A synchronous progress
indicator updates the Editor UI as soon as it reports progress. This is the
opposite of the default behavior, which is to report all progress
asynchronously.  
[Managed](Progress.Options.Managed.html)| Unity manages progress indicators.
When a domain reload happens, the system cancels tasks that support
cancellation, and removes their progress indicators. This is the default for
progress indicators started from C#.  
[Unmanaged](Progress.Options.Unmanaged.html)| An unmanaged progress indicator
is one that Unity does not manage. Unity does not cancel unmanaged progress
indicators when a domain reload happens. This is the default behavior for
internal-use progress indicators started from C++ code.  
  
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

