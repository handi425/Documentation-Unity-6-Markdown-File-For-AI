[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Mouse-Events.html)
  * [中文](/cn/current/Manual/UIE-Mouse-Events.html)
  * [日本語](/ja/current/Manual/UIE-Mouse-Events.html)
  * [한국어](/kr/current/Manual/UIE-Mouse-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Mouse-Events.html)
  * [中文](/cn/current/Manual/UIE-Mouse-Events.html)
  * [日本語](/ja/current/Manual/UIE-Mouse-Events.html)
  * [한국어](/kr/current/Manual/UIE-Mouse-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Mouse events

[](UIE-Keyboard-Events.html)

Keyboard events

[](UIE-Navigation-Events.html)

Navigation events

# Mouse events

Mouse events occur when you interact with the **UI**(User Interface) Allows a
user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) using a mouse. Touch, pens, or other
pointing devices generate other events, not mouse events. In the Mouse event
APIs and in this documentation, the term “mouse” refers only to a physical
mouse or a virtual mouse that emulates a physical mouse.

Mouse events are always preceded by the corresponding `PointerEvent`.

The base class for all mouse events is
[MouseEventBase](../ScriptReference/UIElements.MouseEventBase_1.html).

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[MouseDownEvent](../ScriptReference/UIElements.MouseDownEvent.html) | Sent when the user presses a mouse button. | Yes | Yes | Yes  
[MouseUpEvent](../ScriptReference/UIElements.MouseUpEvent.html) | Sent when the user releases a mouse button. | Yes | Yes | Yes  
[MouseMoveEvent](../ScriptReference/UIElements.MouseMoveEvent.html) | Sent when the user moves the mouse. | Yes | Yes | Yes  
[WheelEvent](../ScriptReference/UIElements.WheelEvent.html) | Sent when the user activates the mouse wheel. | Yes | Yes | Yes  
[MouseEnterWindowEvent](../ScriptReference/UIElements.MouseEnterWindowEvent.html) | Sent when the mouse enters a window. |  |  | Yes  
[MouseLeaveWindowEvent](../ScriptReference/UIElements.MouseLeaveWindowEvent.html) | Sent when the mouse leaves a window. |  |  | Yes  
[MouseEnterEvent](../ScriptReference/UIElements.MouseEnterEvent.html) | Sent when the mouse enters an element or one of its descendants. | Yes |  | Yes  
[MouseLeaveEvent](../ScriptReference/UIElements.MouseLeaveEvent.html) | Sent when the mouse leaves an element or one of its descendants. | Yes |  | Yes  
[MouseOverEvent](../ScriptReference/UIElements.MouseOverEvent.html) | Sent when the mouse enters an element. | Yes | Yes | Yes  
[MouseOutEvent](../ScriptReference/UIElements.MouseOutEvent.html) | Sent when the mouse leaves an element. | Yes | Yes | Yes  
[ContextClickEvent](../ScriptReference/UIElements.ContextClickEvent.html) (obsolete) | Sent when the user presses and releases the third mouse button. Exists for backwards compatibility with IMGUI. | Yes | Yes | Yes  
  
## Unique Properties

**`button`** : The `button` property returns an integer that identifies the
mouse button pressed to trigger an event. The following table lists the
integer and associated mouse button:

**Integer** | **Button**  
---|---  
0 | Left button  
1 | Right button  
2 | Middle button  
  
**`pressedButtons`** : The `pressedButton` property returns an integer that
identifies which combination of mouse buttons are currently pressed.

The number is the sum of the individual buttons’ integer value (see table
below). For example, holding the right mouse button and the middle mouse
button pressed at the same time will result in pressedButton having a value of
6.

**Integer** | **Button**  
---|---  
1 | Left button  
2 | Right button  
4 | Middle button  
  
**`modifiers`** : The `modifiers` property returns the modifier key pressed
during a keyboard event. Some examples of modifiers are the `Shift`, `Ctrl`,
or `Alt` keys.

For more information, see the [Modifier keys
section](https://developer.mozilla.org/en-
US/docs/Web/API/KeyboardEvent/key/Key_Values#modifier_keys) of the MDN
documentation.

**`mousePosition`** : The `mousePosition` property returns the mouse position
within the panel, also known as the screen coordinate system. For more
information on panel coordinates, see the [Visual Tree page](UIE-
VisualTree.html).

**`localMousePosition`** : The `localMousePosition` property returns the
coordinates relative to the target **visual element** A node of a visual tree
that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement).

**`mouseDelta`** : The difference between the pointer’s position during the
previous mouse event and its position during the current mouse event.

## Event list

The following list provides the name, description, and target of each event in
the event family. For more information on the event, see the [UI Toolkit
API](../ScriptReference/UIElements.MouseEventBase_1.html).

### MouseDownEvent

A [MouseDownEvent](../ScriptReference/UIElements.MouseDownEvent.html) is sent
when the mouse button is pressed while the cursor is inside a visual element.

**`target`** : The visual element that receives the mouse capture. Otherwise,
it’s the topmost selectable element under the cursor.

### MouseUpEvent

The [MouseUpEvent](../ScriptReference/UIElements.MouseUpEvent.html) triggers
when a mouse button releases while the cursor is within a visual element.
`MouseUpEvent` is complimentary to `MouseDownEvent`.

**`target`** : The visual element that receives the mouse capture. Otherwise,
it’s the topmost selectable element under the cursor.

### MouseMoveEvent

The [MouseMoveEvent](../ScriptReference/UIElements.MouseMoveEvent.html) is
sent when the cursor hotspot is moved within a visual element.

**`target`** : The visual element that receives the mouse capture. Otherwise,
it’s the topmost selectable element under the cursor.

### WheelEvent

The [WheelEvent](../ScriptReference/UIElements.WheelEvent.html) is sent when
the mouse wheel is pressed.

**`target`** : The visual element that receives the mouse capture. Otherwise,
it’s the topmost selectable element under the cursor.

### MouseEnterWindowEvent

A
[MouseEnterWindowEvent](../ScriptReference/UIElements.MouseEnterWindowEvent.html)
triggers when the cursor is moved into an Editor window. Runtime panels don’t
receive this event when you enter the Game view window.

**`target`** : The visual element that receives the mouse capture. Otherwise,
it’s the topmost selectable element under the cursor.

### MouseLeaveWindowEvent

[MouseLeaveWindowEvent](../ScriptReference/UIElements.MouseLeaveWindowEvent.html)
fires when the cursor exits the space of an Editor window. The
`MouseLeaveWindowEvent` is the counterpoint to `MouseEnterWindowEvent`.

**`target`** : The visual element that receives the mouse capture. Otherwise
it returns null, as the cursor isn’t over an element.

### MouseEnterEvent

The [MouseEnterEvent](../ScriptReference/UIElements.MouseEnterEvent.html) is
sent when the cursor is moved into a visual element, or one of its
descendants.

**`target`** : The visual element under the mouse cursor, or one of its
descendants.

### MouseLeaveEvent

[MouseLeaveEvent](../ScriptReference/UIElements.MouseLeaveEvent.html) triggers
when the cursor moves outside of a visual element. This event differs from
`MouseOutEvent` as this event is sent to each element the mouse exits. This
event doesn’t propagate.

**`target`** : The visual element (or one of its descendants) that the mouse
cursor exits.

### MouseOverEvent

The [MouseOverEvent](../ScriptReference/UIElements.MouseOverEvent.html) is
sent when the cursor enters an element. This differs from `MouseEnterEvent`,
because this event is only sent to the entered element.

**`target`** : The visual element that’s under the mouse cursor.

### MouseOutEvent

The [MouseOutEvent](../ScriptReference/UIElements.MouseOutEvent.html) triggers
when a pointing device moves the cursor outside the boundary of a visual
element.

`MouseOutEvent` is different from `MouseLeaveEvent` in that `MouseOutEvent` is
sent when leaving the visual element to any other element, while
`MouseLeaveEvent` isn’t sent when transitioning from a visual element to
descendant elements.

**`target`** : The visual element that the mouse cursor exited.

### ContextualMenuPopulateEvent

Event sent by the `ContextualMenuManager` when the contextual menu needs to be
populated with menu items.

**`target`** : The visual element for which the contextual menu is being
built.

### ContextClickEvent (obsolete)

Event sent when the user presses and releases the third mouse button. This
event only exists for backward compatibility with IMGUI.

## Examples

### Editor window example

The following code sample creates an Editor window with three buttons that
prints messages to the console when the mouse moves over an element, or
buttons are pressed on the mouse.

This code sample highlights the event firing of both `MouseDownEvent` and
`MouseEnterEvent`, and how to use the event parameters.

To see the example in action, do the following:

  1. Create a new C# script called `MouseEventTestWindow.cs`.
  2. Copy the example into the C# script.
  3. Open the example under **Window > UI Toolkit > Mouse Event Test Window**.

    
    
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    // Open this in the Editor via the menu Window > UI ToolKit > Mouse Event Test Window
    public class MouseEventTestWindow : EditorWindow
    {
        [MenuItem("Window/UI Toolkit/Mouse Event Test Window")]
        public static void ShowExample()
        {
            MouseEventTestWindow wnd = GetWindow<MouseEventTestWindow>();
            wnd.titleContent = new GUIContent("Mouse Event Test Window");
        }
        public void CreateGUI()
        {
            // Add a few buttons
            for (int i = 0; i < 3; i++)
            {
                Button newElement = new Button { name = $"Button {i}", text = $"Button {i}" };
                newElement.style.flexGrow = 1;
                rootVisualElement.Add(newElement);
            }
            // Register mouse event callbacks
            rootVisualElement.RegisterCallback<MouseDownEvent>(OnMouseDown, TrickleDown.TrickleDown);
            rootVisualElement.RegisterCallback<MouseEnterEvent>(OnMouseEnter, TrickleDown.TrickleDown);
        }
    
        private void OnMouseDown(MouseDownEvent evt)
        {
            bool leftMouseButtonPressed = 0 != (evt.pressedButtons & (1 << (int)MouseButton.LeftMouse));
            bool rightMouseButtonPressed = 0 != (evt.pressedButtons & (1 << (int)MouseButton.RightMouse));
            bool middleMouseButtonPressed = 0 != (evt.pressedButtons & (1 << (int)MouseButton.MiddleMouse));
            Debug.Log($"Mouse Down event. Triggered by {(MouseButton)evt.button}.");
            Debug.Log($"Pressed buttons: Left button: {leftMouseButtonPressed} Right button: {rightMouseButtonPressed} Middle button: {middleMouseButtonPressed}");
        }
    
        private void OnMouseEnter(MouseEnterEvent evt)
        {
            VisualElement targetElement = (VisualElement)evt.target;
            Debug.Log($"Mouse is now over element '{targetElement.name}'");
        }
    }
    

### Runtime example

The following code sample prints messages to the console when any mouse
buttons are pressed, showing which button triggered the event, and which
buttons are currently pressed.

This code sample highlights registering a callback to the `MouseDownEvent` and
how to use the event parameters. To see the example in action, do the
following:

  1. Create a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with a valid UIDocument.

  2. Under **Assets > Scripts**, create a C# script called MouseEventTestRuntime.
  3. Copy the example into the C# script.
  4. Attach the MouseEventTestRuntime script to the GameObject with the UIDocument.
  5. Enter Play mode.
  6. Move the mouse over the game view and press or hold buttons on the mouse.

    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class MouseEventTestRuntime : MonoBehaviour
    {
        void Start()
        {
            var root = GetComponent<UIDocument>().rootVisualElement;
            var newLabel = new Label("Move the mouse or press buttons to see the log output");
            newLabel.style.flexGrow = 1;
            root.Add(newLabel);
            root.RegisterCallback<MouseDownEvent>(OnMouseDown, TrickleDown.TrickleDown);
        }
    
        private void OnMouseDown(MouseDownEvent evt)
        {
            bool leftMouseButtonPressed = 0 != (evt.pressedButtons & (1 << (int)MouseButton.LeftMouse));
            bool rightMouseButtonPressed = 0 != (evt.pressedButtons & (1 << (int)MouseButton.RightMouse));
            bool middleMouseButtonPressed = 0 != (evt.pressedButtons & (1 << (int)MouseButton.MiddleMouse));
    
            VisualElement targetElement = (VisualElement)evt.target;
            Debug.Log($"Mouse Down event. Triggered by {(MouseButton)evt.button} over element '{targetElement.name}'");
            Debug.Log($"Pressed buttons: Left button: {leftMouseButtonPressed} Right button: {rightMouseButtonPressed} Middle button: {middleMouseButtonPressed}");
        }
    }
    
    

[](UIE-Keyboard-Events.html)

Keyboard events

[](UIE-Navigation-Events.html)

Navigation events

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

