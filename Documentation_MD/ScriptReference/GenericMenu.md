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

# GenericMenu

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

GenericMenu lets you create custom context menus and dropdown menus.

The example below opens an Editor window with a button. Clicking the button
displays a context menu, which lets you change the color to apply to the GUI
in the window. Copy the example's contents into a script called
GenericMenuExample.cs and put it into a folder in your project called Editor.  
  
![](../StaticFiles/ScriptRefImages/GenericMenu.png).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class GenericMenuExample : [EditorWindow](EditorWindow.html)
    {
        // open the window from the menu item Example -> [GUI](GUI.html) [Color](Color.html)
        [[MenuItem](MenuItem.html)("Example/[GUI](GUI.html) [Color](Color.html)")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow<GenericMenuExample>();
            window.position = new [Rect](Rect.html)(50f, 50f, 200f, 24f);
            window.Show();
        }  
      
        // serialize field on window so its value will be saved when Unity recompiles
        [[SerializeField](SerializeField.html)]
        [Color](Color.html) m_Color = [Color.white](Color-white.html);  
      
        void OnEnable()
        {
            titleContent = new [GUIContent](GUIContent.html)("[GUI](GUI.html) [Color](Color.html)");
        }  
      
        // a method to simplify adding menu items
        void AddMenuItemForColor([GenericMenu](GenericMenu.html) menu, string menuPath, [Color](Color.html) color)
        {
            // the menu item is marked as selected if it matches the current value of m_Color
            menu.AddItem(new [GUIContent](GUIContent.html)(menuPath), m_Color.Equals(color), OnColorSelected, color);
        }  
      
        // the [GenericMenu.MenuFunction2](GenericMenu.MenuFunction2.html) event handler for when a menu item is selected
        void OnColorSelected(object color)
        {
            m_Color = ([Color](Color.html))color;
        }  
      
        void OnGUI()
        {
            // set the [GUI](GUI.html) to use the color stored in m_Color
            [GUI.color](GUI-color.html) = m_Color;  
      
            // display the [GenericMenu](GenericMenu.html) when pressing a button
            if ([GUILayout.Button](GUILayout.Button.html)("Select [GUI](GUI.html) [Color](Color.html)"))
            {
                // create the menu and add items to it
                [GenericMenu](GenericMenu.html) menu = new [GenericMenu](GenericMenu.html)();  
      
                // forward slashes nest menu items under submenus
                AddMenuItemForColor(menu, "RGB/Red", [Color.red](Color-red.html));
                AddMenuItemForColor(menu, "RGB/Green", [Color.green](Color-green.html));
                AddMenuItemForColor(menu, "RGB/Blue", [Color.blue](Color-blue.html));  
      
                // an empty string will create a separator at the top level
                menu.AddSeparator("");  
      
                AddMenuItemForColor(menu, "CMYK/Cyan", [Color.cyan](Color-cyan.html));
                AddMenuItemForColor(menu, "CMYK/Yellow", [Color.yellow](Color-yellow.html));
                AddMenuItemForColor(menu, "CMYK/Magenta", [Color.magenta](Color-magenta.html));
                // a trailing slash will nest a separator in a submenu
                menu.AddSeparator("CMYK/");
                AddMenuItemForColor(menu, "CMYK/Black", [Color.black](Color-black.html));  
      
                menu.AddSeparator("");  
      
                AddMenuItemForColor(menu, "White", [Color.white](Color-white.html));  
      
                // display the menu
                menu.ShowAsContext();
            }
        }
    }
    

### Properties

[allowDuplicateNames](GenericMenu-allowDuplicateNames.html)| Allow the menu to
have multiple items with the same name.  
---|---  
  
### Public Methods

[AddDisabledItem](GenericMenu.AddDisabledItem.html)| Add a disabled item to
the menu.  
---|---  
[AddItem](GenericMenu.AddItem.html)| Add an item to the menu.  
[AddSeparator](GenericMenu.AddSeparator.html)| Add a seperator item to the
menu.  
[DropDown](GenericMenu.DropDown.html)| Show the menu at the given screen rect.  
[GetItemCount](GenericMenu.GetItemCount.html)| Get number of items in the
menu.  
[ShowAsContext](GenericMenu.ShowAsContext.html)| Show the menu under the mouse
when right-clicked.  
  
### Delegates

[MenuFunction](GenericMenu.MenuFunction.html)| Callback function, called when
a menu item is selected.  
---|---  
[MenuFunction2](GenericMenu.MenuFunction2.html)| Callback function with user
data, called when a menu item is selected.  
  
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

