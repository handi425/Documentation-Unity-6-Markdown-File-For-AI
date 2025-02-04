[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/object-oriented-development.html)
  * [中文](/cn/current/Manual/object-oriented-development.html)
  * [日本語](/ja/current/Manual/object-oriented-development.html)
  * [한국어](/kr/current/Manual/object-oriented-development.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/object-oriented-development.html)
  * [中文](/cn/current/Manual/object-oriented-development.html)
  * [日本語](/ja/current/Manual/object-oriented-development.html)
  * [한국어](/kr/current/Manual/object-oriented-development.html)

  * [Scripting](scripting.html)
  * Object-oriented development

[](dotnet-garbage-collection.html)

Garbage collection

[](managing-time-and-frame-rate.html)

Managing time and frame rate

# Object-oriented development

Traditional Unity projects are object-oriented in two related ways:

  * They embrace the object-oriented programming philosophy, which is grounded in the concept of objects, their properties and functions, and the relations between these objects.
  * The original architecture of Unity projects uses an object-based model with types derived from `UnityEngine.Object`. In this model, **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) are composed of GameObjects which in
turn interact with and are controlled by objects of other types.

An alternative to object-oriented development is data-oriented development,
which is both a programming philosophy and a set of technologies that help you
implement those principles. The data-oriented approach offers strong
performance advantages at scale but can be more challenging for inexperienced
developers to learn.

Object-oriented and data-oriented development are not mutually exclusive and
you can combine elements from both. For information on data-oriented
development, refer to [Unity’s Data-Oriented Technology
Stack](https://unity.com/dots).

**Topic** | **Description**  
---|---  
[Managing time and frame rate](managing-time-and-frame-rate.html) | Understand how Unity measures time so you can manage the rate at which time passes in your application and ensure values update according to the appropriate time scale.  
[Instantiating prefabs at runtime](instantiating-prefabs.html) | Instantiate **prefabs** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) programmatically to create structures
and impressive effects in your game with relatively little code.  
[Handling events](event-handling.html) | Make your application responsive to events such as user input, object **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision), and physics and rendering updates.  
[Splitting tasks across frames](Coroutines.html) | Split the execution of a task synchronously across multiple scenes with coroutines. This can be useful for tasks that should progress gradually over several frames, such as a fade out effect.  
[Interacting with web servers](web-request.html) | Use the UnityWebRequest system to allow your application to interact with a web server via HTTP.  
[Adding functionality to objects at runtime](properties.html) | Use the Unity Properties API to implement a visitor design pattern and add new operations to .NET objects at runtime.  
[Moving objects with vectors](scripting-vectors.html) | Use vectors to move objects in a specific direction and magnitude in 2, 3, and 4 dimensions.  
[Using common math functions](class-Mathf.html) | Use common math functions, including trigonometric, logarithmic, and other functions in your application.  
[Using randomness](class-Random.html) | Generate commonly required types of random values.  
[Gizmos and Handles](gizmos-and-handles.html) | Draw lines and shapes in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) and Game view, as well as
interactive handles and controls.  
[Null references](null-reference-exception.html) | Understand and diagnose null reference exceptions in Unity projects.  
[Unity attributes](unity-attributes.html) | Use Unity-specific C# attributes to define special behavior for your code.  
  
## Additional resources

  * [Unity’s Data-Oriented Technology Stack](https://unity.com/dots)
  * [GameObject](class-GameObject.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)

[](dotnet-garbage-collection.html)

Garbage collection

[](managing-time-and-frame-rate.html)

Managing time and frame rate

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

