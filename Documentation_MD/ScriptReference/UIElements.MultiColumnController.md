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

# MultiColumnController

class in UnityEngine.UIElements

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

The default controller for a multi column view. Takes care of adding the
MultiColumnCollectionHeader and reacting to the various callbacks.

### Static Properties

[cellLabelUssClassName](UIElements.MultiColumnController-
cellLabelUssClassName.html)|  The USS class name for default labels cells
inside a multi column view.  
---|---  
[cellUssClassName](UIElements.MultiColumnController-cellUssClassName.html)|
The USS class name for all cells inside a multi column view.  
[headerContainerUssClassName](UIElements.MultiColumnController-
headerContainerUssClassName.html)|  The USS class name for the header
container inside a multi column view.  
[rowContainerUssClassName](UIElements.MultiColumnController-
rowContainerUssClassName.html)|  The USS class name for all row containers
inside a multi column view.  
  
### Constructors

[MultiColumnController](UIElements.MultiColumnController-ctor.html)|
Constructor. It will create the MultiColumnCollectionHeader to use for the
view.  
---|---  
  
### Public Methods

[BindItem](UIElements.MultiColumnController.BindItem.html)|  Binds a row of
multiple cells to an item index.  
---|---  
[DestroyItem](UIElements.MultiColumnController.DestroyItem.html)|  Destroys a
VisualElement when the view is rebuilt or cleared.  
[Dispose](UIElements.MultiColumnController.Dispose.html)|  Unregisters events
and removes the header from the hierarchy.  
[MakeItem](UIElements.MultiColumnController.MakeItem.html)|  Creates a
VisualElement to use in the virtualization of the collection view. It will
create a cell for every visible column.  
[PrepareView](UIElements.MultiColumnController.PrepareView.html)|
Initialization step once the view is set. It will insert the multi column
header in the hierarchy and register to important callbacks.  
[UnbindItem](UIElements.MultiColumnController.UnbindItem.html)|  Unbinds the
row at the item index.  
  
### Events

[columnSortingChanged](UIElements.MultiColumnController-
columnSortingChanged.html)|  Raised when sorting changes for a column.  
---|---  
[headerContextMenuPopulateEvent](UIElements.MultiColumnController-
headerContextMenuPopulateEvent.html)|  Raised when a column is right-clicked
to bring context menu options.  
  
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

