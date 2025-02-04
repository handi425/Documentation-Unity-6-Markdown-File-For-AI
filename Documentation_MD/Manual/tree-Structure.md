[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tree-Structure.html)
  * [中文](/cn/current/Manual/tree-Structure.html)
  * [日本語](/ja/current/Manual/tree-Structure.html)
  * [한국어](/kr/current/Manual/tree-Structure.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tree-Structure.html)
  * [中文](/cn/current/Manual/tree-Structure.html)
  * [日本語](/ja/current/Manual/tree-Structure.html)
  * [한국어](/kr/current/Manual/tree-Structure.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](class-Tree.html)
  * Tree Editor concepts

[](class-Tree.html)

Create trees with Tree Editor

[](terrain-Trees-Mat-Shaders.html)

Shaders and the Ambient-Occlusion folder

# Tree Editor concepts

The Tree Editor tool lets you create trees directly within the Unity Editor.
Use the Tree Editor to create new trees, then use the **Terrain** The
landscape in your scene. A Terrain GameObject adds a large flat plane to your
scene and you can use the Terrain’s Inspector window to create a detailed
landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) system to add the trees to your
world.

For most uses, the SpeedTree Modeler replaces the Tree Editor. For backward
compatibility with content created before SpeedTree was introduced, use Tree
Editor.

## The Tree Hierarchy view

To open the **Tree Hierarchy** view, add a Tree GameObject (**GameObject** >
**3D Object** > **Tree**).

At the top of the tree’s **Inspector** is the **Tree Hierarchy** view, which
shows the tree root node and any branch and leaf groups the tree has. Use the
**Tree Hierarchy** view to add and delete branch and leaf groups, to control
their properties, and to configure the tree.

![Tree Hierarchy view. The first level is the tree root node. Above it is a
branch group, which is connected to the tree root node with a line. There are
four tree editing options on the right, and a recompute button on the
left.](../uploads/Main/TreeStructure.png) Tree Hierarchy view. The first level
is the tree root node. Above it is a branch group, which is connected to the
tree root node with a line. There are four tree editing options on the right,
and a recompute button on the left.

For more information about the Tree Hierarchy view, refer to the [Tree
Hierarchy view UI reference](terrain-Tree-Hierarchy-UI.html).

## Tree levels and groups

The Tree Editor manages branches and leaves in groups, and arranges the groups
in levels.

The tree root doesn’t count as one of the levels, so the first level is the
trunk. Branches growing directly from the trunk are the primary level.
Branches growing from the primary branches are the secondary level. The
branching process continues until the terminal twigs, adding a level each
time.

![A diagram showing tree levels: the first level is the trunk. It has six
primary branches. Each of those branches has four secondary
branches.](../uploads/Main/TreeStructureDiagram.png) A diagram showing tree
levels: the first level is the trunk. It has six primary branches. Each of
those branches has four secondary branches.

A branch group can subdivide into further branch groups. For example, you can
add two branch groups to your trunk, and give each branch group a different
growth angle or its own leaf group.

Leaves are also arranged in groups. Unlike branch groups, leaf groups can’t
further subdivide: you can’t add a leaf or branch group to a leaf group.

For more information about working with branch and leaf groups, refer to
[Design a tree](tree-FirstTree.html). For more information about the Tree
Hierarchy view, refer to the [Tree Hierarchy view UI reference](terrain-Tree-
Hierarchy-UI.html).

## The tree root node

The tree **root node** A transform in an animation hierarchy that allows Unity
to establish consistency between Animation clips for a generic model. It also
enables Unity to properly blend between Animations that have not been authored
“in place” (that is, where the whole Model moves its world position while
animating). [More info](AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](Glossary.html#Rootnode) exposes properties that affect the
entire tree. For example, all branch and leaf groups inherit the ****LOD** The
_Level Of Detail_ (LOD) technique is an optimization that reduces the number
of triangles that Unity has to render for a GameObject when its distance from
the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) Quality** property from the tree root
node, although each branch group can add a multiplier to this value.

For more information about the tree root node, refer to [Root node
reference](tree-Root-Node.html).

## Tree Materials

Trees can have four materials:

  * Leaves.
  * Bark.
  * Cross-section of a broken branch.
  * Fronds.

For information about **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) for these materials, refer to [Shaders
and the Ambient-Occlusion folder](terrain-Trees-Mat-Shaders.html).

## Tree geometry

There are three geometry options for branches:

  * Branch Only.
  * Branch and Fronds.
  * Fronds Only.

Each branch group can have a different geometry option. For example, you can
have a branch group with a Branch Only geometry as the trunk, and a branch
group with Fronds Only geometry as the branches.

To learn more about fronds, refer to [Branch group reference](tree-
Branches.html).

## Additional resources

  * [Shaders and the Ambient-Occlusion folder](terrain-Trees-Mat-Shaders.html)
  * [Performance tips for trees](terrain-Tree-Performance.html)
  * [Tree Hierarchy view UI reference](terrain-Tree-Hierarchy-UI.html)
  * [Root node reference](tree-Root-Node.html)
  * [Branch group reference](tree-Branches.html)
  * [Leaf group reference](tree-Leaves.html)
  * [Terrain Settings reference](terrain-OtherSettings.html)
  * [Mesh Renderer component](class-MeshRenderer.html)

[](class-Tree.html)

Create trees with Tree Editor

[](terrain-Trees-Mat-Shaders.html)

Shaders and the Ambient-Occlusion folder

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

