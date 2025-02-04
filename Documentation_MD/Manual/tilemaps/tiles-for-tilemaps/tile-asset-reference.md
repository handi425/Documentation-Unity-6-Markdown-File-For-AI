[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Tilemaps in Unity](../../tilemaps/tilemaps-landing.html)
  * [Tiles for tilemaps](../../tilemaps/tiles-for-tilemaps/tiles-landing.html)
  * Tile asset reference

[](../../tilemaps/tiles-for-tilemaps/scriptable-tiles/create-scriptable-
tile.html)

Create a scriptable tile

[](../../tilemaps/tile-palettes/tile-palette-landing.html)

Tile palettes

# Tile asset reference

**Tiles** are **Assets** that are arranged on ****Tilemaps** A GameObject that
allows you to quickly create 2D levels using tiles and a grid overlay. [More
info](../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../Glossary.html#Tilemap)** to construct a 2D
environment. Each Tile references a selected ****Sprite** A 2D graphic
objects. If you are used to working in 3D, Sprites are essentially just
standard textures but there are special techniques for combining and managing
sprite textures for efficiency and convenience during development. [More
info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite)**, which is then rendered at the
Tile’s location on the [Tilemap Grid](../grid-reference.html). Refer to
[Creating Tiles](./create-tile-assets.html) for more information about
preparing and importing sprites for your Tiles, and the different methods for
creating the Assets in the Editor.

## Asset properties

Property | Function  
---|---  
**Preview** | Displays a visual preview of the selected Tile.  
**Sprite** | Select the Sprite to be rendered on this Tile. Click the circle icon to the right to open the object picker window to select from the available Sprite Assets, or drag a Sprite directly onto this box.  
**Color** | Tints the Sprite placed on this Tile with the selected Color. When set to white, the Sprite is rendered without a tint.  
****Collider** An invisible shape that is used to handle physical collisions
for an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) Type** | Defines the shape of the Collider generated for the Tile.  
**None** | No Collider is generated.  
**Sprite** | The Collider shape is generated based on the selected **Sprite’s** outline.  
**Grid** | The Collider shape is based on a cell of the **Tilemap**. The shape of a cell depends on the [Cell Layout](../grid-reference.html) of the Tilemap.  
  
## Collider shape

The **Collider Type** set in the **Tile Asset** properties affects the
generation of Collider shapes for each Tile in the Tilemap. The component’s
shape generation behavior corresponds to the **Collider Types** in the
following ways:

Collider Type | Function  
---|---  
**None** | The Tilemap Collider 2D component does not generate any Collider shapes for this Tile.  
**Sprite** | The Tilemap Collider 2D component generates a Collider shape based on the Sprite assigned to the Tile. The Collider shape is based on the [Custom Physics Shape](../../sprite/sprite-editor/custom-physics-shape/custom-physics-shape-landing.html) set for the Sprite.  
**Grid** | The Tilemap Collider 2D component generates a Collider shape based on the shape of the Grid cell, which is determined by the selected Cell Layout of the Grid component.  
  
* * *

  * Page content and screenshots updated for [2020.1](https://docs.unity3d.com/2020.1/Documentation/Manual/30_search.html?q=newin20201) NewIn20201
  * Tilemaps added in [2017.2](https://docs.unity3d.com/2017.2/Documentation/Manual/30_search.html?q=newin20172) NewIn20172

[](../../tilemaps/tiles-for-tilemaps/scriptable-tiles/create-scriptable-
tile.html)

Create a scriptable tile

[](../../tilemaps/tile-palettes/tile-palette-landing.html)

Tile palettes

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

