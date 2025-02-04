[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TextureStreaming-preload.html)
  * [中文](/cn/current/Manual/TextureStreaming-preload.html)
  * [日本語](/ja/current/Manual/TextureStreaming-preload.html)
  * [한국어](/kr/current/Manual/TextureStreaming-preload.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TextureStreaming-preload.html)
  * [中文](/cn/current/Manual/TextureStreaming-preload.html)
  * [日本語](/ja/current/Manual/TextureStreaming-preload.html)
  * [한국어](/kr/current/Manual/TextureStreaming-preload.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Optimizing GPU texture memory with mipmap streaming](TextureStreaming.html)
  * Preload mipmap levels

[](TextureStreaming-override-mipmap-level.html)

Override the mipmap level of a texture

[](TextureStreaming-analyze.html)

Analyze mipmap streaming

# Preload mipmap levels

If you enable a **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) at runtime, mipmap streaming needs
time to stream the mipmap levels into memory.

You can use texture preloading to prevent this. Do the following:

  1. Add a **Streaming Controller** component to the disabled camera. For more information about this component, refer to [Configure mipmap streaming](TextureStreaming-configure.html).
  2. Call the [StreamingController.SetPreloading](../ScriptReference/StreamingController.SetPreloading.html) API on the camera to preload the mipmap levels.

Use
[StreamingController.CancelPreloading](../ScriptReference/StreamingController.CancelPreloading.html)
to cancel preloading.

You can use the following APIs after you enable preloading:

  * [StreamingController.IsPreloading](../ScriptReference/StreamingController.IsPreloading.html) to check if the camera is preloading.
  * [Texture.streamingTextureLoadingCount](../ScriptReference/Texture-streamingTextureLoadingCount.html) and [Texture.streamingTexturePendingLoadCount](../ScriptReference/Texture-streamingTexturePendingLoadCount.html) to check how many textures Unity is still loading mipmap levels for.

If these APIs return values that indicate Unity has finished preloading, you
might need to wait a few frames before you enable the camera to make sure
preloading has finished.

[](TextureStreaming-override-mipmap-level.html)

Override the mipmap level of a texture

[](TextureStreaming-analyze.html)

Analyze mipmap streaming

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

