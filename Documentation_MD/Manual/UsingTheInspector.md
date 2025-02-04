[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UsingTheInspector.html)
  * [中文](/cn/current/Manual/UsingTheInspector.html)
  * [日本語](/ja/current/Manual/UsingTheInspector.html)
  * [한국어](/kr/current/Manual/UsingTheInspector.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UsingTheInspector.html)
  * [中文](/cn/current/Manual/UsingTheInspector.html)
  * [日本語](/ja/current/Manual/UsingTheInspector.html)
  * [한국어](/kr/current/Manual/UsingTheInspector.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * The Inspector window

[](Hierarchy.html)

The Hierarchy window

[](InspectorOptions.html)

Working in the Inspector

# The Inspector window

Use the **Inspector** window to [view and edit
properties](EditingValueProperties.html) and settings for almost everything in
the Unity Editor, including **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), Unity components, Assets,
Materials, and in-Editor settings and preferences.

![The Inspector window docked in the Unity
Editor](../uploads/Main/InspectorWindowCallout.jpg) The Inspector window
docked in the Unity Editor

## Open an Inspector window

To open an Inspector window, do one of the following:

  * From the menu, select **Windows > General > Inspector** to open a floating Inspector window.
  * From any window’s More Items menu (⋮), select **Add Tab > Inspector** to open an Inspector in a new tab.

You can open as many Inspector windows as you want, and [reposition, dock, and
resize](CustomizingYourWorkspace.html) them in the same way you can any other
window.

## Control Inspector window focus

By default, an Inspector window displays properties for the current selection.
The contents of the Inspector change whenever the selection changes. To keep
the same set of properties open, regardless of the current selection, do one
of the following:

  * [Lock the Inspector](InspectorOptions.html#locking-the-inspector) window to the current selection. When you lock an Inspector window, it no longer updates if you change the selection.
  * Open a [focused Inspector](InspectorFocused.html) for a GameObject, Asset, or component. Focused Inspectors only ever display the properties of the items you opened them for.

## Inspect items

What you can see and edit in an Inspector window depends on what you select.
This section describes what an Inspector window displays for different types
of items you can select.

### Inspecting GameObjects

When you select a GameObject (for example, in the [Hierarchy](Hierarchy.html)
or [Scene view](UsingTheSceneView.html)An interactive view into the world you
are creating. You use the Scene View to select and position scenery,
characters, cameras, lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView)), the Inspector displays the
properties of all of its components and Materials. You can [edit the
properties](EditingValueProperties.html), and [reorder the
components](InspectorOptions.html#reordering-components) in the Inspector
window.

### Inspect custom script components

When GameObjects have custom script components attached, the Inspector
displays the **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts)’ public variables. You can edit
script variables in the same way as you edit any other properties, which means
that you can set parameters and default values in your scripts without
modifying the code.

For more information, see [Variables and the Inspector](inspecting-
scripts.html) in the [Scripting section](scripting.html).

### Inspect Assets

When you select an [Asset](AssetWorkflow.html)Any media or data that can be
used in your game or project. An asset may come from a file created outside of
Unity, such as a 3D Model, an audio file or an image. You can also create some
asset types in Unity, such as an Animator Controller, an Audio Mixer or a
Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) (for example, from the [Project
window](ProjectView.html)A window that shows the contents of your `Assets`
folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow)), the Inspector displays
settings that control how Unity imports and uses the Asset at runtime.

Each type of Asset has its own settings. Examples of Asset import settings
that you edit in an Inspector window include the:

  * [Model Import Settings](class-FBXImporter.html) window.
  * [Audio Clip Import Settings](class-AudioClip.html) window.
  * [Texture Import Settings](class-TextureImporter.html) window.

### Inspect settings and preferences

When you open the [Project Settings](comp-ManagerGroup.html)A broad collection
of settings which allow you to configure how Physics, Audio, Networking,
Graphics, Input and many other areas of your project behave. [More info](comp-
ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) (menu: **Edit** > **Project
Settings**), Unity displays them in an Inspector window.

### Inspect Prefabs

When you work with Prefabs, the Inspector window displays some additional
information and provides some additional options. For example:

  * When you [Edit a Prefab Instance](EditingPrefabViaInstance.html), the Inspector window provides options for working with the Prefab Asset and applying overrides.
  * When you apply [Instance overrides](PrefabInstanceOverrides.html), the Inspector window displays the names of properties you override in bold.

For more information about working with Prefabs in the Inspector window, see
the [Prefabs](Prefabs.html)An asset type that allows you to store a GameObject
complete with components and properties. The prefab acts as a template from
which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) section.

## Inspect multiple Items

When you have two or more items selected, you can edit all of the properties
they have in common in an Inspector window. Unity copies the values you supply
to all the selected items. The Inspector window displays a count of the number
of selected items.

### Multiple GameObjects

When you select multiple GameObjects, the Inspector window displays all of the
components they have in common.

  * For property values that are different across two or more selected GameObjects, the Inspector displays a dash (**-**) (1 in the screenshot below).
  * For property values that are the same across all selected GameObjects, the Inspector displays the actual values (2 in the screenshot below).
  * To apply a property value from one selected GameObject to all of the selected GameObjects, right-click the property name and select **Set to Value of _[Name of GameObject]_** from the context menu (3 in the screenshot below).
  * If any of the selected GameObjects has components that are not present on the other selected objects, the Inspector displays a message that some components are hidden.

![Inspector showing multiple selected
GameObjects](../uploads/Main/MultiObjectEdit.png) Inspector showing multiple
selected GameObjects

### Multiple Assets

When you select multiple Assets of the same type, the Inspector window
displays all of the properties they have in common.

  * For property values that are the same across all selected Assets, the Inspector displays the actual values.
  * For property values that are different across two or more selected Assets, the Inspector displays a dash (**-**) (1 in the screenshot below).
  * For properties that you cannot edit for all of the selected Assets at once, the Inspector grays them out (2 in the screenshot below).

![Inspector showing multiple selected Assets of the same
type](../uploads/Main/MultiAssetEdit-Same.png) Inspector showing multiple
selected Assets of the same type

When you select multiple Assets of different types, the Inspector displays a
list that shows how many of each type of Asset are selected. Click any item in
the list to Inspect all Assets of that type.

![Inspector showing multiple selected Assets of different
types](../uploads/Main/MultiAssetEdit-Diff.png) Inspector showing multiple
selected Assets of different types

### Multiple Prefabs

You can inspect multiple selected instances of a Prefab in the same way as you
edit multiple GameObjects, but the Inspector hides the **Select** , **Revert**
, and **Apply** buttons (see [Editing a Prefab via its
instances](EditingPrefabViaInstance.html)).

## Locate an Inspector window’s source

When you open a GameObject or Asset in an Inspector window, you can locate it
in the **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view or Project View using the **Ping**
command.

From the Inspector window’s **More Items** (**⋮**) menu, select **Ping**.
Unity highlights the item in the Hierarchy view or the Project view.

![The ping command highlights the item currently displayed in the
Inspector](../uploads/Main/inspector-ping.png) The ping command highlights the
item currently displayed in the Inspector

* * *

  * Component drag and drop added in Unity 5.6
  * Reorganized Inspector section pages in Unity 2020.1

[](Hierarchy.html)

The Hierarchy window

[](InspectorOptions.html)

Working in the Inspector

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

