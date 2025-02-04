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

#  [EditorToolContext](EditorTools.EditorToolContext.html).PopulateMenu

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

public void
PopulateMenu([UIElements.DropdownMenu](UIElements.DropdownMenu.html) menu);

### Parameters

menu | The Scene view context menu to add menu items to.  
---|---  
  
### Description

Adds menu items to the Scene view context menu.

Refer to MenuUtility for utility functions that add menu items to the Scene
view context menu.

    
    
    public override void PopulateMenu([DropdownMenu](UIElements.DropdownMenu.html) menu)
    {
        // Add all clipboard operations to the context menu (Cut, Copy, Paste, Delete, and Duplicate).
        [ContextMenuUtility.AddClipboardEntriesTo](Actions.ContextMenuUtility.AddClipboardEntriesTo.html)(menu);
    
        // Add an item to the context menu using a delegate or an [EditorAction](Actions.EditorAction.html).
        menu.AppendAction("Parent [Item](Progress.Item.html)/Child [Item](Progress.Item.html)", (item) => [Debug.Log](Debug.Log.html)("Executed Child [Item](Progress.Item.html)."));
    
        // Add an item to the context menu using a predefined [MenuItem](MenuItem.html).
        [ContextMenuUtility.AddMenuItem](Actions.ContextMenuUtility.AddMenuItem.html)(menu, "[GameObject](GameObject.html)/Move To View");
    }
    

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

