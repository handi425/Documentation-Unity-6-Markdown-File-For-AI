[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [Tilemaps in Unity](../../../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * [Isometric tilemaps in Unity](../../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html)
  * [Tilemap Renderer for Isometric Tilemaps](../../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-landing.html)
  * Tilemap Renderer isometric modes

[](../../../../tilemaps/work-with-tilemaps/isometric-
tilemaps/renderer/tilemap-renderer-isometric-landing.html)

Tilemap Renderer for Isometric Tilemaps

[](../../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-
isometric-sprites-sprite-atlas.html)

Sort isometric Sprites with the Sprite Atlas

# Tilemap Renderer isometric modes

The **Tilemap Renderer** component renders the [Tilemap](../../tilemap-
reference.html)A GameObject that allows you to quickly create 2D levels using
tiles and a grid overlay. [More info](../../../../tilemaps/work-with-
tilemaps/tilemap-reference.html)  
See in [Glossary](../../../../Glossary.html#Tilemap) in the **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../../../../CreatingScenes.html)  
See in [Glossary](../../../../Glossary.html#Scene). Unity creates Tilemaps
with the Tilemap Renderer attached by default. The Tilemap Renderer can:

  * Render in batches with **Chunk Mode**
  * Render individually with **Individual Mode**

The Render Mode affects the sorting of Tilemap **Sprites** A 2D graphic
objects. If you are used to working in 3D, Sprites are essentially just
standard textures but there are special techniques for combining and managing
sprite textures for efficiency and convenience during development. [More
info](../../../../sprite/sprite-landing.html)  
See in [Glossary](../../../../Glossary.html#Sprite) when rendered.

## Rendering in batches with Chunk Mode

**Chunk Mode** is the default rendering mode of the Tilemap Renderer.

When set to **Chunk Mode** , the Tilemap Renderer handles Sprites on a Tilemap
in batches and renders them together. They’re treated as a single sort item
when sorted in the [2D Transparent Queue](../../../../2d-renderer-
sorting.html). While this reduces draw calls, other renderers can’t render
between any part of the Tilemap, preventing other rendered Sprites from
interweaving with Tilemap Sprites.

In **Chunk Mode** , the Tilemap Renderer isn’t able to sort Tiles from
multiple textures individually and doesn’t render the tile sprites
consistently. For information on how to work with this, refer to [Use the
Sprite Atlas for sorting Sprites](sort-isometric-sprites-sprite-atlas.html).

## Rendering individually with Individual Mode

In **Individual Mode** , the Tilemap Renderer sorts and renders the Sprites on
a Tilemap with consideration of other Renderers in the Scene, such as the
[Sprite Renderers](../../../../sprite/renderer/renderer-landing.html)A
component that lets you display images as Sprites for use in both 2D and 3D
scenes. [More info](../../../../sprite/renderer/renderer-landing.html)  
See in [Glossary](../../../../Glossary.html#SpriteRenderer) and [Mesh
Renderers](../../../../class-MeshRenderer.html)A mesh component that takes the
geometry from the Mesh Filter and renders it at the position defined by the
object’s Transform component. [More info](../../../../class-MeshRenderer.html)  
See in [Glossary](../../../../Glossary.html#MeshRenderer). Use this mode if
other Renderers interact with Sprites and objects on the Tilemap.

In this mode, the Tilemap Renderer sorts sprites based on their position on
the Tilemap and the sorting properties set in the Tilemap Renderer. For
example, this allows a character sprite to go in-between obstacle sprites
(refer to the example below).

![In Individual Mode, the character can be rendered behind the tower Sprites,
and also appear above the ground
Sprites.](../../../../../uploads/Main/2D_IsoTilemap_14.png) In Individual
Mode, the character can be rendered behind the tower Sprites, and also appear
above the ground Sprites.

Using the same example in **Chunk Mode** , character sprites might get hidden
behind ground sprites:

![The same Scene rendered in Chunk
Mode.](../../../../../uploads/Main/2D_IsoTilemap_15.png) The same Scene
rendered in **Chunk Mode**.

Using **Individual Mode** might reduce performance as there is more overhead
when rendering each sprite individually on the Tilemap.

To sort and render tile sprites on an **Isometric Z as Y** Tilemap, you must
set the **Transparency Sort Axis** to a **Custom Axis**. For more information
on how to do this, refer to [Custom Sorting Axis for Tilemaps in Individual
Mode](sort-sprites-custom-sorting-axis.html).

[](../../../../tilemaps/work-with-tilemaps/isometric-
tilemaps/renderer/tilemap-renderer-isometric-landing.html)

Tilemap Renderer for Isometric Tilemaps

[](../../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-
isometric-sprites-sprite-atlas.html)

Sort isometric Sprites with the Sprite Atlas

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

