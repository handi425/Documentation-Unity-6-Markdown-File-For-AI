[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/prepare-mesh-for-mesh-collider.html)
  * [中文](/cn/current/Manual/prepare-mesh-for-mesh-collider.html)
  * [日本語](/ja/current/Manual/prepare-mesh-for-mesh-collider.html)
  * [한국어](/kr/current/Manual/prepare-mesh-for-mesh-collider.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/prepare-mesh-for-mesh-collider.html)
  * [中文](/cn/current/Manual/prepare-mesh-for-mesh-collider.html)
  * [日本語](/ja/current/Manual/prepare-mesh-for-mesh-collider.html)
  * [한국어](/kr/current/Manual/prepare-mesh-for-mesh-collider.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider shapes](collider-shapes.html)
  * [Mesh colliders](mesh-colliders.html)
  * Prepare a Mesh for Mesh colliders

[](mesh-colliders-introduction.html)

Introduction to Mesh colliders

[](class-MeshCollider.html)

Mesh collider component reference

# Prepare a Mesh for Mesh colliders

Mesh **colliders** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) require a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)’s [Mesh](mesh.html)The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) to be properly configured so that
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) are accurate.

## Allow read and write access to a Mesh

There are particular configurations and optimizations that require a Mesh to
be read/write enabled. For details on what “read/write” means in this context,
refer to documentation on the Mesh API property
[`Mesh.isReadable`](../ScriptReference/Mesh-isReadable.html).

A Mesh must be read/write enabled if any of the following circumstances are
true:

  * The attached **Mesh collider** A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html)  
See in [Glossary](Glossary.html#MeshCollider)’s Transform has negative scaling
(for example, (–1, 1, 1)) and the Mesh is convex.

  * The attached Mesh collider’s Transform is skewed or sheared (for example, when a rotated Transform has a scaled parent Transform).
  * The Mesh collider’s **Cooking Options** (see Configure Mesh cooking) are set to any value other than the default (that is, everything enabled except **None**).

### Make a Mesh read/write enabled

To make a Mesh read/write enabled, the Mesh must have a `Mesh.isReadable`
value of `true`. To apply this via the Editor:

  1. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), select the **model file** A
file containing a 3D data, which may include definitions for meshes, bones,
animation, materials and textures. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#Modelfile) (for example, the FBX file) that
contains the Mesh.

  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), select **Model**.

  3. In the **Meshes** section, enable **Read/Write**.

## Configure Mesh cooking

To calculate collisions with a Mesh collider, the physics system needs to be
able to access the Mesh’s geometry. “Mesh cooking” refers to the process of
converting a 3D mesh from its original format (for example, FBX or OBJ) into a
format that the physics system can read. The cooking process takes the raw
Mesh data and builds spatial search structures so that Unity can respond to
physics queries more quickly.

You can trigger Mesh cooking in the Import Settings (**Import Settings** >
**Model** > **Generate Colliders**) or at run time.

### Optimize Mesh cooking at run time

During the Mesh cooking process, Unity can apply various optimizations to
reduce the size and complexity of the Mesh (for example: removing redundant
vertices, merging overlapping triangles, or simplifying the geometry to reduce
the number of triangles). Unity can then load the optimized mesh more quickly
and efficiently, which reduces memory use and improves overall performance.

To control which optimizations run, use the Mesh collider’s **Cooking
Options** property (which corresponds to the C# enum
[`MeshColliderCookingOptions`](../ScriptReference/MeshColliderCookingOptions.html)).
For an overview of the different cooking options available, see the [Mesh
collider component reference](class-MeshCollider.html).

The default **Cooking Options** are suitable for any Mesh collider that you
cook in the Editor and never re-cook at run time. They are also suitable for
most Mesh colliders that you need at run time (particularly large or
complicated Meshes that only need to cook once). However, you might need to
alter the **Cooking Options** to make collider generation faster if you need
to rapidly generate collision geometry at run time (for example, procedural
surfaces, or Mesh colliders that deform in response to player behaviour).

To optimize Mesh cooking for Meshes that Unity generates at run time, you can
disable the data cleaning steps (**Enable Mesh Cleaning** , and **Weld Co-
Located Vertices**). However, if you disable the data cleaning steps, you must
have another way to validate your Mesh data, to ensure you aren’t using data
that those algorithms would otherwise clean.

  * If **Enable Mesh Cleaning** is disabled, you must ensure that the Mesh has no degenerate triangles (for example, thin triangles where the points are collinear, or triangles with an area close to zero or infinity).
  * If **Weld Colocated Vertices** is disabled, you must ensure that the Mesh has no co-located vertices (that is, multiple vertices existing in the same location).

You can also disable **Cook For Faster Simulation** to save memory usage.

When you change the **Cooking Options** , you need to apply read/write
permission to the Mesh. For guidance on how to do this, see Allow read and
write access to a Mesh.

## Optimize non-rendered Meshes

If a Mesh only needs to provide data for physics calculations and not for
rendering (for example, for invisible colliders), you don’t need to import the
Mesh’s normals. Meshes without normals require less memory and use less disk
space.

To disable normals:

  1. In the Project window, select the Mesh.
  2. In the Inspector’s Import settings, select **Model**.
  3. Navigate to the Geometry section and set **Normals** to **None**.

[](mesh-colliders-introduction.html)

Introduction to Mesh colliders

[](class-MeshCollider.html)

Mesh collider component reference

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

