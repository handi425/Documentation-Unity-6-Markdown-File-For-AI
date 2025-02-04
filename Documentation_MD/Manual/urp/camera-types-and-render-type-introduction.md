[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/camera-types-and-render-type-introduction.html)
  * [中文](/cn/current/Manual/urp/camera-types-and-render-type-introduction.html)
  * [日本語](/ja/current/Manual/urp/camera-types-and-render-type-introduction.html)
  * [한국어](/kr/current/Manual/urp/camera-types-and-render-type-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/camera-types-and-render-type-introduction.html)
  * [中文](/cn/current/Manual/urp/camera-types-and-render-type-introduction.html)
  * [日本語](/ja/current/Manual/urp/camera-types-and-render-type-introduction.html)
  * [한국어](/kr/current/Manual/urp/camera-types-and-render-type-introduction.html)

  * [Working in Unity](../working-in-unity.html)
  * [Cameras](../Cameras.html)
  * [Cameras in URP](../urp/urp-cameras-landing.html)
  * [Camera render types in URP](../urp/camera-types-and-render-type.html)
  * Introduction to camera render types in URP

[](../urp/camera-types-and-render-type.html)

Camera render types in URP

[](../urp/camera-types-and-render-type-change.html)

Change the render type of a camera in URP

# Introduction to camera render types in URP

There are two types of **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) in the Universal **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP):

  * A Base Camera is a general purpose Camera that renders to a render target (a screen, or a [Render Texture](https://docs.unity3d.com/Manual/class-RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture)).

  * An Overlay Camera renders on top of another Camera’s output. You can combine the output of a Base Camera with the output of one or more Overlay Cameras. This is called [Camera stacking](camera-stacking.html).

## Base Camera

Base Camera is the default type of Camera in URP. A Base Camera is a general
purpose Camera that renders to a given render target.

To render anything in URP, you must have at least one Base Camera in your
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene). You can have multiple Base Cameras
in a scene. You can use a Base Camera on its own, or you can use it in a
[Camera stack](camera-stacking.html). For more information on working with
multiple Cameras in URP, refer to [Working with multiple cameras](cameras-
multiple.html).

When you have an active Base Camera in your scene, this icon appears next to
the Camera **Gizmo** A graphic overlay associated with a GameObject in a
Scene, and displayed in the Scene View. Built-in scene tools such as the move
tool are Gizmos, and you can create custom Gizmos using textures or scripting.
Some Gizmos are only drawn when the GameObject is selected, while other Gizmos
are drawn by the Editor regardless of which GameObjects are selected. [More
info](../GizmosMenu.html#GizmosIcons)  
See in [Glossary](../Glossary.html#Gizmo) in the **Scene view** An interactive
view into the world you are creating. You use the Scene View to select and
position scenery, characters, cameras, lights, and all other types of Game
Object. [More info](../UsingTheSceneView.html)  
See in [Glossary](../Glossary.html#SceneView):

![Overlay Camera icon](../../uploads/urp/camera-icon-base.png) Overlay Camera
icon

For information on the properties that Unity exposes in the **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) for a Base Camera, refer to the
[Camera component reference](camera-component-reference.html).

## Overlay Camera

An Overlay Camera is a Camera that renders its view on top of another Camera’s
output. You can use Overlay Cameras to create effects such as **3D objects** A
3D GameObject such as a cube, terrain or ragdoll. [More
info](../GameObjects.html)  
See in [Glossary](../Glossary.html#3DObject) in a 2D **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](../UI-system-compare.html)  
See in [Glossary](../Glossary.html#UI), or a cockpit in a vehicle.

You must use Overlay Cameras in conjunction with one or more Base Cameras
using the [Camera Stacking](camera-stacking.html) system. You cannot use
Overlay Cameras on their own. An Overlay Camera that is not part of a Camera
Stack does not perform any steps of its render loop, and is known as an orphan
Camera.

**Note:** In this version of URP, Overlay Cameras and Camera Stacking are
supported only when using the Universal Renderer.

When you have an active Overlay Camera in your scene, this icon appears next
to the Camera Gizmo in the Scene view:

![Overlay Camera icon](../../uploads/urp/camera-icon-overlay.png) Overlay
Camera icon

The Base Camera in a Camera Stack determines most of the properties of the
Camera Stack. Because you can only use Overlay Cameras in a Camera Stack, URP
uses only the following properties of an Overlay Camera when rendering the
scene:

  * Projection
  * FOV Axis
  * Field of View
  * Physical Camera properties
  * Clipping planes
  * Renderer
  * Clear Depth
  * Render Shadows
  * Culling Mask
  * Occlusion Culling

Unity hides all of the other unused properties in the Inspector. You can
access unused properties using a script, but any changes you make to these
unused properties will not affect the visual output of any Camera Stacks that
use the Overlay Camera.

**Note:** While you can apply **post-processing** A process that improves
product visuals by applying filters and effects before the image appears on
screen. You can use post-processing effects to simulate physical camera and
film properties, for example Bloom and Depth of Field. [More
info](../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../Glossary.html#post-processing) to an individual Overlay
Camera within a camera stack, the effects also apply to all the outputs the
camera stack renders before the Overlay Camera. This is different to how you
can apply post-processing to an individual Base Camera where the effects on
only apply to the Base Camera.

For information on the properties that Unity exposes in the Inspector of an
Overlay Camera, refer to the [Camera component reference](camera-component-
reference.html).

[](../urp/camera-types-and-render-type.html)

Camera render types in URP

[](../urp/camera-types-and-render-type-change.html)

Change the render type of a camera in URP

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

