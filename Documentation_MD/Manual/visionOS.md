[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/visionOS.html)
  * [中文](/cn/current/Manual/visionOS.html)
  * [日本語](/ja/current/Manual/visionOS.html)
  * [한국어](/kr/current/Manual/visionOS.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/visionOS.html)
  * [中文](/cn/current/Manual/visionOS.html)
  * [日本語](/ja/current/Manual/visionOS.html)
  * [한국어](/kr/current/Manual/visionOS.html)

  * [Platform development ](PlatformSpecific.html)
  * visionOS

[](windowsstore-deviceportal.html)

Deploy a Windows or UWP app with the Windows Device Portal

[](webgl.html)

Web

# visionOS

visionOS is the operating system of the Vision Pro, Apple’s latest spatial
computing device. Unity developers can leverage existing 3D **scenes** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and assets to build games or
applications for visionOS. For more information about visionOS, refer to
Apple’s [visionOS Overview](https://developer.apple.com/visionos/learn).

visionOS provides a few different modes in which apps can be displayed:
Windows, Volumes or Spaces. Users can use Windows to present 2D or 3D content
(without stereo), or use Volumes to present 3D content and objects. With
Volumes, users have the flexibility to walk around and interact with 3D
content from any angle.

Depending on application type, visionOS apps can run in either a **Shared
Space** or a **Full Space**. The Shared Space works as a multitasking
environment similar to the desktop of a personal computer; in this mode, users
can see and interact with Windows and Volumes from multiple applications
simultaneously. For more immersive experiences, you can run your application
in a Full Space, which only displays content from one app at time. Windowed
apps always run in a Shared Space. Fully immersive (VR) content always run in
a Full Space. Immersive (MR) content can run in either a Shared Space or a
Full Space, and switch between them, depending on the **Mode** setting of its
Volume **Camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) Window Configuration.

## Requirements

Fully Immersive (VR) and Immersive (MR) apps are only available to Unity Pro,
Unity Enterprise, and Unity Industry users. [Learn more about these
plans](https://unity.com/pricing).

## Getting Started

All visionOS application types require that you install the visionOS module to
the Unity Editor via the [Unity
Hub](https://docs.unity3d.com/hub/manual/AddModules.html). The visionOS module
is available for Unity 2022.3.5f1+.

In addition, Fully Immersive (VR) and Immersive (MR) apps require that you
install extra packages. Refer to [Install PolySpatial and visionOS
support](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@1.2/manual/Install.html)
for instructions.

For Fully Immersive (VR) apps, you need:

  * `com.unity.xr.visionos`

For Immersive (MR) apps, you need:

  * `com.unity.xr.visionos`
  * `com.unity.polyspatial.visionos`
  * `com.unity.polyspatial.xr`

If you do not install these packages, you can only build Windowed apps.

Once you have installed the necessary modules and packages, navigate to
**Project Settings > XR Plug-in Manager > Apple visionOS > App Mode** and
select between **Mixed Reality - Volume or Immersive Space** and **Virtual
Reality - Fully Immersive Space** to configure your build for the desired
application mode.

## Windowed apps

Unity describes applications that live within Windows as Windowed apps. By
default, your Unity content is built as a Windowed app on the visionOS
platform if you don’t install and enable the visionOS **XR** An umbrella term
encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality
(MR) applications. Devices supporting these forms of interactive applications
can be referred to as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) provider **plug-in** A set of code created
outside of Unity that creates functionality in Unity. There are two kinds of
plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies
created with tools like Visual Studio) and Native plug-ins (platform-specific
native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) in the **XR Plug-in Management**
section of your ****Project Settings** A broad collection of settings which
allow you to configure how Physics, Audio, Networking, Graphics, Input and
many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings)**. Refer to [Choose XR
provider plug-ins](XR.html) for more information about enabling provider plug-
ins.

To detect interactions on the Unity application within a Window component on
visionOS, use the “Touch Support” provided by the Input System package
([com.unity.inputsystem](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.6/manual/index.html)).
To learn more about designing for the Window component on visionOS, visit
[Apple’s Human Interface Guidelines for
visionOS](https://developer.apple.com/design/human-interface-
guidelines/windows#visionOS).

## Mixed Reality (Immersive) and Virtual Reality (Fully Immersive) Apps

For more information about developing fully immersive **virtual reality**
Virtual Reality (VR) immerses users in an artificial 3D world of realistic
images and sounds, using a headset and motion tracking. [More
info](VROverview.html)  
See in [Glossary](Glossary.html#VirtualReality) (VR) apps and immersive
**mixed reality** Mixed Reality (MR) combines its own virtual environment with
the user’s real-world environment and allows them to interact with each other.  
See in [Glossary](Glossary.html#MixedReality) (MR) apps for visionOS, please
refer to our [visionOS-specific
documentation](https://create.unity.com/spatial).

[](windowsstore-deviceportal.html)

Deploy a Windows or UWP app with the Windows Device Portal

[](webgl.html)

Web

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

