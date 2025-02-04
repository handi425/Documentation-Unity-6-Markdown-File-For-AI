[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ReducingFilesize.html)
  * [中文](/cn/current/Manual/ReducingFilesize.html)
  * [日本語](/ja/current/Manual/ReducingFilesize.html)
  * [한국어](/kr/current/Manual/ReducingFilesize.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ReducingFilesize.html)
  * [中文](/cn/current/Manual/ReducingFilesize.html)
  * [日本語](/ja/current/Manual/ReducingFilesize.html)
  * [한국어](/kr/current/Manual/ReducingFilesize.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * Reducing the file size of your build

[](OpenGLCoreDetails.html)

OpenGL Core

[](BuildPlayerPipeline.html)

Build Player Pipeline

# Reducing the file size of your build

Keeping the file size of the built app to a minimum is important, especially
for mobile devices or for app stores that impose a size limit. The first step
in reducing the size is to determine which Assets contribute most to it,
because these Assets are the most likely candidates for optimization. This
information is available in the Editor Log just after you have performed the
build. Go to the Console window (menu: **Window** > **General** > **Console**
Abbreviation of **game console**  
See in [Glossary](Glossary.html#console)), click the small drop-down panel in
the top right, and select **Open Editor Log**.

![The Editor Log just after a build](../uploads/Main/FileSizeOptimization.png)
The Editor Log just after a build

The Editor Log provides a summary of Assets broken down by type, and then
lists all the individual Assets in order of size contribution. Typically,
things like Textures, Sounds and Animations take up the most storage, while
**Scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), Levels and **Shaders** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) usually have the smallest impact. The
**File headers** mentioned in the list are not Assets - they are actually the
extra data that is added to “raw” Asset files to store references and
settings. The headers normally make very little difference to Asset size, but
the value might be large if you have numerous large Assets in the Resources
folder.

The Editor Log helps you identify Assets that you might want to remove or
optimize, but you should consider the following before you start:

  * Unity re-codes imported Assets into its own internal formats, so the choice of source Asset type is not relevant. For example, if you have a multi-layer Photoshop Texture in the Project, it is flattened and compressed before building. Exporting the Texture as a .png file does not make any difference to build size, so you should stick to the format that is most convenient for you during development.

  * Unity strips most unused Assets during the build, so you don’t gain anything by manually removing Assets from the Project. The only Assets that are not removed are scripts (which are generally very small anyway) and Assets in the Resources folder (because Unity can’t determine which of these are needed and which are not). With this in mind, you should make sure that the only Assets in the Resources folder are the ones you need for the game. You might be able to replace Assets in the Resources folder with [AssetBundles](AssetBundlesIntro.html) \- this means that Unity loads Assets dynamically, thereby reducing the player size.

## Suggestions for reducing build size

### Textures

Textures usually take up the most space in the build. The first solution to
this is to use compressed **Texture formats** A file format for handling
textures during real-time rendering by 3D graphics hardware, such as a
graphics card or mobile device. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat). See documentation on
[platform-specific Texture compression](class-TextureImporterOverride) for
more information.

If that doesn’t reduce the file size enough, try to reduce the physical size
(in pixels) of the Texture images. To do this without modifying the actual
source content, select the Texture in the Project view, and in the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window reduce the **Max Size**. To
see how this looks in-game, zoom in on a **GameObject** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that uses the Texture, then adjust
the **Max Size** until it starts looking worse in the **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view. Changing the maximum Texture size
does not affect your Texture Asset, just its resolution in the game.

![Changing the Maximum Texture Size does not affect your Texture Asset, just
its resolution in the game](../uploads/Main/FileSizeOptimizationTexture.png)
Changing the Maximum Texture Size does not affect your Texture Asset, just its
resolution in the game

By default, Unity compresses all Textures when importing. For faster workflow
in the Editor, go to **Unity** < **Preferences** and untick the checkbox for
**Compress Assets on Import**. All Textures are compressed in the build,
regardless of this setting.

### Meshes and Animations

You can compress [Meshes](class-Mesh.html) and imported Animation Clips so
that they take up less space in your game file. To enable **Mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) **compression** A method of storing data
that reduces the amount of storage space it requires. See [Texture
Compression](class-TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression), select the Mesh, then in the
Inspector window set the **Mesh Compression** to **Low** , **Medium** or
**High**. Mesh and **Animation compression** The method of compressing
animation data to significantly reduce file sizes without causing a noticeable
reduction in motion quality. Animation compression is a trade off between
saving on memory and image quality. [More info](class-
AnimationClip.html#AssetProperties)  
See in [Glossary](Glossary.html#animationcompression) uses quantization, which
means it takes less space, but the compression can introduce some
inaccuracies. Experiment with what level of compression is acceptable for your
models.

Note that Mesh compression only produces smaller data files, and does not use
less memory at run time. Animation **keyframe** A frame that marks the start
or end point of a transition in an animation. Frames in between the keyframes
are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) reduction produces smaller data
files and uses less memory at run time; generally you should always have it
enabled. See documentation on [Animation Clips](class-
AnimationClip.html)Animation data that can be used for animated characters or
simple animations. It is a simple “unit” piece of motion, such as (one
specific instance of) “Idle”, “Walk” or “Run”. [More info](class-
AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) for more information about
this.

### Reducing .NET library size

Unity supports two .NET API compatibility levels.: .NET 4.x and .NET Standard
2.0. The .NET Standard 2.0 restricts you to a smaller subset of the .NET API,
which can help keep size down.

[](OpenGLCoreDetails.html)

OpenGL Core

[](BuildPlayerPipeline.html)

Build Player Pipeline

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

