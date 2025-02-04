[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)
  * [中文](/cn/current/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)
  * [日本語](/ja/current/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)
  * [한국어](/kr/current/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)
  * [中文](/cn/current/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)
  * [日本語](/ja/current/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)
  * [한국어](/kr/current/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Tilemaps in Unity](../../../tilemaps/tilemaps-landing.html)
  * [Tiles for tilemaps](../../../tilemaps/tiles-for-tilemaps/tiles-landing.html)
  * [Scriptable Tile assets](../../../tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-landing.html)
  * Scriptable tiles

[](../../../tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-
landing.html)

Scriptable Tile assets

[](../../../tilemaps/tiles-for-tilemaps/scriptable-tiles/create-scriptable-
tile.html)

Create a scriptable tile

# Scriptable tiles

Scriptable tiles are tiles that you can assign behavior **scripts** A piece of
code that allows you to create your own Components, trigger game events,
modify Component properties over time and respond to user input in any way you
like. [More info](../../../creating-scripts.html)  
See in [Glossary](../../../Glossary.html#Scripts) to and you can paint with
the scriptable tiles on a **Tilemap** A GameObject that allows you to quickly
create 2D levels using tiles and a grid overlay. [More
info](../../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../../Glossary.html#Tilemap) component.

These C# scripts allow you to customize how the tile interacts with other
tiles or other behaviours defined by the
[TileBase](../../../../ScriptReference/Tilemaps.TileBase.html) class.

All tiles added to a Tilemap component must inherit from `TileBase`.
`TileBase` provides a tilemap with a fixed set of APIs to communicate its
rendering properties. For most cases of the APIs, the location of the tile and
the instance of the tilemap the tile is placed on is passed in as arguments of
the API. You can use this to find any required attributes for setting the tile
information.

The most common methods to override are:

  * `RefreshTile` determines which Tiles in the vicinity are updated when this Tile is added to the Tilemap.
  * `GetTileData` determines what the Tile looks like on the Tilemap.

[](../../../tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-
landing.html)

Scriptable Tile assets

[](../../../tilemaps/tiles-for-tilemaps/scriptable-tiles/create-scriptable-
tile.html)

Create a scriptable tile

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

