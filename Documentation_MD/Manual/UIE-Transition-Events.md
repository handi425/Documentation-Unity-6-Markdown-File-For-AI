[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Transition-Events.html)
  * [中文](/cn/current/Manual/UIE-Transition-Events.html)
  * [日本語](/ja/current/Manual/UIE-Transition-Events.html)
  * [한국어](/kr/current/Manual/UIE-Transition-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Transition-Events.html)
  * [中文](/cn/current/Manual/UIE-Transition-Events.html)
  * [日本語](/ja/current/Manual/UIE-Transition-Events.html)
  * [한국어](/kr/current/Manual/UIE-Transition-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Transition events

[](UIE-Tooltip-Events.html)

Tooltip event

[](UIE-contextual-menus.html)

Contextual menu events

# Transition events

Transition events inform you of the changes in a transition’s state.

UI Toolkit uses transitions when a `VisualElement`’s style property is
modified. Changes to `VisualElement` property are immediately reflected
visually. However, you can use the [`transition` USS property](UIE-
Transitions.html#transition-properties) to interpolate between the initial and
end results gradually.

## The transition’s lifecycle

A transition’s lifecycle has the following stages:

  1. A `VisualElement`’s property is modified when you:

     * Add or remove a class with C# methods. For example: `element.ToggleInClassList()` (where `element` is any `VisualElement`).
     * Use USS with selectors like `:hover`.
     * Manipulate the element’s `style` property. For example: `element.style.backgroundColor = Color.red;` (where `element` is any `VisualElement`).
  2. A `TransitionRunEvent` is sent.

  3. If the resolved `transition-delay` property for the changing property has a value other than `0`, nothing happens for the duration of the delay.

  4. After the delay, a `TransitionStartEvent` is sent, and the transition starts with the property at its initial value.

  5. For the length of time set by `transition-duration`, the transition occurs. During that time, the property goes from its initial to its final value.

  6. If the property is changed to a new value during the transition, `TransitionCancelEvent` is sent. The transition process restarts at step 2.

  7. After the `transition-duration` elapses, the property sets to its final value. A `TransitionEndEvent` is sent.

## Transition events reference table

The following table describes the transition events and their propagation
phases:

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[TransitionRunEvent](../ScriptReference/UIElements.TransitionRunEvent.html) | Sent when a transition is created. |  | Yes |   
[TransitionStartEvent](../ScriptReference/UIElements.TransitionStartEvent.html) | Sent when a transition’s delay phase ends and the transition starts. |  | Yes |   
[TransitionEndEvent](../ScriptReference/UIElements.TransitionEndEvent.html) | Sent when a transition ends. |  | Yes |   
[TransitionCancelEvent](../ScriptReference/UIElements.TransitionCancelEvent.html) | Sent when an a transition is canceled. |  | Yes |   
  
## Behavior

Each transition property has its own lifecycle and its own transition events.
You can access the current property with an event’s `stylePropertyNames`
property.

If a shorthand USS property is changed, every component also gets its own
lifecycle. For example, if you change `margin`, `margin-left`, `margin-right`,
`margin-top` and `margin-bottom`, they all get their own `TransitionRunEvent`,
`TransitionStartEvent` and `TransitionEndEvent`, for a total of 12 separate
events.

If you set `transition-delay` to `0`, the `TransitionRunEvent` and
`TransitionStartEvent` are sent one after the other within a few milliseconds.

If you set `transition-delay` to a value below `0`, the transition won’t start
at the beginning. For example, with a `transition-delay` of `-3` seconds and
`transition-duration` of `5` seconds, the `TransitionRunEvent` and
`TransitionStartEvent` is sent with an `elapsedTime` property set to `3`
seconds and the transition effectively starts at the third second of a five-
second animation.

## Event list

This section describes the `target`, `stylePropertyNames`, and `elapsedTime`
of each transition event.

### TransitionRunEvent

A `TransitionRunEvent` event is sent when a transition is created.

  * **`target`** : The element that executes the transition.
  * **`stylePropertyNames`** : The list of properties modified by the transition.
  * **`elapsedTime`** : The time since the start of the transition.

### TransitionStartEvent

A `TransitionStartEvent` event is sent when the transition’s delay phase ends
and the transition begins.

  * **`target`** : The element that executes the transition.
  * **`stylePropertyNames`** : The list of properties modified by the transition.
  * **`elapsedTime`** : The time since the start of the transition.

### TransitionEndEvent

A `TransitionEndEvent` event is sent when a transition ends.

  * **`target`** : The element that executes the transition.
  * **`stylePropertyNames`** : The list of properties modified by the transition.
  * **`elapsedTime`** : The time since the start of the transition.

### TransitionCancelEvent

A `TransitionCancelEvent` event is sent when a transition is interrupted by
the property being changed again.

  * **`target`** : The element that executes the transition.
  * **`stylePropertyNames`** : The list of properties modified by the transition.
  * **`elapsedTime`** : The time since the start of the transition.

## Examples

  * [Create a transition event](UIE-transition-event-example.html): This example demonstrates the lifecycle of a transition event.
  * [Create looping transitions](UIE-transition-event-loop-example.html): This example demonstrates how to leverage the `TransitionEndEvent` to create transitions that loop.
  * [Create a simple transition with UI Builder and C# script](UIE-transition-example.html): This example demonstrates how to create simple transitions with the **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder and C# script.

## Additional resources

  * [USS transition](UIE-Transitions.html)

[](UIE-Tooltip-Events.html)

Tooltip event

[](UIE-contextual-menus.html)

Contextual menu events

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

