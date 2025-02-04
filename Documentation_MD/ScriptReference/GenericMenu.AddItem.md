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

#  [GenericMenu](GenericMenu.html).AddItem

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

public void AddItem([GUIContent](GUIContent.html) content, bool on,
[GenericMenu.MenuFunction](GenericMenu.MenuFunction.html) func);

### Parameters

content | The GUIContent to add as a menu item.  
---|---  
on | Specifies whether to show the item is currently activated (i.e. a tick next to the item in the menu).  
func | The function to call when the menu item is selected.  
  
### Description

Add an item to the menu.

Additional resources:
[GenericMenu.AddDisabledItem](GenericMenu.AddDisabledItem.html),
[GenericMenu.AddSeparator](GenericMenu.AddSeparator.html).

* * *

## Declaration

public void AddItem([GUIContent](GUIContent.html) content, bool on,
[GenericMenu.MenuFunction2](GenericMenu.MenuFunction2.html) func, object
userData);

### Parameters

content | The GUIContent to add as a menu item.  
---|---  
on | Specifies whether to show the item is currently activated (i.e. a tick next to the item in the menu).  
func | The function to call when the menu item is selected.  
userData | The data to pass to the function called when the item is selected.  
  
### Description

Add an item to the menu.

Additional resources:
[GenericMenu.AddDisabledItem](GenericMenu.AddDisabledItem.html),
[GenericMenu.AddSeparator](GenericMenu.AddSeparator.html).

    
    
    // This example shows how to create a context menu inside a custom [EditorWindow](EditorWindow.html).
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MyWindow : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("TestContextMenu/Open Window")]
        public static void Init()
        {
            var window = GetWindow(typeof(MyWindow));
            window.position = new [Rect](Rect.html)(50, 50, 250, 60);
            window.Show();
        }  
      
        public void Callback(object obj)
        {
            [Debug.Log](Debug.Log.html)("Selected: " + obj);
        }  
      
        public void OnGUI()
        {
            [Event](Event.html) evt = [Event.current](Event-current.html);
            [Rect](Rect.html) contextRect = new [Rect](Rect.html)(10, 10, 100, 100);  
      
            if (evt.type == [EventType.ContextClick](EventType.ContextClick.html))
            {
                [Vector2](Vector2.html) mousePos = evt.mousePosition;
                if (contextRect.Contains(mousePos))
                {
                    // Now create the menu, add items and show it
                    [GenericMenu](GenericMenu.html) menu = new [GenericMenu](GenericMenu.html)();  
      
                    menu.AddItem(new [GUIContent](GUIContent.html)("MenuItem1"), false, Callback, "item 1");
                    menu.AddItem(new [GUIContent](GUIContent.html)("MenuItem2"), false, Callback, "item 2");
                    menu.AddSeparator("");
                    menu.AddItem(new [GUIContent](GUIContent.html)("SubMenu/MenuItem3"), false, Callback, "item 3");
                    menu.AddItem(new [GUIContent](GUIContent.html)("SubMenu/MenuItem4"), false, Callback, "item 4");
                    menu.AddItem(new [GUIContent](GUIContent.html)("SubMenu/MenuItem5"), false, Callback, "item 5");
                    menu.AddSeparator("SubMenu/");
                    menu.AddItem(new [GUIContent](GUIContent.html)("SubMenu/MenuItem6"), false, Callback, "item 6");  
      
                    menu.ShowAsContext();  
      
                    evt.Use();
                }
            }
        }
    }
    
    
    
    // This example shows how to create a context menu inside a custom [EditorWindow](EditorWindow.html).
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MyWindow : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("TestContextMenu/Open Window")]
        public static void Init()
        {
            var window = GetWindow(typeof(MyWindow));
            window.position = new [Rect](Rect.html)(50, 50, 250, 60);
            window.Show();
        }  
      
        bool item2enabled = false;
        public void [Toggle](UIElements.Toggle.html)()
        {
            item2enabled = !item2enabled;
            [Debug.Log](Debug.Log.html)("item2enabled: " + item2enabled);
        }  
      
        public void Item2Callback()
        {
            [Debug.Log](Debug.Log.html)("[Item](Progress.Item.html) 2 Selected");
        }  
      
        public void OnGUI()
        {
            [Event](Event.html) evt = [Event.current](Event-current.html);
            [Rect](Rect.html) contextRect = new [Rect](Rect.html)(10, 10, 100, 100);  
      
            if (evt.type == [EventType.ContextClick](EventType.ContextClick.html))
            {
                [Vector2](Vector2.html) mousePos = evt.mousePosition;
                if (contextRect.Contains(mousePos))
                {
                    // Now create the menu, add items and show it
                    [GenericMenu](GenericMenu.html) menu = new [GenericMenu](GenericMenu.html)();  
      
                    menu.AddItem(new [GUIContent](GUIContent.html)("[Toggle](UIElements.Toggle.html) item 2"), item2enabled, [Toggle](UIElements.Toggle.html));
                    if (item2enabled)
                    {
                        menu.AddItem(new [GUIContent](GUIContent.html)("[Item](Progress.Item.html) 2"), false, Item2Callback);
                    }
                    else
                    {
                        menu.AddDisabledItem(new [GUIContent](GUIContent.html)("[Item](Progress.Item.html) 2"));
                    }  
      
                    menu.ShowAsContext();  
      
                    evt.Use();
                }
            }
        }
    }
    

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

