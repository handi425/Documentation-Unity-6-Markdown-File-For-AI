[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CameraTroubleshooting.html)
  * [中文](/cn/current/Manual/CameraTroubleshooting.html)
  * [日本語](/ja/current/Manual/CameraTroubleshooting.html)
  * [한국어](/kr/current/Manual/CameraTroubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CameraTroubleshooting.html)
  * [中文](/cn/current/Manual/CameraTroubleshooting.html)
  * [日本語](/ja/current/Manual/CameraTroubleshooting.html)
  * [한국어](/kr/current/Manual/CameraTroubleshooting.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * Troubleshooting cameras

[](class-Camera.html)

Camera Inspector window reference for the Built-In Render Pipeline

[](Input.html)

Input

# Troubleshooting cameras

Solve common issues with **cameras** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), such as flickering lights and
shadows.

## Reduce flickering

Objects, lights, and shadows might flicker if they’re far away. The flickering
occurs because distances are too large to calculate positions precisely with
floating point math. In each frame, the object, light, or shadow is at a
slightly different position, so it moves in and out of the view frustum.

Minimise flickering using one of the following approaches:

  * Reduce the far **clipping plane** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](class-Camera.html)  
See in [Glossary](Glossary.html#clippingplane) distance in the Camera
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to avoid the distance of
objects becoming too large for precise calculations.

  * Make everything in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) smaller, to reduce distances across
your whole scene.

Unity calculates lights and shadows with the world space position as the
reference point, for example `0, 0, 0` in a 3D scene. Flickering occurs when
lights and shadows are far away from the world space position. To minimise
flickering, you can enable camera-relative culling, so Unity uses the camera
position as the relative position for shadow calculations. See [Culling
settings in Graphics settings](class-GraphicsSettings.html#culling-settings).

## Additional resources

  * [Camera Inspector windows reference for URP](urp/camera-components-reference-landing.html)
  * [Camera Inspector window reference for the Built-In Render Pipeline](class-Camera.html)

[](class-Camera.html)

Camera Inspector window reference for the Built-In Render Pipeline

[](Input.html)

Input

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

