[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-changedensity.html)
  * [中文](/cn/current/Manual/urp/probevolumes-changedensity.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-changedensity.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-changedensity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-changedensity.html)
  * [中文](/cn/current/Manual/urp/probevolumes-changedensity.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-changedensity.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-changedensity.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Configure the size and density of Adaptive Probe Volumes

[](../urp/probevolumes-showandadjust.html)

Display Adaptive Probe Volumes

[](../urp/probevolumes-usebakingsets.html)

Bake multiple scenes together with Baking Sets

# Configure the size and density of Adaptive Probe Volumes

Refer to [Understanding Adaptive Probe Volumes](probevolumes-concept.html) for
more information about how Adaptive Probe Volumes work.

## Change the size

To ensure the Universal **Render Pipeline** A series of operations that take
the contents of a Scene, and displays them on a screen. Unity lets you choose
from pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) considers static
geometry from all loaded scenes when it places **Light Probes** Light probes
store information about how light passes through space in your scene. A
collection of light probes arranged within a given space can improve lighting
on moving objects and static LOD scenery within that space. [More
info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe), set **Mode** to **Global** in
the Adaptive Probe Volume **Inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) window so the Adaptive Probe
Volume covers the entire **scene** A Scene contains the environments and menus
of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

You can also do one of the following in the Inspector of an Adaptive Probe
Volume, to set the size of an Adaptive Probe Volume:

  * Set **Mode** to **Local** and set the size manually.
  * Set **Mode** to **Local** and select **Fit to all Scenes** , **Fit to Scene** , or **Fit to Selection**. Refer to [Adaptive Probe Volume Inspector reference](probevolumes-inspector-reference.html) for more information.
  * To exclude certain **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) when URP calculates Light Probe
positions, enable **Override Renderer Filters**. For more information about
Layers, refer to [Layers and Layer
Masks](https://docs.unity3d.com/Manual/layers-and-layermasks.html).

You can use multiple Adaptive Probe Volumes in a single scene, and they can
overlap. However in a Baking Set, URP creates only a single Light Probe
structure. trouble

### Resize

To resize the Adaptive Probe Volume, use one of the handles of the box
**gizmo** A graphic overlay associated with a GameObject in a Scene, and
displayed in the Scene View. Built-in scene tools such as the move tool are
Gizmos, and you can create custom Gizmos using textures or scripting. Some
Gizmos are only drawn when the GameObject is selected, while other Gizmos are
drawn by the Editor regardless of which GameObjects are selected. [More
info](../GizmosMenu.html#GizmosIcons)  
See in [Glossary](../Glossary.html#Gizmo) in the **Scene view** An interactive
view into the world you are creating. You use the Scene View to select and
position scenery, characters, cameras, lights, and all other types of Game
Object. [More info](../UsingTheSceneView.html)  
See in [Glossary](../Glossary.html#SceneView). You can’t resize an Adaptive
Probe Volume by changing the **Transform component** A Transform component
determines the Position, Rotation, and Scale of each object in the scene.
Every GameObject has a Transform. [More info](../class-Transform.html)  
See in [Glossary](../Glossary.html#TransformComponent) of the GameObject, or
using the scale gizmo.

In this screenshot, a red box indicates the box gizmo handles.

![The resize handles for Adaptive Probe Volumes.](../../uploads/urp/probe-
volumes/ProbeVolume-Size-gizmo.png)  

## Adjust Light Probe density

You might need to do the following in your project:

  * Increase Light Probe density in highly detailed scenes or areas such as interiors, to get a good lighting result.
  * Decrease Light Probe density in empty areas, to avoid those areas using disk space and increasing bake time unnecessarily.

In the [Inspector for an Adaptive Probe Volume](probevolumes-inspector-
reference.html), enable and adjust **Override Probe Spacing** to set a minimum
and maximum density for the Light Probes in the Adaptive Probe Volume.

The values can’t exceed the **Min Probe Spacing** or **Max Probe Spacing**
values in the **Probe Placement** section of the [Adaptive Probe Volumes
panel](probevolumes-lighting-panel-reference.html), so you might need to
adjust these values first.

You can also add local Adaptive Probe Volumes in different areas with
different **Override Probe Spacing** values, to control Light Probe density
more granularly. For example, in empty areas, add a local Adaptive Probe
Volume with a higher **Override Probe Spacing** minimum value, to make sure
Light Probes have a lower density in those areas.

If you increase Light Probe density, you might increase bake time and how much
disk space your Adaptive Probe Volume uses.

### Decrease Light Probe density for terrain

Because **terrain** The landscape in your scene. A Terrain GameObject adds a
large flat plane to your scene and you can use the Terrain’s Inspector window
to create a detailed landscape. [More info](../terrain-UsingTerrains.html)  
See in [Glossary](../Glossary.html#Terrain) is detailed but less important
than your main scenery or characters, you can do the following:

  1. Put terrain on its own [Layer](https://docs.unity3d.com/Manual/layers-and-layermasks.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](../Layers.html)  
See in [Glossary](../Glossary.html#Layer).

  2. Surround the terrain with an Adaptive Probe Volume.
  3. In the Inspector for the Adaptive Probe Volume, enable **Override Renderer Filters** , then in ****Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](../Layers.html)  
See in [Glossary](../Glossary.html#LayerMask)** select only your terrain
Layer.

  4. To adjust Light Probe density to capture more or less lighting detail, enable **Override Probe Spacing** and adjust the values.

[](../urp/probevolumes-showandadjust.html)

Display Adaptive Probe Volumes

[](../urp/probevolumes-usebakingsets.html)

Bake multiple scenes together with Baking Sets

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

