[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/physics-profiler/physics-2d-profiler-module-reference.html)
  * [中文](/cn/current/Manual/2d-physics/physics-profiler/physics-2d-profiler-module-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/physics-profiler/physics-2d-profiler-module-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/physics-profiler/physics-2d-profiler-module-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/physics-profiler/physics-2d-profiler-module-reference.html)
  * [中文](/cn/current/Manual/2d-physics/physics-profiler/physics-2d-profiler-module-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/physics-profiler/physics-2d-profiler-module-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/physics-profiler/physics-2d-profiler-module-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Physics 2D Profiler](../../2d-physics/physics-profiler/physics-2d-profiler-landing.html)
  * Physics 2D Profiler module reference

[](../../2d-physics/physics-profiler/physics-2d-profiler-landing.html)

Physics 2D Profiler

[](../../2d-physics/physics-profiler/use-physics-profiler-legacy-mode.html)

Use the Physics Profiler Legacy mode

# Physics 2D Profiler module reference

The Physics 2D **Profiler** A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](../../Profiler.html)  
See in [Glossary](../../Glossary.html#Profiler) module displays information
about the physics that the physics system has processed in your project’s
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene). This information can help you
diagnose and resolve performance issues or unexpected discrepancies related to
the physics in your project’s scene.

To open the Profiler window, go to menu: **Window** > **Analysis** >
**Profiler**.

## Chart categories

The Physics 2D Profiler module’s chart tracks different statistics related to
the physics that the physics system processes in the project’s scene, divided
into the following chart categories. Click on the frame chart window or select
a captured frame in the chart graph to track selected categories. To change
the order of the categories in the chart, drag and drop them in the chart’s
legend. You can also click a category’s colored legend to toggle its display.
Refer to the module details pane for more information about the selected
statistics.

**Chart** | **Description**  
---|---  
**Total Contacts** | The total number of contacts that were present in this frame. This includes both **Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision) and Trigger contacts.
Processing and solving contacts can be time consuming therefore they should be
kept to a minimum.  
**Total Shapes** | The total number of [physics shapes](../../../ScriptReference/PhysicsShape2D.html) that were present in this frame. Different [Collider2D](../../../ScriptReference/Collider2D.html) produce different amounts of physics shapes ranging from one to unlimited. You can get the [shape count](../../../ScriptReference/Collider2D-shapeCount.html) and [retrieve the physics shapes](../../../ScriptReference/Collider2D.GetShapes.html) to determine this for any Collider2D.  
**Total Queries** | The total number of queries that were called this frame. This includes queries such as [Physics2D.Raycast](../../../ScriptReference/Physics2D.Raycast.html), [Physics2D.OverlapPoint](../../../ScriptReference/Physics2D.OverlapPoint.html) etc.  
**Total Callbacks** | The total number of [OnCollisionEnter2D](../../../ScriptReference/Collider2D.OnCollisionEnter2D.html), [OnCollisionStay2D](../../../ScriptReference/Collider2D.OnCollisionStay2D.html), [OnCollisionExit2D](../../../ScriptReference/Collider2D.OnCollisionExit2D.html), [OnTriggerEnter2D](../../../ScriptReference/Collider2D.OnTriggerEnter2D.html), [OnTriggerStay2D](../../../ScriptReference/Collider2D.OnTriggerStay2D.html) and [OnTriggerExit2D](../../../ScriptReference/Collider2D.OnTriggerExit2D.html) callbacks that were called in this frame.  
**Total**Joints** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint)** | The total number of any [Joint2D](../../../ScriptReference/Joint2D.html) that were present in this frame.  
**Total Bodies** | The total number of [Rigidbody2D](../../../ScriptReference/Rigidbody2D.html) that were present in this frame.  
**Awake Bodies** | The total number of Rigidbody2D that were both [awake](../../../ScriptReference/Rigidbody2D.IsAwake.html) (not [sleeping](../../../ScriptReference/Rigidbody2D.IsSleeping.html)) and were present in this frame.  
**Dynamic Bodies** | The total number of Rigidbody2D with a [Dynamic](../../../ScriptReference/RigidbodyType2D.Dynamic.html) **body type** Defines a fixed behavior for a 2D Rigidbody. Can be Dynamic (the body moves under simulation and is affected by forces like gravity), Kinematic (the body moves under simulation, but and isn’t affected by forces like gravity) or Static (the body doesn’t move under simulation). [More info](../../2d-physics/rigidbody/introduction-to-rigidbody-2d.html)  
See in [Glossary](../../Glossary.html#BodyType) that were present in this
frame. Dynamic bodies take the most processing of all body types therefore
they should be kept to a minimum.  
**Continuous Bodies** | The total number of Rigidbody2D with a [Continuous](../../../ScriptReference/CollisionDetectionMode2D.Continuous.html) **collision detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#CollisionDetection) mode that were
present in this frame. Continuous bodies are much more expensive than when
using **Discrete collision detection** A collision detection method that
calculates and resolves collisions based on the pose of objects at the end of
each physics simulation step. [More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#discretecollisiondetection) mode
therefore they should be kept to a minimum.  
**Physics Used Memory** | The total amount of persistent memory used exclusively by the 2D physics system. This includes both the core engine and the memory used by each physics component, but does not include the temporary memory used in this frame.  
  
## Module details pane

When you select a frame in the Physics 2D Profiler module, the details pane
displays detailed information about the physics in your project’s scene. The
details pane is sorted by category, where each category exists on a single
line.

The following reference table describes the statistics available, plus its
corresponding **profiler counter** Placed in code with the ProfilerCounter API
to track metrics, such as the number of enemies spawned in your game. [More
info](../../https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-
guide.html)  
See in [Glossary](../../Glossary.html#Profilercounter), and availability in
Release builds. The profiler counters are always available in the Editor and
**Development builds** A development build includes debug symbols and enables
the Profiler. [More info](../../https://docs.unity.com/devops/en/manual/build-
target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](../../Glossary.html#DevelopmentBuild). This information is
also available via the [ProfilerRecorder
API](../../../ScriptReference/Unity.Profiling.ProfilerRecorder.html) and in
the [Profiler Module Editor](../../profiler-module-editor.html) so you can add
them to a custom Profiler module.

### Physics Used Memory

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Total** | The total amount of persistent memory used exclusively by the 2D physics system. This includes both the core engine and the memory used by each physics component, but does not include temporary memory used in this frame. | Physics Used Memory 2D | No  
**Relative** | The relative percentage of memory used by the 2D physics system compared to the overall memory usage of Unity. | N/A | N/A  
  
### Bodies

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Total** | The total number of [Rigidbody2D](../../../ScriptReference/Rigidbody2D.html) that were present in this frame. | Total Bodies | No  
**Awake** | The number of Rigidbody2D that were both [awake](../../../ScriptReference/Rigidbody2D.IsAwake.html) (not [sleeping](../../../ScriptReference/Rigidbody2D.IsSleeping.html)) and were present in this frame. Note that a Rigidbody2D with a [Static](../../../ScriptReference/RigidbodyType2D.Static.html) body type is always asleep. | Awake Bodies | No  
**Asleep** | The number of Rigidbody2D that were both sleeping (not awake) and were present in this frame. Note that a Rigidbody2D with a Static body type is always asleep. | Asleep Bodies | No  
**Dynamic** | The number of Rigidbody2D with a [Dynamic](../../../ScriptReference/RigidbodyType2D.Dynamic.html) body type that were present in this frame. Dynamic bodies take the most processing of all body types therefore they should be kept to a minimum. | Dynamic Bodies | No  
**Kinematic** | The number of Rigidbody2D with a [Kinematic](../../../ScriptReference/RigidbodyType2D.Kinematic.html) body type that were present in this frame. Kinematic bodies have minimal processing therefore they should be used when explicit movement is required but reaction to external forces is not. | Kinematic Bodies | No  
**Static** | The number of Rigidbody2D with a [Static](../../../ScriptReference/RigidbodyType2D.Static.html) body type that were present in this frame. Static bodies take the least processing of all body types therefore they should be used when possible where no movement is required. | Static Bodies | No  
**Discrete** | The number of Rigidbody2D with a [Discrete](../../../ScriptReference/CollisionDetectionMode2D.Discrete.html) collision detection mode that were present in this frame. Discrete bodies are far less expensive than when using [Continuous](../../../ScriptReference/CollisionDetectionMode2D.Continuous.html) collision detection mode therefore they should be used where possible. | Discrete Bodies | No  
**Continuous** | The number of Rigidbody2D with a [Continuous](../../../ScriptReference/CollisionDetectionMode2D.Continuous.html) collision detection mode that were present in this frame. Continuous bodies are much more expensive than when using Discrete collision detection mode therefore they should be kept to a minimum. | Continuous Bodies | No  
  
### Shapes

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Total** | The total number of [physics shapes](../../../ScriptReference/PhysicsShape2D.html) that were present in this frame.. Different [Collider2D](../../../ScriptReference/Collider2D.html) produce different amounts of physics shapes ranging from one to unlimited. You can get the [shape count](../../../ScriptReference/Collider2D-shapeCount.html) and [retrieve the physics shapes](../../../ScriptReference/Collider2D.GetShapes.html) to determine this for any Collider2D. | Total Shapes | No  
**Awake** | A physics shape is awake if it is attached to a [Rigidbody2D](../../../ScriptReference/Rigidbody2D.html) that is [awake](../../../ScriptReference/Rigidbody2D.IsAwake.html). This is the number of physics shapes that were both awake (not [sleeping](../../../ScriptReference/Rigidbody2D.IsSleeping.html)) and were present in this frame. | Awake Shapes | No  
**Asleep** | A physics shape is asleep if it is attached to a Rigidbody2D that is asleep. This is the number of physics shapes that were both sleeping (not awake) and were present in this frame. | Asleep Shapes | No  
**Dynamic** | A physics shape is [Dynamic](../../../ScriptReference/RigidbodyType2D.Dynamic.html) if it is attached to a Rigidbody2D with a Dynamic body type. This is the number of physics shapes that were both Dynamic and were present in this frame. | Dynamic Shapes | No  
**Kinematic** | A physics shape is Dynamic if it is attached to a Rigidbody2D with a [Kinematic](../../../ScriptReference/RigidbodyType2D.Kinematic.html) body type. This is the number of physics shapes that were both Kinematic and were present in this frame. | Kinematic Shapes | No  
**Static** | A physics shape is Dynamic if it is attached to a Rigidbody2D with a [Static](../../../ScriptReference/RigidbodyType2D.Static.html) body type. This is the number of physics shapes that were both Static and were present in this frame. | Static Shapes | No  
  
### Queries

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Total** | The total number of queries that were called this frame. This includes queries such as [Physics2D.Raycast](../../../ScriptReference/Physics2D.Raycast.html), and [Physics2D.OverlapPoint](../../../ScriptReference/Physics2D.OverlapPoint.html). | Total Queries | No  
**Raycast** | The number of ray or line based queries that were called this frame. This includes queries such as Physics2D.Raycast and [Physics2D.Linecast](../../../ScriptReference/Physics2D.Linecast.html). | Raycast Queries | No  
**Shapecast** | The number of shape swept queries that were called this frame. This includes queries such as [Physics2D.BoxCast](../../../ScriptReference/Physics2D.BoxCast.html), [Physics2D.CircleCast](../../../ScriptReference/Physics2D.CircleCast.html), and [Collider2D.Cast](../../../ScriptReference/Collider2D.Cast.html). | Shapecast Queries | No  
**Overlap** | The number of overlap queries that were called this frame. This includes queries such as [Physics2D.OverlapPoint](../../../ScriptReference/Physics2D.OverlapPoint.html), [Physics2D.OverlapCircle](../../../ScriptReference/Physics2D.OverlapCircle.html), and [Collider2D.OverlapCollider](../../../ScriptReference/Collider2D.OverlapCollider.html). | Overlap Queries | No  
**IsTouching** | The number of contact touching queries that were called this frame. This includes queries such as [Physics2D.IsTouching](../../../ScriptReference/Physics2D.IsTouching.html), [Collider2D.IsTouching](../../../ScriptReference/Collider2D.IsTouching.html), [Rigidbody2D.IsTouching](../../../ScriptReference/Rigidbody2D.IsTouchingLayers.html) etc. | IsTouching Queries | No  
**GetContacts** | The number of contact retrieval queries that were called this frame. This includes queries such as [Physics2D.GetContacts](../../../ScriptReference/Physics2D.GetContacts.html), [Collider2D.GetContacts](../../../ScriptReference/Collider2D.GetContacts.html), and [Rigidbody2D.GetContacts](../../../ScriptReference/Rigidbody2D.GetContacts.html). Note that this does not include [Collision2D.GetContacts](../../../ScriptReference/Collision2D-contacts.html) which is not a physics query. | GetContacts Queries | No  
**Particle** | The number of queries that were called by the **particle system** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](../../class-ParticleSystem.html)  
See in [Glossary](../../Glossary.html#particlesystem) in this frame. This is
used when the particle system module is configured to contact 2D physics
**Colliders** An invisible shape that is used to handle physical collisions
for an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) and is entirely controlled by the particle system. Note that this can become quite high but is also very efficient to process. | Particle Queries | No  
  
### Contacts

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Total** | The total number of contacts that were present in this frame. This includes both Collision and Trigger contacts. Processing and solving contacts can be time consuming therefore they should be kept to a minimum. | Total Contacts | No  
**Added** | The number of contacts that were added in this frame. This includes both Collision and Trigger contacts. Adding too many contacts in a single frame can cause performance spikes therefore this should be kept to a minimum. | Added Contacts | No  
**Removed** | The number of contacts that were removed in this frame. This includes both Collision and Trigger contacts. Removing contacts is fast and has minimum impact on performance. | Removed Contacts | No  
**Broadphase Updates** | The number of broadphase updates that were processed in this frame. A broadphase update occurs when physics shapes are added, removed or change in size. Broadphase updates are used to detect contact changes when two physics shapes potentially overlap and can result in a broadphase pair (see below) being created. | Broadphase Updates | No  
**Broadphase Pairs** | The number of broadphase pairs that were processed in this frame. A broadphase pair is created when a broadphase update results in a potential overlap of two physics shapes. A broadphase pair is then processed and the result will be a new contact or it will be ignored if the physics shapes are not configured to contact each other. | Broadphase Pairs | No  
  
### Callbacks

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Total** | The total number of [OnCollisionEnter2D](../../../ScriptReference/Collider2D.OnCollisionEnter2D.html), [OnCollisionStay2D](../../../ScriptReference/Collider2D.OnCollisionStay2D.html), [OnCollisionExit2D](../../../ScriptReference/Collider2D.OnCollisionExit2D.html), [OnTriggerEnter2D](../../../ScriptReference/Collider2D.OnTriggerEnter2D.html), [OnTriggerStay2D](../../../ScriptReference/Collider2D.OnTriggerStay2D.html) and [OnTriggerExit2D](../../../ScriptReference/Collider2D.OnTriggerExit2D.html) callbacks that were called in this frame. | Total Callbacks | No  
**Collision Enter** | The number of OnCollisionEnter2D callbacks that were called in this frame. | Collision Enter | No  
**Collision Stay** | The number of OnCollisionStay2D callbacks that were called in this frame. | Collision Stay | No  
**Collision Exit** | The number of OnCollisionExit2D callbacks that were called in this frame. | Collision Exit | No  
**Trigger Enter** | The number of OnTriggerEnter2D callbacks that were called in this frame. | Trigger Enter | No  
**Trigger Stay** | The number of OnTriggerStay2D callbacks that were called in this frame. | Trigger Stay | No  
**Trigger Exit** | The number of OnTriggerExit2D callbacks that were called in this frame. | Trigger Exit | No  
  
### Solver

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**World Count** | The total number of [physics scene](../../../ScriptReference/PhysicsScene2D.html) that were present in this frame. Each physics scene contains a physics world that can be simulated independently of any other physics world. Having a large number of worlds is not in of itself a performance issue because it will only occupy memory and not perform any work unless it is simulated. | Solver World Count | No  
**Simulation Count** | The number of times all physics scene were simulated either by Unity automatically, by calling [Physics2D.Simulate](../../../ScriptReference/Physics2D.Simulate.html) or by directly calling [PhysicsScene2D.Simulate](../../../ScriptReference/PhysicsScene2D.Simulate.html). | Solver Simulation Count | No  
**Discrete Islands** | An island is a connected graph of bodies connected via mutual joints or mutual contacts. Note that [Static](../../../ScriptReference/RigidbodyType2D.Static.html) body types do not connect islands. The number of contact islands solved when handling the discrete solving step. | Solver Discrete Islands | No  
**Continuous Islands** | An island is a connected graph of bodies connected via mutual joints or mutual contacts. Note that Static body types do not connect islands. This is the number of islands solved when handling the continuous solving step. Solving continuous islands is an extremely expensive process and involves multiple iterations that require islands to be regenerated and reprocessed so this should be kept to a minimum. Only a [Rigidbody2D](../../../ScriptReference/Rigidbody2D.html) with a [Continuous](../../../ScriptReference/CollisionDetectionMode2D.Continuous.html) collision detection mode will result in this additional continuous island being formed and processed. | Solver Continuous Islands | No  
  
### Transform Sync

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Sync Calls** | The total number of Transform sync calls that were called in this frame. A Transform sync (known as a Transform Read) involves checking to see if any Transforms have changed and if so, the Transform poses are read and cause any [Rigidbody2D](../../../ScriptReference/Rigidbody2D.html) or [Collider2D](../../../ScriptReference/Collider2D.html) to be updated. Transforms should not be changed when using physics components however sometimes this is necessary but should be avoided due to potential performance issues if performing too many. Any movements should be performed by using the Rigidbody2D API.  
  
The physics system will perform a single Transform sync as the first part of
performing a simulation step so this will always be at least one if a
simulation occurred (see Simulation Count above). The physics system will also
perform a single Transform sync per-frame if it is handling any Rigidbody2D
interpolation.  
  
Additional calls are shown if either [Physics2D.AutoSyncTransforms](../../../ScriptReference/Physics2D-autoSyncTransforms.html) is active (inactive by default) or if [Physics2D.SyncTransforms](../../../ScriptReference/Physics2D.SyncTransforms.html) is called although both of these should be avoided as they can both have a severe impact on performance. | Total Transform Sync Calls | No  
**Sync Bodies** | The number of Rigidbody2D that were affected by a Transform sync. This should be kept to a minimum, preferably zero. | Transform Sync Bodies | No  
**Sync Colliders** | The number of Collider2D that were affected by a Transform sync. This should be kept to a minimum, preferably zero. | Transform Sync Colliders | No  
**Parent Sync Bodies** | The number of Rigidbody2D that were affected by a Transform sync caused by reparenting a Transform.. This should be kept to a minimum, preferably zero. | Transform Parent Sync Bodies | No  
**Parent Sync Colliders** | The number of Collider2D that were affected by a Transform sync caused by reparenting a Transform. This should be kept to a minimum, preferably zero. | Transform Parent Sync Colliders | No  
  
### Joints

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Total** | The total number of any [Joint2D](../../../ScriptReference/Joint2D.html) that were present in this frame. Solving joints can become expensive so these should be kept to a minimum. | Total Joints | No  
  
### Timings

**Note** : All timings are summed over all physics worlds (see World Count).
The number of times any timing was sampled is shown in square brackets after
the timing itself. Effectively the timing can be divided by the **World
Count** value to give an average time.

**Statistic** | **Description** | **Corresponding Profiler Counter (exact name)** | **Available in Release Players?**  
---|---|---|---  
**Sim** | The total amount of time spent handling a full simulation step. This can be called by Unity automatically, by calling [Physics2D.Simulate](../../../ScriptReference/Physics2D.Simulate.html) or by directly calling [PhysicsScene2D.Simulate](../../../ScriptReference/PhysicsScene2D.Simulate.html). This time includes all the stages involved in completing a simulation step including Transform Sync (read), Calculating Contacts, Integration, Solving Contacts and Joints, Transform Write and Contact Callbacks. | N/A | N/A  
**Sync** | The total amount of time spent processing Transform Sync (see Sync Calls). | N/A | N/A  
**Step** | The total amount of time spent processing simulation steps. This time includes only the core stages involved in completing a simulation step including Calculating Contacts, Integration, Solving Contacts and Joints. | N/A | N/A  
**Write** | The total amount of time spent processing Transform write. This happens during the end of the simulation step where body poses are read and written back to the Transform system. | N/A | N/A  
**Callbacks** | The total amount of time spent processing all callbacks (see Total Callbacks). | N/A | N/A  
  
## Additional resources

  * [Profiler window introduction](../../ProfilerWindow.html)
  * [Profiling your application](../../profiler-profiling-applications.html)

[](../../2d-physics/physics-profiler/physics-2d-profiler-landing.html)

Physics 2D Profiler

[](../../2d-physics/physics-profiler/use-physics-profiler-legacy-mode.html)

Use the Physics Profiler Legacy mode

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

