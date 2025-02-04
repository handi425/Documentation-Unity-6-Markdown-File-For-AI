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

# ContextMenuUtility

class in UnityEditor.Actions

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

Provides methods to add menu items to the Scene view context menu.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Actions;
    using UnityEngine;
    
    // Add a menu item to the [Scene](SceneManagement.Scene.html) View context menu that creates a cube where-ever the mouse clicks.
    public class CreateCube : [EditorAction](Actions.EditorAction.html)
    {
        [GameObject](GameObject.html) m_GameObject;
        int m_UndoStart;
    
        // Prefixing the menu item path with "CONTEXT" indicates that this is a context menu item. Context menu items are
        // not added to the application menu bar. The second section of the menu path is the name of the type that this
        // menu item is applicable to. The context menu in the [Scene](SceneManagement.Scene.html) View for example will look for context menu items for
        // each of the following types:
        //    1. The active [EditorToolContext](EditorTools.EditorToolContext.html) type.
        //    2. The active [EditorTool](EditorTools.EditorTool.html) type.
        //    3. All component types in the selection. Ex, [Transform](Transform.html), [MeshRenderer](MeshRenderer.html), [BoxCollider](BoxCollider.html), etc...
        // As an example, to create a context menu item that is shown when context clicking in the [Scene](SceneManagement.Scene.html) View with a
        // [GameObject](GameObject.html) selected that has a [MeshFilter](MeshFilter.html) component, use "CONTEXT/[MeshFilter](MeshFilter.html)/My [Menu](Menu.html) [Item](Progress.Item.html)".
        [[MenuItem](MenuItem.html)("CONTEXT/[GameObjectToolContext](EditorTools.GameObjectToolContext.html)/Create Cube")]
        static void Init()
        {
            [EditorAction.Start](Actions.EditorAction.Start.html)<CreateCube>();
        }
    
        public CreateCube()
        {
            // Show a preview cube at the cursor.
            m_GameObject = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            // If the action is cancelled, we'll clean up the unused resource by calling [Undo.PerformUndo](Undo.PerformUndo.html)().
            [Undo.RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html)(m_GameObject, "Create Cube");
            // To avoid an unsightly "jump" when the cursor first moves, disable the preview until we have a valid
            // intersection point to place the object.
            m_GameObject.SetActive(false);
            m_UndoStart = [Undo.GetCurrentGroup](Undo.GetCurrentGroup.html)();
        }
    
        public override void OnSceneGUI([SceneView](SceneView.html) view)
        {
            var evt = [Event.current](Event-current.html);
            var id = [GUIUtility.GetControlID](GUIUtility.GetControlID.html)([FocusType.Passive](FocusType.Passive.html));
    
            if (evt.type == [EventType.MouseMove](EventType.MouseMove.html))
            {
                [HandleUtility.AddControl](HandleUtility.AddControl.html)(id, 0);
                // Disable preview object so that we don't intersect with object placement ray.
                m_GameObject.SetActive(false);
                var intersected = [HandleUtility.PlaceObject](HandleUtility.PlaceObject.html)(evt.mousePosition, out var position, out var normal);
                m_GameObject.SetActive(true);
                if (intersected)
                {
                    [Undo.RecordObject](Undo.RecordObject.html)(m_GameObject, "Create Cube");
                    m_GameObject.transform.position = position;
                    m_GameObject.transform.rotation = [Quaternion.LookRotation](Quaternion.LookRotation.html)(normal);
                }
            }
    
            // By checking that no mouse modifiers are active, we can allow for camera movement without breaking the
            // action.
            if (evt.type == [EventType.MouseDown](EventType.MouseDown.html) && evt.modifiers == [EventModifiers.None](EventModifiers.None.html))
            {
                [GUIUtility.hotControl](GUIUtility-hotControl.html) = id;
                evt.Use();
            }
    
            if ([GUIUtility.hotControl](GUIUtility-hotControl.html) == id && evt.type == [EventType.MouseUp](EventType.MouseUp.html))
            {
                evt.Use();
                [GUIUtility.hotControl](GUIUtility-hotControl.html) = 0;
                Finish([EditorActionResult.Success](Actions.EditorActionResult.Success.html));
            }
        }
    
        // Since the object we want to instantiate is already in the scene, there is nothing more to do in the OnFinish
        // function if the action exits successfully. If the action is cancelled however, we'll remove the instantiated
        // object from the scene by calling undo.
        protected override void OnFinish([EditorActionResult](Actions.EditorActionResult.html) result)
        {
            if (result == [EditorActionResult.Canceled](Actions.EditorActionResult.Canceled.html))
            {
                [Undo.PerformUndo](Undo.PerformUndo.html)();
                return;
            }
    
            [Selection.activeObject](Selection-activeObject.html) = m_GameObject;
            // Merge the selection change and [GameObject](GameObject.html) creation/placement to a single undo entry.
            [Undo.CollapseUndoOperations](Undo.CollapseUndoOperations.html)(m_UndoStart);
        }
    }
    

### Static Methods

[AddClipboardEntriesTo](Actions.ContextMenuUtility.AddClipboardEntriesTo.html)|
Adds clipboard operations to the Scene view context menu.  
---|---  
[AddComponentEntriesTo](Actions.ContextMenuUtility.AddComponentEntriesTo.html)|
Adds the component menu items of the current selection to the Scene view
context menu.  
[AddGameObjectEntriesTo](Actions.ContextMenuUtility.AddGameObjectEntriesTo.html)|
Adds the default actions for a GameObject and the component menu items of the
current selection to the Scene view context menu.  
[AddMenuItem](Actions.ContextMenuUtility.AddMenuItem.html)| Add a MenuItem to
the Scene view context menu.  
[AddMenuItemsForType](Actions.ContextMenuUtility.AddMenuItemsForType.html)|
Adds all MenuItem of a specific type to the Scene view context menu.  
[AddMenuItemWithContext](Actions.ContextMenuUtility.AddMenuItemWithContext.html)|
Adds a MenuItem to the Scene view context menu.  
  
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

