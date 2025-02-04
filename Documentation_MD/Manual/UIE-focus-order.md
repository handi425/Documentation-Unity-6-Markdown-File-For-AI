[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-focus-order.html)
  * [中文](/cn/current/Manual/UIE-focus-order.html)
  * [日本語](/ja/current/Manual/UIE-focus-order.html)
  * [한국어](/kr/current/Manual/UIE-focus-order.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-focus-order.html)
  * [中文](/cn/current/Manual/UIE-focus-order.html)
  * [日本語](/ja/current/Manual/UIE-focus-order.html)
  * [한국어](/kr/current/Manual/UIE-focus-order.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * Focus order of elements

[](UIE-Events-Handling.html)

Handle event callbacks and value changes

[](UIE-events-handling-custom-control.html)

Respond to events with custom controls

# Focus order of elements

Each panel has a focus ring that defines the focus order of elements. By
default, a depth-first search (DFS) on the **visual tree** An object graph,
made of lightweight nodes, that holds all the elements in a window or panel.
It defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree) defines the focus order of
elements. For example, the focus order for the tree depicted below is F, B, A,
D, C, E, G, I, H.

![Focus order](../uploads/Main/focus-order.png) Focus order

Some events use the focus order to define which element holds the focus. For
example, the target for a keyboard event is the element in focus.

Use the `focusable` property to control whether a **visual element** A node of
a visual tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) is focusable. By default,
`VisualElements` aren’t focusable, but some subclasses, such as `TextField`,
might be focusable by default.

Use the `tabIndex` property to control the focus order as follows (`tabIndex`
default value of 0):

  * If the `tabIndex` is negative, you can’t use tab on the element.
  * If the `tabIndex` is zero, the element keeps its default tab order, as determined by the focus ring algorithm.
  * If the `tabIndex` is positive, the element is placed in front of other elements that either have a zero `tabIndex` (`tabIndex = 0`) or a `tabIndex` value smaller than its own.

## Additional resources

  * [Events reference](UIE-Events-Reference.html)

[](UIE-Events-Handling.html)

Handle event callbacks and value changes

[](UIE-events-handling-custom-control.html)

Respond to events with custom controls

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

