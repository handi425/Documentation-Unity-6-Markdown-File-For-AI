[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/instantiating-prefabs-wrecks.html)
  * [中文](/cn/current/Manual/instantiating-prefabs-wrecks.html)
  * [日本語](/ja/current/Manual/instantiating-prefabs-wrecks.html)
  * [한국어](/kr/current/Manual/instantiating-prefabs-wrecks.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/instantiating-prefabs-wrecks.html)
  * [中文](/cn/current/Manual/instantiating-prefabs-wrecks.html)
  * [日本語](/ja/current/Manual/instantiating-prefabs-wrecks.html)
  * [한국어](/kr/current/Manual/instantiating-prefabs-wrecks.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Instantiating prefabs at runtime](instantiating-prefabs.html)
  * Replace a character with a ragdoll or wreck

[](instantiating-prefabs-projectiles.html)

Instantiate projectiles and explosions

[](event-handling.html)

Handling events

# Replace a character with a ragdoll or wreck

In a game you might want to switch an asset such as a character, vehicle, or
building from an intact state to a destroyed state. Rather than modifying the
intact version of the GameObject (by removing scripts, adding Rigidbody
components and so on), it’s often more efficient and effective to delete the
intact GameObject and replace it with an instantiated destroyed prefab.

This gives you a lot of flexibility. You could use a different Material for
the destroyed version, attach completely different **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), or instantiate a prefab containing
the GameObject broken into many pieces to represent a wrecked or shattered
state. Any of these options can be achieved with a single call to
`Instantiate`, to bring your destroyed version into the **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), while deleting the original.

Most importantly, you can create the destroyed version which you `Instantiate`
with completely different GameObjects compared to the original. For example,
to create a breakable robot, you would model two versions: one that consists
of a single GameObject with **Mesh** The main graphics primitive of Unity.
Meshes make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer and scripts for robot movement,
and the other that consists of several skeletal parts that can be controlled
individually by physics.

Your game runs faster when using the model with just one GameObject, because
the model contains fewer triangles and so it renders faster than the robot
that has many small parts. Also while your robot is happily walking around,
there is no reason to have it in separate parts.

## Build a wrecked robot prefab without code

To build a wrecked robot prefab without code:

  1. Model your robot with lots of different skeletal parts in your favorite 3D modeling software, and export it into the Assets folder of your Unity Project.

  2. Create an empty Scene in the Unity Editor.

  3. Drag the model from the **Project** window into the empty Scene.

  4. Add Rigidbodies to all parts, by selecting all the parts and choosing **Component > Physics > Rigidbody.**

  5. Add Colliders to all parts by selecting all the parts and choosing **Component > Physics > Mesh Collider** (enable the **Convex** option for faster performance).

  6. Make sure you parent all the parts of your wrecked robot to a single root GameObject.

  7. For an extra special effect, add a smoke-like **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) as a child GameObject to each
of the parts.

  8. Now you have a robot with multiple explodable parts. The parts can fall to the ground because they are controlled by physics, and each part creates a Particle trail due to the attached Particle System. 

  9. Click Play to preview how your model reacts, and make any necessary tweaks.

  10. Drag the root GameObject into the **Assets** folder in the **Project** window to create a new Prefab.

## Build a wrecked robot prefab from code

The following example shows how you can model these steps in code:

    
    
    using UnityEngine;
    public class WreckOnCollision : MonoBehaviour
    {
       public GameObject wreckedVersion;
    
       void OnCollisionEnter()
       {
           Destroy(gameObject);
           Instantiate(wreckedVersion,transform.position,transform.rotation);
       }
    }
    

![An example of a robot Prefab being swapped for a wrecked Prefab when hit by
a projectile](../uploads/Main/PrefabWreckSwap.gif) An example of a robot
Prefab being swapped for a wrecked Prefab when hit by a projectile

You can download a Project containing all these example, here:
**[InstantiatingPrefabsExamples.zip](../uploads/Examples/InstantiatingPrefabsExamples.zip)**

## Additional resources

  * [Prefabs](Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab)

  * [GameObject](class-GameObject.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)

[](instantiating-prefabs-projectiles.html)

Instantiate projectiles and explosions

[](event-handling.html)

Handling events

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

