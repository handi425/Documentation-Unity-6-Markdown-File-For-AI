[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-counters-reference.html)
  * [中文](/cn/current/Manual/profiler-counters-reference.html)
  * [日本語](/ja/current/Manual/profiler-counters-reference.html)
  * [한국어](/kr/current/Manual/profiler-counters-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-counters-reference.html)
  * [中文](/cn/current/Manual/profiler-counters-reference.html)
  * [日本語](/ja/current/Manual/profiler-counters-reference.html)
  * [한국어](/kr/current/Manual/profiler-counters-reference.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * Profiler counters reference

[](profiler-markers.html)

Profiler markers reference

[](performance-profiling-tools.html)

Profiling tools

# Profiler counters reference

Unity has built-in [profiler counters](profiler-adding-information-code-
intro.html#profiler-counters)Placed in code with the ProfilerCounter API to
track metrics, such as the number of enemies spawned in your game. [More
info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-
guide.html)  
See in [Glossary](Glossary.html#Profilercounter) which you can use to collect
and display metrics in custom **Profiler** A window that helps you to optimize
your game. It shows how much time is spent in the various areas of your game.
For example, it can report the percentage of time spent rendering, animating,
or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) modules. The following tables
outline the available built-in profiler counters. This information is also
available via the
[`ProfilerRecorder`](../ScriptReference/Unity.Profiling.ProfilerRecorder.html)
API and in the [Profiler module editor](profiler-module-editor.html) so you
can add them to a custom Profiler module. The following tables contain a list
of profiler counters available in Unity:

  * File access profiler counters
  * Asset loading profiler counters
  * Memory profiler counters
  * Physics profiler counters
  * 2D Physics profiler counters
  * Rendering profiler counters
  * Virtual texturing profiler counters

## File access profiler counters

The available file access profiler counters and availability in release (non-
development) players are as follows:

**Profiler counter** | **Description** | **Availability in release (non-development) players**  
---|---|---  
**File Bytes Read** | Total number of bytes of information Unity read from this file during the selected frames. | Unavailable  
**File Bytes Written** | Total number of bytes of information Unity wrote to this file during the selected frames. | Unavailable  
**File Handles Open** | The total number of file handles held open at any time during this frame. This includes files that Unity opens and closes within the same frame. | Unavailable  
**File Reads Finished** | Number of file reads completed during this frame. | Unavailable  
**File Reads Started** | Number of file reads started during this frame | Unavailable  
**File Seeks** | The number of file seek operations performed in the local file system this frame. A file seek operation involves a search through the contents of a file. | Unavailable  
**Files Closed** | The total number of files successfully closed in the local file system this frame. | Unavailable  
**Files Opened** | The total number of files successfully opened in the local file system this frame. | Unavailable  
**Reads in Flight** | The total number of read operations that were in progress during this frame. | Unavailable  
  
For more information about collecting file access data, refer to [File Access
Profiler module reference](profiler-file-access-module.html).

## Asset loading profiler counters

The available asset loading profiler counters and availability in release
(non-development) players are as follows:

**Profiler counter** | **Description** | **Availability in release (non-development) players**  
---|---|---  
**Audio Reads** | The number of bytes requested from the AsyncReadManager for an audio load. | Unavailable  
**Entities Reads** | The number of bytes requested from the AsyncReadManager by **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in the [Entities package](https://docs.unity3d.com/Packages/com.unity.entities@latest/). | Unavailable  
**Mesh Reads** | The number of bytes requested from the AsyncReadManager for a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) load. | Unavailable  
**Other Reads** | The number of bytes requested from the AsyncReadManager for an unspecified subsystem. | Unavailable  
**Scripting Reads** | The number of bytes requested from the AsyncReadManager via the scripting API. | Unavailable  
**Texture Reads** | The number of bytes requested from the AsyncReadManager for a texture load. | Unavailable  
**Virtual Texture Reads** | The number of bytes requested from the AsyncReadManager for Virtual Texturing. | Unavailable  
  
For more information about collecting asset data, refer to [Asset Loading
Profiler module reference](profiler-asset-loading-module.html).

## Memory profiler counters

The following table outlines the available memory profiler counters and
availability in release (non-development) players.

**Tip:** You can use the
[`Object.FindObjectsByType`](../ScriptReference/Object.FindObjectsByType.html)
method to find objects of specific types, and then pass this information to
[`Profiler.GetRuntimeMemorySizeLong`](../ScriptReference/Profiling.Profiler.GetRuntimeMemorySizeLong.html)
to get their memory amount and then implement this information in release
players. For example, to get the counters for Mesh Count or Mesh Memory, use
`Object.FindObjectsByType<Mesh>().length` and then pass these entries to
`GetRunTimeMemorySizeLong`.

`GetRunTimeMemorySizeLong` has an impact on performance, and doesn’t provide
graphics memory amounts in release builds.

**Profiler counter** | **Description** | **Availability in release (non-development) players**  
---|---|---  
**AnimationClip Count** | The total count of loaded AnimationClips. | Unavailable  
**AnimationClip Memory** | The total amount of memory loaded AnimationClips used in bytes. | Unavailable  
**App Committed Memory** | The total amount of committed memory according to the operating system of the platform in bytes. | Available  
**App Resident Memory** | The total amount of resident memory according to the operating system of the platform in bytes. | Available  
**Asset Count** | The total number of loaded assets. | Unavailable  
**Audio Reserved Memory** | The Audio system’s estimated reserved memory in bytes. | Available  
**Audio Used Memory** | The Audio system’s estimated memory usage in bytes. | Available  
**AudioClip Count** | The total count of loaded AudioClips. | Unavailable  
**AudioClip Memory** | The total amount of memory loaded AudioClips used in bytes. | Unavailable  
****GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) Count** | The total number of GameObject instances in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). | Unavailable  
**GC Allocated In Frame** | The total size of the managed allocations in the selected frame in bytes. | Unavailable  
**GC Allocation In Frame Count** | The amount of managed allocations in the selected frame. | Unavailable  
**GC Reserved Memory** | The total heap size reserved for managed code in bytes. This memory is [garbage collected](performance-garbage-collector.html). | Available  
**GC Used Memory** | The used heap size that managed code uses in bytes. This memory is [garbage collected](performance-garbage-collector.html). | Available  
**Gfx Reserved Memory** | The estimated amount of reserved memory for Textures, render targets, **Shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), and Mesh data in bytes. | Unavailable  
**Gfx Used Memory** | The estimated amount of memory the driver uses on Textures, render targets, Shaders, and Mesh data in bytes. | Unavailable  
**Material Count** | The total count of loaded materials. | Unavailable  
**Material Memory** | The total amount of memory loaded materials used in bytes. | Unavailable  
**Mesh Count** | The total count of loaded Meshes. | Unavailable  
**Mesh Memory** | The total amount of memory loaded Meshes used in bytes. | Unavailable  
**Object Count** | The number of native object instances in your application. | Unavailable  
**Physics Used Memory** | The total amount of memory that the physics system used in bytes. | Unavailable  
**Physics Reserved Memory(2D)** | The total amount of memory that the 2D physics system reserved in bytes. | Unavailable  
**Profiler Reserved Memory** | The memory that the Profiler functionality reserves from the system in bytes. | Available  
**Profiler Used Memory** | The memory that the Profiler functionality uses in bytes. | Available  
**Scene Object Count** | The total number of dynamic `UnityEngine.Object` instances. This number includes the GameObject Count counter, plus the total number of components, and everything which isn’t an asset in the scene. | Unavailable  
**System Total Used Memory** | The total memory used by all applications running on the device in bytes. | Available  
**System Used Memory** | The total amount of resident memory according to the operating system of the platform in bytes. This value is the same as the **App Resident Memory** value. | Available  
**Texture Count** | The total count of loaded textures | Unavailable  
**Texture Memory** | The total amount of memory loaded textures used in bytes. | Unavailable  
**Total Reserved Memory** | The total memory reserved in the operating system for your application in bytes. | Available  
**Total Used Memory** | The total memory your application used in bytes. | Available  
**Video Reserved Memory** | The Video system’s estimated reserved memory in bytes. | Available  
**Video Used Memory** | The Video system’s estimated memory usage in bytes. | Available  
  
For more information about collecting memory data, refer to [Memory
performance data](profiler-memory.html).

## Physics profiler counters

The available physics profiler counters and availability in release (non-
development) players are as follows:

**Profiler counter** | **Description** | **Availability in release (non-development) players**  
---|---|---  
**Active Constraints** | The number of primitive constraints the physics system has processed. | Unavailable  
**Active Dynamic Bodies** | The number of [Rigidbody](../ScriptReference/Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) components and [`ArticulationBody`](../ScriptReference/ArticulationBody.html) components that aren’t in a [sleep](RigidbodiesOverview.html) state. | Unavailable  
**Active Kinematic Bodies** | The number of active Kinematic Rigidbody components. | Unavailable  
**Articulation Bodies** | The number of `ArticulationBody` components in the scene | Unavailable  
**Broadphase Adds** | The total number of colliders that the [broadphase algorithm](https://docs.nvidia.com/gameworks/content/gameworkslibrary/physx/guide/3.3.4/Manual/RigidBodyCollision.html#broad-phase-algorithms) added. | Unavailable  
**Broadphase Adds/Removes** | The total number of colliders that the broadphase algorithm either added or removed. | Unavailable  
**Broadphase Removes** | The total number of colliders that the broadphase algorithm removed. | Unavailable  
**Colliders Synced** | The amount of colliders synced with [Transforms](../ScriptReference/Transform.html). | Unavailable  
**Continuous Overlaps** | The number of overlap events which Unity used continuous **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection to solve. | Unavailable  
**Discreet Overlaps** | The number of overlap events which Unity used discrete **collision detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection) to solve. | Unavailable  
**Dynamic Bodies** | The number of [`Rigidbody`](../ScriptReference/Rigidbody.html) components and [`ArticulationBody`](../ScriptReference/ArticulationBody.html) components. | Unavailable  
**Modified Overlaps** | The number of overlap events which Unity used the [Contact Modification](../ScriptReference/Physics.ContactModifyEvent.html) API to modify. | Unavailable  
**Narrowphase Lost Touches** | The total amount of collision events that were lost since the previous frame. | Unavailable  
**Narrowphase New Touches** | The total amount of collision events that appeared as new since the previous frame. | Unavailable  
**Narrowphase Touches** | The total amount of collision events that were either lost or appeared as new since the previous frame. | Unavailable  
**Overlaps** | The number of overlap events. An overlapping event is when colliders overlap with each other. | Unavailable  
**Physics Queries** | The total amount of physics queries, such as [Raycasts](../ScriptReference/Physics.Raycast.html) and shapecasts. | Unavailable  
**Rigidbodies Synced** | The amount of Rigidbody components synced with Transforms. | Unavailable  
**Static Colliders** | The number of [colliders](../ScriptReference/Collider.html)An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) that don’t have a Rigidbody or ArticulationBody component | Unavailable  
**Trigger Overlaps** | The number of overlap events with trigger colliders (counted in pairs). | Unavailable  
  
For more information about collecting physics data, refer to [Physics Profiler
module reference](ProfilerPhysics.html).

## 2D Physics profiler counters

The available 2D physics profiler counters and availability in release (non-
development) players are as follows:

**Profiler counter** | **Description** | **Availability in release (non-development) players**  
---|---|---  
**Added Contacts** | The number of contacts added in this frame. This includes both Collision and Trigger contacts. | Unavailable  
**Asleep Bodies** | The number of Rigidbody2D that were sleeping (not awake) and present in this frame. | Unavailable  
**Asleep Shapes** | The number of physics shapes that were sleeping (not awake) and present in this frame. | Unavailable  
**Awake Bodies** | The number of Rigidbody2D that were awake and present in this frame. | Unavailable  
**Awake Shapes** | The number of physics shapes that were awake and present in this frame. | Unavailable  
**Broadphase Pairs** | The number of broadphase pairs that the physics system processed in this frame. | Unavailable  
**Broadphase Updates** | The number of broadphase updates that the physics system processed in this frame. | Unavailable  
**Collision Enter** | The number of OnCollisionEnter2D callbacks that the physics system called in this frame. | Unavailable  
**Collision Exit** | The number of OnCollisionExit2D callbacks that the physics system called in this frame. | Unavailable  
**Collision Stay** | The number of OnCollisionStay2D callbacks that the physics system called in this frame. | Unavailable  
**Continuous Bodies** | The number of Rigidbody2D with a [`Continuous`](../ScriptReference/CollisionDetectionMode2D.Continuous.html) collision detection mode that were present in this frame. | Unavailable  
**Discrete Bodies** | The number of Rigidbody2D with a [`Discrete`](../ScriptReference/CollisionDetectionMode2D.Discrete.html) collision detection mode that were present in this frame. | Unavailable  
**Dynamic Bodies** | The number of Rigidbody2D with a [`Dynamic`](../ScriptReference/RigidbodyType2D.Dynamic.html) **body type** Defines a fixed behavior for a 2D Rigidbody. Can be Dynamic (the body moves under simulation and is affected by forces like gravity), Kinematic (the body moves under simulation, but and isn’t affected by forces like gravity) or Static (the body doesn’t move under simulation). [More info](2d-physics/rigidbody/introduction-to-rigidbody-2d.html)  
See in [Glossary](Glossary.html#BodyType) that were present in this frame. | Unavailable  
**Dynamic Shapes** | The number of physics shapes that were both [`Dynamic`](../ScriptReference/RigidbodyType2D.Dynamic.html) and were present in this frame. | Unavailable  
**GetContacts Queries** | The number of contact retrieval queries that the physics system called this frame. This includes queries such as [`Physics2D.GetContacts`](../ScriptReference/Physics2D.GetContacts.html), [`Collider2D.GetContacts`](../ScriptReference/Collider2D.GetContacts.html), and [`Rigidbody2D.GetContacts`](../ScriptReference/Rigidbody2D.GetContacts.html). | Unavailable  
**IsTouching Queries** | The number of contact touching queries that the physics system called this frame. This includes queries such as [`Physics2D.IsTouching`](../ScriptReference/Physics2D.IsTouching.html), [`Collider2D.IsTouching`](../ScriptReference/Collider2D.IsTouching.html), and [`Rigidbody2D.IsTouching`](../ScriptReference/Rigidbody2D.IsTouchingLayers.html). | Unavailable  
**Kinematic Bodies** | The number of Rigidbody2D with a [`Kinematic`](../ScriptReference/RigidbodyType2D.Kinematic.html) body type that were present in this frame. | Unavailable  
**Overlap Queries** | The number of overlap queries that the physics system called this frame. This includes queries such as [`Physics2D.OverlapPoint`](../ScriptReference/Physics2D.OverlapPoint.html), [`Physics2D.OverlapCircle`](../ScriptReference/Physics2D.OverlapCircle.html), and [`Collider2D.OverlapCollider`](../ScriptReference/Collider2D.OverlapCollider.html). | Unavailable  
**Particle Queries** | The number of queries that the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) called in this frame. | Unavailable  
**Raycast Queries** | The number of ray or line based queries that the physics system called this frame. This includes queries such as `Physics2D.Raycast` and [`Physics2D.Linecast`](../ScriptReference/Physics2D.Linecast.html). | Unavailable  
**Removed Contacts** | The number of contacts that the physics system removed in this frame. This includes both Collision and Trigger contacts. | Unavailable  
**Shapecast Queries** | The number of shape swept queries that the physics system called this frame. This includes queries such as [`Physics2D.BoxCast`](../ScriptReference/Physics2D.BoxCast.html), [`Physics2D.CircleCast`](../ScriptReference/Physics2D.CircleCast.html), and [`Collider2D.Cast`](../ScriptReference/Collider2D.Cast.html). | Unavailable  
**Solver Continuous Islands** | The number of islands solved when handling the continuous solving step. | Unavailable  
**Solver Discrete Islands** | The number of contact islands solved when handling the discrete solving step. | Unavailable  
**Solver Simulation Count** | The number of times Unity simulated all physics scenes automatically, or by calling [`Physics2D.Simulate`](../ScriptReference/Physics2D.Simulate.html) or [`PhysicsScene2D.Simulate`](../ScriptReference/PhysicsScene2D.Simulate.html). | Unavailable  
**Solver World Count** | The total number of [physics scenes](../ScriptReference/PhysicsScene2D.html) that were present in this frame. | Unavailable  
**Static Bodies** | The number of Rigidbody2D with a [`Static`](../ScriptReference/RigidbodyType2D.Static.html) body type that were present in this frame. | Unavailable  
**Static** | The number of physics shapes that were both Static and were present in this frame. | Unavailable  
**Total Bodies** | The total number of [`Rigidbody2D`](../ScriptReference/Rigidbody2D.html) that were present in this frame. | Unavailable  
**Total Callbacks** | The total number of [`OnCollisionEnter2D`](../ScriptReference/Collider2D.OnCollisionEnter2D.html), [`OnCollisionStay2D`](../ScriptReference/Collider2D.OnCollisionStay2D.html), [`OnCollisionExit2D`](../ScriptReference/Collider2D.OnCollisionExit2D.html), [OnTriggerEnter2D](../ScriptReference/Collider2D.OnTriggerEnter2D.html), [`OnTriggerStay2D`](../ScriptReference/Collider2D.OnTriggerStay2D.html) and [`OnTriggerExit2D`](../ScriptReference/Collider2D.OnTriggerExit2D.html) callbacks that the physics system called in this frame. | Unavailable  
**Total Contacts** | The total number of contacts that were present in this frame. This includes both Collision and Trigger contacts. | Unavailable  
**Total**Joints** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint)** | The total number of any [`Joint2D`](../ScriptReference/Joint2D.html) that were present in this frame. | Unavailable  
**Total Shapes** | The total number of [physics shapes](../ScriptReference/PhysicsShape2D.html) that were present in this frame. | Unavailable  
**Total Queries** | The total number of queries that the physics system called this frame. This includes queries such as [`Physics2D.Raycast`](../ScriptReference/Physics2D.Raycast.html) and [`Physics2D.OverlapPoint`](../ScriptReference/Physics2D.OverlapPoint.html) | Unavailable  
**Total Transform Sync Calls** | The total number of Transform sync calls that the physics system called in this frame. | Unavailable  
**Transform Parent Sync Bodies** | The number of Rigidbody2D that were affected by a Transform sync caused by reparenting a Transform. | Unavailable  
**Transform Parent Sync Colliders** | The number of Collider2D that were affected by a Transform sync caused by reparenting a Transform. | Unavailable  
**Transform Sync Bodies** | The number of Rigidbody2D that were affected by a Transform sync. | Unavailable  
**Transform Sync Colliders** | The number of Collider2D that were affected by a Transform sync. | Unavailable  
**Trigger Enter** | The number of OnTriggerEnter2D callbacks that were called in this frame. | Unavailable  
**Trigger Exit** | The number of OnTriggerExit2D callbacks that were called in this frame. | Unavailable  
**Trigger Stay** | The number of OnTriggerStay2D callbacks that were called in this frame. | Unavailable  
  
For more information about collecting 2D physics data, refer to [2D Physics
Profiler module reference](2d-physics/physics-profiler/physics-2d-profiler-
module-reference.html).

## Rendering profiler counters

The available rendering profiler counters and availability in release (non-
development) players are as follows:

**Profiler counter** | **Description** | **Availability in release (non-development) players**  
---|---|---  
**Batches Count** | The total number of [batches](DrawCallBatching.html) Unity processed during a frame. This number includes both static and dynamic batches. | Available  
**CPU Main Thread Frame Time** | The time between the start of the frame and the time when the Main Thread finished the work it performed during that frame, in milliseconds. | Available  
**CPU Render Thread Frame Time** | The time between the start of the work on the Render Thread and when Unity calls the `Present` method, in milliseconds. | Available  
**CPU Total Frame Time** | The total CPU frame time, in milliseconds. Unity calculates this as the time between the ends of two frames, including any overheads or time spent waiting between frames. | Available  
**Draw Calls Count** | The total number of draw calls Unity issued during a frame. | Available  
**Dynamic Batched Draw Calls Count** | The number of draw calls Unity combined into dynamic batches. | Unavailable  
**Dynamic Batched Triangles Count** | The number of triangles in the GameObjects included in the dynamic batches. | Unavailable  
**Dynamic Batched Vertices Count** | The number of vertices in the GameObjects included in the dynamic batches. | Unavailable  
**Dynamic Batches Count** | The number of dynamic batches Unity processed during the frame. | Unavailable  
****Dynamic Batching** An automatic Unity process which attempts to render
multiple meshes as if they were a single mesh for optimized graphics
performance. The technique transforms all of the GameObject vertices on the
CPU and groups many similar vertices together. [More
info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) Time** | The time Unity spent creating dynamic batching structures. | Unavailable  
**GPU Frame Time** | The time difference between the beginning and the end of the GPU rendering a single frame, in milliseconds. | Available  
**Index Buffer Upload In Frame Bytes** | The amount of geometry that the CPU uploaded to the GPU in bytes. | Available  
**Index Buffer Upload In Frame Count** | The amount of geometry that the CPU uploaded to the GPU in the frame. | Available  
**Instanced Batched Draw Calls Count** | The number of draw calls Unity combined into instance batches. | Unavailable  
**Instanced Batched Triangles Count** | The number of triangles in the instanced GameObjects. | Unavailable  
**Instanced Batched Vertices Count** | The number of vertices in the instanced GameObjects. | Unavailable  
**Instanced Batches Count** | The number of batches Unity processed to render [instanced](GPUInstancing.html) GameObjects during a frame. | Unavailable  
****Render Textures** A special type of Texture that is created and updated at
runtime. To use them, first create a new Render Texture and designate one of
your Cameras to render into it. Then you can use the Render Texture in a
Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) Bytes** | The amount of memory the RenderTextures used in bytes. | Available  
**Render Textures Changes Count** | The number of times Unity set one or multiple RenderTextures as render targets during the frame. | Available  
**Render Textures Count** | The number of [RenderTextures](class-RenderTexture.html) Unity used during the frame. | Available  
**SetPass Calls Count** | The number of times Unity switched which shader pass it used to render GameObjects during a frame. | Available  
**Shadow Casters Count** | The number of GameObjects that cast shadows in a frame. If a GameObject casts multiple shadows (because multiple lights light it), it has one entry per shadow it casts. | Available  
**Static Batched Draw Calls Count** | The number of draw calls Unity combined into static batches. | Unavailable  
**Static Batched Triangles Count** | The number of triangles in the GameObjects included in the static batches. | Unavailable  
**Static Batched Vertices Count** | The number of vertices in the GameObjects included in the static batches. | Unavailable  
**Static Batches Count** | The number of static batches Unity processed during a frame. | Unavailable  
**Triangles Count** | The number of [triangles](../ScriptReference/Mesh-triangles.html) Unity processed during a frame. | Available  
**Used Buffers Bytes** | The amount of memory GPU buffers used in bytes. | Available  
**Used Buffers Count** | The total number of GPU buffers. This includes vertex, index and compute buffers and all internal buffers required for rendering. | Available  
**Used Textures Bytes** | The amount of memory the textures used in bytes. | Unavailable  
**Used Textures Count** | The number of [textures](Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) Unity used during the frame. | Unavailable  
**Vertex Buffer Upload In Frame Bytes** | The amount of geometry that the CPU uploaded to the GPU in bytes. | Available  
**Vertex Buffer Upload In Frame Count** | The amount of geometry that the CPU uploaded to the GPU in the frame. | Available  
**Vertices Count** | The number of [vertices](../ScriptReference/Mesh-vertices.html) Unity processed during the frame. | Available  
**Video Memory Bytes** | The amount of system memory the video in your application used in bytes. | Available  
**Visible Skinned Meshes Count** | The number of [Skinned Mesh Renderers](class-SkinnedMeshRenderer.html) in the frame. | Available  
  
For more information about collecting rendering data, refer to [Rendering
Profiler module reference](ProfilerRendering.html).

## Virtual texturing profiler counters

The available virtual texturing profiler counters and availability in release
(non-development) players are as follows:

**Profiler counter** | **Description** | **Availability in release (non-development) players**  
---|---|---  
**Atlases** | The number of virtual texture spaces or atlases (maximum of 64). | Unavailable  
**Max Cache Demand** | The highest cache demand of all GPU caches in the selected frame. | Unavailable  
**Max Cache Mip Bias** | The automatic mipmap bias applied to all textures with the same **texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat). If this value isn’t zero, then the cache isn’t large enough to hold all the tiles of that format that are visible. The higher the mipmap bias, the lower the texture quality. | Unavailable  
**Missing Disk Data** | The remaining data (in bytes) that your application needed to read from the disk to satisfy the selected frame. | Unavailable  
**Missing Streaming Tiles** | The number of tiles that were visible on the screen but weren’t in video memory. | Unavailable  
**Read From Disk** | The number of bytes of disk read operations that Unity completed in the selected frame. | Unavailable  
**Required Tiles** | The number of texture tiles that were visible on screen. These are the tiles that the shaders tried to sample to render the selected frame. | Unavailable  
**Total CPU Cache Size** | The amount of memory that Unity allocated to store texture tiles after it loaded them from disk. | Unavailable  
**Total GPU Cache Size** | The size of all GPU caches that the Virtual Texturing module allocated in the selected frame. | Unavailable  
  
For more information about collecting virtual texturing data, refer to
[Virtual Texturing module reference](profiler-virtual-texturing-module.html).

## Additional resources

  * [Adding profiler counters to your code](profiler-add-counters-code.html)
  * [Customizing Profiler modules](profiler-customizing.html)
  * [Profiler module editor reference](profiler-module-editor.html)

[](profiler-markers.html)

Profiler markers reference

[](performance-profiling-tools.html)

Profiling tools

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

