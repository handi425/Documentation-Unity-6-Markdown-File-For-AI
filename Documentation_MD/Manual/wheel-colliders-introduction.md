[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/wheel-colliders-introduction.html)
  * [中文](/cn/current/Manual/wheel-colliders-introduction.html)
  * [日本語](/ja/current/Manual/wheel-colliders-introduction.html)
  * [한국어](/kr/current/Manual/wheel-colliders-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/wheel-colliders-introduction.html)
  * [中文](/cn/current/Manual/wheel-colliders-introduction.html)
  * [日本語](/ja/current/Manual/wheel-colliders-introduction.html)
  * [한국어](/kr/current/Manual/wheel-colliders-introduction.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider shapes](collider-shapes.html)
  * [Wheel colliders](wheel-colliders.html)
  * Introduction to Wheel colliders

[](wheel-colliders.html)

Wheel colliders

[](wheel-colliders-friction.html)

Wheel collider friction

# Introduction to Wheel colliders

To simulate accurate wheel behavior in Unity, you use a Wheel **collider** An
invisible shape that is used to handle physical collisions for an object. A
collider doesn’t need to be exactly the same shape as the object’s mesh - a
rough approximation is often more efficient and indistinguishable in gameplay.
[More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) for each wheel. **Wheel colliders**
A special collider for grounded vehicles. It has built-in collision detection,
wheel physics, and a slip-based tire friction model. It can be used for
objects other than wheels, but it is specifically designed for vehicles with
wheels. [More info](class-WheelCollider.html)  
See in [Glossary](Glossary.html#WheelCollider) manage wheel rotation and
vehicle movement, and also have properties that simulate a suspension system.

The Wheel collider component is represented in the API as the
[`WheelCollider`](../ScriptReference/WheelCollider.html) class.

## Wheel collider raycast

The Wheel collider appears in the **Scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view as a 2D circle (see Wheel collider
visualization). However, it is actually a single [Physics
raycast](../ScriptReference/Physics.Raycast.html). PhysX casts the ray down
the local Y-axis along the direction of suspension through the center of the
wheel. The start and end of the raycast are at the following points:

  * The raycast starts just above the top of the wheel at maximum suspension **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) (that is, just outside the
**Radius** , at the top of the **Suspension Distance** on the Y axis).

  * The raycast ends just below the bottom of the wheel at maximum suspension extension (that is, just outside the **Radius** , at the bottom of the **Suspension Distance** on the Y axis).

This raycast configuration means that a Wheel collider does not actually roll
across other surfaces (such as the ground) while moving. In Play mode, the
rotation of the Wheel collider does not change. However, the rotation of the
wheel model does need to change so that the wheel appears to roll along the
ground. To achieve this, the model and the collider need to be on two separate
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject). The Wheel colliders’ Transform
should be fixed relative to the vehicle, and the models should be able to
rotate. You can then configure the Wheel collider to send its global position
to the wheel model and rotate the wheel model via script. For an example of
this workflow, refer to the walkthrough [Create an example vehicle with Wheel
colliders](WheelColliderTutorial.html).

For more details on the Wheel collider raycast setup in PhysX, refer to the
[PhysX 4.1 Vehicles SDK
documentation](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Index.html).

### Prepare the ground for raycast Wheel colliders

An important implication of the raycast setup is that wheels don’t always
smoothly roll up or step down variations in road level (for example, rolling
up from the road onto a step). When encountering a step or curb, the wheel is
likely to clip and then “pop” up only as the center line crosses the step:

![Two frames of a Wheel collider vehicle navigating a step \(a sharp increase
in the ground surface\). In the first frame, the wheel appears to clip through
the step. This is because the raycast at the center of the wheel model has not
yet reached the step. In the second frame, the wheel model appears correctly
on the step. This change happens when the raycast at the center of the wheel
detects a change in height, causing the wheel to appear to “pop” up the step
rather than roll realistically.](../uploads/Main/wheel-colliders-introduction-
raycast-demo-step.png) Two frames of a Wheel collider vehicle navigating a
step (a sharp increase in the ground surface). In the first frame, the wheel
appears to clip through the step. This is because the raycast at the center of
the wheel model has not yet reached the step. In the second frame, the wheel
model appears correctly on the step. This change happens when the raycast at
the center of the wheel detects a change in height, causing the wheel to
appear to “pop” up the step rather than roll realistically.

The raycast can also slip down into small drops or steps in the road when the
center point reaches them:

![Two frames of a Wheel collider vehicle navigating a drop \(a sharp decrease
in the ground surface\). In the first frame, the wheel appears to sit
correctly over the drop. This is because the raycast at the center of the
wheel model has not yet reached the drop. In the second frame, the wheel model
appears to have fallen into the drop. This change happens when the raycast at
the center of the wheel detects a change in height, causing the wheel to
appear to drop suddenly rather than roll
realistically.](../uploads/Main/wheel-colliders-introduction-raycast-demo-
drop.png) Two frames of a Wheel collider vehicle navigating a drop (a sharp
decrease in the ground surface). In the first frame, the wheel appears to sit
correctly over the drop. This is because the raycast at the center of the
wheel model has not yet reached the drop. In the second frame, the wheel model
appears to have fallen into the drop. This change happens when the raycast at
the center of the wheel detects a change in height, causing the wheel to
appear to drop suddenly rather than roll realistically.

For this reason, the ground **collision** A collision occurs when the physics
engine detects that the colliders of two GameObjects make contact or overlap,
when at least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) geometry must be as smooth as
possible to ensure a smooth and accurate simulation. If you have bumps or dips
in the ground, you must test and iterate on them to make sure you are happy
with the wheels’ behavior.

## Wheel collider visualization

When you select a Wheel collider, the **Scene view** An interactive view into
the world you are creating. You use the Scene View to select and position
scenery, characters, cameras, lights, and all other types of Game Object.
[More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) displays a
[gizmo](GizmosMenu.html)A graphic overlay associated with a GameObject in a
Scene, and displayed in the Scene View. Built-in scene tools such as the move
tool are Gizmos, and you can create custom Gizmos using textures or scripting.
Some Gizmos are only drawn when the GameObject is selected, while other Gizmos
are drawn by the Editor regardless of which GameObjects are selected. [More
info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) which provides a visualization of some
key Wheel collider properties.

![A single Wheel collider gizmo in the Scene view. In this screenshot, all
meshes are disabled in order to clearly display the
gizmo.](../uploads/Main/wheel-collider-gizmo.png) A single Wheel collider
gizmo in the Scene view. In this screenshot, all meshes are disabled in order
to clearly display the gizmo.

The gizmo’s visual indicators are as follows:

  * Large 2D circle: Represents the size of the physics wheel. To change the size, use the Wheel collider’s **Radius** property.
  * Horizontal green line: Represents the halfway point of the Wheel collider along the X axis. The angle of this line represents the rotation of the wheel.
  * Small 3D sphere: Represents the point where the wheel forces are applied. To change this value, use the Wheel collider’s **Force App Point Distance** property.
  * Vertical orange line: The top and bottom points of the line represent the maximum distances that the wheel can move up and down (along the vertical Y axis) from its central point as a result of forces applied to it. To change this value, use the Wheel collider’s **Suspension Distance** property. The point where the orange line intersects the green line represents the “resting” point where the wheel sits when there are no forces or equal forces acting upon it. To change this value, use the Wheel collider’s ****Target Position** A joint property to set the target position that the joint’s drive force should move it to. [More info](class-ConfigurableJoint.html)  
See in [Glossary](Glossary.html#TargetPosition)** property.

You can use the gizmo visualization for quick reference and debugging.

[](wheel-colliders.html)

Wheel colliders

[](wheel-colliders-friction.html)

Wheel collider friction

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

