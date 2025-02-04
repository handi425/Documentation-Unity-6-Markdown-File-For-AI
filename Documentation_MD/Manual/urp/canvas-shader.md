[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/canvas-shader.html)
  * [中文](/cn/current/Manual/urp/canvas-shader.html)
  * [日本語](/ja/current/Manual/urp/canvas-shader.html)
  * [한국어](/kr/current/Manual/urp/canvas-shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/canvas-shader.html)
  * [中文](/cn/current/Manual/urp/canvas-shader.html)
  * [日本語](/ja/current/Manual/urp/canvas-shader.html)
  * [한국어](/kr/current/Manual/urp/canvas-shader.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * [Shader Material Inspector window reference for URP](../urp/shaders-in-universalrp-reference.html)
  * Canvas Shader Graph

[](../urp/particles-unlit-shader.html)

Particles Unlit Shader Material Inspector window reference for URP

[](../shader-built-in-birp-landing.html)

Shaders in the Built-In Render Pipeline

# Canvas Shader Graph

The Canvas material type enables you to author **Shader** A program that runs
on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) Graph shaders that can be applied
to [UGUI user interface
elements](https://docs.unity3d.com/Packages/com.unity.ugui@1.0/manual/UICanvas.html).

## Contexts

This material type comes with a distinct set of Graph Settings, which
significantly affects the Blocks relevant to the Graph. This section provides
details regarding the Blocks automatically added by default in this Master
Stack material type and the Blocks that determine properties for the Graph
Settings of this material type.

### Vertex Context

The Vertex context represents the vertex stage of this shader. Unity executes
any block you connect to this context in the vertex function of this shader.
For more information, refer to [Master
Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.0/manual/Master-
Stack.html).

Vertex blocks are not compatible with the Canvas Master Stack.

### Fragment Context

The Fragment Context contains the default and relevant Blocks for the Canvas
material.

#### Default Fragment Context

When you create a new Canvas material, the Fragment Context contains the
following Blocks by default:

**Property** | **Description** | **Setting dependency** | **Default value**  
---|---|---|---  
**Base Color** | The base color of the material. | None | Color.grey  
**Alpha** | The Material’s alpha value. | None | 1.0  
**Emission** | The color of light to emit from this material’s surface. Emissive materials appear as a source of light in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene). | None | Color.black  
  
#### Relevant Fragment Context

Depending on the Graph Settings you use, Shader Graph might add the following
Blocks to the Fragment Context:

**Property** | **Description** | **Setting dependency** | **Default value**  
---|---|---|---  
**Alpha Clip Threshold** | The alpha value limit that URP uses to determine whether to render each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel). If the alpha value of the pixel is equal to or higher than the limit, URP renders the pixel. If the value is lower than the limit, URP does not render the pixel. The default value is 0.5. |  **Alpha Clipping** enabled | 0.5  
  
## Graph Settings

The following table describes the Surface Options in the Graph Settings:

**Property** | **Description**  
---|---  
**Material Type** | Specifies a type for the material. This allows you to customize the material with different settings depending on the type you select. The options are:  
• **Sprite Custom Lit**  
• **Sprite Lit**  
• **Sprite Unlit**  
• **Canvas**  
• **Decal**  
• **Fullscreen**  
• **Lit**  
• **Unlit** :  
**Alpha Clipping** | Indicates whether this material acts like a [Cutout Shader](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterRenderingMode.html).  
  
## Additional resources

  * [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.0/manual/)

[](../urp/particles-unlit-shader.html)

Particles Unlit Shader Material Inspector window reference for URP

[](../shader-built-in-birp-landing.html)

Shaders in the Built-In Render Pipeline

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

