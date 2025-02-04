[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LoadingResourcesatRuntime.html)
  * [中文](/cn/current/Manual/LoadingResourcesatRuntime.html)
  * [日本語](/ja/current/Manual/LoadingResourcesatRuntime.html)
  * [한국어](/kr/current/Manual/LoadingResourcesatRuntime.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LoadingResourcesatRuntime.html)
  * [中文](/cn/current/Manual/LoadingResourcesatRuntime.html)
  * [日本語](/ja/current/Manual/LoadingResourcesatRuntime.html)
  * [한국어](/kr/current/Manual/LoadingResourcesatRuntime.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Scripting with Assets](ScriptingAssets.html)
  * Loading Resources at Runtime

[](ScriptingAssets.html)

Scripting with Assets

[](StreamingAssets.html)

Streaming Assets

# Loading Resources at Runtime

In some situations, it is useful to make an asset available to a project
without loading it in as part of a **scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). For example, there may be a character
or other object that can appear in any scene of the game but which will only
be used infrequently (this might be a “secret” feature, an error message or a
highscore alert, say). Furthermore, you may even want to load assets from a
separate file or URL to reduce initial download time or allow for
interchangeable game content.

You can use **Resource Folders** in your project to include content in your
player build, which will make it available to load when needed, independently
of the scenes that you build.

## Resource Folders

Resource Folders contain collections of assets that are included in the built
Unity player even when they are not directly referenced from any Scene
included the Build.

To put assets into a Resource Folder, create a new folder in the **Project
window** A window that shows the contents of your `Assets` folder (Project
tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), and name the folder
“Resources”. You can have multiple Resource Folders located at different
subfolders within your Assets folder, and packages may also contain Resources
folders. You can then place assets into that folder in the same way as any
other folder in the Project window. Whenever you want to load an asset from
one of these folders, call
[Resources.Load()](../ScriptReference/Resources.Load.html).

**Note:** All assets found in the Resources folders and their dependencies are
stored in a file in the build output called _resources.assets_. If a scene in
the build references an asset then that asset is serialized into a
_sharedAssets*.assets_ file instead.

Only assets that are in the _Resources folder_ can be accessed through
[Resources.Load()](../ScriptReference/Resources.Load.html). However many more
assets might end up in the _resources.assets_ file since they are
dependencies. For example a Material in the Resources folder might reference a
Texture outside of the Resources folder. In that case the Texture is also
included in the resources.assets file, but it is not available to load
directly.

## Resource Unloading

If you want to destroy scene objects that were loaded using
[Resources.Load()](../ScriptReference/Resources.Load.html) prior to loading
another scene, call [Object.Destroy()](../ScriptReference/Object.Destroy.html)
on them. To release assets and reclaim memory, use
[Resources.UnloadUnusedAssets()](../ScriptReference/Resources.UnloadUnusedAssets.html).

## Limitations and Alternatives

The Resources system is convenient to use, especially for rapid prototyping
and small projects. But it does not scale well and overall use of this feature
is discouraged. For this reason [AssetBundles](AssetBundlesIntro.html) and the
Addressables package are the recommended alternative.

Some downsides of using Resources:

  * Placing a lot of content in this folder will slow down application startup and the length of builds.
  * The Resource folder is not appropriate for delivering custom content for specific platforms.
  * Making changes to Assets in the Resource folder requires a player rebuild and redeployment, whereas AssetBundles are better suited for incremental content updates.

The resources folder can be appropriate for small Assets that are required
throughout the project’s lifetime, that do not require updates, and do not
vary across platforms or devices. Resource assets might be part of the minimal
bootstrapping for a game, with the main content downloaded on-demand with
AssetBundles. But local AssetBundles located in the **StreamingAssets** folder
could also serve that bootstrapping need.

[](ScriptingAssets.html)

Scripting with Assets

[](StreamingAssets.html)

Streaming Assets

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

