[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [2D Physics](../../../../2d-physics/2d-physics.html)
  * [Rigidbody 2D](../../../../2d-physics/rigidbody/rigidbody-2d-landing.html)
  * [Rigidbody 2D body types](../../../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
  * [Kinematic Body Type](../../../../2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-landing.html)
  * Kinematic Body Type reference

[](../../../../2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-
fundamentals.html)

Kinematic Body Type fundamentals

[](../../../../2d-physics/rigidbody/body-types/static/static-body-type-
landing.html)

Static Body Type

# Kinematic Body Type reference

A Kinematic **Rigidbody** A component that allows a GameObject to be affected
by simulated gravity and other forces. [More info](../../../../class-
Rigidbody.html)  
See in [Glossary](../../../../Glossary.html#Rigidbody) 2D behaves like an
immovable object (as if it has infinite mass) during **collisions** A
collision occurs when the physics engine detects that the colliders of two
GameObjects make contact or overlap, when at least one has a Rigidbody
component and is in motion. [More info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#Collision), and mass-related
properties are not available with this **Body Type** Defines a fixed behavior
for a 2D Rigidbody. Can be Dynamic (the body moves under simulation and is
affected by forces like gravity), Kinematic (the body moves under simulation,
but and isn’t affected by forces like gravity) or Static (the body doesn’t
move under simulation). [More
info](../../../../2d-physics/rigidbody/introduction-to-rigidbody-2d.html)  
See in [Glossary](../../../../Glossary.html#BodyType).

## Kinematic Rigidbody 2D properties

**Property** | **Function**  
---|---  
**Body Type** | Select to set the movement behavior and **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#Collider) 2D interaction of this
Rigidbody 2D’s component settings.  
**Dynamic** | Select to set this Rigidbody 2D to the [Dynamic](../dynamic/dynamic-body-type-reference.html) Body Type, which is designed to move under simulation and has all Rigidbody 2D properties available. This is the default Body Type for a Rigidbody 2D.  
**Kinematic** | Select to set this Rigidbody 2D to the Kinematic Body Type, which is designed to move under simulation but only under very explicit user control.  
**Static** | Select to set this Rigidbody 2D to the [Static](../static/static-body-type-reference.html) Body Type, which is designed to not move under simulation at all and behaves like an immovable object with infinite mass. Refer to [Body Type: Static](../static/static-body-type-reference.html) for more information.  
**Material** | Set a common [physics material](../../../physics-material-2d-reference.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](../../../../class-PhysicsMaterial.html)  
See in [Glossary](../../../../Glossary.html#PhysicsMaterial) for all Collider
2Ds attached to this Rigidbody 2D. **Note:** A Collider 2D uses its own
Material property if it has one set. If there is no Material specified here or
in the Collider 2D, the default option is **None (Physics Material 2D)**. This
uses a default Material which you can set in the [Physics
2D](../../../../class-Physics2DManager.html) window.  
**Simulated** | Enable **Simulated** to have the Rigidbody 2D and any attached Collider 2Ds and **Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](../../../../Joints.html)  
See in [Glossary](../../../../Glossary.html#joint) 2Ds to interact with the
physics simulation during runtime. If this is disabled, these components do
not interact with the simulation. Refer to [Rigidbody 2D properties:
Simulated](../../rigidbody-2d-simulated-property.html), below for more
information. This property is enabled by default.  
**Full Kinematic Contact** | Enable this property if you want the Rigidbody 2D to be able to collide with all other Rigidbody 2D **Body Types**. **Note** : When this property is disabled, the Kinematic Rigidbody 2D only collides with Dynamic Rigidbody 2Ds. See Using Full Kinematic Contacts for more details.  
****Collision Detection** An automatic process performed by Unity which
determines whether a moving GameObject with a Rigidbody and collider component
has come into contact with any other colliders. [More
info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#CollisionDetection)** | Define how collisions between Collider 2Ds are detected.  
**Discrete** | Select this option to allow **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../../../class-GameObject.html)  
See in [Glossary](../../../../Glossary.html#GameObject) with Rigidbody 2Ds and
Collider 2Ds to overlap or pass through each other during a physics update, if
they are moving fast enough. Collision contacts are only generated at the new
position.  
**Continuous** | Select this option to ensure GameObjects with Rigidbody 2Ds and Collider 2Ds do not pass through each other during a physics update. Instead, Unity calculates the first impact point of any of the Collider 2Ds, and moves the GameObject there. **Note:** This option takes more CPU time than **Discrete**.  
**Sleeping Mode** | Define how the GameObject “sleeps” to save processor time when it is at rest.  
**Never Sleep** | Select this option to have sleeping disabled. **Important:** This should be avoided where possible, as it can impact system resources.  
**Start Awake** | Select this to have the GameObject initially awake.  
**Start Asleep** | Select this to have the GameObject initially asleep but can be awaken by collisions.  
**Interpolate** | Define how the GameObject’s movement is interpolated between physics updates. **Note** : This is useful when motion tends to be jerky.  
**None** | Select this to not apply movement smoothing.  
**Interpolate** | Select this to smoothen movement based on the GameObject’s positions in previous frames.  
**Extrapolate** | Select this to smoothen movement is smoothed based on an estimate of its position in the next frame.  
**Constraints** | Define any restrictions on the Rigidbody 2D’s motion.  
**Freeze Position** | Stops the Rigidbody 2D moving in the X and Y world axes selectively.  
**Freeze Rotation** | Stops the Rigidbody 2D rotating around the Z world axis selectively.  
**Layer Overrides** | Expand for the Layer override settings.  
**Include Layers** | Select the additional Layers that all Collider 2Ds attached to this Rigidbody 2D should include, when deciding if a collision with another Collider2D should occur or not. Refer to [Rigidbody2D-includeLayers](../../../../../ScriptReference/Rigidbody2D-includeLayers.html) for more information.  
**Exclude Layers** | Select the additional Layers that all Collider 2Ds attached to this Rigidbody 2D should exclude, when deciding if a collision with another Collider 2D should occur or not. Refer to [Rigidbody2D-excludeLayers](../../../../../ScriptReference/Rigidbody2D-excludeLayers.html) for more information.  
  
## Full Kinematic Contacts

Enabling **Full Kinematic Contacts** enables a Kinematic Rigidbody 2D to
collide with all Rigidbody 2D **Body Types**. This is similar to the behavior
of a Dynamic Rigidbody 2D, except the Kinematic Rigidbody 2D is not moved by
the physics system when contacting another Rigidbody 2D. Instead, it behaves
like an immovable object with infinite mass.

When this property is disabled, a Kinematic Rigidbody 2D will only collide
with Dynamic Rigidbody 2Ds and not the other **Body Types**. **Note** :
Trigger Colliders are an exception to this rule. This means that no collision
scripting callbacks
([OnCollisionEnter](../../../../../ScriptReference/Collider2D.OnCollisionEnter2D.html),
[OnCollisionStay](../../../../../ScriptReference/Collider2D.OnCollisionStay2D.html),
[OnCollisionExit](../../../../../ScriptReference/Collider2D.OnCollisionExit2D.html))
will occur.

This can be inconvenient when you are using physics queries (such as
[Physics.Raycast](../../../../../ScriptReference/Physics.Raycast.html)) to
detect where and how a Rigidbody 2D should move, and when you require multiple
Kinematic Rigidbody 2Ds to interact with each other. Enable **Use Full
Kinematic Contacts** to make Kinematic Rigidbody 2D components interact in
this way.

**Note** : **Use Full Kinematic Contacts** allows explicit position and
rotation control of a Kinematic Rigidbody 2D, but still allows full collision
callbacks. In a setup where you need explicit control of all Rigidbody 2Ds,
use Kinematic Rigidbody 2Ds in place of Dynamic Rigidbody 2Ds to still have
full collision callback support.

[](../../../../2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-
fundamentals.html)

Kinematic Body Type fundamentals

[](../../../../2d-physics/rigidbody/body-types/static/static-body-type-
landing.html)

Static Body Type

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

