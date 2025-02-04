[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/svt-marking-textures.html)
  * [中文](/cn/current/Manual/svt-marking-textures.html)
  * [日本語](/ja/current/Manual/svt-marking-textures.html)
  * [한국어](/kr/current/Manual/svt-marking-textures.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/svt-marking-textures.html)
  * [中文](/cn/current/Manual/svt-marking-textures.html)
  * [日本語](/ja/current/Manual/svt-marking-textures.html)
  * [한국어](/kr/current/Manual/svt-marking-textures.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Streaming Virtual Texturing](svt-streaming-virtual-texturing.html)
  * Marking textures as "Virtual Texturing Only"

[](svt-cache-management.html)

Cache Management for Virtual Texturing

[](svt-error-material.html)

Virtual Texturing error material

# Marking textures as “Virtual Texturing Only”

This feature is experimental and not ready for production use. The feature and
documentation might be changed or removed in the future.

In the Unity Editor, you can mark textures that only Virtual Texturing uses.
This optimizes memory usage and **Scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) loading times, and reduces the size of
the build. To mark a texture as one that only Virtual Texturing uses, open its
Texture Importer and enable **Virtual Texture Only**.

![](../uploads/Main/svt-marking-textures01.png)

In practice, when you use Virtual Texturing, you should mark as many textures
as possible as **Virtual Texture Only** to maximize these benefits. Note that
if you mark a texture as **Virtual Texture Only** , you cannot use it with a
regular Texture Sampler in your Project. In the Editor, it might seem like you
can use it with a regular Texture Sampler because a low resolution preview
appears, but an error occurs if you then build a Player.

## How it works

By default, when you load a Scene in the Unity Editor, the Editor loads all
referenced textures into both CPU and GPU memory. The Unity Editor cannot
stream textures into GPU memory from disk, but SVT can stream them from CPU
memory. When you mark a texture as **Virtual Texture Only** , this means that
on scene load the Editor loads it into CPU memory only, and then extracts
tiles from that texture and streams them into GPU memory on demand.

In a Project with many high resolution textures, this significantly reduces
both GPU memory usage and Scene loading times in the Unity Editor. For this
reason, it’s good practice to mark as many textures as possible as **Virtual
Texture Only** , to ensure that the Streaming Virtual Texturing (SVT) system
only streams them from the CPU.

If you don’t mark a texture as **Virtual Texture Only** , and then use it with
Virtual Texturing in the Player, the SVT system keeps a copy of the texture in
both CPU and GPU memory.

## Standard texture artifacts

By default, Unity adds all textures sampled in **Shader** A program that runs
on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) Graph to the build as standard texture
artifacts. Additionally, Virtual Texturing imports all Texture Stack textures
into a tiled streaming file, which Unity also includes in the build.

  * If you mark a texture as **Virtual Texture Only** , Unity doesn’t include it as a standard texture artifact, and includes it only in the tiled streaming file.
  * If you don’t mark a texture as **Virtual Texture Only** , Unity includes it twice in the build; once as a standard texture artifact, and once in the tiled streaming file.

Note that if you mark a texture as **Virtual Texture Only** , but use it as a
standard texture in the Player, the Player build fails.

[](svt-cache-management.html)

Cache Management for Virtual Texturing

[](svt-error-material.html)

Virtual Texturing error material

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

