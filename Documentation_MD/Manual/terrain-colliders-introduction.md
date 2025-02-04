[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-colliders-introduction.html)
  * [中文](/cn/current/Manual/terrain-colliders-introduction.html)
  * [日本語](/ja/current/Manual/terrain-colliders-introduction.html)
  * [한국어](/kr/current/Manual/terrain-colliders-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-colliders-introduction.html)
  * [中文](/cn/current/Manual/terrain-colliders-introduction.html)
  * [日本語](/ja/current/Manual/terrain-colliders-introduction.html)
  * [한국어](/kr/current/Manual/terrain-colliders-introduction.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider shapes](collider-shapes.html)
  * [Terrain colliders](terrain-colliders.html)
  * Introduction to Terrain colliders

[](terrain-colliders.html)

Terrain colliders

[](class-TerrainCollider.html)

Terrain collider component reference

# Introduction to Terrain colliders

[Terrain colliders](class-TerrainCollider.html)A terrain-shaped collider
component that handles collisions for collision surface with the same shape as
the Terrain object it is attached to. [More info](class-TerrainCollider.html)  
See in [Glossary](Glossary.html#TerrainCollider) match the shape of a
[Terrain](script-Terrain.html)The landscape in your scene. A Terrain
GameObject adds a large flat plane to your scene and you can use the Terrain’s
Inspector window to create a detailed landscape. [More info](terrain-
UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) exactly, for extremely accurate
Terrain **collision** A collision occurs when the physics engine detects that
the colliders of two GameObjects make contact or overlap, when at least one
has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) simulation. The Terrain
**collider** An invisible shape that is used to handle physical collisions for
an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) is the most accurate collider type
for Terrains.

![A Terrain GameObject. Right: A Terrain collider, which matches the geometry
of the Terrain GameObject exactly.](../uploads/Main/terrain-colliders-
terrain.png) A Terrain GameObject. Right: A Terrain collider, which matches
the geometry of the Terrain GameObject exactly. ![A Terrain collider, which
matches the geometry of the Terrain GameObject
exactly.](../uploads/Main/terrain-colliders-terrain-collider.png) A Terrain
collider, which matches the geometry of the Terrain GameObject exactly.

## Construction of a Terrain collider

Unlike [primitive colliders](primitive-colliders.html) and [Mesh
colliders](mesh-colliders.html)A free-form collider component which accepts a
mesh reference to define its collision surface shape. [More info](class-
MeshCollider.html)  
See in [Glossary](Glossary.html#MeshCollider), Terrain colliders are
heightmap-based. PhysX generates Terrain colliders from the **heightmap** A
greyscale Texture that stores height data for an object. Each pixel stores the
height difference perpendicular to the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) data of the corresponding Terrain,
rather than from a pre-defined shape or a **Mesh** The main graphics primitive
of Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh).

For detailed information on heightmap-based colliders in PhysX, see the Nvidia
PhysX documentation [Geometry: Height
Fields](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Manual/Geometry.html#height-
Fields).

The Terrain collider builds its collision geometry to match the heightmap data
of the assigned [TerrainData](../ScriptReference/TerrainData.html) asset,
including its shape, position and scale. The benefit of this is that you can
make the shape of the collider exactly the same as the shape of the visible
Terrain, which creates more precise and realistic collisions.

## Colliders for Terrain Trees and Details

A Terrain has two **brush** types that add **Prefabs** An asset type that
allows you to store a GameObject complete with components and properties. The
prefab acts as a template from which you can create new object instances in
the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) to the Terrain: **Trees** and
**Details**. These brushes allow you to quickly add trees, bushes, rocks, and
other terrain details. For more detailed information, see Terrain
documentation on [Brushes](class-Brush.html), [Trees](terrain-Trees.html)A
GameObject and associated Component that allows you to add tree assets to your
Scene. You can add branch levels and leaves to trees in the Tree Inspector
window. [More info](class-Tree.html)  
See in [Glossary](Glossary.html#Tree), and [Grass and other details](terrain-
Grass.html).

When you create a Prefab, you add any colliders you want to that Prefab. When
you use a Tree Brush to apply that Prefab to the Terrain, you need to use the
Terrain collider to enable or disable those colliders. On the Terrain
collider, use **Enable Tree Colliders** to toggle Tree Prefab colliders.

![A Terrain and four trees.](../uploads/Main/terrain-colliders-terrain-
trees.png) A Terrain and four trees. ![The collision geometry of the Terrain.
Note the rectangular colliders around the bottom of each tree trunk. These are
present because the original tree model Prefab contains a Box
collider.](../uploads/Main/terrain-colliders-terrain-trees-collider.png) The
collision geometry of the Terrain. Note the rectangular colliders around the
bottom of each tree trunk. These are present because the original tree model
Prefab contains a Box collider.

The Terrain collider only generates colliders for Prefabs that you add with
the Tree Brush. It does not generate colliders for Prefabs that you add with
the Details Brush, because the Details Brush only renders a Prefab’s Mesh, and
not its colliders. If you want something on the Terrain **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to have a collider, use the Trees
brush to add it.

Unity only generates Tree Prefab colliders at runtime, so they only appear in
the [Physics Debug](PhysicsDebugVisualization.html) collider Geometry view at
runtime.

## Optimize Terrain colliders

The Terrain collider is the correct collider choice for a Terrain in almost
all cases. Terrain colliders accurately represent the shape of the Terrain,
enabling precise **collision detection** An automatic process performed by
Unity which determines whether a moving GameObject with a Rigidbody and
collider component has come into contact with any other colliders. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection) between the Terrain and
other colliders. Terrain colliders also require minimal setup and
configuration time, because Unity automatically generates them when you create
a Terrain.

If you are looking for opportunities to improve performance, you can try an
alternative approach to Terrain collisions only if the Terrain has large flat
areas, or if the physics collision does not need to be very accurate. The
following sections describe two alternative approaches.

### Use a lower resolution Terrain collider

You can create a TerrainData with a lower resolution, and apply it to the
Terrain collider.

Duplicate the Terrain’s existing TerrainData, and reduce the resolution. Set
the TerrainData field of the Terrain collider to the reduced resolution
TerrainData.

Note that Unity displays a warning on the Terrain **Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) that the collider and terrains have
different TerrainDatas, but you can ignore this as long as you’ve done it
intentionally.

### Create a Mesh collider from the Terrain:

You can export the Terrain’s heightmap and use external software to turn it
into a simplified [Mesh collider](mesh-colliders.html).

Install the [Terrain
Tools](https://docs.unity3d.com/Packages/com.unity.terrain-tools@latest)
package. Use the [Export
Heightmap](https://docs.unity3d.com/Packages/com.unity.terrain-
tools@latest?subfolder=/manual/toolbox-export-heightmaps.html) tool to export
the Terrain heightmap. Use 3D modeling software to create a mesh from the
heightmap. Use 3D modeling software to run a mesh simplification routine on
the mesh. Import the mesh back into Unity to use as the source for a mesh
collider.

[](terrain-colliders.html)

Terrain colliders

[](class-TerrainCollider.html)

Terrain collider component reference

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

