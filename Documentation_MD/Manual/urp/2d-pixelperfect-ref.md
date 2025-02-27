[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2d-pixelperfect-ref.html)
  * [中文](/cn/current/Manual/urp/2d-pixelperfect-ref.html)
  * [日本語](/ja/current/Manual/urp/2d-pixelperfect-ref.html)
  * [한국어](/kr/current/Manual/urp/2d-pixelperfect-ref.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2d-pixelperfect-ref.html)
  * [中文](/cn/current/Manual/urp/2d-pixelperfect-ref.html)
  * [日本語](/ja/current/Manual/urp/2d-pixelperfect-ref.html)
  * [한국어](/kr/current/Manual/urp/2d-pixelperfect-ref.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [Precise pixel scaling and rotation via the Pixel Perfect Camera in URP](../urp/2d-pixelperfect.html)
  * Pixel Perfect Camera component reference for URP

[](../urp/pixel-cinemachine.html)

Make Cinemachine compatible with the 2D Pixel Perfect camera in URP

[](../TroubleShooting.html)

Troubleshooting

# Pixel Perfect Camera component reference for URP

Explore the different properties available to customize the appearance of your
2D **pixel** The smallest unit in a computer image. Pixel size depends on your
screen resolution. Pixel lighting is calculated at every screen pixel. [More
info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) art with the **Pixel
Perfect**Camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera)**.

![Property table](../../uploads/urp/2D/2D_Pix_image_7.png) The component’s
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) window

**Property** | **Function**  
---|---  
**Asset Pixels Per Unit** | This is the amount of pixels that make up one unit of the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene). Match this value to the **Pixels
Per Unit** values of all **sprites** A 2D graphic objects. If you are used to
working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](../sprite/sprite-landing.html)  
See in [Glossary](../Glossary.html#Sprite) in the scene.  
**Reference Resolution** | This is the original resolution your assets are designed for.  
**Crop Frame** | Select what to do when there is a difference in **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](../Glossary.html#AspectRatio).  
**Grid Snapping** | Select what to do when snapping.  
**Filter Mode** (Only available when **Stretch Fill** option is selected.) | Select the method Unity uses to upscale the final image.  
**Current Pixel Ratio** | Shows the size ratio of the rendered sprites compared to their original size.  
  
### Reference Resolution

This is the original resolution your Assets are designed for. Scaling up
scenes and assets from this resolution preserves your pixel art cleanly at
higher resolutions.

### Grid Snapping options

#### Upscale Render Texture

By default, the scene is rendered at the pixel perfect resolution closest to
the full screen resolution.

Enable this option to have the scene rendered to a temporary texture set as
close as possible to the **Reference Resolution** , while maintaining the full
screen aspect ratio. This temporary texture is then upscaled to fit the entire
screen.

![Box examples](../../uploads/urp/2D/2D_Pix_image_8.png) Box examples

The result is unaliased and unrotated pixels, which may be a desirable visual
style for certain game projects.

#### Pixel Snapping

Enable this feature to snap **sprite Renderers** A component that lets you
display images as Sprites for use in both 2D and 3D scenes. [More
info](../sprite/renderer/renderer-landing.html)  
See in [Glossary](../Glossary.html#SpriteRenderer) to a grid in world space at
render-time. The grid size is based on the **Assets Pixels Per Unit** value.

**Pixel Snapping** prevents subpixel movement and make sprites appear to move
in pixel-by-pixel increments. This does not affect any **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject)’ Transform positions.

### Crop Frame

Crops the **viewport** The user’s visible area of an app on their screen.  
See in [Glossary](../Glossary.html#Viewport) based on the option selected,
adding black bars to match the **Reference Resolution**. Black bars are added
to make the Game view fit the full screen resolution.

![Uncropped cat](../../uploads/urp/2D/2D_Pix_image_9.png) | ![Cropped cat](../../uploads/urp/2D/2D_Pix_image_10.png)  
---|---  
Uncropped | Cropped  
  
### Filter Mode

**Filter Mode** is only usable when **Stretch Fill** option is selected.

Defaults to **Retro AA** upscale filtering, where the image is upscaled as
close as possible to the screen resolution as a multiple of the **Reference
resolution** , followed by a bilinear filtering to upscale to the target
screen resolution.

**Point** filtering is also available for user preference. If you upscale the
image this way, it can suffer from bad pixel placement, thus losing pixel
perfectness.

![Uncropped cat](../../uploads/urp/2D/2D_Pix_image_11.png) | ![Cropped cat](../../uploads/urp/2D/2D_Pix_image_12.png)  
---|---  
Point | Retro AA  
![Uncropped cat](../../uploads/urp/2D/2D_Pix_image_13.png) | ![Cropped cat](../../uploads/urp/2D/2D_Pix_image_14.png)  
Upscale **Render Texture** A special type of Texture that is created and
updated at runtime. To use them, first create a new Render Texture and
designate one of your Cameras to render into it. Then you can use the Render
Texture in a Material just like a regular Texture. [More info](../class-
RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture) \+ Point | Upscale Render Texture + Retro AA  
  
[](../urp/pixel-cinemachine.html)

Make Cinemachine compatible with the 2D Pixel Perfect camera in URP

[](../TroubleShooting.html)

Troubleshooting

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

