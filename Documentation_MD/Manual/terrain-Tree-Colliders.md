[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-Tree-Colliders.html)
  * [中文](/cn/current/Manual/terrain-Tree-Colliders.html)
  * [日本語](/ja/current/Manual/terrain-Tree-Colliders.html)
  * [한국어](/kr/current/Manual/terrain-Tree-Colliders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-Tree-Colliders.html)
  * [中文](/cn/current/Manual/terrain-Tree-Colliders.html)
  * [日本語](/ja/current/Manual/terrain-Tree-Colliders.html)
  * [한국어](/kr/current/Manual/terrain-Tree-Colliders.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * Add collision to trees

[](terrain-Tree-LOD.html)

Tree level of detail (LOD)

[](terrain-Trees.html)

Add trees to the terrain

# Add collision to trees

Colliders define the shape of an object and are used to calculate physical
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision). You can add a **collider** An
invisible shape that is used to handle physical collisions for an object. A
collider doesn’t need to be exactly the same shape as the object’s mesh - a
rough approximation is often more efficient and indistinguishable in gameplay.
[More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) to a tree asset in the Tree Editor
or to a SpeedTree asset in the SpeedTree Modeler.

## Set up the terrain to support tree colliders

On the **Terrain** The landscape in your scene. A Terrain GameObject adds a
large flat plane to your scene and you can use the Terrain’s Inspector window
to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) tile’s ****Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window, go to ****Terrain
Collider** A terrain-shaped collider component that handles collisions for
collision surface with the same shape as the Terrain object it is attached to.
[More info](class-TerrainCollider.html)  
See in [Glossary](Glossary.html#TerrainCollider)** and make sure **Enable Tree
Colliders** is selected.

**Note** : This option is enabled by default. If you disable it for one tile,
other tiles still enable it, including any new tiles you add.

## Add a collider to Tree Editor trees

To add a **Capsule Collider** A capsule-shaped collider component that handles
collisions for GameObjects like barrels and character limbs. [More
info](class-CapsuleCollider.html)  
See in [Glossary](Glossary.html#capsulecollider) to a tree asset, add it to
the tree’s **prefab** An asset type that allows you to store a GameObject
complete with components and properties. The prefab acts as a template from
which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab):

  1. In the **Hierarchy** window, click **>** next to the tree GameObject to open its prefab.
  2. In the prefab’s **Inspector** window, select **Add Component** > **Physics** > **Capsule Collider** to add the collider.
  3. For information on how to configure the collider, refer to [Capsule Collider component reference](class-CapsuleCollider.html).

To return to the **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), click **<** next to the prefab’s name.

The collider is added to the tree prefab, so you can now access it in the
**Inspector** window of the tree **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). If you’ve already added the tree
to the scene using the **Paint Trees** tool, the collider is added to all
instances of the tree.

## Add a collider to SpeedTree trees

If you created trees in the SpeedTrees Modeler with collision objects, the
Unity Editor accounts for the collision objects when it calculates colliders
on the terrain.

For more information, refer to the SpeedTree [Collision
object](https://docs9.speedtree.com/modeler/doku.php?id=collision_object)
documentation.

## Additional resources

  * [Terrain Collider component reference](class-TerrainCollider.html)
  * [Capsule Collider component reference](class-CapsuleCollider.html)
  * [Physics Collision](collision-section.html)

[](terrain-Tree-LOD.html)

Tree level of detail (LOD)

[](terrain-Trees.html)

Add trees to the terrain

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

