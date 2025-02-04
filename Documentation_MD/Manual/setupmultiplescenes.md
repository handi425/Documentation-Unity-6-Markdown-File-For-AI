[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/setupmultiplescenes.html)
  * [中文](/cn/current/Manual/setupmultiplescenes.html)
  * [日本語](/ja/current/Manual/setupmultiplescenes.html)
  * [한국어](/kr/current/Manual/setupmultiplescenes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/setupmultiplescenes.html)
  * [中文](/cn/current/Manual/setupmultiplescenes.html)
  * [日本語](/ja/current/Manual/setupmultiplescenes.html)
  * [한국어](/kr/current/Manual/setupmultiplescenes.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * [Work with multiple scenes in Unity](MultiSceneEditing.html)
  * Set up multiple scenes

[](MultiSceneEditing.html)

Work with multiple scenes in Unity

[](bakemultiplescenes.html)

Bake data in multiple scenes

# Set up multiple scenes

You can add multiple scenes, edit how you view them, and change the **scene**
A Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) settings.

To create a new scene, see [Creating, loading, and saving Scenes](scenes-
working-with.html).

## Add scenes

To add a new scene to your project, do one of the following:

  * Right click to open the menu of a scene asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) and select **Open Scene
Additive**.

  * Drag one or more scenes from the Project window into the Hierarchy window.

## View scenes

The Hierarchy window displays all the scenes that are part of your project:

![The Hierarchy window with multiple scenes
added.](../uploads/Main/ViewScenes.png) The Hierarchy window with multiple
scenes added.

A: Scenes with unsaved changes have an asterisk by the scene name.  
B: The scene More menu allows you to perform actions on the scene.  
C: The scene divider (an inverted triangle) lets you collapse a scene and hide
its contents from the Hierarchy to better manage multiple scenes.

**Tip** : To add a scene to the Hierarchy window without loading it, press Alt
(macOS: press Option) and drag the scene into the Hierarchy window. This lets
you load the scene when it’s convenient for you.

## Loaded scene More menu (⋮)

You can interact with and edit a loaded scene in several ways.

![The More menu for a loaded scene.](../uploads/Main/LoadedMoreMenu.png) The More menu for a loaded scene. **Setting** | **Description**  
---|---  
**Set Active Scene** | Sets the scene as the target for new **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) created through **scripts** A
piece of code that allows you to create your own Components, trigger game
events, modify Component properties over time and respond to user input in any
way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). For more information, see
[SceneManager.SetActiveScene](https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.SetActiveScene.html#:~:text=The%20active%20Scene%20is%20the,kept%20as%20the%20active%20Scene.).  
**Save Scene** | Saves the scene that you selected.  
**Save Scene As** | Opens your file browser so you can choose where and how to save the scene.  
**Save All** | Saves all the scenes you have open in the Hierarchy window.  
**Unload Scene** | Hides the contents of the scene from the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) and the Hierarchy window. If you
have unsaved changes, save them before you unload the scene to not lose any
changes.  
**Remove Scene** | Removes the scene from the Hierarchy window.  
**Discard changes** | Undoes any changes that you haven’t saved.  
**Select Scene Asset** | Highlights the scene asset in the Project window.  
**Add New Scene** | Adds a new untitled scene below the scene you have selected.  
**GameObject** | Opens a dropdown menu of GameObjects that you can add to the scene you have selected.  
  
## Unloaded scene More menu (⋮)

You can interact with and edit an unloaded scene in fewer ways than you can a
loaded scene.

![The More menu for an unloaded scene.](../uploads/Main/UnloadedMoreMenu.png) The More menu for an unloaded scene. **Setting** | **Description**  
---|---  
**Load Scene** | Displays the contents of the scene in the Hierarchy window and the Scene view, and allows you to edit them.  
**Remove Scene** | Removes the scene from the Hierarchy window.  
**Select Scene Asset** | Highlights the scene asset in the Project window.  
**Add New Scene** | Adds a new untitled scene below the scene you have selected.  
  
## Multiple scenes in Play mode

When you are in Play mode and have multiple scenes in the Hierarchy window,
the Editor displays an additional scene called
[DontDestroyOnLoad](https://docs.unity3d.com/ScriptReference/Object.DontDestroyOnLoad.html).

## Scene-specific settings

The following settings are specific to each scene:

  * [RenderSettings](https://docs.unity3d.com/ScriptReference/RenderSettings.html) and [LightmapSettings](https://docs.unity3d.com/2022.2/Documentation/ScriptReference/LightmapSettings.html) (both found in the Lighting window).
  * Scene settings in the [Occlusion Culling](OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) window.

Each scene manages its own settings, so only settings associated with that
scene save to the scene file.

To change the settings of a specific scene, either open that specific scene
and change the settings, or set the scene as the active scene then change the
settings. Otherwise, if you have multiple scenes open, Unity uses the
rendering settings from the active scene.

When you switch to a new active scene in the Editor or at runtime, Unity
replaces all previous settings with the settings from the new active scene.

## Additional resources

  * [Creating, loading, and saving Scenes](scenes-working-with.html)
  * [Bake data in multiple scenes](bakemultiplescenes.html)
  * [Use scripts to edit multiple scenes](scriptmultiplescenes.html)

[](MultiSceneEditing.html)

Work with multiple scenes in Unity

[](bakemultiplescenes.html)

Bake data in multiple scenes

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

