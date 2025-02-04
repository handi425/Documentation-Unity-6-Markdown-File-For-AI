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

# HierarchyDropFlags

enumeration

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

Define how dragged objects should be dropped relative to already existing
Hierarchy items.

### Properties

[None](HierarchyDropFlags.None.html)| Insert dragged object in the Hierarchy.
The default flag value is 0. The only case in which DropMode is 0 is when
dragging outside items and parentForDraggedObjects is set. Then
dropTargetInstanceID is 0 and the target is passed to the
parentForDraggedObjects.  
---|---  
[DropUpon](HierarchyDropFlags.DropUpon.html)| Drop a dragged object on the
Hierarchy item the mouse is hovering over. The hovered-over item is the
dropTargetInstanceID and the dropped object is inserted as a child of the
target. This flag is also used when dragging and dropping objects from outside
the Hierarchy and into and below the last item in the Hierarchy to add to the
Scene. In this case, the dropTargetInstanceID is the Scene handle.  
[DropBetween](HierarchyDropFlags.DropBetween.html)| Drop a dragged object
between two Hierarchy sibling items the mouse is hovered over. The
dropTargetInstanceID is the Hierarchy item above the hover point, the dropped
object is inserted below the target.  
[DropAfterParent](HierarchyDropFlags.DropAfterParent.html)| Drop a dragged
object into the first child position after the parent of the Hierarchy item
when the mouse is hovering between the parent and the first child. The
dropTargetInstanceID is the first child under a parent and the dropped object
is inserted between the parent and the first child. When using
DropAfterParent, DropBetween and DropAbove are also used to provide
information to locate the dropped object.  
[SearchActive](HierarchyDropFlags.SearchActive.html)| This flag is set if the
Hierarchy is showing search results. If a search is active, only DropUpon is
allowed (no other actions can be performed on a partial list of items).  
[DropAbove](HierarchyDropFlags.DropAbove.html)| Drop a dragged object above
the Hierarchy sibling item the mouse is hovered over. The dropTargetInstanceID
is the Hierarchy item below the hover point and the dropped object is inserted
above the target.  
  
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

