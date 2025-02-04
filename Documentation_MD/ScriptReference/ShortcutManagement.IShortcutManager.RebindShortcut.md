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

#  [IShortcutManager](ShortcutManagement.IShortcutManager.html).RebindShortcut

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

public void RebindShortcut(string shortcutId,
[ShortcutManagement.ShortcutBinding](ShortcutManagement.ShortcutBinding.html)
binding);

### Parameters

shortcutId | ID of shortcut to rebind.  
---|---  
binding | New binding of shortcut.  
  
### Description

Rebinds the shortcut for the given shortcut ID to the given binding in the
active profile.

Creates a new (or modifies the existing) binding override for the given
shortcut ID on the active profile.  
  
Throws `ArgumentNullException` if `shortcutId` is null. Throws
`ArgumentException` if `shortcutId` is not available, i.e. when
[GetAvailableShortcutIds](ShortcutManagement.IShortcutManager.GetAvailableShortcutIds.html)
does not contain `shortcutId`. Throws `InvalidOperationException` if the
active profile is read-only, i.e. when
[IsReadOnlyProfile](ShortcutManagement.IShortcutManager.IsReadOnlyProfile.html)
returns `true` for [activeProfileId](ShortcutManagement.IShortcutManager-
activeProfileId.html).

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

