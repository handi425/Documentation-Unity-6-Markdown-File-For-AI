[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Tilemaps in Unity](../../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * [Isometric tilemaps in Unity](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html)
  * Create a Tile Palette for an Isometric Tilemap

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-
tilemap.html)

Create an Isometric Tilemap

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-
isometric-tilemap.html)

Import Sprites for an Isometric Tilemap

# Create a Tile Palette for an Isometric Tilemap

To create a **Tile Palette** for painting an Isometric **Tilemap** A
GameObject that allows you to quickly create 2D levels using tiles and a grid
overlay. [More info](../../../tilemaps/work-with-tilemaps/tilemap-
reference.html)  
See in [Glossary](../../../Glossary.html#Tilemap):

  1. Open the Tile Palette window. To do this, go to the top menu and select **Window** > **2D** > **Tile Palette** :

  2. Select the **Create New Palette** to open its drop-down menu.

![Select Create New Palette.](../../../../uploads/Main/2D_IsoTilemap_4.png)
Select **Create New Palette**.

  3. Set the **Grid type** to the same layout as the **Isometric** or **Isometric Z As Y** Tilemap you are painting.

  4. Set **Cell Size** to **Manual**. Leave X and Z at their default values, but set Y to the same value as the Y value of the Tilemap’s Cell Size. This value depends on the projection type of the Tilemap. Refer to the [Creating an Isometric Tilemap](create-isometric-tilemap.html) page for more details.

![Set the Cell Size property.](../../../../uploads/Main/2D_IsoTilemap_6.png)
Set the **Cell Size** property.

  5. Select **Create** to finalize your settings and create the new **Tile Palette Asset**.

  6. To make any changes to the Tile Palette, double-click the Asset in the Asset Folder to open it as a [Prefab](../../../Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](../../../Prefabs.html)  
See in [Glossary](../../../Glossary.html#Prefab) and make your changes there.

## Adjusting the Tile height in the Palette

When painting Tiles on an **Isometric Z as Y Tilemap** , you define the Z
position of the **Grid** you are painting on by setting the **Z Position**
value. For this type of Tilemap, the Z position value translates into an
offset along the Y-axis, and Tiles painted with different Z positions appear
to have different heights on the Tilemap.

To do this, use the following steps:

  1. Select the tile palette and open it in the Tile Palette window.

  2. Adjust the **Z Position** by entering the desired value (only whole numbers).

![The Z Position is at the bottom of the Tile
Palette.](../../../../uploads/Main/2D_IsoTilemap_7.png) The **Z Position** is
at the bottom of the Tile Palette.

**Note** : Tiles are painted on a Grid with the set Z position until the value
is changed or reset. To change the value back to the default of 0, select
**Reset**.

In the **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../../../CreatingScenes.html)  
See in [Glossary](../../../Glossary.html#Scene) view, the brush preview now
displays both the Tile at the Cell’s original position with a Z value of 0 as
a blue outline, and its painted position with the Z-as-Y offset applied is
displayed with a white outline.

![](../../../../uploads/Main/2D_IsoTilemap_8.png)

The **Z Position** of a brush can also be adjusted with keyboard shortcuts.
For more information on this, refer to [Isometric brush shortcut
reference](isometric-brush-shortcut-reference.html).

**Note** : To remove Tiles, the **Erase Brush** must have the same **Z
Position** as the target Tile to be removed. The Erase Brush does not erase
Tiles painted on at a different Z position to it.

* * *

  * Isometric Tilemaps added in [2018.3](https://docs.unity3d.com/2018.3/Documentation/Manual/30_search.html?q=newin20183) NewIn20183

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-
tilemap.html)

Create an Isometric Tilemap

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-
isometric-tilemap.html)

Import Sprites for an Isometric Tilemap

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

