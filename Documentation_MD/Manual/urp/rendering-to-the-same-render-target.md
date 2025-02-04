[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/rendering-to-the-same-render-target.html)
  * [中文](/cn/current/Manual/urp/rendering-to-the-same-render-target.html)
  * [日本語](/ja/current/Manual/urp/rendering-to-the-same-render-target.html)
  * [한국어](/kr/current/Manual/urp/rendering-to-the-same-render-target.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/rendering-to-the-same-render-target.html)
  * [中文](/cn/current/Manual/urp/rendering-to-the-same-render-target.html)
  * [日本語](/ja/current/Manual/urp/rendering-to-the-same-render-target.html)
  * [한국어](/kr/current/Manual/urp/rendering-to-the-same-render-target.html)

  * [Working in Unity](../working-in-unity.html)
  * [Cameras](../Cameras.html)
  * [Cameras in URP](../urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](../urp/cameras-multiple.html)
  * Set up split-screen rendering in URP

[](../urp/cameras/add-and-remove-cameras-in-a-stack.html)

Add and remove cameras in a camera stack in URP

[](../urp/cameras/apply-different-post-proc-to-cameras.html)

Apply different post processing effects to separate cameras in URP

# Set up split-screen rendering in URP

In the Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP), multiple [Base
Cameras](camera-types-and-render-type-introduction.html#base-camera) or
[Camera Stacks](camera-stacking.html) can render to the same render target.
This allows you to create effects such as split screen rendering.

If more than one Base **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) or Camera Stack renders to the same
area of a render target, Unity draws each **pixel** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) in the overlapping area multiple
times. Unity draws the Base Camera or Camera Stack with the highest priority
last, on top of the previously drawn pixels. For more information on the
camera render order optimization, refer to [Understand camera render
order](cameras-advanced.html).

You use the Base Camera’s ****Viewport** The user’s visible area of an app on
their screen.  
See in [Glossary](../Glossary.html#Viewport) Rect** property to define the
area of the render target to render to. For more information on viewport
coordinates, refer to the [Unity
Manual](https://docs.unity3d.com/Manual/class-Camera.html) and [API
documentation](https://docs.unity3d.com/ScriptReference/Camera-rect.html).

## Setting up split screen rendering

![Setting up split screen rendering in URP](../../uploads/urp/camera-split-
screen-viewport.png) Setting up split screen rendering in URP

  1. Create a Camera in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene). Its **Render Mode** defaults to
**Base** , making it a Base Camera.

  2. Select the Camera. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector), scroll to the Output section.
Change the values for **Viewport rect** to the following:

     * X: 0
     * Y: 0
     * W: 0.5
     * H: 1
  3. Create another Camera in your scene. Its **Render Mode** defaults to **Base** , making it a Base Camera.
  4. Select the Camera. In the Inspector, scroll to the Output section. Change the values for **Viewport rect** to the following: 
     * X: 0.5
     * Y: 0
     * W: 0.5
     * H: 1

Unity renders the first Camera to the left-hand side of the screen, and the
second Camera to the right-hand side of the screen.

You can change the Viewport rect for a Camera in a script by setting its
`rect` property, like this:

    
    
    myUniversalAdditionalCameraData.rect = new Rect(0.5f, 0f, 0.5f, 0f);
    

[](../urp/cameras/add-and-remove-cameras-in-a-stack.html)

Add and remove cameras in a camera stack in URP

[](../urp/cameras/apply-different-post-proc-to-cameras.html)

Apply different post processing effects to separate cameras in URP

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

