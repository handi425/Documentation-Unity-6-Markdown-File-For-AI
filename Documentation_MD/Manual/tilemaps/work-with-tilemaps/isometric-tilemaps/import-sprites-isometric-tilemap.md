[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-isometric-tilemap.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-isometric-tilemap.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-isometric-tilemap.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-isometric-tilemap.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-isometric-tilemap.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-isometric-tilemap.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-isometric-tilemap.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/import-sprites-isometric-tilemap.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Tilemaps in Unity](../../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * [Isometric tilemaps in Unity](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html)
  * Import Sprites for an Isometric Tilemap

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-
palette-isometric-tilemap.html)

Create a Tile Palette for an Isometric Tilemap

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-
scriptable-brush-methods.html)

Isometric scriptable brush methods

# Import Sprites for an Isometric Tilemap

[Import](../../../sprite/import-images-sprites/import-images-sprites-
landing.html) the individual Tiles or Tilesheet images for your Isometric
**Tilemap** A GameObject that allows you to quickly create 2D levels using
tiles and a grid overlay. [More info](../../../tilemaps/work-with-
tilemaps/tilemap-reference.html)  
See in [Glossary](../../../Glossary.html#Tilemap) into your Unity Project by
placing the Textures into the Assets folder. Select the imported images to
view their [Texture Importer](../../../sprite/import-images-sprites/import-
images-sprites-landing.html) settings in the **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](../../../UsingTheInspector.html)  
See in [Glossary](../../../Glossary.html#Inspector) window.

When importing **Sprites** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../../../sprite/sprite-
landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) for use in an Isometric
Tilemap, use the following recommended settings. For further information about
each setting, refer to the documentation on [Texture Type: Sprite (2D and
UI)](../../../sprite/import-images-sprites/set-texture-type-imported-image-
sprite-2d-ui.html).

  1. **Texture Type** \- Set this to **Sprite (2D and UI)**. Other Texture types are not supported for Tilemaps.
  2. **Sprite Mode** \- Set this to **Single** if the Texture contains only a single Sprite. Set to **Multiple** if it contains multiple Sprite Textures, for example a Sprite sheet with multiple Tile Textures.
  3. ****Pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../../../ShadowPerformance.html)  
See in [Glossary](../../../Glossary.html#pixel) Per Unit (PPU)** \- This value
is the number of pixels that make up one **Unity unit** The unit size used in
Unity projects. By default, 1 Unity unit is 1 meter. To use a different scale,
set the Scale Factor in the Import Settings when importing assets.  
See in [Glossary](../../../Glossary.html#Unityunit) for the selected Sprite.
This determines the size of the Sprite when it is rendered on the Tilemap.
This is also affected by the **Cell Size** setting of the Grid that contains
the Tilemap, which determines how many Unity units make up a single Cell.
Refer to the example below to see how PPU values and the [Grid’s](../../grid-
reference.html) **Cell Size** settings interact.

  4. ****Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](../../../mesh.html)  
See in [Glossary](../../../Glossary.html#Mesh) Type** \- Set to **Tight** to
ensure the Tile Meshes follow the outline of the imported Sprites, and the
Tiles are drawn flush together on the Tilemap. Due to the general diamond
shape of most Isometric Tiles, setting this to **Full Rect** may result in
drawing of wasted transparent spaces at the corners of an Isometric Tile, and
is not recommended.

  5. **Generate Physics Shape** \- If the Tiles do not need to interact with [Physics2D](../../../2d-physics/2d-physics.html), then clear this option. Leave this option enabled to generate a Physics Shape based on the shape of the Tile Sprite, for use with the [Tilemap Collider](../../work-with-tilemaps/tilemap-collider-2d.html) component. To make the generated Physics Shape match the cell of the Tilemap instead, select the Tile Asset and set its [Collider Type](../../../tilemaps/tiles-for-tilemaps/tiles-landing.html) property to **Grid**.

In the example below, the imported Sprite is a 256x128 image, and the
Isometric Tilemap has a **Cell Size** of (XYZ: 1, 0.5, 1) Unity units. To make
the Sprite fit exactly on a single Cell of the Tilemap, set its PPU value to
256. Its entire width then corresponds to one Unity unit, which is equal to
the width (X value: 1) of a single Cell.

![Left: Sprite set to 256 PPU. Right: The same Sprite set to 128
PPU.](../../../../uploads/Main/2D_IsoTilemap_1.png) **Left:** Sprite set to
256 PPU. **Right:** The same Sprite set to 128 PPU.

If the Sprite is set to a PPU value of 128, then it becomes 2 (256px/128)
Unity units in width. This causes the Sprite to visually appear to cover 2
Cells in width when painted on the Tilemap. However, the original Cell
position of the Tile remains unchanged.

After you import the Sprites, refine the outlines of the Sprites by opening
the Sprite Editor for each of them and [editing their
outlines](../../../sprite/sprite-editor/custom-outline-editor/custom-outline-
editor-landing.html). For Sprites in an Isometric Tilemap, you should set the
**Pivot** of the Sprite so that the ‘ground’ is relative to the Sprite.

If the Texture is imported with **Sprite Mode** set to **Multiple** and
contains multiple Sprites, then edit the outline of each Sprite in the Sprite
Editor.

* * *

  * Isometric Tilemaps added in [2018.3](https://docs.unity3d.com/2018.3/Documentation/Manual/30_search.html?q=newin20183) NewIn20183

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-
palette-isometric-tilemap.html)

Create a Tile Palette for an Isometric Tilemap

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-
scriptable-brush-methods.html)

Isometric scriptable brush methods

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

