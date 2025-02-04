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

#  [Progress](Progress.html).Report

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

public static void Report(int id, float progress);

## Declaration

public static void Report(int id, float progress, string description);

## Declaration

public static void Report(int id, int currentStep, int totalSteps);

## Declaration

public static void Report(int id, int currentStep, int totalSteps, string
description);

### Parameters

id | The progress indicator's unique ID.  
---|---  
progress | A new progress value between 0 and 1.  
description | An updated description of the progress indicator. If the the progress status has not changed, or you do not set a description, this is null. To clear the current progress description, pass an empty string such as _""_.  
currentStep | An updated current step.  
totalSteps | An updated total number of steps, from start to finish.  
  
### Description

Reports a running progress indicator's current status.

When you report in steps, you can set the label for the steps with
[Progress.SetStepLabel](Progress.SetStepLabel.html). Note: Changes are applied
on the next application tick unless you call this function from the main
thread using a synchronous progress indicator (see
[Synchronous](Progress.Options.Synchronous.html)).  
  
Additional resources: [Progress.Report](Progress.Report.html),
[Progress.GetProgress](Progress.GetProgress.html),
[Progress.GetDescription](Progress.GetDescription.html),
[Progress.SetDescription](Progress.SetDescription.html).

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

