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

#  [Touch](Touch.html).fingerId

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

public int fingerId;

### Description

The unique index for the touch.

All current touches are reported in the [Input.touches](Input-touches.html)
array or by using the [Input.GetTouch](Input.GetTouch.html) function with the
equivalent array index. However, the array index is not guaranteed to be the
same from one frame to the next. The `fingerId` value, however, consistently
refers to the same touch across frames. This ID value is very useful when
analysing gestures and is more reliable than identifying fingers by their
proximity to previous position, etc.  
  
[Touch.fingerId](Touch-fingerId.html) is not the same as "first" touch,
"second" touch and so on. It is merely a unique id per gesture. You cannot
make any assumptions about fingerId and the number of fingers actually on
screen, since virtual touches will be introduced to handle the fact that the
touch structure is constant for an entire frame (while in reality the number
of touches obviously might not be true, e.g. if multiple tappings occur within
a single frame).

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

