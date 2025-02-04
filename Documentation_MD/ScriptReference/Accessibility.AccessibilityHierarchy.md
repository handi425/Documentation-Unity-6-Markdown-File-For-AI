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

# AccessibilityHierarchy

class in UnityEngine.Accessibility

/

Implemented
in:[UnityEngine.AccessibilityModule](UnityEngine.AccessibilityModule.html)

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

Represents the hierarchy data model that the screen reader uses for reading
and navigating the UI.

A hierarchy must be set to active through
[AssistiveSupport.activeHierarchy](Accessibility.AssistiveSupport-
activeHierarchy.html) when the screen reader is on for the screen reader to
function. If a hierarchy is not set active, the screen reader cannot read and
navigate through the UI. Once an active hierarchy is set, if the hierarchy is
modified, the screen reader must be notified by calling
AssistiveSupport.NotificationDispatcher.SendLayoutChanged or
AssistiveSupport.NotificationDispatcher.SendScreenChanged (depending if the
changes are only at the layout level, or a more considerable screen change).
Modifications in the hierarchy consist of calls to:

  * [AccessibilityHierarchy.AddNode](Accessibility.AccessibilityHierarchy.AddNode.html)
  * [AccessibilityHierarchy.Clear](Accessibility.AccessibilityHierarchy.Clear.html)
  * [AccessibilityHierarchy.InsertNode](Accessibility.AccessibilityHierarchy.InsertNode.html)
  * [AccessibilityHierarchy.MoveNode](Accessibility.AccessibilityHierarchy.MoveNode.html)
  * [AccessibilityHierarchy.RemoveNode](Accessibility.AccessibilityHierarchy.RemoveNode.html)
  * Modifications to node [AccessibilityNode.frame](Accessibility.AccessibilityNode-frame.html) values.

### Properties

[rootNodes](Accessibility.AccessibilityHierarchy-rootNodes.html)|  The root
nodes of the hierarchy.  
---|---  
  
### Constructors

[AccessibilityHierarchy](Accessibility.AccessibilityHierarchy-ctor.html)|
Initializes and returns an instance of an AccessibilityHierarchy.  
---|---  
  
### Public Methods

[AddNode](Accessibility.AccessibilityHierarchy.AddNode.html)|  Creates and
adds a new node with the given label in this hierarchy under the given parent
node. If no parent is provided, the new node is added as a root in the
hierarchy.  
---|---  
[Clear](Accessibility.AccessibilityHierarchy.Clear.html)|  Resets the
hierarchy to an empty state, removing all the nodes and removing focus.  
[ContainsNode](Accessibility.AccessibilityHierarchy.ContainsNode.html)|
Returns whether a given node exists in the hierarchy.  
[GetLowestCommonAncestor](Accessibility.AccessibilityHierarchy.GetLowestCommonAncestor.html)|
Retrieves the lowest common ancestor of two nodes in the hierarchy. The lowest
common ancestor is the node that is the common node that both nodes share in
their path to the root node of their branch in the hierarchy.  
[InsertNode](Accessibility.AccessibilityHierarchy.InsertNode.html)|  Creates
and inserts a new node with the given label at the given index in this
hierarchy under the given parent node. If no parent is provided, the new node
is inserted at the given index as a root in the hierarchy.  
[MoveNode](Accessibility.AccessibilityHierarchy.MoveNode.html)|  Moves the
node elsewhere in the hierarchy, which causes the given node to be parented by
a different node in the hierarchy. An optional index can be supplied for
specifying the position within the list of children the moved node should take
(zero-based). If no index is supplied, the node is added as the last child of
the new parent by default. Root nodes can be moved elsewhere in the hierarchy,
therefore ceasing to be a root. Non-root nodes can be moved to become a root
node by providing null as the new parent node.Warning: The moving operation is
costly as many checks have to be executed to guarantee the integrity of the
hierarchy. Therefore this operation should not be done excessively as it may
affect performance.  
[RefreshNodeFrames](Accessibility.AccessibilityHierarchy.RefreshNodeFrames.html)|
Refreshes all the node frames (i.e. the screen elements' positions) for the
hierarchy.  
[RemoveNode](Accessibility.AccessibilityHierarchy.RemoveNode.html)|  Removes
the node from the hierarchy. Can also optionally remove nodes under the given
node depending on the value of the removeChildren parameter.  
[TryGetNode](Accessibility.AccessibilityHierarchy.TryGetNode.html)|  Tries to
get the node in this hierarchy that has the given ID.  
[TryGetNodeAt](Accessibility.AccessibilityHierarchy.TryGetNodeAt.html)|  Tries
to retrieve the node at the given position on the screen.  
  
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

