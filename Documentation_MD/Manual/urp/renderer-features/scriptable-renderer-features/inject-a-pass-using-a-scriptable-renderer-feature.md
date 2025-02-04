[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)
  * [中文](/cn/current/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)
  * [中文](/cn/current/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)

  * [Rendering](../../../rendering-and-post-processing.html)
  * [Render pipelines](../../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../../urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](../../../urp/inject-a-render-pass.html)
  * [Injecting a render pass via a Scriptable Renderer Feature in URP](../../../urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
  * Create a Scriptable Renderer Feature in URP

[](../../../urp/renderer-features/scriptable-renderer-features/intro-to-
scriptable-renderer-features.html)

Introduction to Scriptable Renderer Features in URP

[](../../../urp/renderer-features/scriptable-renderer-features/apply-
scriptable-feature-to-specific-camera.html)

Apply a Scriptable Renderer Feature to a specific camera type in URP

# Create a Scriptable Renderer Feature in URP

Use the `ScriptableRenderFeature` API to insert a [Scriptable Render
Pass](../../renderer-features/intro-to-scriptable-render-passes.html) into the
Universal **Render Pipeline** A series of operations that take the contents of
a Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](../../../render-
pipelines.html)  
See in [Glossary](../../../Glossary.html#Renderpipeline) (URP) frame rendering
loop.

Follow these steps:

  1. Create a new C# script.

  2. Replace the code with a class that inherits from the `ScriptableRendererFeature` class.
    
        using UnityEngine;
    using UnityEngine.Rendering.Universal;
    
    public class MyRendererFeature : ScriptableRendererFeature
    {
    }
    

  3. In the class, override the `Create` method. For example:
    
        public override void Create()
    {
    }
    

URP calls the `Create` methods on the following events:

     * When the Scriptable Renderer Feature loads the first time.
     * When you enable or disable the Scriptable Renderer Feature.
     * When you change a property in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../../UsingTheInspector.html)  
See in [Glossary](../../../Glossary.html#Inspector)** window of the Renderer
Feature.

  4. In the `Create` method, create an instance of your Scriptable Render Pass, and inject it into the renderer.

For example, if you have a Scriptable Render Pass called `RedTintRenderPass`:

    
        // Define an instance of the Scriptable Render Pass
    private RedTintRenderPass redTintRenderPass;
    
    public override void Create()
    {
        // Create an instance of the Scriptable Render Pass
        redTintRenderPass = new RedTintRenderPass();
    
        // Inject the render pass after rendering the skybox
        redTintRenderPass.renderPassEvent = RenderPassEvent.AfterRenderingSkybox;
    }
    

  5. Override the `AddRenderPasses` method.
    
        public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
    }
    

URP calls the `AddRenderPasses` method every frame, once for each **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](../../../CamerasOverview.html)  
See in [Glossary](../../../Glossary.html#Camera).

  6. Use the `EnqueuePass` API to inject the Scriptable Render Pass into the frame rendering loop.
    
        public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        renderer.EnqueuePass(redTintRenderPass);
    }
    

You can now add the Scriptable Renderer Feature to the active URP asset. Refer
to [How to add a Renderer Feature to a Renderer](../../urp-renderer-
feature.html) for more information.

For a full example, refer to [Example of a complete Scriptable Renderer
Feature](../create-custom-renderer-feature.html).

[](../../../urp/renderer-features/scriptable-renderer-features/intro-to-
scriptable-renderer-features.html)

Introduction to Scriptable Renderer Features in URP

[](../../../urp/renderer-features/scriptable-renderer-features/apply-
scriptable-feature-to-specific-camera.html)

Apply a Scriptable Renderer Feature to a specific camera type in URP

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

