[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/tile-palettes/new-tile-palette-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/new-tile-palette-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/new-tile-palette-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/new-tile-palette-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/tile-palettes/new-tile-palette-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/new-tile-palette-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/new-tile-palette-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/new-tile-palette-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Tilemaps in Unity](../../tilemaps/tilemaps-landing.html)
  * [Tile palettes](../../tilemaps/tile-palettes/tile-palette-landing.html)
  * New tile palette properties reference

[](../../tilemaps/tile-palettes/tools/create-brush-picks-from-tiles-pick-
tool.html)

Create Brush Picks from tiles with the Pick tool

[](../../tilemaps/tile-palettes/tile-palette-preferences-reference.html)

Tile palette preferences reference

# New tile palette properties reference

When you create a new tile palette, you must configure its properties before
the tile palette asset can be created.

Property | Function  
---|---  
**Name** | Provide a name for the created Tile Palette Asset.  
**Grid** | Select the [Grid](../grid-reference.html) layout the created Tile Palette will be used to paint on.  
**Rectangle** | Select this if creating a Palette for the default rectangular **Tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../Glossary.html#Tilemap).  
**Hexagon** | Select this when creating a Palette for a [Hexagonal Tilemap](../work-with-tilemaps/hexagonal-tilemaps.html).  
**Isometric** | Select this when creating a Palette for a [Isometric Tilemap](../work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html). Refer to [Creating a Tile Palette for an Isometric Tilemap](../work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html) for more information.  
**Isometric Z as Y** | Select this when creating a Palette for a [Isometric Z as Y Tilemap](../work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html). Refer to [Creating a Tile Palette for an Isometric Tilemap](../work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html) for more information.  
**Hexagon Type** (only available when the Hexagon Grid type is selected) | Select the type of Hexagonal Tilemap that the Palette will be used to paint on. Refer to the documentation on [Hexagonal Tilemaps](../work-with-tilemaps/hexagonal-tilemaps.html) for more information.  
**Cell Size** | The size of a cell that the Tiles are painted on.  
**Automatic** | The Cell Size is automatically set in **Unity units** The unit size used in Unity projects. By default, 1 Unity unit is 1 meter. To use a different scale, set the Scale Factor in the Import Settings when importing assets.  
See in [Glossary](../../Glossary.html#Unityunit) and based on the size of the
**Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are
essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) used to create the Tile Assets.
If there are multiple Tiles, the Cell Size is adjusted to match the first Tile
from the bottom left of the Palette, so that it fits exactly on a cell.  
**Manual** | Select this option to input custom size values.  
**Sort Mode** | Determines the [transparency sort mode](../../../ScriptReference/TransparencySortMode.html) of Renderers in the Tile Palette.  
**Default** | The default transparency Sort Mode. This mode is determined by the **Graphics Settings** of the project.  
**Orthographic** | Select this mode to sort Renderers based on the perpendicular distance from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) to a Renderer in the Tile
Palette.  
**Perspective** | Select this mode to sort Renderers based on the direct distance from the camera to a Renderer in the Tile Palette.  
**Custom Axis Sort** | Select this mode to sort objects based on their distance along a custom axis.  
**Sort Axis** | Set the XYZ values for the sorting axis, if the **Sort Mode** is set to Custom Axis Sort.  
  
[](../../tilemaps/tile-palettes/tools/create-brush-picks-from-tiles-pick-
tool.html)

Create Brush Picks from tiles with the Pick tool

[](../../tilemaps/tile-palettes/tile-palette-preferences-reference.html)

Tile palette preferences reference

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

