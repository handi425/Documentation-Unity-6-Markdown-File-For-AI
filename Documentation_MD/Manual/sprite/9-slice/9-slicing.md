[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/9-slice/9-slicing.html)
  * [中文](/cn/current/Manual/sprite/9-slice/9-slicing.html)
  * [日本語](/ja/current/Manual/sprite/9-slice/9-slicing.html)
  * [한국어](/kr/current/Manual/sprite/9-slice/9-slicing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/9-slice/9-slicing.html)
  * [中文](/cn/current/Manual/sprite/9-slice/9-slicing.html)
  * [日本語](/ja/current/Manual/sprite/9-slice/9-slicing.html)
  * [한국어](/kr/current/Manual/sprite/9-slice/9-slicing.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Various image sizes without multiple assets](../../sprite/9-slice/9-slice-landing.html)
  * 9-slicing

[](../../sprite/9-slice/9-slice-landing.html)

Various image sizes without multiple assets

[](../../sprite/9-slice/set-sprite-9slicing.html)

Set up your sprite for 9-slicing

# 9-slicing

9-slicing is a 2D technique which allows you to reuse an image at various
sizes without needing to prepare multiple
[Assets](../../AssetWorkflow.html)Any media or data that can be used in your
game or project. An asset may come from a file created outside of Unity, such
as a 3D Model, an audio file or an image. You can also create some asset types
in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture.
[More info](../../AssetWorkflow.html)  
See in [Glossary](../../Glossary.html#Asset). It involves splitting the image
into nine portions, so that when you re-size the [Sprite](../sprite-
landing.html)A 2D graphic objects. If you are used to working in 3D, Sprites
are essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite), the different portions scale or
tile (that is, repeat in a grid formation) in different ways to keep the
Sprite in proportion. This is useful when creating patterns or
[Textures](../../class-TextureImporter.html)An image used when rendering a
GameObject, Sprite, or UI element. Textures are often applied to the surface
of a mesh to give it visual detail. [More info](../../class-
TextureImporter.html)  
See in [Glossary](../../Glossary.html#texture), such as walls or floors in a
2D environment.

This is an example of a 9-sliced Sprite, split into nine sections. Each
section is labelled with a letter from A to I.

![](../../../uploads/Main/9-slice-0.png)

The following points describe what happens when you change the dimensions of
the image:

  * The four corners (A, C, G and I) do not change in size.

  * The B and H sections stretch or tile horizontally.

  * The D and F sections stretch or tile vertically.

  * The E section stretches or tiles both horizontally and vertically.

This section describes how to set 9-slicing up, and which settings to apply
depending on whether you want to stretch or tile the areas shown above.

### Limitations and known issues

  * The only two Collider2Ds that support 9-slicing are BoxCollider2D and PolygonCollider2D.

  * You cannot edit BoxCollider2D or PolygonCollider2D when the **Sprite Renderer** A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](../../sprite/renderer/renderer-landing.html)  
See in [Glossary](../../Glossary.html#SpriteRenderer)’s **Draw Mode** is set
to **Sliced** or **Tiled**. Editing in the **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](../../UsingTheInspector.html)  
See in [Glossary](../../Glossary.html#Inspector) window is disabled, and a
warning appears to notify you that the Collider2D cannot be edited because it
is driven by the Sprite Renderer component’s tiling properties.

  * When the shape is regenerated in **Auto Tiling** , additional edges might appear within the Collider2D’s shape. This may have an effect on **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision).

[](../../sprite/9-slice/9-slice-landing.html)

Various image sizes without multiple assets

[](../../sprite/9-slice/set-sprite-9slicing.html)

Set up your sprite for 9-slicing

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

