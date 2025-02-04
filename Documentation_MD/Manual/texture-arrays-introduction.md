[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/texture-arrays-introduction.html)
  * [中文](/cn/current/Manual/texture-arrays-introduction.html)
  * [日本語](/ja/current/Manual/texture-arrays-introduction.html)
  * [한국어](/kr/current/Manual/texture-arrays-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/texture-arrays-introduction.html)
  * [中文](/cn/current/Manual/texture-arrays-introduction.html)
  * [日本語](/ja/current/Manual/texture-arrays-introduction.html)
  * [한국어](/kr/current/Manual/texture-arrays-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [2D texture arrays](class-Texture2DArray.html)
  * Introduction to 2D texture arrays

[](class-Texture2DArray.html)

2D texture arrays

[](class-Texture2DArray-import.html)

Create a 2D texture array

# Introduction to 2D texture arrays

A texture array is a collection of 2D textures with the same size, format, and
flags. The individual texture in the array are called slices or layers. In a
**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), you can use an index to sample each
slice.

Texture arrays are useful for implementing custom **terrain** The landscape in
your scene. A Terrain GameObject adds a large flat plane to your scene and you
can use the Terrain’s Inspector window to create a detailed landscape. [More
info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) rendering systems or other special
effects where you need an efficient way to access many textures of the same
size and format.

## Platform support

Texture arrays are supported if the platform supports one of the following
graphics APIs:

  * DirectX11 and DirectX12 (Windows)
  * Metal (iOS, macOS)
  * OpenGL Core (macOS, Linux)
  * OpenGL ES 3.0 (Android, WebGL 2.0)
  * Vulkan (Windows, Linux)

To check if a platform supports texture arrays, use the
[SystemInfo.supports2DArrayTextures](../ScriptReference/SystemInfo-
supports2DArrayTextures.html) API at runtime.

[](class-Texture2DArray.html)

2D texture arrays

[](class-Texture2DArray-import.html)

Create a 2D texture array

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

