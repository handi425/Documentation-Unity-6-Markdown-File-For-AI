[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Capture-Events.html)
  * [中文](/cn/current/Manual/UIE-Capture-Events.html)
  * [日本語](/ja/current/Manual/UIE-Capture-Events.html)
  * [한국어](/kr/current/Manual/UIE-Capture-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Capture-Events.html)
  * [中文](/cn/current/Manual/UIE-Capture-Events.html)
  * [日本語](/ja/current/Manual/UIE-Capture-Events.html)
  * [한국어](/kr/current/Manual/UIE-Capture-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Capture events

[](UIE-Events-Reference.html)

Event reference

[](UIE-Change-Events.html)

Change events

# Capture events

Capture events inform you of the changes in the mouse capture state.
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit has two types of capture events:

  * Mouse capture events
  * Pointer capture events

When an element captures the mouse or pointer, it’s the only element that
receives events from the pointing device until the device releases or loses
the capture.

For example, if you click in a text box, the text box captures the mouse. The
mouse can still move around the screen, but it won’t trigger events outside of
the text box. As long as the text box has your mouse captured, it won’t
trigger other events. When the user presses a button on the mouse outside of
the text box, the box releases its mouse capture.

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[MouseCaptureEvent](../ScriptReference/UIElements.MouseCaptureEvent.html) | Sent when an element takes the mouse capture. | ✔ | ✔ |   
[MouseCaptureOutEvent](../ScriptReference/UIElements.MouseCaptureOutEvent.html) | Sent when an element releases or otherwise loses the mouse capture. | ✔ | ✔ |   
[PointerCaptureEvent](../ScriptReference/UIElements.PointerCaptureEvent.html) | Sent when an element captures a pointer. | ✔ | ✔ |   
[PointerCaptureOutEvent](../ScriptReference/UIElements.PointerCaptureOutEvent.html) | Sent when an element releases a pointer. | ✔ | ✔ |   
  
## Behavior

### Mouse capture

Mouse capture events refer to events on a physical mouse, or a virtual mouse
emulating a physical mouse. Capturing a mouse will also result in a
`PointerCaptureEvent` for the mouse pointer.

When an element releases a mouse capture, the corresponding
`MouseCaptureOutEvent` triggers, with the target being the element that
requested the release of the capture.

There can never be two elements that capture the mouse at the same time. If
another **visual element** A node of a visual tree that instantiates or
derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) triggers a `MouseCaptureEvent`,
the element that sent the original `MouseCaptureEvent` loses the capture. This
also triggers a `MouseCaptureOutEvent` on the original element.

### Pointer capture

Pointer events precede mouse events in UI Toolkit. If the pointer type is a
mouse, capturing it will also trigger the corresponding mouse capture events.
Capturing the pointer will also capture the mouse.

## Event list

### MouseCaptureEvent

A `MouseCaptureEvent` event is sent when an element takes the mouse capture.

**`target`** : The element that takes the capture.

### MouseCaptureOutEvent

A `MouseCaptureOutEvent` event is sent when an element releases, or loses the
mouse capture.

**`target`** : The element that loses the capture.

### PointerCaptureEvent

A `PointerCaptureEvent` event is sent when an element takes the pointer
capture.

**`target`** : The element that takes the capture.

### PointerCaptureOutEvent

A `PointerCaptureOutEvent` event is sent when an element releases, or loses
the pointer capture.

**`target`** : The element that loses the capture.

## Examples

The following example demonstrates the behavior of the capture events, and
capturing and releasing pointers.

To see the example in action, do the following:

  1. Under **Assets > Scripts > Editor**, create a new C# file called CaptureEventsTestWindow.cs
  2. Copy the example into the C# script.
  3. From the Editor Toolbar, select **Window > UI Toolkit > Capture Events Test Window**.
  4. Click on the various labels in the dialog window, and watch the console for the output.

    
    
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class CaptureEventsTestWindow : EditorWindow
    {
        [MenuItem("Window/UI Toolkit/Capture Events Test Window")]
        public static void ShowExample()
        {
            var wnd = GetWindow<CaptureEventsTestWindow>();
            wnd.titleContent = new GUIContent("Capture Events Test Window");
        }
    
        private bool m_IsCapturing = false;
    
        public void CreateGUI()
        {
            // Add a few clickable labels that print a message to the console when clicked
            for (int i = 0; i < 4; i++)
            {
                Label clickableLabel = new Label($"Label {i} - Click Me!");
                clickableLabel.RegisterCallback<MouseDownEvent>((evt) => { Debug.Log($"Clicked on label '{(evt.target as Label).text}'"); });
                rootVisualElement.Add(clickableLabel);
            }
    
            // Now add a label that captures the pointer
            Label capturingLabel = new Label("Click here to capture mouse");
            capturingLabel.RegisterCallback<MouseDownEvent>((evt) =>
            {
                if (!m_IsCapturing)
                {
                    capturingLabel.text = "Click here to release mouse";
                    MouseCaptureController.CaptureMouse(capturingLabel);
                    m_IsCapturing = true;
                }
                else
                {
                    capturingLabel.text = "Click here to capture mouse";
                    MouseCaptureController.ReleaseMouse(capturingLabel);
                    m_IsCapturing = false;
                }
            });
            rootVisualElement.Add(capturingLabel);
    
            // Register callbacks to print a message when the mouse is captured or released
            rootVisualElement.RegisterCallback<MouseCaptureEvent>((evt) =>
            {
                Debug.Log("Mouse captured");
            });
            rootVisualElement.RegisterCallback<MouseCaptureOutEvent>((evt) =>
            {
                Debug.Log("Mouse captured released");
            });
        }
    }
    

[](UIE-Events-Reference.html)

Event reference

[](UIE-Change-Events.html)

Change events

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

