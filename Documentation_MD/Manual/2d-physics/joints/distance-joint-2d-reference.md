[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/distance-joint-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/joints/distance-joint-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/distance-joint-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/distance-joint-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/distance-joint-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/joints/distance-joint-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/distance-joint-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/distance-joint-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * [Distance Joint 2D](../../2d-physics/joints/distance-joint-2d-landing.html)
  * Distance Joint 2D component reference

[](../../2d-physics/joints/distance-joint-2d-fundamentals.html)

Distance Joint 2D fundamentals

[](../../2d-physics/joints/fixed-joint-2d-landing.html)

Fixed Joint 2D

# Distance Joint 2D component reference

The **Distance**Joint** A physics component allowing a dynamic connection
between Rigidbody components, usually allowing some degree of movement such as
a hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) 2D** is a 2D joint that attaches
two **GameObjects** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) controlled by
****Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) 2D** physics, and keeps them
a certain distance apart.

## Properties

**Property** | **Function**  
---|---  
**Enable**Collision** A collision occurs when the physics engine detects that
the colliders of two GameObjects make contact or overlap, when at least one
has a Rigidbody component and is in motion. [More
info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision)** | Enable this property to enable collisions between the two connected GameObjects.  
**Connected Rigidbody** | Specify the other object this joint connects to. Leave this as **None** to have the other end of the joint fixed at a point in space defined by the **Connected Anchor** property. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Auto Configure Connected Anchor** | Enable this property to automatically set the anchor location for the other object this joint connects to. You do not need to enter coordinates for the **Connected Anchor** property if you enable this property.  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this GameObject.  
**Connected Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the other GameObject.  
**Auto Configure Distance** | Enable this to automatically detect the current distance between the two GameObjects, and set it as the distance that the Distance Joint 2D keeps between the two GameObjects. When enabled, you do not need to specify the distance between the GameObjects at **Distance**.  
**Distance** | Specify the distance that the Distance Joint 2D keeps between the two GameObjects.  
**Max Distance Only** | Enable this to only enforce a maximum distance. This allows connected GameObjects to move closer to each other, but not further than the distance set by **Distance**. Clear this to keep the distance between the GameObjects fixed.  
**Break Action** | Set the action taken when either a force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
DistanceJoint2D

[](../../2d-physics/joints/distance-joint-2d-fundamentals.html)

Distance Joint 2D fundamentals

[](../../2d-physics/joints/fixed-joint-2d-landing.html)

Fixed Joint 2D

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

