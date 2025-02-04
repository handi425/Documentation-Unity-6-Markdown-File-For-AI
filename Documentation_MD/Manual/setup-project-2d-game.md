[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/setup-project-2d-game.html)
  * [中文](/cn/current/Manual/setup-project-2d-game.html)
  * [日本語](/ja/current/Manual/setup-project-2d-game.html)
  * [한국어](/kr/current/Manual/setup-project-2d-game.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/setup-project-2d-game.html)
  * [中文](/cn/current/Manual/setup-project-2d-game.html)
  * [日本語](/ja/current/Manual/setup-project-2d-game.html)
  * [한국어](/kr/current/Manual/setup-project-2d-game.html)

  * [Working in Unity](working-in-unity.html)
  * [2D in Unity](Unity2D.html)
  * [2D game development](2d-game-development-landing.html)
  * Setup a project for 2D games

[](2d-game-development-landing.html)

2D game development

[](2d-game-creation-wokflow.html)

2D game creation workflow

# Setup a project for 2D games

**Note** : For this guide, Unity recommends and assumes that you choose the
[Universal Render Pipeline (URP)](universal-render-pipeline.html) and not the
[Built-in Render Pipeline](built-in-render-pipeline.html).

  1. Install Unity version 2019 LTS or a later version; see [Installing Unity](GettingStartedInstallingUnity.html).

  2. Create a new project with the [2D template](https://docs.unity3d.com/hub/manual/Templates.html).

  3. In the Package Manager, install the latest [URP package](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest) version; see [Installing the Universal Render Pipeline into an existing Project](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/manual/InstallURPIntoAProject.html).

  4. Install any optional packages you need; see Installing packages.

## Installing packages

Most packages you need to make a 2D game in Unity are included in the Unity
Editor. The following table lists the packages included by default when you
choose the [2D template](https://docs.unity3d.com/hub/manual/Templates.html):

**Package** | **Description**  
---|---  
[2D Animation](https://docs.unity3d.com/Packages/com.unity.2d.animation@latest) | 2D Animation provides the necessary tooling and runtime components for applying skeletal animation to your **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite).  
[2D Pixel Perfect](urp/2d-pixelperfect.html) | The 2D **Pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) Perfect package contains the Pixel
Perfect **Camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) component, which ensures your pixel
art remains crisp and clear at different resolutions, and stable in motion. A
standalone [2D Pixel Perfect
package](https://docs.unity3d.com/Packages/com.unity.2d.pixel-perfect@latest)
that doesn’t require the URP is available if you want to use this package in a
project using the [Built-in Render Pipeline](built-in-render-pipeline.html)
instead.  
[2D PSD Importer](https://docs.unity3d.com/Packages/com.unity.2d.psdimporter@latest) | The 2D PSD Importer package allows you to import multilayered PSD files from Photoshop. You can use this for your Sprites, or to rig your characters.  
[2D Sprite](sprite/sprite-landing.html) | The Sprite Editor provides an in-Editor environment to create and edit Sprite assets. Sprite Editor lets you add custom behavior for editing Sprite-related data.  
[2D SpriteShape](https://docs.unity3d.com/Packages/com.unity.2d.spriteshape@latest) | 2D Sprite Shape allows you to create organic shapes and **terrains** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain), similar to a vector drawing tool.
For example, you can choose the fill texture and border Sprites.  
[2D Tilemap Editor](tilemaps/work-with-tilemaps/tilemap-reference.html) | 2D **Tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](Glossary.html#Tilemap) Editor allows you to create grid-
based worlds with square, hexagonal or isometric tiles. Add your Tiles to the
Tile Palette, and paint and fill Tile Grids using different settings and
brushes. Extra tools let you add smart drawing, randomization or animation to
the Tile assets.  
  
The following table lists some optional packages you can install that might be
particularly useful for 2D game development:

**Package** | **Description**  
---|---  
[Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest) | **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) Graph lets you build your shaders
visually.  
[Cinemachine](https://docs.unity3d.com/Packages/com.unity.cinemachine@latest) | The Cinemachine package is a suite of modules that provide advanced functionality for operating the Unity Camera.  
[2D Tilemap Extras](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest) | The 2D Tilemap Extras package contains reusable 2D and Tilemap Editor **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that you can use for your own
Projects.  
  
[](2d-game-development-landing.html)

2D game development

[](2d-game-creation-wokflow.html)

2D game creation workflow

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

