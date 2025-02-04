[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-memory.html)
  * [中文](/cn/current/Manual/shader-memory.html)
  * [日本語](/ja/current/Manual/shader-memory.html)
  * [한국어](/kr/current/Manual/shader-memory.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-memory.html)
  * [中文](/cn/current/Manual/shader-memory.html)
  * [日本語](/ja/current/Manual/shader-memory.html)
  * [한국어](/kr/current/Manual/shader-memory.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Troubleshooting shaders](shader-troubleshooting.html)
  * [Reducing the size or number of shaders](shader-reducing.html)
  * Control how much memory shaders use

[](avoid-shader-duplication.html)

Troubleshooting shader duplication from AssetBundles

[](shader-debugging.html)

Debugging shaders

# Control how much memory shaders use

In your built application, Unity stores several ‘chunks’ of compressed
**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) variant data. Each chunk contains
multiple shader variants. When Unity loads a **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) at runtime, it loads all the scene’s
chunks into CPU memory and decompresses them.

To reduce memory usage on platforms that have limited memory, you can limit
the size of chunks and how many decompressed chunks Unity keeps in memory.

To do this, in [Player settings](class-PlayerSettings.html)Settings that let
you set various player-specific options for the final game built by Unity.
[More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings), select **Other Settings** >
**Shader Variant Loading** and adjust the following settings:

  * Use **Default chunk size (MB)** to set the maximum size of compressed chunks Unity stores in your built application.
  * Use **Default chunk count** to limit how many decompressed chunks Unity keeps in memory. The default is `0`, which means there’s no limit.

See
[PlayerSettings.SetDefaultShaderChunkCount](../ScriptReference/PlayerSettings.SetDefaultShaderChunkCount.html)
for more information.

You can use **Override** to override the values for each platform
individually. See
[PlayerSettings.SetShaderChunkCountForPlatform](../ScriptReference/PlayerSettings.SetShaderChunkCountForPlatform.html)
for more information.

You can also use [Shader.maximumChunksOverride](../ScriptReference/Shader-
maximumChunksOverride.html) to override **Default chunk count** at runtime.

[](avoid-shader-duplication.html)

Troubleshooting shader duplication from AssetBundles

[](shader-debugging.html)

Debugging shaders

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

