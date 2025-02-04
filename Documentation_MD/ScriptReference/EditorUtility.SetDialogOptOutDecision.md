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

#  [EditorUtility](EditorUtility.html).SetDialogOptOutDecision

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
SetDialogOptOutDecision([DialogOptOutDecisionType](DialogOptOutDecisionType.html)
dialogOptOutDecisionType, string dialogOptOutDecisionStorageKey, bool
optOutDecision);

### Parameters

dialogOptOutDecisionType | The type of opt-out decision a user can make.  
---|---  
dialogOptOutDecisionStorageKey | The unique key setting to store the decision under.  
optOutDecision | Whether to opt out or not.  
  
### Description

This method displays a modal dialog that lets the user opt-out of being shown
the current dialog box again.

Use this method as a short-hand to set the opt-out decision a user can make on
a dialog displayed via [DisplayDialog](EditorUtility.DisplayDialog.html).  
  
You don't need to set this after you call
[DisplayDialog](EditorUtility.DisplayDialog.html), as Unity handles it
automatically.  
  
If the user chooses to opt-out of a dialog box, Unity stores this decision. If
`dialogOptOutDecisionType` is set to
[DialogOptOutDecisionType.ForThisMachine](DialogOptOutDecisionType.ForThisMachine.html)
Unity stores it via [EditorPrefs.SetBool](EditorPrefs.SetBool.html). If
`dialogOptOutDecisionType` is set to
[DialogOptOutDecisionType.ForThisSession](DialogOptOutDecisionType.ForThisSession.html)
Unity stores it via [SessionState.SetBool](SessionState.SetBool.html). In both
cases Unity stores it under the key provided as
`dialogOptOutDecisionStorageKey`.  
  
This method automatically sets the decision in the storage place based on the
provided `dialogOptOutDecisionType`.  
  
Additional resources: [DisplayDialog](EditorUtility.DisplayDialog.html)
function.

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

