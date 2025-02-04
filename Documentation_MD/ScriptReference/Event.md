[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# Event

class in UnityEngine

/

Implemented in:[UnityEngine.IMGUIModule](UnityEngine.IMGUIModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

A UnityGUI event.

Events correspond to user input (key presses, mouse actions), or are UnityGUI
layout or rendering events.  
  
For each event [OnGUI](MonoBehaviour.OnGUI.html) is called in the scripts; so
OnGUI is potentially called multiple times per frame. [Event.current](Event-
current.html) corresponds to "current" event inside OnGUI call.  
  
Additional resources: [GUI Scripting Guide](../Manual/GUIScriptingGuide.html),
[EventType](EventType.html).

### Static Properties

[current](Event-current.html)| The current event that's being processed right
now.  
---|---  
  
### Properties

[alt](Event-alt.html)| Is Alt/Option key held down? (Read Only)  
---|---  
[button](Event-button.html)| Which mouse button was pressed.  
[capsLock](Event-capsLock.html)| Is Caps Lock on? (Read Only)  
[character](Event-character.html)| The character typed.  
[clickCount](Event-clickCount.html)| How many consecutive mouse clicks have we
received.  
[command](Event-command.html)| Is Command/Windows key held down? (Read Only)  
[commandName](Event-commandName.html)| The name of an ExecuteCommand or
ValidateCommand Event.  
[control](Event-control.html)| Is Control key held down? (Read Only)  
[delta](Event-delta.html)| The relative movement of the mouse compared to last
event.  
[displayIndex](Event-displayIndex.html)| Index of display that the event
belongs to.  
[functionKey](Event-functionKey.html)| Is the current keypress a function key?
(Read Only)  
[isKey](Event-isKey.html)| Is this event a keyboard event? (Read Only)  
[isMouse](Event-isMouse.html)| Is this event a mouse event? (Read Only)  
[keyCode](Event-keyCode.html)| The raw key code for keyboard events.  
[modifiers](Event-modifiers.html)| Which modifier keys are held down.  
[mousePosition](Event-mousePosition.html)| The mouse position.  
[numeric](Event-numeric.html)| Is the current keypress on the numeric
keyboard? (Read Only)  
[penStatus](Event-penStatus.html)| Specifies the state of the pen. For
example, whether the pen is in contact with the screen or tablet, whether the
pen is inverted, and whether buttons are pressed.  
[pointerType](Event-pointerType.html)| The type of pointer that created this
event (for example, mouse, touch screen, pen).  
[pressure](Event-pressure.html)| How hard pen pressure is applied, normalized
between 0 (no pressure) and 1 (maximum pressure).  
[shift](Event-shift.html)| Is Shift held down? (Read Only)  
[tilt](Event-tilt.html)| Specifies the angle of the pen relative to the X and
Y axes, expressed in radians.  
[twist](Event-twist.html)| Specifies the rotation of the pen around its axis,
expressed in radians. The default value is 0.  
[type](Event-type.html)| The type of event.  
  
### Public Methods

[GetTypeForControl](Event.GetTypeForControl.html)| Get a filtered event type
for a given control ID.  
---|---  
[Use](Event.Use.html)| Use this event.  
  
### Static Methods

[GetEventCount](Event.GetEventCount.html)| Returns the current number of
events that are stored in the event queue.  
---|---  
[KeyboardEvent](Event.KeyboardEvent.html)| Create a keyboard event.  
[PopEvent](Event.PopEvent.html)| Get the next queued [Event] from the event
system.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

