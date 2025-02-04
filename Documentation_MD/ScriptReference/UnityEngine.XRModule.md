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

# UnityEngine.XRModule

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

The XR module contains the VR and AR related platform support functionality.

### Classes

[CommonUsages](XR.CommonUsages.html)| Defines static variables that are used
to retrieve input features from XR.InputDevice.TryGetFeatureValue.  
---|---  
[InputDevices](XR.InputDevices.html)| An interface for accessing devices in
the XR input subsytem.  
[InputTracking](XR.InputTracking.html)| A collection of methods and properties
for accessing XR input devices by their XR Node representation.  
[XRDisplaySubsystem](XR.XRDisplaySubsystem.html)| An XRDisplaySubsystem
controls rendering to a head tracked display.  
[XRDisplaySubsystemDescriptor](XR.XRDisplaySubsystemDescriptor.html)| Class
providing information about XRDisplaySubsystem registration.  
[XRInputSubsystem](XR.XRInputSubsystem.html)| XRInputSubsystem Instance is
used to enable and disable the inputs coming from a specific plugin.  
[XRInputSubsystemDescriptor](XR.XRInputSubsystemDescriptor.html)| Information
about an Input subsystem.  
[XRMeshSubsystem](XR.XRMeshSubsystem.html)| Allows external systems to provide
dynamic meshes to Unity.  
[XRMeshSubsystemDescriptor](XR.XRMeshSubsystemDescriptor.html)| Information
about an XRMeshSubsystem.  
[XRStats](XR.Provider.XRStats.html)| Provides timing and other statistics from
XR subsystems.  
  
### Structs

[Bone](XR.Bone.html)| A tracked bone on the device at an XRNode in the XR
input subsystem.  
---|---  
[Eyes](XR.Eyes.html)| Contains eye tracking data from the device at an XRNode
in the XR input subsystem.  
[Hand](XR.Hand.html)| A tracked hand on the device at an XRNode in the XR
input subsystem.  
[HapticCapabilities](XR.HapticCapabilities.html)| Describes the haptic
capabilities of the device at an XRNode in the XR input subsystem.  
[InputDevice](XR.InputDevice.html)| Defines an input device in the XR input
subsystem.  
[InputFeatureUsage](XR.InputFeatureUsage.html)| Defines a generic usage that
maps to an input feature on a device. Use the As method to turn into a generic
usage.  
[InputFeatureUsage<T0>](XR.InputFeatureUsage_1.html)| Defines a generic usage
that maps to an input feature on a device.  
[MeshGenerationResult](XR.MeshGenerationResult.html)| Contains event
information related to a generated mesh.  
[MeshId](XR.MeshId.html)| A session-unique identifier for trackables in the
environment, e.g., planes and feature points.  
[MeshInfo](XR.MeshInfo.html)| Contains state information related to a tracked
mesh.  
[MeshTransform](XR.MeshTransform.html)| Contains transform information related
to a tracked mesh.  
[XRMirrorViewBlitMode](XR.XRMirrorViewBlitMode.html)| Engine reserved blit
modes. Blit mode capabilities should be queried from
XRDisplaySubsystemDescriptor.GetAvailableMirrorBlitModeCount and
XRDisplaySubsystemDescriptor.GetMirrorBlitModeByIndex.  
[XRMirrorViewBlitModeDesc](XR.XRMirrorViewBlitModeDesc.html)| Struct that
describes the mirror view blit mode.  
[XRNodeState](XR.XRNodeState.html)| Describes the state of a node tracked by
an XR system.  
  
### Enumerations

[HandFinger](XR.HandFinger.html)| Enumeration describing the AR rendering mode
used with Hand.  
---|---  
[InputDeviceCharacteristics](XR.InputDeviceCharacteristics.html)| A set of bit
flags describing InputDevice characteristics.  
[InputDeviceRole](XR.InputDeviceRole.html)| Enumeration describing the role of
a InputDevice in providing input.  
[InputTrackingState](XR.InputTrackingState.html)| Represents the values being
tracked for this device.  
[MeshChangeState](XR.MeshChangeState.html)| The state of a tracked mesh since
the last query.  
[MeshGenerationOptions](XR.MeshGenerationOptions.html)| Options for generating
meshes.  
[MeshGenerationStatus](XR.MeshGenerationStatus.html)| The status of a
XRMeshSubsystem.GenerateMeshAsync.  
[MeshVertexAttributes](XR.MeshVertexAttributes.html)| A set of vertex
attributes.  
[TrackingOriginModeFlags](XR.TrackingOriginModeFlags.html)| This enum provides
context to where the 0,0,0 point of tracking for InputDevices is.  
[XRNode](XR.XRNode.html)| Enumeration of XR nodes which can be updated by XR
input or sent haptic data.  
  
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

