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

# InputDeviceCharacteristics

enumeration

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

A set of bit flags describing [InputDevice](XR.InputDevice.html)
characteristics.

The XR system combines the **InputDeviceFlags** members into the
[InputDevice.characteristics](XR.InputDevice-characteristics.html) bitmask to
describe the characteristics and capabilities of an input device. You can also
pass a bitwise combination of flags from this enumeration to
[InputDevices.GetDevicesWithCharacteristics](XR.InputDevices.GetDevicesWithCharacteristics.html)
to get a list of devices with specific characteristics. For example, you could
use the following to get the right-hand controller:  
  
`(InputDeviceCharacteristics.HeldInHand | InputDeviceCharacteristics.Right)`.

### Properties

[None](XR.InputDeviceCharacteristics.None.html)| A default value specifying no
flags.  
---|---  
[HeadMounted](XR.InputDeviceCharacteristics.HeadMounted.html)| The InputDevice
is attached to the head.  
[Camera](XR.InputDeviceCharacteristics.Camera.html)| The InputDevice has a
camera and associated camera tracking information.  
[HeldInHand](XR.InputDeviceCharacteristics.HeldInHand.html)| The InputDevice
is held in the user's hand. Typically, a tracked controller.  
[HandTracking](XR.InputDeviceCharacteristics.HandTracking.html)| The
InputDevice provides hand tracking information via a Hand input feature.  
[EyeTracking](XR.InputDeviceCharacteristics.EyeTracking.html)| The InputDevice
provides eye tracking information via an Eyes input feature.  
[TrackedDevice](XR.InputDeviceCharacteristics.TrackedDevice.html)| The
InputDevice provides 3DOF or 6DOF tracking data.  
[Controller](XR.InputDeviceCharacteristics.Controller.html)| The InputDevice
is a game controller.  
[TrackingReference](XR.InputDeviceCharacteristics.TrackingReference.html)| The
InputDevice is an unmoving reference object used to locate and track other
objects in the world.  
[Left](XR.InputDeviceCharacteristics.Left.html)| The InputDevice is associated
with the left side of the user.  
[Right](XR.InputDeviceCharacteristics.Right.html)| The InputDevice is
associated with the right side of the user.  
[Simulated6DOF](XR.InputDeviceCharacteristics.Simulated6DOF.html)| The
InputDevice reports software approximated, positional data.  
  
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

