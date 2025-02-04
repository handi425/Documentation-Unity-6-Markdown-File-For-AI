[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-ElementRef.html)
  * [中文](/cn/current/Manual/UIE-ElementRef.html)
  * [日本語](/ja/current/Manual/UIE-ElementRef.html)
  * [한국어](/kr/current/Manual/UIE-ElementRef.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-ElementRef.html)
  * [中文](/cn/current/Manual/UIE-ElementRef.html)
  * [日本語](/ja/current/Manual/UIE-ElementRef.html)
  * [한국어](/kr/current/Manual/UIE-ElementRef.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * Visual elements reference

[](UIE-encapsulate-uxml-with-logic.html)

Encapsulate UXML documents with logic

[](UIE-uxml-element-BindableElement.html)

BindableElement

# Visual elements reference

The following tables outline the **visual elements** A node of a visual tree
that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) available in the
`UnityEngine.UIElements` and `UnityEditor.UIElements` namespaces.

## Base elements

**Element** | **Namespace** | **C# class**  
---|---|---  
**[`BindableElement`](UIE-uxml-element-BindableElement.html)** | `UnityEngine.UIElements` | [`UnityEngine.UIElements.BindableElement`](../ScriptReference/UIElements.BindableElement.html)  
**[`VisualElement`](UIE-uxml-element-VisualElement.html)** | `UnityEngine.UIElements` | [`UnityEngine.UIElements.VisualElement`](../ScriptReference/UIElements.VisualElement.html)  
  
## Built-in controls

The following table is a reference of all built-in controls available for
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit.

**Element** | **Bindable** | **Data type** | **Namespace** | **C# class**  
---|---|---|---|---  
**[`BoundsField`](UIE-uxml-element-BoundsField.html)** | Yes | [`UnityEngine.Bounds`](../ScriptReference/Bounds.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.BoundsField`](../ScriptReference/UIElements.BoundsField.html)  
**[`BoundsIntField`](UIE-uxml-element-BoundsIntField.html)** | Yes | [`UnityEngine.BoundsInt`](../ScriptReference/BoundsInt.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.BoundsIntField`](../ScriptReference/UIElements.BoundsIntField.html)  
**[`Box`](UIE-uxml-element-Box.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Box`](../ScriptReference/UIElements.Box.html)  
**[`Button`](UIE-uxml-element-Button.html)** | Yes | `string` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Button`](../ScriptReference/UIElements.Button.html)  
**[`ColorField`](UIE-uxml-element-ColorField.html)** | Yes | [`UnityEngine.Color`](../ScriptReference/Color.html) | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ColorField`](../ScriptReference/UIElements.ColorField.html)  
**[`CurveField`](UIE-uxml-element-CurveField.html)** | Yes | [`UnityEngine.AnimationCurve`](../ScriptReference/AnimationCurve.html) | `UnityEditor.UIElements` | [`UnityEditor.UIElements.CurveField`](../ScriptReference/UIElements.CurveField.html)  
**[`DoubleField`](UIE-uxml-element-DoubleField.html)** | Yes | `double` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.DoubleField`](../ScriptReference/UIElements.DoubleField.html)  
**[`DropdownField`](UIE-uxml-element-DropdownField.html)** | Yes | `string` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.DropdownField`](../ScriptReference/UIElements.DropdownField.html)  
**[`EnumField`](UIE-uxml-element-EnumField.html)** | Yes | `Enum` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.EnumField`](../ScriptReference/UIElements.EnumField.html)  
**[`EnumFlagsField`](UIE-uxml-element-EnumFlagsField.html)** | Yes | `Enum` | `UnityEditor.UIElements` | [`UnityEditor.UIElements.EnumFlagsField`](../ScriptReference/UIElements.EnumFlagsField.html)  
**[`FloatField`](UIE-uxml-element-FloatField.html)** | Yes | `float` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.FloatField`](../ScriptReference/UIElements.FloatField.html)  
**[`Foldout`](UIE-uxml-element-Foldout.html)** | Yes | `boolean` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Foldout`](../ScriptReference/UIElements.Foldout.html)  
**[`GradientField`](UIE-uxml-element-GradientField.html)** | Yes | [`UnityEngine.Gradient`](../ScriptReference/Gradient.html) | `UnityEditor.UIElements` | [`UnityEditor.UIElements.GradientField`](../ScriptReference/UIElements.GradientField.html)  
**[`GroupBox`](UIE-uxml-element-GroupBox.html)** | Yes |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.GroupBox`](../ScriptReference/UIElements.GroupBox.html)  
**[`Hash128Field`](UIE-uxml-element-Hash128Field.html)** | Yes | [`UnityEngine.Hash128`](../ScriptReference/Hash128.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Hash128Field`](../ScriptReference/UIElements.Hash128Field.html)  
**[`HelpBox`](UIE-uxml-element-HelpBox.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.HelpBox`](../ScriptReference/UIElements.HelpBox.html)  
**[`IMGUIContainer`](UIE-uxml-element-IMGUIContainer.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.IMGUIContainer`](../ScriptReference/UIElements.IMGUIContainer.html)  
**[`Image`](UIE-uxml-element-Image.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Image`](../ScriptReference/UIElements.Image.html)  
**[`InspectorElement`](UIE-uxml-element-InspectorElement.html)** | Yes |  | `UnityEditor.UIElements` | [`UnityEditor.UIElements.InspectorElement`](../ScriptReference/UIElements.InspectorElement.html)  
**[`IntegerField`](UIE-uxml-element-IntegerField.html)** | Yes | `int` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.IntegerField`](../ScriptReference/UIElements.IntegerField.html)  
**[`Label`](UIE-uxml-element-Label.html)** | Yes | `string` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Label`](../ScriptReference/UIElements.Label.html)  
**[`LayerField`](UIE-uxml-element-LayerField.html)** | Yes | `int` | `UnityEditor.UIElements` | [`UnityEditor.UIElements.LayerField`](../ScriptReference/UIElements.LayerField.html)  
**[`LayerMaskField`](UIE-uxml-element-LayerMaskField.html)** | Yes | `int` | `UnityEditor.UIElements` | [`UnityEditor.UIElements.LayerMaskField`](../ScriptReference/UIElements.LayerMaskField.html)  
**[`ListView`](UIE-uxml-element-ListView.html)** | Yes | `IList` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.ListView`](../ScriptReference/UIElements.ListView.html)  
**[`LongField`](UIE-uxml-element-LongField.html)** | Yes | `long` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.LongField`](../ScriptReference/UIElements.LongField.html)  
**[`MaskField`](UIE-uxml-element-MaskField.html)** | Yes | `int` | `UnityEditor.UIElements` | [`UnityEditor.UIElements.MaskField`](../ScriptReference/UIElements.MaskField.html)  
**[`MinMaxSlider`](UIE-uxml-element-MinMaxSlider.html)** | Yes | [`UnityEngine.Vector2`](../ScriptReference/Vector2.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.MinMaxSlider`](../ScriptReference/UIElements.MinMaxSlider.html)  
**[`MultiColumnListView`](UIE-uxml-element-MultiColumnListView.html)** | Yes |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.MultiColumnListView`](../ScriptReference/UIElements.MultiColumnListView.html)  
**[`MultiColumnTreeView`](UIE-uxml-element-MultiColumnTreeView.html)** | Yes |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.MultiColumnTreeView`](../ScriptReference/UIElements.MultiColumnTreeView.html)  
**[`ObjectField`](UIE-uxml-element-ObjectField.html)** | Yes | [`UnityEngine.Object`](../ScriptReference/Object.html) | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ObjectField`](../ScriptReference/UIElements.ObjectField.html)  
**[`PopupWindow`](UIE-uxml-element-PopupWindow.html)** | Yes | `string` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.PopupWindow`](../ScriptReference/UIElements.PopupWindow.html)  
**[`ProgressBar`](UIE-uxml-element-ProgressBar.html)** | Yes | `float` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.ProgressBar`](../ScriptReference/UIElements.ProgressBar.html)  
**[`PropertyField`](UIE-uxml-element-PropertyField.html)** |  |  | `UnityEditor.UIElements` | [`UnityEditor.UIElements.PropertyField`](../ScriptReference/UIElements.PropertyField.html)  
**[`RadioButton`](UIE-uxml-element-RadioButton.html)** | Yes | `boolean` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.RadioButton`](../ScriptReference/UIElements.RadioButton.html)  
**[`RadioButtonGroup`](UIE-uxml-element-RadioButtonGroup.html)** | Yes | `int` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.RadioButtonGroup`](../ScriptReference/UIElements.RadioButtonGroup.html)  
**[`RectField`](UIE-uxml-element-RectField.html)** | Yes | [`UnityEngine.Rect`](../ScriptReference/Rect.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.RectField`](../ScriptReference/UIElements.RectField.html)  
**[`RectIntField`](UIE-uxml-element-RectIntField.html)** | Yes | [`UnityEngine.RectInt`](../ScriptReference/RectInt.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.RectIntField`](../ScriptReference/UIElements.RectIntField.html)  
**[`RenderingLayerMaskField`](UIE-uxml-element-RenderingLayerMaskField.html)** | Yes | [`System.UInt32`](https://learn.microsoft.com/en-us/dotnet/api/system.uint32?view=net-8.0)  
`UnityEditor.UIElements` | [`UnityEditor.UIElements.RenderingLayerMaskField`](../ScriptReference/UIElements.RenderingLayerMaskField.html)  
**[`RepeatButton`](UIE-uxml-element-RepeatButton.html)** | Yes | `string` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.RepeatButton`](../ScriptReference/UIElements.RepeatButton.html)  
**[`ScrollView`](UIE-uxml-element-ScrollView.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.ScrollView`](../ScriptReference/UIElements.ScrollView.html)  
**[`Scroller`](UIE-uxml-element-Scroller.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Scroller`](../ScriptReference/UIElements.Scroller.html)  
**[`Slider`](UIE-uxml-element-Slider.html)** | Yes | `float` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Slider`](../ScriptReference/UIElements.Slider.html)  
**[`SliderInt`](UIE-uxml-element-SliderInt.html)** | Yes | `int` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.SliderInt`](../ScriptReference/UIElements.SliderInt.html)  
**[`Tab`](UIE-uxml-element-Tab.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Tab`](../ScriptReference/UIElements.Tab.html)  
**[`TabView`](UIE-uxml-element-TabView.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.TabView`](../ScriptReference/UIElements.TabView.html)  
**[`TagField`](UIE-uxml-element-TagField.html)** | Yes | `string` | `UnityEditor.UIElements` | [`UnityEditor.UIElements.TagField`](../ScriptReference/UIElements.TagField.html)  
**[`TemplateContainer`](UIE-uxml-element-TemplateContainer.html)** | Yes |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.TemplateContainer`](../ScriptReference/UIElements.TemplateContainer.html)  
**[`TemplateContainer`](UIE-uxml-element-TemplateContainer.html)** | Yes |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.TemplateContainer`](../ScriptReference/UIElements.TemplateContainer.html)  
**[`TextElement`](UIE-uxml-element-TextElement.html)** | Yes | `string` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.TextElement`](../ScriptReference/UIElements.TextElement.html)  
**[`TextField`](UIE-uxml-element-TextField.html)** | Yes | `string` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.TextField`](../ScriptReference/UIElements.TextField.html)  
**[`Toggle`](UIE-uxml-element-Toggle.html)** | Yes | `boolean` | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Toggle`](../ScriptReference/UIElements.Toggle.html)  
**[`ToggleButtonGroup`](UIE-uxml-element-ToggleButtonGroup.html)** | Yes | [`UnityEngine.UIElements.ToggleButtonGroupState`](../ScriptReference/UIElements.ToggleButtonGroupState.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.ToggleButtonGroup`](../ScriptReference/UIElements.ToggleButtonGroup.html)  
**[`Toolbar`](UIE-uxml-element-Toolbar.html)** |  |  | `UnityEditor.UIElements` | [`UnityEditor.UIElements.Toolbar`](../ScriptReference/UIElements.Toolbar.html)  
**[`ToolbarBreadcrumbs`](UIE-uxml-element-ToolbarBreadcrumbs.html)** |  |  | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ToolbarBreadcrumbs`](../ScriptReference/UIElements.ToolbarBreadcrumbs.html)  
**[`ToolbarButton`](UIE-uxml-element-ToolbarButton.html)** | Yes |  | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ToolbarButton`](../ScriptReference/UIElements.ToolbarButton.html)  
**[`ToolbarMenu`](UIE-uxml-element-ToolbarMenu.html)** | Yes |  | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ToolbarMenu`](../ScriptReference/UIElements.ToolbarMenu.html)  
**[`ToolbarPopupSearchField`](UIE-uxml-element-ToolbarPopupSearchField.html)** |  | `string` | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ToolbarPopupSearchField`](../ScriptReference/UIElements.ToolbarPopupSearchField.html)  
**[`ToolbarSearchField`](UIE-uxml-element-ToolbarSearchField.html)** |  | `string` | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ToolbarSearchField`](../ScriptReference/UIElements.ToolbarSearchField.html)  
**[`ToolbarSpacer`](UIE-uxml-element-ToolbarSpacer.html)** |  |  | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ToolbarSpacer`](../ScriptReference/UIElements.ToolbarSpacer.html)  
**[`ToolbarToggle`](UIE-uxml-element-ToolbarToggle.html)** | Yes | `boolean` | `UnityEditor.UIElements` | [`UnityEditor.UIElements.ToolbarToggle`](../ScriptReference/UIElements.ToolbarToggle.html)  
**[`TreeView`](UIE-uxml-element-TreeView.html)** | Yes |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.TreeView`](../ScriptReference/UIElements.TreeView.html)  
**[`TwoPaneSplitView`](UIE-uxml-element-TwoPaneSplitView.html)** |  |  | `UnityEngine.UIElements` | [`UnityEngine.UIElements.TwoPaneSplitView`](../ScriptReference/UIElements.TwoPaneSplitView.html)  
**[`UnsignedIntegerField`](UIE-uxml-element-UnsignedIntegerField.html)** | Yes | [`System.UInt32`](https://learn.microsoft.com/en-us/dotnet/api/system.uint32?view=net-8.0) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.UnsignedIntegerField`](../ScriptReference/UIElements.UnsignedIntegerField.html)  
**[`UnsignedLongField`](UIE-uxml-element-UnsignedLongField.html)** | Yes | [`System.UInt64`](https://learn.microsoft.com/en-us/dotnet/api/system.uint64?view=net-8.0) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.UnsignedLongField`](../ScriptReference/UIElements.UnsignedLongField.html)  
**[`Vector2Field`](UIE-uxml-element-Vector2Field.html)** | Yes | [`UnityEngine.Vector2`](../ScriptReference/Vector2.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Vector2Field`](../ScriptReference/UIElements.Vector2Field.html)  
**[`Vector2IntField`](UIE-uxml-element-Vector2IntField.html)** | Yes | [`UnityEngine.Vector2Int`](../ScriptReference/Vector2Int.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Vector2IntField`](../ScriptReference/UIElements.Vector2IntField.html)  
**[`Vector3Field`](UIE-uxml-element-Vector3Field.html)** | Yes | [`UnityEngine.Vector3`](../ScriptReference/Vector3.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Vector3Field`](../ScriptReference/UIElements.Vector3Field.html)  
**[`Vector3IntField`](UIE-uxml-element-Vector3IntField.html)** | Yes | [`UnityEngine.Vector3Int`](../ScriptReference/Vector3Int.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Vector3IntField`](../ScriptReference/UIElements.Vector3IntField.html)  
**[`Vector4Field`](UIE-uxml-element-Vector4Field.html)** | Yes | [`UnityEngine.Vector4`](../ScriptReference/Vector4.html) | `UnityEngine.UIElements` | [`UnityEngine.UIElements.Vector4Field`](../ScriptReference/UIElements.Vector4Field.html)  
  
## C# only controls

The following table lists the controls that are only available in C# and do
not have a UXML representation.

**Name** | **Bindable** | **Namespace** | **C# class**  
---|---|---|---  
**`GenericDropdownMenu`** | No | `UnityEngine.UIElements` | [`UnityEngine.UIElements.GenericDropdownMenu`](../ScriptReference/UIElements.GenericDropdownMenu.html)  
  
## Templates

**Element** | **Description** | **Namespace** | **Permitted child elements** | **Attributes**  
---|---|---|---|---  
`Template` | A reference to another UXML template that can be instantiated using the `Instance` element. | `UnityEngine.UIElements` | None |  `name`: A unique string identifier for this element  
`path`: The path of the UXML file to load  
`Instance` | Instance of a `Template` | `UnityEngine.UIElements` | None |  `template`: The `name` of the `Template` to instantiate  
  
## UxmlObject attributes

**Element** | **Description** | **Namespace** | **Permitted child elements** | **Attributes**  
---|---|---|---|---  
`Columns` | Contains descriptions of columns. Must be a child of a parent that supports it, such as [MultiColumnListView](UIE-uxml-element-MultiColumnListView.html) or [MultiColumnTreeView](UIE-uxml-element-MultiColumnTreeView.html). | `UnityEngine.UIElements` | `Column` | None  
`Column` | Describes a column. Must be a child of `Columns`. | `UnityEngine.UIElements` | None |  `name`: The name of this column in code  
`title`: The name displayed in the header of this column  
`width`: The default width of this column in pixels  
  
[](UIE-encapsulate-uxml-with-logic.html)

Encapsulate UXML documents with logic

[](UIE-uxml-element-BindableElement.html)

BindableElement

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

