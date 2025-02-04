[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-CreateNeighborTerrains.html)
  * [中文](/cn/current/Manual/terrain-CreateNeighborTerrains.html)
  * [日本語](/ja/current/Manual/terrain-CreateNeighborTerrains.html)
  * [한국어](/kr/current/Manual/terrain-CreateNeighborTerrains.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-CreateNeighborTerrains.html)
  * [中文](/cn/current/Manual/terrain-CreateNeighborTerrains.html)
  * [日本語](/ja/current/Manual/terrain-CreateNeighborTerrains.html)
  * [한국어](/kr/current/Manual/terrain-CreateNeighborTerrains.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * Create Neighbor Terrains

[](terrain-UsingTerrains.html)

Creating and editing Terrains

[](terrain-Tools.html)

Terrain tools

# Create Neighbor Terrains

The **Create Neighbor Terrains** tool allows you to create adjacent
**Terrain** The landscape in your scene. A Terrain GameObject adds a large
flat plane to your scene and you can use the Terrain’s Inspector window to
create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) tiles, which automatically connect.
In the **Terrain Inspector** , click the **Create Neighbor Terrains** icon.

![Create Neighbor Terrains tool in the Terrain
Inspector](../uploads/Main/1.3.1-CreateNeighborTerrains_grey.png) Create
Neighbor Terrains tool in the Terrain Inspector

To access the **Create Neighbor Terrains** tool from an overlay:

  1. In the **Terrain Tools** overlay, select **Neighbor Terrains Mode** ![Create Neighbor Terrains Menu](../uploads/Main/terrainOverlays-CreateNeighborsButtonMenu.png). Neighbor Terrain tools display at the end of the **Terrain Tools** overlay.
  2. From the available Sculpt Mode tools on the **Terrain Tools** overlay, select **Create Neighbor Terrains** ![Create Neighbor Terrains Menu](../uploads/Main/terrainOverlays-CreateNeighborsButtonMenu.png).

When you select the tool, Unity highlights areas around the selected Terrain
tile, indicating spaces where you can place a new, connected tile.

![Spaces where you can create new Terrain tiles](../uploads/Main/1.3.1-create-
neighbor-terrains.png) Spaces where you can create new Terrain tiles

Enable the **Fill** Heightmap__ Using Neighbors__ checkbox to fill the new
Terrain tile’s heightmap with a cross-blend of neighboring Terrain tiles’
heightmaps, which ensures that the height of the new tile’s edges match up
with adjacent tiles.

Choose a property from the **Fill Heightmap Address Mode** drop-down menu to
determine how to cross-blend the heightmaps of adjacent tiles:

**Property** | **Description**  
---|---  
**Clamp** | Unity performs a cross-blend between the heights along the edges of neighboring Terrain tiles that share a border with the new tile. Each Terrain tile has up to four neighboring tiles: top, bottom, left, and right. If there is no tile in any of the four adjacent spaces, the heights along that respective border are taken as zero.  
**Mirror** | Unity mirrors each of the adjacent Terrain tiles, and cross-blends their heightmaps to produce the heightmap for the new tile. If there is no tile in any of the four adjacent spaces, the heights for that specific tile location are taken as zero.  
  
To create a new Terrain tile, click any of the available spaces next to an
existing tile. The Editor creates a new Terrain tile in the same group as the
selected Terrain, and copies over the settings of the tile it connects to. It
also creates a new [TerrainData](../ScriptReference/TerrainData.html) Asset.

By default, Unity enables **Auto connect** in the [Terrain Settings](terrain-
OtherSettings.html) of a Terrain tile. When **Auto connect** is enabled, the
Terrain system automatically manages the connections between neighboring
Terrain tiles, and a tile automatically connects to any neighbors with the
same **Grouping ID**.

![Terrain Settings for a Terrain
tile](../uploads/Main/1.3.1-TerrainSettings_grey.png) Terrain Settings for a
Terrain tile

On rare occasions, you might lose connections between tiles if you change the
**Grouping ID** , or disable **Auto connect** for one or more tiles. To
recreate connections between Terrain tiles, click the **Reconnect** button.
**Reconnect** only connects two adjacent tiles if they have the same
**Grouping ID** and if both tiles have **Auto Connect** enabled.

Connecting Terrain tiles in a group allows you to use other tools to paint
textures or adjust the heightmaps of the group so that there are no seams. At
run time, the Terrain system automatically blends the tessellation and
**normal map** A type of Bump Map texture that allows you to add surface
detail such as bumps, grooves, and scratches to a model which catch the light
as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) of connected tiles. This ensures
they appear as a single piece of Terrain, without seams or artifacts.

If you attempt to paint across two unconnected tiles in a single stroke, Unity
treats them as separate tiles, so any effects you apply might appear only on
one tile or display differently on each tile.

* * *

  * 2019–04–17 Page amended 

  * Updated content to reflect new UI and options

[](terrain-UsingTerrains.html)

Creating and editing Terrains

[](terrain-Tools.html)

Terrain tools

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

