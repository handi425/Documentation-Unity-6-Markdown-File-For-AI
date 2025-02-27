[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/occlusion-culling-scene-loading.html)
  * [中文](/cn/current/Manual/occlusion-culling-scene-loading.html)
  * [日本語](/ja/current/Manual/occlusion-culling-scene-loading.html)
  * [한국어](/kr/current/Manual/occlusion-culling-scene-loading.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/occlusion-culling-scene-loading.html)
  * [中文](/cn/current/Manual/occlusion-culling-scene-loading.html)
  * [日本語](/ja/current/Manual/occlusion-culling-scene-loading.html)
  * [한국어](/kr/current/Manual/occlusion-culling-scene-loading.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Excluding hidden objects with occlusion culling](OcclusionCulling-landing.html)
  * Set up multiple scenes for occlusion culling

[](occlusion-culling-getting-started.html)

Set up a scene for occlusion culling

[](occlusion-culling-dynamic-gameobjects.html)

Cull moving GameObjects

# Set up multiple scenes for occlusion culling

At runtime, Unity loads only one **occlusion culling** A process that disables
rendering GameObjects that are hidden (occluded) from the view of the camera.
[More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) data asset at a time, no
matter how many Scenes are open. You must therefore prepare your occlusion
culling data differently depending on whether you plan to load one **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) at a time, or multiple Scenes at a
time.

## Loading one Scene at a time

If you load one Scene at a time with
[LoadSceneMode.Single](../ScriptReference/SceneManagement.LoadSceneMode.Single.html),
you must bake the occlusion culling data for each Scene separately, like this:

  1. In the Unity Editor, open a single Scene that you want to bake occlusion culling data for.
  2. Bake the data for the Scene. Unity generates the data and saves it as _Assets/[Scene name]/OcclusionCullingData.asset_. Unity adds a reference to this asset to the open Scene.
  3. Save the Scene.
  4. Repeat steps 1, 2, and 3 for each Scene.

At runtime, load your Scenes like this:

  1. Load a Scene as the default Scene of your Project, or using LoadSceneMode.Single. Unity unloads the active Scene if there is one, along with its occlusion data asset if it has one. Unity then loads your Scene along with its occlusion data asset.

## Loading more than one Scene at a time

If you load multiple Scenes at a time with
[LoadSceneMode.Additive](../ScriptReference/SceneManagement.LoadSceneMode.Additive.html),
you must bake the data for those Scenes together, like this:

  1. In the Unity Editor, open the first Scene of the group that Unity will load at runtime. This becomes the active Scene.
  2. Additively open the other Scenes in the group, so that all of them are open in the Unity Editor at the same time.
  3. Bake the data for all Scenes. Unity generates the data for all of the open Scenes, and saves it as _Assets/[active Scene name]/OcclusionCullingData.asset_. Unity adds a reference to this asset to all of the open Scenes.
  4. Save the Scenes.

At runtime, load your Scenes like this:

  1. Load the first Scene of the group as the default Scene of your Project, or using `LoadSceneMode.Single`. Unity unloads the active Scene if there is one, along with its occlusion data asset if it has one. Unity then loads your Scene along with the shared occlusion data asset.
  2. Load other Scenes as required with `LoadSceneMode.Additive`. If Unity finds that the the occlusion data of an additively loaded Scene is the same as that of the active Scene, occlusion culling works as intended.

Note that the shared occlusion data asset has a larger file size. There is no
additional runtime CPU impact to using a larger occlusion data asset.

For further information on working with multiple Scenes in the Unity Editor,
see the documentation on [multi-Scene editing](MultiSceneEditing.html).

[](occlusion-culling-getting-started.html)

Set up a scene for occlusion culling

[](occlusion-culling-dynamic-gameobjects.html)

Cull moving GameObjects

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

