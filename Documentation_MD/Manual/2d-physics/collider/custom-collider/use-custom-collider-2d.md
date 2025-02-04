[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)
  * [中文](/cn/current/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)
  * [中文](/cn/current/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [2D Physics](../../../2d-physics/2d-physics.html)
  * [Collider 2D](../../../2d-physics/collider/collider-2d-landing.html)
  * [Custom Collider 2D](../../../2d-physics/collider/custom-collider/custom-collider-2d-landing.html)
  * Use a Custom Collider 2D

[](../../../2d-physics/collider/custom-collider/custom-
collider-2d-reference.html)

Custom Collider 2D component reference

[](../../../2d-physics/collider/edit-collider-geometry.html)

Edit the collider's geometry

# Use a Custom Collider 2D

When assigning `PhysicsShape2D` to the Custom **Collider** An invisible shape
that is used to handle physical collisions for an object. A collider doesn’t
need to be exactly the same shape as the object’s mesh - a rough approximation
is often more efficient and indistinguishable in gameplay. [More
info](../../../CollidersOverview.html)  
See in [Glossary](../../../Glossary.html#Collider) 2D, you can do so either
during Edit mode or Play mode. When modifying the Custom Collider 2D in Edit
mode, Unity saves all assigned `PhysicsShape2D` and associated vertices in the
Unity **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../../../CreatingScenes.html)  
See in [Glossary](../../../Glossary.html#Scene), and the `CustomCollider2D`
retains its configuration when the Scene is loaded. This makes it possible to
use Edit mode authoring **scripts** A piece of code that allows you to create
your own Components, trigger game events, modify Component properties over
time and respond to user input in any way you like. [More
info](../../../creating-scripts.html)  
See in [Glossary](../../../Glossary.html#Scripts) to create custom geometry.

When modifying the Custom Collider 2D during Play mode, the Collider will not
retain any changes made to assigned `PhysicsShape2D` and their associated
vertices, and all changes will be lost when exiting Play mode.

[](../../../2d-physics/collider/custom-collider/custom-
collider-2d-reference.html)

Custom Collider 2D component reference

[](../../../2d-physics/collider/edit-collider-geometry.html)

Edit the collider's geometry

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

