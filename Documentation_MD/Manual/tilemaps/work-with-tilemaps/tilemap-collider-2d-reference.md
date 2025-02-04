[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Tilemaps in Unity](../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * Tilemap Collider 2D component reference

[](../../tilemaps/work-with-tilemaps/tilemap-renderer-reference.html)

Tilemap Renderer component reference

[](../../tilemaps/work-with-tilemaps/troubleshoot-mismatched-cell-
layouts.html)

Troubleshoot mismatched Cell Layouts

# Tilemap Collider 2D component reference

The **Tilemap**Collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) 2D** component generates
collider shapes for [tiles](../tiles-for-tilemaps/tile-asset-reference.html)A
simple class that allows a sprite to be rendered on a Tilemap. [More
info](../../tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-
landing.html)  
See in [Glossary](../../Glossary.html#Tile) on a [Tilemap](./tilemap-
reference.html)A GameObject that allows you to quickly create 2D levels using
tiles and a grid overlay. [More info](../../tilemaps/work-with-
tilemaps/tilemap-reference.html)  
See in [Glossary](../../Glossary.html#Tilemap). You control this collider
generation process with the properties found in the component.

## Properties

Property | Description  
---|---  
**Max Tile Change Count** | Set the maximum number of tile changes (such as adding/removing tiles to the tilemap) to accumulate before doing a full collider rebuild instead of an incremental rebuild.  
  
**Note:** A high number of accumulated changes can cause the incremental
rebuild of the **Tilemap Collider 2D** to be slower than a full rebuild.
Decrease this value to resolve this issue.  
**Extrusion Factor** | Set the amount (in Unity world space units) to extrude the collider shape of each tile. This minimizes the gaps between the collider shapes of neighboring tiles and brings them to within the minimum **Vertex Distance** set in the [Composite Collider 2D](../../2d-physics/collider/composite-collider/composite-collider-2d-reference.html) component., which can then compose the tile colliders together.   
  
**Note:** This property isn’t available by default. It becomes available when
you select a Composite Operation and attach a Composite Collider 2D to the
same GameObject.  
**Material** | Select the [Physics Material 2D](../../2d-physics/physics-material-2d-reference.html)Use to adjust the friction and bounce that occurs between 2D physics objects when they collide [More info](../../2d-physics/physics-material-2d-reference.html)  
See in [Glossary](../../Glossary.html#PhysicsMaterial2D) that determines
properties of **collisions** A collision occurs when the physics engine
detects that the colliders of two GameObjects make contact or overlap, when at
least one has a Rigidbody component and is in motion. [More
info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision), such as friction and bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached [Effector 2D](../../2d-physics/effectors/effectors-2d-landing.html).  
**Composite Operations** | Select the [composite operation](../../../ScriptReference/Collider2D.CompositeOperation.html) used by an attached [Composite Collider 2D](../../2d-physics/collider/composite-collider/composite-collider-2d-reference.html) component.  
  
**Note:** When you select any operation besides **None** , the following
properties—**Material** , **Is Trigger** , **Used By Effector** , and **Edge
Radius** —become controlled by the attached Composite Collider 2D component
and are no longer available in this collider’s properties.  
**None** | Select this to have no composite operation take place.  
**Merge** | Select this to have this composite operation compose geometry using a Boolean OR operation.  
**Intersect** | Select this to have this composite operation compose geometry using a Boolean AND operation.  
**Difference** | Select this to have this composite operation compose geometry using a Boolean NOT operation.  
**Flip** | Select this to have this composite operation compose geometry using a Boolean XOR operation.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Layer Overrides** | Expand for the Layer override settings.  
**Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its [API](../../../ScriptReference/Collider2D-layerOverridePriority.html) page for more information.  
**Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its [API](../../../ScriptReference/Collider2D-includeLayers.html) documentation for more information.  
**Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its [API](../../../ScriptReference/Collider2D-excludeLayers.html) documentation for more information.  
**Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its [API](../../../ScriptReference/Collider2D-forceSendLayers.html) documentation for more information.  
**Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its [API](../../../ScriptReference/Collider2D-forceReceiveLayers.html) documentation for more information.  
**Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its [API](../../../ScriptReference/Collider2D-contactCaptureLayers.html) documentation for more information.  
**Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its [API](../../../ScriptReference/Collider2D-callbackLayers.html) documentation for more information.  
  
## Additional resources

  * [Physics 2D Reference](../../2d-physics/2d-physics.html)
  * [Collider 2D](../../2d-physics/collider/collider-2d-landing.html)
  * [Composite Collider 2D](../../2d-physics/collider/composite-collider/composite-collider-2d-reference.html)

* * *

  * New properties added in Unity 2020.1
  * Tilemaps added in [2017.2](https://docs.unity3d.com/2017.2/Documentation/Manual/30_search.html?q=newin20172) NewIn20172 TilemapCollider2D

[](../../tilemaps/work-with-tilemaps/tilemap-renderer-reference.html)

Tilemap Renderer component reference

[](../../tilemaps/work-with-tilemaps/troubleshoot-mismatched-cell-
layouts.html)

Troubleshoot mismatched Cell Layouts

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

