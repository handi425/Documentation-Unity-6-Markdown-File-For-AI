[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetBundles-Preparing.html)
  * [中文](/cn/current/Manual/AssetBundles-Preparing.html)
  * [日本語](/ja/current/Manual/AssetBundles-Preparing.html)
  * [한국어](/kr/current/Manual/AssetBundles-Preparing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetBundles-Preparing.html)
  * [中文](/cn/current/Manual/AssetBundles-Preparing.html)
  * [日本語](/ja/current/Manual/AssetBundles-Preparing.html)
  * [한국어](/kr/current/Manual/AssetBundles-Preparing.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [AssetBundles](AssetBundlesIntro.html)
  * Preparing Assets for AssetBundles

[](AssetBundles-Workflow.html)

AssetBundle workflow

[](AssetBundles-Dependencies.html)

AssetBundle Dependencies

# Preparing Assets for AssetBundles

When defining AssetBundles there are a few rules to be aware of:

  * **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and Assets can’t be included together
in the same AssetBundle. An individual AssetBundle can only contain _either_
Scenes _or_ Assets.

  * A specific Scene or Asset can’t be assigned to more than one AssetBundle
  * AssetBundles can’t contain Script assets
  * Files inside the StreamingAssets folder cannot be put in an AssetBundle
  * The AssetBundle name cannot match the name of the output folder
  * An AssetBundle can only be loaded on the specific platform that it was built for.
  * The Editor can load any AssetBundle, regardless of the current active [platform profile](build-profiles.html). However individual Assets inside an AssetBundle may not load or render successfully if they use a platform specific-format that is not supported on your Editor’s platform. For example, Android **shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) may render as magenta in the Windows
Editor.

Beyond those rules you are free to assign any asset to any bundle you desire.
However, there are certain strategies to consider when setting up your
bundles.

## Logical Entity Grouping

Logical Entity Grouping is a strategy you can use to decide how to organize
what goes into each of your project’s AssetBundles. The principle is to base
your decisions on the functional portion of the project that each piece of
content represents. This includes sections such as User-Interface, characters,
environments, and anything else that may appear frequently throughout the
lifetime of the application.

### Examples

  * Bundling all the textures and layout data for a User-Interface screen
  * Bundling all the models and animations for a character/set of characters
  * Bundling the textures and models for pieces of the scenery shared across multiple levels

Organizing your AssetBundles by Logical Entity Grouping is ideal for
downloadable content (DLC), because it allows you to more easily make small
changes to your project which don’t require your users to re-download large
amounts of additional, unchanged, assets.

The biggest trick to being able to properly implement this strategy is that
the developer assigning assets to their respective bundles must be familiar
with precisely when and where each asset will be used by the project.

## Type Grouping

Type Grouping is a strategy where you assign assets of similar type, such as
audio tracks or language localization files, to a single AssetBundle.

Type grouping can be useful to establish AssetBundles that change rarely.
Grouping AssetBundles this way may result in fewer AssetBundles changing and
requiring distribution when an incremental build is done. The downside is that
more AssetBundles may need to be downloaded and loaded to assemble all
dependent objects together at runtime.

## Concurrent Content Grouping

Concurrent Content Grouping is the idea that you will bundle assets together
that will be loaded and used at the same time. You could think of these types
of bundles as being used for a level based game where each level contains
totally unique characters, textures, music, etc. You would want to be
absolutely certain that an asset in one of these AssetBundles is only used at
the same time the rest of the assets in that bundle are going to be used.
Having a dependency on a single asset inside a Concurrent Content Grouping
bundle would result in significant increased load times. You would be forced
to download the entire bundle for that single asset.

The most common use-case for Concurrent Content Grouping bundles is for
bundles that are based on scenes. In this assignment strategy, each scene
bundle should contain most or all of that scenes dependencies.

**Note:** When building an AssetBundle containing a Scene, any Assets
referenced by that Scene will also be automatically included in the
AssetBundle, unless those Assets are explicitly assigned to a different
AssetBundle. This is convenient when doing Concurrent Content Grouping, but
you need to keep an eye out for duplicated assets if any referenced assets are
also used by other scenes that you are building into separate AssetBundles.

## Additional Tips

A project absolutely can and should mix these strategies as your needs
require. Using the optimal asset assignment strategy for any given scenario
greatly increases efficiency for any project.

For example, a project may decide to group its User-Interface (UI) elements
for different platforms into their own Platform-UI specific bundle but group
its interactive content by level/scene.

Regardless of the strategy you follow, here are some additional tips that are
good to keep in mind across the board:

  * Split frequently updated objects into AssetBundles separate from objects that rarely change
  * Group objects that are likely to be loaded simultaneously. Such as a model, its textures, and its animations
  * If you notice multiple objects across multiple AssetBundles are dependant on a single asset from a completely different AssetBundle, move the dependency to a separate AssetBundle. If several AssetBundles are referencing the same group of assets in other AssetBundles, it may be worth pulling those dependencies into a shared AssetBundle to reduce duplication.
  * If two sets of objects are unlikely to ever be loaded at the same time, such as Standard and High Definition assets, be sure they are in different AssetBundles.
  * Consider splitting apart an AssetBundle if less than 50% of that bundle is ever frequently loaded at the same time
  * Consider combining AssetBundles that are small but whose content is frequently loaded simultaneously
  * If a group of objects are simply different versions of the same object, consider AssetBundle Variants

[](AssetBundles-Workflow.html)

AssetBundle workflow

[](AssetBundles-Dependencies.html)

AssetBundle Dependencies

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

