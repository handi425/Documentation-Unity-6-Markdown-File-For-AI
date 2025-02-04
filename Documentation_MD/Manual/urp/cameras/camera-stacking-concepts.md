[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/cameras/camera-stacking-concepts.html)
  * [中文](/cn/current/Manual/urp/cameras/camera-stacking-concepts.html)
  * [日本語](/ja/current/Manual/urp/cameras/camera-stacking-concepts.html)
  * [한국어](/kr/current/Manual/urp/cameras/camera-stacking-concepts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/cameras/camera-stacking-concepts.html)
  * [中文](/cn/current/Manual/urp/cameras/camera-stacking-concepts.html)
  * [日本語](/ja/current/Manual/urp/cameras/camera-stacking-concepts.html)
  * [한국어](/kr/current/Manual/urp/cameras/camera-stacking-concepts.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](../../urp/cameras-multiple.html)
  * Camera stacking in URP

[](../../urp/cameras-multiple.html)

Multiple cameras in URP

[](../../urp/camera-stacking.html)

Set up a camera stack in URP

# Camera stacking in URP

In the Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../../render-
pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (URP), you use
**camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) stacking to layer the output of
multiple Cameras and create a single combined output. Camera stacking allows
you to create effects such as a 3D model in a 2D **UI**(User Interface) Allows
a user to interact with your application. Unity currently supports three UI
systems. [More info](../../UI-system-compare.html)  
See in [Glossary](../../Glossary.html#UI), or the cockpit of a vehicle.

A camera stack consists of a [Base Camera](../camera-types-and-render-type-
introduction.html#base-camera) and one or more [Overlay Cameras](../camera-
types-and-render-type-introduction.html#overlay-camera). A camera stack
overrides the output of the Base Camera with the combined output of all the
cameras in the camera stack. As a result, anything you can do with the output
of a Base Camera, you can do with the output of a camera stack. For example,
you can render a camera stack to a render target, or apply **post-processing**
A process that improves product visuals by applying filters and effects before
the image appears on screen. You can use post-processing effects to simulate
physical camera and film properties, for example Bloom and Depth of Field.
[More info](../../PostProcessingOverview.html) post processing,
postprocessing, postprocess  
See in [Glossary](../../Glossary.html#post-processing) effects.

Refer to [Set up a camera stack](../camera-stacking.html) for more
information. To download examples of camera stacking in URP, install the
[Camera Stacking samples](../package-sample-urp-package-samples.html#camera-
stacking).

## Camera stacking and rendering order

URP performs several optimizations within a camera, including rendering order
optimizations to reduce overdraw. However, when you use a camera stack, you
define the order in which URP renders the cameras. You must be careful not to
order the cameras in a way that causes excessive overdraw. For more
information on overdraw in URP, refer to [Rendering order
optimizations](../cameras-advanced.html#rendering-order-optimizations).

## Camera stacking and post-processing

You should only apply post-processing to the last camera in the stack, so the
following applies:

  * URP renders the post-processing effects only once, not repeatedly for each camera.
  * The visual effects are consistent, because all the cameras in the stack receive the same post-processing.

## Limitations

You cannot use a mix of different types of renderers (2D and 3D) for cameras
in a camera stack.

## Additional resources

  * [Set up a camera stack](../camera-stacking.html)
  * [Camera component reference](../camera-component-reference.html)

[](../../urp/cameras-multiple.html)

Multiple cameras in URP

[](../../urp/camera-stacking.html)

Set up a camera stack in URP

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

