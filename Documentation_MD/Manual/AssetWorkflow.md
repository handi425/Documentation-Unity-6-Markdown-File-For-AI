[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetWorkflow.html)
  * [中文](/cn/current/Manual/AssetWorkflow.html)
  * [日本語](/ja/current/Manual/AssetWorkflow.html)
  * [한국어](/kr/current/Manual/AssetWorkflow.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetWorkflow.html)
  * [中文](/cn/current/Manual/AssetWorkflow.html)
  * [日本語](/ja/current/Manual/AssetWorkflow.html)
  * [한국어](/kr/current/Manual/AssetWorkflow.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * Asset workflow

[](assets-and-media.html)

Assets and media

[](ImportingAssets.html)

Importing assets

# Asset workflow

An asset is any item that you use in your Unity project to create your game or
app. Assets can represent visual or audio elements in your project, such as 3D
models, textures, **sprites** A 2D graphic objects. If you are used to working
in 3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite), sound effects, or music. Assets can
also represent more abstract items such as color gradients, animation masks,
or arbitrary text or numeric data for any use.

An asset might come from a file created outside of Unity, such as a 3D Model,
an audio file, or an image. You can also create some types of asset in the
Unity Editor, such as a ProBuilder **Mesh** The main graphics primitive of
Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), an **Animator Controller** Controls
animation through Animation Layers with Animation State Machines and Animation
Blend Trees, controlled by Animation Parameters. The same Animator Controller
can be referenced by multiple models with Animator components. [More
info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController), an Audio Mixer, or a
**Render Texture** A special type of Texture that is created and updated at
runtime. To use them, first create a new Render Texture and designate one of
your Cameras to render into it. Then you can use the Render Texture in a
Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture).

## Import, Create, Build, Distribute, Load

![Asset workflow in Unity](../uploads/Main/AssetWorkflowOverview.svg) Asset
workflow in Unity

The above diagram shows the typical workflow when you work with assets in
Unity. Each column represents a separate step and is described below:

  * **Import** assets into the Unity Editor
  * **Create** content using the Unity Editor with those assets.
  * **Build** your app or game file, and optionally its accompanying content bundles
  * **Distribute** the built files so that your users can access them, via a publisher, or an app store
  * **Load** further updates as necessary at runtime, depending on your user’s behavior, and how you have grouped and bundled your content.

### Import

Importing is the process of bringing your source files into the Unity Editor
to work with. When you save or copy a file into your project’s `Assets`
folder, Unity imports that file which allows you to work with it in the
Editor.

It’s important to learn some fundamentals of importing assets into Unity, such
as where the files are stored in your Project, how to adjust the Import
Settings for each kind of asset, what the meta files are for, and how the
Asset Database stores imported data. See [Importing
Assets](ImportingAssets.html) for more detail about these topics.

You can speed up Unity’s processing of assets when working with teams by using
[Unity Accelerator](UnityAccelerator.html).

### Create

Once you have imported some assets into your project, you can start creating
your game or app. This typically involves placing assets into one or more
[Scenes](CreatingScenes.html)A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), and adding
[scripts](scripting.html)A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) which control how the user interacts
with them.

As development on your project grows, you might need to split your assets up
into separate groups which allows your game to incrementally download selected
extra content at runtime.

During the creation process, you can decide a strategy on how to group your
assets into separate **bundles** , and implement the code for choosing when to
load them.

Grouping your assets into bundles allows you reduce the size of your initial
download and load some assets later at runtime. This can help you optimize the
download size and memory usage of your game or app. The recommended way to do
this is to use Unity’s [Addressables](com.unity.addressables.html) system.

### Build

Building refers to the process of exporting your completed project to binary
files which you can then distribute and run on the platform of your choice.
For example, when building for Windows, Unity generates an `.EXE` file, along
with some accompanying data files which you can then distribute.

If you’re using Addressables or Asset Bundles to group your assets into
separate downloadable bundles you also need to build those bundle files for
distribution.

You can build your project on your own computer, or you can use Unity’s [Build
Automation service](https://docs.unity.com/ugs/en-
us/manual/devops/manual/unity-build-automation) which provides automated build
generation and continuous integration for your Unity projects.

### Distribute

Once you have built your game or app and its content bundles, your users need
a way to access it. Your choice of distribution method depends on the
platforms that you’re targeting.

For example, mobile platforms have their own app stores, you could use a
professional publisher, or you could self-host on your own servers.

Unity offers its own [Cloud Content Delivery](https://docs.unity.com/ugs/en-
us/manual/ccd/manual/UnityCCD) service, allowing you to host and deliver your
game or app and its content to your users, and is fully integrated into the
Unity development platform. This can save lots of time and is valuable for
content-rich, live games or applications that require content updates on a
regular basis.

### Load

When users load and use your game or app, the loading process and experience
is defined by the rules and programming that you set up, and the way that you
grouped and bundled your assets.

Using a combination of the techniques and services described here, you can
provide fast initial downloads, and ongoing updates and extra content which
you can roll out over the lifetime of your project.

* * *

## Artist workflow benefits

Unity’s asset workflow has tools and features which make it easy to edit and
design directly in the Unity Editor:

  * Support for many different [file formats](BuiltInImporters.html)
  * [Quick roundtripping](ImportingAssets.html) between Unity and third-party tools
  * [Presets](Presets.html) to apply custom default settings for types of assets
  * Update live content seamlessly using [Addressables](com.unity.addressables.html) and [Cloud Content Delivery](https://docs.unity.com/ugs/en-us/manual/ccd/manual/UnityCCD)

## Programmer workflow benefits

  * A tailored content pipeline (for example, you can write scripts to process assets as Unity imports them, or to control which presets Unity automatically applies based on your own rules).
  * [Modify source assets](ModifyingSourceAssetsThroughScripting.html) through scripting. You can adjust source assets such as materials, meshes or physics through your game code.
  * Save memory using the [Addressable assets system](com.unity.addressables.html), which simplifies content management for complex projects, and provides automatic memory management and profiling tools.
  * Optimize assets for target platforms. When you’re making a multi-platform project, you might have hundreds of different textures, which all need to be packaged at different resolutions for different platforms. Unity packages, resizes and recompresses your assets automatically when you build to each target platform.

## Workflow considerations

When working with assets in Unity there are different strategies you can use.
Which one suits your project depends on factors such as the size of your team,
the size of your project, your target platforms, the memory availability on
those platforms, and whether you want to release updates, patches, and DLC
after publishing it.

For example, if you are working in a team, you could use a [Cache
Server](UnityAccelerator.html) alongside your **version control** A system for
managing file changes. You can use Unity in conjunction with most common
version control tools, including Perforce, Git, Mercurial and PlasticSCM.
[More info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) system to cache Unity’s import
results, to save time across the team.

If you are working with a large number of assets that you want to publish as
separate bundles, you might find it useful to separate some of those groups of
assets out into separate projects, so that members of your team don’t need to
load a single huge project to work on those bundles.

## Platform considerations

If you keep all your assets in a single project, Unity automatically builds
them in the correct format for the current selected platform when you run a
build. However, if you split your assets across multiple projects to build
your bundles separately, you must make a build for each platform you support.
See the Addressables documentation [Building for multiple
platforms](https://docs.unity3d.com/Packages/com.unity.addressables@latest?subfolder=/manual/AddressableAssetsGettingStarted.html%23building-
for-multiple-platforms) for more information.

The characteristics of a platform also determine the restrictions and
possibilities of how you organize your runtime assets. For example, on the
standalone platforms (PC or macOS), virtual memory provides an almost
unbounded pool of memory, so using the [Resources
folder](UnderstandingPerformanceResourcesFolder.html) or large asset bundles
doesn’t typically pose a memory challenge. Conversely, mobile devices and
console platforms typically have limited or nonexistent virtual memory, so
apps built for those platforms must manage asset loading and unloading more
efficiently.

User expectations on a platform are also an important consideration. For
example, on mobile platforms, a long initial download and install process can
lead to players abandoning your app before they ever play it. For this reason,
it’s common for mobile apps to include only a minimal set of assets in the
initial build and to download the remaining assets from a remote server the
first time the user runs your app.

[](assets-and-media.html)

Assets and media

[](ImportingAssets.html)

Importing assets

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

