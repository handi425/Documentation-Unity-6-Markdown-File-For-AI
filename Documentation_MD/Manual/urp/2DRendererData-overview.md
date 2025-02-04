[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2DRendererData-overview.html)
  * [中文](/cn/current/Manual/urp/2DRendererData-overview.html)
  * [日本語](/ja/current/Manual/urp/2DRendererData-overview.html)
  * [한국어](/kr/current/Manual/urp/2DRendererData-overview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2DRendererData-overview.html)
  * [中文](/cn/current/Manual/urp/2DRendererData-overview.html)
  * [日本語](/ja/current/Manual/urp/2DRendererData-overview.html)
  * [한국어](/kr/current/Manual/urp/2DRendererData-overview.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * 2D Renderer asset component reference for URP

[](../urp/2d-light-batching-debugger.html)

Check how Unity batches lights

[](../urp/LightBlendStyles.html)

Light Blend Styles component reference for URP

# 2D Renderer asset component reference for URP

Explore the properties and settings of the 2D Renderer Data Asset to customize
the 2D lighting features.

![The 2D Renderer Data Asset property
settings](../../uploads/urp/2D/2dRendererData_properties.png) The 2D Renderer
Data Asset property settings

The **2D Renderer Data** Asset contains the settings that affect the way **2D
Lights** are applied to lit **Sprites** A 2D graphic objects. If you are used
to working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](../sprite/sprite-landing.html)  
See in [Glossary](../Glossary.html#Sprite). You can set the way Lights emulate
**HDR** high dynamic range  
See in [Glossary](../Glossary.html#HDR) lighting with the [HDR Emulation
Scale](HDREmulationScale.html), or customize your own [Light Blend
Styles](LightBlendStyles.html). Refer to their respective pages for more
information about their properties and options.

## Default Material Type

![The 2D Renderer Data Asset property
settings](../../uploads/urp/2D/Default_Material_Type.png) The 2D Renderer Data
Asset property settings

Unity assigns a Material of the selected **Default Material Type** to Sprites
when they are created. The available options have the following properties and
functions.

**Lit** : Unity assigns a Material with the Lit type (default Material:
Sprite-Lit-Default). 2D Lights affect Materials of this type.

**Unlit** : Unity assigns a Material with the Unlit type (default Material:
Sprite-Lit-Default). 2D Lights do not affect Materials of this type.

**Custom** : Unity assigns a Material with the Custom type. When you select
this option, Unity shows the **Default Custom Material** box. Assign the
desired Material to this box.

![The 2D Renderer Data Asset property
settings](../../uploads/urp/2D/Default_Custom_Material.png) The 2D Renderer
Data Asset property settings

## Use Depth/Stencil Buffer

This option is enabled by default. Clear this option to disable the
Depth/[Stencil](https://docs.unity3d.com/Manual/SL-Stencil.html) Buffer. Doing
so might improve your project’s performance, especially on mobile platforms.
You should clear this option if you are not using any features that require
the Depth/**Stencil Buffer** A memory store that holds an 8-bit per-pixel
value. In Unity, you can use a stencil buffer to flag pixels, and then only
render to pixels that pass the stencil operation. [More info](../class-
RenderTexture.html)  
See in [Glossary](../Glossary.html#stencilbuffer) (such as [Sprite
Mask](https://docs.unity3d.com/Manual/class-SpriteMask.html)A texture which
defines which areas of an underlying image to reveal or hide. [More
info](../sprite/mask/mask-landing.html)  
See in [Glossary](../Glossary.html#SpriteMask)).

## Camera Sorting Layer Texture

The **2D Renderer Data** specifies how Unity supplies the **shader** A program
that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) variable
`CameraSortingLayerTexture` for use in custom shaders. It is recommended that
you use this data in the same frame and on the following layers, as using
`CameraSortingLayerTexture` before it has been captured may result in
unexpected results.

### Foremost Sorting Layer

All Layers captured for use in the supplied Texture will be drawn from the
very back Layer up to and including the Layer specified by **Foremost Sorting
Layer**.

### Downsampling Method

Downsampling reduces the Texture resolution used by
`CameraSortingLayerTexture`. The options are: **None** , **2x Bilinear** ,
**4x Box** , **4x Bilinear**.

## Renderer Features

The 2D Renderer supports [URP Renderer Features](urp-renderer-feature.html).
The setup for the features are called before any of the 2D built-in passes are
queued.

[](../urp/2d-light-batching-debugger.html)

Check how Unity batches lights

[](../urp/LightBlendStyles.html)

Light Blend Styles component reference for URP

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

