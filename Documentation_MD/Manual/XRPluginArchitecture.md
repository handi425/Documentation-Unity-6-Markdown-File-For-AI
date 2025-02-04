[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/XRPluginArchitecture.html)
  * [中文](/cn/current/Manual/XRPluginArchitecture.html)
  * [日本語](/ja/current/Manual/XRPluginArchitecture.html)
  * [한국어](/kr/current/Manual/XRPluginArchitecture.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/XRPluginArchitecture.html)
  * [中文](/cn/current/Manual/XRPluginArchitecture.html)
  * [日本語](/ja/current/Manual/XRPluginArchitecture.html)
  * [한국어](/kr/current/Manual/XRPluginArchitecture.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Overview](xr-support-landing.html)
  * XR architecture

[](VROverview.html)

VR development in Unity

[](VRReference.html)

XR API reference

# XR architecture

Unity supports **XR** An umbrella term encompassing Virtual Reality (VR),
Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting
these forms of interactive applications can be referred to as XR devices.
[More info](XR.html)  
See in [Glossary](Glossary.html#XR) development through its **plug-in** A set
of code created outside of Unity that creates functionality in Unity. There
are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) framework and a set of feature and
tool packages. Go to the [XR Plug-in Management](xr-plugin-management.html)
category in ****Project Settings** A broad collection of settings which allow
you to configure how Physics, Audio, Networking, Graphics, Input and many
other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings)** to enable XR support in a
Unity project and to choose the plug-ins for the XR platforms that your
project supports. Use the Unity Package Manager to install the additional
feature packages.

The following diagram illustrates the current Unity XR plug-in framework
structure and how it works with platform provider implementations:

![The Unity XR plug-in framework structure](../uploads/Main/unity-xr-tech-
stack.png)

XR subsystems define a common interface for XR features. XR plug-ins implement
these subsystem interfaces to provide data to the subsystem at runtime. Your
XR application can access data for an XR feature through Unity Engine and
package APIs.

## XR provider plug-in framework

An XR provider plug-in is a Unity plug-in that supports one or more XR device
platforms. For example, the ARCore plugin supports the Android **AR**
Augmented Reality [More info](AROverview.html)  
See in [Glossary](Glossary.html#AR) platform on hand-held Android devices,
while the OpenXR plug-in supports several XR devices on multiple operating
systems.

An XR provider plug-in implements interfaces defined by the Unity XR SDK.
These interfaces are called _subsystems_. A plug-in that implements one or
more subsystems is called a _provider_ plug-in. Typically, a provider plug-in
uses the device platform’s native libraries to implement the Unity interfaces
for their devices.

Unity uses subsystem interfaces to communicate with providers for various
platforms, powering the XR features of your application. Because of these
interfaces, you can reuse the same feature code in your application across all
XR devices that have a provider for that feature.

### Subsystems

XR subsystems give you access to XR features in your Unity app. The Unity XR
SDK defines a common interface for subsystems so that all provider plug-ins
implementing a feature generally work the same way in your app. Often you can
change the active provider and rebuild your app to run on a different XR
platform, as long as the platforms are largely similar.

The Unity Engine defines a set of fundamental XR subsystems. Unity packages
can provide additional subsystems. For example, the AR Subsystems package
contains many of the AR-specific subsystem interfaces.

The subsystems defined in the Unity Engine include:

Subsystem | Description  
---|---  
[Display](xrsdk-display.html) | Stereo XR display.  
[Input](xrsdk-input.html) | Spatial tracking and controller input.  
[Meshing](xrsdk-meshing.html) | Generate 3D meshes from environment scans.  
  
**Note:** Unity applications typically do not interact with subsystems
directly. Instead, the features provided by a subsystem are exposed to the
application through an XR plug-in or package. For example, the
[ARMeshManager](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARMeshManager.html)
component in the AR Foundation package lets you add the meshes created by the
Meshing subsystem to a **scene** A Scene contains the environments and menus
of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

[](VROverview.html)

VR development in Unity

[](VRReference.html)

XR API reference

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

