[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-uxml-element-PropertyField.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-PropertyField.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-PropertyField.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-PropertyField.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-uxml-element-PropertyField.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-PropertyField.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-PropertyField.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-PropertyField.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Visual elements reference](UIE-ElementRef.html)
  * PropertyField

[](UIE-uxml-element-ProgressBar.html)

ProgressBar

[](UIE-uxml-element-RadioButton.html)

RadioButton

# PropertyField

A PropertyField is a field element specifically designed to be bound to a
[SerializedProperty](../ScriptReference/SerializedProperty.html). Once you
bind a property to a PropertyField, a nested
[BaseField](../ScriptReference/UIElements.BaseField_1.html) element is created
based on the property type. For example, if you bind an int property to a
PropertyField, an [IntegerField](UIE-uxml-element-IntegerField.html) is nested
inside the PropertyField.

**Note** : It’s recommended to use [SerializedObject data binding](UIE-editor-
binding.html) for values that are serialized, and [runtime data binding](UIE-
runtime-binding.html) for other attributes, such as names and style
properties.

## Align a PropertyField with other fields in an Inspector window

By default, PropertyFields are created with the `.unity-base-field__aligned`
USS class, which is also applied to each nested field that gets created upon
binding. However, if you manually add a child BaseField element to a
PropertyField, you must add the style class manually to that child field
element. When the `.unity-base-field__aligned` class is present in an
InspectorElement, the field calculates the label width to align with other
fields in the **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. If there are IMGUI fields
present, **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit fields are aligned with them for
consistency and compatibility.

## C# base class and namespace

**C# class** :
[`PropertyField`](../ScriptReference/UIElements.PropertyField.html)  
**Namespace** : `UnityEditor.UIElements`  
**Base class** :
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html)

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`label` | `string` | Optionally overwrite the label of the generate property field. If no label is provided the string will be taken from the SerializedProperty.  
  
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
`ussClassName` | `.unity-property-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-property-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-property-field__input` | USS class name of input elements in elements of this type.  
`inspectorElementUssClassName` | `.unity-property-field__inspector-property` | USS class name of property fields in inspector elements  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the [Matching Selectors section in the Inspector or the UI
Toolkit Debugger](UIB-testing-ui.html#matching-selectors) to see which USS
selectors affect the components of the `VisualElement` at every level of its
hierarchy.

## Additional resources

  * [Create a custom inspector](UIE-HowTo-CreateCustomInspector.html)
  * [TextField](UIE-uxml-element-TextField.html)
  * [DoubleField](UIE-uxml-element-DoubleField.html)
  * [LongField](UIE-uxml-element-LongField.html)
  * [FloatField](UIE-uxml-element-FloatField.html)
  * [IntegerField](UIE-uxml-element-IntegerField.html)

[](UIE-uxml-element-ProgressBar.html)

ProgressBar

[](UIE-uxml-element-RadioButton.html)

RadioButton

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

