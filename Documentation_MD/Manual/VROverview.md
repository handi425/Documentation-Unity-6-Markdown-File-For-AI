[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/VROverview.html)
  * [中文](/cn/current/Manual/VROverview.html)
  * [日本語](/ja/current/Manual/VROverview.html)
  * [한국어](/kr/current/Manual/VROverview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/VROverview.html)
  * [中文](/cn/current/Manual/VROverview.html)
  * [日本語](/ja/current/Manual/VROverview.html)
  * [한국어](/kr/current/Manual/VROverview.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Overview](xr-support-landing.html)
  * VR development in Unity

[](AROverview.html)

AR development in Unity

[](XRPluginArchitecture.html)

XR architecture

# VR development in Unity

VR development shares common workflows and design considerations with any
real-time 3D development in Unity. However, distinguishing factors include:

  * **Richer user input** : in addition to “traditional” button and joystick controllers, **VR** devices provide spatial head, controller, and (in some cases) hand and finger tracking.
  * **More “intimate” interaction with the environment** : in conjunction with the possibilities of richer input, VR raises the expectations of much closer and “physical” interaction with the environment than typical 3D games and applications. Users expect to be able to pick things up and interact with objects in the environment. With head tracking, the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) can get much closer to the walls and
other boundaries of the environment – even passing through them.

  * **User comfort concerns** : many people experience motion sickness in VR when camera movement doesn’t match the movement of their head. You can mitigate the causes of motion sickness by maintaining a high frame rate, offering a range of locomotion options so that users can choose a mode they are comfortable with, and avoiding moving the camera independently of the user’s head tracking.

To get started with VR development, use the XR Plug-in Management system to
install and enable XR provider plug-ins for the devices you want to support.
See [XR Project set up](configuring-project-for-xr.html) for more information.

## Basic VR scene elements

A basic VR **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) should contain an [XR Origin](xr-
origin.html), which defines the 3D origin for tracking data. This collection
of **GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and components also contains the
main scene Camera and the GameObjects representing the user’s controllers. See
[Set up an XR scene](xr-scene-setup.html) for instructions on setting up a
basic VR scene.

Beyond the basics, you typically need a way for the user to move around and to
interact with the 3D world you have created. The [XR Interaction
Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/)
provides components for creating interactions like selecting and grabbing
objects. It also provides a customizable locomotion system. You can use the
[Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.5/)
in addition to or instead of the **XR** An umbrella term encompassing Virtual
Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications.
Devices supporting these forms of interactive applications can be referred to
as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) Interaction Toolkit.

## VR packages

Most of the features and APIs used for VR development in Unity are provided
through packages. These packages include:

  * Provider plug-ins
  * XR Interaction Toolkit
  * XR Core Utilities
  * Input System
  * VR project template
  * Hand tracking

### VR provider plug-ins

To build VR apps in Unity, use the XR **Plug-in** A set of code created
outside of Unity that creates functionality in Unity. There are two kinds of
plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies
created with tools like Visual Studio) and Native plug-ins (platform-specific
native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) Management system to add and enable
provider plug-ins for the devices you want to support. See [XR Project set
up](configuring-project-for-xr.html) for instructions.

The VR provider plug-ins supported by Unity include:

  * [Apple visionOS XR Plugin](https://docs.unity3d.com/Packages/com.unity.xr.visionos@latest) for the Apple Vision Pro.
  * [Oculus](https://docs.unity3d.com/Packages/com.unity.xr.oculus@4.2/manual/index.html) for Oculus Rift, Meta Quest 2, and Quest Pro.
  * [OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.10/manual/index.html) for any device with an OpenXR runtime, including Meta headsets, VIVE headsets, Valve SteamVR, HoloLens, Windows **Mixed Reality** Mixed Reality (MR) combines its own virtual environment with the user’s real-world environment and allows them to interact with each other.  
See in [Glossary](Glossary.html#MixedReality), and others.

  * PlayStation VR (available to registered PlayStation developers) for Sony PS VR and PS VR2 devices. Visit [PlayStation Partners](https://partners.playstation.net/) for more information.
  * [Mock HMD](https://docs.unity3d.com/Packages/com.unity.xr.mock-hmd@latest/) for simulating a VR headset in the Unity Editor Play mode view.

**Note:** Many headset makers are working toward using the OpenXR runtime as a
standard. However, this process is not complete and there can be feature
discrepancies between OpenXR and a headset maker’s own provider plug-in or SDK

### XR Interaction Toolkit

The [XR Interaction
Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/)
can make it easier and faster to develop VR applications. The XR Interaction
Toolkit provides:

  * An [XR Origin](xr-origin.html) set up with controllers.
  * [XR controller](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/general-setup.html#configure-xr-controller-and-interactor) setups with Input System presets for basic interactions like select and grab.
  * [Interactor and Interactable components](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/architecture.html#interactors) for creating object manipulation.
  * A configurable [locomotion system](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/locomotion.html).
  * [XR UI input](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/ui-setup.html).

### XR Core Utilities

The [XR Core Utilities](https://docs.unity3d.com/Packages/com.unity.xr.core-
utils@2.3/manual/index.html) package contains software utilities used by other
Unity XR plug-ins and packages. Typically, this package gets installed in your
project as a dependency of other XR packages.

### Input System

The Unity [Input
System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/index.html)
package not only supports accessing user input from VR controller buttons and
joysticks, but also provides access to XR tracking data and haptics. The Input
System package is required if you use the XR Interaction Toolkit or the OpenXR
provider plug-in.

## Hand tracking

Hand tracking is a feature that allows users to interact with a VR application
using their hands. Hand tracking is supported by the [XR
Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.2/manual/index.html)
package.

The Hands package provides:

  * A standard [hand data model](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/hand-data/xr-hand-data-model.html).
  * An [API](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/api/UnityEngine.XR.Hands.XRHandSubsystem.html) for accessing hand tracking data.
  * The [XR Hand Skeleton Driver](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/hand-data/xr-hand-visuals.html) component, which maps a set of Transforms to their corresponding hand **joints** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) and updates those Transforms as
tracking data is received.

  * The [XR Hand Mesh Controller](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/hand-data/xr-hand-visuals.html#xr-hand-mesh-controller), which enables and disables a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) as hand tracking is acquired or lost.

  * A [HandVisualizer](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/project-setup/scene-setup.html) sample that demonstrates how to use the hand tracking API.

[](AROverview.html)

AR development in Unity

[](XRPluginArchitecture.html)

XR architecture

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

