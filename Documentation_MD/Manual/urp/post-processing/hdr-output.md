[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/post-processing/hdr-output.html)
  * [中文](/cn/current/Manual/urp/post-processing/hdr-output.html)
  * [日本語](/ja/current/Manual/urp/post-processing/hdr-output.html)
  * [한국어](/kr/current/Manual/urp/post-processing/hdr-output.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/post-processing/hdr-output.html)
  * [中文](/cn/current/Manual/urp/post-processing/hdr-output.html)
  * [日本語](/ja/current/Manual/urp/post-processing/hdr-output.html)
  * [한국어](/kr/current/Manual/urp/post-processing/hdr-output.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Color](../../graphics-color.html)
  * [High dynamic range (HDR)](../../hdr-landing.html)
  * [HDR](../../urp/post-processing/hdr-in-urp.html)
  * HDR Output in URP

[](../../urp/post-processing/hdr-in-urp.html)

HDR

[](../../urp/post-processing/hdr-output-debug-views-urp.html)

HDR Output debug views in URP

# HDR Output in URP

[High Dynamic Range](https://docs.unity3d.com/Manual/HDR.html) content has a
wider color gamut and greater luminosity range than standard definition
content.

URP can output **HDR** high dynamic range  
See in [Glossary](../../Glossary.html#HDR) content for displays which support
that functionality.

**Note** : You can only use HDR Output with a linear color space. For more
information on color spaces in Unity, refer to [Color space](../../color-
spaces-landing.html).

## Understand HDR Output implementation

Unity’s HDR Output is split into the following steps which always occur in
this order:

  1. Tone mapping
  2. Transfer Function

### Tone mapping

Tone mapping is the first step in the HDR Output process. In this step, Unity
balances the exposure and hue of the **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) according to the target display’s
dynamic range. Dynamic range is determined by the following properties:

  * **Minimum brightness**
  * **Maximum brightness**
  * **Paper white brightness**

For more information on these properties, refer to Important tone mapping
values.

At the same time, Unity performs the color space conversion. Unity converts
the colors from the default Rec. 709 color space to the target display’s color
space. This maps the colors in the scene to the wider gamut of colors of the
target display and ensures Unity utilizes the full color gamut available on
the display.

For more information, refer to HDR tone mapping in URP and configure HDR tone
mapping settings.

### Transfer function

The second step of HDR Output is the transfer function. The transfer function
converts the output of the rendering process to levels of brightness of a
given display. Unity determines the correct transfer function for the display
and uses it to encode the output according to the standard the display
expects. This enables Unity to use the correct level of precision for the
gamma and create accurate exposure levels on the target display.

## HDR tone mapping in URP

After you enable **Allow HDR Display Output** , you must configure [tone
mapping](./../post-processing-tonemapping.html) settings for your HDR input.

In order to configure these settings effectively, you need to understand how
certain values related to tone mapping determine the visual characteristics of
your HDR output.

### Important tone mapping values

To properly make use of the capabilities of HDR displays, your
****Tonemapping** The process of remapping HDR values of an image into a range
suitable to be displayed on screen. [More
info](../../PostProcessingOverview.html)  
See in [Glossary](../../Glossary.html#Tonemapping)** configuration must take
into account the capabilities of the target display, specifically these three
values (in nits):

  * **Minimum supported brightness**.
  * **Maximum supported brightness**.
  * **Paper White value** : This value represents the brightness of a paper-white surface represented on the display, which determines the display’s brightness overall.

**Note** : Low Dynamic Range (LDR) and High Dynamic Range (HDR) content do not
appear equally bright on displays with the same Paper White value. This is
because displays apply extra processing to low dynamic range content that
bumps its brightness levels up. For this reason, it is best practice to
implement a calibration menu for your application.

### Usable user interfaces depend on accurate Paper White values

[Unlit](./../unlit-shader.html) materials do not respond to lighting changes,
so it is standard practice to use an Unlit material for user interfaces.
Calculations for Unlit material rendering define brightness with values
between 0 and 1 when you are not specifically targeting HDR displays. In this
context, a value of 1 corresponds to white, and a value of 0 corresponds to
black.

However, in HDR mode, URP uses Paper White values to determine the brightness
of Unlit materials. This is because HDR values can exceed the 0 to 1 range.

As a result, Paper White values determine the brightness of **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](../../UI-system-compare.html)  
See in [Glossary](../../Glossary.html#UI) elements in HDR mode, especially
white elements, whose brightness matches Paper White values.

## Configure HDR tone mapping settings

You can select and adjust tone mapping modes in the [Tonemapping Volume
component](../post-processing-tonemapping.html) settings. You can also adjust
some aspects of your HDR tone mapping configuration with a script. For more
information on this, refer to the HDROutputSettings API.

After you enable **Allow HDR Display Output** , HDR tone mapping options
become visible in the Volume component.

### Tonemapping

URP provides two **Tonemapping** modes: **Neutral** and **ACES**. Each tone
mapping mode has some unique properties.

  * **Neutral** mode is especially suitable for situations where you do not want the tone mapper to color grade your content.
  * **ACES** mode uses the ACES reference color space for feature films. It produces a cinematic, contrasty result.

For more information on these modes, refer to the [HDR Output section of
Tonemapping Volume Override reference](../post-processing-
tonemapping.html#hdr-output).

### The HDROutputSettings API

The
[HDROutputSettings](https://docs.unity3d.com/ScriptReference/HDROutputSettings.html)
API makes it possible to enable and disable HDR mode, as well as query certain
values (such as Paper White).

These values are also listed on the HDR output display table on the Rendering
Debugger. To access the table, navigate to **Window** > **Analysis** >
**Render Pipeline Debugger** > **Rendering** > **HDR Output**.

## Use Offscreen Rendering with HDR Output

When you use offscreen rendering techniques, not all cameras in a scene output
directly to the display, for example, when Unity renders the output to a
**Render Texture** A special type of Texture that is created and updated at
runtime. To use them, first create a new Render Texture and designate one of
your Cameras to render into it. Then you can use the Render Texture in a
Material just like a regular Texture. [More info](../../class-
RenderTexture.html)  
See in [Glossary](../../Glossary.html#RenderTexture). In these situations, use
the output of the **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) before rendering **post-
processing** A process that improves product visuals by applying filters and
effects before the image appears on screen. You can use post-processing
effects to simulate physical camera and film properties, for example Bloom and
Depth of Field. [More info](../../PostProcessingOverview.html) post
processing, postprocessing, postprocess  
See in [Glossary](../../Glossary.html#post-processing).

Unity does not apply HDR Output processing to the output of cameras which use
offscreen rendering techniques. This prevents HDR Output processing from being
applied twice to the camera’s output.

## Use Standard Dynamic Range (SDR) Rendering with HDR Output enabled

HDR Output relies on HDR Rendering to provide **pixel** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](../../ShadowPerformance.html)  
See in [Glossary](../../Glossary.html#pixel) values in the correct format for
tone mapping and color encoding. The values after HDR tone mapping are in nits
and exceed 1. This differs from SDR Rendering where the pixel values are
between 0 and 1. As a result of this, the use of SDR Rendering with HDR Output
can cause the rendered image to look underexposed or oversaturated.

You can use SDR Rendering on a per-camera basis when you have HDR Output
enabled, this can be useful for cameras that only render unlit materials, for
example, for mini-map rendering. However, the use of SDR Rendering with HDR
Output imposes some limitations.

To ensure correct rendering when you use SDR Rendering with HDR Output, you
must avoid any render passes that occur after post-processing. This includes
URP’s built-in effects which insert render passes after post-processing. As a
result, SDR Rendering with HDR Output is incompatible with the following
features:

  * [Upscaling](../universalrp-asset.html#quality)
  * [FXAA](../anti-aliasing.html#fxaa)
  * [HDR Debug Views](hdr-output-debug-views-urp.html)
  * Custom passes which occur after post-processing

### 2D Renderer

To use SDR Rendering with HDR Output on the 2D Renderer, you must ensure post-
processing is turned off.

## Platform Compatibility

URP only supports HDR Output on the following platforms:

  * Windows with DirectX 11, DirectX 12 or Vulkan
  * MacOS devices that use Metal
  * iOS 16+ devices
  * Consoles
  * **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](../../XR.html)  
See in [Glossary](../../Glossary.html#XR) devices with HDR support

  * Android devices that use Vulkan and GLES

**Note** : DirectX 11 only supports HDR Output in the Player, it does not
support HDR Output in the Editor.

[](../../urp/post-processing/hdr-in-urp.html)

HDR

[](../../urp/post-processing/hdr-output-debug-views-urp.html)

HDR Output debug views in URP

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

