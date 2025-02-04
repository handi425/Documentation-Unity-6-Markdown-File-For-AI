[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/draw-configure-trail-behind-moving-gameobject.html)
  * [中文](/cn/current/Manual/draw-configure-trail-behind-moving-gameobject.html)
  * [日本語](/ja/current/Manual/draw-configure-trail-behind-moving-gameobject.html)
  * [한국어](/kr/current/Manual/draw-configure-trail-behind-moving-gameobject.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/draw-configure-trail-behind-moving-gameobject.html)
  * [中文](/cn/current/Manual/draw-configure-trail-behind-moving-gameobject.html)
  * [日本語](/ja/current/Manual/draw-configure-trail-behind-moving-gameobject.html)
  * [한국어](/kr/current/Manual/draw-configure-trail-behind-moving-gameobject.html)

  * [Visual effects](visual-effects.html)
  * [Lines and trails](visual-effects-lines-trails-billboards.html)
  * [Rendering trails](rendering-trails.html)
  * Draw and configure a trail behind a moving GameObject

[](trail-rendering-introduction.html)

Rendering trails for moving GameObjects

[](class-TrailRenderer.html)

Trail Renderer component reference

# Draw and configure a trail behind a moving GameObject

To create a **Trail Renderer** A visual effect that lets you to make trails
behind GameObjects in the Scene as they move. [More info](class-
TrailRenderer.html)  
See in [Glossary](Glossary.html#TrailRenderer):

  1. In the Unity menu bar, go to **GameObject** > **Effects** > **Trail**.
  2. Select the Trail Renderer **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), and parent it to the GameObject
that you want it to generate a trail for.

  3. Use the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to configure the color,
width, and other display settings of the trail.

  4. Preview the trail in Edit Mode by moving the GameObject and observing the effect in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view.

![An example Trail Renderer configuration, and the resulting
trail.](../uploads/Main/TrailRenderer-example2.jpg) An example Trail Renderer
configuration, and the resulting trail.

## Set the Trail Renderer Material

By default, a Trail Renderer uses the built-in Material, **Default-Line**. You
can make many changes to the appearance of the trail without changing this
Material, such as editing the color gradient or width of the trail.

For other effects, such as applying a texture to the trail, you will need to
use a different Material. If you do not want to write your own **Shader** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) for the new Material, Unity’s built-in
[Standard Particle Shaders](shader-StandardParticleShaders.html) work well
with Trail Renderers. If you apply a Texture to a Trail Renderer, the Texture
should be of square dimensions (for example 256x256, or 512x512).

If you apply more than one Material to a Trail Renderer, the trail is rendered
once for each Material.

See [Creating and using Materials](Materials.html) for more information.

[](trail-rendering-introduction.html)

Rendering trails for moving GameObjects

[](class-TrailRenderer.html)

Trail Renderer component reference

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

