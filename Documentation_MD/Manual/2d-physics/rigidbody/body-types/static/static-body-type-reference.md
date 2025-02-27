[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [2D Physics](../../../../2d-physics/2d-physics.html)
  * [Rigidbody 2D](../../../../2d-physics/rigidbody/rigidbody-2d-landing.html)
  * [Rigidbody 2D body types](../../../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
  * [Static Body Type](../../../../2d-physics/rigidbody/body-types/static/static-body-type-landing.html)
  * Static Body Type reference

[](../../../../2d-physics/rigidbody/body-types/static/static-body-type-
fundamentals.html)

Static Body Type fundamentals

[](../../../../2d-physics/rigidbody/rigidbody-2d-simulated-property.html)

Rigidbody 2D Simulated property

# Static Body Type reference

Due to limited behavior, **Rigidbody** A component that allows a GameObject to
be affected by simulated gravity and other forces. [More
info](../../../../class-Rigidbody.html)  
See in [Glossary](../../../../Glossary.html#Rigidbody) 2D with a Static **body
type** Defines a fixed behavior for a 2D Rigidbody. Can be Dynamic (the body
moves under simulation and is affected by forces like gravity), Kinematic (the
body moves under simulation, but and isn’t affected by forces like gravity) or
Static (the body doesn’t move under simulation). [More
info](../../../../2d-physics/rigidbody/introduction-to-rigidbody-2d.html)  
See in [Glossary](../../../../Glossary.html#BodyType) only have a very limited
set of properties are available for this **Body Type**.

## Static Rigidbody 2D properties

**Property** | **Function**  
---|---  
**Body Type** | Select to set the movement behavior and **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#Collider) 2D interaction of this
Rigidbody 2D’s component settings.  
**Dynamic** | Select to set this Rigidbody 2D to the [Dynamic](../dynamic/dynamic-body-type-reference.html) Body Type, which is designed to move under simulation and has all Rigidbody 2D properties available. The is the default Body Type for a Rigidbody 2D.  
**Kinematic** | Select to set this Rigidbody 2D to the [Kinematic](../kinematic/kinematic-body-type-reference.html) Body Type, which is designed to move under simulation but only under very explicit user control. Refer to [Body Type: Kinematic](../kinematic/kinematic-body-type-reference.html) for more information.  
**Static** | Select to set this Rigidbody 2D to the Static Body Type, which is designed to not move under simulation at all and behaves like an immovable object with infinite mass.  
**Material** | Set a common [physics material](../../../physics-material-2d-reference.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](../../../../class-PhysicsMaterial.html)  
See in [Glossary](../../../../Glossary.html#PhysicsMaterial) for all Collider
2Ds attached to this Rigidbody 2D. **Note:** A Collider 2D uses its own
Material property if it has one set. If there is no Material specified here or
in the Collider 2D, the default option is **None (Physics Material 2D)**. This
uses a default Material which you can set in the [Physics
2D](../../../../class-Physics2DManager.html) window.  
  
**Note** : Use this to ensure that all Collider 2Ds attached to the same
**Static** Body Type Rigidbody 2D can all use the same Material.  
**Simulated** | Enable **Simulated** to have the Rigidbody 2D and any attached Collider 2Ds and **Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](../../../../Joints.html)  
See in [Glossary](../../../../Glossary.html#joint) 2Ds to interact with the
physics simulation during runtime. If this is disabled, these components do
not interact with the simulation. Refer to [Rigidbody 2D properties:
Simulated](../../rigidbody-2d-simulated-property.html) for more information.
This property is enabled by default.  
**Layer Overrides** | Expand for the Layer override settings.  
**Include Layers** | Select the additional Layers that all Collider 2Ds attached to this Rigidbody 2D should include, when deciding if a **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#Collision) with another Collider2D
should occur or not. Refer to
[Rigidbody2D-includeLayers](../../../../../ScriptReference/Rigidbody2D-includeLayers.html)
for more information.  
**Exclude Layers** | Select the additional Layers that all Collider 2Ds attached to this Rigidbody 2D should exclude, when deciding if a collision with another Collider 2D should occur or not. Refer to [Rigidbody2D-excludeLayers](../../../../../ScriptReference/Rigidbody2D-excludeLayers.html) for more information.  
  
[](../../../../2d-physics/rigidbody/body-types/static/static-body-type-
fundamentals.html)

Static Body Type fundamentals

[](../../../../2d-physics/rigidbody/rigidbody-2d-simulated-property.html)

Rigidbody 2D Simulated property

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

