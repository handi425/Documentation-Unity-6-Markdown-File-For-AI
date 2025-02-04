[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/line-rendering-introduction.html)
  * [中文](/cn/current/Manual/line-rendering-introduction.html)
  * [日本語](/ja/current/Manual/line-rendering-introduction.html)
  * [한국어](/kr/current/Manual/line-rendering-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/line-rendering-introduction.html)
  * [中文](/cn/current/Manual/line-rendering-introduction.html)
  * [日本語](/ja/current/Manual/line-rendering-introduction.html)
  * [한국어](/kr/current/Manual/line-rendering-introduction.html)

  * [Visual effects](visual-effects.html)
  * [Lines and trails](visual-effects-lines-trails-billboards.html)
  * [Rendering lines](rendering-lines.html)
  * Rendering lines

[](rendering-lines.html)

Rendering lines

[](draw-configure-line-3d-space.html)

Draw and configure a line in 3D space

# Rendering lines

The ****Line Renderer** A component that takes an array of two or more points
in 3D space and draws a straight line between each one. You can use a single
Line Renderer component to draw anything from a simple straight line to a
complex spiral. [More info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer)** component takes an array of
two or more points in 3D space, and draws a straight line between each one.
You can use a Line Renderer to draw anything from a simple straight line to a
complex spiral.

The line is always continuous; if you need to draw two or more completely
separate lines, you should use multiple **GameObjects** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), each with its own Line Renderer.

The Line Renderer does not render lines that have a width in **pixels** The
smallest unit in a computer image. Pixel size depends on your screen
resolution. Pixel lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel). It renders polygons that have a width
in world units. The Line Renderer uses the same algorithm for line rendering
as the [Trail Renderer](class-TrailRenderer.html)A visual effect that lets you
to make trails behind GameObjects in the Scene as they move. [More
info](class-TrailRenderer.html)  
See in [Glossary](Glossary.html#TrailRenderer).

[](rendering-lines.html)

Rendering lines

[](draw-configure-line-3d-space.html)

Draw and configure a line in 3D space

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

