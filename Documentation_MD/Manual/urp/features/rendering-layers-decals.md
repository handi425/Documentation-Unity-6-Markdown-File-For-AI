[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/rendering-layers-decals.html)
  * [中文](/cn/current/Manual/urp/features/rendering-layers-decals.html)
  * [日本語](/ja/current/Manual/urp/features/rendering-layers-decals.html)
  * [한국어](/kr/current/Manual/urp/features/rendering-layers-decals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/rendering-layers-decals.html)
  * [中文](/cn/current/Manual/urp/features/rendering-layers-decals.html)
  * [日本語](/ja/current/Manual/urp/features/rendering-layers-decals.html)
  * [한국어](/kr/current/Manual/urp/features/rendering-layers-decals.html)

  * [Lighting](../../LightingOverview.html)
  * [Lighting in URP](../../urp/lighting-landing.html)
  * [Rendering Layers in URP](../../urp/features/rendering-layers.html)
  * Enable Rendering Layers for Decals in URP

[](../../urp/features/rendering-layers-lights.html)

Enable Rendering Layers for Lights in URP

[](../../urp/lighting/custom-lighting-landing.html)

Custom lighting in URP

# Enable Rendering Layers for Decals in URP

To enable Rendering Layers for decals in your project:

  1. In the **Project** window, select a Renderer asset with a [Decal Renderer Feature](../renderer-feature-decal.html).

  2. In the Decal Renderer Feature, enable **Use Rendering Layers**.

When you enable Rendering Layers for Decals, Unity shows the **Rendering
Layers** property on each Decal Projector.

## Example

This section describes how to configure the following application example:

  * The **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) contains a Decal Projector.

  * The Decal Projector projects a decal on the wall and the ground, but not on the paint bucket.

The following illustration shows the example:

![In image 1, the paint bucket has the Receive decals layer selected. In image
2 it does not, so the Decal Projector does not project on the
bucket.](../../../uploads/urp/lighting/rendering-layers/rendering-layers-
decal-example.png)  
_In image`1`, the paint bucket has the `Receive decals` layer selected. In
image `2` it does not, so the Decal Projector does not project on the bucket._

To implement the example:

  1. Enable Rendering Layers for Decals in your project.

  2. [Create a Decal Projector](../renderer-feature-decal-create.html) in the scene.

  3. Go to **Project Settings** > **Tags and Layers**. Add a Rendering Layer called `Receive decals`.

  4. Select the Decal Projector. In the Rendering Layers property, select `Receive decals`.

  5. Select the paint bucket **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject). In the **Rendering**Layer
Mask** A value defining which layers to include or exclude from an operation,
such as rendering, collision or your own code. [More info](../../Layers.html)  
See in [Glossary](../../Glossary.html#LayerMask)** field, clear the `Receive
decals` layer. Now the Decal Projector does not affect this GameObject.

## Additional resources

  * [`RenderingLayerMask` API](../../../ScriptReference/RenderingLayerMask.html)

[](../../urp/features/rendering-layers-lights.html)

Enable Rendering Layers for Lights in URP

[](../../urp/lighting/custom-lighting-landing.html)

Custom lighting in URP

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

