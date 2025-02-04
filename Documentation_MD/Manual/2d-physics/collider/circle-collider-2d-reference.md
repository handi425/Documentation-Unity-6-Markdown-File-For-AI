[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/collider/circle-collider-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/collider/circle-collider-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/circle-collider-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/circle-collider-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/collider/circle-collider-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/collider/circle-collider-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/circle-collider-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/circle-collider-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Collider 2D](../../2d-physics/collider/collider-2d-landing.html)
  * Circle Collider 2D component reference

[](../../2d-physics/collider/collider-2d-landing.html)

Collider 2D

[](../../2d-physics/collider/box-collider-2d-reference.html)

Box Collider 2D component reference

# Circle Collider 2D component reference

The Circle **Collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) 2D component is a [Collider
2D](./collider-2d-landing.html) that interacts with the 2D physics system for
**collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More
info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision) detection. This collider 2D
is circular in shape, with a defined position and radius within the local
coordinate space of a **sprite** A 2D graphic objects. If you are used to
working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](../../sprite/sprite-
landing.html)  
See in [Glossary](../../Glossary.html#Sprite). Adjust the component properties
to change the shape and behavior of the collider 2D.

**Property** | **Function**  
---|---  
**Material** | Select the [Physics Material 2D](../physics-material-2d-reference.html)Use to adjust the friction and bounce that occurs between 2D physics objects when they collide [More info](../../2d-physics/physics-material-2d-reference.html)  
See in [Glossary](../../Glossary.html#PhysicsMaterial2D) that determines
properties of collisions, such as friction and bounce.  
**Is Trigger** | Enable this option if you want the Collider 2D to behave as a trigger. The physics system ignores the Collider 2D when you enable this option.  
**Used by Effector** | Enable this option if you want an attached Effector 2D to use this Collider 2D.  
**Composite Operations** | Select the [composite operation](../../../ScriptReference/Collider2D.CompositeOperation.html) used by an attached [Composite Collider 2D](composite-collider/composite-collider-2d-reference.html) component.  
  
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
**Radius** | Set the radius of the Circle Collider 2D in local space units.  
**Layer Overrides** | Expand this option to use the Layer override settings.  
**Layer Override Priority** | Assign the decision priority that this Collider 2D uses when resolving conflicting decisions on whether a contact between itself and another Collider 2D should happen or not. For more information, refer to its [API](../../../ScriptReference/Collider2D-layerOverridePriority.html) page.  
**Include Layers** | Select the additional Layers for this Collider 2D to include when deciding if a contact with another Collider2D should happen or not. Refer to its [API](../../../ScriptReference/Collider2D-includeLayers.html) documentation for more information.  
**Exclude Layers** | Select the additional layers for this Collider 2D to exclude when deciding if a contact with another Collider 2D should happen or not. Refer to its [API](../../../ScriptReference/Collider2D-excludeLayers.html) documentation for more information.  
**Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its [API](../../../ScriptReference/Collider2D-forceSendLayers.html) documentation for more information.  
**Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its [API](../../../ScriptReference/Collider2D-forceReceiveLayers.html) documentation for more information.  
**Contact Capture Layers** | Select the Layers of other Collider 2D involved in contact with this Collider2D that you want to capture. Refer to its [API](../../../ScriptReference/Collider2D-contactCaptureLayers.html) documentation for more information.  
**Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its [API](../../../ScriptReference/Collider2D-callbackLayers.html) documentation for more information.  
  
## Additional resources

  * [Collider 2D API documentation](../../../ScriptReference/Collider2D.html)
  * [Rigidbody 2D](../rigidbody/rigidbody-2d-landing.html)

CircleCollider2D

[](../../2d-physics/collider/collider-2d-landing.html)

Collider 2D

[](../../2d-physics/collider/box-collider-2d-reference.html)

Box Collider 2D component reference

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

