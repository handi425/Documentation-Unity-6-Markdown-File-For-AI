[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TextureStreaming-introduction.html)
  * [中文](/cn/current/Manual/TextureStreaming-introduction.html)
  * [日本語](/ja/current/Manual/TextureStreaming-introduction.html)
  * [한국어](/kr/current/Manual/TextureStreaming-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TextureStreaming-introduction.html)
  * [中文](/cn/current/Manual/TextureStreaming-introduction.html)
  * [日本語](/ja/current/Manual/TextureStreaming-introduction.html)
  * [한국어](/kr/current/Manual/TextureStreaming-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Optimizing GPU texture memory with mipmap streaming](TextureStreaming.html)
  * Introduction to mipmap streaming

[](TextureStreaming.html)

Optimizing GPU texture memory with mipmap streaming

[](TextureStreaming-use.html)

Enable mipmap streaming

# Introduction to mipmap streaming

Use mipmap streaming to limit the size of textures in GPU memory.

## How mipmap streaming works

For each texture in the **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) view, Unity automatically calculates
and loads mipmap levels only up to a specific level, instead of loading all of
them. This means that Unity only transfers some mipmap levels per texture from
disk to the CPU and the GPU.

Unity loads mipmap levels at the highest resolution possible, but uses lower
mipmap levels if higher resolution mipmap levels don’t fit in the memory limit
you set. For more information about setting a memory limit, refer to
[Configure mipmap streaming](TextureStreaming-configure.html).

Unity caches mipmap levels on the GPU, to avoid repeatedly loading mipmap
levels from disk and the CPU.

## Limitations

  * Unity doesn’t support mipmap streaming on [terrain](script-Terrain.html)The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) textures, because Unity needs the
highest resolution mipmap levels at all times.

  * Unity doesn’t support mipmap streaming with texture arrays, **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) arrays, or 3D textures.

  * If you use an API such as [Graphics.DrawMeshNow](../ScriptReference/Graphics.DrawMeshNow.html) to render a texture, Unity doesn’t have the information it needs to calculate a mipmap level. Set the mipmap level for the texture manually with the [Texture2D.requestedMipmapLevel](../ScriptReference/Texture2D-requestedMipmapLevel.html) API, or disable mipmap streaming on the texture.
  * Unity might not be able to calculate the correct mipmap level for textures that don’t use the special `_ST` property for texture tiling and offset. For more information about the `_ST` property, refer to [Accessing shader properties in Cg/HLSL](SL-PropertiesInPrograms.html).

[](TextureStreaming.html)

Optimizing GPU texture memory with mipmap streaming

[](TextureStreaming-use.html)

Enable mipmap streaming

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

