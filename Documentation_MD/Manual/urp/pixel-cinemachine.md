[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/pixel-cinemachine.html)
  * [中文](/cn/current/Manual/urp/pixel-cinemachine.html)
  * [日本語](/ja/current/Manual/urp/pixel-cinemachine.html)
  * [한국어](/kr/current/Manual/urp/pixel-cinemachine.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/pixel-cinemachine.html)
  * [中文](/cn/current/Manual/urp/pixel-cinemachine.html)
  * [日本語](/ja/current/Manual/urp/pixel-cinemachine.html)
  * [한국어](/kr/current/Manual/urp/pixel-cinemachine.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [Precise pixel scaling and rotation via the Pixel Perfect Camera in URP](../urp/2d-pixelperfect.html)
  * Make Cinemachine compatible with the 2D Pixel Perfect camera in URP

[](../urp/2d-pixelperfect-prep-sprites.html)

Prepare your sprites for the 2D Pixel Perfect Camera in URP

[](../urp/2d-pixelperfect-ref.html)

Pixel Perfect Camera component reference for URP

# Make Cinemachine compatible with the 2D Pixel Perfect camera in URP

Add the **Cinemachine**Pixel** The smallest unit in a computer image. Pixel
size depends on your screen resolution. Pixel lighting is calculated at every
screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) Perfect** to the Cinemachine Virtual
Cameras to use both the **Pixel Perfect**Camera** A component which creates an
image of a particular viewpoint in your scene. The output is either drawn to
the screen or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera)** and
[Cinemachine](https://unity.com/unity/features/editor/art-and-
design/cinemachine) together. Both systems modify the Camera’s orthographic
size, so using these two systems together in a single **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) would cause them to fight for
control over the Camera and produce unwanted results. The **Cinemachine Pixel
Perfect** extension solves this incompatibility.

**Cinemachine Pixel Perfect** is an
[extension](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.2/manual/CinemachineVirtualCameraExtensions.html)
for the **Cinemachine Virtual Camera** that alters the orthographic size of
the virtual camera. The extension detects the presence of the Pixel Perfect
Camera component, and uses the component settings to calculate for the correct
orthographic size of the virtual camera that best retains the **Sprites** A 2D
graphic objects. If you are used to working in 3D, Sprites are essentially
just standard textures but there are special techniques for combining and
managing sprite textures for efficiency and convenience during development.
[More info](../sprite/sprite-landing.html)  
See in [Glossary](../Glossary.html#Sprite) in a pixel-perfect resolution.

To add this extension to your virtual cameras, use the **Add Extension**
dropdown menu on the Cinemachine Virtual Camera **Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) window. Add this extension to
each virtual camera in your Project.

![](../../uploads/urp/2D/cine_2Dpixelperfect_ex.png)

For each virtual camera attached with this extension, the Pixel Perfect Camera
component then calculates a pixel-perfect orthographic size that best matches
the original size of the virtual camera during **Play Mode** or when **Run In
Edit Mode** is enabled. This is done to match the original framing of each
virtual camera as close as possible when the pixel-perfect calculations are
implemented.

When the [Cinemachine
Brain](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.3/manual/CinemachineBrainProperties.html)
component
[blends](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.3/manual/CinemachineBlending.html)Transition
from one animation to another animation smoothly and seamlessly, such as
blending a character’s walking and running animations according to the
character’s speed.  
See in [Glossary](../Glossary.html#blend) between multiple virtual cameras,
the rendered image is temporarily not pixel-perfect during the transition
between cameras. The image becomes pixel-perfect once the view fully
transitions to a single virtual camera.

The following are the current limitations of the extension:

  * When a virtual camera with the Pixel Perfect extension is set to follow a [Target Group](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.3/manual/CinemachineTargetGroup.html), there may be visible choppiness when the virtual camera is positioned with the [Framing Transposer](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.9/manual/CinemachineBodyFramingTransposer.html) component.
  * If the **Upscale**Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture)** option is enabled on the
Pixel Perfect Camera, there are less possible pixel-perfect resolutions that
match the original orthographic size of the virtual cameras. This may cause
the framing of the virtual cameras to be off by quite a large margin after the
pixel-perfect calculations.

[](../urp/2d-pixelperfect-prep-sprites.html)

Prepare your sprites for the 2D Pixel Perfect Camera in URP

[](../urp/2d-pixelperfect-ref.html)

Pixel Perfect Camera component reference for URP

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

