[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetPackagesCreate.html)
  * [中文](/cn/current/Manual/AssetPackagesCreate.html)
  * [日本語](/ja/current/Manual/AssetPackagesCreate.html)
  * [한국어](/kr/current/Manual/AssetPackagesCreate.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetPackagesCreate.html)
  * [中文](/cn/current/Manual/AssetPackagesCreate.html)
  * [日本語](/ja/current/Manual/AssetPackagesCreate.html)
  * [한국어](/kr/current/Manual/AssetPackagesCreate.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Asset packages](AssetPackages.html)
  * Create and export asset packages

[](AssetPackages.html)

Asset packages

[](AssetPackagesImport.html)

Importing local asset packages

# Create and export asset packages

If you want to share **scenes** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), samples, tools, or other assets, you
can export an **asset package** A collection of files and data from Unity
projects, or elements of projects, which are compressed and stored in one
file, similar to Zip files, with the `.unitypackage` extension. Asset packages
are a handy way of sharing and re-using Unity projects and collections of
assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage) (`.unitypackage` format). You
might want to create an asset package to copy several assets or an entire
scene from one project to another. Another option is to [create your own Unity
package](CustomPackages.html).

Follow these instructions to export an asset package.

**Note** : If your assets are high quality and other users might find them
useful, refer to [Publishing to the Asset Store](AssetStorePublishing.html)
for instructions to create a package draft and upload it to the **Asset
Store** A growing library of free and commercial assets created by Unity and
members of the community. Offers a wide variety of assets, from textures,
models and animations to whole project examples, tutorials and Editor
extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore).

To create and export an asset package:

  1. Open the project you want to export assets from.

  2. Go to the **Project** In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) window and select one or more items
or folders. These items become the starting list for your export. You can also
select the `Assets` folder as a way include all assets as your starting point.

  3. Choose **Assets** Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) > **Export Package** from the menu to
open the **Exporting package** dialog.

![Exporting package dialog](../uploads/Main/ExportPackageDialog.png) Exporting
package dialog

  4. In the dialog, select the assets you want to include in the package by clicking on the boxes.

  5. Leave **Include dependencies** enabled to automatically select any assets used by the assets you already selected. Enabling **Include dependencies** also includes any **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that are directly required by the
selected assets.

  6. Leave **Include all scripts** enabled to export all scripts from your project. If you disable **Include all scripts** but enable **Include dependencies** , Unity still exports the scripts that your selected items directly depend on. Unity doesn’t have a way to determine whether the scripts in your selection reference other scripts. Enabling **Include all scripts** reduces the likelihood of compilation errors when using the exported package in another project.

**Tip** : Selecting all items and enabling both checkboxes is a simple way of
exporting the assets in a scene without manually locating them all.

  7. Click **Export** to bring up the file explorer and choose where you want to store your package file.

  8. Name and save the package.

## Re-exporting asset packages

If you want to change the contents of an asset package and create a newer,
updated version of your asset package, select the asset files you want in your
package (both the unchanged ones and the new ones). Then follow the previous
instructions to export the files.

### Naming strategies

Rename your updated package using incremental names: for example,
`MyAssetPackageVer1`, `MyAssetPackageVer2`. Unity recognizes it as an update,
so you should use a naming convention that’s clear for you and anyone you
share it with.

**Warning:** Don’t remove files from asset packages and then add different
files with the same name. Unity [uses unique IDs](AssetMetadata.html#uniqueID)
to track files, so it recognizes them as different and possibly conflicting
files. In these cases, Unity displays a warning symbol when importing them. If
you have removed a file and then decide to replace it, rename it something
else, even if it is close to the original name.

## Additional resources

  * [Create custom packages](CustomPackages.html)

[](AssetPackages.html)

Asset packages

[](AssetPackagesImport.html)

Importing local asset packages

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

