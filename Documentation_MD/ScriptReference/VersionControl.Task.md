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

# Task

class in UnityEditor.VersionControl

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

A Task describes an instance of a version control operation.

An object of this type allows you to process operations such as
[Provider.Checkout](VersionControl.Provider.Checkout.html),
[Provider.GetLatest](VersionControl.Provider.GetLatest.html), and
[Provider.Submit](VersionControl.Provider.Submit.html). Unity creates this
item almost every time you ask [Provider](VersionControl.Provider.html) to
perform an action. Task objects, that version control operations return,
execute in the background and don't always finish immediately, use
[Task.Wait](VersionControl.Task.Wait.html) if you need to wait for them to
finish.

### Properties

[assetList](VersionControl.Task-assetList.html)| The result of some types of
tasks.  
---|---  
[changeSets](VersionControl.Task-changeSets.html)| List of changesets returned
by some tasks.  
[description](VersionControl.Task-description.html)| A short description of
the current task.  
[messages](VersionControl.Task-messages.html)| May contain messages from the
version control plugins.  
[progressPct](VersionControl.Task-progressPct.html)| A progress percentage for
the current task.  
[resultCode](VersionControl.Task-resultCode.html)| Some task return result
codes, these are stored here.  
[secondsSpent](VersionControl.Task-secondsSpent.html)| Total time spent in
task since the task was started.  
[success](VersionControl.Task-success.html)| Get whether or not the task was
completed succesfully.  
[text](VersionControl.Task-text.html)| Will contain the result of the
Provider.ChangeSetDescription task.  
  
### Public Methods

[SetCompletionAction](VersionControl.Task.SetCompletionAction.html)| Upon
completion of a task a completion task will be performed if it is set.  
---|---  
[Wait](VersionControl.Task.Wait.html)| A blocking wait for the task to
complete.  
  
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

