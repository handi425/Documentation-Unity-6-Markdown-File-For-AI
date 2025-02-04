[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Layout-Events.html)
  * [中文](/cn/current/Manual/UIE-Layout-Events.html)
  * [日本語](/ja/current/Manual/UIE-Layout-Events.html)
  * [한국어](/kr/current/Manual/UIE-Layout-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Layout-Events.html)
  * [中文](/cn/current/Manual/UIE-Layout-Events.html)
  * [日本語](/ja/current/Manual/UIE-Layout-Events.html)
  * [한국어](/kr/current/Manual/UIE-Layout-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Layout events

[](UIE-Drag-Events.html)

Drag-and-drop events

[](UIE-Focus-Events.html)

Focus events

# Layout events

[`GeometryChangedEvent`](../ScriptReference/UIElements.GeometryChangedEvent.html)
is currently the only layout event.

The base class for `GeometryChangedEvent` is the
[EventBase](../ScriptReference/UIElements.EventBase.html) class.

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[GeometryChangedEvent](../ScriptReference/UIElements.GeometryChangedEvent.html) | Sent when the position or the dimensions of an element changes. |  |  |   
  
## Unique properties

**`oldRect`** : The former position and dimensions of the element.

**`newRect`** : The new position and dimensions of the element.

## GeometryChangedEvent

The `GeometryChangedEvent` is sent when either the position or the dimensions
of an element changes. Events of this type are only sent to the event target.

It’s important to unregister from the `GeometryChangedEvent` event after you
receive your callback, as additional layout changes will trigger the callback
again.

**`target`** : The element with a new geometry.

[](UIE-Drag-Events.html)

Drag-and-drop events

[](UIE-Focus-Events.html)

Focus events

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

