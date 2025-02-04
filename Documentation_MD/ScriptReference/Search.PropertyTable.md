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

**Method group is Obsolete**  

# PropertyTable

class in UnityEditor.Search

/

Inherits from:[IMGUI.Controls.TreeView](IMGUI.Controls.TreeView.html)

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

**Obsolete** IMGUI is not support anymore. Use ITableView interface instead.

### Description

The PropertyTable provide an IMGUI widget to display search property results
in a table view.

### Inherited Members

### Properties

[baseIndent](IMGUI.Controls.TreeView-baseIndent.html)| Indent used for all
rows before the tree foldout arrows and content.  
---|---  
[cellMargin](IMGUI.Controls.TreeView-cellMargin.html)| When using a
MultiColumnHeader this value adjusts the cell rects provided for all columns
except the tree foldout column.  
[columnIndexForTreeFoldouts](IMGUI.Controls.TreeView-
columnIndexForTreeFoldouts.html)| When using a MultiColumnHeader this value
should be set to the column index in which the foldout arrows should appear.  
[customFoldoutYOffset](IMGUI.Controls.TreeView-customFoldoutYOffset.html)|
Custom vertical offset of the foldout arrow.  
[depthIndentWidth](IMGUI.Controls.TreeView-depthIndentWidth.html)| Value that
returns how far the foldouts are indented for each increasing depth value.  
[enableItemHovering](IMGUI.Controls.TreeView-enableItemHovering.html)| Set
this property true if item hover effect is wanted. Default value is false.  
[extraSpaceBeforeIconAndLabel](IMGUI.Controls.TreeView-
extraSpaceBeforeIconAndLabel.html)| Value to control the spacing before the
default icon and label. Can be used e.g for placing a toggle button to the
left of the content.  
[foldoutOverride](IMGUI.Controls.TreeView-foldoutOverride.html)| Register a
callback to this property to override the Foldout button in the TreeView.  
[foldoutWidth](IMGUI.Controls.TreeView-foldoutWidth.html)| Width of the built-
in foldout arrow.  
[getNewSelectionOverride](IMGUI.Controls.TreeView-
getNewSelectionOverride.html)| Register a callback to this field to override
how the TreeView handles selection changes in response to keys and mouse
clicks.  
[hasSearch](IMGUI.Controls.TreeView-hasSearch.html)| The current search state
of the TreeView.  
[hoveredItem](IMGUI.Controls.TreeView-hoveredItem.html)| Use this property to
detect which TreeViewItem the mouse cursor is currently hovering over in the
TreeView. This property is only valid if the enableItemHovering property has
been set to true.  
[isDragging](IMGUI.Controls.TreeView-isDragging.html)| True if the user is
currently dragging one or more items in the TreeView, and false otherwise.  
[isInitialized](IMGUI.Controls.TreeView-isInitialized.html)| The TreeView is
initialized by calling Reload(). Therefore returns false until Reload() is
called the first time.  
[multiColumnHeader](IMGUI.Controls.TreeView-multiColumnHeader.html)| Get the
MultiColumnHeader of the TreeView. Can be null if the TreeView was created
without a MultiColumnHeader.  
[rootItem](IMGUI.Controls.TreeView-rootItem.html)| The hidden root item of the
TreeView (it is never rendered).  
[rowHeight](IMGUI.Controls.TreeView-rowHeight.html)| The fixed height used for
each row in the TreeView if GetCustomRowHeight have not been overridden.  
[searchString](IMGUI.Controls.TreeView-searchString.html)| Current search
string of the TreeView.  
[showAlternatingRowBackgrounds](IMGUI.Controls.TreeView-
showAlternatingRowBackgrounds.html)| Enable this to show alternating row
background colors.  
[showBorder](IMGUI.Controls.TreeView-showBorder.html)| Enable this to show a
border around the TreeView.  
[showingHorizontalScrollBar](IMGUI.Controls.TreeView-
showingHorizontalScrollBar.html)| Returns true if the horizontal scroll bar is
showing, otherwise false.  
[showingVerticalScrollBar](IMGUI.Controls.TreeView-
showingVerticalScrollBar.html)| Returns true if the vertical scroll bar is
showing, otherwise false.  
[state](IMGUI.Controls.TreeView-state.html)| The state of the TreeView
(expanded state, selection, scroll etc.)  
[totalHeight](IMGUI.Controls.TreeView-totalHeight.html)| Returns the sum of
the TreeView row heights, the MultiColumnHeader height (if used) and the
border (if used).  
[treeViewControlID](IMGUI.Controls.TreeView-treeViewControlID.html)| The
controlID used by the TreeView to obtain keyboard control focus.  
[treeViewRect](IMGUI.Controls.TreeView-treeViewRect.html)| The Rect the
TreeView is being rendered to.  
[useScrollView](IMGUI.Controls.TreeView-useScrollView.html)| When drawing the
TreeView contents, will it be enclosed within a ScrollView?  
  
### Public Methods

[BeginRename](IMGUI.Controls.TreeView.BeginRename.html)| Shows the rename
overlay for a TreeViewItem.  
---|---  
[CollapseAll](IMGUI.Controls.TreeView.CollapseAll.html)| Collapse all expanded
items in the TreeView.  
[EndRename](IMGUI.Controls.TreeView.EndRename.html)| Ends renaming if the
rename overlay is shown. If called while the rename overlay is not being
shown, this method does nothing.  
[ExpandAll](IMGUI.Controls.TreeView.ExpandAll.html)| Expand all collapsed
items in the TreeView.  
[FrameItem](IMGUI.Controls.TreeView.FrameItem.html)| This will reveal the item
with ID id (by expanding the ancestors of that item) and will make sure it is
visible in the ScrollView.  
[GetExpanded](IMGUI.Controls.TreeView.GetExpanded.html)| Returns a list of
TreeViewItem IDs that are currently expanded in the TreeView.  
[GetRows](IMGUI.Controls.TreeView.GetRows.html)| This is the list of
TreeViewItems that have been built in BuildRows.  
[GetSelection](IMGUI.Controls.TreeView.GetSelection.html)| Returns the list of
TreeViewItem IDs that are currently selected.  
[HasFocus](IMGUI.Controls.TreeView.HasFocus.html)| Returns true if the
TreeView and its EditorWindow have keyboard focus.  
[HasSelection](IMGUI.Controls.TreeView.HasSelection.html)| Returns true if the
TreeView has a selection.  
[IsExpanded](IMGUI.Controls.TreeView.IsExpanded.html)| Returns true if the
TreeViewItem with ID id is currently expanded.  
[IsSelected](IMGUI.Controls.TreeView.IsSelected.html)| Returns true if the
TreeViewItem with ID id is currently selected.  
[OnGUI](IMGUI.Controls.TreeView.OnGUI.html)| This is the main GUI method of
the TreeView, where the TreeViewItems are processed and drawn.  
[Reload](IMGUI.Controls.TreeView.Reload.html)| Call this to force the TreeView
to reload its data. This in turn causes BuildRoot and BuildRows to be called.  
[Repaint](IMGUI.Controls.TreeView.Repaint.html)| Request a repaint of the
window that the TreeView is rendered in.  
[SelectAllRows](IMGUI.Controls.TreeView.SelectAllRows.html)| Selects all rows
in the TreeView.  
[SetExpanded](IMGUI.Controls.TreeView.SetExpanded.html)| Set a single
TreeViewItem to be expanded or collapsed.  
[SetExpandedRecursive](IMGUI.Controls.TreeView.SetExpandedRecursive.html)|
Expand or collapse all items under item with id.  
[SetFocus](IMGUI.Controls.TreeView.SetFocus.html)| Calling this function
changes the keyboard focus to the TreeView.  
[SetFocusAndEnsureSelectedItem](IMGUI.Controls.TreeView.SetFocusAndEnsureSelectedItem.html)|
Calling this function changes the keyboard focus to the TreeView and ensures
an item is selected. Use this function to enable key navigation of the
TreeView.  
[SetSelection](IMGUI.Controls.TreeView.SetSelection.html)| Set the selected
items of the TreeView.  
  
### Protected Methods

[AddExpandedRows](IMGUI.Controls.TreeView.AddExpandedRows.html)| Adds the
expanded rows of the full tree to the input list. Only use this method if a
full tree was built in BuildRoot.  
---|---  
[AfterRowsGUI](IMGUI.Controls.TreeView.AfterRowsGUI.html)| This is called
after all rows have their RowGUI called.  
[BeforeRowsGUI](IMGUI.Controls.TreeView.BeforeRowsGUI.html)| This is called
before any rows have their RowGUI called.  
[BuildRoot](IMGUI.Controls.TreeView.BuildRoot.html)| Abstract method that is
required to be implemented. By default this method should create the full tree
of TreeViewItems and return the root.  
[BuildRows](IMGUI.Controls.TreeView.BuildRows.html)| Override this method to
take control of how the rows are generated.  
[CanBeParent](IMGUI.Controls.TreeView.CanBeParent.html)| Override this method
to control which items are allowed to be parents.  
[CanChangeExpandedState](IMGUI.Controls.TreeView.CanChangeExpandedState.html)|
Override this method to control whether an item can be expanded or collapsed
by key or mouse.  
[CanMultiSelect](IMGUI.Controls.TreeView.CanMultiSelect.html)| Override this
method to control whether the item can be part of a multiselection.  
[CanRename](IMGUI.Controls.TreeView.CanRename.html)| Override this method to
control whether the item can be renamed using a keyboard shortcut or when
clicking an already selected item.  
[CanStartDrag](IMGUI.Controls.TreeView.CanStartDrag.html)| This function is
called whenever a TreeViewItem is clicked and dragged. It returns false by
default.  
[CenterRectUsingSingleLineHeight](IMGUI.Controls.TreeView.CenterRectUsingSingleLineHeight.html)|
Modifies the input rect so it is centered and have a height equal to
EditorGUIUtility.singleLineHeight.  
[CommandEventHandling](IMGUI.Controls.TreeView.CommandEventHandling.html)|
This function is called automatically and handles the ExecuteCommand events
for “SelectAll” and “FrameSelection”. Override this function to extend or
avoid Command events.  
[ContextClicked](IMGUI.Controls.TreeView.ContextClicked.html)| Override this
method to handle context clicks outside any items (but still in the TreeView
rect).  
[ContextClickedItem](IMGUI.Controls.TreeView.ContextClickedItem.html)|
Override this method to handle a context click on an item with ID
TreeViewItem.id.  
[DoesItemMatchSearch](IMGUI.Controls.TreeView.DoesItemMatchSearch.html)|
Override this function to extend or change the search behavior.  
[DoubleClickedItem](IMGUI.Controls.TreeView.DoubleClickedItem.html)| Override
this method to handle double click events on an item.  
[ExpandedStateChanged](IMGUI.Controls.TreeView.ExpandedStateChanged.html)|
Override to get notified when items are expanded or collapsed. This is a
general notification that the expanded state has changed.  
[FindItem](IMGUI.Controls.TreeView.FindItem.html)| Finds a TreeViewItem by an
ID.  
[FindRowOfItem](IMGUI.Controls.TreeView.FindRowOfItem.html)| Returns the row
of the given TreeViewItem.  
[FindRows](IMGUI.Controls.TreeView.FindRows.html)| Useful for converting from
TreeViewItem IDs to TreeViewItems using the current rows.  
[GetAncestors](IMGUI.Controls.TreeView.GetAncestors.html)| This method is e.g.
used for revealing items that are currently under a collapsed item.  
[GetCellRectForTreeFoldouts](IMGUI.Controls.TreeView.GetCellRectForTreeFoldouts.html)|
Utility for multi column setups. This method will clip the input rowRect
against the column rect defined by columnIndexForTreeFoldouts to get the cell
rect where the the foldout arrows appear.  
[GetContentIndent](IMGUI.Controls.TreeView.GetContentIndent.html)| Returns the
horizontal content offset for an item. This is where the content should begin
(after the foldout arrow).  
[GetCustomRowHeight](IMGUI.Controls.TreeView.GetCustomRowHeight.html)|
Override to control individual row heights.  
[GetDescendantsThatHaveChildren](IMGUI.Controls.TreeView.GetDescendantsThatHaveChildren.html)|
Returns all descendants for the item with ID id that have children.  
[GetFirstAndLastVisibleRows](IMGUI.Controls.TreeView.GetFirstAndLastVisibleRows.html)|
Returns the first and the last indices of the rows that are visible in the
scroll view of the TreeView.  
[GetFoldoutIndent](IMGUI.Controls.TreeView.GetFoldoutIndent.html)| Returns the
horizontal foldout offset for an item. This is where the foldout arrow is
rendered.  
[GetRenameRect](IMGUI.Controls.TreeView.GetRenameRect.html)| Override this
method if custom GUI handling are used in RowGUI. This method for controls
where the rename overlay appears.  
[GetRowRect](IMGUI.Controls.TreeView.GetRowRect.html)| Get the rect for a row.  
[HandleDragAndDrop](IMGUI.Controls.TreeView.HandleDragAndDrop.html)| Override
this function to control the drag and drop behavior of the TreeView.  
[KeyEvent](IMGUI.Controls.TreeView.KeyEvent.html)| Override this method to
handle events when the TreeView has keyboard focus.  
[RefreshCustomRowHeights](IMGUI.Controls.TreeView.RefreshCustomRowHeights.html)|
Refreshes the cache of custom row rects based on the heights returned by
GetCustomRowHeight.  
[RenameEnded](IMGUI.Controls.TreeView.RenameEnded.html)| Called when rename
ends either by the user completing the renaming process, when the rename
overlay loses focus or is closed using EndRename.  
[RowGUI](IMGUI.Controls.TreeView.RowGUI.html)| Override this method to add
custom GUI content for the rows in the TreeView.  
[SearchChanged](IMGUI.Controls.TreeView.SearchChanged.html)| Override the
method to get notified of search string changes.  
[SelectionChanged](IMGUI.Controls.TreeView.SelectionChanged.html)| Override
the method to get notified of selection changes.  
[SelectionClick](IMGUI.Controls.TreeView.SelectionClick.html)| Use this method
in RowGUI to peform the logic of a mouse click.  
[SetupDragAndDrop](IMGUI.Controls.TreeView.SetupDragAndDrop.html)| This
function is called when CanStartDrag returns true.  
[SingleClickedItem](IMGUI.Controls.TreeView.SingleClickedItem.html)| Override
this method to handle single click events on an item.  
[SortItemIDsInRowOrder](IMGUI.Controls.TreeView.SortItemIDsInRowOrder.html)|
Returns a list sorted in the order in which they are shown in the TreeView.  
  
### Static Methods

[CreateChildListForCollapsedParent](IMGUI.Controls.TreeView.CreateChildListForCollapsedParent.html)|
Creates a dummy TreeViewItem list. Useful when overriding BuildRows to prevent
building a full tree of items.  
---|---  
[IsChildListForACollapsedParent](IMGUI.Controls.TreeView.IsChildListForACollapsedParent.html)|
Utility method for checking if the childList is identical to the one returned
by the CreateChildListForCollapsedParent method.  
[SetupDepthsFromParentsAndChildren](IMGUI.Controls.TreeView.SetupDepthsFromParentsAndChildren.html)|
Utility method using the depth of the input TreeViewItem to set the correct
depths for all its descendant TreeViewItems.  
[SetupParentsAndChildrenFromDepths](IMGUI.Controls.TreeView.SetupParentsAndChildrenFromDepths.html)|
Utility method for initializing all the parent and children properties of the
rows using the order and the depths values that have been set.  
  
### Delegates

[DoFoldoutCallback](IMGUI.Controls.TreeView.DoFoldoutCallback.html)| Callback
signature used to override the TreeView foldout. See foldoutOverride.  
---|---  
[GetNewSelectionFunction](IMGUI.Controls.TreeView.GetNewSelectionFunction.html)|
A callback which determines how TreeView handles selection changes in response
to keys and mouse clicks.  
  
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

