[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/customize/inject-render-pass-via-script.html)
  * [中文](/cn/current/Manual/urp/customize/inject-render-pass-via-script.html)
  * [日本語](/ja/current/Manual/urp/customize/inject-render-pass-via-script.html)
  * [한국어](/kr/current/Manual/urp/customize/inject-render-pass-via-script.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/customize/inject-render-pass-via-script.html)
  * [中文](/cn/current/Manual/urp/customize/inject-render-pass-via-script.html)
  * [日本語](/ja/current/Manual/urp/customize/inject-render-pass-via-script.html)
  * [한국어](/kr/current/Manual/urp/customize/inject-render-pass-via-script.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](../../urp/inject-a-render-pass.html)
  * Inject a render pass via scripting in URP

[](../../urp/renderer-features/scriptable-renderer-features/scriptable-
renderer-feature-reference.html)

Scriptable Renderer Feature API reference for URP

[](../../urp/customize/custom-pass-injection-points.html)

Injection points reference for URP

# Inject a render pass via scripting in URP

Unity raises a
[beginCameraRendering](https://docs.unity3d.com/ScriptReference/Rendering.RenderPipelineManager-
beginCameraRendering.html) event before it renders each active **Camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) in every frame. If a Camera is
inactive (for example, if the **Camera** component checkbox is cleared on a
Camera GameObject), Unity does not raise a `beginCameraRendering` event for
this Camera.

When you subscribe a method to this event, you can execute custom logic before
Unity renders the Camera. Examples of custom logic include rendering extra
Cameras to **Render Textures** A special type of Texture that is created and
updated at runtime. To use them, first create a new Render Texture and
designate one of your Cameras to render into it. Then you can use the Render
Texture in a Material just like a regular Texture. [More info](../../class-
RenderTexture.html)  
See in [Glossary](../../Glossary.html#RenderTexture), and using those Textures
for effects like planar reflections or surveillance camera views.

Other events in the
[RenderPipelineManager](https://docs.unity3d.com/ScriptReference/Rendering.RenderPipelineManager.html)
class provide more ways to customize URP. You can also use the principles
described in this article with those events.

## Use the RenderPipelineManager API

  1. Subscribe a method to one of the events in the [RenderPipelineManager](https://docs.unity3d.com/ScriptReference/Rendering.RenderPipelineManager.html) class.

  2. In the subscribed method, use the `EnqueuePass` method of a `ScriptableRenderer` instance to inject a custom render pass into the URP frame rendering.

For information about writing a render pass, refer to [Write a render pass
using the render graph system](../render-graph-write-render-pass.html).

Example code:

    
    
    public class EnqueuePass : MonoBehaviour
    {
        [SerializeField] private BlurSettings settings;    
        private BlurRenderPass blurRenderPass;
    
        private void OnEnable()
        {
            ...
            blurRenderPass = new BlurRenderPass(settings);
            // Subscribe the OnBeginCamera method to the beginCameraRendering event.
            RenderPipelineManager.beginCameraRendering += OnBeginCamera;
        }
    
        private void OnDisable()
        {
            RenderPipelineManager.beginCameraRendering -= OnBeginCamera;
            blurRenderPass.Dispose();
            ...
        }
    
        private void OnBeginCamera(ScriptableRenderContext context, Camera cam)
        {
            ...
            // Use the EnqueuePass method to inject a custom render pass
            cam.GetUniversalAdditionalCameraData()
                .scriptableRenderer.EnqueuePass(blurRenderPass);
        }
    }
    

## Example

This example demonstrates how to subscribe a method to the
`beginCameraRendering` event.

To follow the steps in this example, create a [new Unity project using the
**Universal Project Template**](../creating-a-new-project-with-urp.html)

  1. In the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene), create a Cube. Name it Example
Cube.

  2. In your Project, create a C# script. Call it `URPCallbackExample`.

  3. Copy and paste the following code into the script. ```C# using UnityEngine; using UnityEngine.Rendering;

public class URPCallbackExample : MonoBehaviour { // Unity calls this method
automatically when it enables this component private void OnEnable() { // Add
WriteLogMessage as a delegate of the
RenderPipelineManager.beginCameraRendering event
RenderPipelineManager.beginCameraRendering += WriteLogMessage; }

    
        // Unity calls this method automatically when it disables this component
    private void OnDisable()
    {
        // Remove WriteLogMessage as a delegate of the  RenderPipelineManager.beginCameraRendering event
        RenderPipelineManager.beginCameraRendering -= WriteLogMessage;
    }
    
    // When this method is a delegate of RenderPipeline.beginCameraRendering event, Unity calls this method every time it raises the beginCameraRendering event
    void WriteLogMessage(ScriptableRenderContext context, Camera camera)
    {
        // Write text to the console
        Debug.Log($"Beginning rendering the camera: {camera.name}");
    }
    

} ``` > **Note**: When you subscribe to an event, your handler method (in this
example,`WriteLogMessage`) must accept the parameters defined in the event
delegate. In this example, the event delegate
is`RenderPipeline.BeginCameraRendering`, which expects the following
parameters:`<ScriptableRenderContext, Camera>`.

  4. Attach the `URPCallbackExample` script to Example Cube.

  5. Select **Play**. Unity prints the message from the script in the **Console window** A Unity Editor window that shows errors, warnings and other messages generated by Unity, or your own scripts. [More info](../../Console.html)  
See in [Glossary](../../Glossary.html#Consolewindow) each time Unity raises
the `beginCameraRendering` event.

![Unity prints log message in console.](../../../uploads/urp/customizing-
urp/log-message-in-console.png) Unity prints log message in console.

  6. To raise a call to the `OnDisable()` method: In the Play mode, select Example Cube and clear the checkbox next to the script component title. Unity unsubscribes `WriteLogMessage` from the `RenderPipelineManager.beginCameraRendering` event and stops printing the message in the Console window.

![Deactivate the script component. Clear the checkbox next to the script
component title.](../../../uploads/urp/customizing-urp/deactivate-script-
component.png) Deactivate the script component. Clear the checkbox next to the
script component title.

## Use a function in a MonoBehaviour

You can inject a Scriptable Render Pass into a scene via any **GameObject**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) present in the scene. This
gives you more precise control over when the render pass is active. But this
means you must have a GameObject inject the render pass at every point you
want to use it. As a result, it’s better to inject any common effects in your
project via a Scriptable Renderer Feature instead.

When you inject a Scriptable Render Pass into a scene via any GameObject, it’s
important to consider how URP uses this script. The first Camera to render the
Scriptable Render Pass uses up the render pass, and is the only Camera the
render pass applies to. Any Cameras that the Scriptable Render Pass would
apply that render after the first Camera don’t render the effect.

For example, if you have two Cameras and you add the Scriptable Render Pass in
the `Update` method, only the first Camera to render uses the Scriptable
Render Pass effect. This is because the first camera uses up the instance of
the effect. As the second Camera renders before the next call of the `Update`
method, a second instance of the Scriptable Render Pass isn’t available to
use. As a result, the second Camera doesn’t apply the effect from the
Scriptable Render Pass to its output.

## Additional resources

[Write a render pass using the render graph system](../render-graph-write-
render-pass.html)

[](../../urp/renderer-features/scriptable-renderer-features/scriptable-
renderer-feature-reference.html)

Scriptable Renderer Feature API reference for URP

[](../../urp/customize/custom-pass-injection-points.html)

Injection points reference for URP

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

