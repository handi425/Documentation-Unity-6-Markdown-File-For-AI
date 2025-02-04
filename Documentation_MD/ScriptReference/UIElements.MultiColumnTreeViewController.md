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

# MultiColumnTreeViewController

class in UnityEngine.UIElements

/

Inherits
from:[UIElements.BaseTreeViewController](UIElements.BaseTreeViewController.html)

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

Multi-column tree view controller. View controllers of this type are meant to
take care of data virtualized by any
[MultiColumnTreeView](UIElements.MultiColumnTreeView.html) inheritor.

### Properties

[columnController](UIElements.MultiColumnTreeViewController-
columnController.html)|  The column controller, taking care of operations on
the header.  
---|---  
  
### Public Methods

[Dispose](UIElements.MultiColumnTreeViewController.Dispose.html)|  Unregisters
events and removes the header from the hierarchy.  
---|---  
  
### Inherited Members

### Properties

[baseTreeView](UIElements.BaseTreeViewController-baseTreeView.html)|  View for
this controller, cast as a BaseTreeView.  
---|---  
[itemsSource](UIElements.BaseTreeViewController-itemsSource.html)|  Items for
this tree. Contains items that are expanded in the tree.  
[view](UIElements.CollectionViewController-view.html)|  The view for this
controller.  
  
### Public Methods

[CanChangeExpandedState](UIElements.BaseTreeViewController.CanChangeExpandedState.html)|
Determines whether the item with the specified ID can be expanded or
collapsed.  
---|---  
[CollapseAll](UIElements.BaseTreeViewController.CollapseAll.html)|  Collapses
all items in the tree and refreshes the view.  
[CollapseItem](UIElements.BaseTreeViewController.CollapseItem.html)|
Collapses the item with the specified ID, hiding its children. Allows to
collapse the whole hierarchy under that item.  
[CollapseItemByIndex](UIElements.BaseTreeViewController.CollapseItemByIndex.html)|
Collapses the item with the specified index, hiding its children. Allows to
collapse the whole hierarchy under that item.  
[Exists](UIElements.BaseTreeViewController.Exists.html)|  Checks if an ID
exists within this tree.  
[ExpandAll](UIElements.BaseTreeViewController.ExpandAll.html)|  Expands all
items in the tree and refreshes the view.  
[ExpandItem](UIElements.BaseTreeViewController.ExpandItem.html)|  Expands the
item with the specified ID, making its children visible. Allows to expand the
whole hierarchy under that item.  
[ExpandItemByIndex](UIElements.BaseTreeViewController.ExpandItemByIndex.html)|
Expands the item with the specified index, making his children visible. Allows
to expand the whole hierarchy under that item.  
[GetAllItemIds](UIElements.BaseTreeViewController.GetAllItemIds.html)|
Returns all item IDs that can be found in the tree, optionally specifying root
IDs from where to start.  
[GetChildIndexForId](UIElements.BaseTreeViewController.GetChildIndexForId.html)|
Gets the child index under the parent of the item with the specified ID.  
[GetChildrenIds](UIElements.BaseTreeViewController.GetChildrenIds.html)|  Get
all children of a specific ID in the tree.  
[GetChildrenIdsByIndex](UIElements.BaseTreeViewController.GetChildrenIdsByIndex.html)|
Gets the children IDs of the item with the specified index.  
[GetIdForIndex](UIElements.BaseTreeViewController.GetIdForIndex.html)|
Returns the ID for a specified index in the visible items source.  
[GetIndentationDepth](UIElements.BaseTreeViewController.GetIndentationDepth.html)|
Returns the depth of the element at that ID.  
[GetIndentationDepthByIndex](UIElements.BaseTreeViewController.GetIndentationDepthByIndex.html)|
Return the depth of the element at that index.  
[GetIndexForId](UIElements.BaseTreeViewController.GetIndexForId.html)|
Returns the index in the source of the item, by ID.  
[GetParentId](UIElements.BaseTreeViewController.GetParentId.html)|  Returns
the parent ID of an item, by ID.  
[GetRootItemIds](UIElements.BaseTreeViewController.GetRootItemIds.html)|
Returns the root items of the tree, by IDs.  
[GetTreeItemsCount](UIElements.BaseTreeViewController.GetTreeItemsCount.html)|
Get the number of items in the whole tree.  
[HasChildren](UIElements.BaseTreeViewController.HasChildren.html)|  Return
whether the item with the specified ID has one or more child.  
[HasChildrenByIndex](UIElements.BaseTreeViewController.HasChildrenByIndex.html)|
Return whether the item with the specified index has one or more child.  
[IsExpanded](UIElements.BaseTreeViewController.IsExpanded.html)|  Return
whether the item with the specified ID is expanded in the tree.  
[IsExpandedByIndex](UIElements.BaseTreeViewController.IsExpandedByIndex.html)|
Return whether the item with the specified index is expanded in the tree.  
[Move](UIElements.BaseTreeViewController.Move.html)|  Moves an item by ID, to
a new parent and child index.  
[TryRemoveItem](UIElements.BaseTreeViewController.TryRemoveItem.html)|
Removes an item by id.  
[GetItemForId](UIElements.CollectionViewController.GetItemForId.html)|
Returns the item with the specified ID.  
[GetItemForIndex](UIElements.CollectionViewController.GetItemForIndex.html)|
Returns the item with the specified index.  
[GetItemsCount](UIElements.CollectionViewController.GetItemsCount.html)|
Returns the expected item count in the source.  
[SetView](UIElements.CollectionViewController.SetView.html)|  Sets the view
for this controller.  
  
### Protected Methods

[BindItem](UIElements.CollectionViewController.BindItem.html)|  Binds a row to
an item index.  
---|---  
[DestroyItem](UIElements.CollectionViewController.DestroyItem.html)|  Destroys
a VisualElement when the view is rebuilt or cleared.  
[MakeItem](UIElements.CollectionViewController.MakeItem.html)|  Creates a
VisualElement to use in the virtualization of the collection view.  
[PrepareView](UIElements.CollectionViewController.PrepareView.html)|
Initialization step once the view is set.  
[RaiseItemIndexChanged](UIElements.CollectionViewController.RaiseItemIndexChanged.html)|
Invokes the itemIndexChanged event.  
[RaiseItemsSourceChanged](UIElements.CollectionViewController.RaiseItemsSourceChanged.html)|
Invokes the itemsSourceChanged event.  
[SetItemsSourceWithoutNotify](UIElements.CollectionViewController.SetItemsSourceWithoutNotify.html)|
Set the itemsSource without raising the itemsSourceChanged event.  
[UnbindItem](UIElements.CollectionViewController.UnbindItem.html)|  Unbinds a
row to an item index.  
  
### Events

[itemIndexChanged](UIElements.CollectionViewController-itemIndexChanged.html)|
Raised when an item in the source changes index. The first argument is source
index, second is destination index.  
---|---  
[itemsSourceChanged](UIElements.CollectionViewController-
itemsSourceChanged.html)|  Raised when the itemsSource changes.  
  
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

