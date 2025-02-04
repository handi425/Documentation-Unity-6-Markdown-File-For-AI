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

# XRInputSubsystem

class in UnityEngine.XR

/

Inherits from:[IntegratedSubsystem](IntegratedSubsystem.html)

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

XRInputSubsystem Instance is used to enable and disable the inputs coming from
a specific plugin.

Starting up an XRInputSubsystem Instance will cause that plugin to start
feeding input device data to the following
[InputTracking](XR.InputTracking.html) systems:
XR.InputTracking.GetLocalPosition and XR.InputTracking.GetLocalRotation.
Calling the Stop or Shutdown functions will disable polling any input device
data for that plugin.

### Public Methods

[GetSupportedTrackingOriginModes](XR.XRInputSubsystem.GetSupportedTrackingOriginModes.html)|
Gets all TrackingOriginModeFlags that this subsystem supports.  
---|---  
[GetTrackingOriginMode](XR.XRInputSubsystem.GetTrackingOriginMode.html)| Gets
the Tracking Origin Mode.  
[TryGetBoundaryPoints](XR.XRInputSubsystem.TryGetBoundaryPoints.html)| Gets
the list of 3D position values that represents the SDK-set boundary.  
[TryGetInputDevices](XR.XRInputSubsystem.TryGetInputDevices.html)| Gets a list
of all connected InputDevices reported by this XRInputSubsystem.  
[TryRecenter](XR.XRInputSubsystem.TryRecenter.html)| Centers the tracking
features on all InputDevices to the current position and orientation of the
head-mounted device.  
[TrySetTrackingOriginMode](XR.XRInputSubsystem.TrySetTrackingOriginMode.html)|
Attempts to set the TrackingOriginModeFlags of the subsystem.  
  
### Events

[boundaryChanged](XR.XRInputSubsystem-boundaryChanged.html)| An event that
takes the delegate instance that the XRInputSubsystem calls when it changes
its tracking boundary.  
---|---  
[trackingOriginUpdated](XR.XRInputSubsystem-trackingOriginUpdated.html)| An
event that takes the delegate instance that the XRInputSubsystem calls when it
changes the origin it reports devices at.  
  
### Inherited Members

### Properties

[running](IntegratedSubsystem-running.html)| Whether or not the subsystem is
running.  
---|---  
  
### Public Methods

[Destroy](IntegratedSubsystem.Destroy.html)| Destroys this instance of a
subsystem.  
---|---  
[Start](IntegratedSubsystem.Start.html)| Starts an instance of a subsystem.  
[Stop](IntegratedSubsystem.Stop.html)| Stops an instance of a subsystem.  
  
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

