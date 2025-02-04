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

# InputDevices

class in UnityEngine.XR

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

An interface for accessing devices in the XR input subsytem.

To route haptic feedback to XR input devices, specify an
[XRNode](XR.XRNode.html) as the destination. This interface provides access to
input devices using an XRNode. For example, use the use
[XRNode.LeftHand](XR.XRNode.LeftHand.html) and
[XRNode.RightHand](XR.XRNode.RightHand.html) to access the left or right
devices.

### Static Methods

[GetDeviceAtXRNode](XR.InputDevices.GetDeviceAtXRNode.html)| Gets the input
device at a given XRNode endpoint.  
---|---  
[GetDevices](XR.InputDevices.GetDevices.html)| Gets a list of active input
devices available to the XR Input Subsystem.  
[GetDevicesAtXRNode](XR.InputDevices.GetDevicesAtXRNode.html)| Gets a list of
active input devices available to the XR Input Subsystem at a given XRNode
endpoint.  
[GetDevicesWithCharacteristics](XR.InputDevices.GetDevicesWithCharacteristics.html)|
Gets the list of active XR input devices that match the specified
InputDeviceCharacteristics.  
  
### Events

[deviceConfigChanged](XR.InputDevices-deviceConfigChanged.html)| Defines the
delegate to use to register events when an InputDevice's configuration
changes.  
---|---  
[deviceConnected](XR.InputDevices-deviceConnected.html)| Defines the delegate
to use to register events when an InputDevice is connected.  
[deviceDisconnected](XR.InputDevices-deviceDisconnected.html)| Defines the
delegate to use to register events when an InputDevice is disconnected.  
  
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

