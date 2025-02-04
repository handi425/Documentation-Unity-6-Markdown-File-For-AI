[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PerPixelLights-BuiltIn.html)
  * [中文](/cn/current/Manual/PerPixelLights-BuiltIn.html)
  * [日本語](/ja/current/Manual/PerPixelLights-BuiltIn.html)
  * [한국어](/kr/current/Manual/PerPixelLights-BuiltIn.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PerPixelLights-BuiltIn.html)
  * [中文](/cn/current/Manual/PerPixelLights-BuiltIn.html)
  * [日本語](/ja/current/Manual/PerPixelLights-BuiltIn.html)
  * [한국어](/kr/current/Manual/PerPixelLights-BuiltIn.html)

  * [Lighting](LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * Per-pixel and per-vertex lights in the Built-In Render Pipeline

[](lighting-birp.html)

Lighting in the Built-In Render Pipeline

[](lighting-emissive-materials.html)

Emit light from a GameObject in the Built-In Render Pipeline

# Per-pixel and per-vertex lights in the Built-In Render Pipeline

If you use the default [Forward rendering path](rendering-paths-
introduction.html), Unity sets each realtime Light component as one of the
following types:

  * Per-pixel light
  * Per-vertex light
  * Spherical harmonics (SH) per-vertex light

For more information, refer to [Per-pixel and per-vertex
lights](PerPixelLights.html).

The Built-In **Render Pipeline** A series of operations that take the contents
of a Scene, and displays them on a screen. Unity lets you choose from pre-
built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) renders each **GameObject**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) once for each per-pixel light that
affects it.

SH lights are fast, and have little or no performance impact. However, SH
lights don’t support cookies, **normal maps** A type of Bump Map texture that
allows you to add surface detail such as bumps, grooves, and scratches to a
model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap), or specular highlights. They also
have sharp lighting transitions, and might look incorrect.

## How Unity classifies lights

By default, Unity groups lights using the following criteria:

  * The brightest light is always a per-pixel light. This is usually the main Directional Light.
  * The 4 next most important lights are per-vertex lights.
  * The remaining lights are SH lights.

During rendering, Unity finds all lights surrounding a **mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) and calculates which of those lights
affect it most.

For example, in the following image where a sphere GameObject is lit by 8
lights with the same color and intensity, Unity sets the four closest lights
(A to D) as per-pixel lights, lights D to G to per-vertex lights, and lights G
and H as SH lights. Each per-pixel light creates a separate render pass.

![A sphere GameObject lit by 8
lights](../uploads/Main/ForwardLightsExample.png) A sphere GameObject lit by 8
lights ![How Unity classifies the
lights](../uploads/Main/ForwardLightsClassify.png) How Unity classifies the
lights

To help avoid visible light transitions when GameObjects and lights move,
Unity blends lights from one mode to another. In the preceding example, Unity
blends light D from a per-pixel light to a per-vertex light.

For information about optimizing how Unity classifies lights, refer to
[Optimize lighting in the Built-In Render Pipeline](lighting-optimize-
builtin.html).

## Additional resources

  * [Per-pixel and per-vertex lights](PerPixelLights.html)

[](lighting-birp.html)

Lighting in the Built-In Render Pipeline

[](lighting-emissive-materials.html)

Emit light from a GameObject in the Built-In Render Pipeline

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

