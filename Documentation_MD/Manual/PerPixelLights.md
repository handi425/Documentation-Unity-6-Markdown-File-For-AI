[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PerPixelLights.html)
  * [中文](/cn/current/Manual/PerPixelLights.html)
  * [日本語](/ja/current/Manual/PerPixelLights.html)
  * [한국어](/kr/current/Manual/PerPixelLights.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PerPixelLights.html)
  * [中文](/cn/current/Manual/PerPixelLights.html)
  * [日本語](/ja/current/Manual/PerPixelLights.html)
  * [한국어](/kr/current/Manual/PerPixelLights.html)

  * [Lighting](LightingOverview.html)
  * [Light sources](lighting-light-sources.html)
  * [Light components](lighting-light-components.html)
  * Per-pixel and per-vertex lights

[](Lighting.html)

Types of Light component

[](UsingLights.html)

Place Light components

# Per-pixel and per-vertex lights

If you use the default [Forward rendering path](rendering-paths-
introduction.html#forward), each realtime Light component can be one of the
following types:

  * A per-pixel light, which lights each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) of an object accurately.

  * A per-vertex light, which lights each vertex of an object accurately. Unity interpolates lighting for the pixels between vertices.

Per-pixel lights give more accurate results but reduce performance.

The Built-In **Render Pipeline** A series of operations that take the contents
of a Scene, and displays them on a screen. Unity lets you choose from pre-
built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) also sets some lights as
Spherical Harmonic (SH) per-vertex lights, which are the least accurate but
render the fastest.

For more information, refer to the following:

  * [Light limits in the Universal Render Pipeline (URP)](urp/lighting/light-limits-in-urp.html)
  * [Per-pixel and per-vertex lights in the Built-In Render Pipeline](PerPixelLights-BuiltIn.html)

## Additional resources

  * [Choose a lighting setup](choose-a-lighting-setup.html)
  * [Introduction to rendering paths](rendering-paths-introduction.html)

[](Lighting.html)

Types of Light component

[](UsingLights.html)

Place Light components

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

