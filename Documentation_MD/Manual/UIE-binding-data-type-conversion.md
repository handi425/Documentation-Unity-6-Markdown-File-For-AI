[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-binding-data-type-conversion.html)
  * [中文](/cn/current/Manual/UIE-binding-data-type-conversion.html)
  * [日本語](/ja/current/Manual/UIE-binding-data-type-conversion.html)
  * [한국어](/kr/current/Manual/UIE-binding-data-type-conversion.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-binding-data-type-conversion.html)
  * [中文](/cn/current/Manual/UIE-binding-data-type-conversion.html)
  * [日本語](/ja/current/Manual/UIE-binding-data-type-conversion.html)
  * [한국어](/kr/current/Manual/UIE-binding-data-type-conversion.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [SerializedObject data binding](UIE-editor-binding.html)
  * Bindable data types and fields

[](UIE-bindable-elements.html)

Bindable elements reference

[](UIE-binding-implementation-details.html)

Binding system implementation details

# Bindable data types and fields

This section describes the data type conversions and fields supported by
[`PropertyField`](../ScriptReference/UIElements.PropertyField.html).

## Data type conversions

Most built-in controls in UI Toolkit implement the
[`INotifyValueChanged`](../ScriptReference/UIElements.INotifyValueChanged_1.html)
interface for a specific data type. For example, `DoubleField` implements
`INotifyValueChanged<Double>`, which means you can bind the `DoubleField`
control to a property of type `double`. You can bind more data types with the
binding system. For example, you can bind a property of type `int` to a
`DoubleField`.

The following table lists the source and target data types that you can bind:

**Source data type** | **Target data type of`INotifyValueChanged`**  
---|---  
`long` | 

  * `long`
  * `int`
  * `string`
  * `float`

  
`int` | 

  * `int`
  * `string`
  * `float`

  
`double` | 

  * `double`
  * `float`

  
`float` | 

  * `float`
  * `double`

  
`char` | 

  * `char`
  * `string`

  
  
**Note** : To prevent data loss, use a
[`PropertyField`](../ScriptReference/UIElements.PropertyField.html) or use the
appropriate data types as shown in the Fields supported by PropertyField table
below.

## Fields supported by `PropertyField`

When the **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window is populated, if a custom
Editor doesn’t exist for a type, the binding system calls
[`InspectorElement.FillDefaultInspector()`](../ScriptReference/UIElements.InspectorElement.FillDefaultInspector.html).
This creates a
[`PropertyField`](../ScriptReference/UIElements.PropertyField.html) for each
[`SerializedProperty`](../ScriptReference/SerializedProperty.html) on the
`SerializedObject`.

Each [`PropertyField`](../ScriptReference/UIElements.PropertyField.html) has a
matching control under it, such as an `IntegerField` to represent an `int`, or
a `Toggle` to represent a `bool`. If the property has sub-properties, the
[`PropertyField`](../ScriptReference/UIElements.PropertyField.html) has a
`Foldout` control. That `Foldout` has the appropriate default controls under
each sub-property. If you created a custom `PropertyDrawer` for a Property,
the **visual tree** An object graph, made of lightweight nodes, that holds all
the elements in a window or panel. It defines every UI you build with the UI
Toolkit.  
See in [Glossary](Glossary.html#Visualtree) returned from the
`PropertyDrawer`’s `CreatePropertyGUI()` method is used instead.

**Note** :

When you create a custom **UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More info](UI-
system-compare.html)  
See in [Glossary](Glossary.html#UI), don’t use a
[`PropertyField`](../ScriptReference/UIElements.PropertyField.html) unless you
can’t find a specific control for it. For example, to create a control in your
visual tree and bind it to a `Color`, use a
[`ColorField`](../ScriptReference/UIElements.ColorField.html) rather than a
[`PropertyField`](../ScriptReference/UIElements.PropertyField.html). This
makes visual trees more lightweight and operations faster.

The use of `PropertyField` incurs additional overhead because it resolves the
concrete field to use after binding. This extra step can affect performance.
However, `PropertyField` is beneficial for some uses. For example, it supports
custom drawers, which you can use to handle specific properties in a
personalized way. This eliminates the need to guess the field type for
drawing, which can reduce errors.

The following table lists fields supported by
[`PropertyField`](../ScriptReference/UIElements.PropertyField.html) and their
data type:

**Field** | **Data type**  
---|---  
[`BoundsField`](../ScriptReference/UIElements.BoundsField.html) | Bounds  
[`BoundsIntField`](../ScriptReference/UIElements.BoundsIntField.html) | BoundsInt  
[`ColorField`](../ScriptReference/UIElements.ColorField.html) | Color  
[`CurveField`](../ScriptReference/UIElements.CurveField.html) | AnimationCurve  
[`FloatField`](../ScriptReference/UIElements.FloatField.html) | float  
[`GradientField`](../ScriptReference/UIElements.GradientField.html) | Gradient  
[`Hash128Field`](../ScriptReference/UIElements.Hash128Field.html) | Hash128  
[`IntegerField`](../ScriptReference/UIElements.IntegerField.html) | int  
[`IntegerField`](../ScriptReference/UIElements.IntegerField.html) | int, for the ArraySize  
[`LayerMaskField`](../ScriptReference/UIElements.LayerMaskField.html) | unit  
[`LongField`](../ScriptReference/UIElements.LongField.html) | long  
[`ObjectField`](../ScriptReference/UIElements.ObjectField.html) | UnityEngine.Object  
[`PopupField`](../ScriptReference/UIElements.PopupField_1.html)<string> | Enum  
[`RectField`](../ScriptReference/UIElements.RectField.html) | Rect  
[`RectIntField`](../ScriptReference/UIElements.RectIntField.html) | RectInt  
[`TextField`](../ScriptReference/UIElements.TextField.html) | string  
[`TextField`](../ScriptReference/UIElements.TextField.html), with a maxLength=1 | char  
[`Toggle`](../ScriptReference/UIElements.Toggle.html) | bool  
[`Vector2Field`](../ScriptReference/UIElements.Vector2Field.html) | Vector2  
[`Vector2IntField`](../ScriptReference/UIElements.Vector2IntField.html) | Vector2Int  
[`Vector3Field`](../ScriptReference/UIElements.Vector3Field.html) | Vector3  
[`Vector3IntField`](../ScriptReference/UIElements.Vector3IntField.html) | Vector3Int  
[`Vector4Field`](../ScriptReference/UIElements.Vector4Field.html) | Vector4  
  
## Additional resources

  * [SerializedObject data binding](UIE-Binding.html)
  * [Bindable elements](UIE-bindable-elements.html)
  * [Implementation details](UIE-binding-implementation-details.html)
  * [Binding examples](UIE-binding-examples.html)

[](UIE-bindable-elements.html)

Bindable elements reference

[](UIE-binding-implementation-details.html)

Binding system implementation details

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

