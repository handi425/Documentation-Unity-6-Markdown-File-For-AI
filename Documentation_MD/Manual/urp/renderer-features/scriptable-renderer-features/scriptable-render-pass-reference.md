[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)
  * [中文](/cn/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)
  * [中文](/cn/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)

  * [Rendering](../../../rendering-and-post-processing.html)
  * [Render pipelines](../../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../../urp/customizing-urp.html)
  * [Compatibility Mode in URP](../../../urp/compatibility-mode.html)
  * Scriptable Render Pass Compatibility Mode API reference for URP

[](../../../urp/renderer-features/how-to-fullscreen-blit.html)

Example of a Scriptable Renderer Feature in Compatibility mode in URP

[](../../../urp/urp-reference-landing.html)

Universal Render Pipeline reference

# Scriptable Render Pass Compatibility Mode API reference for URP

You can use the following methods within a Scriptable Render Pass to handle
its core functions.

**Note:** Unity no longer develops or improves the rendering path that doesn’t
use the [render graph API](../../render-graph.html). Use the render graph API
instead when developing new graphics features. To use the instructions on this
page, enable **Compatibility Mode (Render Graph Disabled)** in URP graphics
settings (**Project Settings** > **Graphics**).

**Method** | **Description**  
---|---  
`Execute` | Use this method to implement the rendering logic for the Scriptable Renderer Feature.  
  
**Note** : You must not call `ScriptableRenderContext.Submit` on a command
buffer provided by URP. The render pipeline handles this at specific points in
the pipeline.  
`OnCameraCleanup` | Use this method to clean up any resources that were allocated during the render pass.  
`OnCameraSetup` | Use this method to configure render targets and their clear state. You can also use it to create temporary render target textures.  
  
**Note** : When this method is empty, the render pass renders to the active
camera render target.  
  
## Additional resources

  * [Scriptable Render Passes](../intro-to-scriptable-render-passes.html)
  * [How to create a Custom Renderer Feature](../create-custom-renderer-feature.html)

[](../../../urp/renderer-features/how-to-fullscreen-blit.html)

Example of a Scriptable Renderer Feature in Compatibility mode in URP

[](../../../urp/urp-reference-landing.html)

Universal Render Pipeline reference

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

