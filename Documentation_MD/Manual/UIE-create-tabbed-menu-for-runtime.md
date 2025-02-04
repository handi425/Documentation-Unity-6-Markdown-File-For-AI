[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-create-tabbed-menu-for-runtime.html)
  * [中文](/cn/current/Manual/UIE-create-tabbed-menu-for-runtime.html)
  * [日本語](/ja/current/Manual/UIE-create-tabbed-menu-for-runtime.html)
  * [한국어](/kr/current/Manual/UIE-create-tabbed-menu-for-runtime.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-create-tabbed-menu-for-runtime.html)
  * [中文](/cn/current/Manual/UIE-create-tabbed-menu-for-runtime.html)
  * [日本語](/ja/current/Manual/UIE-create-tabbed-menu-for-runtime.html)
  * [한국어](/kr/current/Manual/UIE-create-tabbed-menu-for-runtime.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI examples](UIE-uxml-examples.html)
  * Create a tabbed menu

[](UIE-wrap-content-inside-scrollview.html)

Wrap content inside a scroll view

[](UIE-create-a-popup-window.html)

Create a pop-up window

# Create a tabbed menu

**Version:** 2023.2+

Tabbed menus are widely used in video games and application **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) to organize and present content. Tab and
TabView are powerful controls that simplify the process of creating tabbed
menus.

## Example overview

This example demonstrates how to create tabbed menus in a sample **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and a custom Editor window. The menu
has three tabs. Each tab presents certain content. When you select a tab, the
content associated with that tab displays. The example also uses view data
keys to preserve the tab orders for the Editor window.

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/2023.2/create-a-tabbed-menu).

## Prerequisites

This guide is for developers familiar with the Unity Editor, UI Toolkit, and
C# scripting. Before you start, get familiar with the following:

  * [TabView](UIE-uxml-element-TabView.html)
  * [Tab](UIE-uxml-element-Tab.html)
  * [USS](UIE-USS.html)
  * [UI Builder](UIBuilder.html)
  * [UXML](UIE-UXML.html)

## Create a TabView

Create a UI Document and add a TabView to it.

  1. Create a project in Unity with any template.

  2. In the `Assets` folder, create a UI Document named `TabbedMenu.uxml`.

  3. Double-click `TabbedMenu.uxml` to open it in the UI Builder.

  4. Drag a TabView from the **Library** to the Hierarchy panel.

  5. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) panel of the TabView, do the
following:

     * Set **View Data Key** to `TabbedMenu`.
     * Select the **Reorderable** checkbox.

## Add tabs and tab content

Add three tabs to the TabView. For each tab, add a label as its child element
which displays the tab content.

  1. Under TabView, add three Tabs.

  2. In the Inspector panel of each Tab, set **Label** to the following values:

     * `London` for the first Tab
     * `Paris` for the second Tab
     * `Ottawa` for the third Tab
  3. Set **View Data Key** to the following values:

     * `LondonTab` for the first Tab
     * `ParisTab` for the second Tab
     * `OttawaTab` for the third Tab
  4. In the Hierarchy panel, under each Tab, add a Label.

  5. In the Inspector panel of each Label, Set **Text** to the following values:

     * `London is the capital city of England` for the first Label
     * `Paris is the capital of France` for the second Label
     * `Ottawa is the capital of Canada` for the third Label

## Define the tabbed menu styles

Define the layout for tabs and tab content using USS. You can style the tabs
and the tab content the way you like. This example adds a background color for
the selected tab and hides the tab header underline.

  1. In the `Assets` folder, create a stylesheet named `TabbedMenu.uss`.

  2. Open `TabbedMenu.uss` and add the following styling rules:
    
        /* Style for tabs */
    .unity-tab__header {
        background-color: rgb(229, 223, 223);
        -unity-font-style: bold;
        font-size: 14px;
    }
        
    /* Adds background color for the selected tab */
    .unity-tab__header:checked  {
        background-color: rgb(173, 166, 166);
    }
        
    /* Style for tabContent */
    .tab-content {
        background-color: rgb(255, 255, 255);
        font-size: 20px;
    }
        
    /* By default, each tab header has an underline. This hides the header underline  */
    .unity-tab__header-underline {
        opacity: 0; /* or rgba(0, 0, 0, 0); */
    }
    

  3. Double-click `TabbedMenu.uxml` to open it in UI Builder.

  4. In the StyleSheets panel, select **+** > **Add Existing USS**.

  5. Select the USS file that you created earlier.

  6. Apply `.tab-content` to each Label under Tab.

The finished `TabbedMenu.uxml` looks like the following:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" 
    engine="UnityEngine.UIElements" editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd" 
    editor-extension-mode="False">
      /* Your src might look different. If you save your UXML in UI Builder, USS file is referenced by the file location, fileID and guid. */
      <Style src="TabbedMenu.uss" />
      <ui:TabView reorderable="true" view-data-key="TabbedMenu">
         <ui:Tab label="London" view-data-key="LondonTab">
             <ui:Label text="London is the capital city of England" class="tab-content"/>
         </ui:Tab>
         <ui:Tab label="Paris" view-data-key="ParisTab">
             <ui:Label text="Paris is the capital of France"  class="tab-content"/>
         </ui:Tab>
         <ui:Tab label="Ottawa" view-data-key="OttawaTab">
             <ui:Label text="Ottawa is the capital of Canada" class="tab-content"/>
         </ui:Tab>
      </ui:TabView>
    </ui:UXML>
    

## Use the tabbed menu in a game

Create a UIDocument **GameObject** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the SampleScene and add the UI
Document as the source asset. Create a MonoBehaviour script that attaches the
tabbed menu to the game.

  1. In the SampleScene, select **GameObject** > **UI Toolkit** > **UI Document**. 

  2. In the `Assets` folder, create a C# script named`TabbedMenu.cs` with the following content:
    
        using UnityEngine;
    using UnityEngine.UIElements;
        
    //Inherits from class `MonoBehaviour`. This makes it attachable to a game object as a component.
    public class TabbedMenu : MonoBehaviour
    {
        private void OnEnable()
        {
            UIDocument menu = GetComponent<UIDocument>();
            VisualElement root = menu.rootVisualElement;
        }
    }
    

  3. Select **UIDocument** in the SampleScene.

  4. In the Inspector window, select **TabbedMenu.uxml** from the **Source Asset** list.

  5. Select `TabbedMenu.cs` from the **Add Component** list. 

  6. Enter Play mode.

  7. Select different tabs to see different contents.

  8. Drag the tabs to reorder them.

## Use the tabbed menu in an Editor window

Create a custom Editor window and add the tabbed menu to it. You can drag the
tabs to reorder them. The tab orders are saved when you close and reopen the
Editor window.

  1. In the `Assets` folder, create a folder named `Editor`.

  2. In the `Editor` folder, create a C# script named `TabbedMenuEditorWindow.cs` with the following content:
    
        using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
        
    public class TabbedMenuEditorWindow : EditorWindow
    {
        [MenuItem("Window/Tabbed Menu")]
        public static void ShowExample()
        {
            TabbedMenuEditorWindow wnd = GetWindow<TabbedMenuEditorWindow>();
            wnd.titleContent = new GUIContent("Tabbed Menu");
        }
        
        public void OnEnable()
        {
            VisualElement root = rootVisualElement;
            // Import UXML
            var visualTree = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Assets/TabbedMenu.uxml");
            VisualElement tabbedMenuUXML = visualTree.Instantiate();
            root.Add(tabbedMenuUXML);
        }
    }
    

  3. In the Editor, select **Window** > **Tabbed Menu**.

  4. Select different tabs to see different contents.

  5. Drag the tabs to reorder them.

  6. Close the Editor window and reopen it. The tabs orders are saved.

## Additional resources

  * [Get started with runtime UI](UIE-get-started-with-runtime-ui.html)
  * [Support for Editor UI](UIE-support-for-editor-ui.html)
  * [View data persistence](UIE-ViewData.html)

[](UIE-wrap-content-inside-scrollview.html)

Wrap content inside a scroll view

[](UIE-create-a-popup-window.html)

Create a pop-up window

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

