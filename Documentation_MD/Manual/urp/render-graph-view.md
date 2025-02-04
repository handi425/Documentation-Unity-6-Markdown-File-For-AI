[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/render-graph-view.html)
  * [中文](/cn/current/Manual/urp/render-graph-view.html)
  * [日本語](/ja/current/Manual/urp/render-graph-view.html)
  * [한국어](/kr/current/Manual/urp/render-graph-view.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/render-graph-view.html)
  * [中文](/cn/current/Manual/urp/render-graph-view.html)
  * [日本語](/ja/current/Manual/urp/render-graph-view.html)
  * [한국어](/kr/current/Manual/urp/render-graph-view.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../urp/customizing-urp.html)
  * [Render graph system in URP](../urp/render-graph.html)
  * Analyze a render graph in URP

[](../urp/render-graph-compute-shader-input.html)

Create input data for a compute shader in URP

[](../urp/render-graph-unsafe-pass.html)

Use Compatibility Mode APIs in render graph render passes

# Analyze a render graph in URP

There are several ways to analyse a render graph:

  * Use the Render Graph Viewer
  * Use the Rendering Debugger
  * Use the Frame Debugger

## Use the Render Graph Viewer

To open the **Render Graph Viewer** window, go to **Window > Analysis > Render
Graph Viewer**.

The Render Graph Viewer window displays a render graph, which is the optimized
sequence of render passes the Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) steps through each
frame. The Render Graph Viewer displays both built-in render passes and any
[custom render passes](renderer-features/intro-to-scriptable-render-
passes.html) you create.

For more information about the **Render Graph Viewer** window, refer to
[Render Graph Viewer window reference](render-graph-viewer-reference.html).

### View a render graph

The **Render Graph Viewer** window displays the render graph for the current
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) by default. To select another render
graph, use the dropdown in the **toolbar** A row of buttons and basic controls
at the top of the Unity Editor that allows you to interact with the Editor in
various ways (e.g. scaling, translation). [More info](../Toolbar.html)  
See in [Glossary](../Glossary.html#Toolbar).

#### Example: check how URP uses a resource

You can use the resource access blocks next to a resource name to check how
the render passes use the resource.

![Render Graph Viewer example](../../uploads/urp/render-graph-viewer.png)
Render Graph Viewer example

In the previous example, the `_MainLightShadowmapTexture_` texture goes
through the following stages:

  1. During the first five render passes between **InitFrame** and **SetupCameraProperties** , the texture doesn’t exist.

  2. The **Main Light Shadowmap** render pass creates the texture as a global texture, and has write-only access to it. For more information about global textures, refer to [Transfer textures between passes](render-graph-pass-textures-between-passes.html).

The blue merge bar below **Main Light Shadowmap** means URP merged **Main
Light Shadowmap** , **Additional Lights Shadowmap** and
**SetupCameraProperties** into a single render pass.

  3. The next five render passes don’t have access to the texture.

  4. The first **Draw Objects** render pass has read-only access to the texture.

  5. The next two render passes don’t have access to the texture.

  6. The second **Draw Objects** render pass has read-only access to the texture.

  7. Unity destroys the texture, because it’s no longer needed. 

### Check how URP optimized a render pass

To check the details of a render pass, for example to find out why it’s not a
native render pass or a merged pass, do either of the following:

  * Select the render pass name to display the details in the Pass List.
  * Below the render pass name, hover your cursor over the gray, blue, or flashing blue resource access overview block.

For more information about displaying details of a render pass, refer to
[Render Graph Viewer window reference](render-graph-viewer-reference.html).

## Use the Rendering Debugger

You can use the Rendering Debugger to log the resources URP uses and how it
uses them, in the **Console** window.

To enable logging, follow these steps:

  1. Select **Window > Analysis > Rendering Debugger** to open the **Rendering Debugger** window.
  2. In the left pane, select the **Render Graph** tab.
  3. Enable **Enable Logging**.
  4. Select either **Log Frame Information** to log how URP uses resources, or **Log Resources** to log details about the resources.
  5. Select the new item in the **Console** window to display the full log.

For more information about the Rendering Debugger, refer to [Rendering
Debugger](features/rendering-debugger.html).

## Use the Frame Debugger

Use the [Frame
Debugger](https://docs.unity3d.com/2023.3/Documentation/Manual/frame-debugger-
window.html) to check the render passes and draw calls in the rendering loop.

The Frame Debugger displays the following in the [Event Hierarchy
panel](https://docs.unity3d.com/Manual/frame-debugger-window-event-
hierarchy.html) when the render graph system is active:

  * A parent rendering event called **ExecuteRenderGraph**.
  * Child rendering events called **(RP <render-pass>:<subpass>)**, where `<render-pass>` is the render pass number and `<subpass>` is the subpass number.

The Frame Debugger shows only render passes that contain a draw call.

For more information about the Frame Debugger, refer to [Frame
Debugger](https://docs.unity3d.com/2023.3/Documentation/Manual/frame-debugger-
window.html).

## Additional resources

  * [Render graph system](render-graph.html)
  * [Rendering in the Universal Render Pipeline](rendering-in-universalrp.html)
  * [Frame Debugger](https://docs.unity3d.com/2023.3/Documentation/Manual/frame-debugger-window.html)
  * [Rendering Debugger](features/rendering-debugger.html)
  * [Understand performance](understand-performance.html)

[](../urp/render-graph-compute-shader-input.html)

Create input data for a compute shader in URP

[](../urp/render-graph-unsafe-pass.html)

Use Compatibility Mode APIs in render graph render passes

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

