[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xr-origin.html)
  * [中文](/cn/current/Manual/xr-origin.html)
  * [日本語](/ja/current/Manual/xr-origin.html)
  * [한국어](/kr/current/Manual/xr-origin.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xr-origin.html)
  * [中文](/cn/current/Manual/xr-origin.html)
  * [日本語](/ja/current/Manual/xr-origin.html)
  * [한국어](/kr/current/Manual/xr-origin.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR project set up](configuring-project-for-xr.html)
  * [Set up an XR scene](xr-scene-setup.html)
  * XR Origin

[](xr-input-overview.html)

XR input options

[](xr-plugin-management.html)

XR Plug-in Management settings

# XR Origin

The ****XR** An umbrella term encompassing Virtual Reality (VR), Augmented
Reality (AR) and Mixed Reality (MR) applications. Devices supporting these
forms of interactive applications can be referred to as XR devices. [More
info](XR.html)  
See in [Glossary](Glossary.html#XR) Origin** serves as the center of tracking
space in an XR **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

An **XR Origin** is a set of **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and components that work together
to transform XR tracking data into the scene world space.

The following topics discuss the XR Origin and how to use it in your project:

Topic | Description  
---|---  
XR tracking space | Describes the relationship between the **XR Origin** , the device tracking space and the Unity scene.  
XR Origin configurations | Describes the different **XR Origin** configurations available in Unity.  
  
Refer to [XR Origin
component](https://docs.unity3d.com/Packages/com.unity.xr.core-
utils@2.2/manual/xr-origin-reference.html) for more details about the **XR
Origin** and its child GameObjects and components.

## XR tracking space

XR devices choose an origin point in the real world at initialization. The
positions and orientations of all tracked entities, such as the user’s headset
or hand-held device, XR controllers, hands, and physical objects detected
around the user, are reported relative to this chosen point.

**Note:** The criteria for choosing the initial origin varies by platform.
Typically, a device chooses a point at or directly below the user’s HMD (VR)
or hand-held device (AR).

If you used the tracking data directly in your scene, the user would appear to
be standing at the scene origin point (0, 0 ,0). To make the user appear at a
different location in the scene, you need to transform the tracking data to
the desired position and orientation. Unity provides the **XR Origin** to do
this automatically. Many Unity XR features, including those provided by [AR
Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/)
and the [XR Interaction
Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/),
require an **XR Origin** in the scene. You can choose from a variety of XR
Origin configurations to suit your project.

To position the XR tracking space in a Unity scene, add an **XR Origin**
GameObject at the location where you want the user to appear when the scene
starts. For example, to place the user at the scene origin, place the **XR
Origin** GameObject there. You can rotate the **XR Origin** around its y axis
to face the user in the desired starting direction.

The **XR Origin** contains GameObjects representing tracked entities as
children within its hierarchy. For example, the user’s headset or hand-held
device is represented by the **Camera** A component which creates an image of
a particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) GameObject. Because they are children,
the tracking data controlling the positions and rotations of these GameObjects
is automatically transformed into world space relative to the **XR Origin**.
When the user moves in the real world, these child GameObjects move relative
to the **XR Origin** in the scene.

![Man wearing MR headset reaches toward a virtual
object](../uploads/Main/xr_origin_diagram.webp)  
_By using the**XR Origin** (**A**) as the parent for transforming tracking
data, the tracking origin and the Unity scene origin (**B**) can be in
different places and orientations._

The parent **XR Origin** GameObject doesn’t move when the user walks around
the scene. However, you can move the **XR Origin** with a script to allow the
user to teleport or navigate around the scene via controller input.

## XR Origin configurations

The Unity XR packages provide several **XR Origin** configurations tailored
for different types of XR applications. You can use the **GameObject > XR**
menu to add an **XR Origin** to the current Scene. The available options
depend on which packages you have added to your project.

**Important:** You should never have more than one active **XR Origin** in a
scene. If you need different configurations of the **XR Origin** in a scene
for different purposes, only enable one at the same time.

XR type | Configuration | Menu option | Package | Notes  
---|---|---|---|---  
**VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR), **MR** Mixed Reality  
See in [Glossary](Glossary.html#MR) | XR Rig | **Convert Main Camera To XR Rig** |  [XR Legacy Input Helpers](https://docs.unity3d.com/Packages/com.unity.xr.legacyinputhelpers@2.1/) (installed with the XR Plug-in Management package) | Replaces the standard Camera in a basic Unity Scene. The logic used to replace the main camera can fail in complex scenes. Unity removes this option when you install the XR Interaction Tools package. The **XR Rig** GameObject created by this menu option is slightly different than the **XR Origin** and might not be as compatible with other Unity XR features.  
VR, MR | XR Origin | **XR Origin** |  [XR Core Utils](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.3/) (installed with the XR Interaction Toolkit package) | Does not include GameObjects for controllers.  
VR, MR | XR Origin (VR) | **XR Origin (VR)** | [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/) | Includes controller GameObjects set up for action-based input.  
VR, MR | XR Origin (VR) | **Device-based > XR Origin (VR)** | [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/) | Includes controller GameObjects set up for device-based input.  
**AR** Augmented Reality [More info](AROverview.html)  
See in [Glossary](Glossary.html#AR), MR | XR Origin (AR) | **XR Origin (AR)** | [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/) | Serves as the tracking origin for hand-held AR applications. Includes controller GameObjects. This option is available if you have the XR Interaction Toolkit installed.  
AR | XR Origin (Mobile AR) | **XR Origin (Mobile AR)** | [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/) | Serves as the tracking origin for hand-held AR applications. Does not include controller GameObjects. This option is replaced with **XR Origin (AR)** if you have the XR Interaction Toolkit installed.  
  
**Notes:**

  * In the latest versions of the Unity XR packages, the **XR Rig** has been replaced with the **XR Origin**.
  * The `XROrigin` component also replaces the `CameraOffset` component, providing additional settings. Refer to [XR Origin component](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.2/manual/xr-origin-reference.html) for more information.
  * The **AR Session Origin** configuration has been replaced with **XR Origin (Mobile AR)** and **XR Origin (AR)** in [AR Foundation 5.0+](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/).
  * The **XR Origin (Mobile AR)** and **XR Origin (AR)** configurations are not compatible with earlier versions of the AR Foundation package.

[](xr-input-overview.html)

XR input options

[](xr-plugin-management.html)

XR Plug-in Management settings

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

