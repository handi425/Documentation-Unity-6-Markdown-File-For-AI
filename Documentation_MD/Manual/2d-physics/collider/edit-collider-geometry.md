[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/collider/edit-collider-geometry.html)
  * [中文](/cn/current/Manual/2d-physics/collider/edit-collider-geometry.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/edit-collider-geometry.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/edit-collider-geometry.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/collider/edit-collider-geometry.html)
  * [中文](/cn/current/Manual/2d-physics/collider/edit-collider-geometry.html)
  * [日本語](/ja/current/Manual/2d-physics/collider/edit-collider-geometry.html)
  * [한국어](/kr/current/Manual/2d-physics/collider/edit-collider-geometry.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Collider 2D](../../2d-physics/collider/collider-2d-landing.html)
  * Edit the collider's geometry

[](../../2d-physics/collider/custom-collider/use-custom-collider-2d.html)

Use a Custom Collider 2D

[](../../2d-physics/collider/edit-collider-mode-reference.html)

Edit Collider mode reference

# Edit the collider’s geometry

You can edit a **collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider)’s geometry manually or have
Unity generate its shape automatically.

Unity automatically generates a collider’s geometry when you drag a **sprite**
A 2D graphic objects. If you are used to working in 3D, Sprites are
essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) into the **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) and add a Collider 2D component
to it. The generated collider shape matches the outline of the sprite as close
as possible.

To edit the collider’s shape:

  1. Select **Edit Collider** ![](../../../uploads/Main/edit-collider-inspector-icon.png) in the Inspector window to edit the collider’s geometry. You can also access the collider’s editing mode from the Tools overlay in the Scene view window.  
![](../../../uploads/Main/edit-collider-overlay.png)

  2. To move an existing vertex, select and hold it, then move it to a new location.
  3. To create a new vertex, hover your cursor over the outline of the collider’s shape. A dot shows the position of the cursor on the collider’s geometry. Click on the dot to create a new vertex at that position.
  4. To remove a vertex, hold Ctrl (macOS:Cmd) while hovering your cursor over the edges of the collider’s geometry, which turn red. Click the red edges to remove the vertex that connects them.
  5. Exit the collider editing mode by selecting **Edit Collider** in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../UsingTheInspector.html)  
See in [Glossary](../../Glossary.html#Inspector) window or Tools overlay
again.

[](../../2d-physics/collider/custom-collider/use-custom-collider-2d.html)

Use a Custom Collider 2D

[](../../2d-physics/collider/edit-collider-mode-reference.html)

Edit Collider mode reference

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

