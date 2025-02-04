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

# WSACapability

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

### Description

Options for Universal Windows Platform application capabilities.

A Universal Windows Platform application must specify capabilities for the
system resources and features it expects to use, such as access to the camera.
Unity exposes a subset of these capabilities through Player Settings and
automatically adds any set values to the generated package manifest file. For
capability values that this Unity does not expose, you can add them by editing
the package manifest file.  
For information on Universal Windows Platform capabilities, see [Microsoft's
documentation](https://docs.microsoft.com/en-us/windows/uwp/packaging/app-
capability-declarations).  
  
**Important:** Unity writes application capabilities to the package manifest
when it builds Universal Windows Platform for the first time. Building into an
existing Universal Windows Platform build folder does not update the package
manifest and does not apply any changes.

### Properties

[EnterpriseAuthentication](PlayerSettings.WSACapability.EnterpriseAuthentication.html)|
Allows your application to use Windows domain credentials to log into remote
resources.  
---|---  
[InternetClient](PlayerSettings.WSACapability.InternetClient.html)| Allows
your application to receive incoming data from the internet.  
[InternetClientServer](PlayerSettings.WSACapability.InternetClientServer.html)|
Allows your application to both send and receive internet data.  
[MusicLibrary](PlayerSettings.WSACapability.MusicLibrary.html)| Allows your
application to access files within the user's music library.  
[PicturesLibrary](PlayerSettings.WSACapability.PicturesLibrary.html)| Allows
your application to access files within the user's pictures library.  
[PrivateNetworkClientServer](PlayerSettings.WSACapability.PrivateNetworkClientServer.html)|
Allows your application to send and receive data on the local area network.  
[RemovableStorage](PlayerSettings.WSACapability.RemovableStorage.html)| Allows
your application to access files on removable storage, such as a USB drive or
external hard drive.  
[SharedUserCertificates](PlayerSettings.WSACapability.SharedUserCertificates.html)|
Allows your application to add and access software and hardware-based
certificates in the shared user data store.  
[VideosLibrary](PlayerSettings.WSACapability.VideosLibrary.html)| Allows your
application to access files with the user's video library.  
[WebCam](PlayerSettings.WSACapability.WebCam.html)| Allows your application to
access the video feed of built-in and external webcams.  
[Proximity](PlayerSettings.WSACapability.Proximity.html)| Allows your
application to initiate connections between multiple devices in close
proximity to communicate with one another.  
[Microphone](PlayerSettings.WSACapability.Microphone.html)| Allows your
application to access the audio feed of microphones connected to the device.  
[Location](PlayerSettings.WSACapability.Location.html)| Allows your
application to access the device's location functionality if one is available.  
[HumanInterfaceDevice](PlayerSettings.WSACapability.HumanInterfaceDevice.html)|
Allows your application to interact with connected Human Interface Devices
(HIDs).  
[AllJoyn](PlayerSettings.WSACapability.AllJoyn.html)| Allows your application
AllJoyn-enabled applications and devices on a network to discover and interact
with each other.  
[BlockedChatMessages](PlayerSettings.WSACapability.BlockedChatMessages.html)|
Allows your application to access SMS and MMS messages that the Spam Filter
blocks.  
[Chat](PlayerSettings.WSACapability.Chat.html)| Allows your application to
read and delete text messages, and store messages in the system data store.  
[CodeGeneration](PlayerSettings.WSACapability.CodeGeneration.html)| Allows
your application to access specific APIs that provide just-in-time
compilation.  
[Objects3D](PlayerSettings.WSACapability.Objects3D.html)| Allows your
application to access files within the Windows 3D Object folder.  
[PhoneCall](PlayerSettings.WSACapability.PhoneCall.html)| Allows your
application to access all of the phone lines on the device and perform various
functions.  
[UserAccountInformation](PlayerSettings.WSACapability.UserAccountInformation.html)|
Allows your application to access the end user's name and picture.  
[VoipCall](PlayerSettings.WSACapability.VoipCall.html)| Allows your
application to access voice over internet protocol (VoIP) calling APIs in the
Windows.ApplicationModel.Calls namespace.  
[Bluetooth](PlayerSettings.WSACapability.Bluetooth.html)| Allows your
application to communicate with Bluetooth devices paired with the device.  
[SpatialPerception](PlayerSettings.WSACapability.SpatialPerception.html)|
Allows your application to access spatial mapping data through a mixed reality
device.  
[InputInjectionBrokered](PlayerSettings.WSACapability.InputInjectionBrokered.html)|
Allows your application to inject various forms of input such as HID, touch,
pen, keyboard, or mouse into the system programmatically.  
[Appointments](PlayerSettings.WSACapability.Appointments.html)| Allows your
application to access the end user's appointment store.  
[BackgroundMediaPlayback](PlayerSettings.WSACapability.BackgroundMediaPlayback.html)|
Allows your application to continue media playback while the application is in
the background.  
[Contacts](PlayerSettings.WSACapability.Contacts.html)| Allows your
application limited access to an aggregated view of contacts from various
contacts  
[LowLevelDevices](PlayerSettings.WSACapability.LowLevelDevices.html)| Allows
your application to access custom devices that meet Microsoft-set
requirements.  
[OfflineMapsManagement](PlayerSettings.WSACapability.OfflineMapsManagement.html)|
Allows your application to access offline maps.  
[PhoneCallHistoryPublic](PlayerSettings.WSACapability.PhoneCallHistoryPublic.html)|
Allows your application to read cellular and some voice over internet protocol
(VoIP) call history information on the device.  
[PointOfService](PlayerSettings.WSACapability.PointOfService.html)| Allows
your application to access APIs in the Windows.Devices.PointOfService
namespace.  
[RecordedCallsFolder](PlayerSettings.WSACapability.RecordedCallsFolder.html)|
Allows your application to access the recorded calls folder.  
[RemoteSystem](PlayerSettings.WSACapability.RemoteSystem.html)| Allows your
application to access a list of devices associated with the user's Microsoft
account.  
[SystemManagement](PlayerSettings.WSACapability.SystemManagement.html)| Allows
your application to use basic system administration privileges. This includes
shutting down or rebooting the device and accessing the locale and time zone.  
[UserDataTasks](PlayerSettings.WSACapability.UserDataTasks.html)| Allows your
application to access the current state of the task settings.  
[UserNotificationListener](PlayerSettings.WSACapability.UserNotificationListener.html)|
Allows your application to access the current state of the notification
settings.  
[GazeInput](PlayerSettings.WSACapability.GazeInput.html)| Allows your
application to detect where the user is looking when their device is connected
to a compatible eye-tracking device.  
  
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

