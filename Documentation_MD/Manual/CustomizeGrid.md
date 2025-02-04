[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CustomizeGrid.html)
  * [中文](/cn/current/Manual/CustomizeGrid.html)
  * [日本語](/ja/current/Manual/CustomizeGrid.html)
  * [한국어](/kr/current/Manual/CustomizeGrid.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CustomizeGrid.html)
  * [中文](/cn/current/Manual/CustomizeGrid.html)
  * [日本語](/ja/current/Manual/CustomizeGrid.html)
  * [한국어](/kr/current/Manual/CustomizeGrid.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * [The Scene view](UsingTheSceneView.html)
  * [Scene view grid snapping](GridSnapping.html)
  * Customize the grid

[](GridAlign.html)

Align a GameObject to the grid

[](GridShortcuts.html)

Grid and snap shortcuts

# Customize the grid

This section provides information on how to customize the grid in the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view window.

## Display and hide grid lines

To toggle whether the grid is visible on all axes, select **Toggle grid
visibility** (![](../uploads/Main/SceneGrids-Vis-icon-inline.png)) in the
[Grid and Snap](GridAndSnapOverlay.html).

## Change the axis that the grid appears on

If you are in [orthographic mode](SceneViewNavigation.html) (Iso) and align
your view with an axis, the Editor chooses to display the grid axis orthogonal
to that axis.

To change which axis the grid appears on:

  1. In the **Grid and Snap** overlays **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar), select the downward facing arrow
next to **Toggle grid visibility** (![](../uploads/Main/SceneGrids-Vis-icon-
inline.png)) to open the **Grid Visual** menu. .

  2. In the **Grid Plane** section, select the axis you want to display.

## Resize the grid

You can set the size of the grid lines that display in the **Scene view** An
interactive view into the world you are creating. You use the Scene View to
select and position scenery, characters, cameras, lights, and all other types
of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) window. The size of the grid
affects how your grid looks and how your **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) [automatically snap to the
grid](GridSnap.html) and how your GameObjects [move, rotate, or scale using
snap increments](SnapIncrements.html).

If you set a size for all axes at once, you display a uniform, square-based,
grid. However, you can also use different values on any of the three axes to
display a non-uniform, rectangular-based, grid. By default, the grid is set to
a uniform size of 1 on all axes.

You can also use the **Grid size field** in the [Grid and
Snap](GridAndSnapOverlay.html) to set a uniform grid size without opening the
**Snapping** menu.

To resize the grid:

  1. In the **Grid and Snap** overlay, select the arrow next to the **Grid Snapping** button to open the **Snapping** menu.
  2. To enter a uniform value for the grid size and make all grid lines the same length: 
    1. Select the link icon in the **Size** property.
    2. Enter a value for the **X** property to set the size of the grid lines on all axes.
  3. To enter non-uniform values for the grid size and specify the size of each grid axis separately: 
    1. Make sure that the link icon in the **Size** property is not selected.
    2. Enter a value for the **X** , **Y** , and **Z** properties to set the size of the grid lines on each axis.

**Tip** : You can also use [these keyboard shortcuts](GridShortcuts.md) to
increase or decrease the size of the grid.

## Change the default color of the grid lines

To change the color of the visible grid lines in the **Scene view** window:

  1. Open the Unity [Preferences](Preferences.html) window.
  2. Select the **Colors** tab in the Preferences window.
  3. Use the color picker to set a new color.

## Change the opacity of the grid

To adjust the brightness of the grid lines:

  1. From the **Grid and Snap** overlays toolbar, select the downward facing arrow next to **Toggle grid visibility** (![](../uploads/Main/SceneGrids-Vis-icon-inline.png)) to open the **Grid Visual** menu.
  2. Use the **Opacity** slider to make the grid more or less visible in the Scene view.

## Move the grid to the handle of a GameObject

To move the grid to the handle of a GameObject:

  1. Select a GameObject.
  2. In the **Grid and Snap** overlay, select the downward facing arrow next to **Toggle grid visibility** (![](../uploads/Main/SceneGrids-Vis-icon-inline.png)) to open the **Grid Visual** menu.
  3. In the **Grid Visual** menu, in the **Move to** property, select **Handle** to move the grid to the handle of the selected GameObject.
  4. To move the grid back to its default position, in the **Move to** property, select **Origin**.

## Reset grid values and settings to default

To reset the grid axis and opacity settings to their defaults:

  1. In the **Grid and Snap** overlay, select the downward facing arrow next to **Toggle grid visibility** to open the **Grid Visual** menu (![](../uploads/Main/SceneGrids-Vis-icon-inline.png)).
  2. Select the **More** menu (⋮).
  3. Select **Reset**.

To reset the size of the grid and the increment snap values to their defaults:

  1. In the **Grid and Snap** overlays toolbar, select the downward facing arrow next to **Toggle grid snapping** (![](../uploads/Main/SceneGrids-Mode-icon-inline.png)) to open the **Snapping** menu.
  2. Select the **More** menu (⋮).
  3. Select **Reset**.

## Additional resources

  * [Scene view grid snapping](GridSnapping.html)
  * [Grid and Snap overlay](GridAndSnapOverlay.html)
  * [Overlays](overlays.html)
  * [The Scene view](UsingTheSceneView.html)
  * [Position GameObjects](PositioningGameObjects.html)

[](GridAlign.html)

Align a GameObject to the grid

[](GridShortcuts.html)

Grid and snap shortcuts

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

