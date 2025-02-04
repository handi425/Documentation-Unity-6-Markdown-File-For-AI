[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TroubleShooting.html)
  * [中文](/cn/current/Manual/TroubleShooting.html)
  * [日本語](/ja/current/Manual/TroubleShooting.html)
  * [한국어](/kr/current/Manual/TroubleShooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TroubleShooting.html)
  * [中文](/cn/current/Manual/TroubleShooting.html)
  * [日本語](/ja/current/Manual/TroubleShooting.html)
  * [한국어](/kr/current/Manual/TroubleShooting.html)

  * [Working in Unity](working-in-unity.html)
  * Troubleshooting

[](urp/2d-pixelperfect-ref.html)

Pixel Perfect Camera component reference for URP

[](CreatingEnvironments.html)

World building

# Troubleshooting

This section addresses common problems that can arise when using Unity. The
section addresses each platform separately.

## Platform-specific troubleshooting

### GeForce 7300 GT on macOS 10.6.4

Materials aren’t displayed correctly for GeForce 7300 GT on macOS 10.6.4 due
to buggy video drivers, so the system disables deferred rendering.

## Script editing

### Script opens in default system text editor, even when Visual Studio is set
as the script editor

This happens when Visual Studio reports that it failed to open your script.
The most common cause for this is an external **plug-in** A set of code
created outside of Unity that creates functionality in Unity. There are two
kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) (such as ReSharper) displaying a
dialog at startup, requesting input from the user. This causes Visual Studio
to report that it failed to open.

## Graphics

### Slow frame rate and/or visual artifacts

This might occur if your video card drivers aren’t up to date. Make sure you
have the latest official drivers from your card vendor.

## Shadows

  * Shadows require certain graphics hardware support. Refer to [Shadow Performance](ShadowPerformance.html) page for details.
  * Make sure shadows are enabled in the [Quality](class-QualitySettings.html) window.
  * Shadows on Android and iOS have limitations: soft shadows aren’t available, and in forward **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) only a single directional light
can cast shadows. There is no limit to the number of lights casting shadows in
the deferred rendering path.

### Some GameObjects don’t cast or receive shadows

An object’s [Renderer](class-MeshRenderer.html) must have **Receive Shadows**
enabled for shadows to be rendered onto it. Also, an object must have **Cast
Shadows** enabled to cast shadows on other objects (both are on by default).

Only opaque objects cast and receive shadows. This means that objects using
the built-in [Transparent](shader-TransparentFamily.html) or Particle shaders
will not cast shadows. Usually it’s possible to use [Transparent
Cutout](shader-TransparentCutoutFamily.html) shaders for objects like fences,
vegetation, etc. If you use custom written [Shaders](Shaders.html)A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), they have to be pixel-lit and use the
[Geometry render queue](SL-SubShaderTags.html). Objects using **VertexLit**
shaders don’t receive shadows but are able to cast them.

Only **Pixel lights** cast shadows. If you want to make sure that a light
always casts shadows no matter how many other lights are in the **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), then you can set it to **Force Pixel**
render mode (refer to the [Light](class-Light.html) reference page).

[](urp/2d-pixelperfect-ref.html)

Pixel Perfect Camera component reference for URP

[](CreatingEnvironments.html)

World building

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

