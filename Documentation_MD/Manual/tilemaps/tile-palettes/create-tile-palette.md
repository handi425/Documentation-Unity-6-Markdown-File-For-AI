[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/tile-palettes/create-tile-palette.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/create-tile-palette.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/create-tile-palette.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/create-tile-palette.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/tile-palettes/create-tile-palette.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/create-tile-palette.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/create-tile-palette.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/create-tile-palette.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Tilemaps in Unity](../../tilemaps/tilemaps-landing.html)
  * [Tile palettes](../../tilemaps/tile-palettes/tile-palette-landing.html)
  * Create a Tile Palette

[](../../tilemaps/tile-palettes/tile-palette-landing.html)

Tile palettes

[](../../tilemaps/tile-palettes/brushes/tile-palette-brushes-landing.html)

Tile palette brushes

# Create a Tile Palette

Place a selection of Tiles onto **Tile Palettes** so that you can pick Tiles
from the Palette to paint on **Tilemaps** A GameObject that allows you to
quickly create 2D levels using tiles and a grid overlay. [More
info](../../tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](../../Glossary.html#Tilemap).

## Prerequisites

To create a tilemap you must first ensure you have done the following:

  * Download the **2D Tilemap Editor** package from the [Package Manager](../../Packages.html).

## Create the tile palette asset

To create the tile palette asset, do the the following:

  1. To create a **Tile Palette** , open the **Tile Palette** window by going to **Window > 2D > Tile Palette**.

  2. Select the **New Palette** drop-down menu to open a list of Tile Palettes available in the Project, or for the option to create a new Palette. Select the **Create New Palette** option to create a new Palette.

![](../../../uploads/Main/2d-tile-palette-create-new.png)  
Select the **Create New Palette** option from the dropdown menu.

  3. After selecting the option to create a new Tile Palette, the **Create New Palette** dialog box becomes available. It contains the different property settings and options available when creating a new Palette. Name the newly created Palette and select the desired settings, then select the Create button. Select the folder to save the Palette Asset file into when prompted. The newly created Palette is automatically loaded in the Tile Palette window.

![](../../../uploads/Main/2d-tile-palette-blank.png)  
A blank Tile Palette

  4. Drag and drop Textures or **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) from the Assets folder onto the
**Tile Palette** , and choose where to save the new [Tile Assets](../tiles-
for-tilemaps/tile-asset-reference.html) when prompted. New Tile Assets are
generated in the selected save location, and the Tiles are placed on the grid
of the active Tile Palette window.

![](../../../uploads/Main/2d-tile-palette-drag-drop.png)  
Drag and drop directly onto the Tile Palette window.

  5. Use **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../UsingTheInspector.html)  
See in [Glossary](../../Glossary.html#Inspector) to change the current active
Brush and its properties. For more information on these properties, refer to
the [Brush Inspector window reference](brushes/brush-inspector-
reference.html).

## Editing the Tile Palette

The tools for picking and painting with Tiles can also be used to edit the
Tile Palette directly, allowing you to move and manipulate the Tiles currently
placed on the **Tile Palette**. Select the Palette you want to edit from the
**Palette** dropdown menu (the default Palette is named ‘New Palette’), then
select **Edit** to unlock the Palette for editing.

![](../../../uploads/Main/2d-tile-palette-toggle-edit.png)  
The Tile Palette Edit toggle.

Refer to [Tile Palette editor reference](./tile-palette-editor-reference.html)
for the shortcuts and functions of the Palette tools, which can also be used
to edit the Palette.

## Creating Palette Assets from existing Grid Prefabs

You can convert an existing [Prefab](../../Prefabs.html)An asset type that
allows you to store a GameObject complete with components and properties. The
prefab acts as a template from which you can create new object instances in
the scene. [More info](../../Prefabs.html)  
See in [Glossary](../../Glossary.html#Prefab) to a Palette Asset, so that you
can use it in the Tile Palette window. To do this, the Prefab must not already
be a Palette Asset, and it must have a Grid component on its topmost
****GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject)**.

![](../../../uploads/Main/2d-tile-palette-active-brush-toolbar.png)  
The Tile Palette toolbar

To convert a Prefab, drag and drop it onto the Tile Palette **toolbar** A row
of buttons and basic controls at the top of the Unity Editor that allows you
to interact with the Editor in various ways (e.g. scaling, translation). [More
info](../../Toolbar.html)  
See in [Glossary](../../Glossary.html#Toolbar) (highlighted in the image
above). The Editor automatically converts it to a Palette Asset, and adds a
Grid Palette Asset. The new Palette Asset has the same name as its source, and
it becomes available in the Palette dropdown menu.

## Tile Palette Grid visibility toggle

![](../../../uploads/Main/2d-tile-palette-toggle-grid.png)  
The Tile Palette Grid toggle.

Switch the visibility of the Grid on the Tile Palette on or off by selecting
the toggle highlighted above.

## Tile Palette Gizmos visibility toggle

The Tile Palette can display [Gizmos](../../GizmosMenu.html)A graphic overlay
associated with a GameObject in a Scene, and displayed in the Scene View.
Built-in scene tools such as the move tool are Gizmos, and you can create
custom Gizmos using textures or scripting. Some Gizmos are only drawn when the
GameObject is selected, while other Gizmos are drawn by the Editor regardless
of which GameObjects are selected. [More
info](../../GizmosMenu.html#GizmosIcons)  
See in [Glossary](../../Glossary.html#Gizmo) over the currently selected
Palette Asset, to help you visualize specific criteria. For example, you can
add a Gizmo that displays a special icon for Tiles that contain no Sprites.

![](../../../uploads/Main/2d-tile-palette-gizmos.png)  
The Tile Palette Gizmos toggle.

To display the default Unity and the Palette Asset’s Gizmos on the Tile
Palette, enable the Gizmos toggle (highlighted above). The Tile Palette
immediately displays any component with
[MonoBehaviour.OnDrawGizmos()](../../../ScriptReference/MonoBehaviour.OnDrawGizmos.html)
in the Palette Asset.

To add your own custom gizmos to a Palette Asset, add a component with
`DrawGizmo` to the Palette Asset:

  1. Select the Palette Asset in the ****Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](../../ProjectView.html)  
See in [Glossary](../../Glossary.html#Projectwindow)**.

  2. Open the Palette Asset in [Prefab Mode](../../EditingInPrefabMode.html).
  3. Add the component while in Prefab Mode.
  4. Save the Asset while in Prefab Mode.
  5. Exit Prefab Mode.

[](../../tilemaps/tile-palettes/tile-palette-landing.html)

Tile palettes

[](../../tilemaps/tile-palettes/brushes/tile-palette-brushes-landing.html)

Tile palette brushes

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

