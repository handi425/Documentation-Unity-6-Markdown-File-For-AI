[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UsingCustomEditorTools.html)
  * [中文](/cn/current/Manual/UsingCustomEditorTools.html)
  * [日本語](/ja/current/Manual/UsingCustomEditorTools.html)
  * [한국어](/kr/current/Manual/UsingCustomEditorTools.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UsingCustomEditorTools.html)
  * [中文](/cn/current/Manual/UsingCustomEditorTools.html)
  * [日本語](/ja/current/Manual/UsingCustomEditorTools.html)
  * [한국어](/kr/current/Manual/UsingCustomEditorTools.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * [The Scene view](UsingTheSceneView.html)
  * Custom Editor tools

[](SceneViewContextMenu.html)

Scene view context menu

[](GameView.html)

The Game view

# Custom Editor tools

You can create Editor tools with the [EditorTool
API](../ScriptReference/EditorTools.EditorTool.html).

An Editor tool’s context determines what that tool affects in the Editor.
Tools can be either global tools or component tools.

Access Editor tools in the [Scene view](UsingTheSceneView.html)An interactive
view into the world you are creating. You use the Scene View to select and
position scenery, characters, cameras, lights, and all other types of Game
Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) from these
[overlays](overlays.html):

  * The Tools overlay
  * The Tools Settings overlay

## Tool context

The [`EditorToolContext
API`](../ScriptReference/EditorTools.EditorToolContext.html) changes what the
Editor’s [built-in Transform tools](PositioningGameObjects.html) affect.

The default tool context is
[GameObject](../ScriptReference/EditorTools.GameObjectToolContext.html)The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). A tool with the
[GameObject](../ScriptReference/EditorTools.GameObjectToolContext.html) tool
context affects the [Transform](class-Transform.html) values of a GameObject.
Other contexts can affect different elements. For example, the [Spline tool
context](https://docs.unity3d.com/Packages/com.unity.splines@latest/) makes it
so the **Move** , **Rotate** , and **Scale** tools affect Spline knots and
tangents.

If your project contains multiple tool contexts, you can use the first button
in the Tools overlay to select a tool context. If the tool context button
isn’t selected, then the default GameObject tool context is active. The tool
context button isn’t available from the Tools overlay if there are no extra
tool contexts in your project.

## Global tools vs. component tools

Tools you create with the [EditorTool
API](../ScriptReference/EditorTools.EditorTool.html) can either be global or
component tools.

### Global tools

A global tool affects any GameObject.

A global tool is always available regardless of the type of GameObject you
select. For example, you can always access a Transform tool because the
Transform tool works with any GameObject.

The Tools overlay displays global tools in the section after the built-in
Transform tools, such as **Move** , **Rotate** , **Scale** , and **Rect**.

### Component tools

A component tool affects a specific [component](Components.html)A functional
part of a GameObject. A GameObject can contain any number of components. Unity
has many built-in components, and you can create your own by writing scripts
that inherit from MonoBehaviour. [More info](UsingComponents.html)  
See in [Glossary](Glossary.html#component).

A component tool is only available when you select a GameObject with the
component the tool comes from attached to it. For example, you can only use a
custom manipulator tool for lights when you select a GameObject with a Light
component.

The last buttons in the Tools overlay are component tools. Component tools are
divided into groups based on their component. The availability of component
tools depends on what you have [actively selected](ScenePicking.html#select-
gameobjects) in the **Scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view or Hierarchy window.

## Additional resources

  * [Overlays](overlays.html)
  * [`EditorTool`](../ScriptReference/EditorTools.EditorTool.html)
  * [`EditorToolContext`](../ScriptReference/EditorTools.EditorToolContext.html)
  * [`GameObjectToolContext`](../ScriptReference/EditorTools.GameObjectToolContext.html)

[](SceneViewContextMenu.html)

Scene view context menu

[](GameView.html)

The Game view

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

