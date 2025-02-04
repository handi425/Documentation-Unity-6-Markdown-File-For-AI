[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/svt-streaming-virtual-texturing.html)
  * [中文](/cn/current/Manual/svt-streaming-virtual-texturing.html)
  * [日本語](/ja/current/Manual/svt-streaming-virtual-texturing.html)
  * [한국어](/kr/current/Manual/svt-streaming-virtual-texturing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/svt-streaming-virtual-texturing.html)
  * [中文](/cn/current/Manual/svt-streaming-virtual-texturing.html)
  * [日本語](/ja/current/Manual/svt-streaming-virtual-texturing.html)
  * [한국어](/kr/current/Manual/svt-streaming-virtual-texturing.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * Streaming Virtual Texturing

[](SparseTextures.html)

Sparse Textures

[](svt-requirements-compatibility.html)

Streaming Virtual Texturing requirements and compatibility

# Streaming Virtual Texturing

This feature is experimental and not ready for production use. The feature and
documentation might be changed or removed in the future.

Streaming Virtual Texturing (SVT) is a feature that reduces GPU memory usage
and texture loading times when you have many high resolution textures in your
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). It splits textures into tiles, and
progressively uploads these tiles to GPU memory when they are needed.

SVT lets you set a fixed memory cost. For full texture quality, the required
GPU cache size depends mostly on the frame resolution, and not the number or
resolution of textures in the Scene. The more high resolution textures you
have in your Scene, the more GPU memory you can save with SVT.

The workflow requires no additional import time, no additional build step, and
no additional streaming files. You work with regular Unity Textures in the
Unity Editor.

[](SparseTextures.html)

Sparse Textures

[](svt-requirements-compatibility.html)

Streaming Virtual Texturing requirements and compatibility

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

