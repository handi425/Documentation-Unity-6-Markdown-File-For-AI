[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [2D Physics](../../../2d-physics/2d-physics.html)
  * [Collider 2D](../../../2d-physics/collider/collider-2d-landing.html)
  * [Composite Collider 2D](../../../2d-physics/collider/composite-collider/composite-collider-2d-landing.html)
  * Composite Collider 2D component reference

[](../../../2d-physics/collider/composite-collider/composite-
collider-2d-landing.html)

Composite Collider 2D

[](../../../2d-physics/collider/composite-collider/combine-colliders-
composite-collider-2d.html)

Combine Colliders with the Composite Collider 2D

# Composite Collider 2D component reference

The Composite **Collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../../CollidersOverview.html)  
See in [Glossary](../../../Glossary.html#Collider) 2D component is a [Collider
2D](../collider-2d-landing.html) that interacts with the 2D physics system.
Unlike most Colliders, it doesn’t have an inherent shape. Instead, it merges
the shapes of any [Box Collider 2D](../box-collider-2d-reference.html),
[Polygon Collider 2D](../polygon-collider-2d-reference.html), [Circle Collider
2D](../circle-collider-2d-reference.html) or [Capsule Collider 2D](../capsule-
collider/capsule-collider-2d-reference.html) that it’s set to use. The
Composite Collider 2D uses the vertices (geometry) from any of these
colliders, and merges them together into new geometry controlled by the
Composite Collider 2D itself.

**Property** | **Function**  
---|---  
**Material** | Select the [Physics Material 2D](../../physics-material-2d-reference.html)Use to adjust the friction and bounce that occurs between 2D physics objects when they collide [More info](../../../2d-physics/physics-material-2d-reference.html)  
See in [Glossary](../../../Glossary.html#PhysicsMaterial2D) that determines
properties of **collisions** A collision occurs when the physics engine
detects that the colliders of two GameObjects make contact or overlap, when at
least one has a Rigidbody component and is in motion. [More
info](../../../CollidersOverview.html)  
See in [Glossary](../../../Glossary.html#Collision), such as friction and
bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this Collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached Effector 2D.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Geometry Type** | Select the type of geometry to merge the vertices of the selected Colliders into. Select either **Outlines** or **Polygons** from the dropdown menu.  
**Outlines** | Select this to produce a Collider 2D with hollow outlines, identical to an [Edge Collider 2D](../edge-collider-2d-reference.html).  
**Polygons** | Select this to produce a Collider 2D with solid polygons, identical to a [Polygon Collider 2D](../polygon-collider-2d-reference.html).  
**Use Delaunay**Mesh** The main graphics primitive of Unity. Meshes make up a
large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](../../../mesh.html)  
See in [Glossary](../../../Glossary.html#Mesh)** | Enable this property to an additional Delaunay triangulation step to produce the Collider mesh.  
**Generation Type** | Select the geometry generation method used when either the Composite Collider 2D is changed, or when any of the Colliders composing the Composite Collider 2D is changed.  
**Synchronous** | Select this to have Unity immediately generate new geometry when a change is made to the Composite Collider 2D or to any of the Colliders composing it.  
**Manual** | Select this to have Unity only generate geometry generation happens when you request it. To request generation, either call the [CompositeCollider2D.GenerateGeometry](../../../../ScriptReference/CompositeCollider2D.GenerateGeometry.html) scripting API, or select **Regenerate Geometry** that appears under the selection.  
**Vertex Distance** | Set a value for the minimum spacing allowed for any vertices gathered from Colliders being composed. Any vertex closer than this limit is removed. This allows control over the effective resolution of the vertex compositing.  
**Offset Distance** | Set the value to offset vertices when compositing multiple physics shapes. Any vertices between physics shapes within this distance value are combined. **Note:** It’s recommended to not set this value higher than 1% of the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite)’s length, as this may result
in loss of detail when too many vertices are combined together.  
**Layer Overrides** | Expand for the Layer override settings.  
**Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its [API](../../../../ScriptReference/Collider2D-layerOverridePriority.html) page for more information.  
**Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its [API](../../../../ScriptReference/Collider2D-includeLayers.html) documentation for more information.  
**Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its [API](../../../../ScriptReference/Collider2D-excludeLayers.html) documentation for more information.  
**Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its [API](../../../../ScriptReference/Collider2D-forceSendLayers.html) documentation for more information.  
**Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its [API](../../../../ScriptReference/Collider2D-forceReceiveLayers.html) documentation for more information.  
**Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its [API](../../../../ScriptReference/Collider2D-contactCaptureLayers.html) documentation for more information.  
**Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its [API](../../../../ScriptReference/Collider2D-callbackLayers.html) documentation for more information.  
  
## Additional resources

  * [Collider 2D API documentation](../../../../ScriptReference/Collider2D.html)
  * [Rigidbody 2D](../../rigidbody/rigidbody-2d-landing.html)

CompositeCollider2D

[](../../../2d-physics/collider/composite-collider/composite-
collider-2d-landing.html)

Composite Collider 2D

[](../../../2d-physics/collider/composite-collider/combine-colliders-
composite-collider-2d.html)

Combine Colliders with the Composite Collider 2D

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

