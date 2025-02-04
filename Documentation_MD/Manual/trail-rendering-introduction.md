[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/trail-rendering-introduction.html)
  * [中文](/cn/current/Manual/trail-rendering-introduction.html)
  * [日本語](/ja/current/Manual/trail-rendering-introduction.html)
  * [한국어](/kr/current/Manual/trail-rendering-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/trail-rendering-introduction.html)
  * [中文](/cn/current/Manual/trail-rendering-introduction.html)
  * [日本語](/ja/current/Manual/trail-rendering-introduction.html)
  * [한국어](/kr/current/Manual/trail-rendering-introduction.html)

  * [Visual effects](visual-effects.html)
  * [Lines and trails](visual-effects-lines-trails-billboards.html)
  * [Rendering trails](rendering-trails.html)
  * Rendering trails for moving GameObjects

[](rendering-trails.html)

Rendering trails

[](draw-configure-trail-behind-moving-gameobject.html)

Draw and configure a trail behind a moving GameObject

# Rendering trails for moving GameObjects

The **Trail Renderer** A visual effect that lets you to make trails behind
GameObjects in the Scene as they move. [More info](class-TrailRenderer.html)  
See in [Glossary](Glossary.html#TrailRenderer) component renders a trail of
polygons behind a moving **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), over time. This can be used to
give an emphasized feeling of motion to a moving object, or to highlight the
path or position of moving objects.

The Trail Renderer uses the same algorithm for trail rendering as the [Line
Renderer](class-LineRenderer.html)A component that takes an array of two or
more points in 3D space and draws a straight line between each one. You can
use a single Line Renderer component to draw anything from a simple straight
line to a complex spiral. [More info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer).

## Distance between trail points

The **Min Vertex Distance** value determines how far in world units the
GameObject to which the trail applies must travel before a new segment is
added to the trail. Low values like 0.1 create trail segments more often,
creating smoother trails. Higher values like 1.5 create segments that are more
jagged in appearance. Additionally, wide trails may exhibit visual artifacts
when the vertices are very close together and the trail changes direction
significantly over a short distance.

For performance reasons, it is best to use the largest possible value that
achieves the effect you are trying to create.

[](rendering-trails.html)

Rendering trails

[](draw-configure-trail-behind-moving-gameobject.html)

Draw and configure a trail behind a moving GameObject

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

