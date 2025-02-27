[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/skybox-shaders.html)
  * [中文](/cn/current/Manual/skybox-shaders.html)
  * [日本語](/ja/current/Manual/skybox-shaders.html)
  * [한국어](/kr/current/Manual/skybox-shaders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/skybox-shaders.html)
  * [中文](/cn/current/Manual/skybox-shaders.html)
  * [日本語](/ja/current/Manual/skybox-shaders.html)
  * [한국어](/kr/current/Manual/skybox-shaders.html)

  * [World building](CreatingEnvironments.html)
  * [Sky](sky-landing.html)
  * Configure a skybox with a Skybox Shader

[](skyboxes-using.html)

Create a skybox

[](skybox-material-reference.html)

Skybox Shader Material Inspector window reference

# Configure a skybox with a Skybox Shader

Unity provides multiple **Skybox** A special type of Material used to
represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) Shaders for you to use. Each
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) uses a different set of properties and
generation techniques. Each Shader falls into one of the following two
categories:

**Note:** The [High Definition Render Pipeline (HDRP)](high-definition-render-
pipeline.html) does not support any of the above Shaders and instead includes
multiple sky generation solutions.

## Textured

Generates a skybox from one or multiple textures. The source textures
represent the view of the background from all directions. The Skybox Shaders
in this category are:

  * 6 Sided
  * Cubemap
  * Panoramic

### 6 Sided Skybox shader

This skybox Shader generates a skybox from six separate Textures. Each texture
represents a view of the sky along a particular world axis. To illustrate
this, think of the **Scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as being inside a cube. Each Texture
represents one of the interior faces of the cube and all six combine to create
a seamless environment.

To create a **6 Sided** skybox, you need six individual Textures that, when
combined, map to a net layout like:

![](../uploads/Main/skybox-six-sided-net.png)

To generate the best ambient lighting, the Textures should use a [high dynamic
range (HDR)](hdr-landing.html).

### Cubemap Skybox shader

This skybox Shader generates a skybox from a single [Cubemap Asset](class-
Cubemap-landing.html). This **Cubemap** A collection of six square textures
that can represent the reflections in an environment or the skybox drawn
behind your geometry. The six squares form the faces of an imaginary cube that
surrounds an object; each face represents the view along the directions of the
world axes (up, down, left, right, forward and back). [More info](class-
Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) consists of six square Textures and
represents the entire view of the sky from every direction.

### Panoramic Skybox shader

To generate a skybox, the Panoramic Shader wraps a single Texture spherically
around the Scene.

For information on how to create a Material that uses this skybox Shader, as
well as details on how to render the skybox in your Scene, see [Using
skyboxes](skyboxes-using.html).

To create a **Panoramic** skybox, you need a single 2D Texture that uses
latitude-longitude (cylindrical) mapping, like so:

![](../uploads/Main/skybox-lat-long-layout.png)

To make sure the Texture is 2D:

  1. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), select the Texture.

  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), make sure the **Texture Shape** is
set to **2D**.

To generate the best ambient lighting, the Texture should use a [high dynamic
range (HDR)](hdr-landing.html).

## Procedural Skybox shader

The Procedural skybox Shader does not require any input Textures and instead
generates a skybox purely from the properties set in the Material Inspector.

### Positioning the sun

If you choose to render a sun disk in your skybox (see **Sun** in
[Properties](shader-skybox-procedural.html)), this Shader uses the rotation of
the active [Light](class-Light.html) to position the sun in the skybox. To
find the active Light:

  1. Open the Lighting window (menu: **Window > Rendering > Lighting**).
  2. Navigate to the **Environment** tab.
  3. The Light assigned to **Sun Source** is your Scene’s active Light.
  4. If there is no Light assigned to **Sun Source** , assign the Light in your Scene you want to become the active Light to **Sun Source**.

You can use this behaviour to create a simple day-night cycle. To do this,
continuously rotate your main Directional Light around a particular axis.

### Additional resources

  * [Skybox Shader Material Inspector window reference](skybox-material-reference.html)

[](skyboxes-using.html)

Create a skybox

[](skybox-material-reference.html)

Skybox Shader Material Inspector window reference

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

