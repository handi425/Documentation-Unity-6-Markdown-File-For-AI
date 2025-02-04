[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-manipulators.html)
  * [中文](/cn/current/Manual/UIE-manipulators.html)
  * [日本語](/ja/current/Manual/UIE-manipulators.html)
  * [한국어](/kr/current/Manual/UIE-manipulators.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-manipulators.html)
  * [中文](/cn/current/Manual/UIE-manipulators.html)
  * [日本語](/ja/current/Manual/UIE-manipulators.html)
  * [한국어](/kr/current/Manual/UIE-manipulators.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * Manipulators

[](UIE-events-handling-custom-control.html)

Respond to events with custom controls

[](UIE-Events-Synthesizing.html)

Synthesize and send events

# Manipulators

To separate your event logic from your **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) code, use a manipulator to handle events.
Manipulators are **state machines** The set of states in an Animator
Controller that a character or animated GameObject can be in, along with a set
of transitions between those states and a variable to remember the current
state. The states available will depend on the type of gameplay, but typical
states include things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) that handle user interaction
with UI elements. They store, register, and unregister event callbacks. A
manipulator streamlines setting up that user interaction, so you don’t have to
handle each callback one by one. To handle events, use or inherit from one of
the manipulators that UI Toolkit supports.

To create and use a manipulator:

  1. Define a dedicated class that inherits from a manipulator class supported by UI Toolkit. This class encapsulates the event-handling logic tailored to the specific user interaction you want to manage.
  2. Within the class, implement methods to respond to relevant interactions, such as mouse clicks or drags. These methods capture and process the necessary information to execute the desired behavior.
  3. When you have finished designing the manipulator class, instantiate it and attach it to the target UI element. This attachment lets the manipulator intercept and manage the specified events, orchestrating user interactions while maintaining clear separation from your UI code.

## Supported manipulators

The following table lists the supported manipulator classes:

**Manipulator** | **Inherits from** | **Description**  
---|---|---  
[**`Manipulator`**](../ScriptReference/UIElements.Manipulator.html) |  | Base class for all provided manipulators.  
[**`KeyboardNavigationManipulator`**](../ScriptReference/UIElements.KeyboardNavigationManipulator.html) | `Manipulator` | Handles translation of device-specific input events to higher-level navigation operations with a keyboard.  
[**`MouseManipulator`**](../ScriptReference/UIElements.MouseManipulator.html) | `Manipulator` | Handles mouse input. Has a list of activation filters.  
[**`ContextualMenuManipulator`**](../ScriptReference/UIElements.ContextualMenuManipulator.html) | `MouseManipulator` | Displays a contextual menu when the user clicks the right mouse button or presses the menu key on the keyboard.  
[**`PointerManipulator`**](../ScriptReference/UIElements.PointerManipulator.html) | `MouseManipulator` | Handles pointer input. Has a list of activation filters.  
[**`Clickable`**](../ScriptReference/UIElements.Clickable.html) | `PointerManipulator` | Tracks mouse events on an element, and identifies when a click occurs, which is both a pointer press and release on the same element.  
  
## Examples

The following examples demonstrate how to use manipulators to handle events.
They do the following:

  * Inherit the manipulators from the [`PointerManipulators`](../ScriptReference/UIElements.PointerManipulator.html) class, which handles mouse input.
  * Use the [`activators`](../ScriptReference/UIElements.MouseManipulator-activators.html) list to specify the conditions that activate the manipulator. For example, to activate the manipulator when the user clicks the left mouse button, add [`ManipulatorActivationFilter`](../ScriptReference/UIElements.ManipulatorActivationFilter.html) to the `activators` list with the `button` field set to `MouseButton.LeftMouse`.
  * Use the [`target`](../ScriptReference/UIElements.Manipulator-target.html) property to access the element that the manipulator is attached to.
  * Override the [`RegisterCallbacksOnTarget`](../ScriptReference/UIElements.Manipulator.RegisterCallbacksOnTarget.html) and [`UnregisterCallbacksFromTarget`](../ScriptReference/UIElements.Manipulator.UnregisterCallbacksFromTarget.html) methods to register and unregister the event callbacks.

### Create an ExampleDragger manipulator

The following example creates a manipulator that moves an element when you
click and drag it:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class ExampleDragger : PointerManipulator
    {
        private Vector3 m_Start;
        protected bool m_Active;
        private int m_PointerId;
        private Vector2 m_StartSize;
    
        public ExampleDragger()
        {
            m_PointerId = -1;
            activators.Add(new ManipulatorActivationFilter { button = MouseButton.LeftMouse });
            m_Active = false;
        }
    
        protected override void RegisterCallbacksOnTarget()
        {
            target.RegisterCallback<PointerDownEvent>(OnPointerDown);
            target.RegisterCallback<PointerMoveEvent>(OnPointerMove);
            target.RegisterCallback<PointerUpEvent>(OnPointerUp);
        }
    
        protected override void UnregisterCallbacksFromTarget()
        {
            target.UnregisterCallback<PointerDownEvent>(OnPointerDown);
            target.UnregisterCallback<PointerMoveEvent>(OnPointerMove);
            target.UnregisterCallback<PointerUpEvent>(OnPointerUp);
        }
    
        protected void OnPointerDown(PointerDownEvent e)
        {
            if (m_Active)
            {
                e.StopImmediatePropagation();
                return;
            }
    
            if (CanStartManipulation(e))
            {
                m_Start = e.localPosition;
                m_PointerId = e.pointerId;
    
                m_Active = true;
                target.CapturePointer(m_PointerId);
                e.StopPropagation();
            }
        }
    
        protected void OnPointerMove(PointerMoveEvent e)
        {
            if (!m_Active || !target.HasPointerCapture(m_PointerId))
                return;
    
            Vector2 diff = e.localPosition - m_Start;
    
            target.style.top = target.layout.y + diff.y;
            target.style.left = target.layout.x + diff.x;
    
            e.StopPropagation();
        }
    
        protected void OnPointerUp(PointerUpEvent e)
        {
            if (!m_Active || !target.HasPointerCapture(m_PointerId) || !CanStopManipulation(e))
                return;
    
            m_Active = false;
            target.ReleaseMouse();
            e.StopPropagation();
        }
    }
    

### Create an ExampleResizer manipulator

The following example creates a manipulator that resizes an element when you
drag it:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class ExampleResizer : PointerManipulator
    {
        private Vector3 m_Start;
        protected bool m_Active;
        private int m_PointerId;
        private Vector2 m_StartSize;
        public ExampleResizer()
        {
            m_PointerId = -1;
            activators.Add(new ManipulatorActivationFilter { button = MouseButton.LeftMouse });
            m_Active = false;
        }
    
        protected override void RegisterCallbacksOnTarget()
        {
            target.RegisterCallback<PointerDownEvent>(OnPointerDown);
            target.RegisterCallback<PointerMoveEvent>(OnPointerMove);
            target.RegisterCallback<PointerUpEvent>(OnPointerUp);
        }
    
        protected override void UnregisterCallbacksFromTarget()
        {
            target.UnregisterCallback<PointerDownEvent>(OnPointerDown);
            target.UnregisterCallback<PointerMoveEvent>(OnPointerMove);
            target.UnregisterCallback<PointerUpEvent>(OnPointerUp);
        }
    
        protected void OnPointerDown(PointerDownEvent e)
        {
            if (m_Active)
            {
                e.StopImmediatePropagation();
                return;
            }
    
            if (CanStartManipulation(e))
            {
                m_Start = e.localPosition;
                m_StartSize = target.layout.size;
                m_PointerId = e.pointerId;
                m_Active = true;
                target.CapturePointer(m_PointerId);
                e.StopPropagation();
            }
        }
    
        protected void OnPointerMove(PointerMoveEvent e)
        {
            if (!m_Active || !target.HasPointerCapture(m_PointerId))
                return;
    
            Vector2 diff = e.localPosition - m_Start;
    
            target.style.height = m_StartSize.y + diff.y;
            target.style.width = m_StartSize.x + diff.x;
    
            e.StopPropagation();
        }
    
        protected void OnPointerUp(PointerUpEvent e)
        {
            if (!m_Active || !target.HasPointerCapture(m_PointerId) || !CanStopManipulation(e))
                return;
    
            m_Active = false;
            target.ReleasePointer(m_PointerId);
            m_PointerId = -1;
            e.StopPropagation();
        }
    }
    

### Add or remove a manipulator

To add a manipulator to an element, use the
[`AddManipulator`](../ScriptReference/UIElements.VisualElementExtensions.AddManipulator.html)
method. To remove a manipulator from an element, use the
[`RemoveManipulator`](../ScriptReference/UIElements.VisualElementExtensions.AddManipulator.html)
method.

The following example adds and removes the `ExampleDragger` to a
`VisualElement`:

    
    
    // Create a VisualElement.
    var myElement = new VisualElement();
    var dragger = new ExampleDragger();
    
    // Add manipulators to the VisualElement.
    myElement.AddManipulator(dragger);
    
    // Remove manipulators from the VisualElement.
    myElement.RemoveManipulator(dragger);
    

The following example adds the `ExampleResizer` to a `VisualElement`:

    
    
    var box = new VisualElement()
    {
        style =
        {
            left = 100,
            top = 100,
            width = 100,
            height = 100,
            backgroundColor = Color.red
        },
        pickingMode = PickingMode.Position,
    };
    
    box.AddManipulator(new ExampleResizer());
    

## Additional resources

  * [Handle events](UIE-Events-Handling.html)
  * [Create a drag-and-drop UI inside a custom Editor window](UIE-create-drag-and-drop-ui.html)
  * [Create a drag-and-drop UI to drag between Editor windows](UIE-drag-across-windows.html)

[](UIE-events-handling-custom-control.html)

Respond to events with custom controls

[](UIE-Events-Synthesizing.html)

Synthesize and send events

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

