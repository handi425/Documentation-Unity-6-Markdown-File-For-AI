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

# Item

class in UnityEditor

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

A data structure that provides information about a progress indicator.

### Properties

[cancellable](Progress.Item-cancellable.html)| Returns true if the progress
indicator's associated event can be canceled.  
---|---  
[currentStep](Progress.Item-currentStep.html)| Returns the current step for
this progress indicator.  
[description](Progress.Item-description.html)| Returns the progress
indicator's description.  
[elapsedTime](Progress.Item-elapsedTime.html)| Returns the number of seconds
that the progress indicator has been running for.  
[endTime](Progress.Item-endTime.html)| Returns the time when the progress
indicator ended.  
[exists](Progress.Item-exists.html)| Checks whether the progress indicator
exists.  
[finished](Progress.Item-finished.html)| Returns true if the progress
indicator is finished, but not removed.  
[id](Progress.Item-id.html)| Returns the progress indicator's unique
identifier.  
[indefinite](Progress.Item-indefinite.html)| Returns true if the progress
indicator is indefinite.  
[name](Progress.Item-name.html)| Returns the progress indicator's name.  
[options](Progress.Item-options.html)| Returns the option flags used to start
the progress indicator.  
[parentId](Progress.Item-parentId.html)| Returns the unique ID of the progress
indicator's parent, or -1 if the progress indicator is not a child of another
progress indicator.  
[pausable](Progress.Item-pausable.html)| Returns true if the progress
indicator's task can be paused.  
[paused](Progress.Item-paused.html)| Returns true if the progress indicator is
paused.  
[priority](Progress.Item-priority.html)| Returns the progress indicator's
priority.  
[progress](Progress.Item-progress.html)| Returns the progress value of a
progress indicator's associated task.  
[remainingTime](Progress.Item-remainingTime.html)| Returns this progress
indicator's remaining time to completion.  
[responding](Progress.Item-responding.html)| Returns true if progress is
ongoing, false if the progress indicator has not received any progress report
for more than 5 seconds.  
[running](Progress.Item-running.html)| Returns true if the progress indicator
is running and active.  
[startTime](Progress.Item-startTime.html)| Returns the time when the progress
indicator started.  
[status](Progress.Item-status.html)| Returns the progress indicator's status.  
[stepLabel](Progress.Item-stepLabel.html)| Returns the label that displays the
progress indicator's steps.  
[timeDisplayMode](Progress.Item-timeDisplayMode.html)| Returns the progress
indicator's time display mode.  
[totalSteps](Progress.Item-totalSteps.html)| Returns the total number of
steps, from start to finish, for this progress indicator.  
[updateTime](Progress.Item-updateTime.html)| Returns the last time the
progress indicator was updated.  
  
### Public Methods

[Cancel](Progress.Item.Cancel.html)| Cancels a running progress indicator.  
---|---  
[ClearRemainingTime](Progress.Item.ClearRemainingTime.html)| Resets the
computation of the progress indicator's remaining time.  
[Finish](Progress.Item.Finish.html)| Marks the progress indicator as finished.  
[Pause](Progress.Item.Pause.html)| Pauses a running progress indicator.  
[RegisterCancelCallback](Progress.Item.RegisterCancelCallback.html)| Registers
a callback that is called when the user cancels a running progress indicator's
associated task.  
[RegisterPauseCallback](Progress.Item.RegisterPauseCallback.html)| Registers a
callback that is called when a user pauses a running progress indicator's
task.  
[Remove](Progress.Item.Remove.html)| Finishes and removes an active progress
indicator.  
[Report](Progress.Item.Report.html)| Reports the progress indicator's current
status.  
[Resume](Progress.Item.Resume.html)| Resumes a paused progress indicator.  
[SetDescription](Progress.Item.SetDescription.html)| Sets the progress
indicator's description. To clear the description pass null.  
[SetPriority](Progress.Item.SetPriority.html)| Sets the progress indicator's
priority.  
[SetRemainingTime](Progress.Item.SetRemainingTime.html)| Sets the progress
indicator's remaining time, in seconds.  
[SetStepLabel](Progress.Item.SetStepLabel.html)| Sets the label that displays
the progress indicator's steps.  
[SetTimeDisplayMode](Progress.Item.SetTimeDisplayMode.html)| Set a progress
indicator's time display mode.  
[UnregisterCancelCallback](Progress.Item.UnregisterCancelCallback.html)|
Unregisters a previously registered progress cancellation callback.  
[UnregisterPauseCallback](Progress.Item.UnregisterPauseCallback.html)|
Unregisters a previously registered progress pause callback.  
  
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

