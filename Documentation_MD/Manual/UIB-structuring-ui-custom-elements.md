[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIB-structuring-ui-custom-elements.html)
  * [中文](/cn/current/Manual/UIB-structuring-ui-custom-elements.html)
  * [日本語](/ja/current/Manual/UIB-structuring-ui-custom-elements.html)
  * [한국어](/kr/current/Manual/UIB-structuring-ui-custom-elements.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIB-structuring-ui-custom-elements.html)
  * [中文](/cn/current/Manual/UIB-structuring-ui-custom-elements.html)
  * [日本語](/ja/current/Manual/UIB-structuring-ui-custom-elements.html)
  * [한국어](/kr/current/Manual/UIB-structuring-ui-custom-elements.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI examples](UIE-uxml-examples.html)
  * Create a custom control with two attributes

[](UIE-create-a-conditional-ui.html)

Use Toggle to create a conditional UI

[](UIE-slide-toggle.html)

Create a slide toggle custom control

# Create a custom control with two attributes

**Version** : 2023.2+

This example demonstrates how to create a simple custom control with two
attributes.

## Example overview

This example creates a custom control called `MyElement` with two attributes
and exposes it to UXML and **UI**(User Interface) Allows a user to interact
with your application. Unity currently supports three UI systems. [More
info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder. This example also shows how to
add a custom control to a UI in the UI Builder.

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/2023.2/create-custom-control-with-custom-attributes).

## Prerequisites

This guide is for developers who are familiar with Unity, UI Toolkit, and C#
scripting. Before you start, get familiar with the following:

  * [UXML](UIE-UXML.html)
  * [UI Builder](UIBuilder.html)

## Create the example

To create a new custom control class in C#, inherit it from the
`VisualElement` class. This allows you to create and use this element in C#,
but won’t automatically expose it in UXML and UI Builder. To expose it, add
the [`UxmlElement`](../ScriptReference/UIElements.UxmlElementAttribute.html)
attribute. To expose the attributes, add the
[`UxmlAttribute`](../ScriptReference/UIElements.UxmlAttributeAttribute.html)
attribute to each property that you want to be visible in UXML and the UI
Builder.

  1. Create a Unity project with any template.
  2. In the `Assets` folder, create a C# script named `MyElement.cs` with the following content:

    
    
    using UnityEngine.UIElements;
    
    [UxmlElement]
    partial class MyElement : VisualElement
    {
        [UxmlAttribute]
        public string myString { get; set; } = "default_value";
    
        [UxmlAttribute]
        public int myInt { get; set; } = 2;
    }
    

## Create a UXML to see the attribute

  1. Create a UXML file with any name you want.
  2. Double-click the UXML file to open it in the UI Builder.
  3. In the **Library** section of the UI Builder, select **Project** > **Custom Controls (C#)** > **MyElement**.
  4. Drag **MyElement** to the Hierarchy window.
  5. To see the custom attributes for **MyElement** , go to the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** tab of **MyElement** :

![Custom attributes for a custom
control](../uploads/Main/UIBuilder/CustomElementAttributes.png) Custom
attributes for a custom control

## Additional resources

  * [Create custom controls](UIE-create-custom-controls.html)

[](UIE-create-a-conditional-ui.html)

Use Toggle to create a conditional UI

[](UIE-slide-toggle.html)

Create a slide toggle custom control

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

