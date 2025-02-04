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

#  [TreeView.RowGUIArgs](IMGUI.Controls.TreeView.RowGUIArgs.html).GetCellRect

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

public [Rect](Rect.html) GetCellRect(int visibleColumnIndex);

### Parameters

visibleColumnIndex | Index into the list of visible columns of the multi column header.  
---|---  
  
### Returns

**Rect** Cell rect defined by the intersection between the row rect and the
rect of the visible column.

### Description

If using a MultiColumnHeader for the TreeView this method can be used to get
the cell rects of a row using the visible columns of the MultiColumnHeader.

Note the returned cell rect is affected by the
[TreeView.cellMargin](IMGUI.Controls.TreeView-cellMargin.html) value.  
  
Additional resources:
[MultiColumnHeader](IMGUI.Controls.MultiColumnHeader.html),
[TreeView.RowGUI](IMGUI.Controls.TreeView.RowGUI.html),
[TreeView.RowGUIArgs.GetNumVisibleColumns](IMGUI.Controls.TreeView.RowGUIArgs.GetNumVisibleColumns.html),
[TreeView.RowGUIArgs.GetColumn](IMGUI.Controls.TreeView.RowGUIArgs.GetColumn.html).

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

