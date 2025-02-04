[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/urp-universal-renderer.html)
  * [中文](/cn/current/Manual/urp/urp-universal-renderer.html)
  * [日本語](/ja/current/Manual/urp/urp-universal-renderer.html)
  * [한국어](/kr/current/Manual/urp/urp-universal-renderer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/urp-universal-renderer.html)
  * [中文](/cn/current/Manual/urp/urp-universal-renderer.html)
  * [日本語](/ja/current/Manual/urp/urp-universal-renderer.html)
  * [한국어](/kr/current/Manual/urp/urp-universal-renderer.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Universal Render Pipeline reference](../urp/urp-reference-landing.html)
  * Universal Renderer asset reference for URP

[](../urp/universalrp-asset.html)

Universal Render Pipeline asset reference for URP

[](../urp/urp-global-settings.html)

Graphics settings window reference for URP

# Universal Renderer asset reference for URP

This page describes the URP Universal Renderer settings.

For more information on rendering in URP, also check [Rendering in the
Universal Render Pipeline](rendering-in-universalrp.html).

## How to find the Universal Renderer asset

To find the Universal Renderer asset that a URP asset is using:

  1. Select a URP asset.

  2. In the Renderer List section, click a renderer item or the vertical ellipsis icon (⋮) next to a renderer.

![How to find the Universal Renderer asset](../../uploads/urp/urp-assets/find-
renderer.png) How to find the Universal Renderer asset

## Properties

### Filtering

This section contains properties that define which layers the renderer draws.

Property | Description  
---|---  
**Opaque**Layer Mask** A value defining which layers to include or exclude
from an operation, such as rendering, collision or your own code. [More
info](../Layers.html)  
See in [Glossary](../Glossary.html#LayerMask)** | Select which opaque layers this Renderer draws  
**Transparent Layer Mask** | Select which transparent layers this Renderer draws  
  
### Rendering

This section contains properties related to rendering.

Property | Description  
---|---  
**Rendering Path** | Select the Rendering Path.  
Options:

  * **Forward** : The Forward Rendering Path.
  * **Forward+** : The [Forward+ Rendering Path](rendering/forward-rendering-paths.html).
  * **Deferred** : The [Deferred Rendering Path](rendering/deferred-rendering-path-landing.html).

  
**Depth Priming Mode** | Specify whether Unity uses scene depth data to identify pixels the camera can’t see, then skips the shader fragment stage for those pixels. This speeds up rendering, but has an upfront memory and performance cost. The amount rendering speeds up depends on how many pixels are hidden, and the complexity of the fragment shader code Unity skips.  
  
The options are:

  * **Disabled** : Unity doesn’t perform depth priming.
  * **Auto** : Unity performs depth priming only if it’s already performed a depth prepass. A depth prepass renders scene depth data early in the render pipeline. This option is not supported on Android, iOS, and Apple TV.
  * **Forced** : Unity always performs a depth prepass and depth priming.

  
Depth priming isn’t compatible with the following:

  * Platforms that use tile-based rendering.
  * The Deferred rendering path.
  * Multisample anti-aliasing (MSAA).

  
**Accurate G-buffer normals** | Indicates whether to use a more resource-intensive normal encoding/decoding method to improve visual quality.  
  
This property is available only if **Rendering Path** is set to **Deferred**.  
**Depth Texture Mode** | Specifies the stage in the render pipeline at which to copy the scene depth to a depth texture. The options are:

  * **After Opaques** : URP copies the scene depth after the opaques render pass.
  * **After Transparents** : URP copies the scene depth after the transparents render pass.
  * **Force Prepass** : URP does a depth prepass to generate the scene depth texture.

**Note** : On mobile devices, the **After Transparents** option can lead to a
significant improvement in memory bandwidth. This is because the Copy Depth
pass causes a switch in render target between the Opaque pass and the
Transparents pass. When this occurs, Unity stores the contents of the Color
Buffer in the main memory, and then loads it again once the Copy Depth pass is
complete. The impact increases significantly when MSAA is enabled as Unity
must also store and load the MSAA data alongside the Color Buffer.  
  
### Native RenderPass

This section contains properties related to URP’s Native RenderPass API.

Property | Description  
---|---  
**Native RenderPass** | Indicates whether to use URP’s Native RenderPass API. When enabled, URP uses this API to structure render passes. As a result, you can use [programmable blending](https://docs.unity3d.com/Manual/SL-PlatformDifferences.html#using-shader-framebuffer-fetch) in custom URP shaders. For more information about the RenderPass API, refer to [ScriptableRenderContext.BeginRenderPass](https://docs.unity3d.com/ScriptReference/Rendering.ScriptableRenderContext.BeginRenderPass.html).  
  
**Note** : Enabling this property has no effect on OpenGL ES.  
  
### Shadows

This section contains properties related to rendering shadows.

Property | Description  
---|---  
**Transparent Receive Shadows** | When this option is on, Unity draws shadows on transparent objects.  
  
### Overrides

This section contains **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) properties that this
Renderer overrides.

#### Stencil

With this check box selected, the Renderer processes the **Stencil buffer** A
memory store that holds an 8-bit per-pixel value. In Unity, you can use a
stencil buffer to flag pixels, and then only render to pixels that pass the
stencil operation. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#stencilbuffer) values.

![URP Universal Renderer Stencil override](../../uploads/urp/urp-assets/urp-
universal-renderer-stencil-on.png) URP Universal Renderer Stencil override

For more information on how Unity works with the Stencil buffer, refer to
[ShaderLab: Stencil](https://docs.unity3d.com/Manual/SL-Stencil.html).

In URP, you can use bits 0 to 3 of the stencil buffer for custom rendering
effects. This means you can use stencil indices 0 to 15.

### Compatibility

This section contains settings related to backwards compatibility.

Property | Description  
---|---  
**Intermediate Texture** | This property lets you force URP to renders via an intermediate texture.  
Options:

  * **Auto** : URP uses the information provided by the `ScriptableRenderPass.ConfigureInput` method to determine automatically whether rendering via an intermediate texture is necessary.
  * **Always** : forces rendering via an intermediate texture. Use this option only for compatibility with Renderer Features that do not declare their inputs with `ScriptableRenderPass.ConfigureInput`. Using this option might have a significant performance impact on some platforms.

  
  
### Renderer Features

This section contains the list of Renderer Features assigned to the selected
Renderer.

For information on how to add a Renderer Feature, check [How to add a Renderer
Feature to a Renderer](urp-renderer-feature.html).

URP contains the pre-built Renderer Feature called [Render Objects](renderer-
features/renderer-feature-render-objects.html).

[](../urp/universalrp-asset.html)

Universal Render Pipeline asset reference for URP

[](../urp/urp-global-settings.html)

Graphics settings window reference for URP

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

