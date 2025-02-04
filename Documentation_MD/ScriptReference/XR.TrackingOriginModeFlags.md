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

# TrackingOriginModeFlags

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

This enum provides context to where the 0,0,0 point of tracking for
[InputDevice](XR.InputDevice.html)s is.

Each [XRInputSubsystem](XR.XRInputSubsystem.html) has a single origin for all
reported [InputDevice](XR.InputDevice.html)s. The origin can be relative to
either real-world objects, such as a physical tracking device, or virtual
objects, such as the center of a user-drawn bounding region.

### Properties

[Unknown](XR.TrackingOriginModeFlags.Unknown.html)|
TrackingOriginModeFlags.Unknown enumerates when the XRInputSubsystem was not
able to set its tracking origin or has no tracking.  
---|---  
[Device](XR.TrackingOriginModeFlags.Device.html)|  XRInputSubsystem tracks all
InputDevices in reference to the first known location of a specific
InputDevice when set to TrackingOriginModeFlags.Device.  
[Floor](XR.TrackingOriginModeFlags.Floor.html)|  XRInputSubsystem tracks all
InputDevices in reference to a point on the floor when set to
TrackingOriginModeFlags.Floor.  
[TrackingReference](XR.TrackingOriginModeFlags.TrackingReference.html)|
XRInputSubsystem tracks all InputDevices in reference to an InputDevice with
the InputDeviceCharacteristics.TrackingReference flag set when set to
TrackingOriginModeFlags.TrackingReference.  
[Unbounded](XR.TrackingOriginModeFlags.Unbounded.html)|  XRInputSubsystem
tracks all InputDevices in relation to a world anchor. This world anchor can
change at any time, and is chosen by the runtime.  
  
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

