[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
  * [中文](/cn/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
  * [中文](/cn/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)

  * [Rendering](../../../rendering-and-post-processing.html)
  * [Render pipelines](../../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../../urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](../../../urp/inject-a-render-pass.html)
  * [Injecting a render pass via a Scriptable Renderer Feature in URP](../../../urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
  * Scriptable Renderer Feature API reference for URP

[](../../../urp/renderer-features/create-custom-renderer-feature.html)

Example of a complete Scriptable Renderer Feature in URP

[](../../../urp/customize/inject-render-pass-via-script.html)

Inject a render pass via scripting in URP

# Scriptable Renderer Feature API reference for URP

You can use the following methods within a Scriptable Renderer Feature to
handle its core functions. For more information on Scriptable Renderer Feature
scripting and further details on the methods listed below, refer to
[ScriptableRendererFeature](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ScriptableRendererFeature.html).

**Method** | **Description**  
---|---  
`AddRenderPasses` | Use this method to add one or more Render Passes into the rendering sequence of the renderer with the `EnqueuePass` method.  
  
By default this method applies the render passes to all cameras. To change
this, add logic to return early in the method when a specific camera or camera
type is detected.  
  
**Note** : URP calls this method once per camera when the renderer is set up,
for this reason you should not create or instantiate any resources within this
function.  
`Create` | Use this method to initialize any resources the Scriptable Renderer Feature needs such as Materials and Render Pass instances.  
`Dispose` | Use this method to clean up the resources allocated to the Scriptable Renderer Feature such as Materials.  
`SetupRenderPasses` | Use this method to run any setup the Scriptable Render Passes require. For example, you can set the initial values of properties, or run custom setup methods from your Scriptable Render Passes.  
  
If your Scriptable Renderer Feature accesses camera targets to set up its
Scriptable Render Passes, do it in this method instead of in the
`AddRenderPasses` method.  
  
## Additional resources

  * [Introduction to Scriptable Renderer Features](./intro-to-scriptable-renderer-features.html)
  * [Introduction to Scriptable Render Passes](intro-to-scriptable-renderer-features.html)
  * [How to create a Custom Renderer Feature](../create-custom-renderer-feature.html)

[](../../../urp/renderer-features/create-custom-renderer-feature.html)

Example of a complete Scriptable Renderer Feature in URP

[](../../../urp/customize/inject-render-pass-via-script.html)

Inject a render pass via scripting in URP

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

