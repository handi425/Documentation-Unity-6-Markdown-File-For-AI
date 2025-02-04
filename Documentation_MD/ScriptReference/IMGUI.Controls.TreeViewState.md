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

# TreeViewState

class in UnityEditor.IMGUI.Controls

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

### Description

The TreeViewState contains serializable state information for the TreeView.

This is primarily state that the user could have changed by interacting with
the TreeView, for example the selection state, expanded state, navigation
state and scroll state.  
  
The TreeViewState is the only state that should be serialized/deserialized in
the TreeView. The TreeView itself is not serializable and should be
reconstructed from the tree data it is representing.  
  
All the state contained in this class is updated by the TreeView itself.
Access to this state can also be done through the TreeView API.

### Properties

[expandedIDs](IMGUI.Controls.TreeViewState-expandedIDs.html)| This is the list
of currently expanded TreeViewItem IDs.  
---|---  
[lastClickedID](IMGUI.Controls.TreeViewState-lastClickedID.html)| The ID for
the TreeViewItem that currently is being used for multi selection and key
navigation.  
[scrollPos](IMGUI.Controls.TreeViewState-scrollPos.html)| The current scroll
values of the TreeView's scroll view.  
[searchString](IMGUI.Controls.TreeViewState-searchString.html)| Search string
state that can be used in the TreeView to filter the tree data when creating
the TreeViewItems.  
[selectedIDs](IMGUI.Controls.TreeViewState-selectedIDs.html)| Selected
TreeViewItem IDs. Use of the SetSelection and IsSelected API will access this
state.  
  
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

