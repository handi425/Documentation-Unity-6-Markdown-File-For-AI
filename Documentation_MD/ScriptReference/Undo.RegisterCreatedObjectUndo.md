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

#  [Undo](Undo.html).RegisterCreatedObjectUndo

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

public static void RegisterCreatedObjectUndo([Object](Object.html)
objectToUndo, string name);

### Parameters

objectToUndo | The newly created object. This object is destroyed when the undo operation is performed. When the value is a GameObject, Unity registers the GameObject and its child GameObjects, but not sibling or parent GameObjects.  
---|---  
name | The name of the action to undo. Use this string to provide a short description of the action to be undone. For **Undo** or **Redo** items in the **Edit** menu, Unity adds "Undo" or "Redo" to the string that you provide. For example, if you provide the string "Create GameObject", the Unity Editor displays the menu item **Edit** > **Undo Create GameObject**.  
  
### Description

Registers an undo operation to undo the creation of an object.

This method registers the creation of an object to the undo stack so that
users can undo a create object action. Use this method each time you define an
action that creates an object, for example, inside a custom Editor or menu
item. Unity updates the undo action in the **Edit** menu with the name of the
undo operation. When the user performs the undo action, Unity destroys the
object.  
  
**Note:** The undo process destroys objects in the same way as
[Object.Destroy](Object.Destroy.html), but with no delay.  
  
When you create and modify an object at the same time, use the following
workflow to ensure that
[Undo.RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html) saves
all updates to the object:

  1. Create the object.
  2. Register the object as created with `Undo.RegisterCreatedObjectUndo`.
  3. Register the object with [Undo.RegisterCompleteObjectUndo](Undo.RegisterCompleteObjectUndo.html) so that the Editor records changes to the object. If the object has any child GameObjects, register it with [Undo.RegisterFullObjectHierarchyUndo](Undo.RegisterFullObjectHierarchyUndo.html) instead.
  4. Update the object.

If you do not follow this workflow, `Undo.RegisterCreatedObjectUndo` might not
save any updates to the object other than object creation.  
  
When you register a new object with `Undo.RegisterCreatedObjectUndo`, Unity
registers any changes to objects that are currently recorded by
[Undo.RecordObject](Undo.RecordObject.html) and then stops recording. This
means that after you register a new object, Unity does not record any
subsequent changes to any other objects that `Undo.RecordObject` was already
recording.  
  
When Unity is already recording changes to existing objects with
`Undo.RecordObject` and you want to register newly created objects, it is best
practice to follow this workflow:

  1. Complete any changes you want to make to objects that `Undo.RecordObject` is recording. Unity calls [Undo.FlushUndoRecordObjects](Undo.FlushUndoRecordObjects.html) automatically.
  2. Register newly created objects with `Undo.RegisterCreatedObjectUndo`.

If you do not follow this workflow, Unity might not store the state of the
recorded objects on the undo stack correctly.  
  
The following example shows how to create and modify a GameObject with a child
as an operation that can be undone in a single undo step.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    class CreateGameObjectMenu
    {
        [[MenuItem](MenuItem.html)("Example/Create [GameObject](GameObject.html)")]
        static void CreateGameObject()
        {
            // Create new undo group
            [Undo.IncrementCurrentGroup](Undo.IncrementCurrentGroup.html)();  
      
            // Create [GameObject](GameObject.html) hierarchy
            [GameObject](GameObject.html) go = new [GameObject](GameObject.html)("my [GameObject](GameObject.html)");
            [Undo.RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html)(go, "Create my [GameObject](GameObject.html)");
            [GameObject](GameObject.html) child = new [GameObject](GameObject.html)();
            [Undo.RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html)(child, "Create child");
            [Undo.SetTransformParent](Undo.SetTransformParent.html)(child.transform, go.transform, "Modify parent");  
      
            // Move [GameObject](GameObject.html) hierarchy
            [Undo.RegisterFullObjectHierarchyUndo](Undo.RegisterFullObjectHierarchyUndo.html)(go, "[Update](PlayerLoop.Update.html) my [GameObject](GameObject.html) position");
            go.transform.position = new [Vector3](Vector3.html)(5, 5, 5);  
      
            // Name undo group
            [Undo.SetCurrentGroupName](Undo.SetCurrentGroupName.html)("Create and Reposition [GameObject](GameObject.html) with Child");
        }
    }
    

**Note:** This operation cannot be performed when [isProcessing](Undo-
isProcessing.html) is `true`.

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

