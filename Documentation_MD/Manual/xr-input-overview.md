[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xr-input-overview.html)
  * [中文](/cn/current/Manual/xr-input-overview.html)
  * [日本語](/ja/current/Manual/xr-input-overview.html)
  * [한국어](/kr/current/Manual/xr-input-overview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xr-input-overview.html)
  * [中文](/cn/current/Manual/xr-input-overview.html)
  * [日本語](/ja/current/Manual/xr-input-overview.html)
  * [한국어](/kr/current/Manual/xr-input-overview.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR project set up](configuring-project-for-xr.html)
  * [Set up an XR scene](xr-scene-setup.html)
  * XR input options

[](xr-scene-setup.html)

Set up an XR scene

[](xr-origin.html)

XR Origin

# XR input options

The main options to handle input in an **XR** An umbrella term encompassing
Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR)
applications. Devices supporting these forms of interactive applications can
be referred to as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) game or application include:

  * The XR Interaction Toolkit
  * OpenXR interaction profiles
  * “Traditional” input through the Input System or Input Manager
  * The XR.InputDevice and XR.Node APIs
  * Third-party input libraries

In some cases, you might use more than one of these options at the same time.
For example, you could use the XR Interaction Toolkit to allow the user to
pick up objects in the environment, use the Input System to bind a pause
function to a controller button, and use the XR.Node API to read the hardware
state so that you can animate the controller **GameObject** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

**Note:** The OpenXR **plug-in** A set of code created outside of Unity that
creates functionality in Unity. There are two kinds of plug-ins you can use in
Unity: Managed plug-ins (managed .NET assemblies created with tools like
Visual Studio) and Native plug-ins (platform-specific native code libraries).
[More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in), which supports many different XR
devices and controllers, provides its own, additional way to access XR input
and tracking data. You can still use the XR Interaction Toolkit, the Input
System, or the `XR.InputDevice` and `XR.Node` APIs. (The legacy Input Manager
is not supported when you use the OpenXR plugin.) Refer to [Input in Unity
OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.12/manual/input.html)
for more information.

### XR Interaction Toolkit

The [XR Interaction
Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/general-
setup.html#configure-xr-controller-and-interactor) builds on the Input System
and the base `UnityEngine.XR` API to support XR input and interaction. It
provides a near ready-to-use set of components for handling XR input and
defining interactions between the user and the environment and the **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI).

The XR Interaction Toolkit provides:

  * [Interactors](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/architecture.html#interactors): objects in the scene that allow the user to interact with scene GameObjects. Typically driven by XR controllers or the user’s hands.
  * [Interactables](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/architecture.html#interactables)A UI component property that determines whether the component can accept input. [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Selectable.html)  
See in [Glossary](Glossary.html#Interactable): objects in the scene that the
user can interact with (using an interactor).

  * [UI interaction](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/ui-setup.html): supports interaction with Unity’s built-in UI elements.
  * [Locomotion](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/locomotion.html): supports various modes of locomotion, including continuous movement, teleportation, and climbing.

### Input System or Input Manager

You can access the controls of XR Controllers, such as buttons and joysticks,
in the same ways you would access any **game controller** A device to control
objects and characters in a game.  
See in [Glossary](Glossary.html#gamecontroller). To access tracking data, use
the [XR.InputTracking](xr_input.html) API in code. You can also use the Input
System
[TrackedPoseDriver](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.5/api/UnityEngine.InputSystem.XR.TrackedPoseDriver.html)
component to control a GameObject with a tracked device such as a HMD or
controller. The
[TrackedPoseDriver](https://docs.unity3d.com/Packages/com.unity.xr.legacyinputhelpers@2.1/manual/index.html#tracked-
pose-driver) component is also available from the Legacy Input Helpers
package, in case you are not using the Input System.

**Note:** When you use the OpenXR plug-in, you must use the Input System. The
**Input Manager** Settings where you can define all the different input axes,
buttons and controls for your project. [More info](class-InputManager.html)  
See in [Glossary](Glossary.html#InputManager) is not supported.

### XR Hand tracking input

The [XR
Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/index.html)
package provides access to hand tracking data from XR devices that support it.
To access this data, you must also use an XR provider plug-in that has been
updated to support hand tracking, such as [OpenXR version
1.12](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.12/manual/index.html).

The XR Hands package provides the following:

  * The [XRHandTrackingSubsystem](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/api/UnityEngine.XR.Hands.XRHandSubsystem.html) which allows an XR device to send hand data to a Unity app.
  * A [hand tracking API](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/hand-data/xr-hand-tracking.html) Unity apps can use to access the data.
  * Support for the OpenXR [Meta Aim Hand feature](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/features/metahandtrackingaim.html) extension, which provides a gesture aiming system along with OpenXR input bindings for hand tracking data.

### visionOS input

Your input options on visionOS depend on whether your app is running in
windowed mode, **mixed reality** Mixed Reality (MR) combines its own virtual
environment with the user’s real-world environment and allows them to interact
with each other.  
See in [Glossary](Glossary.html#MixedReality) mode, or **virtual reality**
Virtual Reality (VR) immerses users in an artificial 3D world of realistic
images and sounds, using a headset and motion tracking. [More
info](VROverview.html)  
See in [Glossary](Glossary.html#VirtualReality) mode.

In windowed mode, the user’s gaze and pinch gestures are translated into touch
events by the operating system. Your app doesn’t have access to the raw input
data. visionOS reports a maximum of two touch points.

In mixed reality mode, the input options further depend on whether your app is
running in a shared space with other apps or in an immersive space. In a
shared space, the situation is similar to that of a windowed app; the
operating system translates the user’s gaze and hand movements into touch
gestures. In this case, you can use the [Spatial Pointer
Device](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest?subfolder=/manual/PolySpatialInput.html#spatial-
pointer-device-data) to access 3D touch data rather than just 2D. In an
immersive space, you also have access to 3D ray origin and direction of the
user’s gaze at the start of the gesture. In addition, you have access to ARKit
data such as head and hand tracking, plane detection, scene reconstruction
meshes, and image tracking.

In virtual reality mode, you have access to ARKit data such as head and hand
tracking, plane detection, scene reconstruction meshes, and image tracking.
(You do not have access to the **Spatial Pointer Device** or other
PolySpatial-specific components.)

For more information, refer to [PolySpatial visionOS:
Input](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest?subfolder=/manual/Input.html).

### XR Input APIs

The XR Input APIs provide direct access to XR input. The API lets you find
connected XR devices and read their tracking data and state of their input
hardware.

Refer to [Unity XR Input](xr_input.html) for more information about the XR
input API.

### Third-party input APIs

Device makers and other third parties often provide their own input and
interaction APIs that you can use instead of or in addition to those provided
by Unity.

[](xr-scene-setup.html)

Set up an XR scene

[](xr-origin.html)

XR Origin

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

