[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2d-light-batching-debugger.html)
  * [中文](/cn/current/Manual/urp/2d-light-batching-debugger.html)
  * [日本語](/ja/current/Manual/urp/2d-light-batching-debugger.html)
  * [한국어](/kr/current/Manual/urp/2d-light-batching-debugger.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2d-light-batching-debugger.html)
  * [中文](/cn/current/Manual/urp/2d-light-batching-debugger.html)
  * [日本語](/ja/current/Manual/urp/2d-light-batching-debugger.html)
  * [한국어](/kr/current/Manual/urp/2d-light-batching-debugger.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * [Optimizing 2D lights](../urp/2d-light-optimize.html)
  * Check how Unity batches lights

[](../urp/2d-light-batching-intro.html)

Introduction to 2D light batching

[](../urp/2DRendererData-overview.html)

2D Renderer asset component reference for URP

# Check how Unity batches lights

To open and use the debugger, follow these steps:

  1. Open the debugger window by going to **Window > 2D > Light Batching Debugger**.  
![Opening the Light Batching Debugger window](../../uploads/urp/2D/light-
batching-debugger-0.png)

  2. View the Light Batching Debugger updates in real time by keeping the Game view and the debugger window open at the same time.  
![Light Batching Debugger window without a selected
batch.](../../uploads/urp/2D/light-batching-debugger-1.png)

  3. Select a batch from the left side of the debugger window to view Lights and Shadow Casters in the current batch.  
![Light Batching Debugger window with selected
batch.](../../uploads/urp/2D/light-batching-debugger-2.png)  
Sorting Layers that are color coded differently means that they’re in
different batches with different **Batch IDs** and aren’t batched together.  
![Differently color coded](../../uploads/urp/2D/light-batching-debugger-
color-1.png)  
Sorting Layers that share the same color code are batched together and will
share the same **Batch ID**.  
![Similarly color coded](../../uploads/urp/2D/light-batching-debugger-
color-2.png)

  4. Select adjacent batches to compare the differences between the selected batches. The debugger window displays the Light(s) and Shadow Caster(s) included in each batch in separate panels.  
![Light Batching Debugger window](../../uploads/urp/2D/light-batching-
debugger-3.png)  
In this example, **Light A** exists in **Batch 0** and not in **Batch 1**. The
debugger provides instructions at the bottom of the window on what you need to
do to have Unity batch the two selected batches together; that is, **Batch 0**
contains **Light A** which currently only targets the **BG** Sorting Layer. By
having **Light A** also target the **Default** Sorting Layer, Unity may be
able to batch both **Batch 0** and **Batch 1** together.

[](../urp/2d-light-batching-intro.html)

Introduction to 2D light batching

[](../urp/2DRendererData-overview.html)

2D Renderer asset component reference for URP

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

