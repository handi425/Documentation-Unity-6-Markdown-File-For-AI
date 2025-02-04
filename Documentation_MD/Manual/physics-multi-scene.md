[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/physics-multi-scene.html)
  * [中文](/cn/current/Manual/physics-multi-scene.html)
  * [日本語](/ja/current/Manual/physics-multi-scene.html)
  * [한국어](/kr/current/Manual/physics-multi-scene.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/physics-multi-scene.html)
  * [中文](/cn/current/Manual/physics-multi-scene.html)
  * [日本語](/ja/current/Manual/physics-multi-scene.html)
  * [한국어](/kr/current/Manual/physics-multi-scene.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * Multi-scene physics

[](class-Cloth.html)

Cloth

[](PhysicsDebugVisualization.html)

Physics Debug window reference

# Multi-scene physics

You can use multiple physics Scenes to manage or work around complex physics
contexts. In particular, you can create and set up independent Scenes with
physics properties that are different from those of the main **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

![Example: trajectory prediction](../uploads/Main/physics-multi-scene-
pool.png) Example: trajectory prediction

## Use case examples

  * You can instantiate multiple physics Scenes based on the main Scene in order to predict **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) **collisions** A collision occurs
when the physics engine detects that the colliders of two GameObjects make
contact or overlap, when at least one has a Rigidbody component and is in
motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) and trajectories (as depicted
above).

  * You can isolate a very detailed character in its own physics Scene to more easily filter its collisions with elements of other physics Scenes.
  * You can create pre-populated physics Scenes to be able to entirely destroy and reload them in order to improve determinism in your physics environment.

## Creating and using independent physics Scenes

You can use [Multi-Scene editing](MultiSceneEditing.html) to create multiple
Scenes in general (although you can also instantiate them by script). However,
you have to use the Unity scripting API to use independent physics Scenes in
runtime.

More precisely, to get the expected physics results, you must write a script
that takes care at least of the following tasks for each separate physics
Scene:

  1. Load the Scene so that it’s independent from the main Scene.
  2. Get the Scene physics to set up the physics properties that you want to make different from the main Scene.
  3. Enable the Scene’s physics simulation – as it cannot auto-simulate.

[](class-Cloth.html)

Cloth

[](PhysicsDebugVisualization.html)

Physics Debug window reference

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

