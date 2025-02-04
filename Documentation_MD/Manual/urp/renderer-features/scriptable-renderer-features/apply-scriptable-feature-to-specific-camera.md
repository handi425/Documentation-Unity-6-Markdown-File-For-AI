[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)
  * [中文](/cn/current/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)
  * [中文](/cn/current/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)

  * [Rendering](../../../rendering-and-post-processing.html)
  * [Render pipelines](../../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../../urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](../../../urp/inject-a-render-pass.html)
  * [Injecting a render pass via a Scriptable Renderer Feature in URP](../../../urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
  * Apply a Scriptable Renderer Feature to a specific camera type in URP

[](../../../urp/renderer-features/scriptable-renderer-features/inject-a-pass-
using-a-scriptable-renderer-feature.html)

Create a Scriptable Renderer Feature in URP

[](../../../urp/renderer-features/create-custom-renderer-feature.html)

Example of a complete Scriptable Renderer Feature in URP

# Apply a Scriptable Renderer Feature to a specific camera type in URP

This guide covers how to apply a Scriptable Renderer Feature to a specific
**camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](../../../CamerasOverview.html)  
See in [Glossary](../../../Glossary.html#Camera) type.

This method allows you to control which cameras the effect of a Scriptable
Renderer Feature applies to. This is particularly relevant when a project uses
additional cameras to render elements such as reflections where the use of the
Scriptable Renderer Feature could lead to unexpected results.

You can add logic to the Scriptable Renderer Feature script to check for a
specific camera type, before the Scriptable Renderer Feature applies the
effect.

This guide is split into the following sections:

  * Prerequisites
  * Apply Scriptable Renderer Feature to a specific Camera

## Prerequisites

This guide assumes that you already have a complete Scriptable Renderer
Feature to work with. If you do not, refer to [How to Create a Custom Renderer
Feature](../create-custom-renderer-feature.html).

##  Apply Scriptable Renderer Feature to Game Cameras

This script applies the Scriptable Renderer Feature to a specific camera type.
In this example, it applies the feature only to Game cameras.

  1. Open the C# script of the Scriptable Renderer Feature you want to apply to the cameras.

  2. In the `AddRenderPasses` method, add the following `if` statement:
    
        if (renderingData.cameraData.cameraType == CameraType.Game)
    

  3. Add the necessary render passes from the Scriptable Renderer Feature to the renderer with the `EnqueuePass` method as shown below.
    
        if (renderingData.cameraData.cameraType == CameraType.Game)
    {
        renderer.EnqueuePass(yourRenderPass);
    }
    

This Scriptable Renderer Feature now only applies to Cameras with the Game
camera type.

> **Note** : Be aware that URP calls the `AddRenderPasses` method at least
> once per camera per frame so it is best to minimise complexity here to avoid
> performance issues.

## Additional resources

  * [Introduction to Scriptable Renderer Features](./intro-to-scriptable-renderer-features.html)
  * [Introduction to Scriptable Render Passes](../intro-to-scriptable-render-passes.html)
  * [How to create a Custom Renderer Feature](../create-custom-renderer-feature.html)

[](../../../urp/renderer-features/scriptable-renderer-features/inject-a-pass-
using-a-scriptable-renderer-feature.html)

Create a Scriptable Renderer Feature in URP

[](../../../urp/renderer-features/create-custom-renderer-feature.html)

Example of a complete Scriptable Renderer Feature in URP

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

