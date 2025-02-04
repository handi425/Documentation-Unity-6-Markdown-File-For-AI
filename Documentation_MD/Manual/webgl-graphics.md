[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-graphics.html)
  * [中文](/cn/current/Manual/webgl-graphics.html)
  * [日本語](/ja/current/Manual/webgl-graphics.html)
  * [한국어](/kr/current/Manual/webgl-graphics.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-graphics.html)
  * [中文](/cn/current/Manual/webgl-graphics.html)
  * [日本語](/ja/current/Manual/webgl-graphics.html)
  * [한국어](/kr/current/Manual/webgl-graphics.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Web graphics

[](webgl-caching.html)

Cache behavior in Web

[](webgl-audio.html)

Audio in Web

# Web graphics

[WebGL](https://www.khronos.org/webgl/)A JavaScript API that renders 2D and 3D
graphics in a web browser. The Unity Web build option allows Unity to publish
content as JavaScript programs which use HTML5 technologies and the WebGL
rendering API to run Unity content in a web browser. [More info](webgl.html)  
See in [Glossary](Glossary.html#WebGL) is an API for rendering graphics in web
browsers, which is based on the functionality of the OpenGL ES graphics
library. WebGL 2.0 roughly matches with the OpenGL ES 3.0 functionality.

## Camera clear

By default, Unity Web clears the drawing buffer after each frame, which means
the content of the frame buffer clears regardless of the
[Camera.clearFlags](https://docs.unity3d.com/ScriptReference/Camera-
clearFlags.html) setting. However, you can change this behavior at
instantiation time. To do this, set
`webglContextAttributes.preserveDrawingBuffer` to `true` in the `index.html`
file of your Web template.

**Note** : If you set any [WebGL context
attributes](https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/getContextAttributes), you must also add
a line to preserve the **Power Preference** [Player setting](class-
PlayerSettingsWebGL.html#Publishing).

    
    
    script.onload = () => {
      config['webglContextAttributes'] = {
        preserveDrawingBuffer: true, //Add this line to preserve the Camera.clearFlags setting
        powerPreference: {{{ WEBGL_POWER_PREFERENCE }}} //Add this line to preserve the Power Preference Player setting
      };
      createUnityInstance(canvas, config, (progress) => {
    
    

## Global illumination

Unity Web only supports [baked GI](LightingInUnity.html#globalIllumination).
Realtime **Global Illumination** A group of techniques that model both direct
and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) isn’t currently supported
in Web. In addition, Unity Web supports Non-Directional **lightmaps** A pre-
rendered texture that contains the effects of light sources on static objects
in the scene. Lightmaps are overlaid on top of scene geometry to create the
effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) only.

## Linear rendering

Some web browsers don’t support [sRGB DXT texture compression](class-
TextureImporterOverride). This can decrease the quality of rendering
performance when using linear rendering, due to runtime decompression of all
the DXT textures.

## Video clip importer

You can’t use `VideoClipImporter` to import video clips to your Unity project,
because it might increase the initial asset data download size and prevent
network streaming. For video playback, use the URL option in the VideoPlayer
component and place the asset in the StreamingAssets/ directory to use the
built-in network streaming of your browser.

## Web shader code restrictions

The [WebGL 2.0
specification](https://www.khronos.org/registry/webgl/specs/2.0/) imposes some
limitations on GLSLS **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code. This is mainly relevant when you
write your own shaders. Here are some of the restrictions:

  * **Precision qualifiers** : WebGL 2.0 requires you to specify the precision of all variables in the shader. You can use `highp`, `mediump`, or `lowp` to specify the precision of the variable. If you don’t specify the precision, the shader will use the default precision, which is `mediump`. You can also use `precision` to specify the precision of a block of variables.

**Note:** Due to limited available memory in Web, avoid including unwanted
shader variants which can lead to unnecessary memory usage. Therefore, it’s
recommended to familiarize yourself with [shader variants](shader-
variants.html)A verion of a shader program that Unity generates according to a
specific combination of shader keywords and their status. A Shader object can
contain multiple shader variants. [More info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant) and [shader stripping](shader-
variant-stripping.html), and take extra care to ensure that you don’t add
shaders with too many variants (for example, Unity’s [Standard Shader](shader-
StandardShader.html)) to the [Always-included Shaders](class-
GraphicsSettings.html#Always) section in [Graphics Settings](class-
GraphicsSettings.html).

## Font rendering

Unity Web supports dynamic font rendering similar to other Unity platforms.
However, as it doesn’t have access to the fonts installed on the user’s
machine, if you want to use any fonts, make sure to include them in the
project folder (including any fallback fonts for international characters, or
bold/italic versions of fonts), and [set as fallback font names](UIE-fallback-
font.html).

## Anti-aliasing

WebGL supports anti-aliasing on most (but not on all) combinations of browsers
and GPUs. To use it, anti-aliasing must be enabled in the default
[Quality](class-QualitySettings.html) setting for the Web platform.

## Reflection probes

Unity Web supports all reflection probes.

## WebGL 2.0 support

Unity includes support for the [WebGL 2.0
API](https://www.khronos.org/registry/webgl/specs/latest/2.0/), which brings
OpenGL ES 3.0-level rendering capabilities to the web. By default, Unity Web
builds support the WebGL 2.0 API.

Browsers with WebGL 2.0 support have the following advantages:

  * The content in the Standard Shader is of high quality.
  * Support for [GPU Instancing](GPUInstancing.html) and directional lightmap.
  * There’s no restrictions on indexing and loops in shader code.
  * Improved performance.

### Additional resources:

  * [Reflection Probe](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe)

  * [Build your Web application](webgl-building.html)
  * [Web Player settings](class-PlayerSettingsWebGL.html)

* * *

[](webgl-caching.html)

Cache behavior in Web

[](webgl-audio.html)

Audio in Web

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

