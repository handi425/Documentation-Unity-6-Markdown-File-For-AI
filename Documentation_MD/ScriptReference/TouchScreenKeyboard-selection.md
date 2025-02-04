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

#  [TouchScreenKeyboard](TouchScreenKeyboard.html).selection

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

public [RangeInt](RangeInt.html) selection;

### Description

Gets or sets the character range of the selected text within the string
currently being edited.

For example: if the keyboard is editing a [text](TouchScreenKeyboard-
text.html) "abcdef" and the "cde" substring is selected, the return value is a
[RangeInt](RangeInt.html) with the [RangeInt.start](RangeInt-start.html) value
set to 2 and a [RangeInt.length](RangeInt-length.html) value of 3. Similarly,
setting selection to a [RangeInt](RangeInt.html) with the
[RangeInt.start](RangeInt-start.html) value set to 2 and a
[RangeInt.length](RangeInt-length.html) value of 3 will select "cde" of the
string "abcdef".  
  
If the caret is between two characters and no text is selected, then the
[RangeInt.length](RangeInt-length.html) property is 0.  
  
This always returns an empty range (start 0, length 0) if
[canGetSelection](TouchScreenKeyboard-canGetSelection.html) is false.

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

