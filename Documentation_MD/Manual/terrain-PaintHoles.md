[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-PaintHoles.html)
  * [中文](/cn/current/Manual/terrain-PaintHoles.html)
  * [日本語](/ja/current/Manual/terrain-PaintHoles.html)
  * [한국어](/kr/current/Manual/terrain-PaintHoles.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-PaintHoles.html)
  * [中文](/cn/current/Manual/terrain-PaintHoles.html)
  * [日本語](/ja/current/Manual/terrain-PaintHoles.html)
  * [한국어](/kr/current/Manual/terrain-PaintHoles.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Terrain tools](terrain-Tools.html)
  * Paint Holes

[](terrain-RaiseLowerTerrain.html)

Raise or Lower Terrain

[](terrain-PaintTexture.html)

Paint Texture

# Paint Holes

Use the **Paint Holes** tool to hide portions of your **Terrain** The
landscape in your scene. A Terrain GameObject adds a large flat plane to your
scene and you can use the Terrain’s Inspector window to create a detailed
landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain). It allows you to paint openings in
the Terrain for formations such as caves and cliffs.

To access the tool, click the **Paint Terrain** icon, and select **Paint
Holes** from the drop-down menu.

![Paint Holes tool in the Terrain
Inspector](../uploads/Main/1.3.2-PaintHoles.png) Paint Holes tool in the
Terrain Inspector

To access **Paint Holes** from an overlay:

  1. In the **Terrain Tools** overlay, select **Sculpt Mode** ![Sculpt Mode Menu](../uploads/Main/terrainOverlays-SculptModeMenuButton.png). Sculpt Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Sculpt Mode tools on the **Terrain Tools** overlay, select **Paint Holes** ![Paint Holes button](../uploads/Main/terrainOverlays-PaintHolesButton.png).

To paint holes, click and drag the cursor across the Terrain. To erase holes
from the Terrain, click and drag while holding down the Shift key. Use the
**Brush Size** slider to control the size of your tool. The **Opacity** slider
determines the strength of the Brush when you apply it to the Terrain.

![](../uploads/Main/1.3.2-TerrainHole.png)

Internally, Unity uses a Texture to define the opacity mask for a Terrain
surface. When you use the **Paint Holes** tool to paint on a Terrain, it
modifies this Texture. Thus, any holes you paint are visible only if the
Terrain Material you use clips or discards texels based on this mask.

Because this tool uses a Texture, you might see aliased edges surrounding
holes you paint. Therefore, for example, when you make a cave, you might
choose to hide the aliased edges of the hole with other geometry such as rock
meshes.

Terrain holes work with lighting, physics, and **NavMesh** A mesh that Unity
generates to approximate the walkable areas and obstacles in your environment
for path finding and AI-controlled navigation. [More
info](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavInnerWorkings.html%23walkable-
areas)  
See in [Glossary](Glossary.html#NavMesh) baking. Unity discards the Terrain
information in areas where you paint holes to ensure accurate lighting,
Terrain **Colliders** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider), and baked NavMeshes.

To support physics Colliders, the resolution of the hole’s mask Texture is
equal to the resolution of the Terrain’s **heightmap** A greyscale Texture
that stores height data for an object. Each pixel stores the height difference
perpendicular to the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) \- 1.

## Additional resources

  * [Digging into Terrain Paint Holes in Unity 2019.3](https://unity.com/blog/engine-platform/digging-into-terrain-paint-holes-in-unity-2019-3)

* * *

  * Paint Holes added in [2019.3](https://docs.unity3d.com/2019.3/Documentation/Manual/30_search.html?q=newin20193) NewIn20193

[](terrain-RaiseLowerTerrain.html)

Raise or Lower Terrain

[](terrain-PaintTexture.html)

Paint Texture

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

