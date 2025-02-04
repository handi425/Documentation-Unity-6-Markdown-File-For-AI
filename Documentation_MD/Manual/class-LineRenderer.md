[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-LineRenderer.html)
  * [中文](/cn/current/Manual/class-LineRenderer.html)
  * [日本語](/ja/current/Manual/class-LineRenderer.html)
  * [한국어](/kr/current/Manual/class-LineRenderer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-LineRenderer.html)
  * [中文](/cn/current/Manual/class-LineRenderer.html)
  * [日本語](/ja/current/Manual/class-LineRenderer.html)
  * [한국어](/kr/current/Manual/class-LineRenderer.html)

  * [Visual effects](visual-effects.html)
  * [Lines and trails](visual-effects-lines-trails-billboards.html)
  * [Rendering lines](rendering-lines.html)
  * Line Renderer component reference

[](draw-configure-line-3d-space.html)

Draw and configure a line in 3D space

[](rendering-trails.html)

Rendering trails

# Line Renderer component reference

[Switch to Scripting](../ScriptReference/LineRenderer.html "Go to LineRenderer
page in the Scripting Reference")

Explore properties and settings for the **Line Renderer** component reference,
to configure and render a line between points in 3D space.

The Line Renderer component has two sections:

  * Scene Tools panel reference
  * Line Renderer properties reference

## Scene Tools panel reference

The properties in the **Scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) Tools panel change depending on whether
the **Line Renderer Scene Editing Mode** is set to **None** , **Edit Points**
, or **Create Points**.

To set the current Scene Editing Mode, use the **Edit Points** and **Create
Points** buttons.

![Line Renderer Edit Points and Create Points buttons](../uploads/Main/line-
renderer-scene-editing-mode.png) Line Renderer Edit Points and Create Points
buttons

### Scene Editing Mode: None

By default, there is no Scene Editing Mode set.

**Control** | **Description**  
---|---  
**Simplify Preview** | Enable **Simplify Preview** to see a preview of the results of the simplification operation.  
**Tolerance** | Set the amount by which the simplified line can deviate from the original line.  
  
A value of 0 results in no deviation, and therefore little or no
simplification. Higher positive values result in more deviation from the
original line, and therefore more simplification.  
  
The default value is 1.  
**Simplify** | Click **Simplify** to reduce the number of elements in the Line Renderer’s **Positions** array.  
  
The simplification operation uses the [Ramer-Douglas-Peucker
algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm)
to reduce the number of points, based on the **Tolerance** value.  
  
### Scene Editing Mode: Edit Points

To set the Scene Editing Mode to **Edit Points** , select the **Edit Points**
button. Select it again to set the Scene Editing Mode to **None**.

**Control** | **Description**  
---|---  
**Show Wireframe** | When enabled, Unity draws a wireframe in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) that visualizes the line.  
**Subdivide Selected** | This button is enabled when you select two or more adjacent points. Pressing this button inserts a new point between the selected adjacent points.  
  
### Scene Editing Mode: Create Points

To set the Scene Editing Mode to **Create Points** , select the **Create
Points** button. Select it again to set the Scene Editing Mode to **None**.

**Control** | **Description**  
---|---  
**Input** | Set the input method you want to use to create points.  
| **Mouse position** | Create points based on the mouse position in the Scene view.  
| **Physics Raycast** | Create points based on a [raycast](../ScriptReference/Physics.Raycast.html) into the Scene. Unity creates the point at the position where the raycast hits.  
****Layer Mask** A value defining which layers to include or exclude from an
operation, such as rendering, collision or your own code. [More
info](Layers.html)  
See in [Glossary](Glossary.html#LayerMask)** | The layer mask to use when performing a raycast. This property is visible only when **Input** is set to **Physics Raycast**.  
**Min Vertex Distance** | When you drag the mouse to create points in the Scene view, the Line Renderer creates a new point when this distance from the last point is exceeded.  
**Offset** | The offset applied to created points. When **Input** is set to **Mouse Position** , Line Renderer applies the offset from the Scene **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). When Input is set to **Physics
Raycast** , Line Renderer applies the offset from the raycast normal.  
  
## Line Renderer properties reference

This section contains the following sub-sections:

  * Line settings
  * MaterialsAn asset that defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material)

  * Lighting
  * Probes
  * Additional Settings

### Line settings

**Property** | **Function**  
---|---  
**Loop** | Enable this to connect the first and last positions of the line, and form a closed loop.  
**Positions** | The array of Vector3 points to connect.  
**Width** | Define a width value, and a curve value to control the width of your line along its length.  
  
The curve is sampled at each vertex, so its accuracy is limited by the number
of vertices in your line. The overall width of the line is controlled by the
width value.  
**Color** | Define a gradient to control the color of the line along its length.  
  
Unity samples colors from the Color gradient at each vertex. Between each
vertex, Unity applies linear interpolation to colors. Adding more vertices to
your line might give a closer approximation of a detailed gradient.  
**Corner Vertices** | This property dictates how many extra vertices are used when drawing corners in a line. Increase this value to make the line corners appear rounder.  
**End Cap Vertices** | This property dictates how many extra vertices are used to create end caps on the line. Increase this value to make the line caps appear rounder.  
**Alignment** | Set the direction that the line faces.  
| **View** | The line faces the Camera.  
| **TransformZ** | The line faces the Z axis of its **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent).  
**Texture Mode** | Control how the Texture is applied to the line.  
| **Stretch** | Map the texture once along the entire length of the line.  
| **Tile** | Repeat the texture along the line, based on its length in world units. To set the tiling rate, use [Material.SetTextureScale](../ScriptReference/Material.SetTextureScale.html).  
| **DistributePerSegment** | Map the texture once along the entire length of the line, assuming all vertices are evenly spaced.  
| **RepeatPerSegment** | Repeat the texture along the line, repeating at a rate of once per line segment. To adjust the tiling rate, use [Material.SetTextureScale](../ScriptReference/Material.SetTextureScale.html).  
**Shadow Bias** | Set the amount to move shadows away from the Light to remove shadowing artifacts caused by approximating a volume with billboarded geometry.  
**Generate Lighting Data** | If enabled, Unity builds the line geometry with normals and tangents included. This allows it to use Materials that use the Scene lighting.  
**Use World Space** | If enabled, the points are considered as world space coordinates. If disabled, they are local to the transform of the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to which this component is
attached.  
  
### Materials

The **Materials** section lists all the [materials](class-Material.html) that
this component uses.

**Property** | **Description**  
---|---  
**Size** | The number of elements in the material list.  
  
If you decrease the number of elements, Unity deletes the elements at the end
of the list. If you increase the number of elements, Unity adds new elements
to the end of the list. Unity populates new elements with the same material
that the element at the end of the list uses.  
**Element** | The materials in the list. You can assign a material asset to each element.  
  
By default, Unity orders the list alphabetically based on the name of the
materials. This list is reorderable, and Unity updates the number of the
elements automatically as you change their order.  
  
## Lighting

The **Lighting** section contains properties that relate to lighting.

**Property** | **Description**  
---|---  
**Cast Shadows** | Specify if and how this Renderer casts shadows when a suitable [Light](class-Light.html) shines on it.  
  
This property corresponds to the
[Renderer.shadowCastingMode](../ScriptReference/Renderer-
shadowCastingMode.html) API.  
| **On** | This Renderer casts a shadow when a shadow-casting Light shines on it.  
| **Off** | This Renderer does not cast shadows.  
| **Two-sided** | This Renderer casts two-sided shadows. This means that single-sided objects like a plane or a quad can cast shadows, even if the light source is behind the mesh.  
  
For [Baked Global Illumination](class-LightingSettings.html#MixedLighting) or
Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) to support two-sided shadows, the
material must support [Double Sided Global
Illumination](https://docs.unity3d.com/Manual/class-Material.html).  
| **Shadows Only** | This Renderer casts shadows, but the Renderer itself isn’t visible.  
**Receive Shadows** | Specify if Unity displays shadows cast onto this Renderer.  
  
This property only has an effect if you enable [Baked Global
Illumination](class-LightingSettings.html#MixedLighting) or Enlighten
[Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting)
for this scene.  
  
This property corresponds to the
[Renderer.receiveShadows](../ScriptReference/Renderer-receiveShadows.html)
API.  
**Contribute Global Illumination** | Include this Renderer in global illumination calculations, which take place at bake time.  
  
This property only has an effect if you enable [Baked Global
Illumination](class-LightingSettings.html#MixedLighting) or Enlighten
[Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting)
for this scene.  
  
Enabling this property enables the Contribute GI flag in the GameObject’s
[Static Editor Flags](StaticObjects.html). It corresponds to the
[StaticEditorFlags.ContributeGI](../ScriptReference/StaticEditorFlags.ContributeGI.html)
API.  
**Receive Global Illumination** | Whether Unity provides global illumination data to this Renderer from baked lightmaps, or from runtime Light Probes.  
  
This property is only editable if you enable **Contribute Global
Illumination**. It only has an effect if you enable [Baked Global
Illumination](class-LightingSettings.html#MixedLighting) or Enlighten
[Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting)
for this scene.  
  
This property corresponds to the
[MeshRenderer.receiveGI](../ScriptReference/MeshRenderer-receiveGI.html) API.  
| **Lightmaps** | Unity provides global illumination data to this Renderer from lightmaps.  
| **Light Probes** | Unity provides global illumination data to this Renderer from [Light Probes](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) in the scene.  
**Prioritize Illumination** | Enable this property to always include this Renderer in Enlighten Realtime Global Illumination calculations. This ensures that the Renderer is affected by distant emissives, even those which are normally excluded from Global Illumination calculations for performance reasons.  
  
This property is visible only if **Contribute GI** is enabled in the
GameObject’s [Static Editor Flags](StaticObjects.html), your project uses the
Built-in Render Pipeline, and Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) is enabled in your scene.  
  
### Probes

The **Probes** section contains properties relating to [Light
Probe](LightProbes.html) and [Reflection Probes](class-ReflectionProbe.html)A
rendering component that captures a spherical view of its surroundings in all
directions, rather like a camera. The captured image is then stored as a
Cubemap that can be used by objects with reflective materials. [More
info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe).

**Property** | **Description**  
---|---  
**Light Probes** | Set how this Renderer receives light from the [Light Probes](LightProbes.html) system.  
  
This property corresponds to the
[Renderer.lightProbeUsage](../ScriptReference/Renderer-lightProbeUsage.html)
API.  
| **Off** | The Renderer doesn’t use any interpolated Light Probes.  
| **Blend Probes** | The Renderer uses one interpolated Light Probe. This is the default value.  
| **Use Proxy Volume** | The Renderer uses a 3D grid of interpolated Light Probes.  
| **Custom Provided** | The Renderer extracts Light Probe shader uniform values from the [MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html).  
**Proxy Volume Override** | Set a reference to another GameObject that has a Light Probe Proxy Volume component.  
  
This property is only visible when **Light Probes** is set to **Use Proxy
Volume**.  
**Reflection Probes** | Set how the Renderer receives reflections from the [Reflection Probe](class-ReflectionProbe.html) system.  
  
This property corresponds to the
[Renderer.probeAnchor](../ScriptReference/Renderer-probeAnchor.html) API.  
| **Off** | Disables Reflection Probes. Unity uses a skybox for reflection.  
| **Blend Probes** | Enables Reflection Probes. Blending occurs only between Reflection Probes. This is useful in indoor environments where the character may transition between areas with different lighting settings.  
| **Blend Probes and Skybox** | Enables Reflection Probes. Blending occurs between Reflection Probes, or between Reflection Probes and the default reflection. This is useful for outdoor environments.  
| **Simple** | Enables Reflection Probes, but no blending occurs between Reflection Probes when there are two overlapping volumes.  
**Anchor Override** | Set the Transform that Unity uses to determine the interpolation position when using the [Light Probe](LightProbes.html) or [Reflection Probe](class-ReflectionProbe.html) systems. By default, this is the centre of the bounding box of the Renderer’s geometry.  
  
This property corresponds to the
[Renderer.probeAnchor](../ScriptReference/Renderer-probeAnchor.html) API.  
  
### Additional Settings

The **Additional Settings** section contains additional properties.

**Property** | **Description**  
---|---  
**Motion Vectors** | Set whether to use motion vectors to track this Renderer’s per-pixel, screen-space motion from one frame to the next. You can use this information to apply post-processing effects such as motion blur.  
  
**Note:** not all platforms support motion vectors. See
[SystemInfo.supportsMotionVectors](../ScriptReference/SystemInfo-
supportsMotionVectors.html) for more information.  
  
This property corresponds to the
[Renderer.motionVectorGenerationMode](../ScriptReference/Renderer-
motionVectorGenerationMode.html) API.  
| **Camera Motion Only** | Use only Camera movement to track motion.  
| **Per Object Motion** | Use a specific pass to track motion for this Renderer.  
| **Force No Motion** | Do not track motion.  
**Dynamic Occlusion** | When **Dynamic Occlusion** is enabled, Unity’s [occlusion culling](OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) system culls this Renderer
when it is blocked from a Camera’s view by a Static Occluder. Otherwise, the
system does not cull this Renderer when it is blocked from a Camera’s view by
a Static Occluder.  
  
Dynamic Occlusion is enabled by default. Disable it for effects such as
drawing the outline of a character behind a wall.  
**Sorting Layer** | The name of this Renderer’s [Sorting Layer](class-TagManager.html).  
**Order in Layer** | This Renderer’s order within a [Sorting Layer](class-TagManager.html).  
  
LineRenderer

[](draw-configure-line-3d-space.html)

Draw and configure a line in 3D space

[](rendering-trails.html)

Rendering trails

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

