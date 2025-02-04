[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Tilemaps in Unity](../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * Tilemap component reference

[](../../tilemaps/work-with-tilemaps/tilemap-collider-2d.html)

Tilemap Collider 2D

[](../../tilemaps/work-with-tilemaps/tilemap-renderer-reference.html)

Tilemap Renderer component reference

# Tilemap component reference

The ****Tilemap** A GameObject that allows you to quickly create 2D levels
using tiles and a grid overlay. [More info](../../tilemaps/work-with-
tilemaps/tilemap-reference.html)  
See in [Glossary](../../Glossary.html#Tilemap)** component stores and manages
[Tile Assets](../tiles-for-tilemaps/tile-asset-reference.html) for creating 2D
levels. It transfers the required information from the tiles placed on it to
other related components such as the [Tilemap Renderer](./tilemap-renderer-
reference.html) and the [Tilemap Collider 2D](./tilemap-
collider-2d-reference.html).

The 2D Tilemap Editor package is automatically installed when you create a
project with the [2D
template](https://docs.unity3d.com/hub/manual/Templates.html). You can install
the 2D Tilemap Editor directly from the Unity registry via the [Package
Manager](../../upm-ui-install.html).

To create, edit, and pick the tiles for [painting onto a tilemap](../tile-
palettes/tile-palette-editor-reference.html), refer to the [Tile
Palette](../tile-palettes/create-tile-palette.html) (menu: **Window** > **2D**
> **Tile Palette**) documentation for more information on its features and
tools.

## Properties

Property | Description  
---|---  
**Animation Frame Rate** | Set the frame rate at which tile animations play. Increasing or decreasing this value changes the frame rate of the tile animations. For example, if set to 2, tile animations play at double the base frame rate. If set to 3, tile animations play at triple the base frame rate.  
**Color** | Select a color to apply as a tint to the tiles on this tilemap. Set to white (default color) to have Unity render the tiles without tint.  
**Tile Anchor** | Enter the amount (in cells) along the xyz axes to offset tile anchor positions on the tilemap.  
**Orientation** | Select the orientation of tiles on the tilemap. Each of the following options performs the same function by orienting the tiles along the selected plane.  
**XY** | Unity orients tiles along the XY plane.  
**XZ** | Unity orients tiles along the XZ plane.  
**YX** | Unity orients tiles along the YX plane.  
**YZ** | Unity orients tiles along the YZ plane.  
**ZX** | Unity orients tiles along the ZX plane.  
**ZY** | Unity orients tiles along the ZY plane.  
**Custom** | Select this option to enable the custom orientation settings below.  
**Offset** | Set the position offset of the custom orientation. This option is only available when you set the tilemap’s **Orientation** to **Custom**.  
**Rotation** | Set the rotation of the custom orientation. This option is only available when you set the tilemap’s **Orientation** to **Custom**.  
**Scale** | Set the scale of the custom orientation. This option is only available when you set the tilemap’s **Orientation** to **Custom**.  
**Info** | Expand this to view the assets present in the tilemap.  
**Tiles** | Displays a list of [Tile Assets](../tiles-for-tilemaps/tile-asset-reference.html) present in the tilemap.  
****Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites
are essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite)** | Displays a list of sprites present in the tilemap.  
  
## Additional resources

  * [Tilemap Renderer component reference](./tilemap-renderer-reference.html)
  * [Tile Palette preferences reference](../tile-palettes/tile-palette-preferences-reference.html)

Tilemap

[](../../tilemaps/work-with-tilemaps/tilemap-collider-2d.html)

Tilemap Collider 2D

[](../../tilemaps/work-with-tilemaps/tilemap-renderer-reference.html)

Tilemap Renderer component reference

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

