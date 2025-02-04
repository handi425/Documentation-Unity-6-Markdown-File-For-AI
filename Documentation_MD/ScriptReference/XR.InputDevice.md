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

# InputDevice

struct in UnityEngine.XR

/

Implemented in:[UnityEngine.XRModule](UnityEngine.XRModule.html)

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

Defines an input device in the XR input subsystem.

To retrieve input features or route haptic feedback to XR input devices,
specify an [XRNode](XR.XRNode.html) as the destination. Use
[XRNode.LeftHand](XR.XRNode.LeftHand.html) and
[XRNode.RightHand](XR.XRNode.RightHand.html) to send haptic data to left or
right devices. You can send haptic data either as an impulse or as a buffer of
raw bytes that is played back through the haptic device. You can stop haptic
output or query the device for its buffered capabilities at any time.

### Properties

[characteristics](XR.InputDevice-characteristics.html)| Read Only. A bitmask
of enumerated flags describing the characteristics of this InputDevice.  
---|---  
[isValid](XR.InputDevice-isValid.html)| Read Only. True if the device is
currently a valid input device; otherwise false.  
[manufacturer](XR.InputDevice-manufacturer.html)| The manufacturer of the
connected Input Device.  
[name](XR.InputDevice-name.html)| Read Only. The name of the device in the XR
system. This is a platform provided unique identifier for the device.  
[serialNumber](XR.InputDevice-serialNumber.html)| The serial number of the
connected Input Device. Blank if no serial number is available.  
[subsystem](XR.InputDevice-subsystem.html)| Gets the XRInputSubsystem that
reported this InputDevice.  
  
### Public Methods

[SendHapticBuffer](XR.InputDevice.SendHapticBuffer.html)| Sends a raw buffer
of haptic data to the device.  
---|---  
[SendHapticImpulse](XR.InputDevice.SendHapticImpulse.html)| Sends a haptic
impulse to a device.  
[StopHaptics](XR.InputDevice.StopHaptics.html)| Stop all haptic playback for a
device.  
[TryGetFeatureUsages](XR.InputDevice.TryGetFeatureUsages.html)| Gets a list of
all the input feature usages available on this device. For example, "Trigger"
or "Device Position".  
[TryGetFeatureValue](XR.InputDevice.TryGetFeatureValue.html)| Retrieves
information about the input feature specified by the Usage parameter. Those
functions which take a time parameter allow querying for that feature at a
particular point in time  
[TryGetHapticCapabilities](XR.InputDevice.TryGetHapticCapabilities.html)| Gets
the haptic capabilities of the device.  
  
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

