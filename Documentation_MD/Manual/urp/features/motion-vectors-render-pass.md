[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/motion-vectors-render-pass.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-render-pass.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-render-pass.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-render-pass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/motion-vectors-render-pass.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-render-pass.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-render-pass.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-render-pass.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Motion vectors in URP](../../urp/features/motion-vectors-landing.html)
  * Motion vectors render pass in URP

[](../../urp/features/motion-vectors-shader-support.html)

Built-in shader support for motion vectors in URP

[](../../urp/features/motion-vectors-custom-shader.html)

Output a motion vector texture in a custom shader in URP

# Motion vectors render pass in URP

Understand how the **MotionVectors** render pass renders the motion vector
texture.

## Location in the frame loop

URP renders motion vectors at the `BeforeRenderingPostProcessing` event.
Before that event the motion vector texture might not be set or might contain
previous frame’s motion vector data.

## MotionVectors pass structure

URP renders the motion vector texture in 2 steps:

  1. URP renders the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) motion vectors in the
**MotionVectors** full-screen pass. This pass uses the depth texture and the
camera matrices for the current and the previous frames to calculate the
camera motion vectors. This pass has a fixed per-camera computation load and
does not require special motion vector support from renderers or materials.

  2. URP draws a per-object motion vector **shader** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) pass for [each renderer and
material combination that supports motion vectors](motion-vectors.html#cases-
when-motion-vectors).

[](../../urp/features/motion-vectors-shader-support.html)

Built-in shader support for motion vectors in URP

[](../../urp/features/motion-vectors-custom-shader.html)

Output a motion vector texture in a custom shader in URP

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

