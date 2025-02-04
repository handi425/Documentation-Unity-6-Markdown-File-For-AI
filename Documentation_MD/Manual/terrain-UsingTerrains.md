[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-UsingTerrains.html)
  * [中文](/cn/current/Manual/terrain-UsingTerrains.html)
  * [日本語](/ja/current/Manual/terrain-UsingTerrains.html)
  * [한국어](/kr/current/Manual/terrain-UsingTerrains.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-UsingTerrains.html)
  * [中文](/cn/current/Manual/terrain-UsingTerrains.html)
  * [日本語](/ja/current/Manual/terrain-UsingTerrains.html)
  * [한국어](/kr/current/Manual/terrain-UsingTerrains.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * Creating and editing Terrains

[](script-Terrain.html)

Terrain

[](terrain-CreateNeighborTerrains.html)

Create Neighbor Terrains

# Creating and editing Terrains

To add a Terrain GameObject to your Scene, select **GameObject > 3D Object >
Terrain** from the menu. This also adds a corresponding Terrain Asset to the
Project view. When you do this, the landscape is initially a large, flat
plane. The Terrain’s Inspector window provides a number of tools to create
detailed landscape features.

![Terrain editing tools in the
Inspector](../uploads/Main/1.1-TerrainInspector.png) Terrain editing tools in
the Inspector

Terrain editing tools in the Inspector

The **toolbar** A row of buttons and basic controls at the top of the Unity
Editor that allows you to interact with the Editor in various ways (e.g.
scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar) provides five options to adjust your
Terrain:

  * Create adjacent Terrain tiles.
  * Sculpt and paint your Terrain.
  * Add trees.
  * Add details such as grass, flowers, and rocks.
  * Change general settings for the selected Terrain.

For more information about each of these icons, see [Create Neighbor
Terrains](terrain-CreateNeighborTerrains.html), [Terrain tools](terrain-
Tools.html), [Trees](terrain-Trees.html)A GameObject and associated Component
that allows you to add tree assets to your Scene. You can add branch levels
and leaves to trees in the Tree Inspector window. [More info](class-Tree.html)  
See in [Glossary](Glossary.html#Tree), [Grass and other details](terrain-
Grass.html), and [Terrain Settings](terrain-OtherSettings.html).

Select the paintbrush icon to access painting tools, which allow you to modify
the Terrain. Use the cursor to sculpt the height of the Terrain, or paint
texture onto the Terrain. Choose from several built-in Brush shapes, or define
your own Brush using a texture. You can also change the size and opacity (the
strength of the applied effect) of the Brush. Once you’ve defined the
properties, your cursor takes the shape of the selected Brush. Click or drag
on the Terrain to create different shapes and textures.

Similar to how you paint with a Brush on the Terrain, you can add textures,
trees, and details like grass, flowers, and rocks. You can also create
additional connected Terrain tiles, change the height of an entire tile, and
even write custom Brushes with complex effects.

## Terrain Overlay Windows

Terrain tools can be used with overlays. When a Terrain **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) is selected, overlays will appear
in the **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) View. These overlays can be docked,
dragged, and collapsed.

The **Terrain Toolbar** overlay contains the terrain tools, divided into
categories. From left to right, the menu buttons are **Sculpt Mode** ,
**Materials Mode** , **Foliage Mode** , and **Neighbor Terrains Mode**. If
there are custom tools which inherit from
[TerrainAPI.TerrainPaintToolWithOverlays](../ScriptReference/TerrainTools.TerrainPaintToolWithOverlays_1.html),
they will appear in a fifth menu button for **Custom Brushes Mode**.

![Terrain Toolbar](../uploads/Main/terrainOverlays-TerrainToolbar.png) Terrain
Toolbar

The **Tool Settings** overlay can be found under the overlay with this icon
![Tool settings icon](../uploads/Main/terrainOverlays-toolSettingsIcon.png).
Some tools have additional settings that can be edited. For example, here is
what the tool settings overlay looks like for the Set Height Tool.

![Set Height Tool Settings](../uploads/Main/terrainOverlays-
ToolSettingsSetHeight.png) Set Height Tool Settings

Certain tools may have brush masks. When selecting a tool that has access to
brushes, the **Brush Masks** overlay will be visible.

![Brush Masks in Overlays](../uploads/Main/terrainOverlays-BrushMasks.png)
Brush Masks in Overlays

Certain tools which have access to brushes may also have access to the **Brush
Attributes** overlay, in which users can change tool settings like brush
opacity and size.

![Brush Attributes in Overlays](../uploads/Main/terrainOverlays-
BrushAttributes.png) Brush Attributes in Overlays

The Paint Details tool has access to Target Strength in this overlay.

![Brush Attributes Target Strength in
Overlays](../uploads/Main/terrainOverlays-BrushAttributesTargetStrength.png)
Brush Attributes Target Strength in Overlays

## Terrain keyboard shortcuts

The Terrain **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) has the following keyboard
shortcuts enabled by default.

Keys | Function  
---|---  
Comma ( , ) and Period ( . ) | Cycle through the available Brushes  
Shift-Comma ( < ) and Shift-Period ( > ) | Cycle through the available objects for trees, textures, and details  
Open Bracket ( [ ) and Close Bracket ( ] ) | Decrease and increase the Brush Size  
Minus ( - ) and Equal ( = ) | Decrease and increase Brush Opacity  
  
To set your own custom shortcuts, use the **Shortcuts Manager**.

  * On Windows and Linux, select **Edit > Shortcuts**.
  * On macOS, select **Unity > Shortcuts**.

Under **Category** A Profiler category identifies the workload data for a
Unity subsystem (for example, Rendering, Scripting and Animation categories).
Unity applies colour-coding to categories to help visually distinguish the
types of data in the Profiler window. [More info](ProfilerWindow.html)  
See in [Glossary](Glossary.html#category), select **Terrain** to display
Terrain-related shortcut assignments. For more information about setting and
modifying shortcuts, see the [Shortcuts Manager](ShortcutsManager.html) page.

![List of Terrain shortcuts](../uploads/Main/1.1-TerrainShortcuts.png) List of
Terrain shortcuts

Additionally, the standard F keystroke works slightly differently for Terrain.
As Terrains are typically very large, when you press the F key, the **Scene
view** An interactive view into the world you are creating. You use the Scene
View to select and position scenery, characters, cameras, lights, and all
other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) focuses on the area where you
position the cursor. This provides a very quick and intuitive way to jump to
the Terrain area you want to edit. If you press F while the cursor is not over
a Terrain tile, it uses the standard framing behavior, framing the selection
around the whole GameObject when you place the cursor over the Scene view.

## Additional resources

  * [Scripting Reference for custom Terrain tools](../ScriptReference/TerrainTools.TerrainPaintTool_1.html)

* * *

  * 2019–04–17 Page amended 

  * Updated content to match new UI and added information about keyboard shortcuts

[](script-Terrain.html)

Terrain

[](terrain-CreateNeighborTerrains.html)

Create Neighbor Terrains

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

