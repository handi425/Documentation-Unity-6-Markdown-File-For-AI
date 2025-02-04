[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/PrepShader.html)
  * [中文](/cn/current/Manual/urp/PrepShader.html)
  * [日本語](/ja/current/Manual/urp/PrepShader.html)
  * [한국어](/kr/current/Manual/urp/PrepShader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/PrepShader.html)
  * [中文](/cn/current/Manual/urp/PrepShader.html)
  * [日本語](/ja/current/Manual/urp/PrepShader.html)
  * [한국어](/kr/current/Manual/urp/PrepShader.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * Prepare and upgrade sprites for 2D lighting in URP

[](../urp/Setup.html)

Set up the 2D Renderer asset in URP

[](../urp/2d/tilemap-renderer-2d-renderer.html)

Enable 2D lighting with the Tilemap Renderer in URP

# Prepare and upgrade sprites for 2D lighting in URP

Prepare your **sprites** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../sprite/sprite-landing.html)  
See in [Glossary](../Glossary.html#Sprite) and existing materials to be lit by
2D lighting.

To light a sprite with [2D lights](2DLightProperties.html), first go to the
[Sprite Renderer](../sprite/renderer/renderer-landing.html)A component that
lets you display images as Sprites for use in both 2D and 3D scenes. [More
info](../sprite/renderer/renderer-landing.html)  
See in [Glossary](../Glossary.html#SpriteRenderer) component of the sprite and
assign a material with a **Shader** A program that runs on the GPU. [More
info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) that reacts to 2D lights. When you
drag sprites onto the **scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene), Unity automatically assigns the
`Sprite-Lit-Default` material to them which enables them to interact and
appear lit by 2D lights.

You can also [create a custom Shader](ShaderGraph.html) that reacts to lights
with the [Shader Graph
package](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest).

## Upgrading existing materials

If you are installing the URP package into an existing project with
preexisting **prefabs** An asset type that allows you to store a GameObject
complete with components and properties. The prefab acts as a template from
which you can create new object instances in the scene. [More
info](../Prefabs.html)  
See in [Glossary](../Glossary.html#Prefab), materials or scenes, you will need
to upgrade any materials used to a lighting compatible Shader if you want to
use the package’s 2D lighting features.

**Warning:** The following task automatically upgrades a scene or project in a
one way process. Unity can’t revert upgraded scenes or projects to their
previous state. Before you start this task, back up any files you don’t want
to lose or converted.

To upgrade your project, go to **Window > Rendering > Render Pipeline
Converter**. Enable **Material Upgrade** and then select **Convert Assets** to
begin the upgrade.

For information on converting assets made for a Built-in **Render Pipeline** A
series of operations that take the contents of a Scene, and displays them on a
screen. Unity lets you choose from pre-built render pipelines, or write your
own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) project to assets
compatible with 2D URP, refer to [Render Pipeline Converter](features/rp-
converter.html).

[](../urp/Setup.html)

Set up the 2D Renderer asset in URP

[](../urp/2d/tilemap-renderer-2d-renderer.html)

Enable 2D lighting with the Tilemap Renderer in URP

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

