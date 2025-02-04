[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-uxml-element-TabView.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-TabView.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-TabView.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-TabView.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-uxml-element-TabView.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-TabView.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-TabView.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-TabView.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Visual elements reference](UIE-ElementRef.html)
  * TabView

[](UIE-uxml-element-Tab.html)

Tab

[](UIE-uxml-element-TagField.html)

TagField

# TabView

You can group multiple [Tab](UIE-uxml-element-Tab.html) elements within a
TabView element to create a tab-based navigation system.

## Create a TabView

You can create a TabView with **UI**(User Interface) Allows a user to interact
with your application. Unity currently supports three UI systems. [More
info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder, UXML, or C#.

To create a TabView with C#, create a new instance of the
[TabView](../ScriptReference/UIElements.TabView.html) object and then add Tab
elements to it. For example:

    
    
    var tabView = new TabView("Title text");
    var tab1 = new Tab("Tab 1");
    var tab2 = new Tab("Tab 2");
    var tab3 = new Tab("Tab 3");
    tabView.Add(tab1);
    tabView.Add(tab2);
    tabView.Add(tab3);
    

## Make tabs reorderable

To make tabs reorderable with a TabView, set the
[`reorderable`](../ScriptReference/UIElements.TabView.reorderable.html)
property to `true`.

To persist the tab order for a TabView in the Editor UI, assign a unique
[`view-data-key`](../ScriptReference/UIElements.TabView.viewDataKey.html) to
both the TabView and its contained Tab elements. The `view-data-key` stores
the state of the tabs. If you left the `view-data-key` empty, the tab state
doesn’t persist when the document is reloaded. for more information, refer to
[View data persistence](UIE-ViewData.html).

## Examples

The following UXML example creates a TabView with Tabs:

    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <TabView>
           <Tab label="UXML Tab A">
               <Label text="UXML tab: This is some content for the first Tab." />
           </Tab>
           <Tab label="UXML Tab B">
               <Label text="UXML tab: This is some content for the second Tab." />
           </Tab>
        </TabView>
    </UXML>
    

The following C# example illustrates some of the customizable functionalities
of the TabView and its Tabs:

    
    
    /// <sample>
    // Create a TabView with Tabs that only contains a label.
    var csharpTabViewWithLabels = new TabView() { style = { marginTop = 15 } }; // marginTop not required, only for demonstration purposes.
    var tabOne = new Tab("One");
    tabOne.Add(new Label("Tab with labels only: This is some content for the first Tab.") { style = { marginTop = 10 } });
    csharpTabViewWithLabels.Add(tabOne);
    var tabTwo = new Tab("Two");
    tabTwo.Add(new Label("Tab with labels only: This is some content for the second Tab.") { style = { marginTop = 10 } });
    csharpTabViewWithLabels.Add(tabTwo);
    container.Add(csharpTabViewWithLabels);
    
    // Create a TabView with Tabs that only contains an icon.
    var csharpTabViewWithIcons = new TabView() { style = { marginTop = 15 } }; // marginTop not required, only for demonstration purposes.
    var tabIconConnect = new Tab(EditorGUIUtility.FindTexture("CloudConnect"));
    tabIconConnect.Add(new Label("Tab with icons only: This is some content for the first Tab.") { style = { marginTop = 10 } });
    csharpTabViewWithIcons.Add(tabIconConnect);
    var tabIconStore = new Tab(EditorGUIUtility.FindTexture("Asset Store"));
    tabIconStore.Add(new Label("Tab with icons only: This is some content for the second Tab.") { style = { marginTop = 10 } });
    csharpTabViewWithIcons.Add(tabIconStore);
    container.Add(csharpTabViewWithIcons);
    
    // Create a TabView with Tabs that only contains an icon and a label.
    var csharpTabViewWithIconsAndLabels = new TabView() { style = { marginTop = 15 } }; // marginTop not required, only for demonstration purposes.
    var tabConnect = new Tab("Connect", EditorGUIUtility.FindTexture("CloudConnect"));
    tabConnect.Add(new Label("Tab with an icon and a labels: This is some content for the first Tab.") { style = { marginTop = 10 } });
    csharpTabViewWithIconsAndLabels.Add(tabConnect);
    var tabStore = new Tab("Store", EditorGUIUtility.FindTexture("Asset Store"));
    tabStore.Add(new Label("Tab with an icon and a labels: This is some content for the second Tab.") { style = { marginTop = 10 } });
    csharpTabViewWithIconsAndLabels.Add(tabStore);
    container.Add(csharpTabViewWithIconsAndLabels);
    
    // Create a TabView that allows re-ordering of the tabs.
    var csharpReorderableTabView = new TabView() { reorderable = true, style = { marginTop = 10 } }; // marginTop not required, only for demonstration purposes.
    var tabA = new Tab("Tab A");
    tabA.Add(new Label("Reorderable tabs: This is some content for Tab A") { style = { marginTop = 10 } });
    csharpReorderableTabView.Add(tabA);
    var tabB = new Tab("Tab B");
    tabB.Add(new Label("Reorderable tabs: This is some content for Tab B") { style = { marginTop = 10 } });
    csharpReorderableTabView.Add(tabB);
    var tabC = new Tab("Tab C");
    tabC.Add(new Label("Reorderable tabs: This is some content for Tab C") { style = { marginTop = 10 } });
    csharpReorderableTabView.Add(tabC);
    container.Add(csharpReorderableTabView);
    
    // Create a TabView with closeable tabs.
    var closeTabInfoLabel = new Label($"Last tab closed: None");
    void UpdateLabel(string newLabel) => closeTabInfoLabel.text = $"Last tab closed: {newLabel}";
    var cSharpCloseableTabs = new TabView() { style = { marginTop = 10 } }; // marginTop not required, only for demonstration purposes.
    var closeableTabA = new Tab("Title A") { closeable = true };
    closeableTabA.closed += (tab) => { UpdateLabel(tab.label); };
    closeableTabA.Add(new Label("Closeable tabs: This is some content for Tab A") { style = { marginTop = 10 } });
    cSharpCloseableTabs.Add(closeableTabA);
    var closeableTabB = new Tab("Title B") { closeable = true };
    closeableTabB.closed += (tab) => { UpdateLabel(tab.label); };
    closeableTabB.Add(new Label("Closeable tabs: This is some content for Tab B") { style = { marginTop = 10 } });
    cSharpCloseableTabs.Add(closeableTabB);
    var closeableTabC = new Tab("Title C") { closeable = true };
    closeableTabC.closed += (tab) => { UpdateLabel(tab.label); };
    closeableTabC.Add(new Label("Closeable tabs: This is some content for Tab C") { style = { marginTop = 10 } });
    cSharpCloseableTabs.Add(closeableTabC);
    container.Add(cSharpCloseableTabs);
    container.Add(closeTabInfoLabel);
    
    // Create a TabView and apply custom styling to specific areas of their tabs.
    var csharpCustomStyledTabView = new TabView() { style = { marginTop = 15 }, classList = { "some-styled-class" }}; // marginTop not required, only for demonstration purposes.
    var customStyledTabOne = new Tab("One");
    customStyledTabOne.Add(new Label("Custom styled tabs: This is some content for the first Tab."));
    csharpCustomStyledTabView.Add(customStyledTabOne);
    var customStyledTabTwo = new Tab("Two");
    customStyledTabTwo.Add(new Label("Custom styled tabs: This is some content for the second Tab."));
    csharpCustomStyledTabView.Add(customStyledTabTwo);
    container.Add(csharpCustomStyledTabView);
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** >
**Samples**.

For more examples, refer to the following:

-[Create a tabbed menu](UIE-create-tabbed-menu-for-runtime.html).

## C# base class and namespace

**C# class** : [`TabView`](../ScriptReference/UIElements.TabView.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** :
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html)

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`reorderable` | `boolean` | A property that adds dragging support to tabs.  
  
The default value is `false`. Set this value to `true` to allow the user to
reorder tabs in the tab view.  
  
## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
  
This element also inherits the following attributes from
[`VisualElement`](UIE-uxml-element-VisualElement.html):

**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`data-source` | `Object` | Assigns a data source to this VisualElement which overrides any inherited data source. This data source is inherited by all children.  
`data-source-path` | `string` | Path from the data source to the value.  
`data-source-type` | `System.Type` | The possible type of data source assignable to this VisualElement.  
  
This information is only used by the UI Builder as a hint to provide some
completion to the data source path field when the effective data source cannot
be specified at design time.  
`language-direction` | [`UIElements.LanguageDirection`](../ScriptReference/UIElements.LanguageDirection.html) | Indicates the directionality of the element’s text. The value will propagate to the element’s children.  
  
Setting the languageDirection to RTL adds basic support for right-to-left
(RTL) by reversing the text and handling linebreaking and word wrapping
appropriately. However, it does not provide comprehensive RTL support, as this
would require text shaping, which includes the reordering of characters, and
OpenType font feature support. Comprehensive RTL support is planned for future
updates, which will involve additional APIs to handle language, script, and
font feature specifications.  
  
To enhance the RTL functionality of this property, users can explore available
third-party plugins in the Unity Asset Store and make use of
`ITextElementExperimentalFeatures.renderedText`  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The
standard practice is to give an element a unique name.  
`picking-mode` | [`UIElements.PickingMode`](../ScriptReference/UIElements.PickingMode.html) | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Sets the `VisualElement` style values.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | [`UIElements.UsageHints`](../ScriptReference/UIElements.UsageHints.html) | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence, such as tree expanded states, scroll position, or zoom level.  
  
This key is used to save and load the view data from the view data store. If
you don’t set this key, the persistence is disabled for the associated
`VisualElement`. For more information, refer to [View data persistence](UIE-
ViewData.html).  
  
## USS classes

The following table lists all the C# public property names and their related
USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-tab-view` | USS class name of elements of this type.  
`contentContainerUssClassName` | `.unity-tab-view__content-container` | USS class name for the content container of this type.  
`reorderableUssClassName` | `.unity-tab-view__reorderable` | The USS class name for reorderable tab view.  
`verticalUssClassName` | `.unity-tab-view__vertical` | The USS class name for vertical tab view.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the [Matching Selectors section in the Inspector or the UI
Toolkit Debugger](UIB-testing-ui.html#matching-selectors) to see which USS
selectors affect the components of the `VisualElement` at every level of its
hierarchy.

## Additional resources

  * [Tab](UIE-uxml-element-Tab.html)

[](UIE-uxml-element-Tab.html)

Tab

[](UIE-uxml-element-TagField.html)

TagField

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

