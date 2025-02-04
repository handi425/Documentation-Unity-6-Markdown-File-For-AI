[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetBundles-Troubleshooting.html)
  * [中文](/cn/current/Manual/AssetBundles-Troubleshooting.html)
  * [日本語](/ja/current/Manual/AssetBundles-Troubleshooting.html)
  * [한국어](/kr/current/Manual/AssetBundles-Troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetBundles-Troubleshooting.html)
  * [中文](/cn/current/Manual/AssetBundles-Troubleshooting.html)
  * [日本語](/ja/current/Manual/AssetBundles-Troubleshooting.html)
  * [한국어](/kr/current/Manual/AssetBundles-Troubleshooting.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [AssetBundles](AssetBundlesIntro.html)
  * Troubleshooting

[](AssetBundles-Patching.html)

Patching with AssetBundles

[](AssetBundles-Integrity.html)

AssetBundle Download Integrity and Security

# Troubleshooting

## Tips for Investigating AssetBundle Build results

The following methods can be useful for collecting information after an
AssetBundle build has run. These can be useful when investigating unexpected
behavior, or when tuning the assignment of assets to bundles.

### Logs

The [Unity Editor log](log-files.html) collects information during a build,
such as warning or error messages. And at the end of an AssetBundle build
there is a detailed message logged that shows information about the type and
size breakdown for each AssetBundle.

### Build Report

AssetBundle builds generate a BuildReport which is a Unity SerializedFile
written to `Library/LastBuild.buildreport` inside the project directory. This
file is useful for seeing a summary of the timings for build steps and a
detailed view of the contents of the AssetBundle. The
[BuildReport](../ScriptReference/Build.Reporting.BuildReport.html) API can be
used to read information from the BuildReport file.

Two unsupported tools are available for viewing the content of the
BuildReport:

  * [Build Report Inspector](https://docs.unity3d.com/Packages/com.unity.build-report-inspector@latest)
  * [Project Auditor](https://github.com/Unity-Technologies/ProjectAuditor)

### .manifest files

The manifest files generated alongside each AssetBundle give some human-
readable details about the contents of an AssetBundle.

## Clean Builds

To speed up iteration time Unity supports incremental building for
AssetBundles. For example, elements from past builds can be reused for aspects
of the project that have not changed since the last build. While this can
speed up iteration time, there are a few limitations on its ability to detect
changes in the input, especially if **scripts** A piece of code that allows
you to create your own Components, trigger game events, modify Component
properties over time and respond to user input in any way you like. [More
info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) run by build callbacks are changing
data in a non-deterministic way. Therefore, you should always perform a clean
build rather than an incremental build when you are building an official
release of your AssetBundles.

The `BuildAssetBundleOptions.ForceRebuildAssetBundle` flag, passed as an
option to BuildPipeline.BuildAssetBundles(), is the recommended way to perform
a clean build.

In some rare cases it might also be desirable to erase the Library/ShaderCache
directory. This cache is not flushed when
BuildAssetBundleOptions.ForceRebuildAssetBundle is specified. On many projects
the **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) compilation phase can be quite a time
consuming step, so erasing the cache can add a lot of time to the next Player
or AssetBundle build.

Alternatively, the most reliable way to perform a completely clean build is to
stop Unity, erase the project’s Library directory, and then restart Unity.
This can be very time consuming because all the project Assets need to be
reimported and other data is regenerated.

## Examining AssetBundle contents

In some cases you might want to look directly inside an AssetBundle, or
compare the contents of two AssetBundles.

The Unity Editor installation includes the `WebExtract` and `Binary2Text`
executables. You can use WebExtract to extract the files that are nested
inside the AssetBundle, similar to extracting a zip file. Then you can use
Binary2Text to produce a text format dump of the contents of a binary
SerializedFile. Its output is somewhat similar to the yaml format used by
Unity.

Another similar mechanism to see the content of an AssetBundle’s
SerializedFiles in text form is to run `UnityDataTools` with its “dump”
argument.

The raw content of Serialized files tends to be very technical and very large,
especially when Shaders or Meshes or binary data is present. But these dumps
can also provide a wealth of information if you can narrow down a problem to
specific objects within a file. Comparing the extracted content of two similar
AssetBundles using a diff tool can be a convenient way to narrow down the
precise differences.

## Target Switching

The arguments to the BuildPipeline.BuildAssetBundles API lets you specify the
target (and subtarget) platform where you will be deploying the AssetBundles.

It is possible the requested platform is different from what is currently
configured in the [Build Profiles](build-profiles.html)A set of customizable
configuration settings to use when creating a build for your target platform.
[More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile) window. However you should
always make sure the settings in Build Profiles match the settings for your
AssetBundle build, prior to triggering your build script. When the targets
don’t match, Unity must recompile the Editor scripts to reflect the new
platform and also potentially trigger imports for Assets like textures that
have platform specific representations. Then at the end of the build it will
restore the state back to match the original target platform. Typically this
works fine, but it can add significant time to each build, which can add up
when performing a lot of build iterations. Furthermore the script that
contains the call to BuildPipeline.BuildAssetBundles will continue to execute
in the script domain as compiled for the current target, not the specified
build target. This is only a problem if the build script, or callback scripts,
expects platform-specific code or assemblies to be available. For many
projects this subtle difference will not be an issue. But to help avoid this
sort of pitfall you should always make sure that any code executed during a
build checks the target dynamically (e.g. with `if` statements) instead of
using platform conditional compilation (#ifdef statements).

For command line builds the `--buildTarget` [command line
argument](EditorCommandLineArguments.html) should be used to match the target
you want to build.

## Asset Duplication

Unity’s AssetBundle system will discover all dependencies of an Object when
the Object is built into an AssetBundle. This is done using the Asset
Database. This dependency information is used to determine the set of Objects
that will be included in an AssetBundle.

Assignment to AssetBundles happens at the Asset level. The Objects inside an
Asset that is explicitly assigned to an AssetBundle will only be built into
that single AssetBundle. Depending which signature of
[BuildPipeline.BuildAssetBundles](../ScriptReference/BuildPipeline.BuildAssetBundles.html)
is called, an Asset is “explicitly assigned” either by setting the Asset’s
[AssetImporter.assetBundleName](../ScriptReference/AssetImporter.assetBundleName.html)
property to a non-empty string, or by listing it in
[AssetBundleBuild.assetNames](../ScriptReference/AssetBundleBuild.assetNames.html).

Any Object that is part of an Asset that is not explicitly assigned in an
AssetBundle will be included in each AssetBundle that contains any Objects
that reference it.

In other words, if two different Objects are assigned to two different
AssetBundles, but both have references to a common dependency Object, then
that dependency Object will be copied into both AssetBundles. The duplicated
dependency will also be instanced, meaning that the two copies of the
dependency Object will be considered different Objects with a different
identifiers. This will increase the total size of the application’s
AssetBundles. This will also cause two different copies of the Object to be
loaded into memory if the application loads both of its parents.

There are several ways to address this problem:

  1. Ensure that Objects built into different AssetBundles do not share dependencies. Any Objects which do share dependencies can be placed into the same AssetBundle without duplicating their dependencies.

     * This method usually is not viable for projects with many shared dependencies. It can produce monolithic AssetBundles that must be rebuilt and re-downloaded too frequently to be convenient or efficient.
  2. Segment AssetBundles so that no two AssetBundles that share a dependency will be loaded at the same time.

     * This method may work for certain types of projects, such as level-based games. However there is still a trade-off, because duplicated objects will increase the build time and sizes of the project’s AssetBundles, and could impact loading times.
  3. Ensure that all dependency assets are built into their own AssetBundles. This entirely eliminates the risk of duplicated assets, but also introduces complexity. The application must track dependencies between AssetBundles, and ensure that the right AssetBundles are loaded before calling any AssetBundle.LoadAsset APIs.

Object dependencies are tracked via the AssetDatabase API, located in the
UnityEditor namespace. As the namespace implies, this API is only available in
the Unity Editor and not at runtime.
[AssetDatabase.GetDependencies](../ScriptReference/AssetDatabase.GetDependencies.html)
can be used to locate all of the immediate dependencies of a specific Object
or Asset. Note that these dependencies may have their own dependencies so this
can be a recursive calculation. The assignment of Assets to AssetBundles will
either be defined explicitly by passing arrays of AssetBundleBuild structures
when calling BuildPipeline.BuildAssetBundles, or can be queried using the
AssetImporter API. It is possible to write an Editor script that ensures that
all of an AssetBundle’s direct or **indirect dependencies** An **indirect** ,
or transitive dependency occurs when your project requests a package which
itself “depends on” another package. For example, if your project depends on
the `alembic@1.0.7` package which in turn depends on the `timeline@1.0.0`
package, then your project has an direct dependency on Alembic and an indirect
dependency on Timeline. [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency) are assigned to
AssetBundles, or that no two AssetBundles share dependencies that have not
been assigned to an AssetBundle.

**Note** : When building AssetBundles with the
[Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html)
package, the `Addressables Analyze` window can be used to discover duplicated
assets.

## Sprite Atlas Duplication

The following sections describe a quirk of asset dependency calculation code
when used in conjunction with automatically-generated **sprite** A 2D graphic
objects. If you are used to working in 3D, Sprites are essentially just
standard textures but there are special techniques for combining and managing
sprite textures for efficiency and convenience during development. [More
info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) atlases.

Any automatically-generated **sprite atlas** A utility that packs several
sprite textures tightly together within a single texture known as an atlas.
[More info](sprite/atlas/v2/v2-landing.html)  
See in [Glossary](Glossary.html#SpriteAtlas) will be assigned to the
AssetBundle containing the Sprite Objects from which the sprite atlas was
generated. If the sprite Objects are assigned to multiple AssetBundles, then
the sprite atlas will not be assigned to an AssetBundle and will be
duplicated. If the Sprite Objects are not assigned to an AssetBundle, then the
sprite atlas will also not be assigned to an AssetBundle.

To ensure that sprite atlases are not duplicated, check that all sprites
tagged into the same sprite atlas are assigned to the same AssetBundle.

## Android Textures

Due to heavy device fragmentation in the Android ecosystem, it’s often
necessary to compress textures into several different formats. While all
Android devices support ETC1, ETC1 doesn’t support textures with alpha
channels.

To use AssetBundle Variants, all textures that can’t be cleanly compressed
using ETC1 must be isolated into texture-only AssetBundles. Next, create
sufficient variants of these AssetBundles to support the non-ETC2-capable
slices of the Android ecosystem, using vendor-specific texture **compression**
A method of storing data that reduces the amount of storage space it requires.
See [Texture Compression](class-TextureImporterOverride), [Animation
Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) formats such as DXT5, PVRTC. For
each AssetBundle Variant, change the included textures’ TextureImporter
settings to the compression format appropriate to the Variant.

At runtime, support for the different **texture compression** 3D Graphics
hardware requires Textures to be compressed in specialized formats which are
optimized for fast Texture sampling. [More info](class-
TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) formats can be detected
using the
[SystemInfo.SupportsTextureFormat](http://docs.unity3d.com/ScriptReference/SystemInfo.SupportsTextureFormat.html?_ga=1.141687282.1751468213.1479139860)
API. This information should be used to select and load the AssetBundle
Variant containing textures compressed in a supported format.

More information on Android texture compression formats can be found
[here](http://developer.android.com/guide/topics/graphics/opengl.html#textures).

## Interactions between Shaders and AssetBundles

When you build an AssetBundle, Unity uses information in that bundle to select
which shader variants to compile. This includes information about the
**scenes** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), materials, [Graphics
Settings](https://docs.unity3d.com/Manual/class-GraphicsSettings.html), and
[ShaderVariantCollections](../ScriptReference/ShaderVariantCollection.html) in
the AssetBundle.

Separate build pipelines compile their own shaders independently of other
pipelines. If both a Player build and an Addressables build reference a
shader, Unity compiles two separate copies of the shader, one for each
pipeline.

This process doesn’t account for any runtime information such as keywords,
textures, or changes due to code execution. If you want to include specific
shaders in your build, either include a ShaderVariantCollection with the
desired shaders, or include the shader in your build manually by adding it to
the Always Included Shaders list in your graphics settings.

[](AssetBundles-Patching.html)

Patching with AssetBundles

[](AssetBundles-Integrity.html)

AssetBundle Download Integrity and Security

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

