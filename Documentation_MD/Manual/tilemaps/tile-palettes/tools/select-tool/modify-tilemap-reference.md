[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/tile-palettes/tools/select-tool/modify-tilemap-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/tools/select-tool/modify-tilemap-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/tools/select-tool/modify-tilemap-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/tools/select-tool/modify-tilemap-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/tile-palettes/tools/select-tool/modify-tilemap-reference.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/tools/select-tool/modify-tilemap-reference.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/tools/select-tool/modify-tilemap-reference.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/tools/select-tool/modify-tilemap-reference.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [Tilemaps in Unity](../../../../tilemaps/tilemaps-landing.html)
  * [Tile palettes](../../../../tilemaps/tile-palettes/tile-palette-landing.html)
  * [Tile palette editor tools](../../../../tilemaps/tile-palettes/tools/tile-palette-tools-landing.html)
  * [The Select tool](../../../../tilemaps/tile-palettes/tools/select-tool/select-tool-landing.html)
  * Modify Tilemap reference

[](../../../../tilemaps/tile-palettes/tools/select-tool/grid-selection-
properties-reference.html)

Grid Selection properties reference

[](../../../../tilemaps/tile-palettes/tools/move-tiles-with-move-tool.html)

Move tiles with the Move tool

# Modify Tilemap reference

The **gizmo** A graphic overlay associated with a GameObject in a Scene, and
displayed in the Scene View. Built-in scene tools such as the move tool are
Gizmos, and you can create custom Gizmos using textures or scripting. Some
Gizmos are only drawn when the GameObject is selected, while other Gizmos are
drawn by the Editor regardless of which GameObjects are selected. [More
info](../../../../GizmosMenu.html#GizmosIcons)  
See in [Glossary](../../../../Glossary.html#Gizmo) **toolbar** A row of
buttons and basic controls at the top of the Unity Editor that allows you to
interact with the Editor in various ways (e.g. scaling, translation). [More
info](../../../../Toolbar.html)  
See in [Glossary](../../../../Glossary.html#Toolbar) in this section has
different gizmos you can use to change the **tilemap** A GameObject that
allows you to quickly create 2D levels using tiles and a grid overlay. [More
info](../../../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../../../Glossary.html#Tilemap) and its contents. You can
select different options and behaviors for inserting or removing rows and
columns of blank cells into the tilemap from the dropdown menu.

## Gizmo toolbar

Select a gizmo from the toolbar to activate as specific gizmo to change the
selected contents in the tilemap. The following table describes each option,
with links to examples showing how they affect the tilemap.

**Gizmo** | **Function**  
---|---  
None | No gizmo is active or shown in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../../../CreatingScenes.html)  
See in [Glossary](../../../../Glossary.html#Scene) view.  
Move | Activates and displays a **Move** gizmo in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](../../../../UsingTheSceneView.html)  
See in [Glossary](../../../../Glossary.html#SceneView). Use this to change the
offset of the selected contents.  
Rotate | Activates and displays a **Rotate** gizmo in the Scene view. Use this to change the rotation of the selected contents.  
Scale | Activates and displays a **Scale** gizmo in the Scene view. Use this to change the scale of the selected contents.  
Transform | Activates and displays a **Transform** gizmo in the Scene view. Use this to change the offset, rotation and scale of the selected contents all at once.  
  
### Gizmo function examples

**None**

![](../../../../../uploads/Main/None_ex.png)  
Default Tilemap and selected cell location. No Gizmo is activated or visible.

**Move**

![](../../../../../uploads/Main/Move_ex.png)  
**Left:** Default Tilemap and selected cell location. **Right:** Offset
changed for the selected cell locations.

**Rotate**

![](../../../../../uploads/Main/Rotate_ex.png)  
**Left:** Default Tilemap and selected cell location. **Right:** Rotation
changed for the selected cell locations.

**Scale**

![](../../../../../uploads/Main/Scale_ex.png)  
**Left** : Default Tilemap and selected cell location. **Right** : Scale
changed for the selected cell locations.

**Transform**

![](../../../../../uploads/Main/Transform_ex.png)  
**Left:** Default Tilemap and selected cell location. **Right:** Offset,
rotation and scale of the selected cell locations are modified.

## Cell rows and columns options

The dropdown menu provides different options for inserting or removing rows
and columns of blank cells onto the tilemap. After selecting one of the
dropdown menu options, enter the number of rows or columns to insert or remove
into the box and select **Modify**.

The following table describes each option, with links to examples showing how
they affect the tilemap.

**Property** | **Function**  
---|---  
Insert Row | Inserts one or more rows of blank cells at the selected location. Existing cells are displaced upward along the positive y-axis.  
Insert Row Before | Inserts one or more rows of blank cells below the selected location. Existing cells are displaced downward along the negative y-axis.  
Delete Row | Removes one or more rows of cells at the selected location and above. Existing cells above then collapse down to fill the space left by the deleted rows.  
Delete Row Before | Removes one or more rows of cells below the selected location. Existing cells below then shift upward along the positive y-axis to fill the space left by the deleted rows.  
Insert Column | Inserts one or more columns of blank cells at the selected location. Existing cells are displaced to the right along the positive x-axis.  
Insert Column Before | Inserts one or more columns of blank cells to the left of the selected cell. Existing cells are displaced to the left along the negative x-axis.  
Delete Column | Removes one or more columns of cells at the selected location and to its right. Existing cells then shift to the left along the negative x-axis to fill the space left by the deleted columns.  
Delete Column Before | Removes one or more columns of cells to the left of the selected cell. Existing cells shifted to the right along the positive x-axis to fill the space left by the deleted columns.  
  
### Examples of different dropdown menu options

**Insert Row**

![Insert Row](../../../../../uploads/Main/InsertRow_ex.png)  
**Left:** _Default Tilemap and selected cell location._ **Right:** _Insert
Row._

**Insert Row Before**

![Insert Row Before](../../../../../uploads/Main/InsertRowB4_ex.png)  
**Left:** _Default Tilemap and selected cell location._ **Right:** _Insert Row
Before._

**Delete Row**

![Delete Row](../../../../../uploads/Main/DelRow_ex.png)  
**Left:** _Default Tilemap and selected cell location._ **Right:** _Delete
Row._

**Delete Row Before**

![Delete Row Before](../../../../../uploads/Main/DelRowB4_ex.png)  
**Left:** _Default Tilemap and selected cell location._ **Right:** _Delete Row
Before._

**Insert Column**

![Insert Column](../../../../../uploads/Main/InsCol_ex.png)  
**Left:** _Default Tilemap and selected cell location._ **Right:** _Insert
Column._

**Insert Column Before**

![Insert Column Before](../../../../../uploads/Main/InsColB4_ex.png)  
**Left:** _Default Tilemap and selected cell location._ **Right:** _Insert
Column Before._

**Delete Column**

![Delete Column](../../../../../uploads/Main/DelCol_ex.png)**Left:** _Default
Tilemap and selected cell location._ **Right:** _Delete Column._

**Delete Column Before**

![Delete Column Before](../../../../../uploads/Main/DelColB4_ex.png)  
**Left:** _Default Tilemap and selected cell location._ **Right:** _Delete
Column Before._

### Multiple cell selection

When multiple cells are selected, the lower-leftmost cell is the main point of
reference when applying the Modify Tilemap options. See the following examples
of selecting multiple cells then modifying the Tilemap.

![Insert Row with multiple selected
cells](../../../../../uploads/Main/InsertRow_mult_ex.png)  
**Left:** _Default Tilemap with multiple cells selected._ **Right:** _Insert
Row._

![Insert Column with multiple selected
cells](../../../../../uploads/Main/InsertCol_mult_ex.png)  
**Left:** _Default Tilemap with multiple cells selected._ **Right:** _Insert
Column._

![Delete Row with multiple selected
cells](../../../../../uploads/Main/DelRow_mult_ex.png)  
**Left:** _Default Tilemap with multiple cells selected._ **Right:** _Delete
Row._

![Delete Column with multiple selected
cells](../../../../../uploads/Main/DelCol_mult_ex.png)  
**Left:** _Default Tilemap with multiple cells selected._ **Right:** _Delete
Column._

## Additional resources

  * [Grid Selection properties](./grid-selection-properties-reference.html)
  * [Tile Palette editor reference](../../tile-palette-editor-reference.html)

[](../../../../tilemaps/tile-palettes/tools/select-tool/grid-selection-
properties-reference.html)

Grid Selection properties reference

[](../../../../tilemaps/tile-palettes/tools/move-tiles-with-move-tool.html)

Move tiles with the Move tool

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

