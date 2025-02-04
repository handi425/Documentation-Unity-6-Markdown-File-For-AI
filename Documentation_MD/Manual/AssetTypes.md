[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetTypes.html)
  * [中文](/cn/current/Manual/AssetTypes.html)
  * [日本語](/ja/current/Manual/AssetTypes.html)
  * [한국어](/kr/current/Manual/AssetTypes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetTypes.html)
  * [中文](/cn/current/Manual/AssetTypes.html)
  * [日本語](/ja/current/Manual/AssetTypes.html)
  * [한국어](/kr/current/Manual/AssetTypes.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * Supported Asset Types

[](ParallelImport.html)

Importing assets simultaneously

[](BuiltInImporters.html)

Built-in Importers

# Supported Asset Types

Unity supports many different types of assets and most common image file
types, including BMP, TIFF, TGA, JPG, and PSD.

If you save layered Photoshop (.psd) files in your `Assets` folder, Unity
imports them as flattened images. You can find out more about [importing
images as textures](ImportingTextures.html), or [importing images as
sprites](sprite/sprite-editor/sprite-editor-landing.html).

For the full list of Unity’s built-in importers, supported file types and
supported filename extensions, see [Built-in
importers](BuiltInImporters.html).

Listed below are some of the more common types of asset that you might want to
use when getting started with Unity, and links to find out more about how to
work with them.

## Commonly used asset types

Type | Description  
---|---  
**3D Model Files** | Unity supports the FBX file format, which means that you can import data from any 3D modeling software that supports FBX. Unity also natively supports importing SketchUp files. For a list of 3D modeling software that Unity supports, see [Model file formats](3D-formats.html).  
  
3D Model files can contain many types of asset, such as [meshes](FBXImporter-
Model.html), [animation](class-AnimationClip.html), [materials](FBXImporter-
Materials.html)An asset that defines how a surface should be rendered. [More
info](class-Material.html)  
See in [Glossary](Glossary.html#Material) and textures.  
  
For more information about importing 3D model files, see [Importing
Models](ImportingModelFiles.html).  
  
Unity also supports [SketchUp](class-SketchUpImporter.html) and
[SpeedTree](class-SpeedTreeImporter.html) formats.  
**Image files** | Unity imports image files as textures. Unity supports most common image file types, such as BMP, TIF, TGA, JPG, and PSD. If you save your layered Photoshop (.psd) files in your `Assets` folder, Unity imports them as flattened images. Read more about [importing textures](class-TextureImporter.html).  
**Audio files** | Unity supports many audio file formats. It’s generally best to import uncompressed audio file formats such as `.wav` or `.aiff`, because during import Unity applies the **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) settings specified in your import
settings. Read more about [importing audio files](AudioFiles.html).  
**Text, HTML, XML, JSON** | Unity can import arbitrary data from files, allowing you to store and use data from external sources. These are all handled by the [Text Asset Importer](class-TextAsset.html).  
**Plug-ins and code-related assets** | You can drop managed and native [plug-ins](./plug-ins.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) into your Unity project as assets
(such as `.dll` files) to expand the functionality of your game or app. Unity
also supports [assembly definitions](assembly-definition-files.html) to help
you create and organize your **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts) into assemblies.  
**Native Assets** | There are a range of asset types that are native to the Unity Editor. You can create assets of these types using Editor features. When you create these, Unity saves the files which represent them as asset files in the Assets folder of your project.  
  
These include [animations](animeditor-CreatingANewAnimationClip.html),
[curves](EditingCurves.html), [gradients](PartSysUsage.html), [masks](class-
AvatarMask.html)Can refer to a Sprite Mask, a UI Mask, or a Layer Mask [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Mask.html)  
See in [Glossary](Glossary.html#Mask), [materials](Materials.html), and
[presets](Presets.html). For the full list, see the NativeFormatImporter type
in the [Built-in Importer list](BuiltInImporters.html) below.  
  
## Assets in the Unity Package Manager

You can install a wide range of assets, including plug-ins, tools, and
libraries directly into Unity through the **Unity Package Manager (UPM)**.
These are a new type of package, and are available through the [Package
Manager window](upm-ui.html). For more information about packages in general,
see the [Packages](Packages.html)Packages are collections of assets to be
shared and re-used in Unity. The [Unity Package Manager](upm-ui.html) (UPM)
can display, add, and remove packages from your project. These packages are
native to the Unity Package Manager and provide a fundamental method of
delivering Unity functionality. However, the Unity Package Manager can also
display [Asset Store packages](AssetStorePackages.html) that you downloaded
from the Asset Store. [More info](Packages.html)  
See in [Glossary](Glossary.html#Packages) documentation.

## Reusing assets between projects

As you build your game, Unity stores a lot of metadata about your assets, such
as import settings and links to other assets, among other information. If you
want to transfer your assets into a different project and preserve all this
information, you can export your assets into one of these containers:

  * A [custom package](CustomPackages.html), which you can access and manage inside [Unity’s Package Manager](Packages.html).
  * An [asset package](AssetPackages.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage), which you can create directly
in the Editor.

[](ParallelImport.html)

Importing assets simultaneously

[](BuiltInImporters.html)

Built-in Importers

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

