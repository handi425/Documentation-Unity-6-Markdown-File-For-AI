[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/instantiating-prefabs-intro.html)
  * [中文](/cn/current/Manual/instantiating-prefabs-intro.html)
  * [日本語](/ja/current/Manual/instantiating-prefabs-intro.html)
  * [한국어](/kr/current/Manual/instantiating-prefabs-intro.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/instantiating-prefabs-intro.html)
  * [中文](/cn/current/Manual/instantiating-prefabs-intro.html)
  * [日本語](/ja/current/Manual/instantiating-prefabs-intro.html)
  * [한국어](/kr/current/Manual/instantiating-prefabs-intro.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Instantiating prefabs at runtime](instantiating-prefabs.html)
  * Introduction to instantiating prefabs

[](instantiating-prefabs.html)

Instantiating prefabs at runtime

[](instantiating-prefabs-structure.html)

Build a structure with prefabs

# Introduction to instantiating prefabs

To instantiate a **prefab** An asset type that allows you to store a
GameObject complete with components and properties. The prefab acts as a
template from which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) at runtime, your code needs a
reference to the prefab. To make this reference, you can create a public field
of type `GameObject` in your code, then assign the prefab you want to use to
this field in the **Inspector** A Unity window that displays information about
the currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

The script example below has a single public variable, `myPrefab`, which is a
reference to a prefab. It creates an instance of that prefab in the `Start`
method.

    
    
    using UnityEngine;
    public class InstantiationExample : MonoBehaviour 
    {
        // Reference to the Prefab. Drag a Prefab into this field in the Inspector.
        public GameObject myPrefab;
    
        // This script will simply instantiate the Prefab when the game starts.
        void Start()
        {
            // Instantiate at position (0, 0, 0) and zero rotation.
            Instantiate(myPrefab, new Vector3(0, 0, 0), Quaternion.identity);
        }
    }
    

To use this example:

  1. Create a new MonoBehaviour script in your Project, and name it `InstantiationExample`.
  2. Copy and the code above and paste it into your new script, and save it.
  3. Create an empty GameObject using the menu **GameObject** > **Create Empty**.
  4. Add the script to the new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) as a component by dragging it onto
the empty GameObject.

  5. [Create any Prefab](CreatingPrefabs.html), and drag it from the ****Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow)** into the **My Prefab** field
in the script component.

![Dragging a Prefab from the Project window into the My Prefab field in the
script component](../uploads/Main/PrefabDragIntoField.png) Dragging a Prefab
from the Project window into the My Prefab field in the script component

When you enter Play mode, you should see your prefab instantiate at position
(0, 0, 0) in the **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

You can drag a different prefab into the **My Prefab** field in the
**Inspector** window to change which prefab is instantiated, without having to
change the script.

Because this first example is very simple, it may not seem to provide any
advantage over just placing a prefab into the Scene yourself. However, being
able to instantiate prefabs using code provides you with powerful abilities to
dynamically create complex configurations of GameObjects while your game or
app is running, as shown in the other examples in this section.

## Common scenarios

Instantiating prefabs at runtime is useful in the following common scenarios:

  * Building a structure out of a single prefab by replicating it multiple times in different positions, for example in a grid or circle formation.

  * Firing a projectile prefab from a launcher. The projectile prefab could be a complex configuration containing a ****Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh)**, ****Rigidbody** A component that
allows a GameObject to be affected by simulated gravity and other forces.
[More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody)**, ****Collider** An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider)**, **AudioSource** , **Dynamic
Light** , and a child GameObject with its own trail ****Particle System** A
component that simulates fluid entities such as liquids, clouds and flames by
generating and animating large numbers of small 2D images in the scene. [More
info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem)**.

  * A vehicle, building, or character, for example a robot, breaking apart into many pieces. In this scenario, the example script deletes and replaces the complete, operational robot prefab with a wrecked robot prefab. This wrecked prefab consists of separate broken parts of the robot, each set up with Rigidbodies and Particle Systems of their own. This technique allows you to blow up a robot into many pieces, with just one line of code, which replaces the original GameObject with a wrecked prefab.

The following sections show you how to implement these scenarios.

## Additional resources

  * [Build a structure with prefabs](instantiating-prefabs-structure.html)
  * [Instantiate projectiles and explosions](instantiating-prefabs-projectiles.html)
  * [Simulate character destruction](instantiating-prefabs-wrecks.html)

[](instantiating-prefabs.html)

Instantiating prefabs at runtime

[](instantiating-prefabs-structure.html)

Build a structure with prefabs

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

