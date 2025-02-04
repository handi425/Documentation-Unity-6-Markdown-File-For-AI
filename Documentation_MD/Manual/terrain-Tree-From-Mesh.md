[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-Tree-From-Mesh.html)
  * [中文](/cn/current/Manual/terrain-Tree-From-Mesh.html)
  * [日本語](/ja/current/Manual/terrain-Tree-From-Mesh.html)
  * [한국어](/kr/current/Manual/terrain-Tree-From-Mesh.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-Tree-From-Mesh.html)
  * [中文](/cn/current/Manual/terrain-Tree-From-Mesh.html)
  * [日本語](/ja/current/Manual/terrain-Tree-From-Mesh.html)
  * [한국어](/kr/current/Manual/terrain-Tree-From-Mesh.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](class-Tree.html)
  * Create trees and leaves from meshes

[](tree-FirstTree.html)

Design a tree

[](terrain-Tree-Performance.html)

Performance tips for trees

# Create trees and leaves from meshes

You can base a Tree Editor tree or its leaves on meshes that you have imported
into Unity.

Working with an imported **mesh** The main graphics primitive of Unity. Meshes
make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) isn’t the same as working with
SpeedTree. For more information about importing from SpeedTree, refer to
[Import trees from SpeedTree](SpeedTree-landing.html).

## Import a mesh

To learn about exporting models from a 3D modeling application and importing
them into Unity, refer to [Models](models.html)A 3D model representation of an
object, such as a character, a building, or a piece of furniture. [More
info](3D-formats.html)  
See in [Glossary](Glossary.html#Model).

The mesh you want to use needs to be in the `Ambient-Occlusion` folder the
trees are in. For more information, refer to [Shaders and the Ambient-
Occlusion folder](terrain-Trees-Mat-Shaders.html).

## Use a mesh for the tree

A Tree Editor tree has a **Mesh Filter** A mesh component that takes a mesh
from your assets and passes it to the Mesh Renderer for rendering on the
screen. [More info](class-MeshFilter.html)  
See in [Glossary](Glossary.html#MeshFilter) component that can reference your
imported mesh.

To assign your imported mesh to the tree:

  1. In the **Inspector** window > **Tree Hierarchy** view, select either the root node or one of the branch groups.
  2. In the **Mesh (Mesh Filter)** component, select the mesh picker (circle).
  3. In the **Select** Mesh window, select the mesh you want to use.

When you use an imported mesh, you can’t add leaves or branches to the tree.

## Use a mesh for the leaves

You can use the leaf group’s mesh geometry mode to use an imported mesh. It
can be flowers, fruit, or any other object you want to attach to the tree.

Note that the mesh’s transform must be `0,0,0`. Any other transform is added
as a distance from the tree, so the object floats by the tree instead of being
attached to the branches. Hide the original mesh from the **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) to avoid seeing it at the `0,0,0`
location.

## Additional resources

  * [Tree level of detail (LOD)](terrain-Tree-LOD.html)
  * [Shaders and the Ambient-Occlusion folder](terrain-Trees-Mat-Shaders.html)
  * [Tree Hierarchy view UI reference](terrain-Tree-Hierarchy-UI.html)
  * [Root node reference](tree-Root-Node.html)
  * [Branch group reference](tree-Branches.html)
  * [Leaf group reference](tree-Leaves.html)
  * [Terrain Settings reference](terrain-OtherSettings.html)

[](tree-FirstTree.html)

Design a tree

[](terrain-Tree-Performance.html)

Performance tips for trees

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

