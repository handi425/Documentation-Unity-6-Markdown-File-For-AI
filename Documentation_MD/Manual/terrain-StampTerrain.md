[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-StampTerrain.html)
  * [中文](/cn/current/Manual/terrain-StampTerrain.html)
  * [日本語](/ja/current/Manual/terrain-StampTerrain.html)
  * [한국어](/kr/current/Manual/terrain-StampTerrain.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-StampTerrain.html)
  * [中文](/cn/current/Manual/terrain-StampTerrain.html)
  * [日本語](/ja/current/Manual/terrain-StampTerrain.html)
  * [한국어](/kr/current/Manual/terrain-StampTerrain.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Terrain tools](terrain-Tools.html)
  * Stamp Terrain

[](terrain-SmoothHeight.html)

Smooth Height

[](class-TerrainLayer.html)

Terrain Layers

# Stamp Terrain

Use the **Stamp Terrain** tool to stamp a brush shape on top of the current
[heightmap](terrain-Heightmaps.html)A greyscale Texture that stores height
data for an object. Each pixel stores the height difference perpendicular to
the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap). In the **Terrain Inspector** ,
click on the **Paint Terrain** icon and select **Stamp Terrain** from the
drop-down menu.

![Stamp Terrain tool in the Terrain
Inspector](../uploads/Main/1.3.6-StampTerrain.png) Stamp Terrain tool in the
Terrain Inspector

To access the **Stamp**Terrain** The landscape in your scene. A Terrain
GameObject adds a large flat plane to your scene and you can use the Terrain’s
Inspector window to create a detailed landscape. [More info](terrain-
UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain)** tool from an overlay:

  1. In the **Terrain Tools** overlay, select **Sculpt Mode** ![Sculpt Mode Menu](../uploads/Main/terrainOverlays-SculptModeMenuButton.png). Sculpt Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Sculpt Mode tools on the **Terrain Tools** overlay, select **Stamp Terrain** ![Stamp Terrain button](../uploads/Main/terrainOverlays-StampTerrainButton.png).

**Stamp Terrain** is useful if you create a custom brush using a Texture that
represents a heightmap with a specific geological feature, such as a hill.

With the **Stamp Terrain** tool, you can choose an existing brush and apply it
with a single click. Each click raises the Terrain to the set **Stamp Height**
in the shape of the selected brush. To multiply the **Stamp Height** by a
percentage, move the **Opacity** slider to change its value. For example, a
**Stamp Height** of 200 and an **Opacity** of 50% sets the height of each
stamp to 100.

The **Max <–> Add** slider lets you choose whether to pick the maximum height,
or add the height of your stamp to the Terrain’s current height.

  * If you set the **Max <–> Add** value to 0, then stamp onto the Terrain, Unity compares the height of your stamp to the current height of the stamped area, and sets the final height to the value that is higher.

  * If you set the **Max <–> Add** value to 1, then stamp onto the Terrain, Unity adds the height of your stamp to the current height of the stamped area, so that the final height is the sum of both values.

Enable the **Subtract** checkbox to subtract the height of any stamps you
apply to the Terrain from the existing height of the stamped area. Note that
**Subtract** works only if your **Max <–> Add** value is greater than zero,
for example, if you set the **Max <–> Add** value to 1. If the stamp height
exceeds the current height of the stamped area, the system levels the height
to zero.

* * *

  * 2019–04–18 Page published 

  * Updated content to reflect new UI and options

[](terrain-SmoothHeight.html)

Smooth Height

[](class-TerrainLayer.html)

Terrain Layers

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

