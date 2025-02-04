[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sky.html)
  * [中文](/cn/current/Manual/sky.html)
  * [日本語](/ja/current/Manual/sky.html)
  * [한국어](/kr/current/Manual/sky.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sky.html)
  * [中文](/cn/current/Manual/sky.html)
  * [日本語](/ja/current/Manual/sky.html)
  * [한국어](/kr/current/Manual/sky.html)

  * [World building](CreatingEnvironments.html)
  * [Sky](sky-landing.html)
  * Sky

[](sky-landing.html)

Sky

[](skyboxes-using.html)

Create a skybox

# Sky

A sky is a type of background that a **Camera** A component which creates an
image of a particular viewpoint in your scene. The output is either drawn to
the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) draws before it renders a frame. This
type of background greatly benefits 3D games and applications because it
provides a sense of depth and makes the environment seem much larger than it
actually is. The sky itself can contain anything, such as clouds, mountains,
buildings, and other unreachable objects, to create the illusion of distant
three-dimensional surroundings. Unity can also use a sky to generate realistic
ambient lighting in your **Scene** A Scene contains the environments and menus
of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

![The High Definition Render Pipelines Physically Based Sky in the
Fontainebleau demo.](../uploads/Main/HDRP-PBSky.png) The High Definition
Render Pipeline’s Physically Based Sky in the Fontainebleau demo.

## Sky and render pipelines

The sky solutions you can use depend on which [render pipeline](render-
pipelines.html)A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) your Project uses.

**Render pipeline** | **Sky Solution**  
---|---  
[**Universal Render Pipeline (URP)**](universal-render-pipeline.html) | URP uses the same sky solution as the Built-in Render Pipeline and allows you to specify the sky on a per-Scene basis and override the sky for an individual Camera.  
  
• For information on how to set the sky on a per-Scene basis, see the
[Lighting window documentation](lighting-window.html).  
• For information on how to override the sky for a specific Camera, see the
[Skybox component documentation](sky-landing.html).  
[**High Definition Render Pipeline (HDRP)**](high-definition-render-pipeline.html) | HDRP includes its own sky solution that uses the [Volume system](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Volumes.html). Each Volume can include an override to specify a type of sky to draw. Each Camera interpolates between the sky settings for every Volume that affects it and draws the result.  
  
For information on how to create a sky in HDRP, see the [Visual Environment
documentation](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.high-definition@latest/index.html?subfolder=/manual/Override-Visual-
Environment.html).  
[**Built-in Render Pipeline**](built-in-render-pipeline.html) | The Built-in Render Pipeline uses a skybox Material to define a sky for Cameras to draw. You can specify the sky on a per-Scene basis and also override the sky for an individual Camera.  
  
• For information on how to set the sky on a per-Scene basis, see the
[Lighting window documentation](lighting-window.html).  
• For information on how to override the sky for a specific Camera, see the
[Skybox component documentation](sky-landing.html).  
  
## Skyboxes

A **skybox** A special type of Material used to represent skies. Usually six-
sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) is a cube with a different texture on
each face. When you use a skybox to render a sky, Unity essentially places
your Scene inside the skybox cube. Unity renders the skybox first, so the sky
always renders at the back.

**Note:** The [High Definition Render Pipeline (HDRP)](high-definition-render-
pipeline.html) does not support skybox Materials and instead includes multiple
sky generation solutions.

Similar to other sky implementations, you can use a skybox to do the
following:

  * Render a skybox around your Scene.
  * Configure your lighting settings to create realistic ambient lighting based on the skybox.
  * Override the skybox that an individual Camera uses, using the [skybox component](sky-landing.html).

## Additional resources

  * [Add ambient light from the environment](lighting-ambient-light.html)
  * [Cubemaps](class-Cubemap-landing.html)A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap)

[](sky-landing.html)

Sky

[](skyboxes-using.html)

Create a skybox

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

