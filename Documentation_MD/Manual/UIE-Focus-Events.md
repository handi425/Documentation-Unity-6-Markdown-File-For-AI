[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Focus-Events.html)
  * [中文](/cn/current/Manual/UIE-Focus-Events.html)
  * [日本語](/ja/current/Manual/UIE-Focus-Events.html)
  * [한국어](/kr/current/Manual/UIE-Focus-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Focus-Events.html)
  * [中文](/cn/current/Manual/UIE-Focus-Events.html)
  * [日本語](/ja/current/Manual/UIE-Focus-Events.html)
  * [한국어](/kr/current/Manual/UIE-Focus-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Focus events

[](UIE-Layout-Events.html)

Layout events

[](UIE-Input-Events.html)

Input events

# Focus events

Focus events occur when an element gains or loses focus.

Focus events are useful when you need to change focus to and away from
**visual elements** A node of a visual tree that instantiates or derives from
the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html)
class. You can style the look, define the behaviour, and display it on screen
as part of the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement). Controls often use focus
events to change their contents, depending on the focus state. For example, a
text field can display placeholder text while it isn’t in focus, or it can
react to the `FocusInEvent` to clear the placeholder text.

Focus can change on a visual element from user interactions, such as tabbing
or clicking, or using C# **scripts** A piece of code that allows you to create
your own Components, trigger game events, modify Component properties over
time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts) with `element.Focus()`.

Focus events separate into two distinct types:

  * `FocusOutEvent` and `FocusInEvent` are sent along the propagation path just before a focus change occurs.
  * `FocusEvent` and `BlurEvent` are sent to the event target, immediately after the change in focus.

The base class for all focus events is
[FocusEventBase](../ScriptReference/UIElements.FocusEventBase_1.html).

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[FocusOutEvent](../ScriptReference/UIElements.FocusOutEvent.html) | Sent before an element loses focus. | ✔ | ✔ |   
[FocusInEvent](../ScriptReference/UIElements.FocusInEvent.html) | Sent before an element gains focus. | ✔ | ✔ |   
[BlurEvent](../ScriptReference/UIElements.BlurEvent.html) | Sent after an element has lost focus. | ✔ |  |   
[FocusEvent](../ScriptReference/UIElements.FocusEvent.html) | Sent after an element has gained focus. | ✔ |  |   
  
## Unique properties

The following section explains relevant properties unique to focus events.
This isn’t a complete list of all properties within the focus event family.
For a full list, see the
[FocusEventBase](../ScriptReference/UIElements.FocusEventBase_1.html) in the
API documentation.

**`relatedTarget`** : Contains the visual element that’s the secondary target
of an event. For `FocusOut` and `Blur` events, it contains the element that
gains focus. For `FocusIn` and `Focus` events, it contains the element that
loses focus.

**Event** | **target** | **relatedTarget**  
---|---|---  
Blur | The element that loses focus. | The element that gains focus.  
Focus | The element that gains focus. | The element that loses focus.  
focusIn | The element that gains focus. | The element that loses focus.  
focusOut | The element that loses focus. | The element that gains focus.  
  
## Event list

### FocusOutEvent

The `FocusOutEvent` is sent when an element is about to lose focus.

**`target`** : The element that will lose focus.

**`relatedTarget`** : The element that will gain focus.

### FocusInEvent

The `FocusInEvent` is sent when an element is about to gain focus.

**`target`** : The element that will gain focus.

**`relatedTarget`** : The element that will lose focus.

### BlurEvent

The `BlurEvent` is sent after an element lost focus.

**`target`** : The element that lost focus.

**`relatedTarget`** : The element that gained focus.

### FocusEvent

The `FocusEvent` is sent after an element gained focus.

**`target`** : The element that gained focus.

**`relatedTarget`** : The element that lost focus.

## Examples

The following example shows how to use placeholder text in a TextField.

After you create the elements through UXML, the script assigns a placeholder
text to the TextField. When the TextField is in focus, `FocusInEvent` fires
and clears the placeholder text. `FocusOutEvent` toggles the placeholder mode
based on the TextField contents.

To see the example in action, do the following:

  1. Create a new C# script called PlaceHolderExample.
  2. Copy the example code into the C# script.
  3. Under **Window > UI Toolkit > PlaceHolderExample**, open the newly created Editor window.

    
    
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class PlaceHolderExample : EditorWindow
    {
        [MenuItem("Window/UI Toolkit/PlaceHolderExample")]
        public static void ShowExample()
        {
            PlaceHolderExample wnd = GetWindow<PlaceHolderExample>();
            wnd.titleContent = new GUIContent("PlaceHolderExample");
        }
    
        private bool placeHolderMode = true;
        private const string placeHolderText = "Write here";
    
        public void CreateGUI()
        {
            TextField textField = new TextField();
            textField.value = placeHolderText;
            rootVisualElement.Add(textField);
    
            textField.RegisterCallback<FocusInEvent>(OnFocusInTextField);
            textField.RegisterCallback<FocusOutEvent>(OnFocusOutTextField);
        }
    
        private void OnFocusInTextField(FocusInEvent evt)
        {
            // If the text field just received focus and the user might want to write
            // or edit the text inside, the placeholder text should be cleared (if active)
            if (placeHolderMode)
            {
                var textField = evt.target as TextField;
                if (textField != null)
                {
                    textField.value = "";
                }
            }
        }        
    
        private void OnFocusOutTextField(FocusOutEvent evt)
        {
            // If the text field is empty after the user is done editing and the
            // element lost focus, write placeholder text into the text field
            var textField = evt.target as TextField;
            if (textField != null)
            {
                placeHolderMode = string.IsNullOrEmpty(textField.value);
                if (placeHolderMode)
                    textField.value = placeHolderText;
            }    
        }
    }
    

[](UIE-Layout-Events.html)

Layout events

[](UIE-Input-Events.html)

Input events

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

