[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/renderer/set-sort-point-sprite.html)
  * [中文](/cn/current/Manual/sprite/renderer/set-sort-point-sprite.html)
  * [日本語](/ja/current/Manual/sprite/renderer/set-sort-point-sprite.html)
  * [한국어](/kr/current/Manual/sprite/renderer/set-sort-point-sprite.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/renderer/set-sort-point-sprite.html)
  * [中文](/cn/current/Manual/sprite/renderer/set-sort-point-sprite.html)
  * [日本語](/ja/current/Manual/sprite/renderer/set-sort-point-sprite.html)
  * [한국어](/kr/current/Manual/sprite/renderer/set-sort-point-sprite.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sprite Renderer](../../sprite/renderer/renderer-landing.html)
  * Set the sort point of a sprite

[](../../sprite/renderer/change-color-sprite.html)

Change the color of a sprite

[](../../sprite/renderer/sprite-renderer-reference.html)

Sprite Renderer reference

# Set the sort point of a sprite

This property is only available when the **Sprite** A 2D graphic objects. If
you are used to working in 3D, Sprites are essentially just standard textures
but there are special techniques for combining and managing sprite textures
for efficiency and convenience during development. [More
info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) Renderer’s **Draw Mode** is set
to **Simple**.

In a 2D project, the Main **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) is set to [Orthographic
Projection mode](../../class-Camera.html) by default. In this mode, Unity
renders sprites in the order of their distance to the camera, along the
direction of the Camera’s view.

![Orthographic Camera: Side view \(top\) and Game view
\(bottom\)](../../../uploads/Main/2DSpriteRenderer_SortPoint.png)
**Orthographic Camera:** Side view (top) and Game view (bottom)

By default, a Sprite’s **Sort Point** is set to its **Center** , and Unity
measures the distance between the camera’s Transform position and the Center
of the Sprite to determine their render order.

To set to a different **Sort Point** from the Center, select the **Pivot**
option. Edit the Sprite’s Pivot position in the [Sprite Editor](../sprite-
editor/sprite-editor-landing.html).

* * *

SpriteRenderer

[](../../sprite/renderer/change-color-sprite.html)

Change the color of a sprite

[](../../sprite/renderer/sprite-renderer-reference.html)

Sprite Renderer reference

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

