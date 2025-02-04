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

# GenericDropdownMenu

class in UnityEngine.UIElements

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

GenericDropdownMenu allows you to display contextual menus with default
textual options or any [VisualElement](UIElements.VisualElement.html).

The GenericDropdownMenu is a generic implementation of a dropdown menu that
you can use in both Editor UI and runtime UI.  
  
The following example creates a dropdown menu with three items. It displays
the menu when the user clicks the button. The example also demonstrates how to
set the width of the dropdown menu with the `DropDown` method.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    public class MenuExample : [EditorWindow](EditorWindow.html)
    {  
      
        [[MenuItem](MenuItem.html)("Window/UI Toolkit/MenuExample")]
        public static void ShowExample()
        {
            MenuExample wnd = GetWindow<MenuExample>();
            wnd.titleContent = new [GUIContent](GUIContent.html)("MenuExample");
        }
        public void CreateGUI()
        {
            [VisualElement](UIElements.VisualElement.html) root = rootVisualElement;  
      
            // Create a button.
            var button = new [Button](UIElements.Button.html)();
            button.text = "[Button](UIElements.Button.html)";
            button.style.width = 70;  
      
            // Create a dropdown menu with three items.
            var menu = new [GenericDropdownMenu](UIElements.GenericDropdownMenu.html)();
            menu.AddItem("[Item](Progress.Item.html) 1", false, a => { [Debug.Log](Debug.Log.html)("[Item](Progress.Item.html) 1 was selected"); }, null);
            menu.AddItem("[Item](Progress.Item.html) 2", false, a => { [Debug.Log](Debug.Log.html)("[Item](Progress.Item.html) 2 was selected"); }, null);
            menu.AddItem("[Item](Progress.Item.html) 3 has a very very long label", false, a => { [Debug.Log](Debug.Log.html)("[Item](Progress.Item.html) 3 was selected"); }, null);  
      
            // When the button is clicked, the dropdown menu is displayed aligned with the button's world boundaries.
            button.clicked += () =>
            {
                // The third and the fourth parameters of the DropDown set the width of the dropdown menu.
                // This sets the width of the dropdown menu to the width of the container.
                menu.DropDown(button.worldBound, button, false);
                // This sets the width of the dropdown menu to the width of the button.
                // menu.DropDown(button.worldBound, button, true, false);
                // This sets the width of the dropdown menu to the width of the longest item.
                // menu.DropDown(button.worldBound, button, true, true);
            };
             root.Add(button);
        }
    }
    

### Static Properties

[checkmarkUssClassName](UIElements.GenericDropdownMenu-
checkmarkUssClassName.html)|  USS class name of separators in elements of this
type.  
---|---  
[containerInnerUssClassName](UIElements.GenericDropdownMenu-
containerInnerUssClassName.html)|  USS class name of inner containers in
elements of this type.  
[containerOuterUssClassName](UIElements.GenericDropdownMenu-
containerOuterUssClassName.html)|  USS class name of outer containers in
elements of this type.  
[contentWidthUssClassName](UIElements.GenericDropdownMenu-
contentWidthUssClassName.html)|  USS class name that's added when the
GenericDropdownMenu fits the width of its content.  
[itemContentUssClassName](UIElements.GenericDropdownMenu-
itemContentUssClassName.html)|  USS class name of labels in elements of this
type.  
[itemUssClassName](UIElements.GenericDropdownMenu-itemUssClassName.html)|  USS
class name of labels in elements of this type.  
[labelUssClassName](UIElements.GenericDropdownMenu-labelUssClassName.html)|
USS class name of labels in elements of this type.  
[separatorUssClassName](UIElements.GenericDropdownMenu-
separatorUssClassName.html)|  USS class name of separators in elements of this
type.  
[ussClassName](UIElements.GenericDropdownMenu-ussClassName.html)|  USS class
name of elements of this type.  
  
### Properties

[contentContainer](UIElements.GenericDropdownMenu-contentContainer.html)|
Returns the content container for the GenericDropdownMenu. Allows users to
create their own dropdown menu if they don't want to use the default
implementation.  
---|---  
  
### Constructors

[GenericDropdownMenu](UIElements.GenericDropdownMenu-ctor.html)|  Initializes
and returns an instance of GenericDropdownMenu.  
---|---  
  
### Public Methods

[AddDisabledItem](UIElements.GenericDropdownMenu.AddDisabledItem.html)|  Adds
a disabled item to this menu using a default VisualElement.  
---|---  
[AddItem](UIElements.GenericDropdownMenu.AddItem.html)|  Adds an item to this
menu using a default VisualElement.  
[AddSeparator](UIElements.GenericDropdownMenu.AddSeparator.html)|  Adds a
visual separator after the previously added items in this menu.  
[DropDown](UIElements.GenericDropdownMenu.DropDown.html)|  Displays the menu
at the specified position.  
  
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

