[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SelectGameObjects.html)
  * [中文](/cn/current/Manual/SelectGameObjects.html)
  * [日本語](/ja/current/Manual/SelectGameObjects.html)
  * [한국어](/kr/current/Manual/SelectGameObjects.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SelectGameObjects.html)
  * [中文](/cn/current/Manual/SelectGameObjects.html)
  * [日本語](/ja/current/Manual/SelectGameObjects.html)
  * [한국어](/kr/current/Manual/SelectGameObjects.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * [The Scene view](UsingTheSceneView.html)
  * [Pick and select GameObjects in the Scene view](ScenePicking.html)
  * Select GameObjects

[](ScenePicking.html)

Pick and select GameObjects in the Scene view

[](SelectionPiercingMenu.html)

Select a GameObject that overlaps with other GameObjects

# Select GameObjects

You can select a single **GameObject** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the [Scene
view](UsingTheSceneView.html)An interactive view into the world you are
creating. You use the Scene View to select and position scenery, characters,
cameras, lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) or from the [Hierarchy
window](Hierarchy.html). You can also select more than one GameObject at a
time.

The Editor highlights selected GameObjects and their children in the Scene
view. By default, the selection outline color is orange, and the child outline
color is blue. You can also choose to highlight selected the wireframes of
selected GameObjects in a different color. You can change all of these outline
highlight colors from the [Preferences window](Preferences.html). To open the
**Preferences** window, go to **Edit > Preferences** (macOS: **Unity >
Settings**) in the main menu.

If you are working with a large **Scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that contains a lot of Scene items,
such as GameObjects, **Terrain** The landscape in your scene. A Terrain
GameObject adds a large flat plane to your scene and you can use the Terrain’s
Inspector window to create a detailed landscape. [More info](terrain-
UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) objects, **Cameras** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), and Lights, selecting multiple
objects can be difficult. To help you select only the items you want, use the
Scene picking controls to block some objects from being picked or use the
[selection piercing menu](SelectionPiercingMenu.html).

For more information about the outline and wireframe selection visualizations,
refer to [Gizmos menu](GizmosMenu.html).

To select a single GameObject:

  * Click on it in the [Scene view](UsingTheSceneView.html). If you repeatedly click on the shared space between overlapping GameObjects, the selection cycles between them. You can also use the [selection piercing menu](SelectionPiercingMenu.html) to select a specific GameObject when multiple GameObjects are in the same location.
  * Click on the name of the GameObject in the [Hierarchy window](Hierarchy.html).

To select or deselect multiple GameObjects:

  * Drag a rectangle around multiple GameObjects to selects anything that is inside this bounding box.
  * Hold the **Shift** key and select GameObjects in the Scene. You can also use hold **Ctrl** (macOS: **Command**) and select a GameObject to add or remove GameObjects from the selection.

**Note:** When a feature in the Editor needs a single selected GameObject to
perform an action, it looks for an “active” object. For example, when the
Editor has to decide which GameObject to use as the pivot for transform tools
while in Pivot mode. By default, Unity considers the last GameObject you
select to be the “active” object. When you hold **Shift** and select one of
several selected GameObjects, you change which one of them is active. If a
GameObject is active in the Scene view, Unity doesn’t display any visible cues
that it’s active. However, you can see which GameObject is active in the Scene
view when you repeatedly hold **Shift** and click in [Pivot
mode](PositioningGameObjects.html#GizmoHandlePositions) with multiple objects
selected.

## Additional resources

  * [Pick and select GameObjects](ScenePicking.html)
  * [Hierarchy window](Hierarchy.html)
  * [Select a GameObject that overlaps with other GameObjects](SelectionPiercingMenu.html)**
  * [Gizmos menu](GizmosMenu.html)]

[](ScenePicking.html)

Pick and select GameObjects in the Scene view

[](SelectionPiercingMenu.html)

Select a GameObject that overlaps with other GameObjects

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

