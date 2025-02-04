[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xr-render-pipeline-compatibility.html)
  * [中文](/cn/current/Manual/xr-render-pipeline-compatibility.html)
  * [日本語](/ja/current/Manual/xr-render-pipeline-compatibility.html)
  * [한국어](/kr/current/Manual/xr-render-pipeline-compatibility.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xr-render-pipeline-compatibility.html)
  * [中文](/cn/current/Manual/xr-render-pipeline-compatibility.html)
  * [日本語](/ja/current/Manual/xr-render-pipeline-compatibility.html)
  * [한국어](/kr/current/Manual/xr-render-pipeline-compatibility.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR graphics](xr-graphics.html)
  * Universal Render Pipeline compatibility in XR

[](xr-graphics.html)

XR graphics

[](SinglePassStereoRendering.html)

Stereo rendering

# Universal Render Pipeline compatibility in XR

Support for **XR** An umbrella term encompassing Virtual Reality (VR),
Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting
these forms of interactive applications can be referred to as XR devices.
[More info](XR.html)  
See in [Glossary](Glossary.html#XR) features in the Universal **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP) varies by URP package
version. This page details compatibility between XR features in Unity 6 and
the latest compatible URP version.

To determine which version of URP is compatible with your current Unity
version, refer to the [Requirements and
compatibility](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/?subfolder=/manual/requirements.html) page in the
Universal Render Pipeline documentation.

Unity 6 supports the following **AR** Augmented Reality [More
info](AROverview.html)  
See in [Glossary](Glossary.html#AR) and **VR** Virtual Reality [More
info](VROverview.html)  
See in [Glossary](Glossary.html#VR) features in the Universal Render Pipeline:

**Feature** | **Supported in XR**  
---|---  
**Post-processing** A process that improves product visuals by applying
filters and effects before the image appears on screen. You can use post-
processing effects to simulate physical camera and film properties, for
example Bloom and Depth of Field. [More info](PostProcessingOverview.html)
post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effects: Bloom | Yes  
Post-processing effects: MotionBlur | Yes  
Post-processing effects: Lens Distortion | No  
Post-processing effects: **Depth of Field** A post-processing effect that
simulates the focus properties of a camera lens. [More
info](PostProcessingOverview.html)  
See in [Glossary](Glossary.html#DepthofField) | Yes  
Post-processing effects: **ToneMapping** The process of remapping HDR values
of an image into a range suitable to be displayed on screen. [More
info](PostProcessingOverview.html)  
See in [Glossary](Glossary.html#Tonemapping) | Yes  
Other post-processing effects (color adjustment, etc.) | Yes  
GI (Global Illumination) | Yes  
**HDR** high dynamic range  
See in [Glossary](Glossary.html#HDR) | Yes  
MSAA | Yes  
Physical **Camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) | No  
CopyColor / ColorDepth | Yes  
Multi Display | No  
Camera Stacking | Yes  
Cascaded Shadow | Yes  
sRGB | Yes  
**Skybox** A special type of Material used to represent skies. Usually six-
sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) | Yes  
Fog | Yes  
**Billboard** A textured 2D object that rotates so that it always faces the
Camera. [More info](class-BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) | Yes  
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) Graph | Yes (1)  
Particles | Yes  
**Terrain** The landscape in your scene. A Terrain GameObject adds a large
flat plane to your scene and you can use the Terrain’s Inspector window to
create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) | Yes  
2D **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) (Canvas Renderer, Text Mesh Pro) | Yes  
URP Debug (Scene View Mode, Frame Debug) | Yes (2)  
  
  * (1) Although Shader Graph shaders can run in XR, Shader Graph doesn’t currently support the XR utility feature to create SPI-compatible shader input textures. Unity will expand support for Shader Graph functionality in future releases.
  * (2) Unity supports frame debugging for mock HMDs. Currently, there is no support for Meta/Oculus.

To learn more about post-processing effects, refer to the [Effect
list](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/?subfolder=/manual/EffectList.html) page in the
Universal Render Pipeline documentation.

[](xr-graphics.html)

XR graphics

[](SinglePassStereoRendering.html)

Stereo rendering

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

