[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-grid-cells.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-grid-cells.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-grid-cells.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-grid-cells.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-grid-cells.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-grid-cells.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-grid-cells.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-grid-cells.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Tilemaps in Unity](../../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * [Isometric tilemaps in Unity](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html)
  * Isometric tilemap grid cells

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-
tilemaps.html)

Isometric tilemaps

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-
renderer-isometric-landing.html)

Tilemap Renderer for Isometric Tilemaps

# Isometric tilemap grid cells

The **Cell Size** and **Cell Layout** properties of the Grid object the
**Tilemap** A GameObject that allows you to quickly create 2D levels using
tiles and a grid overlay. [More info](../../../tilemaps/work-with-
tilemaps/tilemap-reference.html)  
See in [Glossary](../../../Glossary.html#Tilemap) is the child of determine
some of the characteristics of the tilemap’s appearance. For more information
on these properties, refer to the [Grid component reference](../../grid-
reference.html).

When the Cell Layout property is set to Isometric Z as Y, tiles on the tilemap
have their Z-axis value is added to its Y-axis value. This causes the Tile to
be visually offset along the Y-axis by that value, creating the illusion of
height as the Tiles are placed on the Tilemap.

Isometric Tilemaps use either **dimetric projection** or true **isometric
projection** parallel projection angles. For more information about the two
forms of projection, please refer to this
[article](https://en.wikipedia.org/wiki/Isometric_computer_graphics) for
further details.

Changing the Cell Size of the Grid component changes the size of angles that
make up each Cell, which affects the type of projection being simulated. By
default, Cell Size of the Isometric Cell Layout is **(1, 0.5, 1)** which
simulates **dimetric projection** angles. True **isometric projection**
instead uses a Y value of **0.57735**.

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-
tilemaps.html)

Isometric tilemaps

[](../../../tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-
renderer-isometric-landing.html)

Tilemap Renderer for Isometric Tilemaps

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

