[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)
  * [中文](/cn/current/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)
  * [中文](/cn/current/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../urp/customizing-urp.html)
  * Introduction to Scriptable Render Passes in URP

[](../../urp/customizing-urp.html)

Custom rendering and post-processing in URP

[](../../urp/urp-renderer-feature-landing.html)

Adding pre-built effects via Renderer Features in URP

# Introduction to Scriptable Render Passes in URP

Scriptable Render Passes are a way to alter how Unity renders a **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) or the objects within a scene.
They allow you to fine tune how Unity renders each scene in your project on a
scene-by-scene basis.

You inject a Scriptable Render Pass into the **render pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) to achieve a custom
visual effect. For more information, refer to [Adding a Scriptable Render Pass
to the frame rendering loop](../inject-a-render-pass.html).

A Scriptable Render Pass lets you to do the following:

  * Change the properties of materials in your scene.
  * Change the order that Unity renders **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) in.

  * Lets Unity read **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) buffers and use them in
**shaders** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader).

For example, you can use a Scriptable Render Pass to blur a camera’s view when
showing the in-game menu.

Unity injects Scriptable Render Passes at certain points during the URP render
loop. These points are called injection points. You can change the injection
point Unity inserts your pass at to control how the Scriptable Render Pass
affects the appearance of your scene. For more information on injection
points, refer to [Injection Points](../customize/custom-pass-injection-
points.html).

## Additional resources

  * [Adding pre-built effects with Renderer Features in URP](../urp-renderer-feature-landing.html)
  * [How to create a Custom Renderer Feature](create-custom-renderer-feature.html)
  * [Scriptable Renderer Feature Reference](scriptable-renderer-features/scriptable-renderer-feature-reference.html)
  * [How to inject a Custom Render Pass via scripting](../customize/custom-pass-injection-points.html)

[](../../urp/customizing-urp.html)

Custom rendering and post-processing in URP

[](../../urp/urp-renderer-feature-landing.html)

Adding pre-built effects via Renderer Features in URP

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

