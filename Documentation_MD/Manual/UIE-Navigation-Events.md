[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Navigation-Events.html)
  * [中文](/cn/current/Manual/UIE-Navigation-Events.html)
  * [日本語](/ja/current/Manual/UIE-Navigation-Events.html)
  * [한국어](/kr/current/Manual/UIE-Navigation-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Navigation-Events.html)
  * [中文](/cn/current/Manual/UIE-Navigation-Events.html)
  * [日本語](/ja/current/Manual/UIE-Navigation-Events.html)
  * [한국어](/kr/current/Manual/UIE-Navigation-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Navigation events

[](UIE-Mouse-Events.html)

Mouse events

[](UIE-Panel-Events.html)

Panel events

# Navigation events

Navigation events occur at runtime when the user presses the D-pad, moves a
joystick, or presses the `Escape`, `Enter` or arrow keys. They’re an indicator
that the user is trying to navigate the **UI**(User Interface) Allows a user
to interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI), but they’re not limited to a specific
input device, such as a keyboard. The difference from a [Focus](UIE-Focus-
Events.html) event is that the navigation event doesn’t require the focus to
move to a new UI element.

The base class for all navigation events is
[NavigationEventBase](../ScriptReference/UIElements.NavigationEventBase_1.html).

All navigation events trickle down, bubble up, and are cancellable, but it’s
recommended to listen to these events during the bubble-up propagation phase.
This is because navigation events are triggered by input events that might
also be used to interact with individual controls. For example, a button will
react to a press of the `Enter` key with a button click, and it will cancel
the `NavigationSubmitEvent`. Listening to these events during the bubble-up
phase makes sure that they’re navigation events.

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[NavigationMoveEvent](../ScriptReference/UIElements.NavigationMoveEvent.html) | Sent when user makes a move input. | ✔ | ✔ | ✔  
[NavigationCancelEvent](../ScriptReference/UIElements.NavigationCancelEvent.html) | Sent when the user makes a cancel input. | ✔ | ✔ | ✔  
[NavigationSubmitEvent](../ScriptReference/UIElements.NavigationSubmitEvent.html) | Sent when the user makes a submit input. | ✔ | ✔ | ✔  
  
## Event list

### NavigationMoveEvent

The `NavigationMoveEvent` is sent when the user presses the D-pad, moves a
joystick, or presses the arrow keys.

Some controls will use the arrow keys for their own functionality. For
example, the [ListView](UIE-uxml-element-ListView.html) allows the user to
select items using the up and down arrow keys. In this case, the control will
cancel the `NavigationMoveEvent` and the event won’t enter the bubble-up
phase.

**`direction`** : The direction of the navigation. (`None`, `Left`, `Up`,
`Right`, `Down`)

**`move`** : The move vector. If the event was triggered by an analog axis
input, like a joystick, this property gives access to the directional vector.

### NavigationCancelEvent

The `NavigationCancelEvent` is triggered when the user cancels the current
navigation action, such as by pressing the `Escape`` key on the keyboard. It’s
important to note that this event doesn’t affect the currently focused
element, which means that the UI element that had focus before the
cancellation remains selected.

### NavigationSubmitEvent

The `NavigationSubmitEvent` is triggered when the user presses the submit
button, such as by pressing the `Enter`` key on the keyboard.

If a control handles the event itself, it cancels the event, preventing it
from entering the bubble-up phase. For example, a [TextField](UIE-uxml-
element-TextField.html) that has the focus will stop the
`NavigationSubmitEvent` from bubbling up. On the other hand, a focusable
[Label](UIE-uxml-element-Label.html) or [Image](UIE-uxml-element-Image.html)
will allow the `NavigationSubmitEvent` to bubble up to its parent elements,
allowing them to handle the event if needed.

## Example

The following code example shows how to register callbacks for navigation
events in a runtime UI:

    
    
    using UnityEngine.UIElements;
    
    public class MyNavigationHandler : MonoBehaviour
    {
      void OnEnable()
      {
        // Get a reference to the root visual element
        var uiDocument = GetComponent<UIDocument>();
        var rootVisualElement = uiDocument.rootVisualElement;
    
        // Register for navigation events
        rootVisualElement.RegisterCallback<NavigationCancelEvent>(OnNavCancelEvent);
        rootVisualElement.RegisterCallback<NavigationMoveEvent>(OnNavMoveEvent);
        rootVisualElement.RegisterCallback<NavigationSubmitEvent>(OnNavSubmitEvent);
      }
    
      private void OnNavSubmitEvent(NavigationSubmitEvent evt)
      {
        Debug.Log($"OnNavSubmitEvent {evt.propagationPhase}");
      }
    
      private void OnNavMoveEvent(NavigationMoveEvent evt)
      {
        Debug.Log($"OnNavMoveEvent {evt.propagationPhase} - move {evt.move} - direction {evt.direction}");
      }
    
      private void OnNavCancelEvent(NavigationCancelEvent evt)
      {
        Debug.Log($"OnNavCancelEvent {evt.propagationPhase}");
      }
    }
    

## Additional resources

  * [Dispatch events](UIE-Events-Dispatching.html)
  * [Handle events](UIE-Events-Handling.html)
  * [Synthesize and send events](UIE-Events-Synthesizing.html)

[](UIE-Mouse-Events.html)

Mouse events

[](UIE-Panel-Events.html)

Panel events

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

