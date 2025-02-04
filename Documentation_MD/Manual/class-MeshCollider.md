[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-MeshCollider.html)
  * [中文](/cn/current/Manual/class-MeshCollider.html)
  * [日本語](/ja/current/Manual/class-MeshCollider.html)
  * [한국어](/kr/current/Manual/class-MeshCollider.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-MeshCollider.html)
  * [中文](/cn/current/Manual/class-MeshCollider.html)
  * [日本語](/ja/current/Manual/class-MeshCollider.html)
  * [한국어](/kr/current/Manual/class-MeshCollider.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider shapes](collider-shapes.html)
  * [Mesh colliders](mesh-colliders.html)
  * Mesh collider component reference

[](prepare-mesh-for-mesh-collider.html)

Prepare a Mesh for Mesh colliders

[](wheel-colliders.html)

Wheel colliders

# Mesh collider component reference

[Switch to Scripting](../ScriptReference/MeshCollider.html "Go to MeshCollider
page in the Scripting Reference")

The ****Mesh** The main graphics primitive of Unity. Meshes make up a large
part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) **collider** An invisible shape that is
used to handle physical collisions for an object. A collider doesn’t need to
be exactly the same shape as the object’s mesh - a rough approximation is
often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider)** takes a [Mesh Asset](class-
Mesh.html) and builds a collider that matches the geometry of that Mesh. It is
more accurate for **collision** A collision occurs when the physics engine
detects that the colliders of two GameObjects make contact or overlap, when at
least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection than using primitives,
and is a better option for complicated Meshes.

Mesh colliders that are marked as **Convex** can collide with other **Mesh
colliders**.

**Property** | **Description**  
---|---  
**Convex** | Enable the checkbox to make the Mesh collider collide with other Mesh colliders. **Convex** Mesh colliders are limited to 255 triangles.  
**Is Trigger** | Enable **Is Trigger** to use the collider as a trigger for events. When **Is Trigger** is enabled, other colliders pass through this collider, and trigger the messages [`OnTriggerEnter`](../ScriptReference/Collider.OnTriggerEnter.html), [`OnTriggerStay`](../ScriptReference/Collider.OnTriggerStay.html), and [`OnTriggerExit`](../ScriptReference/Collider.OnTriggerExit.html).  
**Provides Contacts** | Enable **Provides Contacts** to generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages [`OnCollisionEnter`](../ScriptReference/Collider.OnCollisionEnter.html), [`OnCollisionStay`](../ScriptReference/Collider.OnCollisionStay.html), or [`OnCollisionExit`](../ScriptReference/Collider.OnCollisionExit.html). When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default.  
**Cooking Options** | Enable or disable the Mesh cooking options that affect how the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#PhysicsEngine) processes Meshes. When you set
the **Cooking Options** to any other value than the default settings (that is,
everything enabled except **None**), the Mesh collider must use a Mesh that
has an [`isReadable`](../ScriptReference/Mesh-isReadable.html) value of
`true`. For details on Mesh cooking, refer to [Prepare a Mesh for Mesh
colliders](prepare-mesh-for-mesh-collider.html).  
| **None** | Disables all **Cooking Options**. This is disabled by default.  
| **Everything** | Enables all **Cooking Options**. This is enabled by default.  
| **Cook for Faster Simulation** | The cooking process preprocesses the Mesh data and stores it in memory to speed up run time calculations at run time. This is particularly useful for complex Meshes in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). When this setting is disabled, the
physics engine uses a faster cooking time, but retrieves the mesh data more
slowly at run time. This is enabled by default.  
| **Enable Mesh Cleaning** | The cooking process attempts to clear the Mesh of degenerate triangles on the Mesh (that is, triangles in which all three points are collinear, and do not form a triangle shape) and other geometrical artifacts. This results in a Mesh that is better suited for use in **collision detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection), and tends to produce more
accurate contact points. When this setting is disabled, the physics engine
uses a faster cooking time but implements less optimization. This is enabled
by default.  
| **Weld Colocated Vertices** | The cooking process combines vertices that have the same position. This results in a Mesh that is better suited for use in collision detection, and tends to produce more accurate contact points. When this setting is disabled, the physics engine uses a faster cooking time but implements less optimization. This is enabled by default.  
| **Use Fast Midphase** | The cooking process uses the fastest mid-phase acceleration structure and algorithm available for your output platform. The fastest algorithm doesn’t require any R-Trees for spatial access. If you encounter midphase issues at runtime, disable this option; Unity then uses the slower legacy midphase algorithm instead. This is enabled by default.  
**Material** | Reference to the [Physics Material](class-PhysicsMaterial.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](class-PhysicsMaterial.html)  
See in [Glossary](Glossary.html#PhysicsMaterial) that determines how this
collider interacts with others.  
**Mesh** | Reference to the Mesh to use for collisions.  
  
## Layer overrides

The Layer Overrides section provides properties that allow you to override the
project-wide [Layer-based collision detection](LayerBasedCollision.html)
settings for this collider.

**Property** | **Description**  
---|---  
**Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.   
For example, if a collider with a **Layer Override Priority** of 1 collides
with a Collider with a **Layer Override Priority** of 2, the physics system
uses the settings for the Collider with the **Layer Override Priority** of 2.  
**Include Layers** | Choose which Layers to include in collisions with this collider.  
**Exclude Layers** | Choose which Layers to exclude in collisions with this collider.  
  
[](prepare-mesh-for-mesh-collider.html)

Prepare a Mesh for Mesh colliders

[](wheel-colliders.html)

Wheel colliders

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

