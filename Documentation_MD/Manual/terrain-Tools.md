[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-Tools.html)
  * [中文](/cn/current/Manual/terrain-Tools.html)
  * [日本語](/ja/current/Manual/terrain-Tools.html)
  * [한국어](/kr/current/Manual/terrain-Tools.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-Tools.html)
  * [中文](/cn/current/Manual/terrain-Tools.html)
  * [日本語](/ja/current/Manual/terrain-Tools.html)
  * [한국어](/kr/current/Manual/terrain-Tools.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * Terrain tools

[](terrain-CreateNeighborTerrains.html)

Create Neighbor Terrains

[](terrain-RaiseLowerTerrain.html)

Raise or Lower Terrain

# Terrain tools

To access the **Terrain** The landscape in your scene. A Terrain GameObject
adds a large flat plane to your scene and you can use the Terrain’s Inspector
window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) painting tools, click on a Terrain
object in the **Hierarchy** window and open an **Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. In the Inspector, click the
**Paint Terrain** (paintbrush) icon to reveal the list of Terrain tools.

![Terrain tools drop-down menu](../uploads/Main/TerrainToolsDropdown_grey.png)
Terrain tools drop-down menu

You can also access Terrain painting tools from the Terrain Tools overlay in
**Sculpt Mode** ![Sculpt Mode Menu button](../uploads/Main/terrainOverlays-
SculptModeMenuButton.png) or **Materials Mode** ![Material Mode Menu
button](../uploads/Main/terrainOverlays-MaterialModeMenuButton.png).

![Terrain Toolbar](../uploads/Main/terrainOverlays-TerrainToolbar.png) Terrain
Toolbar

The Terrain component provides six distinct tools:

  * **Raise or Lower Terrain** : paint the **heightmap** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) with a paintbrush tool.

  * **Paint Holes** : hide portions of the Terrain.
  * **Paint Texture** : apply surface textures.
  * **Set Height** : adjust the heightmap toward a specific value.
  * **Smooth Height** : smooth the heightmap to soften Terrain features.
  * **Stamp Terrain** : stamp a brush shape on top of the current heightmap.

You can also create your own custom Terrain tools. For more information about
this, see API documentation on
[TerrainAPI.TerrainPaintTool](../ScriptReference/TerrainTools.TerrainPaintTool_1.html),
and see Unity’s [GitHub repository for Terrain
Tools](https://github.com/Unity-Technologies/TerrainToolSamples).

To create a custom Terrain tool with overlay support, refer to API
documentation on
[TerrainAPI.TerrainPaintToolWithOverlays](../ScriptReference/TerrainTools.TerrainPaintToolWithOverlays_1.html).

* * *

  * 2019–10–22 Page amended 

  * Updated screenshot to match the new UI and added the Paint Holes tool.

[](terrain-CreateNeighborTerrains.html)

Create Neighbor Terrains

[](terrain-RaiseLowerTerrain.html)

Raise or Lower Terrain

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

