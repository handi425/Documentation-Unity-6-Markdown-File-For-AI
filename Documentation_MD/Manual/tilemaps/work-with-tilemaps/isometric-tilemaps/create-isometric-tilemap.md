[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Tilemaps in Unity](../../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * [Isometric tilemaps in Unity](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html)
  * Create an Isometric Tilemap

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-
sprites-custom-sorting-axis.html)

Sort Sprites with a Custom Sorting Axis

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-
palette-isometric-tilemap.html)

Create a Tile Palette for an Isometric Tilemap

# Create an Isometric Tilemap

When creating an **Isometric**Tilemap** A GameObject that allows you to
quickly create 2D levels using tiles and a grid overlay. [More
info](../../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../../Glossary.html#Tilemap)**, there are additional
configuration steps to take compared to [creating a regular
Tilemap](../create-tilemap.html).

## Create the Isometric Tilemap

To create an Isometric Tilemap, go to **GameObject** > **2D Object** and
select either **Isometric Tilemap** or **Isometric Z as Y Tilemap**.

After creating the Isometric Tilemap, there are additional settings that need
to set with the Project and Grid settings for the Isometric Tilemap to be
rendered properly.

## Custom Axis Sorting

To render the Tiles of an Isometric Tilemap, Tiles placed further to the
‘back’ of the Tilemap need to be rendered first before those in front to
create the **pseudo-depth** of an isometric perspective. To ensure that all
Renderers in the **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../../../CreatingScenes.html)  
See in [Glossary](../../../Glossary.html#Scene) conform to this logic, a
Custom Axis is used as the [Sorting Axis](../../../2d-renderer-sorting.html).
Set the **Transparency Sort Mode** to ‘Custom Axis’ and enter (0,1,0) for the
XYZ values of the **Transparency Sort Axis**.

Go to **Edit** > **Project Settings** > **Graphics** > **Camera Settings** to
set the **Custom Axis** settings.

Set the **Transparency Sort Axis** XYZ values to (0,1,0) to cause all
Renderers which are at a higher Y position in the Scene to be rendered first,
and appear behind Renderers at a lower Y position.

With the **Isometric Z as Y Tilemap** , Tiles with different [Z-position
values](./create-tile-palette-isometric-tilemap.html) are offset along the
Y-axis and appear to be at different heights, producing a ‘stacking’ effect
with Tiles at the same XY Cell Position. By default, the generic isometric
Transparency Sort Axis setting of (0,1,0) does not consider the Tile’s
Z-position values during sorting which results in the Tiles being rendered out
of intended order (see the example below).

![Left: With \(0,1,0\), Tiles rendered in incorrect order. Right: With
\(0,1,-0.26\), Tiles appear correctly stacked on each
other.](../../../../uploads/Main/Iso-axis-compare.png) **Left:** With (0,1,0),
Tiles rendered in incorrect order. **Right:** With (0,1,–0.26), Tiles appear
correctly ‘stacked’ on each other.

Set the **Transparency Sort Axis** to **(0,1,–0.26)** to correctly render
Tiles with different Z positions. The Z-axis is set to –0.26 to give a bias to
Tiles with higher Z positions to be drawn first.

* * *

  * Isometric Tilemaps added in [2018.3](https://docs.unity3d.com/2018.3/Documentation/Manual/30_search.html?q=newin20183) NewIn20183

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-
sprites-custom-sorting-axis.html)

Sort Sprites with a Custom Sorting Axis

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-
palette-isometric-tilemap.html)

Create a Tile Palette for an Isometric Tilemap

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

