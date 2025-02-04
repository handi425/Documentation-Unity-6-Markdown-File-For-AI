[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/tile-palettes/tools/select-tool/grid-selection-properties-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/tools/select-tool/grid-selection-properties-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/tools/select-tool/grid-selection-properties-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/tools/select-tool/grid-selection-properties-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/tile-palettes/tools/select-tool/grid-selection-properties-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/tools/select-tool/grid-selection-properties-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/tools/select-tool/grid-selection-properties-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/tools/select-tool/grid-selection-properties-reference.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [Tilemaps in Unity](../../../../tilemaps/tilemaps-landing.html)
  * [Tile palettes](../../../../tilemaps/tile-palettes/tile-palette-landing.html)
  * [Tile palette editor tools](../../../../tilemaps/tile-palettes/tools/tile-palette-tools-landing.html)
  * [The Select tool](../../../../tilemaps/tile-palettes/tools/select-tool/select-tool-landing.html)
  * Grid Selection properties reference

[](../../../../tilemaps/tile-palettes/tools/select-tool/select-tiles-with-
select-tool.html)

Select tiles with the Select tool

[](../../../../tilemaps/tile-palettes/tools/select-tool/modify-tilemap-
reference.html)

Modify Tilemap reference

# Grid Selection properties reference

Use the [Select tool](./select-tiles-with-select-tool.html) to select one or
more grid cells. The Grid Selection ****Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](../../../../UsingTheInspector.html)  
See in [Glossary](../../../../Glossary.html#Inspector)** window displays the
contents and properties of the tiles at the selected location.

**Property** | **Function**  
---|---  
**Tile** | Displays the tile at the selected cell location. If you select multiple cells, and they display the same tile, then this property displays that tiles’ name. If you select multiple cells with different tiles, this property is blank.  
****Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites
are essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../../../sprite/sprite-landing.html)  
See in [Glossary](../../../../Glossary.html#Sprite)** | Displays the sprite assigned to the tile in the **Tile** property above. If you select multiple cells with the same tile, then this displays the same sprite. If you select multiple cells with different tiles, this property is blank. This is grayed out by default and can’t be edited.  
**Color** | The vertex color of the sprite. This is grayed out if Lock Color is enabled, so you can’t edit it.  
****Collider** An invisible shape that is used to handle physical collisions
for an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#Collider) Type** | The collider type of the tiles at the selected location. This is grayed out and can’t be edited.  
**Position** | Enter the offset (in cells) for each axis to shift the tile sprites along the respective axis. This changes where Unity displays the tile sprites on the **tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](../../../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../../../Glossary.html#Tilemap), but doesn’t change the
tiles’ actual cell positions on the tilemap.  
**Rotation** | This rotates one or more tile sprites at the selected location. Enter the rotation (in degrees) for each axis to rotate the tile sprites around the respective axis. This changes how Unity displays the tile sprites on the tilemap, but doesn’t change the tiles’ actual cell positions on the tilemap.  
**Scale** | Scales the size of one or more tile sprites at the selected location. Enter the factor for each axis to scale the tile sprite by along the respective axis. This changes how Unity displays the tile sprites on the tilemap, but doesn’t change the tiles’ actual cell positions on the tilemap.  
**Lock Color** | Select this to prevent changes to the Color of the tile, and clear this to enable the **Color** property. When this property is grayed out, its state remains fixed. Refer to the [Tilemaps.TileFlags](../../../../../ScriptReference/Tilemaps.TileFlags.html) set in the [Tile Asset](../../../tiles-for-tilemaps/tile-asset-reference.html) to change this property.  
**Lock Transform** | Select this to prevent changes to the Transforms of the tile, and clear this to enable the **Transform** properties. When this property is grayed out, its state remains fixed. Refer to the [Tilemaps.TileFlags](../../../../../ScriptReference/Tilemaps.TileFlags.html) set in the [Tile Asset](../../../tiles-for-tilemaps/tile-asset-reference.html) to change this property.  
**Delete Selection** | Select this to delete the contents of selected cells in the tilemap.  
  
## Additional resources

  * [Modify Tilemap reference](./modify-tilemap-reference.html)
  * [Tile Palette editor reference](../../tile-palette-editor-reference.html)

[](../../../../tilemaps/tile-palettes/tools/select-tool/select-tiles-with-
select-tool.html)

Select tiles with the Select tool

[](../../../../tilemaps/tile-palettes/tools/select-tool/modify-tilemap-
reference.html)

Modify Tilemap reference

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

