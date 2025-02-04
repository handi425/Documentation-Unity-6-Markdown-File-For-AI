[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Build-MultiProcess.html)
  * [中文](/cn/current/Manual/Build-MultiProcess.html)
  * [日本語](/ja/current/Manual/Build-MultiProcess.html)
  * [한국어](/kr/current/Manual/Build-MultiProcess.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Build-MultiProcess.html)
  * [中文](/cn/current/Manual/Build-MultiProcess.html)
  * [日本語](/ja/current/Manual/Build-MultiProcess.html)
  * [한국어](/kr/current/Manual/Build-MultiProcess.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [AssetBundles](AssetBundlesIntro.html)
  * Multi-Process AssetBundle Building (Experimental)

[](AssetBundles-Integrity.html)

AssetBundle Download Integrity and Security

[](ScriptingAssets.html)

Scripting with Assets

# Multi-Process AssetBundle Building (Experimental)

Multi-Process AssetBundle Building is a significant improvement to the way
AssetBundles are built compared with previous versions of Unity. This feature
(introduced in 2023.1) is initially offered side-by-side with the existing
build code, and is disabled by default. The new functionality only applies to
AssetBundles that are built with BuildPipeline.BuildAssetBundles(), not to
those built with Addressables.

This feature provides improved build performance and addresses some long-
standing issues with AssetBundles. To facilitate adoption it offers a high
degree of compatibility in its output and is available through the existing
API.

The new mechanism makes use of the Asset Database to perform multiple parallel
imports, as well as caching intermediate files. In many cases a clean build
will be faster when this feature is enabled, and incremental builds can be
much faster and more accurate. In addition, you can use the
[Accelerator](UnityAccelerator.html)The Unity Accelerator is an external tool
that provides an asset cache that keeps copies of a team’s imported assets.
The goal of the Accelerator is to speed up teamwork and reduce iteration time
by coordinating asset sharing so that you don’t need to reimport portions of
your project. [More info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator) to share build artifacts between
machines, making it possible for builds from one machine to speed up similar
builds on other machines. For more information see also [Parallel
Import](ParallelImport.html).

When Multi-Process building is enabled it also moves the **shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) compilation work to its own dedicated
build step, which can make it clearer how much time is spent compiling
shaders, compared to other steps of a build.

## Enabling Multi-Process AssetBundle building

To enable the new feature in the user interface

  1. Open the [Editor](class-EditorManager.html) settings (top menu: **Edit > Project Settings**, then select the **Editor** category).
  2. Click the check box for **Multi-Process AssetBundle Building**.

The setting is exposed to scripting using
[EditorBuildSettings.UseParallelAssetBundleBuilding](../ScriptReference/EditorBuildSettings.UseParallelAssetBundleBuilding.html).

## Differences and Known Limitations

  * **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Optimization is not enabled when using
Multi-Process AssetBundle Building. It is silently forced to “off” during the
build. Note: In practice Mesh Optimization adds a high cost and complexity to
the building process, and often does not give very much gain at runtime.

  * **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) Atlas V1 is not supported. An error is
printed when this older format is detected. You should update V1 assets to
[SpriteAtlasV2](sprite/atlas/v2/v2-landing.html) in order to build
successfully.

  * The way that objects influence each other is now calculated across all AssetBundles rather than within the scope of each individual AssetBundle. For example, if a material needs a certain shader feature to be enabled, then that shader feature will be enabled, even if the shader is part of a different AssetBundle. This gives results closer to what is typically expected, but can result in some longer shader compilation times, especially if a shader is repeated in multiple AssetBundles. See also [Shader keywords](shader-keywords.html).
  * Given identical input, the output from a multi-process build will not be binary-identical to a non-multi-process build. However, the output should be functionally identical. This means that if you have already shipped AssetBundles to users, then updating your project to use Multi-Process building may result in changes to all your AssetBundle files. When you push your next release this can trigger downloads for your live users. The binary differences come from improvements and bug fixes that can result in slightly different object naming or ordering inside the AssetBundle.
  * The disk space used by your Project’s Library folder can grow larger because we use the AssetDatabase to cache intermediate build artifacts. These artifacts are fully flushed at the beginning of a build when the [BuildAssetBundleOptions.ForceRebuildAssetBundle](../ScriptReference/BuildAssetBundleOptions.ForceRebuildAssetBundle.html) flag is specified.
  * When Multi-Process is enabled, the AssetBundle hash is a hash value of the uncompressed contents of the AssetBundle. This serves as a file version identifier that is independent of the **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) and that doesn’t incorporate the
content of the AssetBundle header. **Tip:** the
[BuildAssetBundleOptions.AssetBundleStripUnityVersion](../ScriptReference/BuildAssetBundleOptions.AssetBundleStripUnityVersion.html)
flag can be useful to exclude the Unity version from the AssetBundle content,
and hence from the hash.

  * With this new way of calculating hashes, the hash can only be determined by running the full build. Therefore [AssetBundleManifest.GetAssetBundleHash](../ScriptReference/AssetBundleManifest.GetAssetBundleHash.html) returns 0 when BuildPipeline.BuildAssetBundles is called with [BuildAssetBundleOptions.DryRunBuild](../ScriptReference/BuildAssetBundleOptions.DryRunBuild.html).

## Build Callbacks

If you are adapting an existing project which uses Build Callbacks to work
with the Multi-Process AssetBundle Building, you may need to make code changes
to your Build Callback code.

During a build, **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) files are loaded and resaved into the
output format. Script code may be executed during this time, for example via
the
[IProcessSceneWithReport.OnProcessScene](../ScriptReference/Build.IProcessSceneWithReport.OnProcessScene.html)
build callback. When Multi-Process AssetBundle Building is used this script
code will execute in the context of an Import job inside a AssetDatabase
worker process, similar to how a ScriptedImporter can run.

For scene callbacks that work entirely with the state of the scene that is
loaded there will be no problem running as part of an AssetDatabase importer.
But certain situations may cause trouble:

  * Changing Assets. You should never create, delete or modify external assets from within a build callback. There are now specific protections which prevent calls to AssetDatabase APIs that change assets. A scripting exception is thrown with a clear error message if those calls are made.

  * Dependency tracking. In some contexts it is necessary for a build callback to read the contents of other assets outside of the scene. If the scene also references that asset explicitly, this works properly without any additional change. If not, you need to update your build callback implementation to use the new [BuildPipelineContext.DependOnAsset](../ScriptReference/Build.BuildPipelineContext.DependOnAsset.html) call so that the dependency is tracked. Otherwise future incremental builds might re-use cached artifacts that are out of date, and the callback script will not be invoked.

  * Singletons and Global State. The multi-process nature of the new build system means that scenes and other assets are loaded in different worker processes, rather than all being loaded in sequence inside the main Unity Process. This means code that uses shared access to global data, such as a Singleton, may stop working. It might be necessary to rework any code that depends on shared memory to use data stored directly in the scene, or inside an asset or possibly a temporary file.

### Callback versioning

Because of caching, an incremental build only invokes a build callback if the
scene or another dependency has changed since the last build. If the script
callback has changed and must be run again, you can force this to occur by
incrementing the
[BuildCallbackVersion](../ScriptReference/Build.BuildCallbackVersionAttribute.html)
attribute on the callback. For callbacks that do not specify that attribute
the default version number is 1.

Note: there are other circumstances in which scripting code may be invoked
during a build, for example the
[Awake](../ScriptReference/MonoBehaviour.Awake.html) method on MonoBehaviour-
derived classes with the
[ExecuteInEditMode](../ScriptReference/ExecuteInEditMode.html) attribute. If
you have code is performing actions that aren’t permitted during an
AssetDatabase import then you might need to change that code. **Tip:** the
[BuildPipeline.isBuildingPlayer](../ScriptReference/BuildPipeline.isBuildingPlayer.html)
API returns true during AssetBundle builds, so you can use it to add
conditional logic, for example to avoid executing problematic code during a
build but to still permit it when entering Playmode.

## Diagnostics flags for Advanced Troubleshooting

In addition to the general techniques and tools mentioned in the [AssetBundle
Trouble](AssetBundles-Troubleshooting.html) topic, these are a few [Diagnostic
flags](Preferences.html) available in the Preference Window which can aid in
collecting detailed information about an AssetBundle build. These flags are
intended for advanced use and in the future they may change, or be removed.

### Backward Compatibility Mode

The `BuildPipelineBinaryBackwardCompatibilityMode` diagnostic flag is specific
to Multi-Process AssetBundle builds. When enabled, certain behaviors are
changed to more closely match the behavior of the existing AssetBundle build
logic. In some cases enabling this flag will result in AssetBundles that have
precisely matching binary content to a build performed with the Multi-Process
project setting turned off. This flag is off by default because most of the
differences in the AssetBundle content are the result of intentional
improvements, and the compatibility mode might be removed in the future.
However this flag might be useful in existing projects, where it can be
important to have minimal churn in AssetBundle content.

### Build Profiling

When the `BuildPipelineTEPCapture` Diagnostic flag is enabled then calls to
`BuildPipeline.BuildAssetBundles` will generate a “trace event” format
**profiler** A window that helps you to optimize your game. It shows how much
time is spent in the various areas of your game. For example, it can report
the percentage of time spent rendering, animating, or in your game logic.
[More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) file. You can use this file to get a
detailed view of what steps the build performed, including steps performed in
each AssetDatabase worker process.

This file is overwritten for each build and can be found at the path
`Logs/BuildAssetBundlesTEP.json`. This is the file format supported by Chrome
Tracing, see [Trace Event
Format](https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/edit?usp=sharing)
for details. One way to view the content is to open it with the
chrome://tracing tool in Google Chrome or another Chromium-based browser.

### Build Debug Files

The `BuildPipelineWriteDebugFiles` flag is specific to Multi-Process
AssetBundle builds. When enabled, the build writes extra JSON format files
into the `Temp/BuildInstructions` folder. These files are only useful for
testing and debugging purposes, they are not required or consumed by the build
itself. When sending bug reports to Unity, it might be useful to provide these
files, especially if it is not possible to submit the full project.

[](AssetBundles-Integrity.html)

AssetBundle Download Integrity and Security

[](ScriptingAssets.html)

Scripting with Assets

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

