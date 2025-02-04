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

# IPointerEvent

interface in UnityEngine.UIElements

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

This interface describes properties available to pointer events.

### Properties

[actionKey](UIElements.IPointerEvent-actionKey.html)|  Gets a boolean value
that indicates whether the platform-specific action key is pressed. True means
the action key is pressed. False means it isn't.  
---|---  
[altitudeAngle](UIElements.IPointerEvent-altitudeAngle.html)|  Gets the angle
of the stylus relative to the surface, in radians  
[altKey](UIElements.IPointerEvent-altKey.html)|  Gets a boolean value that
indicates whether the Alt key is pressed. True means the Alt key is pressed.
False means it isn't.  
[azimuthAngle](UIElements.IPointerEvent-azimuthAngle.html)|  Gets the angle of
the stylus relative to the x-axis, in radians.  
[button](UIElements.IPointerEvent-button.html)|  Gets a value that indicates
which mouse button was pressed or released (if any) to cause this event: 0 is
the left button, 1 is the right button, 2 is the middle button. A negative
value indicates that no mouse button changed state during this event.  
[clickCount](UIElements.IPointerEvent-clickCount.html)|  Gets the number of
times the button was pressed.  
[commandKey](UIElements.IPointerEvent-commandKey.html)|  Gets a boolean value
that indicates whether the Windows/Cmd key is pressed. True means the
Windows/Cmd key is pressed. False means it isn't.  
[ctrlKey](UIElements.IPointerEvent-ctrlKey.html)|  Gets a boolean value that
indicates whether the Ctrl key is pressed. True means the Ctrl key is pressed.
False means it isn't.  
[deltaPosition](UIElements.IPointerEvent-deltaPosition.html)|  Gets the
difference between the pointer's position during the previous mouse event and
its position during the current mouse event.  
[deltaTime](UIElements.IPointerEvent-deltaTime.html)|  Gets the amount of time
that has elapsed since the last recorded change in pointer values, in seconds.  
[isPrimary](UIElements.IPointerEvent-isPrimary.html)|  Gets a boolean value
that indicates whether the pointer is a primary pointer. True means the
pointer is a primary pointer. False means it isn't.  
[localPosition](UIElements.IPointerEvent-localPosition.html)|  Gets the
pointer position in the current target's coordinate system.  
[modifiers](UIElements.IPointerEvent-modifiers.html)|  Gets flags that
indicate whether modifier keys (Alt, Ctrl, Shift, Windows/Cmd) are pressed.  
[penStatus](UIElements.IPointerEvent-penStatus.html)|  Specifies the state of
the pen. For example, whether the pen is in contact with the screen or tablet,
whether the pen is inverted, and whether buttons are pressed. On macOS,
penStatus will not reflect changes to button mappings.  
[pointerId](UIElements.IPointerEvent-pointerId.html)|  Gets the identifier of
the pointer that sends the event.  
[pointerType](UIElements.IPointerEvent-pointerType.html)|  Gets the type of
pointer that created the event.  
[position](UIElements.IPointerEvent-position.html)|  Gets the pointer position
in the Screen or World coordinate system.  
[pressedButtons](UIElements.IPointerEvent-pressedButtons.html)|  Gets a
bitmask that describes the buttons that are currently pressed.  
[pressure](UIElements.IPointerEvent-pressure.html)|  Gets the amount of
pressure currently applied by a touch.  
[radius](UIElements.IPointerEvent-radius.html)|  Gets an estimate of the
radius of a touch.  
[radiusVariance](UIElements.IPointerEvent-radiusVariance.html)|  Gets the
accuracy of the touch radius.  
[shiftKey](UIElements.IPointerEvent-shiftKey.html)|  Gets a boolean value that
indicates whether the Shift key is pressed. True means the Shift key is
pressed. False means it isn't.  
[tangentialPressure](UIElements.IPointerEvent-tangentialPressure.html)|  Gets
the pressure applied to an additional pressure-sensitive control on the
stylus.  
[tilt](UIElements.IPointerEvent-tilt.html)|  Specifies the angle of the pen
relative to the X and Y axis respectively, in radians.  
[twist](UIElements.IPointerEvent-twist.html)|  Gets the rotation of the stylus
around its axis, in radians.  
  
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

