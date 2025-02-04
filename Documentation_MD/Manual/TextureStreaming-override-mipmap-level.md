[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TextureStreaming-override-mipmap-level.html)
  * [中文](/cn/current/Manual/TextureStreaming-override-mipmap-level.html)
  * [日本語](/ja/current/Manual/TextureStreaming-override-mipmap-level.html)
  * [한국어](/kr/current/Manual/TextureStreaming-override-mipmap-level.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TextureStreaming-override-mipmap-level.html)
  * [中文](/cn/current/Manual/TextureStreaming-override-mipmap-level.html)
  * [日本語](/ja/current/Manual/TextureStreaming-override-mipmap-level.html)
  * [한국어](/kr/current/Manual/TextureStreaming-override-mipmap-level.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Optimizing GPU texture memory with mipmap streaming](TextureStreaming.html)
  * Override the mipmap level of a texture

[](TextureStreaming-configure.html)

Configure mipmap streaming

[](TextureStreaming-preload.html)

Preload mipmap levels

# Override the mipmap level of a texture

You configure Unity to override the mipmap level of a texture using the
following:

  * The **Priority** property in the **Texture Import Settings** window of the texture.
  * The [Texture2D.requestedMipmapLevel](../ScriptReference/Texture2D-requestedMipmapLevel.html) API.

## Use the Priority property

Follow these steps:

  1. Select the texture asset in the **Project** window.
  2. In the **Texture Import Settings** window, in the **Advanced** section, set a **Priority** value between –128 and 127.

When Unity needs to reduce mipmap levels to meet the memory limit, it
considers textures in priority order from low to high until it meets the
limit. This means textures with a higher priority value are more likely to
keep their higher-resolution mipmap levels.

Unity removes a mipmap level of a lower-priority texture every time it
considers textures at that priority or higher. For example, if you set one
texture to a **Priority** of 1 and another texture to a **Priority** of 5,
Unity might remove four mipmap levels before it considers the second texture.

You can also use the following APIs to set the **Priority** value:

  * [TextureImporter.streamingMipmapsPriority](../ScriptReference/TextureImporter-streamingMipmapsPriority.html)
  * [Texture2D.streamingMipmapsPriority](../ScriptReference/Texture2D-streamingMipmapsPriority.html)
  * [IHVImageFormatImporter.streamingMipmapsPriority](../ScriptReference/IHVImageFormatImporter-streamingMipmapsPriority.html)

## Use the API

Use the following APIs:

  * [Texture2D.requestedMipmapLevel](../ScriptReference/Texture2D-requestedMipmapLevel.html) to request that Unity overrides the mipmap level of the texture.
  * [Texture2D.IsRequestedMipmapLevelLoaded](../ScriptReference/Texture2D.IsRequestedMipmapLevelLoaded.html) to check if Unity loads your requested mipmap level.
  * [Texture2D.ClearRequestedMipmapLevel](../ScriptReference/Texture2D.ClearRequestedMipmapLevel.html) if you no longer want to override the mipmap level.

You can use the `Mesh.GetUVDistributionMetric` API to get an estimate of the
UV density of a **mesh** The main graphics primitive of Unity. Meshes make up
a large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh). This helps you calculate the mipmap
level you need, based on the position of the **camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). For example code, refer to
[Mesh.GetUVDistributionMetric](../ScriptReference/Mesh.GetUVDistributionMetric.html).

### Override mipmap levels on all textures

Use [Texture.streamingTextureForceLoadAll](../ScriptReference/Texture-
streamingTextureForceLoadAll.html) to load all mipmap levels for all textures.

## Additional resources

  * [TextureImporter.streamingMipmaps](../ScriptReference/TextureImporter-streamingMipmaps.html)
  * [IHVImageFormatImporter.streamingMipmaps](../ScriptReference/IHVImageFormatImporter-streamingMipmaps.html)

[](TextureStreaming-configure.html)

Configure mipmap streaming

[](TextureStreaming-preload.html)

Preload mipmap levels

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

