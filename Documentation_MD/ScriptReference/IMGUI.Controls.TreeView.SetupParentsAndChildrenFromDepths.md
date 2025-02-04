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

#  [TreeView](IMGUI.Controls.TreeView.html).SetupParentsAndChildrenFromDepths

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

protected static void
SetupParentsAndChildrenFromDepths([IMGUI.Controls.TreeViewItem](IMGUI.Controls.TreeViewItem.html)
root, IList<TreeViewItem> rows);

### Parameters

root | The hidden root item.  
---|---  
rows | TreeViewItems where only the depth property have been set.  
  
### Description

Utility method for initializing all the parent and children properties of the
rows using the order and the depths values that have been set.

Some tree data models are based on order and depth information only. This
method can be called after creating all the rows to initalize the ‘parent’ and
‘children’ properties for each TreeViewItem in ‘rows’ based on the depth
information for each item. This method assumes that the data presented in
`rows` is in the order it should appear from top to bottom in the TreeView.  
  
Additional resources:
[SetupDepthsFromParentsAndChildren](IMGUI.Controls.TreeView.SetupDepthsFromParentsAndChildren.html),
[BuildRoot](IMGUI.Controls.TreeView.BuildRoot.html).

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

