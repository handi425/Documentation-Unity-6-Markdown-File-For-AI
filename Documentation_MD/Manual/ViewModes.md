[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ViewModes.html)
  * [中文](/cn/current/Manual/ViewModes.html)
  * [日本語](/ja/current/Manual/ViewModes.html)
  * [한국어](/kr/current/Manual/ViewModes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ViewModes.html)
  * [中文](/cn/current/Manual/ViewModes.html)
  * [日本語](/ja/current/Manual/ViewModes.html)
  * [한국어](/kr/current/Manual/ViewModes.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * [The Scene view](UsingTheSceneView.html)
  * Scene view View Options overlay

[](SceneVisibility.html)

Scene visibility

[](GizmosMenu.html)

Gizmos menu

# Scene view View Options overlay

You can use the **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view View Options **toolbar** A row of
buttons and basic controls at the top of the Unity Editor that allows you to
interact with the Editor in various ways (e.g. scaling, translation). [More
info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar) [overlay](overlays.html) to choose
various options for viewing the Scene and to enable/disable lighting and
audio. These controls only affect the **Scene view** An interactive view into
the world you are creating. You use the Scene View to select and position
scenery, characters, cameras, lights, and all other types of Game Object.
[More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) during development and have no
effect on the built game.

![](../uploads/Main/SceneViewControlBar.png)

## Draw mode menu

The first dropdown menu selects which **Draw Mode** will be used to depict the
Scene. The available options are:

**Draw Mode** |  | **Function**  
---|---|---  
**Shading Mode** |  |   
| Shaded | Show surfaces with their textures visible.  
| Wireframe | Draw meshes with a wireframe representation.  
| Shaded Wireframe | Show meshes textured and with wireframes overlaid.  
**Miscellaneous** |  |   
| Shadow Cascades | Show directional light [shadow cascades](shadow-cascades.html).  
| Render Paths | Show the [rendering path](RenderingPaths.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) for each GameObject using a
color code:  
  
Blue indicates [deferred shading](RenderTech-DeferredShading.html)A rendering
path in the Built-in Render Pipeline that places no limit on the number of
Lights that can affect a GameObject. All Lights are evaluated per-pixel, which
means that they all interact correctly with normal maps and so on.
Additionally, all Lights can have cookies and shadows. [More info](RenderTech-
DeferredShading.html)  
See in [Glossary](Glossary.html#Deferredshading)  
Yellow indicates [forward rendering](RenderTech-ForwardRendering.html)A
rendering path that renders each object in one or more passes, depending on
lights that affect the object. Lights themselves are also treated differently
by Forward Rendering, depending on their settings and intensity. [More
info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering)  
Red indicates [vertex lit](RenderTech-VertexLit.html)  
| Alpha Channel | Render colors with alpha.  
| Overdraw | Render **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) as transparent “silhouettes”. The
transparent colors accumulate, making it easy to spot places where one object
is drawn over another.  
| Mipmaps | Show ideal texture sizes using a color code:   
  
Red indicates that the texture is larger than necessary (at the current
distance and resolution)  
Blue indicates that the texture might be larger. The ideal texture sizes
depend on the resolution at which your application will run and how close the
Camera can get to particular surfaces.  
| Texture Mipmap Streaming | Tint GameObjects green, red, or blue, depending on their status in the [Texture Mipmap Streaming](TextureStreaming.html) system. For more information, see documentation on [Mipmap Streaming debugging](TextureStreaming-API#DebuggingAPI).  
| **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites
are essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) Mask | Sprite Masks are used to either hide or reveal parts of a Sprite or group of Sprites. See [Sprite Masks](sprite/mask/mask-landing.html)A texture which defines which areas of an underlying image to reveal or hide. [More info](sprite/mask/mask-landing.html)  
See in [Glossary](Glossary.html#SpriteMask) for more information.  
**Deferred** |  | These modes let you view each of the elements of the G-buffer (**Albedo** , **Specular** , **Smoothness** and **Normal**) in isolation. See documentation on [Deferred Shading](RenderTech-DeferredShading.html) for more information.  
**Global Illumination** |  | The following modes are available to help visualize aspects of the [Global Illumination](lighting-window.html)A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) system: **Systems** ,
**Clustering** , **Lit Clustering** , **UV Charts** , and
**Contributors/Receivers**. See documentation on [GI
Visualisations](GIVis.html) for information about each of these modes.  
**Realtime Global Illumination** |  | The following modes are available to help visualize aspects of the [Enlighten Realtime Global Illumination](realtime-gi-using-enlighten.html) system: **Albedo** , **Emissive** , **Indirect** , and **Directionality**. See documentation on [GI Visualisations](GIVis.html) for information about each of these modes.  
**Baked Global Illumination** |  | The following modes are available to help visualize aspects of the Baked Global Illumination system: **Baked Light Map** , **Directionality** , ****Shadowmask** A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#Shadowmask)**, **Albedo** , **Emissive** ,
**UV Charts** , **Texel Validity** , **UV Overlap** , **Baked**Lightmap** A
pre-rendered texture that contains the effects of light sources on static
objects in the scene. Lightmaps are overlaid on top of scene geometry to
create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) Culling**, **Lightmap Indices** ,
and **Light Overlap**. See documentation on [GI Visualisations](GIVis.html)
for information about each of these modes.  
**Material Validator** |  | There are two **Material Validator** modes: **Albedo** and **Metal Specular**. These allow you to check whether your physically-based materials use values within the recommended ranges. See [Physically Based Material Validator](MaterialValidator.html) for more information.   
  
## 2D, lighting and Audio switches

To the right of the **Render Mode** menu are three buttons that switch certain
Scene view options on or off:

  * **2D** : switches between 2D and 3D view for the Scene. In 2D mode the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) is oriented looking towards positive
z, with the x-axis pointing right and the y-axis pointing up.

  * **Lighting** : turns Scene view lighting (lights, object shading, etc) on or off.
  * **Audio** : turns Scene view **audio effects** Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](class-AudioEffectMixer.html)  
See in [Glossary](Glossary.html#AudioEffect) on or off.

## Effects button and menu

The menu (activated by the icon to the right of the **Audio** button) has
options to enable or disable rendering effects in the Scene view.

  * **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox): a skybox texture rendered in the
Scene’s background

  * **Clouds** : Shows cloud layers and volumetric clouds. Only available when using a SRP that supports clouds.
  * **Fog** A post-processing effect that overlays a color onto objects depending on the distance from the camera. Use this to simulate fog or mist in outdoor environments, or to hide clipping of objects near the camera’s far clip plane. [More info](PostProcessingOverview.html)  
See in [Glossary](Glossary.html#Fog): gradual fading of the view to a flat
color with distance from the camera.

  * **Flares** : **lens flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](class-LensFlare.html)  
See in [Glossary](Glossary.html#LensFlare) on lights.

  * **Always Refresh** : Defines whether animated materials display the animation. When selected, any time-based effects (for example, Shaders) will animate. For example, Scene effects (like grass waving on a Terrain).
  * **Post Processing** : Shows [Post-processing](PostProcessingOverview.html)A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effects.

  * **Particle Systems** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem): Shows [Particle
System](ParticleSystems.html) effects.

The **Effects** button itself acts as a switch that enables or disables all
the selected effects at once.

## Scene visibility switch

The Scene visibility switch toggles Scene visibility for GameObjects on and
off. When it’s on, Unity applies the Scene visibility settings. When it’s off,
Unity ignores them.

For more information, refer to the documentation on [Scene
Visibility](SceneVisibility.html).

## Layers menu

Select which layers display in the Scene view from the
[Layers](Layers.html)Layers in Unity can be used to selectively opt groups of
GameObjects in or out of certain processes or calculations. This includes
camera rendering, lighting, physics collisions, or custom calculations in your
own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#Layer) dropdown menu.

## Camera settings menu

The Camera settings menu contains options for configuring the Scene view
camera. For more information, refer to the documentation on [Camera
settings](SceneViewCamera.html).

## Gizmos menu

The **Gizmos** A graphic overlay associated with a GameObject in a Scene, and
displayed in the Scene View. Built-in scene tools such as the move tool are
Gizmos, and you can create custom Gizmos using textures or scripting. Some
Gizmos are only drawn when the GameObject is selected, while other Gizmos are
drawn by the Editor regardless of which GameObjects are selected. [More
info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) menu contains options for how objects,
icons, and gizmos are displayed. This menu is available in both the Scene view
and the [Game view](GameView.html). Refer to documentation on the [Gizmos
Menu](GizmosMenu.html) manual page for more information.

## Additional resources

  * [Overlays](overlays.html)
  * [Display or hide an overlay](display-and-hide-overlay.html)
  * [Layers](Layers.html)

[](SceneVisibility.html)

Scene visibility

[](GizmosMenu.html)

Gizmos menu

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

