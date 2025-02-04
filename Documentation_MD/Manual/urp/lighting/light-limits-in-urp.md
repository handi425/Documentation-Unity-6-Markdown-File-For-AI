[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/lighting/light-limits-in-urp.html)
  * [中文](/cn/current/Manual/urp/lighting/light-limits-in-urp.html)
  * [日本語](/ja/current/Manual/urp/lighting/light-limits-in-urp.html)
  * [한국어](/kr/current/Manual/urp/lighting/light-limits-in-urp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/lighting/light-limits-in-urp.html)
  * [中文](/cn/current/Manual/urp/lighting/light-limits-in-urp.html)
  * [日本語](/ja/current/Manual/urp/lighting/light-limits-in-urp.html)
  * [한국어](/kr/current/Manual/urp/lighting/light-limits-in-urp.html)

  * [Lighting](../../LightingOverview.html)
  * [Lighting in URP](../../urp/lighting-landing.html)
  * Light limits in URP

[](../../urp/lighting/lighting-in-urp.html)

Introduction to lighting in the Universal Render Pipeline

[](../../urp/lights-placement-tool.html)

View and control a light from its perspective in URP

# Light limits in URP

If you use the default Forward [rendering path](../rendering-paths-
introduction-urp.html)The technique that a render pipeline uses to render
graphics. Choosing a different rendering path affects how lighting and shading
are calculated. Some rendering paths are more suited to different platforms
and hardware than others. [More info](../../RenderingPaths.html)  
See in [Glossary](../../Glossary.html#RenderingPath), the Universal **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (URP) has a maximum of 9
lights for each **GameObject** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject):

  * 1 Main Light, which is a per-pixel light by default. This is the main Directional Light in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene), or the brightest light.

  * 8 Additional Lights, which are also per-pixel lights by default. You can set them as per-vertex lights instead.

For more information about per-pixel and per-vertex lights, refer to [Per-
pixel and per-vertex lights](../../PerPixelLights.html).

There are also the following limits per **camera** A component which creates
an image of a particular viewpoint in your scene. The output is either drawn
to the screen or captured as a texture. [More
info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera):

  * Desktop and console platforms: 256 Additional Lights
  * Mobile platforms: 32 Additional Lights.
  * OpenGL ES 3.0 and earlier: 16 Additional Lights.

The Main Light is always visible per camera.

To add more lights per object or per camera, use the Forward+ or Deferred
rendering paths instead. For more information, refer to [Choose a rendering
path in URP](../rendering-paths-comparison.html)

## Additional resources

  * [Lighting settings in the URP Asset Inspector window](../universalrp-asset.html#lighting)

[](../../urp/lighting/lighting-in-urp.html)

Introduction to lighting in the Universal Render Pipeline

[](../../urp/lights-placement-tool.html)

View and control a light from its perspective in URP

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

