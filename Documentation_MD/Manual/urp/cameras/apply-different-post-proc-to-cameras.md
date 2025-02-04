[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
  * [中文](/cn/current/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
  * [日本語](/ja/current/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
  * [한국어](/kr/current/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
  * [中文](/cn/current/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
  * [日本語](/ja/current/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
  * [한국어](/kr/current/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](../../urp/cameras-multiple.html)
  * Apply different post processing effects to separate cameras in URP

[](../../urp/rendering-to-the-same-render-target.html)

Set up split-screen rendering in URP

[](../../urp/rendering-to-a-render-texture.html)

Render a camera's output to a Render Texture in URP

# Apply different post processing effects to separate cameras in URP

In the Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../../render-
pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (URP) you can apply
separate post processing effects to different **cameras** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) in the same **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene).

![The output of two cameras. Image A shows a camera with a Color Adjustment
override. Image B shows the second camera with a Vignette
override.](../../../uploads/urp/apply-different-post-proc-to-separate-
cameras.png) The output of two cameras. Image A shows a camera with a Color
Adjustment override. Image B shows the second camera with a Vignette override.

## Set up your scene

To set up your scene for multiple **post-processing** A process that improves
product visuals by applying filters and effects before the image appears on
screen. You can use post-processing effects to simulate physical camera and
film properties, for example Bloom and Depth of Field. [More
info](../../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../../Glossary.html#post-processing) effects on different
cameras, use the following steps:

  1. Create multiple cameras in your scene (**GameObject** > **Camera**).
  2. Enable **Post Processing** on each camera.
  3. Create an empty **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) for each separate post-
processing effect you want.

  4. Add a volume component to each empty GameObject. To do this, select the GameObject and in the Inspector window select **Add Component** > **Volume**.
  5. Create a volume profile for each empty GameObject. In the GameObject’s **Volume** component, go to the **Profile** property and select **New**.
  6. Create new layer for each post-processing effect. For more information, refer to [Layers](../../Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](../../Layers.html)  
See in [Glossary](../../Glossary.html#Layer).

## Apply different post processing effects to each camera

With the scene set up, the following steps show how to create and apply a
post-processing effect to each camera in the scene.

  1. Select one of the GameObjects with a volume component and select **Add Override**.
  2. Choose a [post-processing effect](../EffectList.html) from the dropdown.
  3. Select the **Layer** dropdown and choose one of the layers created when you set up the scene.
  4. Select the camera you want to apply this effect to.
  5. In the Inspector window, go to **Environment** > **Volume Mask** and select the same layer that you chose for the GameObject.
  6. Repeat steps 1–5 for each GameObject and Camera pair that your scene requires.

**Note:** Some effects apply to all cameras in a scene by default. As a result
of this, you might need to add the same effect to each volume. This overrides
the effects from other volumes on individual cameras with the new values that
you set.

Each camera now applies post-processing as assigned to it by the GameObject on
the same layer as it’s volume mask.

**Note:** The Scene Camera might display some post-processing effects from the
Default layer. To avoid this and create a clear view of your scene, open the
Effects dropdown in the View options overlay in the **Scene view** An
interactive view into the world you are creating. You use the Scene View to
select and position scenery, characters, cameras, lights, and all other types
of Game Object. [More info](../../UsingTheSceneView.html)  
See in [Glossary](../../Glossary.html#SceneView) and turn off **Post
Processing**.

[](../../urp/rendering-to-the-same-render-target.html)

Set up split-screen rendering in URP

[](../../urp/rendering-to-a-render-texture.html)

Render a camera's output to a Render Texture in URP

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

