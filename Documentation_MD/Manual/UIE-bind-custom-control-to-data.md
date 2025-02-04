[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-bind-custom-control-to-data.html)
  * [中文](/cn/current/Manual/UIE-bind-custom-control-to-data.html)
  * [日本語](/ja/current/Manual/UIE-bind-custom-control-to-data.html)
  * [한국어](/kr/current/Manual/UIE-bind-custom-control-to-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-bind-custom-control-to-data.html)
  * [中文](/cn/current/Manual/UIE-bind-custom-control-to-data.html)
  * [日本語](/ja/current/Manual/UIE-bind-custom-control-to-data.html)
  * [한국어](/kr/current/Manual/UIE-bind-custom-control-to-data.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Custom controls](UIE-custom-controls.html)
  * Bind custom controls to data

[](UIE-custom-tag-name-and-attributes.html)

Customize UXML tag names and attributes

[](UIE-define-a-namespace-prefix.html)

Define a namespace prefix

# Bind custom controls to data

You bind custom controls to serialized properties to synchronize values
between the control and the property. You can create a bindable custom control
derived from the [`BaseField`](../ScriptReference/UIElements.BaseField_1.html)
generic base class instead of
[`BindableElement`](../ScriptReference/UIElements.BindableElement.html). This
provides the following advantages:

  * Implements the `INotifyValueChanged` interface for the generic parameter type that you specify.
  * Makes the control focusable by default.
  * Provides a horizontal layout with a label element on the left and input on the right.

![FloatField is a built-in UI Toolkit control which inherits from
BaseField.<br/>A. The label element.<br/>B. The input
element.](../uploads/Main/base-field-example.png) FloatField is a built-in UI
Toolkit control which inherits from `BaseField`.  
A. The label element.  
B. The input element.

**Note** : It’s possible to create custom controls derived from built-in
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) controls if you understand their internal
hierarchy and existing USS classes. Unity discourages this practice because
your custom controls might be dependent on their internal structure, which is
subject to change in the future.

To [bind](UIE-Binding.html) custom controls to data:

  * Implement the [`INotifyValueChanged`](../ScriptReference/UIElements.INotifyValueChanged_1.html) interface and listen for [`ChangeEvent`](../ScriptReference/UIElements.ChangeEvent_1.html)s as needed.
  * Inherit from the [`BindableElement`](../ScriptReference/UIElements.BindableElement.html) class or implement the [`IBindable`](../ScriptReference/UIElements.IBindable.html) interface.

Refer to [SerializedObject data binding](UIE-Binding.html) for more details.

For a bindable custom control example, refer to [Create a bindable custom
control](UIE-create-bindable-custom-control.html).

## Additional resources

  * [Create custom controls](UIE-create-custom-controls.html)
  * [SerializedObject data binding](UIE-Binding.html)
  * [Create a bindable custom control](UIE-create-bindable-custom-control.html)

[](UIE-custom-tag-name-and-attributes.html)

Customize UXML tag names and attributes

[](UIE-define-a-namespace-prefix.html)

Define a namespace prefix

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

