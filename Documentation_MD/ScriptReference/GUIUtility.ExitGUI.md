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

#  [GUIUtility](GUIUtility.html).ExitGUI

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

public static void ExitGUI();

### Description

Puts the GUI in a state that will prevent all subsequent immediate mode GUI
functions from evaluating for the remainder of the GUI loop by throwing an
[ExitGUIException](ExitGUIException.html).

In Unity's immediate mode GUI system, the GUI loop procedes by calling
[GUI](GUI.html) methods during a sequence of [Event](Event.html)s and these
methods take action according to the [Event.type](Event-type.html). For
example, when using [GUILayout](GUILayout.html), controls will first receive a
[EventType.Layout](EventType.Layout.html) event to determine how much space
they need, and then later receive a
[EventType.Repaint](EventType.Repaint.html) event to actually draw into the
space allocated for them.  
  
In this sequence, it is expected that control IDs are requested and used in
the same order for each [Event](Event.html) that is processed during the GUI
loop, and that the event loop does not re-enter itself. Use
[GUIUtility.ExitGUI](GUIUtility.ExitGUI.html) in situations that might violate
these assumptions, such as when a change in some value might change what
controls are displayed next. Using this method can prevent errors such as
`ArgumentException: Getting control 0's position in a group with only 0
controls when doing Repaint`.  
  
Additional resources: [GetControlID](GUIUtility.GetControlID.html).

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

