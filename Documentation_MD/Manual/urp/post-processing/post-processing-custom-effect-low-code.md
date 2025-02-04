[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
  * [中文](/cn/current/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
  * [日本語](/ja/current/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
  * [한국어](/kr/current/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
  * [中文](/cn/current/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
  * [日本語](/ja/current/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
  * [한국어](/kr/current/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../../urp/post-processing-in-urp.html)
  * [Custom post-processing in URP](../../urp/post-processing/custom-post-processing.html)
  * Create a low-code custom post-processing effect in URP

[](../../urp/post-processing/custom-post-processing.html)

Custom post-processing in URP

[](../../urp/post-processing/custom-post-processing-with-volume.html)

Create a custom post-processing effect with Volume support in URP

# Create a low-code custom post-processing effect in URP

The example on this page shows how to use the Full Screen Render Pass Renderer
Feature to create a grayscale custom **post-processing** A process that
improves product visuals by applying filters and effects before the image
appears on screen. You can use post-processing effects to simulate physical
camera and film properties, for example Bloom and Depth of Field. [More
info](../../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../../Glossary.html#post-processing) effect.

For more information on the Full Screen Render Pass Renderer Feature, refer to
the [Full Screen Pass Renderer Feature reference](../renderer-
features/renderer-feature-full-screen-pass.html).

## Prerequisites

This example requires the following:

  * A Unity project with the URP package installed.

  * The **Scriptable Render Pipeline Settings** property refers to a URP asset (**Project Settings** > **Graphics** > **Scriptable Render Pipeline Settings**).

## Create a Fullscreen Shader Graph

You must create a Fullscreen **Shader** A program that runs on the GPU. [More
info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) Graph to create a custom post-
processing effect.

  1. Create a new Shader Graph in your Project. To do this right-click in the Project window and select **Create** > **Shader Graph** > **URP** > **Fullscreen Shader Graph**.

  2. Add a **URP Sample Buffer** node. To do this right-click in the Shader Graph window, and select **Create Node**. Then locate and select **URP Sample Buffer**.

  3. In the **URP Sample Buffer** node’s **Source Buffer** dropdown menu, select **BlitSource**.

  4. Add a **Vector 3** node.

  5. Assign the **Vector 3** node the following values: 
     * **X** = 0.2126
     * **Y** = 0.7152
     * **Z** = 0.0722
  6. Add a **Dot Product** node.

  7. Connect the nodes as shown below.

![Grayscale Fullscreen Shader Graph with all nodes connected.](../../../uploads/urp/post-proc/custom-effect/grayscale-effect-shader-graph.png) Grayscale Fullscreen Shader Graph with all nodes connected. Node | Connection  
---|---  
**URP Sample Buffer** |  **Output** to **Dot Product A**  
**Vector 3** |  **Out** to **Dot Product B**  
**Dot Product** |  **Out** to **Fragment Base Color**  
  8. Save your Shader Graph.

  9. Create a new Material in your Project. To do this right-click in the Project window and select **Create** > **Material**.

  10. Apply the Shader Graph shader to the Material. To do this, open the Material in the Inspector and select **Shader** > **Shader Graphs** , then select the Shader Graph you created in the previous steps.

## Use the Material in a Full Screen Pass Renderer Feature

Once you’ve created a compatible Shader Graph and Material, you can use the
Material with a Full Screen Pass Renderer Feature to create a custom post-
processing effect.

  1. Select your project’s Universal Renderer.

If you created your project using the **Universal 3D** template, you can find
the Universal Renderers in the following project folder: **Assets** >
**Settings**.

  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../UsingTheInspector.html)  
See in [Glossary](../../Glossary.html#Inspector), click **Add Renderer
Feature** and select **Full Screen Pass Renderer Feature**. For more
information on adding Renderer Features refer to [How to add a Renderer
Feature to a Renderer](./../urp-renderer-feature.html).

  3. Set the **Pass Material** field to the Material you created with the Fullscreen Shader Graph.

  4. Set **Injection Point** to **After Rendering Post Processing**.

  5. Set **Requirements** to **Color**.

You should now notice the effect in both **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) view and Game view.

![Example scene with a grayscale custom post-processing
effect.](../../../uploads/urp/post-proc/custom-effect/grayscale-custom-
effect.png) Example scene with a grayscale custom post-processing effect.

[](../../urp/post-processing/custom-post-processing.html)

Custom post-processing in URP

[](../../urp/post-processing/custom-post-processing-with-volume.html)

Create a custom post-processing effect with Volume support in URP

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

