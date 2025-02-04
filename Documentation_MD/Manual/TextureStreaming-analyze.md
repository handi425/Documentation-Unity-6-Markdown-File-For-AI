[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TextureStreaming-analyze.html)
  * [中文](/cn/current/Manual/TextureStreaming-analyze.html)
  * [日本語](/ja/current/Manual/TextureStreaming-analyze.html)
  * [한국어](/kr/current/Manual/TextureStreaming-analyze.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TextureStreaming-analyze.html)
  * [中文](/cn/current/Manual/TextureStreaming-analyze.html)
  * [日本語](/ja/current/Manual/TextureStreaming-analyze.html)
  * [한국어](/kr/current/Manual/TextureStreaming-analyze.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Optimizing GPU texture memory with mipmap streaming](TextureStreaming.html)
  * Analyze mipmap streaming

[](TextureStreaming-preload.html)

Preload mipmap levels

[](SparseTextures.html)

Sparse Textures

# Analyze mipmap streaming

The ****Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)** view has a Debug Draw Mode that helps
you visualize and debug [mipmap streaming](TextureStreaming.html) in your
scene. To enable it, follow these steps:

  1. Select **Debug Draw Mode** in the [Scene view View Options overlay](ViewModes.html).
  2. Select **Texture Mipmap Streaming**.

The Debug Draw Mode tints **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) the following colours:

  * Green if a texture uses fewer mipmap levels.
  * Red if a texture uses fewer mipmap levels because mipmap streaming doesn’t have enough resources to load them all.
  * Blue if a texture that doesn’t use mipmap streaming, or there’s no renderer calculating the mipmap levels.

**Note:** If you use the [MainTexture](../ScriptReference/Material-
mainTexture.html) API to set a main texture, the texture won’t display in the
Debug Draw Mode.

If your project uses a scriptable **render pipeline** A series of operations
that take the contents of a Scene, and displays them on a screen. Unity lets
you choose from pre-built render pipelines, or write your own. [More
info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), use the following to analyze
mipmap streaming instead:

  * [Rendering Debugger in URP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.0/manual/features/rendering-debugger)
  * [Rendering Debugger in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/rendering-debugger-window-reference)

## Get mipmap streaming information in a script

To get information about texture memory, use the following properties:

  * [Texture.currentTextureMemory](../ScriptReference/Texture-currentTextureMemory.html)
  * [Texture.desiredTextureMemory](../ScriptReference/Texture-desiredTextureMemory.html)
  * [Texture.totalTextureMemory](../ScriptReference/Texture-totalTextureMemory.html)
  * [Texture.targetTextureMemory](../ScriptReference/Texture-targetTextureMemory.html)
  * [Texture.nonStreamingTextureMemory](../ScriptReference/Texture-nonStreamingTextureMemory.html)

To get information about the number of textures or renderers that mipmap
streaming affects, use the following properties:

  * [Texture.streamingMipmapUploadCount](../ScriptReference/Texture-streamingMipmapUploadCount.html)
  * [Texture.nonStreamingTextureCount](../ScriptReference/Texture-nonStreamingTextureCount.html)
  * [Texture.streamingTextureCount](../ScriptReference/Texture-streamingTextureCount.html)
  * [Texture.streamingRendererCount](../ScriptReference/Texture-streamingRendererCount.html)

To get information about the mipmap levels for a texture, use the following
properties:

  * [Texture2D.desiredMipmapLevel](../ScriptReference/Texture2D-desiredMipmapLevel.html)
  * [Texture2D.loadingMipmapLevel](../ScriptReference/Texture2D-loadingMipmapLevel.html)
  * [Texture2D.loadedMipmapLevel](../ScriptReference/Texture2D-loadedMipmapLevel.html)

[](TextureStreaming-preload.html)

Preload mipmap levels

[](SparseTextures.html)

Sparse Textures

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

