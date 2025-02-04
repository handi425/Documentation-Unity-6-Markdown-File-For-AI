[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-create-custom-controls.html)
  * [中文](/cn/current/Manual/UIE-create-custom-controls.html)
  * [日本語](/ja/current/Manual/UIE-create-custom-controls.html)
  * [한국어](/kr/current/Manual/UIE-create-custom-controls.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-create-custom-controls.html)
  * [中文](/cn/current/Manual/UIE-create-custom-controls.html)
  * [日本語](/ja/current/Manual/UIE-create-custom-controls.html)
  * [한국어](/kr/current/Manual/UIE-create-custom-controls.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Custom controls](UIE-custom-controls.html)
  * Create a custom control

[](UIE-custom-controls.html)

Custom controls

[](UIE-custom-tag-name-and-attributes.html)

Customize UXML tag names and attributes

# Create a custom control

A good custom control is abstract, self-contained, and recurring.

A [Slide Toggle](UIE-slide-toggle.html) is a good example of a custom control:

  * It’s abstract. You use it to switch between one setting and another.
  * It’s self-contained. You give it a label and an initial value. A Slide Toggle triggers an event when its state changes.
  * It’s recurring. You can use it in multiple places in an application.

The menu bar of your application isn’t a good example of a custom control:

  * It’s not abstract. It’s specific to your application.
  * It’s not self-contained. It probably has dependencies on other parts of your application.
  * It’s not recurring. There is probably only one menu in your application.

After you have created a custom control, you can style it with USS and add
logic to handle events in C#.

## Create and use a custom control

To create a custom control, do the following:

  * Add the [`UxmlElement`](../ScriptReference/UIElements.UxmlElementAttribute.html) attribute to the custom control class definition.
  * Declare the custom control class as a partial class.
  * Inherit it from [`VisualElement`](../ScriptReference/UIElements.VisualElement.html) or one of its derived classes.

For example:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    [UxmlElement]
    public partial class ExampleElement : VisualElement {}
    

You can use your custom controls in UXML and **UI**(User Interface) Allows a
user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder after you create them.

The following example UXML document uses the custom control:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements">
        <ExampleElement />
    </ui:UXML>
    

By default, the custom control appears in the Library tab in UI Builder. If
you want to hide it from the Library tab, add the
[`HideInInspector`](../ScriptReference/HideInInspector.html) attribute.

## Initialize a custom control

Custom controls inherit from `VisualElement`. A `VisualElement` isn’t bound to
the lifetime of a **GameObject** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and doesn’t receive any of these
callbacks:

  * `Awake()`
  * `OnEnable()`
  * `OnDisable()`
  * `OnDestroy()`

You can initialize a custom control in its constructor. However, if your
application needs it, you can delay initialization until the custom control is
added to the UI. To do this, register a callback for an
[`AttachToPanelEvent`](../ScriptReference/UIElements.AttachToPanelEvent.html).
To detect that your custom control has been removed from the UI, use the
[`DetachFromPanelEvent`](../ScriptReference/UIElements.DetachFromPanelEvent.html)
callback.

    
    
    public CustomControl()
    {
        RegisterCallback<AttachToPanelEvent>(e =>
            { /* do something here when element is added to UI */ });
        RegisterCallback<DetachFromPanelEvent>(e =>
            { /* do something here when element is removed from UI */ });
    }
    

UI Toolkit dispatches these two events for all elements and doesn’t need a
custom `VisualElement` subclass. For more information, refer to [Panel
events](UIE-Panel-Events.html).

## Style custom controls with USS

Use USS to customize the look of a custom control the same way as a built-in
control. You can also create [USS custom properties](UIE-USS-
CustomProperties.html) to style a custom control.

**Note** : The **Inspector** A Unity window that displays information about
the currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window in the UI Builder doesn’t
show USS custom properties. To edit USS custom properties, use a text editor
to edit your USS file directly.

To interact with custom USS properties for a custom control in C#, use the
[`CustomStyleProperty`](../ScriptReference/UIElements.CustomStyleProperty_1.html)
structure and the
[`CustomStylesResolvedEvent`](../ScriptReference/UIElements.CustomStyleResolvedEvent.html)
event.

[`CustomStyleProperty`](../ScriptReference/UIElements.CustomStyleProperty_1.html)
describes the name and type of property you read from the stylesheet.

UI Toolkit dispatches
[`CustomStylesResolvedEvent`](../ScriptReference/UIElements.CustomStyleResolvedEvent.html)
for any element that directly receives a custom USS property. It dispatches
the event for any element that a selector matches, for selectors where the
rule contains the value of the custom property. UI Toolkit doesn’t dispatch
the event for elements that inherit the value. The event holds a reference to
an [`ICustomStyle`](../ScriptReference/UIElements.ICustomStyle.html) object.
You must use its
[`TryGetValue()`](../ScriptReference/UIElements.ICustomStyle.TryGetValue.html)
method to read the effective value of a
[`CustomStyleProperty`](../ScriptReference/UIElements.CustomStyleProperty_1.html).
This method has overloads for different types of
[`CustomStyleProperty`](../ScriptReference/UIElements.CustomStyleProperty_1.html).

For a custom style with a custom control example, refer to [Create custom
style for a custom control](UIE-create-custom-style-custom-control.html).

**Note** : You can’t define transitions for custom style properties.

## Handle events for custom controls

For detailed information on how to handle events for custom controls, refer to
[Handle events](UIE-Events-Handling.html).

**Note** :

  * Unity dispatches keyboard events to the currently focused element. To handle [keyboard events](UIE-Keyboard-Events.html) for a custom control, set properties related to `focus`.
  * To handle touch and mouse input events, register callbacks for the relevant event types, such as [pointer events](UIE-Pointer-Events.html) and [mouse events](UIE-Mouse-Events.html), in the constructor.

## Best practices and tips

  * Expose properties that a custom control represents and other functional aspects of its behavior as UXML properties, and expose properties that affect the look of a custom control as USS properties.

  * Use a namespace that’s unique, short, and readable to avoid name **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) with other elements.

  * Keep UXML attributes primitive. Data that you can specify in UXML is limited to a set of primitive data types. UXML doesn’t support complex data structures or collections. Pass complex data to your custom controls at runtime via C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) or data binding, not in UXML.

  * In C#, expose USS classes or names as constants. This allows you to locate elements by class or name using [UQuery](UIE-UQuery.html).

  * Adopt the [BEM standard](https://sparkbox.com/foundry/bem_by_example) for USS classes. This allows you to address every element with a class list selector.

  * Use static callbacks for a lower memory footprint. When you register an instance method to be used as a callback, you might create unnecessary allocations. To avoid allocations, use anonymous static lambda functions that call into regular C# static methods. You can retrieve the context of the current element through the [`EventBase.currentTarget`](../ScriptReference/UIElements.EventBase-currentTarget.html) property.

  * Render custom geometry through the [`generateVisualContent`](../ScriptReference/UIElements.VisualElement-generateVisualContent.html) callback for custom controls. For an example usage that renders a partially filled circle, refer to the [RadialProgress example](UIE-radial-progress.html).

  * Custom controls are convenient. However, you might achieve the same outcomes with the following:

    * Assemble your UI from existing elements, and change their styles and properties.
    * Use UXML templates. Use regular C# `MonoBehaviour`s to add logic that pertains to the specific UI Document that holds your UI. (To learn how to use `MonoBehaviour`s to control UI in a UI Document, see [Create your first runtime UI](UIE-HowTo-CreateRuntimeUI.html).) To achieve encapsulation, create properties and methods inside your `MonoBehaviour` that internally fetch [`VisualElement`](../ScriptReference/UIElements.VisualElement.html)s with [UQuery](UIE-UQuery.html) and manipulate their properties.

## Additional resources

  * [Customize UXML tag names and attributes](UIE-custom-tag-name-and-attributes.html)
  * [Bind custom control to data](UIE-bind-custom-control-to-data.html)
  * [Define a namespace prefix](UIE-define-a-namespace-prefix.html)
  * [Create a custom control with two attributes](UIB-structuring-ui-custom-elements.html)
  * [Create a slide toggle custom control](UIE-slide-toggle.html)
  * [Create a radial progress indicator](UIE-radial-progress.html)
  * [Create a bindable custom control](UIE-create-bindable-custom-control.html)
  * [Create a custom style for a custom control](UIE-create-custom-style-custom-control.html)

[](UIE-custom-controls.html)

Custom controls

[](UIE-custom-tag-name-and-attributes.html)

Customize UXML tag names and attributes

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

