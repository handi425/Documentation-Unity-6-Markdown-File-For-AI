[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-PaintTexture.html)
  * [中文](/cn/current/Manual/terrain-PaintTexture.html)
  * [日本語](/ja/current/Manual/terrain-PaintTexture.html)
  * [한국어](/kr/current/Manual/terrain-PaintTexture.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-PaintTexture.html)
  * [中文](/cn/current/Manual/terrain-PaintTexture.html)
  * [日本語](/ja/current/Manual/terrain-PaintTexture.html)
  * [한국어](/kr/current/Manual/terrain-PaintTexture.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Terrain tools](terrain-Tools.html)
  * Paint Texture

[](terrain-PaintHoles.html)

Paint Holes

[](terrain-SetHeight.html)

Set Height

# Paint Texture

Use the **Paint Texture** tool to add textures, such as grass, snow, or sand,
to your **Terrain** The landscape in your scene. A Terrain GameObject adds a
large flat plane to your scene and you can use the Terrain’s Inspector window
to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain). It allows you to draw areas of tiled
texture directly onto the Terrain. In the Terrain **Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), click the [**Paint
Terrain**](terrain-Tools.html) icon, and select **Paint Texture** from the
list of Terrain tools.

![Paint Texture tool in the Terrain
Inspector](../uploads/Main/1.3.3-PaintTexture_grey.png) Paint Texture tool in
the Terrain Inspector

To access the **Paint Texture** tool from an overlay:

  1. In the **Terrain Tools** overlay, select **Materials Mode** ![Material Mode Menu button](../uploads/Main/terrainOverlays-MaterialModeMenuButton.png). Materials Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Materials Mode tools on the **Terrain Tools** overlay, select **Paint Texture** ![Paint Texture](../uploads/Main/terrainOverlays-PaintTextureButton.png).

To configure the tool, you must first click the **Edit Terrain Layers** button
to add [Terrain Layers](class-TerrainLayer.html). The first Terrain Layer you
add flood-fills your Terrain with the configured texture. You can add multiple
Terrain Layers. However, the number of Terrain Layers each tile supports
depends on your specific **render pipeline** A series of operations that take
the contents of a Scene, and displays them on a screen. Unity lets you choose
from pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline). See the [Rendering
performance section on Terrain Layers](class-TerrainLayer.html#Performance)
for more information.

Next, you must choose a [Brush](class-Brush.html) for painting. Brushes are
Assets based on Textures, which define the shape of a brush. Select from the
built-in Brushes or create your own, then adjust the **Brush Size** and
**Opacity** (strength of the applied effect) of the brush.

Finally, in the **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view, click and drag the cursor across
the Terrain to create areas of tiled texture. You can paint across tile
boundaries to blend adjacent regions with a natural, organic look. Be aware,
however, that the Terrain system adds the selected Terrain Layer to any
Terrain you paint on, which might affect performance as mentioned above.

* * *

  * 2019–04–17 Page published 

  * Updated content to match new UI

[](terrain-PaintHoles.html)

Paint Holes

[](terrain-SetHeight.html)

Set Height

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

