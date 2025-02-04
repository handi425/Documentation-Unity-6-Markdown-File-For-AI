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

# MenuItem

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

The `MenuItem` attribute allows you to add menu items to the main menu and
Inspector window context menus.

The `MenuItem` attribute turns any static function into a menu command. Only
static functions can use the `MenuItem` attribute.  
  
To create a hotkey, use the following special characters:

  * **%** : Represents **Ctrl** on Windows and Linux. **Cmd** on macOS.
  * **^** : Represents **Ctrl** on Windows, Linux, and macOS.
  * **#** : Represents **Shift**.
  * **&** : Represents **Alt**.

If no special modifier key combinations are required, the key can be given
after an underscore. For example, to create a menu with the hotkeys
**Shift+Alt+G** , use `"MyMenu/Do Something #&g"`. To create a menu with
hotkey **G** with no required key modifiers to press, use `"MyMenu/Do
Something _g"`.  
  
A space character must precede hotkey text. For example, `"MyMenu/Do_g"` isn't
interpreted as a hotkey, but `"MyMenu/Do _g"` is.  
  
Some special keyboard keys are supported as hotkeys. For example, "#LEFT"
would map to Shift-Left. The keys supported like this are: LEFT, RIGHT, UP,
DOWN, F1 .. F12, HOME, END, PGUP, PGDN, INS, DEL, BACKSPACE, TAB, and SPACE.  
  
When adding menu items to the "GameObject/" menu to create custom GameObjects,
be sure to call
[GameObjectUtility.SetParentAndAlign](GameObjectUtility.SetParentAndAlign.html)
to ensure that the new GameObject is reparented correctly in the case of a
context click (see example below). Your function should also call
[Undo.RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html) to make
the creation undoable and set [Selection.activeObject](Selection-
activeObject.html) to the newly created object. Also note that in order for a
menu item in "GameObject/" to be propagated to the hierarchy Create dropdown
and hierarchy context menu, it must be grouped with the other GameObject
creation menu items. This can be achieved by setting its priority to 10 (see
example below). Note that for legacy purposes MenuItems in "GameObject/Create
Other" with no explicit priority set will receive a priority of 10 instead of
the default 1000 - we encourage using a more descriptive category name than
"Create Other" and explicitly setting the priority to 10.  
  
You can use `MenuItem` to add menu items to the right-click context menu in
the Project window. The context menu in the Project window uses the same menu
items as the Assets menu. When you add a menu item to the Assets menu, that
menu item is also added to the context menu in the Project window. For
example, `"Assets/Do something"` adds the `Do something` menu item to the
context menu in the Project window.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class MenuTest : [MonoBehaviour](MonoBehaviour.html)
    {
        // Add a menu item named "Do Something" to MyMenu in the menu bar.
        [[MenuItem](MenuItem.html)("MyMenu/Do Something")]
        static void DoSomething()
        {
            [Debug.Log](Debug.Log.html)("Doing Something...");
        }  
      
        // Add a menu item named "Log Selected [Transform](Transform.html) Name" to MyMenu in the menu bar.
        // We want this to be validated menu item: an item that is only enabled if specific conditions are met.
        // To achieve this, we use a second function below to validate the menu item.
        // so it will only be enabled if we have a transform selected.
        [[MenuItem](MenuItem.html)("MyMenu/Log Selected [Transform](Transform.html) Name")]
        static void LogSelectedTransformName()
        {
            [Debug.Log](Debug.Log.html)("Selected [Transform](Transform.html) is on " + Selection.activeTransform.gameObject.name + ".");
        }  
      
        // Validate the menu item defined by the function above.
        // The "Log Selected [Transform](Transform.html) Name" menu item is disabled if this function returns false.
        // We tell the [Editor](Editor.html) that this is a validation function by decorating it with a [MenuItem](MenuItem.html) attribute
        // and passing true as the second parameter.
        // This invokes the [MenuItem](MenuItem.html)(string itemName, bool isValidateFunction) attribute constructor
        // resulting in the function being treated as the validator for "Log Selected [Transform](Transform.html) Name" menu item.
        [[MenuItem](MenuItem.html)("MyMenu/Log Selected [Transform](Transform.html) Name", true)]
        static bool ValidateLogSelectedTransformName()
        {
            // Return false if no transform is selected.
            return [Selection.activeTransform](Selection-activeTransform.html) != null;
        }  
      
        // Add a menu item named "Do Something with a Shortcut Key" to MyMenu in the menu bar
        // and give it a shortcut (ctrl-g on Windows, cmd-g on macOS).
        [[MenuItem](MenuItem.html)("MyMenu/Do Something with a Shortcut Key %g")]
        static void DoSomethingWithAShortcutKey()
        {
            [Debug.Log](Debug.Log.html)("Doing something with a Shortcut Key...");
        }  
      
        // Add a menu item called "Double Mass" to a [Rigidbody](Rigidbody.html)'s context menu.
        [[MenuItem](MenuItem.html)("CONTEXT/[Rigidbody](Rigidbody.html)/Double Mass")]
        static void DoubleMass([MenuCommand](MenuCommand.html) command)
        {
            [Rigidbody](Rigidbody.html) body = ([Rigidbody](Rigidbody.html))command.context;
            body.mass = body.mass * 2;
            [Debug.Log](Debug.Log.html)("Doubled [Rigidbody](Rigidbody.html)'s Mass to " + body.mass + " from Context [Menu](Menu.html).");
        }  
      
        // Add a menu item to create custom GameObjects.
        // [Priority](Progress.Priority.html) 10 ensures it is grouped with the other menu items of the same kind
        // and propagated to the hierarchy dropdown and hierarchy context menus.
        [[MenuItem](MenuItem.html)("[GameObject](GameObject.html)/MyCategory/Custom Game Object", false, 10)]
        static void CreateCustomGameObject([MenuCommand](MenuCommand.html) menuCommand)
        {
            // Create a custom game object
            [GameObject](GameObject.html) go = new [GameObject](GameObject.html)("Custom Game Object");
            // Ensure it gets reparented if this was a context click (otherwise does nothing)
            [GameObjectUtility.SetParentAndAlign](GameObjectUtility.SetParentAndAlign.html)(go, menuCommand.context as [GameObject](GameObject.html));
            // Register the creation in the undo system
            [Undo.RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html)(go, "Create " + go.name);
            [Selection.activeObject](Selection-activeObject.html) = go;
        }  
      
        // Add a menu item called "Test" to the [Scene](SceneManagement.Scene.html) view context menu when the
        // [EditorToolContext](EditorTools.EditorToolContext.html) "TestToolContext" is engaged.
        [[MenuItem](MenuItem.html)("CONTEXT/TestToolContext/Test")]
        static void TestToolContextItem()
        {
            [Debug.Log](Debug.Log.html)("Testing Test [Tool](Tool.html) Context [Menu](Menu.html) [Item](Progress.Item.html)");
        }  
      
        // Add a menu item called "Test" to the [Scene](SceneManagement.Scene.html) view context menu when the
        // [EditorTool](EditorTools.EditorTool.html) "TestTool" is engaged.
        [[MenuItem](MenuItem.html)("CONTEXT/TestTool/Test")]
        static void TestToolItem()
        {
            [Debug.Log](Debug.Log.html)("Testing Test [Tool](Tool.html) [Menu](Menu.html) [Item](Progress.Item.html)");
        }
    }

### Constructors

[MenuItem](MenuItem-ctor.html)| Creates a menu item and invokes the static
function that follows it when the menu item is selected.  
---|---  
  
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

