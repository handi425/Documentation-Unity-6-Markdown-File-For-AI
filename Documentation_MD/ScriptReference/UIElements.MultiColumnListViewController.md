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

# MultiColumnListViewController

class in UnityEngine.UIElements

/

Inherits
from:[UIElements.BaseListViewController](UIElements.BaseListViewController.html)

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

Multi-column list view controller. View controllers of this type are meant to
take care of data virtualized by any
[MultiColumnListView](UIElements.MultiColumnListView.html) inheritor.

### Properties

[columnController](UIElements.MultiColumnListViewController-
columnController.html)|  The column controller, taking care of operations on
the header.  
---|---  
  
### Constructors

[MultiColumnListViewController](UIElements.MultiColumnListViewController-
ctor.html)|  The constructor for MultiColumnListViewController.  
---|---  
  
### Public Methods

[Dispose](UIElements.MultiColumnListViewController.Dispose.html)|  Unregisters
events and removes the header from the hierarchy.  
---|---  
  
### Inherited Members

### Properties

[baseListView](UIElements.BaseListViewController-baseListView.html)|  View for
this controller, cast as a BaseListView.  
---|---  
[itemsSource](UIElements.CollectionViewController-itemsSource.html)|  The
items source stored in a non-generic list.  
[view](UIElements.CollectionViewController-view.html)|  The view for this
controller.  
  
### Public Methods

[AddItems](UIElements.BaseListViewController.AddItems.html)|  Adds a certain
amount of items at the end of the collection.  
---|---  
[ClearItems](UIElements.BaseListViewController.ClearItems.html)|  Removes all
items from the source.  
[Move](UIElements.BaseListViewController.Move.html)|  Moves an item in the
source.  
[NeedsDragHandle](UIElements.BaseListViewController.NeedsDragHandle.html)|
Returns whether this item needs a drag handle or not with the Animated drag
mode.  
[RemoveItem](UIElements.BaseListViewController.RemoveItem.html)|  Removes an
item from the source, by index.  
[RemoveItems](UIElements.BaseListViewController.RemoveItems.html)|  Removes
items from the source, by indices.  
[GetIdForIndex](UIElements.CollectionViewController.GetIdForIndex.html)|
Returns the id for the specified index.  
[GetIndexForId](UIElements.CollectionViewController.GetIndexForId.html)|
Returns the index for the specified id.  
[GetItemForId](UIElements.CollectionViewController.GetItemForId.html)|
Returns the item with the specified ID.  
[GetItemForIndex](UIElements.CollectionViewController.GetItemForIndex.html)|
Returns the item with the specified index.  
[GetItemsCount](UIElements.CollectionViewController.GetItemsCount.html)|
Returns the expected item count in the source.  
[SetView](UIElements.CollectionViewController.SetView.html)|  Sets the view
for this controller.  
  
### Protected Methods

[RaiseItemsAdded](UIElements.BaseListViewController.RaiseItemsAdded.html)|
Invokes the itemsAdded event.  
---|---  
[RaiseItemsRemoved](UIElements.BaseListViewController.RaiseItemsRemoved.html)|
Invokes the itemsRemoved event.  
[RaiseOnSizeChanged](UIElements.BaseListViewController.RaiseOnSizeChanged.html)|
Invokes the itemsSourceSizeChanged event.  
[BindItem](UIElements.CollectionViewController.BindItem.html)|  Binds a row to
an item index.  
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

[itemsAdded](UIElements.BaseListViewController-itemsAdded.html)|  Raised when
an item is added to the CollectionViewController.itemsSource.  
---|---  
[itemsRemoved](UIElements.BaseListViewController-itemsRemoved.html)|  Raised
when an item is removed from the CollectionViewController.itemsSource.  
[itemsSourceSizeChanged](UIElements.BaseListViewController-
itemsSourceSizeChanged.html)|  Raised when the
CollectionViewController.itemsSource size changes.  
[itemIndexChanged](UIElements.CollectionViewController-itemIndexChanged.html)|
Raised when an item in the source changes index. The first argument is source
index, second is destination index.  
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

