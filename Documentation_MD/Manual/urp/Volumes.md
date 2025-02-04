[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/Volumes.html)
  * [中文](/cn/current/Manual/urp/Volumes.html)
  * [日本語](/ja/current/Manual/urp/Volumes.html)
  * [한국어](/kr/current/Manual/urp/Volumes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/Volumes.html)
  * [中文](/cn/current/Manual/urp/Volumes.html)
  * [日本語](/ja/current/Manual/urp/Volumes.html)
  * [한국어](/kr/current/Manual/urp/Volumes.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Volumes in URP](../urp/volumes-landing-page.html)
  * Understand volumes in URP

[](../urp/volumes-landing-page.html)

Volumes in URP

[](../urp/set-up-a-volume.html)

Set up a volume in URP

# Understand volumes in URP

The Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) uses volumes for
[post-processing](add-post-processing.html)A process that improves product
visuals by applying filters and effects before the image appears on screen.
You can use post-processing effects to simulate physical camera and film
properties, for example Bloom and Depth of Field. [More
info](../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../Glossary.html#post-processing) effects. Volumes can
override or extend **scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) properties depending on the
**camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) position relative to each volume.

You can create the following dedicated volume **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject):

  * Global Volume
  * Box Volume
  * Sphere Volume
  * Convex **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](../mesh.html)  
See in [Glossary](../Glossary.html#Mesh) Volume

You can also add a Volume component to any GameObject. A scene can contain
multiple GameObjects with Volume components. You can add multiple Volume
components to a GameObject.

At runtime, URP goes through all the enabled Volume components attached to
active GameObjects in the scene, and determines each volume’s contribution to
the final scene settings. URP uses the camera position and the Volume
component properties to calculate the contribution. URP interpolates values
from all volumes with a non-zero contribution to calculate the final property
values.

## Global and local volumes

There are two types of volume:

  * Global volumes affect the camera everywhere in the scene.
  * Local volumes affect the camera only if the camera is near the bounds of the **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](../CollidersOverview.html)  
See in [Glossary](../Glossary.html#Collider) on the parent GameObject.

Refer to [Set up a volume](set-up-a-volume.html) for more information.

## Volume Profiles and Volume Overrides

Each Volume component references a Volume Profile, which contains scene
properties in one or more Volume Overrides. Each Volume Override controls
different settings.

![Vignette post-processing effect in the URP Template
SampleScene](../../uploads/urp/post-proc/post-proc-as-volume-override.png) A
GameObject with a global volume. The Volume Profile has **Vignette** and
****Tonemapping** The process of remapping HDR values of an image into a range
suitable to be displayed on screen. [More
info](../PostProcessingOverview.html)  
See in [Glossary](../Glossary.html#Tonemapping)** Volume Overrides.

Refer to the following for more information:

  * [Create a Volume Profile](Volume-Profile.html)
  * [Configure Volume Overrides](VolumeOverrides.html)

## Default volumes

All URP scenes have two default global volumes:

  * The Default Volume for your whole project, which uses the Volume Profile set in **Project Settings** > **Graphics** > **URP** > **Default Volume Profile**.
  * The global volume for the active quality level, which uses the Volume Profile set in the active [URP Asset](universalrp-asset.html) > **Volumes** > **Volume Profile**.

URP evaluates the default volumes only when you first load a scene or when you
change the [quality level](https://docs.unity3d.com/Manual/class-
QualitySettings.html), instead of every frame. If you use only the default
volumes in a scene, URP has less work to do at runtime.

URP sets the default volumes to the lowest priority, so any volume you add to
a scene overrides them.

Refer to the following for more information:

  * [Configure the Default Volume](set-up-a-volume.html#configure-the-default-volume)
  * [Configure the global volume for a quality level](set-up-a-volume.html#configure-the-global-volume-for-a-quality-level)

[](../urp/volumes-landing-page.html)

Volumes in URP

[](../urp/set-up-a-volume.html)

Set up a volume in URP

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

