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

#  [TreeView](IMGUI.Controls.TreeView.html).BuildRows

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

protected IList<TreeViewItem>
BuildRows([IMGUI.Controls.TreeViewItem](IMGUI.Controls.TreeViewItem.html)
root);

### Parameters

root | Root item that was created in the BuildRoot method.  
---|---  
  
### Returns

**IList <TreeViewItem>** The rows list shown in the TreeView. Can later be
accessed using GetRows().

### Description

Override this method to take control of how the rows are generated.

This method is called when Reload is called and every time items are expanded
or collapsed. The default implementation of BuildRows takes care of caching
the expanded rows based on the full tree and the expanded state of items.  
  
For very large data-sets or for data that change often it can be desirable to
only create the rows of the TreeView and not the full tree. In this situation
override this method to build the rows manually. If a collapsed parent is
encountered then the descendants of that parent can be omitted (since they are
not visible). Set the children of that item using the
CreateChildListForCollapsedParent() method.  
  
When using this approach then
[BuildRoot](IMGUI.Controls.TreeView.BuildRoot.html) should just create the
root TreeViewItem (and not the full tree). You will need to add your own
delegate to getNewSelectionOverride in order to handle selection changes. Also
ensure to override GetAncestors() and GetDescendantsThatHaveChildren() and use
the model data to fetch this information, otherwise framing and expanding sub-
trees will fail.  
  
When building the rows manually remember to use the search string of the
TreeView to filter items.  
  
Additional resources: [BuildRoot](IMGUI.Controls.TreeView.BuildRoot.html),
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

