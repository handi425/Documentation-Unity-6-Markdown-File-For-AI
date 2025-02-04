[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Keyboard-Events.html)
  * [中文](/cn/current/Manual/UIE-Keyboard-Events.html)
  * [日本語](/ja/current/Manual/UIE-Keyboard-Events.html)
  * [한국어](/kr/current/Manual/UIE-Keyboard-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Keyboard-Events.html)
  * [中文](/cn/current/Manual/UIE-Keyboard-Events.html)
  * [日本語](/ja/current/Manual/UIE-Keyboard-Events.html)
  * [한국어](/kr/current/Manual/UIE-Keyboard-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Keyboard events

[](UIE-Input-Events.html)

Input events

[](UIE-Mouse-Events.html)

Mouse events

# Keyboard events

Keyboard events occur when you press or release keys on the keyboard. Each
event includes information about the
[modifier](../ScriptReference/UIElements.KeyboardEventBase_1-modifiers.html),
[text
character](../ScriptReference/UIElements.KeyboardEventBase_1-character.html),
and related [key
code](../ScriptReference/UIElements.KeyboardEventBase_1-keyCode.html) for the
event.

Many standard controls use the `KeyDownEvent` to encode shortcuts or
accessibility behaviors. The following examples all use keyboard events:

  * The `Toggle` and `Button` classes listen for `Enter` and `Spacebar` key presses as replacement actions for mouse clicks.
  * The **ScrollView** A UI Control which displays a large set of Controls in a viewable area that you can see by using a scrollbar. [More info](UIE-uxml-element-ScrollView.html)  
See in [Glossary](Glossary.html#ScrollView) and Slider controls use
directional arrow key presses to modulate their values.

  * The **TextField control** A TextField control displays a non-interactive piece of text to the user, such as a caption, label for other GUI controls, or instruction. [More info](gui-Controls.html)  
See in [Glossary](Glossary.html#TextFieldcontrol) looks at both the `keyCode`
property and the character property to execute special actions or to accept
text.

The base class for all keyboard events is
[KeyboardEventBase](../ScriptReference/UIElements.KeyboardEventBase_1.html).

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[KeyDownEvent](../ScriptReference/UIElements.KeyDownEvent.html) | Sent when the user presses a key on the keyboard. | Yes | Yes | Yes  
[KeyUpEvent](../ScriptReference/UIElements.KeyUpEvent.html) | Sent when the user releases a key on the keyboard. | Yes | Yes | Yes  
  
## Unique properties

**`keyCode`** : The `keyCode` property returns a character key that
corresponds directly to a physical key on an input device, such as a keyboard
or joystick. The difference between the `character` property and the `keyCode`
property is that `keyCode` represents a physical key, while `character`
represents the entry of a specific character. For example, both `a` and `A`
return `keyCode=KeyCode.A` during a `keyDownEvent`.

**`character`** : The `character` property returns a character code during a
`keyDownEvent`.

**`modifiers`** : The `modifiers` property returns which modifier key is held
down. Some examples of modifier keys are the `Shift`, `Ctrl`, or `Alt` keys.

For more information, see the [Modifier keys
section](https://developer.mozilla.org/en-
US/docs/Web/API/KeyboardEvent/key/Key_Values#modifier_keys) of the MDN
documentation.

## Event List

The following list provides the name, description, and target of each event in
the event family.

By default, a **visual element** A node of a visual tree that instantiates or
derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) doesn’t receive keyboard
events. Only elements that are focusable and currently in focus are targeted
for keyboard events. This is because keyboard events trickle down and bubble
up, allowing parent elements to receive them as well.

In summary, to begin receiving keyboard events, you must mark the element as
`focusable=true` and explicitly give it focus using `element.Focus()`. This
ensures that the element is eligible to receive keyboard events.

### KeyDownEvent

A [KeyDownEvent](../ScriptReference/UIElements.KeyDownEvent.html) is sent each
time you press a key on the keyboard. The key pressed contains the `keyCode`
property for that event. If that key press has text input associated with it,
additional events are sent for each character of text input. The `character`
property contains the character for those events.

When you press and release `a`, **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit sends the following events:

    
    
    KeyDownEvent { keyCode=KeyCode.A }
    KeyDownEvent { character=’a’ }
    KeyUpEvent { keyCode=KeyCode.A }
    
    

When you press and release `Ctrl+a`, UI Toolkit sends the following events:

    
    
    KeyDownEvent { keyCode=KeyCode.LeftControl, modifiers=EventModifiers.Control }
    KeyDownEvent { keyCode=KeyCode.A, modifiers=EventModifiers.Control }
    KeyUpEvent { keyCode=KeyCode.A, modifiers=EventModifiers.Control }
    KeyUpEvent { keyCode=KeyCode.LeftControl }
    
    

**`target`** : The visual element that has focus. If no element has focus, the
root visual element of the panel.

### KeyUpEvent

A [KeyUpEvent](../ScriptReference/UIElements.KeyUpEvent.html) is sent when you
release a key on the keyboard. The keyCode property for that event contains
the key being released. `KeyDownEvent` has additional events sent when a
keystroke has an associated text input.

When you press and release `a`, UI Toolkit sends the following events:

    
    
    KeyDownEvent { keyCode=KeyCode.A }
    KeyDownEvent { character=’a’ }
    KeyUpEvent { keyCode=KeyCode.A }
    

When you press and release `Ctrl+a`, UI Toolkit sends the following events:

    
    
    KeyDownEvent { keyCode=KeyCode.LeftControl, modifiers=EventModifiers.Control }
    KeyDownEvent { keyCode=KeyCode.A, modifiers=EventModifiers.Control }
    KeyUpEvent { keyCode=KeyCode.A, modifiers=EventModifiers.Control }
    KeyUpEvent { keyCode=KeyCode.LeftControl }
    
    

**`target`** : The visual element that has focus. If no element has focus, the
root visual element of the panel.

## Examples

The following code example prints a message to the console when you press a
key in a TextField. This code sample highlights the event firing of both
`KeyUpEvent` and `KeyDownEvent`.

  1. Create a Unity project with any template.

  2. In the SampleScene, select **GameObject** > **UI Toolkit** > **UI Document**.

  3. Create a C# script named `KeyboardEventTest.cs` with the following contents:
    
        using UnityEngine;
    using UnityEngine.UIElements;
    
    // Add KeyboardEventTest to a GameObject with a valid UIDocument.
    // When the user presses a key, it will print the keyboard event properties to the console.
    [RequireComponent(typeof(UIDocument))]
    public class KeyboardEventTest : MonoBehaviour
    {
        void OnEnable()
        {
            var root = GetComponent<UIDocument>().rootVisualElement;
            root.Add(new Label("Press any key to see the keyDown properties"));
            root.Add(new TextField());
            root.Q<TextField>().Focus();
            root.RegisterCallback<KeyDownEvent>(OnKeyDown, TrickleDown.TrickleDown);
            root.RegisterCallback<KeyUpEvent>(OnKeyUp, TrickleDown.TrickleDown);
        }
        void OnKeyDown(KeyDownEvent ev)
        {
            Debug.Log("KeyDown:" + ev.keyCode);
            Debug.Log("KeyDown:" + ev.character);
            Debug.Log("KeyDown:" + ev.modifiers);
        }
    
        void OnKeyUp(KeyUpEvent ev)
        {
            Debug.Log("KeyUp:" + ev.keyCode);
            Debug.Log("KeyUp:" + ev.character);
            Debug.Log("KeyUp:" + ev.modifiers);
        }
    }
    

  4. Select the UIDocument **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the Hierarchy window.

  5. Drag `KeyboardEventTest.cs` to **Add Component** in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

  6. Enter Play mode and type in the TextField.

## Additional resources

  * [UI Toolkit events](UIE-Events.html)
  * [UI Toolkit built-in controls reference](UIE-ElementRef.html#built-in-controls)
  * [UI Toolkit controls](UIE-Controls.html)

[](UIE-Input-Events.html)

Input events

[](UIE-Mouse-Events.html)

Mouse events

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

