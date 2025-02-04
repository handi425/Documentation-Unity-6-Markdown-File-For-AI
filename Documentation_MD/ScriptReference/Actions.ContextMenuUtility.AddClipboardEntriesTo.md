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

#  [ContextMenuUtility](Actions.ContextMenuUtility.html).AddClipboardEntriesTo

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
AddClipboardEntriesTo([UIElements.DropdownMenu](UIElements.DropdownMenu.html)
menu);

## Declaration

public static void
AddClipboardEntriesTo([UIElements.DropdownMenu](UIElements.DropdownMenu.html)
menu, bool cutEnabled, bool copyEnabled, bool pasteEnabled, bool
duplicateEnabled, bool deleteEnabled);

### Parameters

menu | The Scene view context menu to add a clipboard operations to.  
---|---  
cutEnabled | Whether to enable the Cut operation in the Scene view context menu. When Cut is disabled, it is greyed out in the Scene view context menu.  
copyEnabled | Whether to enable the Copy operation in the Scene view context menu. If Copy is disabled, it is greyed out in the Scene view context menu.  
pasteEnabled | Whether to enable the Paste operation in the Scene view context menu. If Paste is disabled, it is greyed out in the Scene view context menu.  
duplicateEnabled | Whether to enable the Duplicate operation in the Scene view context menu. If Duplicate is disabled, it is greyed out in the Scene view context menu.  
deleteEnabled | Whether to enable the Delete operation in the Scene view context menu. If Delete is disabled, it is greyed out in the Scene view context menu.  
  
### Description

Adds clipboard operations to the Scene view context menu.

By default, the Cut, Copy, Duplicate, and Delete operations are greyed out in
the Scene view context menu if you do not have a GameObject selected in the
Scene. The Paste operation is greyed out if the clipboard is empty. The method
overload provides additional control over whether these operations are greyed
out.

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

