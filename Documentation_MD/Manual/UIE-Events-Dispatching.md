[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Events-Dispatching.html)
  * [中文](/cn/current/Manual/UIE-Events-Dispatching.html)
  * [日本語](/ja/current/Manual/UIE-Events-Dispatching.html)
  * [한국어](/kr/current/Manual/UIE-Events-Dispatching.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Events-Dispatching.html)
  * [中文](/cn/current/Manual/UIE-Events-Dispatching.html)
  * [日本語](/ja/current/Manual/UIE-Events-Dispatching.html)
  * [한국어](/kr/current/Manual/UIE-Events-Dispatching.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * Dispatch events

[](UIE-Events.html)

Control behavior with events

[](UIE-capture-the-pointer.html)

Capture the pointer with a manipulator

# Dispatch events

The **event system** A way of sending events to objects in the application
based on input, be it keyboard, mouse, touch, or custom input. The Event
System consists of a few components that work together to send events. [More
info](UIE-Runtime-Event-System.html)  
See in [Glossary](Glossary.html#EventSystem) listens for events that come from
the operating system or **scripts** A piece of code that allows you to create
your own Components, trigger game events, modify Component properties over
time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts), then uses the
[EventDispatcher](../ScriptReference/UIElements.EventDispatcher.html) to
dispatch those events to **visual elements** A node of a visual tree that
instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement). The event dispatcher
determines an appropriate dispatching strategy for each event it sends. Once
determined, the dispatcher executes the strategy.

Visual elements implement default behaviors for several events. This involves
the creation and execution of additional events. For example, a
[`PointerMoveEvent`](../ScriptReference/UIElements.PointerMoveEvent.html) can
generate an additional
[`PointerEnterEvent`](../ScriptReference/UIElements.PointerEnterEvent.html)
and a
[`PointerLeaveEvent`](../ScriptReference/UIElements.PointerLeaveEvent.html).
These events enter a queue and process after the current event. For example,
the `PointerMoveEvent` finishes processing before the `PointerEnterEvent` and
`PointerLeaveEvent` events.

## Dispatch behavior of event types

Each event type has its own dispatch behavior. The behavior of each event type
breaks down into two stages:

  * **Trickles down** : Events sent to elements during the trickle-down phase.
  * **Bubbles up** : Events sent to elements during the bubble-up phase.

For a list of dispatch behavior for each event type, see the [Event reference
page](UIE-Events-Reference.html).

## Event propagation

After the event dispatcher selects the event target, it computes the
propagation path of the event. The propagation path is an ordered list of
visual elements that receive the event. The propagation path occurs in the
following order:

  1. The path starts at the root of the visual element tree and descends towards the target. This is the **trickle-down phase**.
  2. The event target receives the event.
  3. The event then ascends the tree towards the root. This is the **bubble-up phase**.

![Propagation path](../uploads/Main/UIElementsEvents.png) Propagation path

Most event types are sent to all elements along the propagation path. Some
event types skip the bubble-up phase, and some event types are sent to the
event target only.

If you hide or disable an element, it won’t receive events. Events still
propagate to the ancestors and descendants of a hidden or disabled element.

## Event target

As an event travels along the propagation path, `Event.currentTarget` updates
to the element handling the event. Within an event callback function, there
are two properties that log the dispatch behavior:

  * [`EventBase.currentTarget`](../ScriptReference/UIElements.EventBase-currentTarget.html) is the visual element on which the callback was registered.
  * [`EventBase.target`](../ScriptReference/UIElements.EventBase-target.html) is the element where the event occurs, for example, the element directly under the pointer.

The target of an event depends on the event type. For pointer events, the
target is most commonly the topmost pickable element, directly under the
pointer. For keyboard events, the target is the element that has focus.

UI Toolkit events have a `target` property that contains a reference to the
element where the event occurred. For most events that originate from the
operating system, the dispatch process finds the event target automatically.

The target element is stored in `EventBase.target` and doesn’t change during
the dispatch process. The property `Event.currentTarget` updates to the visual
element currently handling the event.

## Picking mode and custom shapes

Most pointer events use the picking mode to decide their target. The
`VisualElement` class has a `pickingMode` property that supports the following
values:

  * [`PickingMode.Position`](../ScriptReference/UIElements.PickingMode.Position.html) (default): performs picking based on the position rectangle.
  * [`PickingMode.Ignore`](../ScriptReference/UIElements.PickingMode.Ignore.html): prevents picking as the result of a pointer event.

You can override the
[`VisualElement.ContainsPoint()`](../ScriptReference/UIElements.VisualElement.ContainsPoint.html)
method to perform custom intersection logic.

## Additional resources

  * [Handle event callbacks and value changes](UIE-Events-Handling.html)
  * [Synthesize and send events](UIE-Events-Synthesizing.html)
  * [Events reference](UIE-Events-Reference.html)

[](UIE-Events.html)

Control behavior with events

[](UIE-capture-the-pointer.html)

Capture the pointer with a manipulator

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

