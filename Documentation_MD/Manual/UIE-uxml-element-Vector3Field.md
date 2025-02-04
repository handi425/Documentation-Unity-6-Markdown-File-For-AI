[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-uxml-element-Vector3Field.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-Vector3Field.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-Vector3Field.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-Vector3Field.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-uxml-element-Vector3Field.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-Vector3Field.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-Vector3Field.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-Vector3Field.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Visual elements reference](UIE-ElementRef.html)
  * Vector3Field

[](UIE-uxml-element-Vector2IntField.html)

Vector2IntField

[](UIE-uxml-element-Vector3IntField.html)

Vector3IntField

# Vector3Field

A Vector3Field lets users enter a [Vector3](../ScriptReference/Vector3.html)
value.

**Note** : To align a Vector3Field with other fields in an **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, simply apply the `.unity-
base-field__aligned` USS class to it. For more information, refer to
[`BaseField`](../ScriptReference/UIElements.BaseField_1.html).

## Create a Vector3Field

You can create a Vector3Field with **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder, UXML, and C#. The following C#
example creates a Vector3Field with the default value `(15.5, 12.5, 14.5)`:

    
    
    Vector3Field myElement = new Vector3Field("Label text");
    // Set the default value to (15.5, 12.5, 14.5).
    myElement.value = new Vector3(15.5f, 12.5f, 14.5f);
    

## Example

The following UXML example creates a Vector3Field with a placeholder:

    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <Vector3Field label="UXML Field" name="the-uxml-field" />
    </UXML>
    

The following C# example illustrates some of the customizable functionalities
of the Vector3Field:

    
    
    /// <sample>
    // Get a reference to the field from UXML and assign a value to it.
    var uxmlField = container.Q<Vector3Field>("the-uxml-field");
    uxmlField.value = new Vector3(23.8f, 12.6f, 88.3f);
    
    // Create a new field, disable it, and give it a style class.
    var csharpField = new Vector3Field("C# Field");
    csharpField.SetEnabled(false);
    csharpField.AddToClassList("some-styled-field");
    csharpField.value = uxmlField.value;
    container.Add(csharpField);
    
    // Mirror the value of the UXML field into the C# field.
    uxmlField.RegisterCallback<ChangeEvent<Vector3>>((evt) =>
    {
        csharpField.value = evt.newValue;
    });
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** >
**Samples**.

## C# base class and namespace

**C# class** :
[`Vector3Field`](../ScriptReference/UIElements.Vector3Field.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** :
[`BaseCompositeField_3`](../ScriptReference/UIElements.BaseCompositeField_3.html)

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `Vector3` | The value associated with the field.  
  
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
`ussClassName` | `.unity-vector3-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-vector3-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-vector3-field__input` | USS class name of input elements in elements of this type.  
`ussClassName` | `.unity-composite-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-composite-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-composite-field__input` | USS class name of input elements in elements of this type.  
`spacerUssClassName` | `.unity-composite-field__field-spacer` | USS class name of spacers in elements of this type.  
`multilineVariantUssClassName` | `.unity-composite-field--multi-line` | USS class name of elements of this type when the fields are displayed on multiple lines.  
`fieldGroupUssClassName` | `.unity-composite-field__field-group` | USS class name of field groups in elements of this type.  
`fieldUssClassName` | `.unity-composite-field__field` | USS class name of fields in elements of this type.  
`firstFieldVariantUssClassName` | `.unity-composite-field__field--first` | USS class name of the first field in elements of this type.  
`twoLinesVariantUssClassName` | `.unity-composite-field--two-lines` | USS class name of elements of this type when the fields are displayed on two lines.  
`ussClassName` | `.unity-base-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-field__input` | USS class name of input elements in elements of this type.  
`noLabelVariantUssClassName` | `.unity-base-field--no-label` | USS class name of elements of this type, when there is no label.  
`labelDraggerVariantUssClassName` | `.unity-base-field__label--with-dragger` | USS class name of labels in elements of this type, when there is a dragger attached on them.  
`mixedValueLabelUssClassName` | `.unity-base-field__label--mixed-value` | USS class name of elements that show mixed values  
`alignedFieldUssClassName` | `.unity-base-field__aligned` | USS class name of elements that are aligned in a inspector element  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the [Matching Selectors section in the Inspector or the UI
Toolkit Debugger](UIB-testing-ui.html#matching-selectors) to see which USS
selectors affect the components of the `VisualElement` at every level of its
hierarchy.

## Additional resources

  * [Vector2Field](UIE-uxml-element-Vector2Field.html)
  * [Vector2IntField](UIE-uxml-element-Vector2IntField.html)
  * [Vector3IntField](UIE-uxml-element-Vector3IntField.html)
  * [Vector4Field](UIE-uxml-element-Vector4Field.html)

[](UIE-uxml-element-Vector2IntField.html)

Vector2IntField

[](UIE-uxml-element-Vector3IntField.html)

Vector3IntField

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

