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

# Undo

class in UnityEditor

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

Lets you register undo operations on specific objects you are about to perform
changes on.

The Undo system stores delta changes in the undo stack.  
  
Undo operations automatically combine together based on events. For example,
mouse down events split undo groups. Grouped undo operations appear and work
as a single undo. To control grouping manually, use
[Undo.IncrementCurrentGroup](Undo.IncrementCurrentGroup.html).  
  
By default, the name shown in the UI is selected from the actions from the
group using a hardcoded ordering of the different kinds of actions. To
manually set the name, use
[Undo.SetCurrentGroupName](Undo.SetCurrentGroupName.html).  
  
Undo operations store either per property or per object state. They scale well
with any Scene size.  
  
The most important operations are outlined below:  
  
Modify object properties:  
`Undo.RecordObject (myGameObject.transform, "Zero Transform Position");`  
`myGameObject.transform.position = Vector3.zero;`  
  
Add a component:  
`Undo.AddComponent<Rigidbody>(myGameObject);`  
  
Create a new GameObject:  
`var go = new GameObject();`  
`Undo.RegisterCreatedObjectUndo (go, "Created go");`  
  
Destroy a GameObject or component:  
`Undo.DestroyObjectImmediate (myGameObject);`  
  
Change transform parenting:  
`Undo.SetTransformParent (myGameObject.transform, newTransformParent, "Set new
parent");`

### Static Properties

[isProcessing](Undo-isProcessing.html)| Returns true if the editor is
currently processing undo or redo operations, false otherwise.  
---|---  
[postprocessModifications](Undo-postprocessModifications.html)| Callback that
is triggered whenever a new set of property modifications is created.  
[undoRedoEvent](Undo-undoRedoEvent.html)| Callback that is triggered after any
undo or redo event.  
[undoRedoPerformed](Undo-undoRedoPerformed.html)| Callback that is triggered
after an undo or a redo was executed.  
[willFlushUndoRecord](Undo-willFlushUndoRecord.html)| Invoked before the Undo
system performs a flush.  
  
### Static Methods

[AddComponent](Undo.AddComponent.html)| Adds a component to the game object
and registers an undo operation for this action.  
---|---  
[ClearAll](Undo.ClearAll.html)| Removes all undo and redo operations from
respectively the undo and redo stacks.  
[ClearUndo](Undo.ClearUndo.html)| Removes all Undo operation for the
identifier object registered using Undo.RegisterCompleteObjectUndo from the
undo stack.  
[CollapseUndoOperations](Undo.CollapseUndoOperations.html)| Collapses all undo
operations down to group index together into one step.  
[DestroyObjectImmediate](Undo.DestroyObjectImmediate.html)| Destroys the
object and records an undo operation so that it can be recreated.  
[FlushUndoRecordObjects](Undo.FlushUndoRecordObjects.html)| Ensure objects
recorded using RecordObject or RecordObjects are registered as an undoable
action. In most cases there is no reason to invoke FlushUndoRecordObjects
since it's automatically done right after mouse-up and certain other events
that conventionally marks the end of an action.  
[GetCurrentGroup](Undo.GetCurrentGroup.html)| Unity automatically groups undo
operations by the current group index.  
[GetCurrentGroupName](Undo.GetCurrentGroupName.html)| Get the name that will
be shown in the UI for the current undo group.  
[IncrementCurrentGroup](Undo.IncrementCurrentGroup.html)| Unity automatically
groups undo operations by the current group index.  
[MoveGameObjectToScene](Undo.MoveGameObjectToScene.html)| Move a GameObject
from its current Scene to a new Scene. It is required that the GameObject is
at the root of its current Scene.  
[PerformRedo](Undo.PerformRedo.html)| Perform an Redo operation.  
[PerformUndo](Undo.PerformUndo.html)| Perform an Undo operation.  
[RecordObject](Undo.RecordObject.html)| Records any changes done on the object
after the RecordObject function.  
[RecordObjects](Undo.RecordObjects.html)| Records multiple undoable objects in
a single call. This is the same as calling Undo.RecordObject multiple times.  
[RegisterChildrenOrderUndo](Undo.RegisterChildrenOrderUndo.html)| Stores a
copy of the order of the object's children on the undo stack.  
[RegisterCompleteObjectUndo](Undo.RegisterCompleteObjectUndo.html)| Stores a
copy of the object states on the undo stack.  
[RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html)| Registers an
undo operation to undo the creation of an object.  
[RegisterFullObjectHierarchyUndo](Undo.RegisterFullObjectHierarchyUndo.html)|
Copy the states of a hierarchy of objects onto the undo stack.  
[RegisterImporterUndo](Undo.RegisterImporterUndo.html)| Copies the state of
the importer for the given asset path.  
[RevertAllDownToGroup](Undo.RevertAllDownToGroup.html)| Performs all undo
operations up to the group index without storing a redo operation in the
process.  
[RevertAllInCurrentGroup](Undo.RevertAllInCurrentGroup.html)| Performs the
last undo operation but does not record a redo operation.  
[SetCurrentGroupName](Undo.SetCurrentGroupName.html)| Set the name of the
current undo group.  
[SetSiblingIndex](Undo.SetSiblingIndex.html)| Sets the sibling index of
transform and records an undo operation.  
[SetTransformParent](Undo.SetTransformParent.html)| Sets the parent of
transform to the new parent and records an undo operation.  
  
### Delegates

[PostprocessModifications](Undo.PostprocessModifications.html)| Delegate used
for postprocessModifications.  
---|---  
[UndoRedoCallback](Undo.UndoRedoCallback.html)| Delegate used for
undoRedoPerformed.  
[UndoRedoEventCallback](Undo.UndoRedoEventCallback.html)| Delegate used for
undoRedoEvent.  
[WillFlushUndoRecord](Undo.WillFlushUndoRecord.html)| Delegate used for
willFlushUndoRecord.  
  
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

