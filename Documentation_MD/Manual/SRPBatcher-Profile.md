[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SRPBatcher-Profile.html)
  * [中文](/cn/current/Manual/SRPBatcher-Profile.html)
  * [日本語](/ja/current/Manual/SRPBatcher-Profile.html)
  * [한국어](/kr/current/Manual/SRPBatcher-Profile.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SRPBatcher-Profile.html)
  * [中文](/cn/current/Manual/SRPBatcher-Profile.html)
  * [日本語](/ja/current/Manual/SRPBatcher-Profile.html)
  * [한국어](/kr/current/Manual/SRPBatcher-Profile.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [Scriptable Render Pipeline (SRP) Batcher in URP](SRPBatcher-landing.html)
  * Troubleshoot the SRP Batcher in URP

[](SRPBatcher-Enable.html)

Enable the SRP Batcher in URP

[](SRPBatcher-Incompatible.html)

Remove SRP Batcher compatibility for GameObjects in URP

# Troubleshoot the SRP Batcher in URP

You can check the status of SRP batches in the [Frame
Debugger](FrameDebugger.html) window. Each SRP Batch displays how many draw
calls Unity used, which keywords Unity attached to the **shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), and the reason why Unity didn’t batch
that draw call with the previous one.

To check the status of SRP Batcher batches:

  1. In the Editor, open the Frame Debugger (menu: **Window** > **Analysis** > **Frame Debugger**).
  2. In the Frame Debugger, go to **Render Camera** > **Render Opaques**.
  3. Expand the **RenderLoopNewBatcher. Draw** list.
  4. Select on the **SRP Batch** you want to inspect.

In the example below, the reason is: **Nodes have different shaders**. This
means that the shader for that SRP batch is different to the one in the
previous SRP batch. Because the SRP Batcher used a different shader, the SRP
Batcher created a new batch. If several SRP batches have a low number of draw
calls, it often means the project uses too many shader variants.

![In the Frame Debugger window, you can find details about individual SRP
batches, including why the SRP Batcher created a new SRP batch instead of
continuing the existing
one.](../uploads/Main/SRP_Batcher_batch_information.png) In the Frame Debugger
window, you can find details about individual SRP batches, including why the
SRP Batcher created a new SRP batch instead of continuing the existing one.

If you write your own Scriptable **Render Pipeline** A series of operations
that take the contents of a Scene, and displays them on a screen. Unity lets
you choose from pre-built render pipelines, or write your own. [More
info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), instead of using either the
Universal Render Pipeline or the High Definition Render Pipeline, try to write
a generic multi-purpose shader with a minimal number of keywords. This is
optimal because you can use as many material properties as you want.

[](SRPBatcher-Enable.html)

Enable the SRP Batcher in URP

[](SRPBatcher-Incompatible.html)

Remove SRP Batcher compatibility for GameObjects in URP

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

