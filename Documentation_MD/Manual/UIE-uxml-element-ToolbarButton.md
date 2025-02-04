[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-uxml-element-ToolbarButton.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-ToolbarButton.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-ToolbarButton.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-ToolbarButton.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-uxml-element-ToolbarButton.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-ToolbarButton.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-ToolbarButton.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-ToolbarButton.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Visual elements reference](UIE-ElementRef.html)
  * ToolbarButton

[](UIE-uxml-element-ToolbarBreadcrumbs.html)

ToolbarBreadcrumbs

[](UIE-uxml-element-ToolbarMenu.html)

ToolbarMenu

# ToolbarButton

A ToolbarButton is an [Editor-only](UIB-interface-overview.html#enable-editor-
extension-authoring-for-ui-documents-uxml) control that serves as a button in
a [Toolbar](UIE-uxml-element-Toolbar.html)A row of buttons and basic controls
at the top of the Unity Editor that allows you to interact with the Editor in
various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar). It’s a [Button](UIE-uxml-element-
Button.html) with a predefined style that matches the Toolbar style.

## Create a ToolbarButton

You can create a ToolbarButton with **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder, UXML, or C#. The following C#
example creates a ToolbarButton with a label:

    
    
    using UnityEditor.UIElements;
    ...
    var toolbarButton = new ToolbarButton(() => { Debug.Log("Button clicked"); }) { text = "Click me" };
    

## C# base class and namespace

**C# class** :
[`ToolbarButton`](../ScriptReference/UIElements.ToolbarButton.html)  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : [`Button`](../ScriptReference/UIElements.Button.html)

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`display-tooltip-when-elided` | `boolean` | When true, a tooltip displays the full version of elided text, and also if a tooltip had been previously provided, it will be overwritten.  
`emoji-fallback-support` | `boolean` | Specifies the order in which the system should look for Emoji characters when rendering text. If this setting is enabled, the global Emoji Fallback list will be searched first for characters defined as Emoji in the Unicode 14.0 standard.  
`enable-rich-text` | `boolean` | When false, rich text tags will not be parsed.  
`focusable` | `boolean` | True if the element can be focused.  
`icon-image` | `Object` | The Texture, **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite), or VectorImage that will represent an
icon within a Button element.  
`parse-escape-sequences` | `boolean` | Specifies whether escape sequences are displayed as is or if they are replaced by the character they represent.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`text` | `string` | The text to be displayed.  
  
Changing this value will implicitly invoke the `INotifyValueChanged_1.value`
setter, which will raise a `ChangeEvent_1` of type string.  
  
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
`ussClassName` | `.unity-toolbar-button` | USS class name of elements of this type.  
`ussClassName` | `.unity-button` | USS class name of elements of this type.  
  
Unity adds this USS class to every instance of the Button element. Any styling
applied to this class affects every button located beside, or below the
stylesheet in the visual tree.  
`iconUssClassName` | `.unity-button--with-icon` | The USS class name for Button elements with an icon.  
  
Unity adds this USS class to an instance of the Button element if the
instance’s `Button.iconImage` property contains a valid Texture. Any styling
applied to this class affects every button with an icon located beside, or
below the stylesheet in the visual tree.  
`ussClassName` | `.unity-text-element` | USS class name of elements of this type.  
`selectableUssClassName` | `.unity-text-element__selectable` | USS class name of selectable text elements.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the [Matching Selectors section in the Inspector or the UI
Toolkit Debugger](UIB-testing-ui.html#matching-selectors) to see which USS
selectors affect the components of the `VisualElement` at every level of its
hierarchy.

## Additional resources

  * [Toolbar](UIE-uxml-element-Toolbar.html)
  * [Button](UIE-uxml-element-Button.html)

[](UIE-uxml-element-ToolbarBreadcrumbs.html)

ToolbarBreadcrumbs

[](UIE-uxml-element-ToolbarMenu.html)

ToolbarMenu

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

