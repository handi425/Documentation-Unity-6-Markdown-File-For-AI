[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SpeedTreeImporter-Model.html)
  * [中文](/cn/current/Manual/SpeedTreeImporter-Model.html)
  * [日本語](/ja/current/Manual/SpeedTreeImporter-Model.html)
  * [한국어](/kr/current/Manual/SpeedTreeImporter-Model.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SpeedTreeImporter-Model.html)
  * [中文](/cn/current/Manual/SpeedTreeImporter-Model.html)
  * [日本語](/ja/current/Manual/SpeedTreeImporter-Model.html)
  * [한국어](/kr/current/Manual/SpeedTreeImporter-Model.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Import trees from SpeedTree](SpeedTree-landing.html)
  * [SpeedTree Import Settings window](class-SpeedTreeImporter.html)
  * Model tab

[](class-SpeedTreeImporter.html)

SpeedTree Import Settings window

[](SpeedTreeImporter-Materials.html)

Materials tab

# Model tab

Use the **Model** tab to change the model settings for imported SpeedTree
assets.

To change materials settings for the [SpeedTree](SpeedTree.html) model, see
the [Materials tab](SpeedTreeImporter-Materials.html).

![SpeedTree Importer Model tab](../uploads/Main/class-SpeedTreeImporter-
Model.png) SpeedTree Importer Model tab

The **Model** tab has these sections:

**(A)** The Meshes, MaterialAn asset that defines how a surface should be
rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material), Lighting, Additional Settings, and
Wind sections allow you to adjust global import settings for the model.

**(B)** The LODThe _Level Of Detail_ (LOD) technique is an optimization that
reduces the number of triangles that Unity has to render for a GameObject when
its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) section has a specialized variation of
the [LOD Group](class-LODGroup.html)A component to manage level of detail
(LOD) for GameObjects. [More info](class-LODGroup.html)  
See in [Glossary](Glossary.html#LODGroup) component for importing SpeedTree
models. You can set smooth transitions between LOD levels, adjust thresholds
for each LOD level, and use the level-specific LOD options to turn off
resource-heavy effects.

**(C)** The **Revert** and **Apply** options always appear, but you can only
select them after you make changes to the import settings. If you change
settings in the [Remapped Materials](SpeedTreeImporter-
Materials.html#remapped) section of the **Materials** tab, the **Apply &
Generate Materials** option appears.

**(D)** The properties for the **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) (read-only) appear at the bottom
of the ****Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** view, including a preview of the
SpeedTree Model.

## Meshes

**Property** | **Description**  
---|---  
**Unit Conversion** | Apply a global scale to the imported SpeedTree model. The default setting is **ft to m** because the SpeedTree Modeler uses feet and Unity uses meters as world units.  
| **Leave As Is** | Don’t apply any unit conversion. Interpret the values in the **model file** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#Modelfile) as meters.  
| **ft to m** | Convert from feet to meters.  
| **cm to m** | Convert from centimeters to meters.  
| **inch to m** | Convert from inches to meters.  
| **Custom** | Apply a user-specified scale factor to the model.  
**Scale Factor** | Scale the model by a custom value. This property is visible only when **Unit Conversion** is set to **Custom**.  
  
## Material

**Property** | **Description**  
---|---  
**Main Color** | Choose a color to modulate the diffuse lighting component.  
**Color Variation** | Enable color variation for the model. This property uses **Main Color** and **Variation Color (RGB) Intensity (A)** along with the model’s world position to pick the final color. Color variation helps add a more natural look to clusters of SpeedTree models.  
**Variation Color (RGB), Intensity (A)** | Choose the color and intensity used in the **Color Variation** process. This property is visible only when **Color Variation** is enabled.  
****Normal Map** A type of Bump Map texture that allows you to add surface
detail such as bumps, grooves, and scratches to a model which catch the light
as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap)** | Enable **Bump maps** An image texture used to represent geometric detail across the surface of a mesh, for example bumps and grooves. Can be represented as a heightmap or a normal map. [More info](StandardShaderMaterialParameterNormalMap.html)  
See in [Glossary](Glossary.html#Bumpmap) on the model.  
**Subsurface Scattering** | Enable subsurface scattering effects. This **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) effect simulates the light scattered
out the back side of leaves and other two-sided SpeedTree materials.  
  
## Lighting

**Property** | **Description**  
---|---  
**Cast Shadows** | Let the model cast shadows on its environment when directly lit by a light source.  
**Receive Shadows** | Let the model receive shadows from other GameObjects in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).  
****Light Probes** Light probes store information about how light passes
through space in your scene. A collection of light probes arranged within a
given space can improve lighting on moving objects and static LOD scenery
within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe)** | Enable Light Probes rendering for the model.  
  
## Additional Settings

**Property** | **Description**  
---|---  
**Motion Vectors** | Set the **Motion Vector** property for the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer of each LOD GameObject. For
details about the motion vector rendering options, refer to the [Mesh Renderer
component](class-MeshRenderer.html#additional-settings).  
**Generate**Colliders** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider)** | Generate **mesh colliders** A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html)  
See in [Glossary](Glossary.html#MeshCollider) for the model. This property is
available only for .st9 files.  
  
## Wind

The following options are available for .spm or .st files.

To adjust wind for .st9 files, refer to the [Wind tab](SpeedTreeImporter-
Wind.html).

**Property** | **Description**  
---|---  
**Wind Quality** | Choose the level of wind quality to use for this asset. Options with more wind effects have a higher performance cost.  
| **None** | No wind effects.  
| **Fastest** | Global sway is applied to the model.  
| **Fast** | Global sway and leaf ripple are applied to the model.  
| **Better** | Global sway, branch motion, and leaf ripple are applied to the model.  
| **Best** | Global sway, branch motion, leaf ripple, and leaf tumbling are applied to the model.  
| **Palm** | Global sway, branch motion, leaf ripple, leaf tumbling, and frond ripple are applied to the model.  
  
## LOD

**Note** : This section assumes you have already read the documentation on the
[LOD Group](class-LODGroup.html) component. The section on [Working with
SpeedTree Models](class-LODGroup.html#SpeedTreeModels) explains key concepts
and workflow information that are crucial for understanding how to import
SpeedTree models.

The LOD Group component for the SpeedTree Importer is different from the
generic LOD Group component that appears on a SpeedTree instance in Unity:

  * **Fade Mode** options aren’t available because the **Fade Mode** is already set to **Speed Tree**.
  * The playhead for the preview is missing because you can only preview the LOD transitions when an instance of the model is placed in the scene.
  * The options governing the LOD transitions are the same as the LOD Group component, with the only difference being the **Smooth Transitions** property. Enable **Smooth Transitions** to reveal the other properties for LOD transition animations: **Animate Cross-fading** , **Crossfade Width** , and **Fade Out Width**.
  * Each LOD level has its own set of options that allow you to enable or disable resource-heavy effects.

### The LOD Group selection bar

The LOD Group selection bar represents the different LOD levels as colored
boxes. When a level box is selected, a blue outline appears around it:

![The LOD Group selection bar](../uploads/Main/SpeedTreeImporterModel-
selectionbar.png) The LOD Group selection bar

The percentage that appears in each LOD level box represents the threshold at
which that level becomes active, based on the ratio of the GameObject’s screen
space height to the total screen height.

To select a level, click on the level box. To change the percentage value for
a level, drag the boundary to the left or right of the level container. You
can also customize which properties are enabled or disabled on each level as
an optimization strategy.

### Level-specific LOD options

For each LOD level defined on your SpeedTree asset, you can customize a
variety of properties. The properties correspond to other settings in the
**Model** tab and override global import settings.

To set LOD options on a specific LOD level, select the LOD level box on the
LOD Group selection bar and enable **Customize LOD options**.

![The level-specific LOD Options](../uploads/Main/class-SpeedTreeImporter-
Model_LOD_CustomizeLodOptions.png) The level-specific LOD Options

When you enable customization for an LOD level, the SpeedTree Importer
generates a new material for that LOD level.

**Note** : Customized LOD levels negatively affect batching and instancing and
increase memory consumption. But customizations can help with some GPU
bottleneck scenarios if you disable shader-heavy effects for an LOD level.
[Profile](Profiler.html) your scene for CPU and GPU before and after you
customize to see the impact on performance.

### Billboard LODs

Billboards are treated differently from other LOD meshes:

  * If **billboards** A textured 2D object that rotates so that it always faces the Camera. [More info](class-BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) are available in the SpeedTree
model, customizations are automatically enabled.

  * Some resource-heavy properties such as **Light Probes** and **Wind** are disabled by default or have reduced value range for performance reasons.

[](class-SpeedTreeImporter.html)

SpeedTree Import Settings window

[](SpeedTreeImporter-Materials.html)

Materials tab

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

