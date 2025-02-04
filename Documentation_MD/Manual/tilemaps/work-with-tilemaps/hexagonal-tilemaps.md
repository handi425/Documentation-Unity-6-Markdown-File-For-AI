[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Tilemaps in Unity](../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * Hexagonal Tilemaps

[](../../tilemaps/work-with-tilemaps/create-tilemap.html)

Create a tilemap

[](../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-
landing.html)

Isometric tilemaps in Unity

# Hexagonal Tilemaps

In addition to regular [Tilemaps](./tilemap-reference.html)A GameObject that
allows you to quickly create 2D levels using tiles and a grid overlay. [More
info](../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../Glossary.html#Tilemap), Unity provides both
**Hexagonal Point Top** and **Hexagonal Flat Top** Tilemaps. Hexagonal tiles
are often used in strategic tabletop games, because they have consistent
distance between their centres and any point on their edge, and neighboring
tiles always share edges. This makes them ideal for constructing almost any
kind of large play area and allows players to make tactical decisions
regarding movement and positioning.

The Hexagonal Tilemap uses an offset coordinate system, where alternative rows
or columns are offset by half a cell when aligning the cells to the hexagonal
grid. For Hexagonal Point Top Tilemaps, every odd row is offset to the right
by half a cell’s width. For Hexagonal Flat Top Tilemaps, every odd column is
offset to the top by half a cell’s height.

![Example: Hexagonal Point Top Tilemap. Offset rows are colored in
yellow.](../../../uploads/Main/hex-tilemap-pointtop-offset.png) Example:
Hexagonal Point Top Tilemap. Offset rows are colored in yellow. ![Example:
Hexagonal Flat Top Tilemap. Offset columns are colored in
yellow.](../../../uploads/Main/hex-tilemap-flattop-offset.png) Example:
Hexagonal Flat Top Tilemap. Offset columns are colored in yellow.

## Creating a Hexagonal Tilemap

To create a **Hexagonal Tilemap** , follow the same steps to [create a regular
Tilemap](./create-tilemap.html) (menu: **GameObject > 2D Object**) but choose
one of the **Hexagonal** options in the **2D Object** menu.

* * *

  * Hexagonal Tilemaps added in [2018.2](https://docs.unity3d.com/2018.2/Documentation/Manual/30_search.html?q=newin20182) NewIn20182

[](../../tilemaps/work-with-tilemaps/create-tilemap.html)

Create a tilemap

[](../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-
landing.html)

Isometric tilemaps in Unity

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

