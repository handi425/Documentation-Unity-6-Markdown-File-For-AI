[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-SmoothHeight.html)
  * [中文](/cn/current/Manual/terrain-SmoothHeight.html)
  * [日本語](/ja/current/Manual/terrain-SmoothHeight.html)
  * [한국어](/kr/current/Manual/terrain-SmoothHeight.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-SmoothHeight.html)
  * [中文](/cn/current/Manual/terrain-SmoothHeight.html)
  * [日本語](/ja/current/Manual/terrain-SmoothHeight.html)
  * [한국어](/kr/current/Manual/terrain-SmoothHeight.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Terrain tools](terrain-Tools.html)
  * Smooth Height

[](terrain-SetHeight.html)

Set Height

[](terrain-StampTerrain.html)

Stamp Terrain

# Smooth Height

The Smooth Height tool smooths the [heightmap](terrain-Heightmaps.html)A
greyscale Texture that stores height data for an object. Each pixel stores the
height difference perpendicular to the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) and softens **Terrain** The
landscape in your scene. A Terrain GameObject adds a large flat plane to your
scene and you can use the Terrain’s Inspector window to create a detailed
landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) features. In the Terrain
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), select **Paint Terrain** , and
select **Smooth Height** from the list of Terrain tools.

![Smooth Height tool in the Terrain
Inspector](../uploads/Main/1.3.5-SmoothHeight_grey.png) Smooth Height tool in
the Terrain Inspector

To access the **Set Height** tool from an overlay:

  1. In the **Terrain Tools** overlay, select **Sculpt Mode** ![Sculpt Mode Menu](../uploads/Main/terrainOverlays-SculptModeMenuButton.png). Sculpt Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Sculpt Mode tools on the **Terrain Tools** overlay, select **Smooth Height** ![Smooth Height](../uploads/Main/terrainOverlays-SmoothHeightButton.png).

The **Smooth Height** tool averages out nearby areas, softens the landscape
and reduces the appearance of abrupt changes; it does not significantly raise
or lower Terrain height.

Smoothing is useful after you paint with brushes containing high frequency
patterns. These brush patterns tend to introduce sharp, jagged edges into a
landscape, but you can use the Smooth Height tool to soften that roughness.

Adjust the Blur Direction value to control which areas to soften. If you set
**Blur Direction** to –1, the tool softens exterior (convex) edges of your
Terrain. If you set **Blur Direction** to 1, the tool softens interior
(concave) edges of your Terrain. To smooth all parts of your Terrain evenly,
set **Blur Direction** to 0.

The **Brush Size** value determines the size of the Brush to use, and the
**Opacity** value determines how quickly the tool smooths out the area you’re
painting.

* * *

  * 2019–04–17 Page published 

  * Updated content to reflect new UI and options

[](terrain-SetHeight.html)

Set Height

[](terrain-StampTerrain.html)

Stamp Terrain

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

