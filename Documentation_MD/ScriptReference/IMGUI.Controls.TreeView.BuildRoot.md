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

#  [TreeView](IMGUI.Controls.TreeView.html).BuildRoot

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

protected [IMGUI.Controls.TreeViewItem](IMGUI.Controls.TreeViewItem.html)
BuildRoot();

### Returns

**TreeViewItem** The root of the tree. This item can later be accessed by
'rootItem'.

### Description

Abstract method that is required to be implemented. By default this method
should create the full tree of TreeViewItems and return the root.

This method together with [BuildRows](IMGUI.Controls.TreeView.BuildRows.html)
are responsible for initializing the TreeView. A TreeView can be created using
two distinct approaches: 1) Create the root and the full tree of items. 2)
Create the root and the rows.  
  
Approach 1 is the default since the TreeView then has automatic handling of
building the rows, ancestor information etc. Approach 2 is desirable for very
large data-sets or for data that change often. See more info in
[BuildRows](IMGUI.Controls.TreeView.BuildRows.html).  
  
Each TreeViewItem needs to be constructed with a unique integer ID (unique
among all the items in the TreeView) and the ID needs to be consistent the
same for same data element regardles of expanded state. The ID is used for
finding items in the tree, for the selection state, expanded state and
navigation.  
  
For a properly initialized TreeView all the TreeViewItems need to have
initialized the ‘parent’, ‘children’ and ‘depth’ properties. Depending on the
tree data model it can be useful to either set the parent and children
properties or the depth property and then use either
SetupParentsAndChildrenFromDepths or SetupDepthsFromParentsAndChildren to set
the uninitialized properties for all the rows in one call.  
  
Additional resources: [BuildRows](IMGUI.Controls.TreeView.BuildRows.html),
[SetupParentsAndChildrenFromDepths](IMGUI.Controls.TreeView.SetupParentsAndChildrenFromDepths.html),
[SetupDepthsFromParentsAndChildren](IMGUI.Controls.TreeView.SetupDepthsFromParentsAndChildren.html),
[TreeViewItem](IMGUI.Controls.TreeViewItem.html).

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

