[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/package-sample-urp-package-samples.html)
  * [中文](/cn/current/Manual/urp/package-sample-urp-package-samples.html)
  * [日本語](/ja/current/Manual/urp/package-sample-urp-package-samples.html)
  * [한국어](/kr/current/Manual/urp/package-sample-urp-package-samples.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/package-sample-urp-package-samples.html)
  * [中文](/cn/current/Manual/urp/package-sample-urp-package-samples.html)
  * [日本語](/ja/current/Manual/urp/package-sample-urp-package-samples.html)
  * [한국어](/kr/current/Manual/urp/package-sample-urp-package-samples.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Get started with URP](../urp/introduction-landing.html)
  * [Installing and upgrading URP](../urp/InstallingAndConfiguringURP.html)
  * [Creating a URP project](../urp/creating-a-urp-project.html)
  * Package samples reference for URP

[](../urp/package-samples.html)

Import a package sample in URP

[](../urp/InstallURPIntoAProject.html)

Install URP into an existing project

# Package samples reference for URP

The package samples that URP provides are:

  * URP Package Samples: A collection of example **shaders** A program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), C# **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](../creating-scripts.html)  
See in [Glossary](../Glossary.html#Scripts), and other assets you can build
upon or use in your application. Refer to [URP Package Samples](package-
sample-urp-package-samples.html).

  * URP RenderGraph Samples: A collection of example [Scriptable Renderer Features](renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html) demonstrating how to use the render graph system. For more information about the render graph samples, refer to [Render graph system](render-graph.html).

## URP Package Samples

URP Package Samples is a [package sample](package-samples.html) for the
Universal **Render Pipeline** A series of operations that take the contents of
a Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP). It contains example
shaders, C# scripts, and other assets you can build upon, use to learn how to
use a feature, or use directly in your application. For information on how to
import URP Package Samples into your project, refer to [Importing package
samples](package-samples.html#importing-package-samples).

Each example uses its own [URP Asset](universalrp-asset.html) so, if you want
to build an example **scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene), [add the example’s URP Asset to
your Graphics settings](InstallURPIntoAProject.html#set-urp-active). If you
don’t do this, Unity might strip shaders or render passes that the example
uses.

### Camera Stacking

The `URP Package Samples/CameraStacking` folder contains examples for [Camera
Stacking](camera-stacking.html). The following table describes each **Camera**
A component which creates an image of a particular viewpoint in your scene.
The output is either drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) Stacking example in this folder.

**Example** | **Description**  
---|---  
**Mixed field of view** | The example in `CameraStacking/MixedFOV` demonstrates how to use Camera Stacking in a first-person application to prevent the character’s equipped items from clipping into the environment. This setup also makes it possible to have different fields of view for the environment camera and the equipped items camera.  
**Split screen** | The example in `CameraStacking/SplitScreenPPUI` demonstrates how to create a split-screen camera setup where each screen has its own Camera Stack. It also demonstrates how to apply **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](../Glossary.html#post-processing) on world-space and screen-
space camera **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](../UI-
system-compare.html)  
See in [Glossary](../Glossary.html#UI).  
**3D**skybox** A special type of Material used to represent skies. Usually
six-sided. [More info](../sky-landing.html)  
See in [Glossary](../Glossary.html#Skybox)** | The example in `CameraStacking/3D Skybox` uses Camera Stacking to transform a miniature environment into a skybox. One overlay camera renders a miniature city and another renders miniature planets. The overlay cameras render to **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) that the main camera did not draw
to. With some additional scripted translation, this makes the miniature
environment appear full size in the background of the main camera’s view.  
  
### Decals

The `URP Package Samples/Decals` folder contains examples for
[decals](renderer-feature-decal.html). The following table describes each
decal example in this folder.

**Example** | **Description**  
---|---  
**Blob shadows** | The example in `Decals/BlobShadow` uses the [Decal Projector component](renderer-feature-decal.html) to cast a shadow under a character. This method of shadow rendering is less resource-intensive than shadow maps and is suitable for use on low-end devices.  
**Paint splat** | The example in `Decals/PaintSplat` uses a WorldSpaceUV Sub Graph and the [Simple Noise](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Simple-Noise-Node.html) Shader Graph node to create procedural decals. The noise in each paint splat uses the world position of the Decal Projector component.  
**Proxy lighting** | The example in `Decals/ProxyLighting` builds on the **Blob shadows** example and uses Decal Projectors to add proxy spotlights. These decals modify the emission of surfaces inside the projector’s volume.  
  
**Note** : To demonstrate the extent of its lighting simulation, this example
disables normal real-time lighting.  
  
### Lens Flares

The `URP Package Samples/LensFlares` folder contains **lens flare** A
component that simulates the effect of lights refracting inside a camera lens.
Use a Lens Flare to represent very bright lights or add atmosphere to your
scene. [More info](../class-LensFlare.html)  
See in [Glossary](../Glossary.html#LensFlare) examples. The following table
describes each lens flare example in this folder.

**Example** | **Description**  
---|---  
**Sun flare** | The `LensFlares/SunFlare` example demonstrates how to use the [Lens Flare component](shared/lens-flare/lens-flare-component.html) to add a lens flare effect to the main directional light in the scene.  
**Lens flare showroom** | The `LensFlares/LensFlareShowroom` example helps you to author lens flares. To use it:  
1\. In the Hierarchy window, select the **Lens Flare** GameObject.  
2\. In the Lens Flare component, assign a
[LensFlareDataSRP](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@12.0/api/UnityEngine.Rendering.LensFlareDataSRP.html) asset to
the **Lens Flare Data** property.  
3\. Change the Lens Flare component and data properties and view the lens
flare in the Game View.  
**Note** : If the text box is in the way, disable the Canvas in the scene.  
  
### Lighting

The `URP Package Samples/Lighting` folder contains examples for
[lighting](lighting-landing.html). The following table describes each lighting
example in this folder.

**Example** | **Description**  
---|---  
**Reflection probes** | The example in `Lighting/Reflection Probes` uses [reflection probes](lighting/reflection-probes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](../class-ReflectionProbe.html)  
See in [Glossary](../Glossary.html#ReflectionProbe) to create reflection maps
for a reflective sphere **GameObject** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject). This sample shows how the
**Probe Blending** and **Box Projection** settings can change the reflection
within a scene that uses reflection probes.  
  
### Renderer Features

The `URP Package Samples/RendererFeatures` folder contains examples for
[Renderer Features](urp-renderer-feature.html). The following table describes
each Renderer Feature example in this folder.

**Example** | **Description**  
---|---  
****Ambient occlusion** A method to approximate how much ambient light (light
not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](../Glossary.html#Ambientocclusion)** | The example in `RendererFeatures/AmbientOcclusion` uses a Renderer Feature to add [screen space ambient occlusion (SSAO)](post-processing-ssao.html) to URP. For an example of how to set up this effect, refer to the `SSAO_Renderer` asset.  
**Glitch effect** | The example in `RendererFeatures/GlitchEffect` uses the [Render Objects](renderer-features/renderer-feature-render-objects.html) Render Feature and the [Scene Color](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Scene-Color-Node.html) Shader Graph node to draw some GameObjects with a glitchy effect. For an example of how to set up this effect, refer to the `Glitch_Renderer` asset.  
**Keep frame** | The example in `RendererFeatures/KeepFrame` uses a custom Renderer Feature to preserve frame color between frames. The example uses this to create a swirl effect from a simple particle system.  
**Note** : The effect is only visible in Play Mode.  
**Occlusion effect** | The example in `RendererFeatures/OcclusionEffect` uses the Render Objects Renderer Feature to draw occluded geometry. The example achieves this effect without any code and sets everything up in the `OcclusionEffect_Renderer` asset.  
**Trail effect** | The example in `RendererFeatures/TrailEffect` uses the Renderer Feature from the **Keep frame** example on an additional camera to create a trail map. To do this, the additional camera draws depth to a RenderTexture. The `Sand_Graph` shader samples the map and displaces vertices on the ground.  
  
### Shaders

The `URP Package Samples/Shaders` folder contains examples for shaders. The
following table describes each shader example in this folder.

**Example** | **Description**  
---|---  
**Lit** | The example in `Shaders/Lit` demonstrates how different properties of the [Lit shader](lit-shader.html) affect the surface of some geometry. You can use the materials and textures as guidelines on how to set up materials in URP.  
  
[](../urp/package-samples.html)

Import a package sample in URP

[](../urp/InstallURPIntoAProject.html)

Install URP into an existing project

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

