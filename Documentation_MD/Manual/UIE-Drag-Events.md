[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Drag-Events.html)
  * [中文](/cn/current/Manual/UIE-Drag-Events.html)
  * [日本語](/ja/current/Manual/UIE-Drag-Events.html)
  * [한국어](/kr/current/Manual/UIE-Drag-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Drag-Events.html)
  * [中文](/cn/current/Manual/UIE-Drag-Events.html)
  * [日本語](/ja/current/Manual/UIE-Drag-Events.html)
  * [한국어](/kr/current/Manual/UIE-Drag-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Drag-and-drop events

[](UIE-Command-Events.html)

Command events

[](UIE-Layout-Events.html)

Layout events

# Drag-and-drop events

Drag events are sent during operations where **visual elements** A node of a
visual tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) have drag-and-drop behavior.
This is an Editor-only event.

To implement drag-and-drop functionality, make sure that visual elements
register callbacks for specific events.

Visual elements that support drag operations separate into two types:

  * Draggable visual elements
  * Droppable visual elements

You can select a draggable visual element, drag it to a droppable visual
element, and release the element to drop it.

The base class for all drag-and-drop events is
[DragAndDropEventBase](../ScriptReference/UIElements.DragAndDropEventBase_1.html).

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[DragExitedEvent](../ScriptReference/UIElements.DragExitedEvent.html) | Sent when the drag-and-drop process ends. | ✔ | ✔ |   
[DragUpdatedEvent](../ScriptReference/UIElements.DragUpdatedEvent.html) | Sent when the dragged element moves over a drop target. | ✔ | ✔ | ✔  
[DragPerformEvent](../ScriptReference/UIElements.DragPerformEvent.html) | Sent when the dragged element drops onto a target. | ✔ | ✔ | ✔  
[DragEnterEvent](../ScriptReference/UIElements.DragEnterEvent.html) | Sent when the dragged element enters a new `VisualElement`. | ✔ |  |   
[DragLeaveEvent](../ScriptReference/UIElements.DragLeaveEvent.html) | Sent when the dragged element exits the current drop target. | ✔ |  |   
  
## Make visual elements draggable

To make a visual element draggable, you need to register callbacks on the
following three event types:

  * [PointerDownEvent](../ScriptReference/UIElements.PointerDownEvent.html)
  * [PointerUpEvent](../ScriptReference/UIElements.PointerUpEvent.html)
  * [PointerMoveEvent](../ScriptReference/UIElements.PointerMoveEvent.html)

Use the following steps for a drag operation:

  1. Set its state to “being dragged”.
  2. Add the appropriate data to [`DragAndDrop`](../ScriptReference/DragAndDrop.html).
  3. Call [`DragAndDrop.StartDrag()`](../ScriptReference/DragAndDrop.StartDrag.html).
  4. Provide a visual cue to the drag operation. The drop area visual element should remove this feedback when it receives a `DragPerformEvent` or a `DragExitedEvent`.

## Event list

### DragExitedEvent

The [`DragExitedEvent`](../ScriptReference/UIElements.DragExitedEvent.html) is
sent when the user drags any draggable object over a visual element and
releases the mouse pointer. When a drop area visual element receives a
`DragExitedEvent`, it needs to remove all feedback from drag operations.

### DragUpdatedEvent

The [`DragUpdatedEvent`](../ScriptReference/UIElements.DragUpdatedEvent.html)
is sent when the pointer moves over a visual element as the user moves a
draggable object.

When a drop area visual element receives a `DragUpdatedEvent`, it needs to
update the drop feedback. For example, you can move the “ghost” of the dragged
object so it stays under the mouse pointer.

The drop area visual element should also examine
[`DragAndDrop`](../ScriptReference/DragAndDrop.html) properties and set
`DragAndDrop.visualMode` to indicate the effect of a drop operation. For
example, a drop operation could create a new object, move an existing object,
or reject the drop operation.

### DragPerformEvent

The [`DragPerformEvent`](../ScriptReference/UIElements.DragPerformEvent.html)
is sent when the user drags any draggable object and releases the mouse
pointer over a visual element. This only occurs if a visual element sets
[`DragAndDrop.visualMode`](../ScriptReference/DragAndDrop-visualMode.html) to
something other than `DragAndDropVisualMode.None` or
`DragAndDropVisualMode.Rejected` to indicate that it can accept dragged
objects.

When a drop area visual element receives a `DragPerformEvent`, it needs to act
on the dragged objects stored in `DragAndDrop.objectReferences`,
`DragAndDrop.paths` or `DragAndDrop.GetGenericData()`.

For example, it might add new visual elements at the location where the user
drops the objects.

### DragEnterEvent

The [`DragEnterEvent`](../ScriptReference/UIElements.DragEnterEvent.html) is
sent when the pointer enters a visual element during a drag operation.

When a drop area visual element receives a `DragEnterEvent`, it needs to
provide feedback that lets the user know that it, or one of its children, is a
target for a potential drop operation. For example, you can add a [USS](UIE-
USS.html) class to the target element and display a “ghost” of the dragged
object under the mouse pointer.

### DragLeaveEvent

The [`DragLeaveEvent`](../ScriptReference/UIElements.DragLeaveEvent.html) is
sent when the pointer exits a visual element as the user moves a draggable
object.

When a drop area visual element receives a `DragLeaveEvent`, it needs to stop
providing drop feedback. For example, you can remove the USS class that you
added when the target element received a `DragEnterEvent`, and no longer
display the “ghost” of the dragged object.

## Examples

  * [Create a drag-and-drop UI to drag between Editor windows](UIE-drag-across-windows.html)

[](UIE-Command-Events.html)

Command events

[](UIE-Layout-Events.html)

Layout events

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

