[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html)
  * [中文](/cn/current/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html)
  * [日本語](/ja/current/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html)
  * [한국어](/kr/current/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html)
  * [中文](/cn/current/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html)
  * [日本語](/ja/current/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html)
  * [한국어](/kr/current/Manual/urp/urp-shaders/fullscreen-master-stack-shader-graph.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../../urp/post-processing-in-urp.html)
  * [Custom post-processing in URP](../../urp/post-processing/custom-post-processing.html)
  * [Creating a full-screen shader in Shader Graph in URP](../../urp/urp-shaders/fullscreen-master-stack-urp.html)
  * Fullscreen Master Stack reference for Shader Graph in URP

[](../../urp/urp-shaders/fullscreen-master-stack-urp.html)

Creating a full-screen shader in Shader Graph in URP

[](../../urp/urp-shaders/fullscreen-master-stack-reference.html)

Fullscreen Master Stack in Shader Graph reference for URP

# Fullscreen Master Stack reference for Shader Graph in URP

Use the Fullscreen Master Stack to create a **Shader** A program that runs on
the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) Graph material to apply to the
entire screen at the end of the rendering process. You can use this to create
custom post-process and custom pass effects.

![A full-screen shader that applies a raindrop effect to the
screen.](../../../uploads/urp/Fullscreen-shader-rain.png) A full-screen shader
that applies a raindrop effect to the screen.

## Contexts

A shader graph contains the following contexts:

  * Vertex context
  * Fragment context

The Fullscreen Master Stack has its own [Graph Settings](fullscreen-master-
stack-reference.html) that determine which blocks you can use in the Shader
Graph contexts.

This section contains information on the blocks that this Master Stack
material type uses by default, and which blocks you can use to affect the
Graph Settings.

###  Vertex context

The Vertex context represents the vertex stage of this shader. Unity executes
any block you connect to this context in the vertex function of this shader.
For more information, refer to [Master
Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph@14.0/manual/Master-
Stack.html).

Vertex blocks are not compatible with the Fullscreen Master Stack.

###  Fragment context

The Fragment context represents the fragment (or pixel) stage of this shader.
Unity executes any block you connect to this context in the fragment function
of this shader. For more information, refer to [Master
Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph@14.0/manual/Master-
Stack.html).

### Default

When you create a new Fullscreen Master Stack, the Fragment context contains
the following blocks by default.

**Property** | **Description** | **Setting Dependency** | **Default Value**  
---|---|---|---  
**Base Color** | The base color of the material. | None | Color.grey  
**Alpha** | The Material’s alpha value. This determines how transparent the material is. The expected range is 0 - 1. | None | 1.0  
  
### Relevant

The following blocks are also compatible with the Fullscreen master stack.

**Property** | **Description** | **Setting Dependency** | **Default Value**  
---|---|---|---  
**Eye Depth** | Scales a value to world space to represent the depth from the near plane. This value represents a point in world space, determined by the platform you use. For more information, refer to [The Depth (Z) direction in Shaders](https://docs.unity3d.com/Manual/SL-PlatformDifferences.html). | In **Graph Settings** : • Enable **Depth Write**.  
• Set **Depth Write Mode** to **LinearEye**. | 0  
**Linear 01 Depth** | Uses a linear depth value between 0 and 1. | In **Graph Settings** : • Enable **Depth Write**.  
• Set **Depth Write Mode** to **Linear01**. | 0  
**Raw Depth** | Samples the depth value from the depth buffer. You can also use this setting with a nonlinear depth value. | In **Graph Settings** : • Enable **Depth Write**.  
• Set **Depth Write Mode** to **Raw**. | 0  
  
## Fullscreen Master Stack reference

For more information about the properties available in the Fullscreen Master
Stack, refer to the [Master Stack Fullscreen reference for URP](fullscreen-
master-stack-reference.html).

[](../../urp/urp-shaders/fullscreen-master-stack-urp.html)

Creating a full-screen shader in Shader Graph in URP

[](../../urp/urp-shaders/fullscreen-master-stack-reference.html)

Fullscreen Master Stack in Shader Graph reference for URP

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

