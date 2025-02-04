[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sort-sprites/sort-sprites.html)
  * [中文](/cn/current/Manual/sprite/sort-sprites/sort-sprites.html)
  * [日本語](/ja/current/Manual/sprite/sort-sprites/sort-sprites.html)
  * [한국어](/kr/current/Manual/sprite/sort-sprites/sort-sprites.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sort-sprites/sort-sprites.html)
  * [中文](/cn/current/Manual/sprite/sort-sprites/sort-sprites.html)
  * [日本語](/ja/current/Manual/sprite/sort-sprites/sort-sprites.html)
  * [한국어](/kr/current/Manual/sprite/sort-sprites/sort-sprites.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sprites sorting order](../../sprite/sort-sprites/sort-sprites-landing.html)
  * Sort sprites

[](../../sprite/sort-sprites/sort-sprites-landing.html)

Sprites sorting order

[](../../sprite/sort-sprites/sort-sprites-using-scripts.html)

Sort sprites using scripts

# Sort sprites

Unity’s Graphics settings (menu: **Edit** > **Project Settings** >
**Graphics**) provide a setting called **Transparency Sort Mode** , which you
can use to control how to sort sprites depending on their position in relation
to the Camera. More specifically, it uses the sprite’s position on an axis to
determine which ones are transparent compared to others.

An example of when you might use this setting is to sort **sprites** A 2D
graphic objects. If you are used to working in 3D, Sprites are essentially
just standard textures but there are special techniques for combining and
managing sprite textures for efficiency and convenience during development.
[More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) along the y-axis. This is quite
common in 2D games, where sprites that are higher up the y-axis are sorted
behind sprites that are lower, to make them appear further away.

**Notes:**

  * If you set the **Transparency Sort Mode** to **Custom Axis** , you also need to set the **Transparency Sort Axis**.

  * If the **Transparency Sort Mode** is set to **Custom Axis** , renderers in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) view are sorted based on the
distance of this axis from the **camera** A component which creates an image
of a particular viewpoint in your scene. The output is either drawn to the
screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera). Use a value between –1 and 1 to
define the axis. For example: X=0, Y=1, Z=0 sets the axis direction to up.
X=1, Y=1, Z=0 sets the axis to a diagonal direction between X and Y.

![Example: Set the Transparency Sort Mode to Custom Axis, and set the Y value
for the Transparency Sort Axis to a value higher than
0.](../../../uploads/Main/AxisDistanceSort2.png) Example: Set the
**Transparency Sort Mode** to **Custom Axis** , and set the **Y** value for
the **Transparency Sort Axis** to a value higher than 0.

[](../../sprite/sort-sprites/sort-sprites-landing.html)

Sprites sorting order

[](../../sprite/sort-sprites/sort-sprites-using-scripts.html)

Sort sprites using scripts

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

