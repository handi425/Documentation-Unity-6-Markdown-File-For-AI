[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [Tilemaps in Unity](../../../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * [Isometric tilemaps in Unity](../../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html)
  * [Tilemap Renderer for Isometric Tilemaps](../../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-landing.html)
  * Sort isometric Sprites with the Sprite Atlas

[](../../../../tilemaps/work-with-tilemaps/isometric-
tilemaps/renderer/tilemap-renderer-isometric-modes.html)

Tilemap Renderer isometric modes

[](../../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-
sprites-custom-sorting-axis.html)

Sort Sprites with a Custom Sorting Axis

# Sort isometric Sprites with the Sprite Atlas

In **Chunk Mode** , the **Tilemap** A GameObject that allows you to quickly
create 2D levels using tiles and a grid overlay. [More
info](../../../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../../../Glossary.html#Tilemap) Renderer isn’t able to
sort Tiles from multiple textures individually and doesn’t render the tile
**sprites** A 2D graphic objects. If you are used to working in 3D, Sprites
are essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../../../sprite/sprite-landing.html)  
See in [Glossary](../../../../Glossary.html#Sprite) consistently.

![](../../../../../uploads/Main/2D_IsoTilemap_10.png)

Pack all the individual Sprites that make up the Tilemap into a single [Sprite
Atlas](https://docs.unity3d.com/Manual/SpriteAtlas.html)A utility that packs
several sprite textures tightly together within a single texture known as an
atlas. [More info](../../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../../Glossary.html#SpriteAtlas) to solve this issue.
To do this:

  1. Create a **Sprite Atlas** from the Assets menu (go to: **Atlas > Create > Sprite Atlas**).

  2. Add the Sprites to the Sprite Atlas by dragging them to the **Objects for Packing** list in the Atlas’ **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../../../UsingTheInspector.html)  
See in [Glossary](../../../../Glossary.html#Inspector) window.

![Objects for packing list](../../../../../uploads/Main/2D_IsoTilemap_11.png)
**Objects for packing** list

  3. Click **Pack Preview**. Unity packs the Sprites into the Sprite Atlas during Play mode, and correctly sorts and renders them. This is only visible in the Editor during Play mode.

![Isometric tilemap](../../../../../uploads/Main/2D_IsoTilemap_12.png)
Isometric tilemap

[](../../../../tilemaps/work-with-tilemaps/isometric-
tilemaps/renderer/tilemap-renderer-isometric-modes.html)

Tilemap Renderer isometric modes

[](../../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-
sprites-custom-sorting-axis.html)

Sort Sprites with a Custom Sorting Axis

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

