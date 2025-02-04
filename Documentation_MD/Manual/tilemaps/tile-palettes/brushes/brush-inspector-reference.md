[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/tile-palettes/brushes/brush-inspector-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/brushes/brush-inspector-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/brushes/brush-inspector-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/brushes/brush-inspector-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/tile-palettes/brushes/brush-inspector-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/brushes/brush-inspector-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/brushes/brush-inspector-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/brushes/brush-inspector-reference.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Tilemaps in Unity](../../../tilemaps/tilemaps-landing.html)
  * [Tile palettes](../../../tilemaps/tile-palettes/tile-palette-landing.html)
  * [Tile palette brushes](../../../tilemaps/tile-palettes/brushes/tile-palette-brushes-landing.html)
  * Brush Inspector window reference

[](../../../tilemaps/tile-palettes/brushes/create-scriptable-brush.html)

Create a Scriptable Brush

[](../../../tilemaps/tile-palettes/brushes/active-brush-shortcuts-
reference.html)

Active brush shortcuts reference

# Brush Inspector window reference

You can use the Brush **Inspector** A Unity window that displays information
about the currently selected GameObject, asset or project settings, allowing
you to inspect and edit the values. [More
info](../../../UsingTheInspector.html)  
See in [Glossary](../../../Glossary.html#Inspector) to change the current
[active brush](./active-brush.html) and its properties.

The **Brush Inspector** window is at the bottom of the [Tile Palette
editor](../tile-palette-editor-reference.html) window. To minimize or expand
the **Brush Inspector** , select the **Brush Inspector** visibility toggle at
the upper right corner of the window, or drag the edge of the **Brush
Inspector** window.

Select the brush type for the active brush from the dropdown menu from one of
the available brushes provided by the [2D Tilemap Extras
package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest).

Refer to the [Scriptable
Brushes](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/Brushes.html)
documentation for more information on their specific properties and usage.

Brush Type | Description  
---|---  
**Brush type dropdown** | Select the [active brush](./active-brush.html)’s brush type from the available options.  
**Default Brush** | The default brush with the default properties.  
**GameObject Brush** | Select this brush to instance, place and manipulate **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../../class-GameObject.html)  
See in [Glossary](../../../Glossary.html#GameObject) onto the ****Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](../../../CreatingScenes.html)  
See in [Glossary](../../../Glossary.html#Scene)** view.  
**Group Brush** | Select this brush to pick tiles which are grouped together according to their position and set properties.  
**Random Brush** | Select this brush to place random tiles onto a **tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](../../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../../Glossary.html#Tilemap) from a [Tile
Set](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/RandomBrush.html%23usage)
you define. For more information about the brush and how to define a Tile Set,
refer to the [Random
Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/RandomBrush.html)
documentation in the [2D Tilemap Extras
package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest).  
**Line Brush** | Select this brush to draw a line of tiles onto the tilemap.  
  
## Default Brush properties

The following properties are visible by default when you select the **Default
Brush**. Some properties are common to all brush types.

Property | Function  
---|---  
**Script** | Displays the currently assigned script Asset that provides a fixed set of APIs for painting on Tilemaps. The default is the [GridBrush](../../../../ScriptReference/GridBrushBase.html). Users may use or create their own [Scriptable Brushes](./create-scriptable-brush.html) which become available from the dropdown menu. The Script property updates to reflect the current active Brush.  
**Flood Fill Contiguous Only** | Enable this property to have the [Flood Fill tool](../tools/fill-area-with-flood-fill-tool.html) only affect Tiles on a Tilemap which are both the same as the targeted Tile and are contiguous to each other from the targeted position. When disabled, Flood Fill will change all Tiles which are the same as the targeted Tile on a Tilemap regardless of their position. This only affects the Default Brush.  
**Lock Z Position** | Enable this property to change the z-position of the active Brush. Disable to prevent any changes to the current z-position of the active Brush.  
**Z Position** | Only available when **Lock Z Position** is disabled. Enter the desired z-axis value (only whole numbers) for this Brush when painting Tiles, which also adjusts the relative heights of Tiles on a [Z as Y Isometric Tilemap](../../work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html). Refer to [Adjusting the Tile height in the Palette](../../work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html) for more information.  
**Reset** | Select to reset the z-position value back to zero.  
  
## GameObject Brush properties

The following properties are visible only when you select the **GameObject
Brush**. For more information about the brush and how to use it, refer to the
[GameObject
Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/GameObjectBrush.html)
documentation in the [2D Tilemap Extras
package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest).

Property | Description  
---|---  
**Cell** | Displays the positions and details of the element(s) contained in this brush in a linear array. This is non-interactable and you can’t change or add to the properties in this section.  
**Size** | Set the brush size by specifying the **X** , **Y** , and **Z** values in cells for each axis.  
**Pivot** | Set the pivot coordinates to define the brush’s rotation point.  
**Anchor** | Set the anchor coordinates of the cells that decide where in the cells the brush places GameObjects when you paint with it.  
  
## Group Brush properties

The following properties are visible only when you select the **Group Brush**.
For more information about the brush and how to use it, refer to the [Group
Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/GroupBrush.html)
documentation in the [2D Tilemap Extras
package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest).

Property | Description  
---|---  
**Gap** | Set the brush’s search radius. The value you set specifies the number of cells along each axis the brush search will scan. The brush then repeats the scan from each selected tile until the **Limit** value is reached.  
**Limit** | Set the brush’s total range. The value you set specifies the number of cells around the initial picked position. The brush value represents the maximum number of cells from the point of origin that the brush search will scan.  
  
## Random Brush properties

The following properties are visible only when you select the **Random
Brush**. For more information about the brush and how to use and define [Tile
Sets](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/RandomBrush.html%23usage),
refer to the [Random
Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/RandomBrush.html)
documentation in the [2D Tilemap Extras
package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest).

Property | Description  
---|---  
**Pick Random Tiles** | Enable this property to pick the tiles from the current selection as a random Tile Set.  
**Add To Random Tiles** | Enable this property to add the picked Tile Sets to existing Tile Sets instead of replacing them.  
**Tile Set Size** | Set the size of the Tile Set that this brush paints.  
**Number of Tiles** | The number of Tile Sets that this brush paints.  
  
## Line Brush properties

The following properties are visible only when you select the **Line Brush**.
For more information about the brush and how to use it, refer to the [Line
Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/LineBrush.html)
documentation in the [2D Tilemap Extras
package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest).

Property | Description  
---|---  
**Fill Gaps** | Enable to have Unity create orthogonal connections between all tiles that connect the start and end of the line painted.  
**Line Start** | Set the coordinates of the starting point of the line.  
  
## Additional resources

  * [2D Tilemap Extras package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest)
  * [Tile Palette editor reference](../tile-palette-editor-reference.html)

[](../../../tilemaps/tile-palettes/brushes/create-scriptable-brush.html)

Create a Scriptable Brush

[](../../../tilemaps/tile-palettes/brushes/active-brush-shortcuts-
reference.html)

Active brush shortcuts reference

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

