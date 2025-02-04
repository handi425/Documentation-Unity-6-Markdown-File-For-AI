[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [2D Physics](../../../2d-physics/2d-physics.html)
  * [Rigidbody 2D](../../../2d-physics/rigidbody/rigidbody-2d-landing.html)
  * [Rigidbody 2D body types](../../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
  * Introduction to Rigidbody 2D body types

[](../../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-
landing.html)

Rigidbody 2D body types

[](../../../2d-physics/rigidbody/body-types/dynamic/dynamic-body-type-
landing.html)

Dynamic Body Type

# Introduction to Rigidbody 2D body types

There are three options for **Body Type** Defines a fixed behavior for a 2D
Rigidbody. Can be Dynamic (the body moves under simulation and is affected by
forces like gravity), Kinematic (the body moves under simulation, but and
isn’t affected by forces like gravity) or Static (the body doesn’t move under
simulation). [More info](../../../2d-physics/rigidbody/introduction-to-
rigidbody-2d.html)  
See in [Glossary](../../../Glossary.html#BodyType) which define the behavior
of the **Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](../../../class-Rigidbody.html)  
See in [Glossary](../../../Glossary.html#Rigidbody) 2D. Any **Collider** An
invisible shape that is used to handle physical collisions for an object. A
collider doesn’t need to be exactly the same shape as the object’s mesh - a
rough approximation is often more efficient and indistinguishable in gameplay.
[More info](../../../CollidersOverview.html)  
See in [Glossary](../../../Glossary.html#Collider) 2D attached to that
Rigidbody 2D inherits the Rigidbody 2D’s Body Type as well.

The selected Body Type defines the Rigidbody 2D’s movement behavior (position
and rotation) and Collider interactions. When a Body Type changes, Unity
recalculates various mass-related internal properties, and all existing
contacts for the Collider 2Ds attached to the Rigidbody 2D need to be re-
evaluated during the **GameObject** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](../../../class-GameObject.html)  
See in [Glossary](../../../Glossary.html#GameObject)’s next FixedUpdate.
Depending on how many contacts and Collider 2Ds are attached to the body,
changing the Body Type can cause variations in performance.

The properties of the Rigidbody 2D component in its **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](../../../UsingTheInspector.html)  
See in [Glossary](../../../Glossary.html#Inspector) window differs depending
on which Body Type you have selected.

[](../../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-
landing.html)

Rigidbody 2D body types

[](../../../2d-physics/rigidbody/body-types/dynamic/dynamic-body-type-
landing.html)

Dynamic Body Type

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

