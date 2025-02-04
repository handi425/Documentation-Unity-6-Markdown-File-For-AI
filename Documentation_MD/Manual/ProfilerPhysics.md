[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ProfilerPhysics.html)
  * [中文](/cn/current/Manual/ProfilerPhysics.html)
  * [日本語](/ja/current/Manual/ProfilerPhysics.html)
  * [한국어](/kr/current/Manual/ProfilerPhysics.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ProfilerPhysics.html)
  * [中文](/cn/current/Manual/ProfilerPhysics.html)
  * [日本語](/ja/current/Manual/ProfilerPhysics.html)
  * [한국어](/kr/current/Manual/ProfilerPhysics.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * Physics Profiler module

[](PhysicsDebugVisualization.html)

Physics Debug window reference

[](LightingOverview.html)

Lighting

# Physics Profiler module

The Physics **Profiler** A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module displays information about
the physics that the physics system has processed in your project’s **scene**
A Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). This information can help you diagnose
and resolve performance issues or unexpected discrepancies related to the
physics in your project’s scene. You can also use the [Physics Debug
Visualization](PhysicsDebugVisualization.html) to further debug and understand
issues with physics in your application.

To open the Profiler window, go to menu: **Window > Analysis > Profiler**.

![Physics Profiler module](../uploads/Main/profiler-physics-module.png)
Physics Profiler module

## Chart categories

The Physics Profiler module’s chart tracks the time your application spends on
physics. The timings are divided into different chart categories. To change
the order of the categories in the chart, you can drag them in the chart’s
legend. You can also click a category’s colored legend to toggle its display.
When you click on the chart, you can see the exact numerical values of each
chart category in the module details pane below the chart.

**Chart** | **Function**  
---|---  
**Physics Used Memory** | The total amount of memory that the physics module has used  
**Active Dynamic Bodies** | The number of [Rigidbody](../ScriptReference/Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) components and
[ArticulationBody](../ScriptReference/ArticulationBody.html) components that
aren’t in a [sleep](RigidbodiesOverview.html) state.  
**Active Kinematic Bodies** | The number of active Kinematic Rigidbody components. A Kinematic Rigidbody is active when [MovePosition](../ScriptReference/Rigidbody.MovePosition.html) or [MoveRotation](../ScriptReference/Rigidbody.MoveRotation.html) is called in a frame, and remains active in the next frame.  
  
**Note** : Unity might process Kinematic Rigidbody components that have joints
attached multiple times per frame, and this contributes to the value
displayed.  
**Dynamic Bodies** | The number of Rigidbody components and ArticulationBody components.  
**Overlaps** | The number of overlap events. An overlapping event is when [colliders](../ScriptReference/Collider.html)An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) overlap with each other.  
**Trigger Overlaps** | The number of overlap events with trigger colliders (counted in pairs).  
**Discreet Overlaps** | The number of overlap events which Unity used discrete **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection to solve.  
**Continuous Overlaps** | The number of overlap events which Unity used continuous **collision detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection) to solve.  
**Physics Queries** | The total amount of physics queries, such as [Raycasts](../ScriptReference/Physics.Raycast.html) and shapecasts.  
  
## Module details pane

When you click on the Physics Profiler module, the module details pane
displays further information about the physics in your project’s scene.

**Statistic** | **Description**  
---|---  
**Physics Used Memory** | The total amount of memory that the physics module has used.  
**Dynamic Bodies** | The number of [Rigidbody](../ScriptReference/Rigidbody.html) components and [ArticulationBody](../ScriptReference/ArticulationBody.html) components.  
**Articulation Bodies** | The number of ArticulationBody components in the scene  
**Active Dynamic Bodies** | The number of Rigidbody components and ArticulationBody components that aren’t in a [sleep](RigidbodiesOverview.html) state..  
**Active Kinematic Bodies** | The number of active Kinematic Rigidbody components. A Kinematic Rigidbody is active when [MovePosition](../ScriptReference/Rigidbody.MovePosition.html) or [MoveRotation](../ScriptReference/Rigidbody.MoveRotation.html) is called in a frame, and remains active in the next frame.  
  
**Note** : Unity might process Kinematic Rigidbody components that have joints
attached multiple times per frame, and this contributes to the value
displayed.  
**Static Colliders** | The number of [colliders](../ScriptReference/Collider.html) that don’t have a Rigidbody or ArticulationBody component  
**Colliders Synced** | The amount of colliders synced with [Transforms](../ScriptReference/Transform.html).  
**Rigidbodies Synced** | The amount of Rigidbody components synced with Transforms.  
**Physics Queries** | The total amount of physics queries, such as [Raycasts](../ScriptReference/Physics.Raycast.html) and shapecasts.  
**Total Overlaps** | The number of overlap events. An overlapping event is when colliders overlap with each other.  
| Discreet | The number of overlap events which Unity used **discrete collision detection** A collision detection method that calculates and resolves collisions based on the pose of objects at the end of each physics simulation step. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#discretecollisiondetection) to solve.  
| Continuous | The number of overlap events which Unity used **continuous collision detection** A collision detection method that calculates and resolves collisions over the entire physics simulation step. This can prevent fast-moving objects from tunnelling through walls during a simulation step. [More info](ContinuousCollisionDetection.html)  
See in [Glossary](Glossary.html#continuouscollisiondetection) to solve.  
| Trigger | The number of overlap events with trigger colliders (counted in pairs).  
| Modified | The number of overlap events which Unity used the [Contact Modification](../ScriptReference/Physics.ContactModifyEvent.html) API to modify.  
**Broadphase Adds/Removes** | The total number of colliders that the [broadphase algorithm](https://docs.nvidia.com/gameworks/content/gameworkslibrary/physx/guide/3.3.4/Manual/RigidBodyCollision.html#broad-phase-algorithms) either added or removed.  
**Narrowphase Touches** | The total amount of collision events that were either lost or appeared as new since the previous frame.  
  
The numbers displayed in the Profiler might not correspond to the exact number
of **GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with physics components in your
Scene. This is because Unity processes some physics components at a different
rate depending on which other components affect it (for example, an attached
Joint component). To calculate the exact number of GameObjects with specific
physics components attached, you must write a custom script with the
[FindObjectsOfType](../ScriptReference/Object.FindObjectsOfType.html)
function.

The Physics Profiler module doesn’t display the number of sleeping Rigidbody
components. These are components which don’t engage with the physics system,
so the Profiler doesn’t process them. For more information on sleeping
Rigidbody components, see the documentation on
[Rigidbody](RigidbodiesOverview.html).

## Understanding physics performance issues

The physics simulation runs on a separate fixed frequency update cycle from
the main logic’s update loop, and can only advance time via a
[Time.fixedDeltaTime](../ScriptReference/Time-fixedDeltaTime.html) per call.
This is similar to the difference between
[Update](../ScriptReference/MonoBehaviour.Update.html) and
[FixedUpdate](../ScriptReference/MonoBehaviour.FixedUpdate.html). For more
information on this, see the documentation on the [Time window](class-
TimeManager.html).

When a heavy logics or graphics frame takes a long amount of time, the
Profiler has to call the physics simulation multiple times per frame. This
means that an already resource-intensive frame takes even more time and
resources. This might cause the physics simulation to temporarily stop
according to the **Maximum Allowed Timestep** value, which you can set in the
Project Settings window (menu: **Edit > Project Settings > Time**)

To detect this in your Project, select the [CPU Usage Profiler
module](ProfilerCPU.html) and check the number of calls for
**Physics.Processing** or **Physics.Simulate** in the Overview section in the
**Hierarchy** view.

![CPU Usage Profiler with the value of 2 in the Calls
column](../uploads/Main/profiler-physics-cpu-module.png) CPU Usage Profiler
with the value of 2 in the **Calls** column

In this example image, the value of 2 in the Calls column indicates that the
physics simulation was called two times over the last logical frame.

A call count close to 10 might indicate an issue. As a first solution, reduce
the frequency of the physics simulation, and if the issue continues, check
what might have caused the heavy frame before the physics system had to use a
lot of simulation calls to catch up with the game time. Sometimes, a heavy
graphics frame might cause more physics simulation calls later on in a Scene.

For more detailed information about the physics simulation in your Scene,
select the search box at the top of the module details pane, search for
**Physics.Processing** , and then select **Calls** from the dropdown at the
top right of the pane. This displays the names of the physics system tasks
that run to update your Scene. The two most common names you’re likely to see
are:

  * **Pxs:** short for ‘PhysX solver’, which are physics system tasks that **joints** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) require as well as resolving contacts
for overlapping Rigidbody components.

  * **ScScene:** used for tasks that update the Scene, run the broad phase and narrow phase, and integrate Rigidbody components (moving them in space due to forces and impulses).

## Legacy Physics Profiler module

You can switch to the **Legacy** mode to see the older version of the Physics
Profiler module, which was the default module in older versions of Unity. To
do this, select **Legacy** from the dropdown menu in the top right of the
Physics Profiler module’s details pane.

In this mode, you can load and inspect Profiler data that was saved in an
older version of Unity. If you switch to this mode to inspect data captured in
a newer version of Unity, then the data displayed is unreliable and
inaccurate. You should always use the **Current** mode to inspect new Physics
Profiler data.

![CPU Usage Profiler in Legacy mode](../uploads/Main/profiler-physics-legacy-module.png) CPU Usage Profiler in Legacy mode **Statistic** | **Description**  
---|---  
**Active Dynamic** | The number of active non-Kinematic Rigidbody components. An active Rigidbody is one that isn’t [sleeping](RigidbodiesOverview.html).  
**Active Kinematic** | The number of active Kinematic Rigidbody components. A Kinematic Rigidbody is active when [MovePosition](../ScriptReference/Rigidbody.MovePosition.html) or [MoveRotation](../ScriptReference/Rigidbody.MoveRotation.html) is called in a frame, and remains active in the next frame.  
  
**Note:** Unity might process Kinematic Rigidbody components that have joints
attached multiple times per frame, and this contributes to the value
displayed.  
**Static Colliders** | The number of Collider components on GameObjects that don’t have Rigidbody components attached to the GameObjects or their parent GameObjects.  
  
Collider components on GameObjects or parent GameObjects that have Rigidbody
components do not count as Static Colliders. These are called Compound
Colliders. Compound Colliders arrange multiple Colliders of a body in a
convenient way, rather than having all of the Colliders on the same GameObject
as the Rigidbody component.  
**Rigidbody** | The number of Rigidbody components processed by the physics system, irrespective of the components’ sleeping state.  
**Trigger Overlaps** | The number of overlapping triggers (counted in pairs).  
**Active Constraints** | The number of primitive constraints the physics system has processed. Constraints are used as a building block of Joints as well as collision response. For example, restricting a linear or rotational degree of freedom of a [ConfigurableJoint](../ScriptReference/ConfigurableJoint.html) involves a primitive constraint per each restriction.  
**Contacts** | The total number of contact pairs between all Colliders in the Scene, including the amount of trigger overlap pairs. A contact is a pair of Colliders that either touch or overlap. Note: Unity creates contact pairs per Collider pair once the distance between them is below a certain user configurable limit. As such, you might see contacts generated for Rigidbody components that are not yet touching or overlapping. See documentation on [Collider.contactOffset](../ScriptReference/Collider-contactOffset.html) and [ContactPoint.separation](../ScriptReference/ContactPoint-separation.html) for more details.  
  
## Additional resources

  * [Profiler window introduction](ProfilerWindow.html)
  * [Profiling your application](profiler-profiling-applications.html)

[](PhysicsDebugVisualization.html)

Physics Debug window reference

[](LightingOverview.html)

Lighting

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

