[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/scriptmultiplescenes.html)
  * [中文](/cn/current/Manual/scriptmultiplescenes.html)
  * [日本語](/ja/current/Manual/scriptmultiplescenes.html)
  * [한국어](/kr/current/Manual/scriptmultiplescenes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/scriptmultiplescenes.html)
  * [中文](/cn/current/Manual/scriptmultiplescenes.html)
  * [日本語](/ja/current/Manual/scriptmultiplescenes.html)
  * [한국어](/kr/current/Manual/scriptmultiplescenes.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * [Work with multiple scenes in Unity](MultiSceneEditing.html)
  * Use scripts to edit multiple scenes

[](bakemultiplescenes.html)

Bake data in multiple scenes

[](scene-templates.html)

Scene Templates

## Use scripts to edit multiple scenes

You can edit multiple **scenes** A Scene contains the environments and menus
of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) using **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) within the Editor or at runtime.

## Use scripts within the Editor

When using (or running) scripts within the Editor, use:

  * [Scene struct](https://docs.unity3d.com/ScriptReference/SceneManagement.Scene.html): Available both in the Editor and at runtime, Scene struct contains read-only properties that relate to the scene itself, such as name and asset path.
  * [EditorSceneManager](https://docs.unity3d.com/ScriptReference/SceneManagement.EditorSceneManager.html) API: This class is only available only in the Editor and has several functions to implement all the Multi-Scene editing features described in the pages [Setup multiple scenes](setupmultiplescenes.html) and [Bake data in multiple scenes](bakemultiplescenes.html).
  * SceneSetup utility class: A utility class that you can use to store information about a scene that is in the Hierarchy window.

## Use runtime scripts

When using scripts at runtime to edit multiple scenes, use the functions in
the
[SceneManager](https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.html)
class such as `LoadScene` and `UnloadScene`.

**Tips** :

  * To instantiate a [prefab](Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) in a scene, use
[PrefabUtility.InstantiatePrefab](https://docs.unity3d.com/2022.2/Documentation/ScriptReference/PrefabUtility.InstantiatePrefab.html).

  * To move objects to the root of a scene, use [Undo.MoveGameObjectToScene](https://docs.unity3d.com/2022.2/Documentation/ScriptReference/Undo.MoveGameObjectToScene.html).
  * To avoid having to setup your Hierarchy window every time you restart the Editor, or to store different setups, use [EditorSceneManager.GetSceneManagerSetup](https://docs.unity3d.com/2022.2/Documentation/ScriptReference/SceneManagement.EditorSceneManager.GetSceneManagerSetup.html), which also gets a list of SceneSetup objects that describes the current setup. You can serialize the objects into a `ScriptableObject` along with any other information you want to store about your scene setup. To restore your Hierarchy window, recreate the list of `SceneSetups` and use [EditorSceneManager.RestoreSceneManagerSetup](https://docs.unity3d.com/2022.2/Documentation/ScriptReference/SceneManagement.EditorSceneManager.RestoreSceneManagerSetup.html).
  * To get a list of your loaded scenes at runtime, get the `sceneCount` and iterate over the scenes with [`GetSceneAt`](https://docs.unity3d.com/2022.2/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneAt.html).

[](bakemultiplescenes.html)

Bake data in multiple scenes

[](scene-templates.html)

Scene Templates

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

