[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AROverview.html)
  * [中文](/cn/current/Manual/AROverview.html)
  * [日本語](/ja/current/Manual/AROverview.html)
  * [한국어](/kr/current/Manual/AROverview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AROverview.html)
  * [中文](/cn/current/Manual/AROverview.html)
  * [日本語](/ja/current/Manual/AROverview.html)
  * [한국어](/kr/current/Manual/AROverview.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Overview](xr-support-landing.html)
  * AR development in Unity

[](xr-meta-quest.html)

Meta Quest

[](VROverview.html)

VR development in Unity

# AR development in Unity

Augmented Reality (AR) involves a new set of design challenges compared to
**VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) or traditional real-time 3D applications.
By definition, an _augmented_ reality app overlays its content on the real
world around the user. To place an object in the real world, you must first
determine where to place for it. For example, you may want to place a virtual
painting on a physical wall. If you place a virtual potted plant, you may want
it on a physical table or the floor. An **AR** app receives information about
the world from the user’s device, such as the locations of planar surfaces,
the detection of objects, people, faces, and so on; and must decide how to use
this information to create a good experience for the user.

When you open a typical AR **scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) in Unity, you will not find many **3D
objects** A 3D GameObject such as a cube, terrain or ragdoll. [More
info](GameObjects.html)  
See in [Glossary](Glossary.html#3DObject) in the scene or the Hierarchy view.
Instead, most **GameObjects** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the scene define the settings
and logic of the app. 3D content is typically created as **prefabs** An asset
type that allows you to store a GameObject complete with components and
properties. The prefab acts as a template from which you can create new object
instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) that are added to the scene at runtime
in response to AR-related events.

![A typical AR scene in Unity](../uploads/Main/xr-ar-scene.png)  
  
_A typical AR scene in the Unity Editor_

## Basic AR scene elements

A basic AR scene contains the following GameObjects and components:

  * **AR Session** GameObject 
    * [AR Session component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/session.html)
    * [AR Input Manager component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARInputManager.html)
  * ****XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) Origin (Mobile AR)** GameObject

    * [XR Origin component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARSessionOrigin.html)
    * ****Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) Offset** GameObject

      * [AR Camera Manager component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/Camera/camera-components.html#ar-camera-manager-component)
      * [AR Camera Background component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/Camera/camera-components.html#ar-camera-background-component)

If you have the [XR Interaction
Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/)
installed, the XR Origin option for AR applications changes to **XR Origin
(AR)** , which adds GameObjects for representing hand-held controllers and the
toolkit components needed for interaction with objects in the scene.

  * **XR Origin (AR)** GameObject 
    * [XR Origin component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARSessionOrigin.html)
    * **Camera Offset** GameObject 
      * [AR Camera Manager component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/Camera/camera-components.html#ar-camera-manager-component)
      * [AR Camera Background component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/Camera/camera-components.html#ar-camera-background-component)
      * **LeftHand/RightHand Controller** GameObjects 
        * [XR Controller (Action-based) component](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/xr-controller-action-based.html)
        * [XR Ray Interactor component](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/xr-ray-interactor.html)
        * [Line Renderer component](class-LineRenderer.html)
        * [XR Interactor Line Visual component](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/xr-interactor-line-visual.html)
        * [Sorting Group component](sprite/sorting-group/sorting-group-landing.html)

**Tips:**

  * Use the **GameObject > XR** menu to add these GameObjects and their associated components to a scene. (You can also open the menu by right-clicking in the **Hierarchy** window.)
  * You should never have more than one active **XR Origin** in a scene.

In addition to these session GameObjects, you need the corresponding [AR
manager](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/architecture/managers.html#trackables-
and-trackable-managers) component for each type of AR feature that your
application uses.

Refer to [Set up an XR scene](xr-scene-setup.html) for an overview of how to
set up any XR scene.

Refer to the [AR
Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/index.html)
package documentation, including [Scene set
up](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/project-
setup/scene-setup.html) for more in-depth information on creating AR
applications.

## AR packages

To build AR apps in Unity, you can install the [AR
Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/)
package along with the XR provider **plug-ins** A set of code created outside
of Unity that creates functionality in Unity. There are two kinds of plug-ins
you can use in Unity: Managed plug-ins (managed .NET assemblies created with
tools like Visual Studio) and Native plug-ins (platform-specific native code
libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) for the devices you want to support.
To develop AR/**MR** Mixed Reality  
See in [Glossary](Glossary.html#MR) apps for the Apple Vision Pro device, you
also need the [PolySpatial visionOS
packages](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest).
Unity provides additional packages, including Unity Mars and the XR
Interaction Toolkit to make it easier and faster to develop AR experiences.

### AR provider plug-ins

The AR provider plug-ins supported by Unity include:

  * [Apple ARKit XR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.arkit@6.0) on iOS
  * [Apple visionOS XR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.visionos@latest) on visionOS
  * [Google ARCore XR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.arcore@6.0) on Android
  * [OpenXR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.10/manual/index.html) for any AR device with an OpenXR runtime, including HoloLens 2 and others.

Use the XR Plug-in Management system to add and enable one or more of these
plug-ins. Refer to [XR Project set up](configuring-project-for-xr.html) for
instructions.

**Note:** Depending on the platform or device, you might need to install
additional packages along with OpenXR. For example, to build an AR app for
HoloLens 2, you must install the Microsoft’s [Mixed Reality OpenXR
Plugin](https://learn.microsoft.com/en-us/windows/mixed-
reality/develop/unity/mixed-reality-openxr-plugin).

### AR Foundation

The [AR
Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/)
package supports AR development in Unity.

AR Foundation enables you to create multiplatform AR apps with Unity. In an AR
Foundation project, you choose which AR features to enable by adding the
corresponding manager components to your scene. When you build and run your
app on an AR device, AR Foundation enables these features using the platform’s
native AR SDK, so you can create once and deploy to the world’s leading AR
platforms.

A device can be AR-capable without supporting all possible AR features.
Available functionality depends on both the device platform and the
capabilities of the specific device. For example, ARCore, Google’s AR platform
for Android, does not currently support body tracking, so body tracking can’t
be used when you build your app for the Android platform. Even on the same
platform, capabilities can vary from device to device. For example, a specific
device model might support AR through its world-facing camera, but not its
user-facing camera.

For more information about AR Foundation, refer to the [AR Foundation package
documentation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/).

### PolySpatial visionOS packages

Augmented and **mixed reality** Mixed Reality (MR) combines its own virtual
environment with the user’s real-world environment and allows them to interact
with each other.  
See in [Glossary](Glossary.html#MixedReality) development for the Apple Vision
Pro device relies on a set of packages that implement the Unity PolySpatial
architecture on the visionOS platform.

The PolySpatial architecture splits a Unity game or app into two logical
pieces: a simulation controller and a presentation view. The simulation
controller drives all of the app-specific logic, such as MonoBehaviours and
other scripting, **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) behavior, asset management, physics, and
so on. Almost all of your game’s behavior is part of the simulation. The
presentation view handles both input and output, which includes rendering to
the display and other forms of output, such as audio. The view sends input
received from the operating system – including pinch gestures and head
position – to the simulation for processing each frame. After each simulation
step, the view updates the display by rendering **pixels** The smallest unit
in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) to the screen, submitting audio buffers
to the system, etc.

On the visionOS platform, the simulation part runs in a Unity Player, while
the presentation view is rendered by Apple’s RealityKit. For every visible
object in the simulation, a corresponding object exists in the RealityKit
scene graph.

**Note:** PolySpatial is only used for augmented and mixed reality on the
Apple Vision Pro. **Virtual reality** Virtual Reality (VR) immerses users in
an artificial 3D world of realistic images and sounds, using a headset and
motion tracking. [More info](VROverview.html)  
See in [Glossary](Glossary.html#VirtualReality) and windowed apps run in a
Unity Player that also controls rendering (using the Apple Metal graphics
API).

### Unity Mars

[Unity Mars](https://docs.unity3d.com/Packages/com.unity.mars@latest/)
provides purpose-built authoring tools and better workflows for creating AR
applications.

  * **Plain-language authoring:** You can define simple rules that can be stated in plain language like, “on every horizontal surface, create grass,” to specify how your app content should augment a scene based on the AR features detected by a user’s device.
  * **Proxy-based workflow:** you add proxies to a scene to represent real-world AR features. You can set conditions and actions on your proxies to specify how your app should respond when a matching object is detected in the real world. For example, you can add a proxy to a scene that activates whenever a suitable horizontal plane is detected.
  * **In-Editor simulation:** Unity Mars provides a simulation mode, along with pre-built sample environments, that helps you test your AR logic inside the Editor.
  * **Customizable building-blocks:** Unity Mars contains templates and other building blocks for creating all or part of an AR application. For example, the Training Template provides UI and logic that you can use to build an AR tutorial that walks a trainee through a series of steps.

Unity Mars requires a compatible license. The Unity Pro, Unity Enterprise, and
Unity Industrial Collection plans include Mars. You can also obtain a license
for Unity Mars separately if you have a different plan. Refer to [Unity
Mars](https://unity.com/products/unity-mars) for more information.

### XR Interaction Toolkit

The [Unity XR Interaction
Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/)
provides tools for building both AR and VR interactions. The AR functionality
provided by the XR Interaction Toolkit includes:

  * AR gesture system to map screen touches to gesture events
  * AR placement Interactable component to help place virtual objects in the real world
  * AR gesture Interactor and Interactable components to support object manipulations such as place, select, translate, rotate, and scale
  * AR annotations to inform users about AR objects placed in the real world

[](xr-meta-quest.html)

Meta Quest

[](VROverview.html)

VR development in Unity

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

