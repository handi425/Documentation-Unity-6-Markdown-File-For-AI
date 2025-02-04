[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-Tree-LOD.html)
  * [中文](/cn/current/Manual/terrain-Tree-LOD.html)
  * [日本語](/ja/current/Manual/terrain-Tree-LOD.html)
  * [한국어](/kr/current/Manual/terrain-Tree-LOD.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-Tree-LOD.html)
  * [中文](/cn/current/Manual/terrain-Tree-LOD.html)
  * [日本語](/ja/current/Manual/terrain-Tree-LOD.html)
  * [한국어](/kr/current/Manual/terrain-Tree-LOD.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * Tree level of detail (LOD)

[](SpeedTreeImporter-Materials.html)

Materials tab

[](terrain-Tree-Colliders.html)

Add collision to trees

# Tree level of detail (LOD)

Trees from Tree Editor and trees from SpeedTree handle their level of detail
(LOD) differently.

## SpeedTree

A SpeedTree **Prefab** An asset type that allows you to store a GameObject
complete with components and properties. The prefab acts as a template from
which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) has an LODGroup component. Refer to
[LOD](LevelOfDetail.html)The _Level Of Detail_ (LOD) technique is an
optimization that reduces the number of triangles that Unity has to render for
a GameObject when its distance from the Camera increases. [More
info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) and [LOD Group](class-LODGroup.html)A
component to manage level of detail (LOD) for GameObjects. [More info](class-
LODGroup.html)  
See in [Glossary](Glossary.html#LODGroup) for more information about
configuring LOD components.

## Tree Editor

Tree Editor trees don’t have an LODGroup component. Unity’s LOD system uses a
2D to 3D transition zone to blend 2D **billboards** A textured 2D object that
rotates so that it always faces the Camera. [More info](class-
BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) with 3D tree models. This prevents
a sudden popping of 2D and 3D trees, which is important for realism in **VR**
Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR).

**Note** : Billboard trees don’t receive local lighting such as Point Lights
and Spot Lights. They work with directional lights, but lighting on the
billboards updates only when you rotate the **camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera).

Tree Editor controls LOD at two levels:

  * The tree root node.
  * Individual branch groups, as a multiplier of the tree **root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](Glossary.html#Rootnode)’s LOD.

The leaves and bark **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) also have LOD defaults. These are
built-in shaders, and you can’t edit them.

Each **Terrain** The landscape in your scene. A Terrain GameObject adds a
large flat plane to your scene and you can use the Terrain’s Inspector window
to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) tile has settings for tree drawing,
such as the distance from the camera where trees switch to billboard mode.
These settings can impact the gaming experience when they create transitions
that are visible to the player. Refer to the [Terrain Settings
reference](terrain-OtherSettings.html) for more information.

## Additional resources

  * [Create trees with Tree Editor](class-Tree.html)
  * [Terrain Settings reference](terrain-OtherSettings.html)
  * [Import trees from SpeedTree](SpeedTree-landing.html)

[](SpeedTreeImporter-Materials.html)

Materials tab

[](terrain-Tree-Colliders.html)

Add collision to trees

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

