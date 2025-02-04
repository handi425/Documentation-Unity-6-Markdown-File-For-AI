[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/collider/custom-collider/custom-collider-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/collider/custom-collider/custom-collider-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/custom-collider/custom-collider-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/custom-collider/custom-collider-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/collider/custom-collider/custom-collider-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/collider/custom-collider/custom-collider-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/custom-collider/custom-collider-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/custom-collider/custom-collider-2d-reference.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [2D Physics](../../../2d-physics/2d-physics.html)
  * [Collider 2D](../../../2d-physics/collider/collider-2d-landing.html)
  * [Custom Collider 2D](../../../2d-physics/collider/custom-collider/custom-collider-2d-landing.html)
  * Custom Collider 2D component reference

[](../../../2d-physics/collider/custom-collider/custom-
collider-2d-landing.html)

Custom Collider 2D

[](../../../2d-physics/collider/custom-collider/use-custom-collider-2d.html)

Use a Custom Collider 2D

# Custom Collider 2D component reference

The Custom **Collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../../CollidersOverview.html)  
See in [Glossary](../../../Glossary.html#Collider) 2D is a [Collider
2D](../collider-2d-landing.html) that interacts with the 2D physics system.
Unlike other colliders, you don’t configure this collider in the Unity Editor,
instead you configure the collider by assigning
[PhysicsShape2D](../../../../ScriptReference/PhysicsShape2D.html) geometry to
it via the
[PhysicsShapeGroup2D](../../../../ScriptReference/PhysicsShapeGroup2D.html)
API.

You can define the collider’s shape by adding, removing, and modifying the
`PhysicsShape2D` shapes. Refer to the
[PhysicsShape2D](../../../../ScriptReference/PhysicsShapeGroup2D.html) API
documentation for more information. This also means that a Custom Collider 2D
can contain an unlimited number of low-level `PhysicsShape2D` and form any
shape, or emulate other types of Collider 2D.

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
**Custom Shape Count** (Read only) | Indicates how many `PhysicsShape2D` the Collider is using.  
**Custom Vertex Count** (Read Only) | Indicates how many vertices all `PhysicsShape2D` in the Collider are using.  
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

CustomCollider2D

[](../../../2d-physics/collider/custom-collider/custom-
collider-2d-landing.html)

Custom Collider 2D

[](../../../2d-physics/collider/custom-collider/use-custom-collider-2d.html)

Use a Custom Collider 2D

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

