[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/InspectorFocused.html)
  * [中文](/cn/current/Manual/InspectorFocused.html)
  * [日本語](/ja/current/Manual/InspectorFocused.html)
  * [한국어](/kr/current/Manual/InspectorFocused.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/InspectorFocused.html)
  * [中文](/cn/current/Manual/InspectorFocused.html)
  * [日本語](/ja/current/Manual/InspectorFocused.html)
  * [한국어](/kr/current/Manual/InspectorFocused.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * [The Inspector window](UsingTheInspector.html)
  * Focused Inspectors

[](InspectorOptions.html)

Working in the Inspector

[](EditingValueProperties.html)

Editing properties

# Focused Inspectors

A focused **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) is a dedicated Inspector window for
a specific **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), Unity component, or Asset. It
always displays the properties of the item you opened it for, even if you
select something else in the **Scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) or Project.

Focused Inspectors work just like regular Inspectors, except for the following
differences:

  * They do not update to show the properties for the current selection.
  * You cannot lock them. Each focused Inspector shows a specific item’s properties, so there’s no need.
  * You cannot toggle between Debug and Normal mode from a focused Inspector.

You can open as many focused Inspectors as you want. Focused Inspectors open
in floating windows that you can [reposition, dock, and
resize](CustomizingYourWorkspace.html) in the same way you can any other
window.

Unity saves any open focused Inspectors when you close a Project, and restores
them when you reopen it.

## Open focused Inspectors

There are several ways to open a focused Inspector, depending on what you’re
inspecting.

Unity adds focused Inspectors to the list of open windows (Menu: **Window >
Panels > _[LIST OF OPEN WINDOWS]_**).

Select a focused Inspector from the list to bring it to the front.

### For GameObjects and Project Assets

To open a focused Inspector for a single GameObject or Asset:

  1. Right-click a GameObject in the Hierarchy view, or an Asset in the Project view.
  2. From the context menu, select **Properties**.

Alternatively, select the GameObject or Asset and do one of the following:

  * From the main menu, select **Assets > Properties**.
  * Use the **Alt + P** / **Option + Shift + P** shortcut.

Unity opens the focused Inspector in a new window.

To open focused Inspectors for multiple GameObjects and/or Assets:

  1. Select any combination of GameObjects in the Hierarchy view and Assets in the Project view.
  2. Do one of the following:
  3. Right-click one of the selected items, and from the context menu, select **Properties**.
  4. From the main menu, select **Assets > Properties**.
  5. Use the **Alt + P** / **Option + Shift + P** shortcut.

Unity opens a new window with a focused Inspector tab for each selected item.

The image below shows three selected items (left), two GameObjects and one
Asset, and the window you get when you open a focused Inspector for them
(right).

![](../uploads/Main/focused-inspector-multi.png)

### For components

To open a focused Inspector for one of a GameObject’s components:

  1. Inspect the GameObject and locate the component you want to open a focused Inspector for.
  2. From the component’s **More items** (**⋮**) menu, select **Properties**.

This is useful for frequently edited properties. For example you may want to
move a GameObject often, but leave the rest of its properties unchanged. In
that case, you can open its **Transform component** A Transform component
determines the Position, Rotation, and Scale of each object in the scene.
Every GameObject has a Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent).

The image below shows a **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) open in a regular Inspector (1), and
its Transform component open in a focused Inspector (2). Notice that the
focused Inspector’s tab header displays the name of the GameObject that the
component belongs to.

![](../uploads/Main/focused-inspector-component.png)

### For reference properties

When a GameObject has reference properties, you can open focused Inspectors
for the GameObjects or Assets they reference.

  1. Inspect the GameObject and locate the property whose reference you want to open in a focused Inspector.
  2. Right-click the reference field and select **Properties** from the context menu.

### For hover items

You can set up a shortcut to open a focused Inspector for whichever item in
the Hierarchy view or Project view that you hover the pointer over.

To assign a keyboard shortcut to the **PropertyEditor > OpenMouseOver**
command, use the [Shortcuts Manager](ShortcutsManager.html).

This is useful when you want to open a focused Inspector for an item without
affecting the current selection.

## Locate a focused Inspector’s source

To locate the item whose properties are displayed in a focused Inspector, do
one of the following:

  * From the focused Inspector’s **More Items** (**⋮**) menu, select **Ping**. Unity highlights the item in the Hierarchy view or the Project view.

![](../uploads/Main/focused-inspector-ping.png)

  * Hover the pointer over the focused Inspector’s tab header to display a tooltip that shows the full path to the item in the Scene Hierarchy or the Project.

![](../uploads/Main/focused-inspector-tooltip.png)

[](InspectorOptions.html)

Working in the Inspector

[](EditingValueProperties.html)

Editing properties

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

