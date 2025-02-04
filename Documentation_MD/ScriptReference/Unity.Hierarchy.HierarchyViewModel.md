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

# HierarchyViewModel

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

A hierarchy view model is a read-only filtering view of a
[HierarchyFlattened](Unity.Hierarchy.HierarchyFlattened.html).

### Properties

[Count](Unity.Hierarchy.HierarchyViewModel.Count.html)|  The total number of
nodes.  
---|---  
[Hierarchy](Unity.Hierarchy.HierarchyViewModel.Hierarchy.html)|  Accesses the
Hierarchy.  
[HierarchyFlattened](Unity.Hierarchy.HierarchyViewModel.HierarchyFlattened.html)|
Accesses the HierarchyFlattened.  
[IsCreated](Unity.Hierarchy.HierarchyViewModel.IsCreated.html)|  Whether this
object is valid and uses memory.  
[this[int]](Unity.Hierarchy.HierarchyViewModel.Index_operator.html)|  Gets the
HierarchyNode at a specified index.  
[UpdateNeeded](Unity.Hierarchy.HierarchyViewModel.UpdateNeeded.html)|  Whether
the hierarchy view model requires an update.  
[Updating](Unity.Hierarchy.HierarchyViewModel.Updating.html)|  Whether the
hierarchy view model is currently updating.  
  
### Constructors

[HierarchyViewModel](Unity.Hierarchy.HierarchyViewModel-ctor.html)|
Cosntructs a new HierarchyViewModel.  
---|---  
  
### Public Methods

[ClearFlags](Unity.Hierarchy.HierarchyViewModel.ClearFlags.html)|  Clears the
specified flags on all hierarchy nodes.  
---|---  
[Contains](Unity.Hierarchy.HierarchyViewModel.Contains.html)|  Determines if a
specified node is in the hierarchy view model.  
[Dispose](Unity.Hierarchy.HierarchyViewModel.Dispose.html)|  Disposes this
object and releases its memory.  
[DoesNotHaveAllFlags](Unity.Hierarchy.HierarchyViewModel.DoesNotHaveAllFlags.html)|
Gets whether or not all of the specified flags are not set on any hierarchy
node.  
[DoesNotHaveAllFlagsCount](Unity.Hierarchy.HierarchyViewModel.DoesNotHaveAllFlagsCount.html)|
Gets the number of nodes that do not have all of the specified flags set.  
[DoesNotHaveAnyFlags](Unity.Hierarchy.HierarchyViewModel.DoesNotHaveAnyFlags.html)|
Gets whether or not any of the specified flags are not set on any hierarchy
node.  
[DoesNotHaveAnyFlagsCount](Unity.Hierarchy.HierarchyViewModel.DoesNotHaveAnyFlagsCount.html)|
Gets the number of nodes that do not have any of the specified flags set.  
[EnumerateNodesWithAllFlags](Unity.Hierarchy.HierarchyViewModel.EnumerateNodesWithAllFlags.html)|
Gets an enumerable of all hierarchy nodes that have all of the specified flags
set.  
[EnumerateNodesWithAnyFlags](Unity.Hierarchy.HierarchyViewModel.EnumerateNodesWithAnyFlags.html)|
Gets an enumerable of all hierarchy nodes that have any of the specified flags
set.  
[EnumerateNodesWithoutAllFlags](Unity.Hierarchy.HierarchyViewModel.EnumerateNodesWithoutAllFlags.html)|
Gets an enumerable of all hierarchy nodes that do not have all of the
specified flags set.  
[EnumerateNodesWithoutAnyFlags](Unity.Hierarchy.HierarchyViewModel.EnumerateNodesWithoutAnyFlags.html)|
Gets an enumerable of all hierarchy nodes that do not have any of the
specified flags set.  
[GetChildrenCount](Unity.Hierarchy.HierarchyViewModel.GetChildrenCount.html)|
Gets the number of child nodes that a hierarchy node has.  
[GetChildrenCountRecursive](Unity.Hierarchy.HierarchyViewModel.GetChildrenCountRecursive.html)|
Gets the number of child nodes that a hierarchy node has, including children
of children.  
[GetDepth](Unity.Hierarchy.HierarchyViewModel.GetDepth.html)|  Determines the
depth of a node.  
[GetEnumerator](Unity.Hierarchy.HierarchyViewModel.GetEnumerator.html)|  Gets
the HierarchyNode enumerator.  
[GetFlags](Unity.Hierarchy.HierarchyViewModel.GetFlags.html)|  Gets all the
flags set on a given hierarchy node.  
[GetIndicesWithAllFlags](Unity.Hierarchy.HierarchyViewModel.GetIndicesWithAllFlags.html)|
Gets the indices for all hierarchy nodes that have all of the specified flags
set.  
[GetIndicesWithAnyFlags](Unity.Hierarchy.HierarchyViewModel.GetIndicesWithAnyFlags.html)|
Gets the indices for all hierarchy nodes that have any of the specified flags
set.  
[GetIndicesWithoutAllFlags](Unity.Hierarchy.HierarchyViewModel.GetIndicesWithoutAllFlags.html)|
Gets the indices of all hierarchy nodes that do not have all of the specified
flags set.  
[GetIndicesWithoutAnyFlags](Unity.Hierarchy.HierarchyViewModel.GetIndicesWithoutAnyFlags.html)|
Gets the indices of all hierarchy nodes that do not have any of the specified
flags set.  
[GetNextSibling](Unity.Hierarchy.HierarchyViewModel.GetNextSibling.html)|
Gets the next sibling of a node.  
[GetNodesWithAllFlags](Unity.Hierarchy.HierarchyViewModel.GetNodesWithAllFlags.html)|
Gets all hierarchy nodes that have all of the specified flags set.  
[GetNodesWithAnyFlags](Unity.Hierarchy.HierarchyViewModel.GetNodesWithAnyFlags.html)|
Gets all hierarchy nodes that have any of the specified flags set.  
[GetNodesWithoutAllFlags](Unity.Hierarchy.HierarchyViewModel.GetNodesWithoutAllFlags.html)|
Gets all hierarchy nodes that do not have all of the specified flags set.  
[GetNodesWithoutAnyFlags](Unity.Hierarchy.HierarchyViewModel.GetNodesWithoutAnyFlags.html)|
Gets all hierarchy nodes that do not have any of the specified flags set.  
[GetParent](Unity.Hierarchy.HierarchyViewModel.GetParent.html)|  Gets the
parent of a hierarchy node.  
[HasAllFlags](Unity.Hierarchy.HierarchyViewModel.HasAllFlags.html)|  Gets
whether or not all of the specified flags are set on any hierarchy node.  
[HasAllFlagsCount](Unity.Hierarchy.HierarchyViewModel.HasAllFlagsCount.html)|
Gets the number of nodes that have all of the specified flags set.  
[HasAnyFlags](Unity.Hierarchy.HierarchyViewModel.HasAnyFlags.html)|  Gets
whether or not any of the specified flags are set on any hierarchy node.  
[HasAnyFlagsCount](Unity.Hierarchy.HierarchyViewModel.HasAnyFlagsCount.html)|
Gets the number of nodes that have any of the specified flags set.  
[IndexOf](Unity.Hierarchy.HierarchyViewModel.IndexOf.html)|  Gets the zero-
based index of a specified node.  
[SetFlags](Unity.Hierarchy.HierarchyViewModel.SetFlags.html)|  Sets the
specified flags on all hierarchy nodes.  
[SetQuery](Unity.Hierarchy.HierarchyViewModel.SetQuery.html)|  Sets the search
query.  
[ToggleFlags](Unity.Hierarchy.HierarchyViewModel.ToggleFlags.html)|  Toggles
the specified flags on all hierarchy nodes.  
[Update](Unity.Hierarchy.HierarchyViewModel.Update.html)|  Updates the
hierarchy view model and requests a rebuild of the list of HierarchyNode that
filters the HierarchyFlattened.  
[UpdateIncremental](Unity.Hierarchy.HierarchyViewModel.UpdateIncremental.html)|
Updates the hierarchy view model incrementally.  
[UpdateIncrementalTimed](Unity.Hierarchy.HierarchyViewModel.UpdateIncrementalTimed.html)|
Updates the hierarchy view model incrementally until a time limit is reached.  
  
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

