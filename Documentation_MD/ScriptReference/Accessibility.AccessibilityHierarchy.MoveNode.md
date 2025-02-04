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

#
[AccessibilityHierarchy](Accessibility.AccessibilityHierarchy.html).MoveNode

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

public bool
MoveNode([Accessibility.AccessibilityNode](Accessibility.AccessibilityNode.html)
node, [Accessibility.AccessibilityNode](Accessibility.AccessibilityNode.html)
newParent, int newChildIndex);

### Parameters

node | The node to move.  
---|---  
newParent | The new parent of the moved node, or `null` if the moved node should be made into a root node.  
newChildIndex | An optional zero-based index for positioning the moved node in the new parent's children list, or in the list of roots if the node is becoming a root node. If the index is not provided or is invalid, the moved node will be the last child of its parent.  
  
### Returns

**bool** Whether the node was successfully moved.

### Description

Moves the node elsewhere in the hierarchy, which causes the given node to be
parented by a different node in the hierarchy. An optional index can be
supplied for specifying the position within the list of children the moved
node should take (zero-based). If no index is supplied, the node is added as
the last child of the new parent by default.  
Root nodes can be moved elsewhere in the hierarchy, therefore ceasing to be a
root. Non-root nodes can be moved to become a root node by providing `null` as
the new parent node.  
  
**Warning:** The moving operation is costly as many checks have to be executed
to guarantee the integrity of the hierarchy. Therefore this operation should
not be done excessively as it may affect performance.  

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

