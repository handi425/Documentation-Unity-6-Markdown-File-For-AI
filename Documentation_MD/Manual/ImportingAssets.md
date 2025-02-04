[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ImportingAssets.html)
  * [中文](/cn/current/Manual/ImportingAssets.html)
  * [日本語](/ja/current/Manual/ImportingAssets.html)
  * [한국어](/kr/current/Manual/ImportingAssets.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ImportingAssets.html)
  * [中文](/cn/current/Manual/ImportingAssets.html)
  * [日本語](/ja/current/Manual/ImportingAssets.html)
  * [한국어](/kr/current/Manual/ImportingAssets.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * Importing assets

[](AssetWorkflow.html)

Asset workflow

[](ParallelImport.html)

Importing assets simultaneously

# Importing assets

You can bring assets created outside of Unity into your Unity project. To do
this, you can either export the file directly into the `Assets` folder for
your project, or copy it into that folder. For many common formats, you can
save your source file directly into your project’s `Assets` folder and Unity
can read it. Unity also detects when you save new changes to the file and re-
imports files as necessary.

When you create a Unity project, Unity creates a folder (named after your
project) which contains the following subfolders:

  * `Temp`
  * `Library`
  * `Assets`
  * `ProjectSettings`
  * `Logs`
  * `Packages`

You can save or copy files that you want to use in your project into the
`Assets` folder, and you can use the **Project window** A window that shows
the contents of your `Assets` folder (Project tab) [More
info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) inside Unity to view the
contents of your `Assets` folder. Therefore, if you save or copy a file to
your `Assets` folder, Unity imports it and it then appears in your Project
window.

When you modify a file in Unity, Unity does not modify your original source
file, even though you can often choose between various ways to compress,
modify, or otherwise process the asset within Unity. Instead, the import
process reads your source file, and creates a game-ready representation of
your asset internally, matching your chosen import settings. If you modify the
import settings for an asset, or make a change to the source file in the
`Assets` folder, Unity re-imports the asset again to reflect your changes.

**Warning:** In most cases, the items that appear in your Project window
represent actual files on your computer. If you delete them within the Unity
Editor Project window, you also delete them from your computer.

Unity automatically detects files as they are added to the `Assets` folder, or
if they are modified. When you put any asset into your `Assets` folder, it
appears in your Project window.

![The Project window shows Assets that Unity has imported into your
project](../uploads/Main/ProjectBrowser.png) The Project window shows Assets
that Unity has imported into your project

If you drag a file from your computer’s file browser into Unity’s Project
window, Unity makes a copy and places it into your `Assets` folder. You can
then access this copy from the Project window.

To bring collections of assets into your project from another Unity project,
you can use [Asset packages](AssetPackages.html)A collection of files and data
from Unity projects, or elements of projects, which are compressed and stored
in one file, similar to Zip files, with the `.unitypackage` extension. Asset
packages are a handy way of sharing and re-using Unity projects and
collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage).

## Asset Import Settings

The simplest way to safely move or rename your assets is to always do it from
within Unity’s project folder. This way, Unity automatically moves or renames
the corresponding meta file. To read more about .meta files and the import
process, see [How Unity imports
assets](AssetWorkflow.html#howUnityImportsAssets).

Each type of asset that Unity supports has a set of Import Settings, which
affect how the asset appears or behaves. To view an asset’s import settings,
select the asset in the Project View. The import settings for this asset will
appear in the **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). The options that appear vary
depending on the type of asset selected.

For example, an image’s import settings allow you to choose whether Unity
imports it as a Texture, a 2D **sprite** A 2D graphic objects. If you are used
to working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite), or a **normal map** A type of Bump
Map texture that allows you to add surface detail such as bumps, grooves, and
scratches to a model which catch the light as if they are represented by real
geometry.  
See in [Glossary](Glossary.html#Normalmap). The import settings for an FBX
file allow you to adjust the scale, generate normals or **lightmap** A pre-
rendered texture that contains the effects of light sources on static objects
in the scene. Lightmaps are overlaid on top of scene geometry to create the
effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) coordinates, and split & trim
**animation clips** Animation data that can be used for animated characters or
simple animations. It is a simple “unit” piece of motion, such as (one
specific instance of) “Idle”, “Walk” or “Run”. [More info](class-
AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) defined in the file.

![Clicking on an image asset in the Project window shows the import settings
for that asset in the
Inspector](../uploads/Main/AssetWorkflowImportSettings.png) Clicking on an
image asset in the Project window shows the import settings for that asset in
the Inspector

For other asset types, the import settings look different. The various
settings you see relate to the type of asset selected. Here’s an example of an
Audio asset, with its related import settings shown in the inspector:

![An Audio asset selected in the Project window shows the Audio import
settings for that asset in the
Inspector](../uploads/Main/ImportSettingsAudioExample.png) An Audio asset
selected in the Project window shows the Audio import settings for that asset
in the Inspector

If you are developing a cross-platform project, you can override the “default”
settings and assign different import settings on a per-platform basis.

## Asset processing

Unity reads and processes any files that you add to the `Assets` folder, and
converts the contents of the file to internal game-ready data. The asset files
themselves remain unchanged, and the internal data is stored in the project’s
`Library` folder. This data is part of the Unity Editor’s [Asset
Database](AssetDatabase.html).

Using internal formats for assets allows Unity to have internal versions of
your assets ready to use at runtime in the Editor, and to keep your unmodified
source files in the `Assets` folder. A distinction between the asset files and
the internal versions means that you can quickly edit the asset file, and have
the Editor pick up the changes automatically. For example, you can save `.psd`
files directly into your `Assets` folder, but hardware such as mobile devices
and PC graphics cards can’t process that format directly in order to render
them as textures. Instead, Unity can convert an internal version into a format
that those platforms can process.

Unity stores the internal representation of your assets in the `Library`
folder, which behaves like a cache folder. As a user, you should never need to
alter the `Library` folder manually; if you do, you might negatively affect
your project in the Unity Editor. This also means that you should not include
the `Library` folder under **version control** A system for managing file
changes. You can use Unity in conjunction with most common version control
tools, including Perforce, Git, Mercurial and PlasticSCM. [More
info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl).

**Note:** If your project is not open in Unity, you can safely delete the
`Library` folder, because Unity can regenerate all of its data from the
`Assets` and `ProjectSettings` folders the next time you launch your project.

## Complex assets

In some cases, Unity might create multiple assets while importing a single
asset file. For example:

  * When a 3D file (such as an FBX file) defines Materials or contains embedded Textures. To handle this, Unity extracts the [Materials and embedded Textures](FBXImporter-Materials.html) as separate assets.
  * When you want to import an image file as multiple 2D sprites. You should use the 2D [Sprite Editor](sprite/sprite-editor/sprite-editor-landing.html) to define multiple sprites from a single graphic image. Unity displays each sprite defined in the Editor as a separate Sprite asset in the Project window.
  * When a 3D file contains multiple animation timelines or multiple clips. To handle this, Unity automatically defines separate animation timelines or clips based on its [animation import settings](Splittinganimations.html). The resulting multiple animation clips appear as separate Animation Clip assets in the Project window.

## See also

  * [Asset packages](AssetPackages.html)
  * [Materials and Shaders](Materials.html)
  * [Textures and Videos](Textures.html)
  * [Sprite Editor](sprite/sprite-editor/sprite-editor-landing.html)
  * [Sprite Atlas](sprite/atlas/v2/v2-landing.html)A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](sprite/atlas/v2/v2-landing.html)  
See in [Glossary](Glossary.html#SpriteAtlas)

  * [Audio Files](AudioFiles.html)
  * [Tracker Modules](TrackerModules.html)

[](AssetWorkflow.html)

Asset workflow

[](ParallelImport.html)

Importing assets simultaneously

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

