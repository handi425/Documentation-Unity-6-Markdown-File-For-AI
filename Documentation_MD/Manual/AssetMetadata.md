[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetMetadata.html)
  * [中文](/cn/current/Manual/AssetMetadata.html)
  * [日本語](/ja/current/Manual/AssetMetadata.html)
  * [한국어](/kr/current/Manual/AssetMetadata.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetMetadata.html)
  * [中文](/cn/current/Manual/AssetMetadata.html)
  * [日本語](/ja/current/Manual/AssetMetadata.html)
  * [한국어](/kr/current/Manual/AssetMetadata.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * Asset Metadata

[](class-TextAsset.html)

Text assets

[](AssetDatabase.html)

The Asset Database

# Asset Metadata

When Unity imports assets, it also stores and manages additional data about
the asset, such as what import settings Unity should use to import the asset,
and where the asset is used throughout your project. Below is a description of
how this process works:

  1. Unity assigns the asset a unique ID.
  2. Unity creates a `.meta` file to accompany the asset file.
  3. Unity [processes the asset](ImportingAssets.html#processing).

The [Import settings](ImportingAssets.html) for any given asset affects how
Unity processes the asset. If you modify the asset file, or any of the asset’s
import settings, Unity reimports the asset. For more information, see [Assets
and their import settings](ImportingAssets.html#importSettings).

## Unique IDs

The Unity Editor frequently checks the contents of the `Assets` folder against
the list of assets it already knows about. When you place an asset in the
`Assets` folder, Unity detects that you have added a new file.

When Unity finds the new file, it assigns a unique ID to the asset. This is an
ID that Unity uses internally to reference the asset, so that Unity can move
or rename the asset without breaking anything.

The IDs are not normally visible in the Editor,

## Meta files

The image below shows `.meta` files that Unity creates for each item in your
project’s `Assets` folder. Unity creates meta files for asset files and
folders.

These files are hidden in Unity’s **Project window** A window that shows the
contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), and might also be hidden in
your file system by default (see [Wikipedia: Hidden file and hidden
directory](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory)),
so you might not see them in Windows Explorer or Finder unless you make your
hidden files visible on your computer.

![The relationship between the Assets folder in your Unity project on your
computer, meta files, and the Project window in
Unity](../uploads/Main/AssetWorkflowFolderAndProjectWindow.png) The
relationship between the `Assets` folder in your Unity project on your
computer, meta files, and the Project window in Unity

This example demonstrates that Unity creates a `.meta` file for each asset or
folder inside the project’s `Assets` folder, because they appear in a system
file browser. However, these `.meta` files are not visible in the Project
window because they are hidden by default. To make them visible, open the
[Mode](class-VersionControlSettings.html) project setting and enable **Visible
Meta Files**.

When Unity creates a `.meta` file for an asset, it writes the asset’s ID
inside the `.meta` file and stores the `.meta` file in the same location as
the asset file.

The `.meta` files contain the unique ID assigned to the asset, and values for
all the [import settings](ImportingAssets.html#importSettings) you see in the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window when you select an asset in
your Project window. For example, for a [Texture](class-
TextureImporter.html)An image used when rendering a GameObject, Sprite, or UI
element. Textures are often applied to the surface of a mesh to give it visual
detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture), this includes the Texture Type, Wrap
Mode, Filter Mode, and **Aniso Level** The anisotropic filtering (AF) level of
a texture. Allows you to increase texture quality when viewing a texture at a
steep angle. Good for floor and ground textures. [More info](class-
TextureImporter.html)  
See in [Glossary](Glossary.html#AnisoLevel) import settings.

If you change the import settings for an asset, Unity saves those new settings
to the `.meta` file that accompanies the asset. Unity then re-imports the
asset according to your updated settings, and updates the corresponding
imported “game-ready” data in the project’s `Library` folder.

### Meta files and asset files

**Important** : Meta files contain important information about how the asset
is used in the Project, and they must stay with the asset file they relate to.
If you move or rename an asset within Unity’s own Project window, Unity also
automatically moves or renames the corresponding .meta file. However, if you
move or rename an asset outside of Unity (that is, in Windows Explorer, or
Finder on macOS), you must move or rename the .meta file to match.

If an asset loses its meta file (for example, if you move or rename the asset
outside of Unity, but don’t move or rename the corresponding .meta file), any
reference to that asset is broken in your project. In this situation, Unity
notices that the asset does not have a corresponding meta file, generates a
new one for the moved/renamed asset as if it is a brand new asset, and deletes
the old “orphaned” .meta file.

This process can cause significant problems in your project. For example: * If
a texture asset loses its .meta file, any materials that use that texture lose
their reference to that texture. To fix it, you would need to manually re-
assign that texture to any materials which require it. * If a script asset
loses its .meta file, any **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) or **Prefabs** An asset type that
allows you to store a GameObject complete with components and properties. The
prefab acts as a template from which you can create new object instances in
the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) that have that script assigned instead
have an “unassigned script” component, and lose their functionality. To fix
it, you would need to manually re-assign that script to any GameObjects which
require it.

## Empty folders, meta files, and version control

Unity assigns each folder in your project’s `Assets` folder its own `.meta`
file. However, some **version control** A system for managing file changes.
You can use Unity in conjunction with most common version control tools,
including Perforce, Git, Mercurial and PlasticSCM. [More
info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) systems (VCS) can’t store
empty folders. This means that when you add or delete an empty folder from
your project, your VCS stores the `.meta` file as added or removed, but
doesn’t store the change of adding or removing the folder itself, which can be
confusing or problematic.

To help with this issue, Unity behaves in the following specific ways relating
to empty folders:

If Unity detects an empty folder that no longer has a corresponding meta file,
when that folder previously had a meta file, Unity assumes the meta file was
removed via the deletion of the folder by another user in your VCS, and
deletes the empty folder locally.

If Unity detects a new meta file for a folder, but that folder does not exist
locally, Unity assumes the new meta file was created via to the addition of
the folder by another user in the VCS, and creates the corresponding empty
folder locally.

[](class-TextAsset.html)

Text assets

[](AssetDatabase.html)

The Asset Database

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

