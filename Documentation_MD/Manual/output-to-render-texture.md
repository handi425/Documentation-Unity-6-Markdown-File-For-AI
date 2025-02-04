[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/output-to-render-texture.html)
  * [中文](/cn/current/Manual/output-to-render-texture.html)
  * [日本語](/ja/current/Manual/output-to-render-texture.html)
  * [한국어](/kr/current/Manual/output-to-render-texture.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/output-to-render-texture.html)
  * [中文](/cn/current/Manual/output-to-render-texture.html)
  * [日本語](/ja/current/Manual/output-to-render-texture.html)
  * [한국어](/kr/current/Manual/output-to-render-texture.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Rendering to a texture](render-texture-landing.html)
  * Render a camera view to a Render Texture

[](render-texture-landing.html)

Rendering to a texture

[](class-CustomRenderTexture-landing.html)

Drawing to textures with shaders via Custom Render Textures

# Render a camera view to a Render Texture

A **Render Texture** is a type of [Texture](class-TextureImporter.html)An
image used when rendering a GameObject, Sprite, or UI element. Textures are
often applied to the surface of a mesh to give it visual detail. [More
info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) that Unity creates and updates at run
time. To use a Render Texture, create a new Render Texture using **Assets >
Create > Render Texture** and assign it to **Target Texture** in your
[Camera](class-Camera.html)A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) component. Then you can use the Render
Texture in a **Material** An asset that defines how a surface should be
rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) just like a regular Texture.

To create a live arena camera in your game:

  1. Create a new Render Texture asset using **Assets >Create >Render Texture**.
  2. Create a new Camera using **GameObject > Camera**.
  3. Assign the **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) to the **Target Texture** of
the new Camera.

  4. Create a new 3D cube using **GameObject > 3D Object > Cube**.
  5. Drag the Render Texture onto the cube to create a Material that uses the render texture.
  6. Enter Play Mode, and observe that the cube’s texture is updated in real-time based on the new Camera’s output.

![Render Textures are set up as demonstrated
above](../uploads/Main/RenderTextureLiveCam.jpg) Render Textures are set up as
demonstrated above

## Additional resources

  * [Render Texture Inspector window reference](class-RenderTexture.html)
  * [Render a camera’s output to a Render Texture in URP](urp/rendering-to-a-render-texture.html)

[](render-texture-landing.html)

Rendering to a texture

[](class-CustomRenderTexture-landing.html)

Drawing to textures with shaders via Custom Render Textures

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

