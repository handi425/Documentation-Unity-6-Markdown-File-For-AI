[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-slide-toggle.html)
  * [中文](/cn/current/Manual/UIE-slide-toggle.html)
  * [日本語](/ja/current/Manual/UIE-slide-toggle.html)
  * [한국어](/kr/current/Manual/UIE-slide-toggle.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-slide-toggle.html)
  * [中文](/cn/current/Manual/UIE-slide-toggle.html)
  * [日本語](/ja/current/Manual/UIE-slide-toggle.html)
  * [한국어](/kr/current/Manual/UIE-slide-toggle.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI examples](UIE-uxml-examples.html)
  * Create a slide toggle custom control

[](UIB-structuring-ui-custom-elements.html)

Create a custom control with two attributes

[](UIE-create-bindable-custom-control.html)

Create a bindable custom control

# Create a slide toggle custom control

**Version** : 2023.2+

This example demonstrates how to create a “switch-like” variation of a toggle.

## Example overview

The example creates a custom control: a toggle that users can flip with the
mouse, the keyboard, a gamepad, and other devices. It comes with a label that
can describe what the toggle represents.

![](../uploads/Main/slide-toggle-finished.gif)

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/2023.2/slide-toggle).

## Prerequisites

This guide is for developers familiar with the Unity Editor, **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit, and C# scripting. Before you
start, get familiar with the following:

  * [UI Builder](UIBuilder.html)
  * [Visual Tree](UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree)

  * [UXML](UIE-UXML.html)
  * [USS](UIE-USS.html)
  * [Handling events](UIE-Events-Handling.html)

## Create the slide toggle class

Create the slide toggle class with a C# script.

  1. Create a Unity project with the 3D template. A 3D template has a better visual effect for this example. However, you can use any template.
  2. Create a folder named `slide-toggle` to store your files.
  3. In the `slide-toggle` folder, create a C# script named `SlideToggle.cs`.
  4. Open `SlideToggle.cs` in a text editor and replace its content with the following:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    namespace MyUILibrary
    {
        // Derives from BaseField<bool> base class. Represents a container for its input part.
        [UxmlElement]
        public partial class SlideToggle : BaseField<bool>
        {
            // In the spirit of the BEM standard, the SlideToggle has its own block class and two element classes. It also
            // has a class that represents the enabled state of the toggle.
            public static readonly new string ussClassName = "slide-toggle";
            public static readonly new string inputUssClassName = "slide-toggle__input";
            public static readonly string inputKnobUssClassName = "slide-toggle__input-knob";
            public static readonly string inputCheckedUssClassName = "slide-toggle__input--checked";
    
            VisualElement m_Input;
            VisualElement m_Knob;
    
            // Custom controls need a default constructor. This default constructor calls the other constructor in this
            // class.
            public SlideToggle() : this(null) { }
    
            // This constructor allows users to set the contents of the label.
            public SlideToggle(string label) : base(label, null)
            {
                // Style the control overall.
                AddToClassList(ussClassName);
    
                // Get the BaseField's visual input element and use it as the background of the slide.
                m_Input = this.Q(className: BaseField<bool>.inputUssClassName);
                m_Input.AddToClassList(inputUssClassName);
    
                // Create a "knob" child element for the background to represent the actual slide of the toggle.
                m_Knob = new();
                m_Knob.AddToClassList(inputKnobUssClassName);
                m_Input.Add(m_Knob);
    
                // There are three main ways to activate or deactivate the SlideToggle. All three event handlers use the
                // static function pattern described in the Custom control best practices.
    
                // ClickEvent fires when a sequence of pointer down and pointer up actions occurs.
                RegisterCallback<ClickEvent>(evt => OnClick(evt));
                // KeydownEvent fires when the field has focus and a user presses a key.
                RegisterCallback<KeyDownEvent>(evt => OnKeydownEvent(evt));
                // NavigationSubmitEvent detects input from keyboards, gamepads, or other devices at runtime.
                RegisterCallback<NavigationSubmitEvent>(evt => OnSubmit(evt));
            }
    
            static void OnClick(ClickEvent evt)
            {
                var slideToggle = evt.currentTarget as SlideToggle;
                slideToggle.ToggleValue();
    
                evt.StopPropagation();
            }
    
            static void OnSubmit(NavigationSubmitEvent evt)
            {
                var slideToggle = evt.currentTarget as SlideToggle;
                slideToggle.ToggleValue();
    
                evt.StopPropagation();
            }
    
            static void OnKeydownEvent(KeyDownEvent evt)
            {
                var slideToggle = evt.currentTarget as SlideToggle;
    
                // NavigationSubmitEvent event already covers keydown events at runtime, so this method shouldn't handle
                // them.
                if (slideToggle.panel?.contextType == ContextType.Player)
                    return;
    
                // Toggle the value only when the user presses Enter, Return, or Space.
                if (evt.keyCode == KeyCode.KeypadEnter || evt.keyCode == KeyCode.Return || evt.keyCode == KeyCode.Space)
                {
                    slideToggle.ToggleValue();
                    evt.StopPropagation();
                }
            }
    
            // All three callbacks call this method.
            void ToggleValue()
            {
                value = !value;
            }
    
            // Because ToggleValue() sets the value property, the BaseField class dispatches a ChangeEvent. This results in a
            // call to SetValueWithoutNotify(). This example uses it to style the toggle based on whether it's currently
            // enabled.
            public override void SetValueWithoutNotify(bool newValue)
            {
                base.SetValueWithoutNotify(newValue);
    
                //This line of code styles the input element to look enabled or disabled.
                m_Input.EnableInClassList(inputCheckedUssClassName, newValue);
            }
        }
    }
    

## Style the slide toggle

Style the slide toggle with a USS file.

  1. In the `slide-toggle` folder, create a USS file named `SlideToggle.uss`.
  2. Open `SlideToggle.uss` in a text editor and replace its contents with the following:

    
    
    .slide-toggle__input {
        background-color: var(--unity-colors-slider_groove-background);
        max-width: 25px;
        border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
        overflow: visible;
        border-left-width: 1px;
        border-right-width: 1px;
        border-top-width: 1px;
        border-bottom-width: 1px;
        border-right-color: var(--unity-colors-slider_thumb-border);
        border-top-color: var(--unity-colors-slider_thumb-border);
        border-bottom-color: var(--unity-colors-slider_thumb-border);
        max-height: 16px;
        margin-top: 10px;
        border-left-color: var(--unity-colors-slider_thumb-border);
        transition-property: background-color;
        transition-duration: 0.5s;
    }
    
    .slide-toggle__input-knob {
        height: 16px;
        width: 16px;
        background-color: var(--unity-colors-slider_thumb-background);
        position: absolute;
        border-top-left-radius: 25px;
        border-bottom-left-radius: 25px;
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
        top: -1px;
        transition-property: translate, background-color;
        transition-duration: 0.5s, 0.5s;
        translate: -1px 0;
        border-left-width: 1px;
        border-right-width: 1px;
        border-top-width: 1px;
        border-bottom-width: 1px;
        border-left-color: var(--unity-colors-slider_thumb-border);
        border-right-color: var(--unity-colors-slider_thumb-border);
        border-top-color: var(--unity-colors-slider_thumb-border);
        border-bottom-color: var(--unity-colors-slider_thumb-border);
    }
    
    .slide-toggle__input--checked {
        background-color: rgb(0, 156, 10);
    }
    
    .slide-toggle__input--checked > .slide-toggle__input-knob {
        translate: 8px 0;
    }
    
    .slide-toggle:focus .slide-toggle__input-knob {
        border-left-width: 1px;
        border-right-width: 1px;
        border-top-width: 1px;
        border-bottom-width: 1px;
        border-left-color: var(--unity-colors-input_field-border-focus);
        border-right-color: var(--unity-colors-input_field-border-focus);
        border-top-color: var(--unity-colors-input_field-border-focus);
        border-bottom-color: var(--unity-colors-input_field-border-focus);
    }
    

## Add a slide toggle to a UXML file with the UI Builder

  1. In the `slide-toggle` folder, create a UI Document file named `SlideToggleUsage.uxml`.
  2. Open `SlideToggleUsage.uxml` in the UI Builder.
  3. In the UI Builder, select **Library** > **Project** > **MyUILibrary**.
  4. Drag a **SlideToggle** into the **Hierarchy** window.
  5. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)**, enter a label text for your
toggle in the **Label** field.

  6. In the **StyleSheets** section, add `SlideToggle.uss` as the existing USS.
  7. Save and close the UI Builder.

## Test the slide toggle

  1. In the SampleScene, create a UI Document **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

  2. Select the UI Document, and drag `SlideToggleUsage.uxml` into the **Source Asset** field in the **Inspector**.
  3. Enter play mode. You can click on the toggle, press Enter, press Return, or press Space and get it to flip back and forth.

## Additional resources

  * [Create custom controls](UIE-create-custom-controls.html)
  * [Built-in Unity variables](UIE-USS-UnityVariables.html)
  * [BEM standard](http://getbem.com/)

[](UIB-structuring-ui-custom-elements.html)

Create a custom control with two attributes

[](UIE-create-bindable-custom-control.html)

Create a bindable custom control

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

