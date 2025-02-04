[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2d-light-batching-intro.html)
  * [中文](/cn/current/Manual/urp/2d-light-batching-intro.html)
  * [日本語](/ja/current/Manual/urp/2d-light-batching-intro.html)
  * [한국어](/kr/current/Manual/urp/2d-light-batching-intro.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2d-light-batching-intro.html)
  * [中文](/cn/current/Manual/urp/2d-light-batching-intro.html)
  * [日本語](/ja/current/Manual/urp/2d-light-batching-intro.html)
  * [한국어](/kr/current/Manual/urp/2d-light-batching-intro.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * [Optimizing 2D lights](../urp/2d-light-optimize.html)
  * Introduction to 2D light batching

[](../urp/2d-lights-optimize-methods.html)

Optimize 2D lights

[](../urp/2d-light-batching-debugger.html)

Check how Unity batches lights

# Introduction to 2D light batching

Use the **Light Batching Debugger** to visualize how Unity batches [2D
Lights](2DLightProperties.html) and [Shadow Casters](2DShadows.html) according
to the [Sorting Layers](../class-TagManager.html#SortingLayers) they target in
the **scene** A Scene contains the environments and menus of your game. Think
of each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

For Unity to batch Sorting Layers, the layers need to fulfill the following
conditions:

  * The layers share the same sets of Lights; that is, the 2D Lights target the same Sorting Layers.
  * The layers share the same sets of Shadow Casters; that is, the Shadow Casters target the same Sorting Layers.

The debugger compares adjacent batches and highlights the Lights or Shadow
Casters that target each Sorting Layer, and displays which Lights or Shadow
Casters you need to add or remove for Unity to be able to batch the Sorting
Layers.

Check how Unity batches 2D lights in your project with the [Light Batching
Debugger window.](2d-light-batching-debugger.html).

## Examples of different batching scenarios

The following are examples of how Unity batches Lights and Shadow Casters
under different conditions. Each example consists of two Sorting Layers named
**BG** and **Default** , and two Lights named **A** and **B**.

### Scenario 1

**Conditions:**

  * **Lights A** and **B** target both the **BG** and **Default** Sorting Layers.
  * Shadows are disabled for both Lights; that is, there are no Shadow Casters.

![Batch Case 1](../../uploads/urp/2D/light-batching-debugger-4.png) Batch Case
1

**Result:** Unity batches both Lights together as they target the same layers.

![Batch Case 1](../../uploads/urp/2D/light-batching-debugger-5.png) Batch Case
1

### Scenario 2

**Conditions:**

  * **Light A** targets **BG** , while **Light B** targets **Default**.
  * Shadows are disabled for both Lights.

![Batch Case 2](../../uploads/urp/2D/light-batching-debugger-6.png) Batch Case
2

**Result:** Unity doesn’t batch the layers as both Lights target different
Sorting Layers.

![Batch Case 2](../../uploads/urp/2D/light-batching-debugger-7.png) Batch Case
2

### Scenario 3

**Conditions:**

  * Both **Lights A** and **B** target both **BG** and **Default** Sorting Layers.
  * Shadows are enabled for both Lights and the Shadow Casters target both the **BG** and **Default** layers.

![Batch Case 3](../../uploads/urp/2D/light-batching-debugger-8.png) Batch Case
3

**Result:** Unity batches the layers as both Lights and sets of Shadow Casters
target the same layers.

![Batch Case 3](../../uploads/urp/2D/light-batching-debugger-9.png) Batch Case
3

### Scenario 4

**Conditions:** * Both **Lights A** and **B** target both **BG** and
**Default**. * Shadows are only enabled for **Light A** , and the Shadow
Caster targets both **BG** and **Default**.

![Batch Case 4](../../uploads/urp/2D/light-batching-debugger-10.png) Batch
Case 4

**Result:** Unity batches the layers as the Shadow Caster targets both Sorting
Layers so that both layers share the same shadow settings, making the light
texture the same for both layers.

![Batch Case 4](../../uploads/urp/2D/light-batching-debugger-11.png) Batch
Case 4

### Scenario 5

**Conditions:**

  * Both **Lights A** and **B** target both the **BG** and **Default** Sorting Layers.
  * Shadows are enabled for both Lights, and the Shadow Caster only targets the **BG** layer.

![Batch Case 5](../../uploads/urp/2D/light-batching-debugger-12.png) Batch
Case 5

**Result:** Unity doesn’t batch the layers as the Shadow Caster targets one
layer and not the other; this results in the light textures of both layers not
being the same and unable to be batched.

![Batch Case 5](../../uploads/urp/2D/light-batching-debugger-13.png)

[](../urp/2d-lights-optimize-methods.html)

Optimize 2D lights

[](../urp/2d-light-batching-debugger.html)

Check how Unity batches lights

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

