[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/working-with-textures.html)
  * [中文](/cn/current/Manual/urp/working-with-textures.html)
  * [日本語](/ja/current/Manual/urp/working-with-textures.html)
  * [한국어](/kr/current/Manual/urp/working-with-textures.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/working-with-textures.html)
  * [中文](/cn/current/Manual/urp/working-with-textures.html)
  * [日本語](/ja/current/Manual/urp/working-with-textures.html)
  * [한국어](/kr/current/Manual/urp/working-with-textures.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../urp/customizing-urp.html)
  * [Render graph system in URP](../urp/render-graph.html)
  * Textures in the Render Graph system in URP

[](../urp/render-graph-write-render-pass.html)

Write a render pass using the render graph system in URP

[](../urp/render-graph-create-a-texture.html)

Create a texture in the render graph system in URP

# Textures in the Render Graph system in URP

How to access and use textures in a custom render pass in the Universal
**Render Pipeline** A series of operations that take the contents of a Scene,
and displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP).

Page | Description  
---|---  
[Create a texture in the render graph system](render-graph-create-a-texture.html) | Create a texture in a render graph system render pass.  
[Import a texture into the render graph system](render-graph-import-a-texture.html) | To create or use a **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture) in a render graph system
render pass, use the `RTHandle` API.  
[Use a texture in a render pass](render-graph-read-write-texture.html) | To allow a render pass to read from or write to a texture, use the render graph system API to set the texture as an input or output.  
[Transfer a texture between passes](render-graph-pass-textures-between-passes.html) | Set a texture as a global texture, or add the texture to the frame data.  
  
## Additional resources

  * [Use frame data](accessing-frame-data.html)
  * The **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](../Glossary.html#blit) examples in the [URP RenderGraph
Samples](package-sample-urp-package-samples.html)

  * [Example of a complete Scriptable Renderer Feature](renderer-features/create-custom-renderer-feature.html)

[](../urp/render-graph-write-render-pass.html)

Write a render pass using the render graph system in URP

[](../urp/render-graph-create-a-texture.html)

Create a texture in the render graph system in URP

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

