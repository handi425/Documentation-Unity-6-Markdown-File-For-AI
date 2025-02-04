[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/scriptable-render-pipeline-introduction.html)
  * [中文](/cn/current/Manual/scriptable-render-pipeline-introduction.html)
  * [日本語](/ja/current/Manual/scriptable-render-pipeline-introduction.html)
  * [한국어](/kr/current/Manual/scriptable-render-pipeline-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/scriptable-render-pipeline-introduction.html)
  * [中文](/cn/current/Manual/scriptable-render-pipeline-introduction.html)
  * [日本語](/ja/current/Manual/scriptable-render-pipeline-introduction.html)
  * [한국어](/kr/current/Manual/scriptable-render-pipeline-introduction.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * Scriptable Render Pipeline fundamentals

[](render-pipelines-overview.html)

Introduction to render pipelines

[](choose-a-render-pipeline-landing.html)

Choosing a render pipeline

# Scriptable Render Pipeline fundamentals

This page explains how Unity’s [Scriptable Render Pipeline (SRP)](scriptable-
render-pipeline-introduction.html) works, and introduces some key concepts and
terminology. The information on this page is applicable to the Universal
**Render Pipeline** A series of operations that take the contents of a Scene,
and displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP), the High Definition
Render Pipeline (HDRP), and custom render pipelines that are based on SRP.

The Scriptable Render Pipeline is a thin API layer that lets you schedule and
configure rendering commands using C# **scripts** A piece of code that allows
you to create your own Components, trigger game events, modify Component
properties over time and respond to user input in any way you like. [More
info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). Unity passes these commands to its
low-level graphics architecture, which then sends instructions to the graphics
API.

URP and HDRP are built on top of SRP. You can also create your own custom
render pipeline on top of SRP.

## Render Pipeline Instance and Render Pipeline Asset

Every render pipeline based on SRP has two key customized elements:

  * A **Render Pipeline Instance**. This is an instance of a class that defines the functionality of your render pipeline. Its script inherits from [RenderPipeline](../ScriptReference/Rendering.RenderPipeline.html), and overrides its `Render()` method.
  * A **Render Pipeline Asset**. This is an asset in your Unity Project that stores data about which Render Pipeline Instance to use, and how to configure it. Its script inherits from [RenderPipelineAsset](../ScriptReference/Rendering.RenderPipelineAsset.html) and overrides its `CreatePipeline()` method.

For more information on these elements, and instructions on how to create them
in a custom render pipeline, see [Creating a Render Pipeline Asset and a
Render Pipeline Instance](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@17.0/manual/index.html).

## ScriptableRenderContext

`ScriptableRenderContext` is a class that acts as an interface between the
custom C# code in the render pipeline and Unity’s low-level graphics code.

Use the
[ScriptableRenderContext](../ScriptReference/Rendering.ScriptableRenderContext.html)
API to schedule and execute rendering commands. For information, see
[Scheduling and executing rendering commands in the Scriptable Render
Pipeline](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@17.0/manual/srp-using-scriptable-render-context.html).

## Additional resources

  * [Universal Render Pipeline](universal-render-pipeline.html)
  * [High Definition Render Pipeline](high-definition-render-pipeline.html)
  * [Creating a custom render pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/srp-custom.html)

[](render-pipelines-overview.html)

Introduction to render pipelines

[](choose-a-render-pipeline-landing.html)

Choosing a render pipeline

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

