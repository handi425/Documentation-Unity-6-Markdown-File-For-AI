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

# ShortcutAttribute Constructor

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

public ShortcutAttribute(string id, Type context = null);

## Declaration

public ShortcutAttribute(string id, Type context, [KeyCode](KeyCode.html)
defaultKeyCode,
[ShortcutManagement.ShortcutModifiers](ShortcutManagement.ShortcutModifiers.html)
defaultShortcutModifiers = None);

## Declaration

public ShortcutAttribute(string id, [KeyCode](KeyCode.html) defaultKeyCode,
[ShortcutManagement.ShortcutModifiers](ShortcutManagement.ShortcutModifiers.html)
defaultShortcutModifiers = None);

## Declaration

public ShortcutAttribute(string id, Type context, string tag,
[KeyCode](KeyCode.html) defaultKeyCode,
[ShortcutManagement.ShortcutModifiers](ShortcutManagement.ShortcutModifiers.html)
defaultShortcutModifiers = None);

## Declaration

public ShortcutAttribute(string id, Type context, string tag,
[KeyCode](KeyCode.html) defaultKeyCode,
[ShortcutManagement.ShortcutModifiers](ShortcutManagement.ShortcutModifiers.html)
defaultShortcutModifiers = None, int priority);

### Parameters

id | Shortcut ID.  
---|---  
context | Optional shortcut context type.  
defaultKeyCode | Optional key code for default binding.  
defaultShortcutModifiers | Optional shortcut modifiers for default binding.  
tag | Optional custom context used to filter shortcuts after window context is determined.  
priority | Optional priority for adjusting order position in Helper Bar.  
  
### Description

Creates an attribute for an _action shortcut_ with an ID, optional context,
and optional default binding.

An action shortcut is triggered when the binding for the shortcut is pressed
down. The method on which this attribute is placed must either take no
arguments or a single argument of type
[ShortcutArguments](ShortcutManagement.ShortcutArguments.html).  
  
You can bind a
[ClutchShortcutAttribute](ShortcutManagement.ClutchShortcutAttribute.html) and
a [ShortcutAttribute](ShortcutManagement.ShortcutAttribute.html) to the same
mouse button. In this case, the action shortcut triggers when the mouse button
is released.  
  
The ID is used to display the shortcut in the configuration interface unless
the optional displayName property is set. Use a forward slash group multiple
shortcuts together in the configuration interface, e.g. "MyWindow/Shortcut1"
and "MyWindow/Shortcut2".

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

