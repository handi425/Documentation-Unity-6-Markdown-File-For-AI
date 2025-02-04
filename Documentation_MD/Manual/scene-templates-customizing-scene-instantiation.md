[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/scene-templates-customizing-scene-instantiation.html)
  * [中文](/cn/current/Manual/scene-templates-customizing-scene-instantiation.html)
  * [日本語](/ja/current/Manual/scene-templates-customizing-scene-instantiation.html)
  * [한국어](/kr/current/Manual/scene-templates-customizing-scene-instantiation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/scene-templates-customizing-scene-instantiation.html)
  * [中文](/cn/current/Manual/scene-templates-customizing-scene-instantiation.html)
  * [日本語](/ja/current/Manual/scene-templates-customizing-scene-instantiation.html)
  * [한국어](/kr/current/Manual/scene-templates-customizing-scene-instantiation.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * [Scene Templates](scene-templates.html)
  * Customizing new scene creation

[](scene-templates-editing.html)

Editing scene templates

[](scene-templates-settings.html)

Scene template settings

# Customizing new scene creation

To run custom code when Unity instantiates a new **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) from a template, create a Scene
Template Pipeline script and connect it to the template. Each time you create
a new scene from the template, Unity creates a new instance of the pipeline
script as well.

To connect the script to a template:

  1. Inspect the template to [edit its properties](scene-templates-editing.html).
  2. Set the **Scene Template Pipeline** property to point to your Scene Template Pipeline script.

You can also use the
[`SceneTemplateAsset.templatePipeline`](../ScriptReference/SceneTemplate.SceneTemplateAsset-
templatePipeline.html) method to connect the script to the template via C#.

A Scene Template Pipeline script must derive from the
[`ISceneTemplatePipeline`] interface or [`SceneTemplatePipelineAdapter`]. It
should implement the events you want to react to; for example,
`BeforeTemplateInstantiation` or `AfterTemplateInstantiation` in the code
below.

**Example:**

    
    
    using UnityEditor.SceneTemplate;
    using UnityEngine;
    using UnityEngine.SceneManagement;
    public class DummySceneTemplatePipeline : ISceneTemplatePipeline
    {
        public void BeforeTemplateInstantiation(SceneTemplateAsset sceneTemplateAsset, bool isAdditive, string sceneName)
        {
            if (sceneTemplateAsset)
            {
                Debug.Log($"Before Template Pipeline {sceneTemplateAsset.name} isAdditive: {isAdditive} sceneName: {sceneName}");
            }
        }
    
        public void AfterTemplateInstantiation(SceneTemplateAsset sceneTemplateAsset, Scene scene, bool isAdditive, string sceneName)
        {
            if (sceneTemplateAsset)
            {
                Debug.Log($"After Template Pipeline {sceneTemplateAsset.name} scene: {scene} isAdditive: {isAdditive} sceneName: {sceneName}");
            }
        }
    }
    

## Scene Template instantiation sequence

When you create a new scene from a template with cloneable dependencies, Unity
performs several file operations. Most of these operations trigger Unity
events that you can listen for, and react to, in **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

The instantiation sequence is as follows:

  1. You click **Create** in the [New Scene dialog](CreatingScenes.html#new-scene-dialog). Unity calls the: 
     * Scene template asset.
     * Template Scene. This is the Unity Scene associated with the template.
     * New Scene. This is a new instance of the template Scene.
  2. Unity triggers the `ISceneTemplatePipeline.BeforeTemplateInstantiation` event for the template asset, and binds the asset to a `ISceneTemplatePipeline` script that it triggers.

  3. Unity triggers the [`SceneTemplate.NewTemplateInstantiating`](../ScriptReference/SceneTemplate.SceneTemplateService-newSceneTemplateInstantiating.html) event.

  4. Unity creates a new scene that is a copy of the template scene.

  5. Unity creates a folder with the same name as the new scene, and copies all cloneable dependencies into that folder.

  6. Unity opens the new scene in memory, and triggers the following events: 
     * [`EditorSceneManager.sceneOpening`](../ScriptReference/SceneManagement.EditorSceneManager-sceneOpening.html)
     * [`MonoBehavior.OnValidate`](../ScriptReference/MonoBehaviour.OnValidate.html) (on all GameObjects that implement it)
     * [`EditorSceneManager.sceneOpened`](../ScriptReference/SceneManagement.EditorSceneManager-sceneOpened.html)
  7. Unity remaps references to all cloneable assets, so the new scene points to the clones.

  8. Unity saves the new scene, and triggers the following events: 
     * [`EditorSceneManager.sceneSaving`](../ScriptReference/SceneManagement.EditorSceneManager-sceneSaving.html)
     * [`EditorSceneManager.sceneSaved`](../ScriptReference/SceneManagement.EditorSceneManager-sceneSaved.html)
  9. Unity triggers the `ISceneTemplatePipeline.AfterTemplateInstantiation` for the template asset, and binds the asset to a `ISceneTemplatePipeline` script that it triggers.

  10. Unity triggers the [`SceneTemplate.NewTemplateInstantiated`](../ScriptReference/SceneTemplate.SceneTemplateService-newSceneTemplateInstantiated.html) event.

* * *

[](scene-templates-editing.html)

Editing scene templates

[](scene-templates-settings.html)

Scene template settings

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

