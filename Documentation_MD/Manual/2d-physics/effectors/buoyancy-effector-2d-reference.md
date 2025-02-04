[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Effectors 2D](../../2d-physics/effectors/effectors-2d-landing.html)
  * Buoyancy Effector 2D reference

[](../../2d-physics/effectors/area-effector-2d-reference.html)

Area Effector 2D reference

[](../../2d-physics/effectors/point-effector-2d-reference.html)

Point Effector 2D reference

# Buoyancy Effector 2D reference

The Buoyancy Effector 2D defines simple fluid behaviour such as floating and
the drag and flow of fluid. You can also control a fluid surface, with the
fluid behaviour taking place below.

## Properties

**Property** | **Function**  
---|---  
**Use**Collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) Mask** | Check this box to enable the ‘Collider Mask’ property. If this is not enabled, the Global **Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision) Matrix will be used as the
default for all Collider 2Ds.  
**Collider Mask** | The mask used to select specific Layers allowed to interact with the effector. Note that this option only displays if you have selected **Use Collider Mask**.  
**Surface Level** | Defines the surface location of the buoyancy fluid. When a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) is above this line, no
buoyancy forces are applied. When a GameObject is intersecting or completely
below this line, buoyancy forces are applied. This is a location specified as
a world-space offset along the world y-axis, but is also scaled by the
GameObject’s **Transform** component.  
**Density** | The density of the fluid. Colliders with a higher density sink, those with a lower density float, and those with the same density appear suspended in the fluid.  
**Linear Drag** | The drag coefficient affecting positional movement of a GameObject. This only applies when inside the fluid.  
**Angular Drag** | The drag coefficient affecting rotational movement of a GameObject. This only applies when inside the fluid.  
**Flow Angle** | The world-space angle (in degrees) for the direction of fluid flow. Fluid flow applies buoyancy forces in the specified direction.  
**Flow Magnitude** | The “power” of the fluid flow force. Combined with **Fluid Angle** , this specifies the level of buoyancy force applied to GameObjects inside the fluid. The magnitude can also be negative, in which case the buoyancy forces are applied at 180 degrees to the **Flow Angle.**  
**Flow Variation** | Enter a value here to randomly vary the fluid forces. Specify a positive or negative variation to randomly add or subtract from the **Fluid Magnitude**.  
  
BuoyancyEffector2D

[](../../2d-physics/effectors/area-effector-2d-reference.html)

Area Effector 2D reference

[](../../2d-physics/effectors/point-effector-2d-reference.html)

Point Effector 2D reference

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

