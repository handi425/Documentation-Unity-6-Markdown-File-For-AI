[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-create-a-popup-window.html)
  * [中文](/cn/current/Manual/UIE-create-a-popup-window.html)
  * [日本語](/ja/current/Manual/UIE-create-a-popup-window.html)
  * [한국어](/kr/current/Manual/UIE-create-a-popup-window.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-create-a-popup-window.html)
  * [中文](/cn/current/Manual/UIE-create-a-popup-window.html)
  * [日本語](/ja/current/Manual/UIE-create-a-popup-window.html)
  * [한국어](/kr/current/Manual/UIE-create-a-popup-window.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI examples](UIE-uxml-examples.html)
  * Create a pop-up window

[](UIE-create-tabbed-menu-for-runtime.html)

Create a tabbed menu

[](UIE-create-a-conditional-ui.html)

Use Toggle to create a conditional UI

# Create a pop-up window

This example demonstrates how to use
[`UnityEditor.PopupWindow`](../ScriptReference/PopupWindow.html) to create a
pop-up window.

## Example overview

This example creates a pop-up window that’s displayed through a button in a
custom Editor window. The pop-up window has three toggles and closes when it
isn’t in focus.

![A pop-up window displays when the button is
selected.](../uploads/Main/uxml/popup-window.png) A pop-up window displays
when the button is selected.

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/2023/create-a-popup-window).

## Prerequisites

This guide is for developers familiar with the Unity Editor, **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit, and C# scripting. Before you
start, get familiar with the following:

  * [UXML](UIE-UXML.html)
  * [USS](UIE-USS.html)
  * [`UnityEditor.PopupWindow`](../ScriptReference/PopupWindow.html)

## Create a custom Editor window

Create a custom Editor window with a button. Define the button in a UI
Document (UXML file) and style it in a USS file. Finally, define the button
logic in a C# script so that when you click the button, the pop-up window
displays.

  1. Create a Unity project with any template.

  2. Right-click in the Project window, and then select **Create** > **UI Toolkit** > **Editor Window**.

  3. In the **C#** box of the **UI Toolkit Editor Window Creator** window, enter `PopupExample`.

  4. Select **Confirm**. This creates three files: `PopupExample.cs`, `PopupExample.uxml`, and `PopupExample.uss`.

  5. Replace `PopupExample.uxml` with the following content:
    
               
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements" editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd" editor-extension-mode="True">
    <Style src="PopupExample.uss" />
    <ui:Button text="Popup Options" display-tooltip-when-elided="true" class="popup-button" />
    </ui:UXML>
         
    

  6. Replace `PopupExample.cs` with the following content:
    
                
    using UnityEditor;
    using UnityEngine.UIElements;
    using PopupWindow = UnityEditor.PopupWindow;
        
    public class PopupExample : EditorWindow
    {
         //Add menu item
         [MenuItem("Examples/Popup Example")]
         static void Init()
         {
              EditorWindow window = EditorWindow.CreateInstance<PopupExample>();
              window.Show();
         }
        
         private void CreateGUI()
         {
              var visualTreeAsset = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Assets/ui-toolkit-manual-code-examples/create-a-popup-window/PopupExample.uxml");
              visualTreeAsset.CloneTree(rootVisualElement);
        
              var button = rootVisualElement.Q<Button>();
              button.clicked += () => PopupWindow.Show(button.worldBound, new PopupContentExample());
         }
    }
    

  7. Replace `PopupExample.uss` with the following content:
    
        .popup-button {
        width: 200px;
    }
    

## Create the pop-up window content

Create a UI Document (UXML file) to define the content in the pop-up window.
Create a C# class to set the window size and to display the window.

  1. In the `Editor` folder, create a UI Document named `PopupWindowContent.uxml` with the following content:
    
        <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements" editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../../UIElementsSchema/UIElements.xsd" editor-extension-mode="True">
        <ui:Toggle label="Toggle 1" name="Toggle1"/>
        <ui:Toggle label="Toggle 2" />
        <ui:Toggle label="Toggle 3" />
    </ui:UXML>
    

  2. In the `Editor` folder, create a C# file named `PopupContentExample.cs` with the following content:
    
        using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
        
    public class PopupContentExample : PopupWindowContent
    { 
        public override void OnOpen()
        {
            Debug.Log("Popup opened: " + this);
        }
        
        public override VisualElement CreateGUI()
        {
            var visualTreeAsset = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Assets/ui-toolkit-manual-code-examples/create-a-popup-window/PopupWindowContent.uxml");
            return visualTreeAsset.CloneTree();
        }
        
        public override void OnClose()
        {
            Debug.Log("Popup closed: " + this);
        }
    }
    

  3. To test the pop-up window, from the menu, select **Example** > **Popup Example** > **Popup Options**. 

[](UIE-create-tabbed-menu-for-runtime.html)

Create a tabbed menu

[](UIE-create-a-conditional-ui.html)

Use Toggle to create a conditional UI

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

