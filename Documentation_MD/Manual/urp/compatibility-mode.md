[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/compatibility-mode.html)
  * [中文](/cn/current/Manual/urp/compatibility-mode.html)
  * [日本語](/ja/current/Manual/urp/compatibility-mode.html)
  * [한국어](/kr/current/Manual/urp/compatibility-mode.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/compatibility-mode.html)
  * [中文](/cn/current/Manual/urp/compatibility-mode.html)
  * [日本語](/ja/current/Manual/urp/compatibility-mode.html)
  * [한국어](/kr/current/Manual/urp/compatibility-mode.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../urp/customizing-urp.html)
  * Compatibility Mode in URP

[](../urp/customize/custom-pass-injection-points.html)

Injection points reference for URP

[](../urp/renderer-features/write-a-scriptable-render-pass.html)

Write a Scriptable Render Pass in Compatibility Mode in URP

# Compatibility Mode in URP

If you enable **Compatibility Mode (Render Graph Disabled)** in URP graphics
settings, you can write a Scriptable Render Pass without using the [render
graph API](render-graph.html). The setting is in **Project Settings** >
**Graphics** > **Pipeline Specific Settings** > **URP** > **Render Graph**.

**Note:** Unity no longer develops or improves the **rendering path** The
technique that a render pipeline uses to render graphics. Choosing a different
rendering path affects how lighting and shading are calculated. Some rendering
paths are more suited to different platforms and hardware than others. [More
info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath) that doesn’t use the [render
graph API](render-graph.html). Use the render graph API instead when
developing new graphics features.

Page | Description  
---|---  
[Write a Scriptable Render Pass in Compatibility Mode](renderer-features/write-a-scriptable-render-pass.html) | An example of creating a Scriptable Render Pass in Compatibility Mode.  
[Example of a Scriptable Renderer Feature in Compatibility mode](renderer-features/how-to-fullscreen-blit.html) | An example that describes how to create a custom Renderer Feature that performs a full screen **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](../Glossary.html#blit).  
[Scriptable Render Pass Compatibility Mode API reference for URP](renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html) | Reference for the Scriptable Render Pass API.  
  
[](../urp/customize/custom-pass-injection-points.html)

Injection points reference for URP

[](../urp/renderer-features/write-a-scriptable-render-pass.html)

Write a Scriptable Render Pass in Compatibility Mode in URP

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

