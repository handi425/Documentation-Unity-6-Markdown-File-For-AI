[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-events-handling-custom-control.html)
  * [中文](/cn/current/Manual/UIE-events-handling-custom-control.html)
  * [日本語](/ja/current/Manual/UIE-events-handling-custom-control.html)
  * [한국어](/kr/current/Manual/UIE-events-handling-custom-control.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-events-handling-custom-control.html)
  * [中文](/cn/current/Manual/UIE-events-handling-custom-control.html)
  * [日本語](/ja/current/Manual/UIE-events-handling-custom-control.html)
  * [한국어](/kr/current/Manual/UIE-events-handling-custom-control.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * Respond to events with custom controls

[](UIE-focus-order.html)

Focus order of elements

[](UIE-manipulators.html)

Manipulators

# Respond to events with custom controls

If you’re implementing [custom controls](UIE-custom-controls.html), you can
respond to **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit events in the following ways:

  * [Register an event callback](UIE-Events-Handling.html#register-an-event-callback)
  * Override the HandleEventBubbleUp or HandleEventTrickleDown virtual methods

Your response to events depends on the situation. The following are the
differences between callbacks and virtual method overrides:

  * Callbacks must register on instances of the class. Virtual methods require modifying the class itself.
  * Virtual method overrides have a slight performance advantage because they don’t require a lookup in the callback registry during the propagation phase.

## Override the HandleEventBubbleUp or HandleEventTrickleDown virtual methods

A virtual method override applies to all instances of the class. For a class
that overrides
[`HandleEventBubbleUp`](../ScriptReference/UIElements.CallbackEventHandler.HandleEventBubbleUp.html)
or
[`HandleEventTrickleDown`](../ScriptReference/UIElements.CallbackEventHandler.HandleEventTrickleDown.html),
you can also register callbacks on its instances.

To override the `HandleEventBubbleUp` or `HandleEventTrickleDown` methods, or
both, derive a new subclass of `VisualElement`.

`HandleEventBubbleUp` and `HandleEventTrickleDown` execute on each instance of
a **visual element** A node of a visual tree that instantiates or derives from
the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html)
class. You can style the look, define the behaviour, and display it on screen
as part of the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) subclass when that instance
receives an event.

The following example shows how to customize those virtual methods:

    
    
    override void HandleEventBubbleUp(EventBase evt)
    {
        // Call the base function.
        base.HandleEventBubbleUp(evt);
    
        if (evt.eventTypeId == PointerDownEvent.TypeId())
        {
            // ...
        }
        else if (evt.eventTypeId == MouseUpEvent.TypeId())
        {
            // ...
        }
        // More event types
    }
    

For a given class instance, executing custom code in the following cases have
the same results:

  * In a callback set for the BubbleUp phase
  * In the HandleEventBubbleUp method override

In either case, if you stop the propagation of the event, it prevents
reactions to the event after you have executed the current target callbacks
and method overrides.

## Best practices

The following are best practices for handing events with custom controls.

### Implement behaviors

In general, to implement behaviors from your element, use a
`HandleEventBubbleUp` method override.

Given that the BubbleUp is the default propagation phase for callbacks, you
can move any code from callbacks to a `HandleEventBubbleUp` method without any
concerns about changing the timing of code execution.

The benefits of implementing behaviors as method overrides include:

  * Method overrides don’t require a lookup in the callback registry.
  * Instances without callbacks don’t enter the propagation process.

### Stop event propagation

When handling an event inside a callback or a virtual method override, you can
stop further event propagation by calling one of the StopPropagation methods
on the event. For example, a parent panel might stop propagation during the
trickle-down phase to prevent its children from receiving events.

You can’t prevent the execution of the
[`EventBase.PreDispatch()`](../ScriptReference/UIElements.EventBase.PreDispatch.html)
and
[`EventBase.PostDispatch()`](../ScriptReference/UIElements.EventBase.PostDispatch.html)
methods inside the event class itself.

The following methods affect event propagation:

  * [`StopImmediatePropagation()`](../ScriptReference/UIElements.EventBase.StopImmediatePropagation.html): Stops the event propagation process immediately to prevent any subsequent callbacks from executing for the event.
  * [`StopPropagation()`](../ScriptReference/UIElements.EventBase.StopPropagation.html): Stops the event propagation process after the last callback on the current element. This ensures that all callbacks execute on the current element, while preventing any further elements from responding to the event.

## Additional resources

  * [HandleEventBubbleUp](../ScriptReference/UIElements.CallbackEventHandler.HandleEventBubbleUp.html)
  * [HandleEventTrickleDown](../ScriptReference/UIElements.CallbackEventHandler.HandleEventTrickleDown.html)
  * [EventBase.PreDispatch()](../ScriptReference/UIElements.EventBase.PreDispatch.html)
  * [EventBase.PostDispatch()](../ScriptReference/UIElements.EventBase.PostDispatch.html)
  * [StopImmediatePropagation()](../ScriptReference/UIElements.EventBase.StopImmediatePropagation.html)
  * [StopPropagation()](../ScriptReference/UIElements.EventBase.StopPropagation.html)

[](UIE-focus-order.html)

Focus order of elements

[](UIE-manipulators.html)

Manipulators

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

