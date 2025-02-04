[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TextureStreaming-configure.html)
  * [中文](/cn/current/Manual/TextureStreaming-configure.html)
  * [日本語](/ja/current/Manual/TextureStreaming-configure.html)
  * [한국어](/kr/current/Manual/TextureStreaming-configure.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TextureStreaming-configure.html)
  * [中文](/cn/current/Manual/TextureStreaming-configure.html)
  * [日本語](/ja/current/Manual/TextureStreaming-configure.html)
  * [한국어](/kr/current/Manual/TextureStreaming-configure.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Optimizing GPU texture memory with mipmap streaming](TextureStreaming.html)
  * Configure mipmap streaming 

[](TextureStreaming-use.html)

Enable mipmap streaming

[](TextureStreaming-override-mipmap-level.html)

Override the mipmap level of a texture

# Configure mipmap streaming

## Set which cameras use mipmap streaming

By default, all **cameras** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) in your **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) use mipmap streaming when you enable
it.

### Disable mipmap streaming on a single camera

Follow these steps:

  1. Select a camera in your scene.
  2. In the **Inspector** window, select **Add Component** > **Streaming Controller**.
  3. Disable the **Streaming Controller** component.

### Enable mipmap streaming on a single camera

Follow these steps:

  1. Go to **Edit** > **Project Settings** > **Quality**.
  2. In the **Textures** section, under **Mipmap Streaming** , disable **Add All Cameras**.
  3. Add a **Streaming Controller** component to the camera, and make sure it’s enabled.

## Set which mipmap levels a camera uses

Use the **Mipmap Bias** setting in a **Streaming Controller** component to
force Unity to load smaller or larger mipmap levels than the ones mipmap
streaming automatically chooses.

Unity adds the **Mipmap Bias** value to mipmap levels from textures in the
camera view. For example, if you set **Mipmap Bias** to 2 and mipmap streaming
chooses mipmap level 1 for a texture, Unity loads mipmap level 3 (1 + 2).

You can also use the
[StreamingController.streamingMipmapBias](../ScriptReference/StreamingController-
streamingMipmapBias.html) API to control this setting.

## Set the memory budget for textures

To set the maximum GPU memory that Unity uses for textures, follow these
steps:

  1. Go to **Edit** > **Project Settings** > **Quality**.
  2. In the **Textures** section, set the **Memory Budget** value in MB.

The memory budget is for both mipmap streaming, and all the mipmap levels of
textures that don’t use mipmap streaming. For example, if you set **Memory
Budget** to 100 MB, and you have 90 MB of textures that don’t use mipmap
streaming, the memory budget for mipmap streaming is 10 MB.

To avoid exceeding the memory budget, Unity does the following:

  * Loads lower-resolution mipmap levels for textures. This can cause textures to pop or load slowly.
  * Removes unused mipmap levels from GPU memory, to make room for mipmap levels it needs.

You can use the **Max Level Reduction** property to stop Unity removing mipmap
levels smaller than a certain level. This value is also the mipmap level Unity
loads at first startup. For example, if you set **Max Level Reduction** to 2,
Unity loads only mipmap levels at level 2 and larger, and keeps them in
memory.

Unity must keep mipmap levels above the **Max Level Reduction** value in GPU
memory. This might mean Unity exceeds the memory budget.

### Estimate a memory budget

To estimate a memory budget for your project, follow these steps:

  1. While your project runs, use the [Texture.desiredTextureMemory](../ScriptReference/Texture-desiredTextureMemory.html) API to get the total size of the textures Unity loads.
  2. Set **Memory Budget** to slightly higher than that value.

This lets you make sure Unity has enough texture memory available for the most
resource-intensive areas of your scene, and prevent textures from dropping to
a lower resolution. If you have extra memory available, you can set a larger
memory budget so that Unity can keep texture data that’s not visible in your
scene in a GPU cache.

**Note:** If you use `Texture.desiredTextureMemory` in the Editor, the total
size might include textures Unity uses to render Editor windows.

### Set the memory budget at runtime

You can use the following APIs to set and control the memory budget at
runtime:

  * [QualitySettings](../ScriptReference/QualitySettings.html), for example `QualitySettings.streamingMipmapsActive`.
  * [Texture2D.streamingTextureDiscardUnusedMips](../ScriptReference/Texture-streamingTextureDiscardUnusedMips.html)

[](TextureStreaming-use.html)

Enable mipmap streaming

[](TextureStreaming-override-mipmap-level.html)

Override the mipmap level of a texture

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

