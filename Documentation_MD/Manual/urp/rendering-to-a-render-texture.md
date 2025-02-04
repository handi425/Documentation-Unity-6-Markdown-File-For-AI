[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/rendering-to-a-render-texture.html)
  * [中文](/cn/current/Manual/urp/rendering-to-a-render-texture.html)
  * [日本語](/ja/current/Manual/urp/rendering-to-a-render-texture.html)
  * [한국어](/kr/current/Manual/urp/rendering-to-a-render-texture.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/rendering-to-a-render-texture.html)
  * [中文](/cn/current/Manual/urp/rendering-to-a-render-texture.html)
  * [日本語](/ja/current/Manual/urp/rendering-to-a-render-texture.html)
  * [한국어](/kr/current/Manual/urp/rendering-to-a-render-texture.html)

  * [Working in Unity](../working-in-unity.html)
  * [Cameras](../Cameras.html)
  * [Cameras in URP](../urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](../urp/cameras-multiple.html)
  * Render a camera's output to a Render Texture in URP

[](../urp/cameras/apply-different-post-proc-to-cameras.html)

Apply different post processing effects to separate cameras in URP

[](../urp/User-Render-Requests.html)

Create a render request in URP

# Render a camera’s output to a Render Texture in URP

In the Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP), a **Camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) can render to the screen or to a
[Render Texture](https://docs.unity3d.com/Manual/class-RenderTexture.html)A
special type of Texture that is created and updated at runtime. To use them,
first create a new Render Texture and designate one of your Cameras to render
into it. Then you can use the Render Texture in a Material just like a regular
Texture. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture). Rendering to a screen is
the default and is the most common use case, but rendering to a Render Texture
allows you to create effects such as CCTV camera monitors.

If you have a Camera that is rendering to a Render Texture, you must have a
second Camera that then renders that Render Texture to the screen. In URP, all
Cameras that render to Render Textures perform their render loops before all
Cameras that render to the screen. This ensures that the Render Textures are
ready to render to the screen. For more information on Camera rendering order
in URP, refer to [Rendering order and overdraw](cameras-advanced.html).

## Render to a Render Texture that renders to the screen

  1. Create a Render Texture Asset in your project. To do this select **Assets** > **Create** > **Rendering** > **Render Texture**.
  2. Create a **Quad** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](../PrimitiveObjects.html)  
See in [Glossary](../Glossary.html#Quad) game object in your **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

  3. Create a material in your Project.
  4. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector), drag the Render Texture to the
material’s **Base Map** field.

  5. In the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](../UsingTheSceneView.html)  
See in [Glossary](../Glossary.html#SceneView), drag the material on to the
quad.

  6. Create a camera in your scene.
  7. Select the Base Camera and in the Inspector, drag the Render Texture on to the **Output Texture** property.
  8. Create another camera in your scene.
  9. Place the quad within the view of the new Base Camera.

The first Camera now renders its view to the Render Texture. The second Camera
renders the scene including the Render Texture to the screen.

You can set the output target for a camera in a script by setting the
`targetTexture` property of the camera:

    
    
    myCamera.targetTexture = myRenderTexture;
    

[](../urp/cameras/apply-different-post-proc-to-cameras.html)

Apply different post processing effects to separate cameras in URP

[](../urp/User-Render-Requests.html)

Create a render request in URP

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

