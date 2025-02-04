[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-canvas-size.html)
  * [中文](/cn/current/Manual/webgl-canvas-size.html)
  * [日本語](/ja/current/Manual/webgl-canvas-size.html)
  * [한국어](/kr/current/Manual/webgl-canvas-size.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-canvas-size.html)
  * [中文](/cn/current/Manual/webgl-canvas-size.html)
  * [日本語](/ja/current/Manual/webgl-canvas-size.html)
  * [한국어](/kr/current/Manual/webgl-canvas-size.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Configure a Web Canvas size

[](webgl-input.html)

Input in Web

[](webgl-browser-access-device.html)

Web browser access to device features

# Configure a Web Canvas size

In a Web application, the canvas element is where the browser draws the
graphics when rendering a game. This section describes how to configure the
visible size of the Web canvas element, and the resolution that the game
renders to.

To configure your Web Canvas size, you must consider the following types of
canvas size:

**Canvas Size elements** | **Description**  
---|---  
**Canvas element CSS size** | This Document Object Model (DOM) specifies the visible area on the web page that the canvas takes up. You can configure the canvas size using HTML or JavaScript.  
**WebGL render target size** | This size specifies the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) resolution that the GPU renders your
game to. You can manage this size in sync with the CSS size to provide pixel-
perfect rendering, or decouple it from the CSS size.  
  
If the above two canvas size elements don’t match, the browser will stretch
the rendered **WebGL** A JavaScript API that renders 2D and 3D graphics in a
web browser. The Unity Web build option allows Unity to publish content as
JavaScript programs which use HTML5 technologies and the WebGL rendering API
to run Unity content in a web browser. [More info](webgl.html)  
See in [Glossary](Glossary.html#WebGL) output to fill the visible canvas area
on the web page.

## Decouple the render resolution

Decoupling the render resolution is useful when implementing downscaled low
DPI (Dots per inch) rendering on high DPI display. This helps to not only
conserve the GPU fill rate power but also helps if your application is
sensitive to the rendering resolution. For example, if your application logic
uses screen space pixel units, but for the application itself to work
properly, it requires a specific resolution.

By default, Unity keeps the canvas element CSS size and the WebGL render
target size in sync and provides 1:1 pixel perfect rendering. If the web page
in JavaScript modifies the canvas CSS size, Unity will automatically adjust
the WebGL render target size to match it. By default, this match is done to
implement high DPI rendering.

### Override DPI scale

If you want to override the DPI scale, open the `index.html` file and add the
Unity Instance configuration variable `devicePixelRatio=<double>`. For
example, setting `devicePixelRatio=1` on the Web site template page will force
Unity to always apply low DPI rendering. Refer to [Web template build
configuration and interaction](web-templates-build-configuration.html) for an
example.

### Manually change the Web canvas render size

To manually configure the canvas size, you must first disable the automatic
size synchronization. To do so, in the `index.html` file of the Web template,
set the Unity Instance configuration variable to false:
`matchWebGLToCanvasSize=false`. When this is set, Unity leaves the render
target size of the canvas as-is but you can always configure the size, if
required.

For example, to change the CSS size of the canvas, edit the following text in
the `index.html` file:

    
    
    <div id="unity-container" style="position: absolute; width: 100%; height: 100%">
      <canvas id="unity-canvas" width={{{ WIDTH }}} height={{{ HEIGHT }}} style="width: 100%; height: 100%"></canvas>
    </div>
    

[](webgl-input.html)

Input in Web

[](webgl-browser-access-device.html)

Web browser access to device features

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

