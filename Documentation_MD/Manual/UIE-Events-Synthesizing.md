[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Events-Synthesizing.html)
  * [中文](/cn/current/Manual/UIE-Events-Synthesizing.html)
  * [日本語](/ja/current/Manual/UIE-Events-Synthesizing.html)
  * [한국어](/kr/current/Manual/UIE-Events-Synthesizing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Events-Synthesizing.html)
  * [中文](/cn/current/Manual/UIE-Events-Synthesizing.html)
  * [日本語](/ja/current/Manual/UIE-Events-Synthesizing.html)
  * [한국어](/kr/current/Manual/UIE-Events-Synthesizing.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * Synthesize and send events

[](UIE-manipulators.html)

Manipulators

[](UIE-Events-Reference.html)

Event reference

# Synthesize and send events

Before you synthesize and send custom events, understand [how the UI Toolkit
event system allocates and sends operating system events](UIE-Events-
Dispatching.html).

UI Toolkit sends events to **visual elements** A node of a visual tree that
instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) through the panel. If an event
has no target, it’s sent to the root element of the panel. To have a
propagation path, an element must have a target, and the sender must set that
target in advance. Some event types don’t need a target. For example, keyboard
events are sent to the focused element, and pointer events are sent to the
element under the pointer.

The event system uses a pool of events to avoid allocating event objects
repeatedly.

To synthesize and send your own events:

  1. Get an event object from the pool of events.
  2. Fill in the event properties.
  3. Enclose the event in a `using` block to ensure it’s returned to the event pool.
  4. Pass the event to `panel.visualTree.SendEvent()`.

You can send operating system events, such as keyboard and pointer events. To
do so, use a `UnityEngine.Event` to initialize the **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit event.

The following example demonstrates how to synthesize and send events:

    
    
    void SynthesizeAndSendKeyDownEvent(IPanel panel, KeyCode code,
         char character = '\0', EventModifiers modifiers = EventModifiers.None)
    {
        // Create a UnityEngine.Event to hold initialization data.
        var evt = new Event() {
            type = EventType.KeyDownEvent,
            keyCode = code,
            character = character,
            modifiers = modifiers
        };
    
        using (KeyDownEvent keyDownEvent = KeyDownEvent.GetPooled(evt))
        {
            panel.visualTree.SendEvent(keyDownEvent);
        }
    }
    

**Important** : Don’t send events that are from outside the operating system
or aren’t present in the `UnityEngine.Event` types. UI Toolkit sends some
events as a reaction to internal state changes. External processes must not
send those events. For example, if you send
[`PointerCaptureEvent`](../ScriptReference/UIElements.PointerCaptureEvent.html),
visual elements assume that the underlying conditions for that event are met
and won’t set pointer capture for them. This might break the internal
configurations of the visual element and cause undefined behaviors.

## Additional resources

  * [Events reference](UIE-Events-Reference.html)
  * [Handle event callbacks and value changes](UIE-Events-Handling.html)
  * [Dispatch events](UIE-Events-Dispatching.html)
  * [Manipulators](UIE-manipulators.html)

[](UIE-manipulators.html)

Manipulators

[](UIE-Events-Reference.html)

Event reference

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

