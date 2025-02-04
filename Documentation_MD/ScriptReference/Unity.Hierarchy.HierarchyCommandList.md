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

# HierarchyCommandList

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

Represents a list of commands that modify a hierarchy.

### Properties

[Capacity](Unity.Hierarchy.HierarchyCommandList.Capacity.html)|  The capacity
in bytes for storing commands in the command list.  
---|---  
[IsCreated](Unity.Hierarchy.HierarchyCommandList.IsCreated.html)|  Determines
if this object is valid and uses memory.  
[IsEmpty](Unity.Hierarchy.HierarchyCommandList.IsEmpty.html)|  Determines if
the command list is empty.  
[IsExecuting](Unity.Hierarchy.HierarchyCommandList.IsExecuting.html)|
Determines if the command list is currently executing.  
[Size](Unity.Hierarchy.HierarchyCommandList.Size.html)|  The current size in
bytes used by commands in the command list.  
  
### Constructors

[HierarchyCommandList](Unity.Hierarchy.HierarchyCommandList-ctor.html)|
Constructs a new HierarchyCommandList.  
---|---  
  
### Public Methods

[Add](Unity.Hierarchy.HierarchyCommandList.Add.html)|  Adds a new node that
has a specified parent node to the hierarchy.  
---|---  
[Clear](Unity.Hierarchy.HierarchyCommandList.Clear.html)|  Clears all commands
from the command list.  
[ClearProperty](Unity.Hierarchy.HierarchyCommandList.ClearProperty.html)|
Clears a property value for the specified hierarchy node.  
[Dispose](Unity.Hierarchy.HierarchyCommandList.Dispose.html)|  Disposes the
command list and releases its memory.  
[Execute](Unity.Hierarchy.HierarchyCommandList.Execute.html)|  Executes all
the commands in the hierarchy command list.  
[ExecuteIncremental](Unity.Hierarchy.HierarchyCommandList.ExecuteIncremental.html)|
Executes one command from the hierarchy command list.  
[ExecuteIncrementalTimed](Unity.Hierarchy.HierarchyCommandList.ExecuteIncrementalTimed.html)|
Executes commands from the hierarchy command list until a time limit is
reached.  
[Remove](Unity.Hierarchy.HierarchyCommandList.Remove.html)|  Removes a node
from the hierarchy.  
[RemoveChildren](Unity.Hierarchy.HierarchyCommandList.RemoveChildren.html)|
Recursively removes all children of a node.  
[Reserve](Unity.Hierarchy.HierarchyCommandList.Reserve.html)|  Reserves memory
for nodes to use. Use this to avoid memory allocation hits when you add
batches of nodes.  
[SetName](Unity.Hierarchy.HierarchyCommandList.SetName.html)|  Sets a name for
a hierarchy node.  
[SetParent](Unity.Hierarchy.HierarchyCommandList.SetParent.html)|  Sets the
parent node of a hierarchy node.  
[SetProperty](Unity.Hierarchy.HierarchyCommandList.SetProperty.html)|  Sets a
value for a property of a hierarchy node.  
[SetSortIndex](Unity.Hierarchy.HierarchyCommandList.SetSortIndex.html)|  Sets
the sorting index for a hierarchy node.  
[SortChildren](Unity.Hierarchy.HierarchyCommandList.SortChildren.html)|  Sorts
the child nodes of a hierarchy node by their sort index.  
  
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

