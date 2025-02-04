[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TextureStreaming-use.html)
  * [中文](/cn/current/Manual/TextureStreaming-use.html)
  * [日本語](/ja/current/Manual/TextureStreaming-use.html)
  * [한국어](/kr/current/Manual/TextureStreaming-use.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TextureStreaming-use.html)
  * [中文](/cn/current/Manual/TextureStreaming-use.html)
  * [日本語](/ja/current/Manual/TextureStreaming-use.html)
  * [한국어](/kr/current/Manual/TextureStreaming-use.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Optimizing GPU texture memory with mipmap streaming](TextureStreaming.html)
  * Enable mipmap streaming

[](TextureStreaming-introduction.html)

Introduction to mipmap streaming

[](TextureStreaming-configure.html)

Configure mipmap streaming

# Enable mipmap streaming

To enable mipmap streaming, follow these steps:

  1. Go to **Edit** > **Project Settings** > **Quality**.
  2. In the **Textures** section, enable **Mipmap Streaming**.

By default, this enables mipmap streaming for all the **cameras** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) in your project.

In the Editor, mipmap streaming is active in both Edit mode and Play mode by
default. For more information about configuring mipmap streaming in the
Editor, refer to [Editor settings](class-EditorManager.html)

## Make a texture work with mipmap streaming

Follow these steps:

  1. Select a texture asset in the **Project** window.
  2. In the **Texture Import Settings** window, select **Advanced** to open advanced settings.
  3. Ensure that **Generate Mipmap** is enabled.
  4. Enable **Stream Mipmap Levels**.

If you build your project for Android, you must also follow these steps:

  1. Open the [**Build Profiles**](build-profiles.html) window.
  2. Set ****Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) Method** to **LZ4** or **LZ4HC**.

### Lightmaps

To enable mipmap streaming for **lightmaps** A pre-rendered texture that
contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), follow these steps:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In the **Other Settings** section, enable **Lightmap Streaming**.

You can edit the mipmap streaming settings of the lightmap assets in the same
way that you can edit settings of any other texture, but they reset to their
default values when Unity regenerates the lightmaps. To solve this, you can
tell Unity to apply these values when it generates the lightmaps. Use the
**Lightmap Streaming Enabled** and **Streaming Priority** in the [Player
settings window](class-PlayerSettings.html).

### Custom meshes

If you create a custom **mesh** The main graphics primitive of Unity. Meshes
make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) in a Unity script, Unity doesn’t
automatically calculate the UV density of the mesh. This means Unity loads the
wrong mipmap levels.

To prevent this, do either of the following:

  * Use the [Mesh.RecalculateUVDistributionMetrics](../ScriptReference/Mesh.RecalculateUVDistributionMetrics.html) API to manually calculate the UV density of the mesh after you create it.
  * [Import the mesh as a model file](ImportingModelFiles.html) instead.

### Objects that don’t have a standard Renderer component

Unity can’t calculate the correct mipmap level for the following objects,
because they don’t use a standard [Renderer](../ScriptReference/Renderer.html)
component:

  * [Decals](visual-effects-decals.html) textures.
  * [Reflection Probe](ReflectionProbes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) textures, because they use
mipmap levels to store lookup tables for material roughness.

  * **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite), which use a [Sprite
Renderer](sprite/renderer/renderer-landing.html)A component that lets you
display images as Sprites for use in both 2D and 3D scenes. [More
info](sprite/renderer/renderer-landing.html)  
See in [Glossary](Glossary.html#SpriteRenderer) component.

  * **Shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that use UV texture coordinates in a
channel other than [Mesh.uv](../ScriptReference/Mesh-uv.html) (also called
UV0).

  * Shaders that change texture coordinates other than scale and translation.

For these objects, use the
[Texture2D.requestedMipmapLevel](../ScriptReference/Texture2D-requestedMipmapLevel.html)
API to override mipmap streaming and set mipmap levels manually. If you don’t
do this, Unity uses low-resolution mipmap levels, which might display as
blurry depending on the distance from the camera.

## Additional resources

  * [Texture2D.streamingMipmaps](../ScriptReference/Texture2D-streamingMipmaps.html)
  * [SystemInfo.supportsMipStreaming](../ScriptReference/SystemInfo-supportsMipStreaming.html)

[](TextureStreaming-introduction.html)

Introduction to mipmap streaming

[](TextureStreaming-configure.html)

Configure mipmap streaming

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

