[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SpecialFolders.html)
  * [中文](/cn/current/Manual/SpecialFolders.html)
  * [日本語](/ja/current/Manual/SpecialFolders.html)
  * [한국어](/kr/current/Manual/SpecialFolders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SpecialFolders.html)
  * [中文](/cn/current/Manual/SpecialFolders.html)
  * [日本語](/ja/current/Manual/SpecialFolders.html)
  * [한국어](/kr/current/Manual/SpecialFolders.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * Reserved folder name reference

[](AssetDatabaseBatching.html)

Batching with the AssetDatabase

[](ImportActivityWindow.html)

Import Activity window

# Reserved folder name reference

Every Unity project has an `Assets` folder in the project root which contains
the project’s [assets](AssetWorkflow.html)Any media or data that can be used
in your game or project. An asset may come from a file created outside of
Unity, such as a 3D Model, an audio file or an image. You can also create some
asset types in Unity, such as an Animator Controller, an Audio Mixer or a
Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset). The [Project
window](ProjectView.html)A window that shows the contents of your `Assets`
folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) displays the contents of the
`Assets` folder.

Some limitations apply when choosing names for new folders. There are some
names for subfolders of the `Assets` folder that Unity reserves for certain
subtypes of assets, and which have special compilation significance or are
used to categorize assets for the Editor or Player. These folder names and
their meaning are detailed in the following table.

Folder name | Description  
---|---  
`Editor` | Reserved for Editor scripts, which add functionality to the Unity Editor at authoring time but aren’t available in Player builds at runtime. An alternative to placing scripts in a folder called `Editor` is to [create an assembly definition asset](assembly-definitions-creating.html) for Editor code. The exact location of an `Editor` folder determines the script compilation order of its contents. For more information, refer to [Special folders and script compilation order](script-compile-order-folders.html).  
**Maximum number of folders with this name per project:** Unlimited  
**Valid location for folder** : Root of the `Assets` folder or any of its
subfolders.  
**Place relevant assets in** : `Editor` folder or any of its subfolders.  
  
**Note:** MonoBehaviour scripts in an `Editor` folder can’t be attached to
GameObjects as components.  
`Editor Default Resources` | Reserved for asset files that Editor scripts can load on-demand using [EditorGUIUtility.Load](../ScriptReference/EditorGUIUtility.Load.html).  
**Maximum number of folders with this name per project:** 1  
**Valid location for folder** : Root of the `Assets` folder only.  
**Place relevant assets in** : `Editor Default Resources` folder or any of its
subfolders.  
  
**Note** : Always include the subfolder path in the path passed to
[EditorGUIUtility.Load](../ScriptReference/EditorGUIUtility.Load.html) if your
asset files are in subfolders.  
`Gizmos` | Reserved for image files used by the [Gizmos.DrawIcon](../ScriptReference/Gizmos.DrawIcon.html) function to draw icons in a **Scene** view. For more information, refer to [Gizmos and Handles](gizmos-and-handles.html).  
**Maximum number of folders with this name per project:** 1  
**Valid location for folder** : Root of the `Assets` folder only.  
**Place relevant assets in** : `Gizmos` folder or any of its subfolders.  
  
**Note** : Always include the subfolder path in the path passed to the
[Gizmos.DrawIcon](../ScriptReference/Gizmos.DrawIcon.html) function if your
asset files are in subfolders.  
`Resources` | Reserved for assets to load on-demand from a script at application runtime rather than creating references to assets in a scene. For more information, refer to [Loading Resources at Runtime](LoadingResourcesatRuntime.html).  
**Maximum number of folders with this name per project:** Unlimited  
**Valid location for folder** : Root of the `Assets` folder or any of its
subfolders.  
**Place relevant assets in** : `Resources` folder or any of its subfolders.  
  
**Note** : Always include the subfolder path in the path passed to the
[Resources.Load](../ScriptReference/Resources.Load.html) function if your
asset files are in subfolders. Assets in a `Resources` folder increase the
size of Player builds and assets not required at runtime must be manually
cleaned up to prevent them degrading your application’s performance. For more
information, refer to [The Resources
folder](UnderstandingPerformanceResourcesFolder.html). If the `Resources`
folder is an `Editor` subfolder, the assets in it are loadable from Editor
scripts but are removed from Player builds, so use the
[EditorGUIUtility.Load](../ScriptReference/EditorGUIUtility.Load.html) to load
them instead.  
`Plugins` | Reserved for third-party plugins. For platform-specific information on valid folder path patterns, refer to [Import and configure plug-ins](plug-in-inspector.html).  
`StreamingAssets` | Reserved for asset files that should be available in their original format at runtime for streaming. For more information, refer to [Streaming Assets](StreamingAssets.html).  
**Maximum number of folders with this name per project:** 1  
**Valid location for folder** : Root of the `Assets` folder only.  
**Place relevant assets in** : `SteamingAssets` folder or any of its
subfolders.  
  
## Platform-specific folders

For information on folder name formats and extensions which denote **plug-
ins** A set of code created outside of Unity that creates functionality in
Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins
(managed .NET assemblies created with tools like Visual Studio) and Native
plug-ins (platform-specific native code libraries). [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Plug-in) or asset types specific to particular
platforms, refer to [Platform development](PlatformSpecific.html).

## Hidden assets

During the [import](ImportingAssets.html) process, Unity ignores the following
files and folders in the `Assets` folder and its subfolders:

  * Hidden folders.
  * Files and folders which start with `.`, except for those under `StreamingAssets` where this pattern is not ignored.
  * Files and folders which end with `~`.
  * Files and folders named `cvs`.
  * Files with the extension `.tmp`.

This prevents importing special and temporary files created by the operating
system or other applications.

**Note** : For folders created through the Editor’s create menu, the Editor
automatically converts a dot (`.`) prefix into an underscore (`_`) prefix to
prevent crashes. For example, a folder created in the Editor and named
`.folder` is automatically renamed `_folder`. If you want to name a folder
with a dot prefix, create it directly in your local file system instead.

## Additional resources

  * [Script compilation order](script-compile-order-folders.html)

[](AssetDatabaseBatching.html)

Batching with the AssetDatabase

[](ImportActivityWindow.html)

Import Activity window

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

