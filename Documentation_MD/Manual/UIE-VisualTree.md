[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-VisualTree.html)
  * [中文](/cn/current/Manual/UIE-VisualTree.html)
  * [日本語](/ja/current/Manual/UIE-VisualTree.html)
  * [한국어](/kr/current/Manual/UIE-VisualTree.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-VisualTree.html)
  * [中文](/cn/current/Manual/UIE-VisualTree.html)
  * [日本語](/ja/current/Manual/UIE-VisualTree.html)
  * [한국어](/kr/current/Manual/UIE-VisualTree.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [The visual tree](UIE-VisualTree-landing.html)
  * Introduction to visual elements and the visual tree

[](UIE-VisualTree-landing.html)

The visual tree

[](UIE-panels.html)

Panels

# Introduction to visual elements and the visual tree

The most basic building block in **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit is a **visual element** A node of
a visual tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement). The visual elements are
ordered into a hierarchy tree with parent-child relationships. This is called
the **visual tree** An object graph, made of lightweight nodes, that holds all
the elements in a window or panel. It defines every UI you build with the UI
Toolkit.  
See in [Glossary](Glossary.html#Visualtree).

The diagram below displays a simplified example of the visual tree, and the
rendered result in UI Toolkit.

![Simplified hierarchy of the visual
tree](../uploads/Main/VisualTreeExample.png) Simplified hierarchy of the
visual tree

The Root in the diagram represents the
[`EditorWindow.rootVisualElement`](../ScriptReference/EditorWindow-
rootVisualElement.html) in the Editor UI and the
[`UIDocument.rootVisualElement`](../ScriptReference/UIElements.UIDocument-
rootVisualElement.html) in a runtime UI.

The [`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class
is the base for all nodes in the visual tree. The `VisualElement` base class
contains properties such as styles, layout data, and event handlers. Visual
elements can have children and descendant visual elements. For example, in the
diagram above, the first `Box` visual element has three child visual elements:
`Label`, `Checkbox`, and `Slider`.

You can customize the appearance of visual elements through inline styles and
stylesheets. You can also use event callbacks to modify the behavior of a
visual element.

[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) derives
into subclasses that define additional behavior and functionality, such as
controls. UI Toolkit includes a variety of built-in controls with specialized
behavior. A control is an element of a graphical user interface. For example,
the following items are available as built-in controls:

  * [Buttons](UIE-uxml-element-Button.html)
  * [Toggles](UIE-uxml-element-Toggle.html)A checkbox that allows the user to switch an option on or off. [More info](UIE-uxml-element-Toggle.html)  
See in [Glossary](Glossary.html#Toggle)

  * [Text input fields](UIE-uxml-element-TextField.html)A field that allows the user to input a Text string [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-InputField.html)  
See in [Glossary](Glossary.html#TextInputField)

A control includes the visual of the control, and the scripted logic to
operate and interact with the control. It can consist of a single visual
element, or a combination of multiple visual elements. For example, the Toggle
control contains three elements:

  * A text label
  * An image of a box
  * An image of a checkmark

![Toggle control](../uploads/Main/uie-toggle-control.png) Toggle control

The implementation of the Toggle control defines the behavior of the control.
It has an internal value of whether the toggle state is true or false. This
logic alternates the visibility of the checkmark image when the value changes.

You can also combine visual elements together and modify their behavior to
create [custom controls](UIE-create-custom-controls.html).

To use a control in a UI, add it to the visual tree.

## Additional resources

  * [Structure UI with UXML](UIE-UXML.html)
  * [Structure UI with C# scripts](UIE-Controls.html)
  * [UXML elements Reference](UIE-ElementRef.html)

[](UIE-VisualTree-landing.html)

The visual tree

[](UIE-panels.html)

Panels

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

