[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LayerBasedCollision.html)
  * [中文](/cn/current/Manual/LayerBasedCollision.html)
  * [日本語](/ja/current/Manual/LayerBasedCollision.html)
  * [한국어](/kr/current/Manual/LayerBasedCollision.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LayerBasedCollision.html)
  * [中文](/cn/current/Manual/LayerBasedCollision.html)
  * [日本語](/ja/current/Manual/LayerBasedCollision.html)
  * [한국어](/kr/current/Manual/LayerBasedCollision.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * [Layers](Layers.html)
  * Layer-based collision detection

[](create-layers.html)

Create functional layers in Unity

[](layers-and-layermasks.html)

Layers and layerMasks

# Layer-based collision detection

Layer-based **collision** A collision occurs when the physics engine detects
that the colliders of two GameObjects make contact or overlap, when at least
one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection is a way to make a
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) collide with another GameObject
that is set up to a specific Layer or Layers.

![Objects colliding with their own
layer](../uploads/Main/LayerBasedCollision.png) Objects colliding with their
own layer

The image above shows six GameObjects (3 planes, 3 cubes) in the **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view, and the **Layer Collision
Matrix** in the window to the right. The Layer Collision Matrix defines which
GameObjects can collide with which Layers.

In the example, the Layer Collision Matrix is set up so that only GameObjects
that belong to the same layer can collide:

  * Layer 1 is checked for Layer 1 only
  * Layer 2 is checked for Layer 2 only
  * Layer 3 is checked for Layer 3 only

Change this to suit your needs: if, for example, you want Layer 1 to collide
with Layer 2 and 3, but not with Layer 1, find the row for **Layer 1** , then
check the boxes for the **Layer 2** and **Layer 3** colums, and leave the
**Layer 1** column checkbox blank.

## Setting up layer-based collision detection

  1. To select a Layer for your GameObjects to belong to, select the GameObject, navigate to the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, select the **Layer**
dropdown at the top, and either choose a Layer or add a new Layer. Repeat for
each GameObject until you have finished assigning your GameObjects to Layers.
![](../uploads/Main/LayerBasedCollisionLayer.png)

  2. In the Unity menu bar, go to **Edit** > **Project Settings** , then select the **Physics** category to open the [Physics](class-PhysicsManager.html) window.
  3. Select which layers on the Collision Matrix will interact with the other layers by checking them. ![](../uploads/Main/LayerCollisionMatrix.png)

[](create-layers.html)

Create functional layers in Unity

[](layers-and-layermasks.html)

Layers and layerMasks

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

