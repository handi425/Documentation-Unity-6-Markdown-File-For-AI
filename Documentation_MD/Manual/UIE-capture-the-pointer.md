[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-capture-the-pointer.html)
  * [中文](/cn/current/Manual/UIE-capture-the-pointer.html)
  * [日本語](/ja/current/Manual/UIE-capture-the-pointer.html)
  * [한국어](/kr/current/Manual/UIE-capture-the-pointer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-capture-the-pointer.html)
  * [中文](/cn/current/Manual/UIE-capture-the-pointer.html)
  * [日本語](/ja/current/Manual/UIE-capture-the-pointer.html)
  * [한국어](/kr/current/Manual/UIE-capture-the-pointer.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * Capture the pointer with a manipulator

[](UIE-Events-Dispatching.html)

Dispatch events

[](UIE-Events-Handling.html)

Handle event callbacks and value changes

# Capture the pointer with a manipulator

When you handle pointer input, you might want the control to capture a
pointer. When a **visual element** A node of a visual tree that instantiates
or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) captures a pointer, Unity sends
all the events associated with the pointer to the visual element regardless of
whether the pointer hovers over the visual element. For example, if you create
a control that receives drag events and captures the pointer, the control
still receives drag events regardless of the pointer location.

The [`Manipulator`](../ScriptReference/UIElements.Manipulator.html) class
provides a convenient way to capture the pointer. The `Manipulator` class is a
base class for all manipulators. A manipulator is a class that handles pointer
input and sends events to a visual element. For example, the
[`Clickable`](../ScriptReference/UIElements.Clickable.html) class is a
manipulator that sends a
[`PointerDownEvent`](../ScriptReference/UIElements.PointerDownEvent.html) when
the user clicks on a visual element. After a
[`PointerDownEvent`](../ScriptReference/UIElements.PointerDownEvent.html),
some elements must capture the pointer position to ensure it receives all
subsequent pointer events, even when the cursor is no longer hovering over the
element. For example, when you click on a button, slider, or scroll bar.

To capture the pointer, call
[`PointerCaptureHelper.CapturePointer`](../ScriptReference/UIElements.PointerCaptureHelper.CapturePointer.html).

To release the pointer, call
[`PointerCaptureHelper.ReleasePointer`](../ScriptReference/UIElements.PointerCaptureHelper.ReleasePointer.html).
If another element is already capturing the pointer when you call
`CapturePointer()`, the element receives a
[`PointerCaptureOutEvent`](../ScriptReference/UIElements.PointerCaptureOutEvent.html)
event and loses the capture.

Only one element in the application can have the capture at any moment. While
an element has the capture, it’s the target of all subsequent pointer events
except mouse wheel events. This only applies to pointer events that don’t
already have a set target and rely on the dispatch process to determine the
target.

For more information, see the [Capture events](UIE-Capture-Events.html).

## Additional resources

  * [Capture events](UIE-Capture-Events.html)
  * [Create a drag-and-drop UI inside a custom Editor window](UIE-create-drag-and-drop-ui.html)
  * [Manipulators](UIE-manipulators.html)
  * [Events reference](UIE-Events-Reference.html)

[](UIE-Events-Dispatching.html)

Dispatch events

[](UIE-Events-Handling.html)

Handle event callbacks and value changes

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

