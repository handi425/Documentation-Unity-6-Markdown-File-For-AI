[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Input-Events.html)
  * [中文](/cn/current/Manual/UIE-Input-Events.html)
  * [日本語](/ja/current/Manual/UIE-Input-Events.html)
  * [한국어](/kr/current/Manual/UIE-Input-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Input-Events.html)
  * [中文](/cn/current/Manual/UIE-Input-Events.html)
  * [日本語](/ja/current/Manual/UIE-Input-Events.html)
  * [한국어](/kr/current/Manual/UIE-Input-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Input events

[](UIE-Focus-Events.html)

Focus events

[](UIE-Keyboard-Events.html)

Keyboard events

# Input events

The `InputEvent` is sent when the user submits text into a text field. This
event updates when there is a change in focus, such as a
`PointerCaptureOutEvent` that on a touch screen.

For default keyboard inputs, the `inputEvent` fires for each keystroke.
`InputEvent` doesn’t fire when the TextField populates from an indirect
source, such as an automated script.

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[InputEvent](../ScriptReference/UIElements.InputEvent.html) | Sent when data is input to a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement), typically a control. |  |  |   
  
## Unique properties

**`previousData`** : The former data.

**`newData`** : The new data.

## Event list

### InputEvent

Event sent when data is input to visual elements that implement
[TextInputBaseField](../ScriptReference/UIElements.TextInputBaseField_1.html).
This event differs from `ChangeEvent` in that it’s sent for every input event
in the control, even if the value of the control hasn’t changed.

**`target`** : The element where the input occurred.

[](UIE-Focus-Events.html)

Focus events

[](UIE-Keyboard-Events.html)

Keyboard events

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

