[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/renderer-feature-render-objects.html)
  * [中文](/cn/current/Manual/urp/renderer-features/renderer-feature-render-objects.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/renderer-feature-render-objects.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/renderer-feature-render-objects.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/renderer-feature-render-objects.html)
  * [中文](/cn/current/Manual/urp/renderer-features/renderer-feature-render-objects.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/renderer-feature-render-objects.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/renderer-feature-render-objects.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../urp/customizing-urp.html)
  * [Adding pre-built effects via Renderer Features in URP](../../urp/urp-renderer-feature-landing.html)
  * Render Objects Renderer Feature reference for URP

[](../../urp/renderer-features/how-to-custom-effect-render-objects.html)

Example of creating a custom rendering effect via the Render Objects Renderer
Feature in URP

[](../../urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)

Custom render pass workflow in URP

# Render Objects Renderer Feature reference for URP

Refer to: [How to use the Render Objects Renderer Feature](how-to-custom-
effect-render-objects.html).

## Properties

The Render Objects Renderer Feature contains the following properties.

Property | Description  
---|---  
**Name** | Use this field to edit the name of the feature.  
**Event** | The event in the URP queue when Unity executes this Renderer Feature.  
**Filters** | Settings that let you configure which objects this Renderer Feature renders.  
Queue | Select whether the feature renders opaque or transparent objects.  
**Layer Mask** A value defining which layers to include or exclude from an
operation, such as rendering, collision or your own code. [More
info](../../Layers.html)  
See in [Glossary](../../Glossary.html#LayerMask) | The Renderer Feature renders objects from layers you select in this property.  
**Pass Names** | If a Pass in a **shader** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) has the `LightMode` Pass Tag,
this Renderer Feature processes only the shaders where the value of the
`LightMode` Pass Tag equals one of the values in the Pass Names property.  
**Overrides** | Settings in this section let you configure overrides for certain properties when rendering with this Renderer Feature.  
Override Mode | Specify the material override mode.  
Material | (Override Mode is set to Material) When rendering an object, Unity replaces the Material assigned to it with this Material. This will override all material properties with this material  
Shader | (Override Mode is set to Shader) When rendering an object, Unity replaces the material assigned to it with this shader. This maintains all material properties and allows the override shader to access these properties. This is currently not SRPBatcher compatible and less performant.  
Depth | Selecting this option lets you specify how this Renderer Feature affects or uses the Depth buffer. This option contains the following items:  
Write Depth: this option defines whether the Renderer Feature updates the
Depth buffer when rendering objects.  
Depth Test: the condition which determines when this Renderer Feature renders
pixels of a given object.  
Stencil | With this check box selected, the Renderer processes the Stencil buffer values.  
For more information on how Unity works with the Stencil buffer, refer to
[ShaderLab: Stencil](https://docs.unity3d.com/Manual/SL-Stencil.html).  
Camera | Selecting this option lets you override the following Camera properties:  
Field of View: when rendering objects, the Renderer Feature uses this Field of
View instead of the value specified on the Camera.  
Position Offset: when rendering objects, the Renderer Feature moves them by
this offset.  
Restore: with this option selected, the Renderer Feature restores the original
Camera matrices after executing the render passes in this Renderer Feature.  
  
[](../../urp/renderer-features/how-to-custom-effect-render-objects.html)

Example of creating a custom rendering effect via the Render Objects Renderer
Feature in URP

[](../../urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)

Custom render pass workflow in URP

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

