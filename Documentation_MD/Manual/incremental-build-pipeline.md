[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/incremental-build-pipeline.html)
  * [中文](/cn/current/Manual/incremental-build-pipeline.html)
  * [日本語](/ja/current/Manual/incremental-build-pipeline.html)
  * [한국어](/kr/current/Manual/incremental-build-pipeline.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/incremental-build-pipeline.html)
  * [中文](/cn/current/Manual/incremental-build-pipeline.html)
  * [日本語](/ja/current/Manual/incremental-build-pipeline.html)
  * [한국어](/kr/current/Manual/incremental-build-pipeline.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * Incremental build pipeline

[](build-profiles-reference.html)

Build Profiles window reference

[](comp-ManagerGroup.html)

Project Settings

# Incremental build pipeline

For faster iteration during development, Unity uses an incremental build
pipeline that only rebuilds parts of the application if they have changed
since the previous build (stored in the project’s `Library/Bee` directory),
including build steps such as asset serialization, code compilation, data
**compression** A method of storing data that reduces the amount of storage
space it requires. See [Texture Compression](class-TextureImporterOverride),
[Animation Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression), and signing.

This setup has a local cache that reuses some specific parts of builds (such
as non-embedded packages and libIL2CPP artifacts) across different projects.
The location of this cache is set using the `BEE_CACHE_DIRECTORY` environment
variable, and defaults to a different location depending on your operating
system:

  * On Windows, `BEE_CACHE_DIRECTORY` defaults to `%USERPROFILE%\AppData\Local\Unity\Caches\bee`
  * On Mac, `BEE_CACHE_DIRECTORY` defaults to `$HOME/Library/Unity/cache/bee`
  * On Linux, `BEE_CACHE_DIRECTORY` defaults to `$XDG_CONFIG_HOME/.cache/unity3d/bee` (if `$XDG_CONFIG_HOME` is set) or `$HOME/.cache/unity3d/bee`

The incremental build pipeline also automates the [Scripts Only
Build](../ScriptReference/BuildOptions.BuildScriptsOnly.html) feature.
****Scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) Only Build** is therefore only
available in the [Build Profiles](build-profiles.html)A set of customizable
configuration settings to use when creating a build for your target platform.
[More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile) window for the platforms that
don’t use incremental builds.

The incremental build pipeline works for both the Mono and **IL2CPP** A Unity-
developed scripting back-end which you can use as an alternative to Mono when
building projects for some platforms. [More info](./scripting-backends-
il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) [scripting backend](scripting-
backends.html)A framework that powers scripting in Unity. Unity supports three
different scripting backends depending on target platform: Mono, .NET and
IL2CPP. Universal Windows Platform, however, supports only two: .NET and
IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend), although the output file
structure changes depending on which scripting backend your project uses.

By default, Unity uses the incremental build pipeline for both release and
**development builds** A development build includes debug symbols and enables
the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-
target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild). See the Creating non-
incremental builds section below for details on how to make a clean build,
which may be useful if the cache has been corrupted somehow.

## Platform compatibility

Unity supports the incremental build pipeline for the following platforms:

  * Standalone (Windows, Mac and Linux)
  * Web
  * Xbox One
  * Xbox Series X and Xbox Series S
  * Android
  * iOS
  * tvOS

## Creating non-incremental builds

In some scenarios, it can be useful or necessary to create builds that don’t
use the incremental build pipeline.

To create a clean, non-incremental, build:

  1. Open the **Build Profiles** window (**File** > **Build Profiles**).
  2. Next to the **Build** button, select the drop-down.
  3. Select **Clean Build**.

In general, if expected changes are not present after an incremental build and
you think there is a problem with the incremental build pipeline, create a
clean build. The most common reason for this is when you implement or make
changes to build process callbacks that affect assets.

Since the build process can’t know how a callback you’ve implemented affects
an asset, it can’t determine how to rebuild the asset. Unity only regenerates
files if the file’s dependencies change. This means if the callback modifies a
file that Unity generates, and the file’s dependencies don’t change, the
callback can apply modifications to an already modified file. For example, if
the callback adds new entries to an [Android App Manifest](android-
manifest.html), and the dependencies for the Android App Manifest don’t
change, the callback still adds the new entries, which results in an invalid
file.

If you change a callback or its input data and you want Unity to rebuild
assets that the callback affects, create a clean build. Examples of callbacks
include:

  * [PostProcessSceneAttribute](../ScriptReference/Callbacks.PostProcessSceneAttribute.html)
  * [IPreprocessShaders.OnProcessShader](../ScriptReference/Build.IPreprocessShaders.OnProcessShader.html)
  * [IPreprocessComputeShaders.OnProcessComputeShader](../ScriptReference/Build.IPreprocessComputeShaders.OnProcessComputeShader.html)

**Note** : If you make changes to an asset, Unity rebuilds that asset when it
builds the application. This also includes processing any callback that
affects it which means you don’t need to create a clean build if you make
changes to an asset, only if you make changes to a build process callback.

[](build-profiles-reference.html)

Build Profiles window reference

[](comp-ManagerGroup.html)

Project Settings

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

