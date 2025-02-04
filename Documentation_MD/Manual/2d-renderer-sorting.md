[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-renderer-sorting.html)
  * [中文](/cn/current/Manual/2d-renderer-sorting.html)
  * [日本語](/ja/current/Manual/2d-renderer-sorting.html)
  * [한국어](/kr/current/Manual/2d-renderer-sorting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-renderer-sorting.html)
  * [中文](/cn/current/Manual/2d-renderer-sorting.html)
  * [日本語](/ja/current/Manual/2d-renderer-sorting.html)
  * [한국어](/kr/current/Manual/2d-renderer-sorting.html)

  * [Working in Unity](working-in-unity.html)
  * [2D in Unity](Unity2D.html)
  * 2D renderer sorting

[](2d-game-art-syle-reference.html)

2D game art style reference

[](sprite/sprite-landing.html)

Sprites

# 2D renderer sorting

## Overview

Unity sorts Renderers according to a priority order that depends on their
types and usages. You can specify the render order of Renderers through their
[Render Queue](SL-SubShaderTags.html). In general, there are two main queues:
the [Opaque queue](../ScriptReference/Rendering.RenderQueue.Geometry.html) and
the [Transparent
queue](../ScriptReference/Rendering.RenderQueue.Transparent.html). 2D
Renderers are mainly within the Transparent queue, and include the [Sprite
Renderer](sprite/renderer/renderer-landing.html)A component that lets you
display images as Sprites for use in both 2D and 3D scenes. [More
info](sprite/renderer/renderer-landing.html)  
See in [Glossary](Glossary.html#SpriteRenderer), [Tilemap
Renderer](tilemaps/work-with-tilemaps/tilemap-renderer-reference.html), and
[Sprite Shape Renderer](sprite/shape-renderer/shape-renderer-landing.html)
types.

## Transparent Queue Sorting Order by Priority

2D Renderers within the Transparent Queue generally follow the priority order
below:

  1. Sorting Layer and Order in Layer

  2. Specify Render Queue

  3. Distance to Camera

     * Perspective
     * Orthographic
     * Custom Axis sort mode
     * Sprite Sort Point
  4. Sorting Group

  5. Material/Shader

  6. Tiebreaker

There are other factors which can cause the sorting order to differ from the
regular priority order. These factors vary from project to project.

## Sorting Layer and Order in Layer

The [Sorting Layer](https://docs.unity3d.com/Manual/class-
TagManager.html#SortingLayers) and **Order in Layer** (in the Renderer’s
**Property** settings) are available to all 2D Renderers through the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window or via the Unity Scripting
API. Set the Renderer to an existing **Sorting Layer** or create a new one to
determine its priority in the rendering queue. Change the value of the **Order
in Layer** to set the Renderer’s priority among other Renderers within the
same **Sorting Layer**.

## Specify Render Queue

You can specify the Render Queue type of the Renderer in its Material settings
or in the **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) settings of its Material. This is
useful for grouping and sorting Renderers which are using different Materials.
Refer to documentation on [ShaderLab: SubShader Tags](SL-SubShaderTags.html)
for more details.

## Distance to Camera

The [Camera component](class-Camera.html) sorts Renderers based on its
**Projection** setting. The two options are **Perspective** and
**Orthographic**.

### Perspective

In this mode, the sorting distance of a Renderer is the direct distance of the
Renderer from the **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)’s position.

### Orthographic

The sorting distance of a Renderer is the distance between the position of the
Renderer and the Camera along the Camera’s view direction. For the default 2D
setting, this is along the (0, 0, 1) axis.

When you set the Camera component to **Perspective** or **Orthographic,**
Unity automatically sets the Camera’s
[TransparencySortMode](../ScriptReference/TransparencySortMode.html) to match
the selected mode. You can set the Transparency Sort Mode manually in two
ways:

  * Open the ****Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings)** and go to [Graphics](class-
GraphicsSettings.html#Camera), then under **Camera Settings** use Transparent
Sort Mode

  * Set the Camera’s [TransparencySortMode](../ScriptReference/TransparencySortMode.html) via the Scripting API.

The Camera **Transparency Sort Mode** settings are under the **Graphics**
category in the **Project Settings** (main menu: **Edit** > **Project
Settings** > **Graphics**). When this is set to **Default** , a Camera
component’s Projection setting take priority. When this is set to an option
other than **Default** , the Camera component’s Projection setting remains the
same, but the Camera’s **Transparency Sort Mode** changes to that option.

An additional option available through the Project settings and via the
Scripting API is the [Custom Axis sort
mode](../ScriptReference/TransparencySortMode.CustomAxis.html).

### Custom Axis sort mode

Select this mode to sort Renderers based on their distance along the custom
axis you set in the Project settings (main menu: **Edit** > **Project
Settings** > **Graphics** > **Transparency Sort Axis**). This is commonly used
in projects with [Isometric Tilemaps](tilemaps/work-with-tilemaps/isometric-
tilemaps/isometric-tilemap-landing.html) to sort and render the Tile Sprites
correctly on the Tilemap. Refer to [Creating an Isometric
Tilemap](tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-
tilemap.html) for further information.

**Note:** If your project is a 2D Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP) project, the
**Transparency Sort Mode** isn’t available in the **Project Settings** , and
is instead configured in the 2D Renderer asset properties. Refer to the
[Configure the 2D Renderer Asset
documentation](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/manual/2DRendererData-
overview.html) for more information.

### Sprite Sort Point

By default, a **Sprite** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite)’s **[Sort Point](sprite/renderer/set-
sort-point-sprite.html)** is set to its **Center** , and Unity measures the
distance between the camera’s Transform position and the Center of the Sprite
to determine their render order during sorting. An alternate option is to set
a Sprite’s **Sort Point** to its **Pivot** position in World Space. Select the
**Pivot** option in the Sprite’s [Sprite Renderer](sprite/renderer/renderer-
landing.html) property settings and edit the Sprite’s Pivot position in the
[Sprite Editor](sprite/sprite-editor/sprite-editor-landing.html).

## Sorting Group

The [Sorting Group](sprite/sorting-group/sorting-group-landing.html) is a
component that groups Renderers which share a common root together for sorting
purposes. All Renderers within the same Sorting Group share the same **Sorting
Layer, Order in Layer,** and **Distance to Camera**. Refer to documentation on
the [Sorting Group](sprite/sorting-group/sorting-group-landing.html) component
and its settings for more details.

## Material/Shader

Unity sorts Renderers with the same [Material settings](Shaders.html) together
for more efficient rendering performance, such as with [dynamic
batching](DrawCallBatching.html)An automatic Unity process which attempts to
render multiple meshes as if they were a single mesh for optimized graphics
performance. The technique transforms all of the GameObject vertices on the
CPU and groups many similar vertices together. [More
info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching).

## Tiebreaker

When multiple Renderers have identical sorting priority, the tiebreaker is the
order that Unity places the Renderers in the Render Queue. Because this is an
internal process that you have no control over, you should use the sorting
options (such as **Sorting Layers** and **Sorting Groups**) to make sure all
Renderers have distinct sorting priorities.

[](2d-game-art-syle-reference.html)

2D game art style reference

[](sprite/sprite-landing.html)

Sprites

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

