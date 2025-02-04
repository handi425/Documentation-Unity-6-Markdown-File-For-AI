[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/skyboxes-using.html)
  * [中文](/cn/current/Manual/skyboxes-using.html)
  * [日本語](/ja/current/Manual/skyboxes-using.html)
  * [한국어](/kr/current/Manual/skyboxes-using.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/skyboxes-using.html)
  * [中文](/cn/current/Manual/skyboxes-using.html)
  * [日本語](/ja/current/Manual/skyboxes-using.html)
  * [한국어](/kr/current/Manual/skyboxes-using.html)

  * [World building](CreatingEnvironments.html)
  * [Sky](sky-landing.html)
  * Create a skybox

[](sky.html)

Sky

[](skybox-shaders.html)

Configure a skybox with a Skybox Shader

# Create a skybox

To create a new **skybox** A special type of Material used to represent skies.
Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) Material:

  1. From the menu bar, click **Assets > Create > Material**.
  2. In the ****Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader)** drop-down, click **Skybox** then the
skybox Shader you want to use.

  3. You can now fill out the properties on the Material to set up the skybox. The properties available on the Material depend on the skybox Shader the Material uses.

**Note** : Each skybox Shader has its own set of prerequisite Textures that
differ in number and **Texture format** A file format for handling textures
during real-time rendering by 3D graphics hardware, such as a graphics card or
mobile device. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat). For information on the
Textures a particular skybox Shader requires, see the documentation for that
skybox Shader. You can find the list of skybox Shaders and their documentation
on the [skybox Shaders](skybox-shaders.html) page.

## Drawing a skybox in your Scene

After you create a skybox Material, you can render it in your **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). To do this:

  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. In the window that appears, click the **Environment** tab.
  3. Assign the skybox Material to the **Skybox Material** property.

This draws the skybox in the background of every **Camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) in your Scene. If you instead only
want to draw the skybox for a particular Camera, see Drawing a skybox for a
particular Camera.

## Drawing a skybox for a particular Camera

If you only want to draw a skybox in the background of a particular Camera,
use the [Skybox component](sky-landing.html). When you attach this component
to a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with a Camera, it overrides the
skybox that the Camera draws. To attach and set up the Skybox component:

  1. Select a Camera in your Scene and view it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

  2. Click **Add Component > Rendering > Skybox**.
  3. On the Skybox component, assign the skybox Material to the **Custom Skybox** property.

## Best Practices

If your Skybox includes a sun, moon, or other light in it, set up a
Directional Light that points in the same direction as the light. This makes
it appear as though the light in your skybox creates shadows in your Scene. If
there are multiple Directional Lights in your Scene, you can choose which
Directional Light the Skybox uses. To do this:

  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. Click the **Scene** tab.
  3. Assign the Directional Light you want to use to the **Sun Source** property.

If you want to have fog in your Scene, match the fog color to the color of the
skybox. This makes the fog blend to the color of the Scene sky. To do this:

  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. Click the **Environment** tab.
  3. In the **Other Settings** section, enable the **Fog** checkbox.
  4. Set the **Color** property to a color that suits your skybox. For this, you can use the ink dropper tool to select a color from the Scene.

[](sky.html)

Sky

[](skybox-shaders.html)

Configure a skybox with a Skybox Shader

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

