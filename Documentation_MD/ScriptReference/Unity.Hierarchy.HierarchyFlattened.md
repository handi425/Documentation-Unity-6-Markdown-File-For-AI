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

# HierarchyFlattened

class in Unity.Hierarchy

/

Implemented
in:[UnityEngine.HierarchyCoreModule](UnityEngine.HierarchyCoreModule.html)

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

Represents a read-only array of
[HierarchyFlattenedNode](Unity.Hierarchy.HierarchyFlattenedNode.html) over a
[Hierarchy](Unity.Hierarchy.Hierarchy.html). Used as an acceleration structure
for query purposes.

Querying information about nodes completes much faster than the same methods
on [Hierarchy](Unity.Hierarchy.Hierarchy.html) because they are stored during
the updates.

### Properties

[Count](Unity.Hierarchy.HierarchyFlattened.Count.html)|  The total number of
nodes.  
---|---  
[Hierarchy](Unity.Hierarchy.HierarchyFlattened.Hierarchy.html)|  Accesses the
hierarchy.  
[IsCreated](Unity.Hierarchy.HierarchyFlattened.IsCreated.html)|  Whether this
object is valid and uses memory or not.  
[this[int]](Unity.Hierarchy.HierarchyFlattened.Index_operator.html)|  Gets the
HierarchyFlattenedNode at a specified index.  
[UpdateNeeded](Unity.Hierarchy.HierarchyFlattened.UpdateNeeded.html)|
Determines if the flattened hierarchy needs an update.  
[Updating](Unity.Hierarchy.HierarchyFlattened.Updating.html)|  Whether the
flattened hierarchy is currently updating.  
  
### Constructors

[HierarchyFlattened](Unity.Hierarchy.HierarchyFlattened-ctor.html)|
Cosntructs a new HierarchyFlattened.  
---|---  
  
### Public Methods

[Contains](Unity.Hierarchy.HierarchyFlattened.Contains.html)|  Determines if a
specified node is in the hierarchy flattened.  
---|---  
[Dispose](Unity.Hierarchy.HierarchyFlattened.Dispose.html)|  Disposes this
object to release its memory.  
[EnumerateChildren](Unity.Hierarchy.HierarchyFlattened.EnumerateChildren.html)|
Gets an enumerable of children HierarchyNode for the specified node.  
[GetChildrenCount](Unity.Hierarchy.HierarchyFlattened.GetChildrenCount.html)|
Gets the number of child nodes that a hierarchy node has.  
[GetChildrenCountRecursive](Unity.Hierarchy.HierarchyFlattened.GetChildrenCountRecursive.html)|
Gets the number of child nodes that a hierarchy node has, including children
of children.  
[GetDepth](Unity.Hierarchy.HierarchyFlattened.GetDepth.html)|  Determines the
depth of a node.  
[GetEnumerator](Unity.Hierarchy.HierarchyFlattened.GetEnumerator.html)|  Gets
the HierarchyFlattenedNode enumerator.  
[GetNextSibling](Unity.Hierarchy.HierarchyFlattened.GetNextSibling.html)|
Gets the next sibling of a node.  
[GetParent](Unity.Hierarchy.HierarchyFlattened.GetParent.html)|  Gets the
parent of a hierarchy node.  
[IndexOf](Unity.Hierarchy.HierarchyFlattened.IndexOf.html)|  Gets the zero-
based index of a specified node.  
[Update](Unity.Hierarchy.HierarchyFlattened.Update.html)|  Updates the
flattened hierarchy and requests a rebuild of the list of
HierarchyFlattenedNode from the Hierarchy topology.  
[UpdateIncremental](Unity.Hierarchy.HierarchyFlattened.UpdateIncremental.html)|
Updates the flattened hierarchy incrementally.  
[UpdateIncrementalTimed](Unity.Hierarchy.HierarchyFlattened.UpdateIncrementalTimed.html)|
Incrementally updates the flattened hierarchy until a time limit is reached.  
  
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

