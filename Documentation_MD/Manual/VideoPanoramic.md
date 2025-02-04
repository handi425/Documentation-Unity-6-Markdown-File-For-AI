[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/VideoPanoramic.html)
  * [中文](/cn/current/Manual/VideoPanoramic.html)
  * [日本語](/ja/current/Manual/VideoPanoramic.html)
  * [한국어](/kr/current/Manual/VideoPanoramic.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/VideoPanoramic.html)
  * [中文](/cn/current/Manual/VideoPanoramic.html)
  * [日本語](/ja/current/Manual/VideoPanoramic.html)
  * [한국어](/kr/current/Manual/VideoPanoramic.html)

  * [Video and cutscenes](Video.html)
  * [Video Player](VideoPlayer.html)
  * Panoramic video

[](video-clock.html)

Clock management with the Video Player component

[](profiler-video-profiler-module.html)

Video Profiler module

# Panoramic video

Unity’s panoramic video feature enables you to:

  * Easily include real-world video shot in 360 degrees.
  * Reduce **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) complexity in **VR** Virtual Reality
[More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) by including a pre-rendered backdrop video
instead of real geometry.

Unity supports 180 and 360 degree videos in either an
[equirectangular](https://en.wikipedia.org/wiki/Equirectangular_projection)
layout (longitude and latitude) or a
[cubemap](https://docs.unity3d.com/2017.2/Documentation/Manual/class-
Cubemap.html) layout (6 frames).

Equirectangular 2D videos should have an **aspect ratio** The relationship of
an image’s proportional dimensions, such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio) of exactly 2:1 for 360 content,
or 1:1 for 180 content.

![Equirectangular 2D video](../uploads/Main/Equirectangular2D.jpg)
Equirectangular 2D video

Cubemap 2D videos should have an aspect ratio of 1:6, 3:4, 4:3, or 6:1,
depending on face layout:

![Cubemap 2D video](../uploads/Main/Cubemap2D.jpg) Cubemap 2D video

To use the panoramic video features in the Unity Editor, you must have access
to panoramic video clips, or know how to author them.

This page describes the following steps to display any panoramic video in the
Editor:

  1. Set up a [Video Player](class-VideoPlayer.html) to play the video source to a [Render Texture](class-RenderTexture.html).

  2. Set up a [Skybox](sky-landing.html) Material that receives the Render Texture.

  3. Set the Scene to use the Skybox Material.

**Note** : This is a resource-intensive feature. For best visual results, use
panoramic videos in the highest possible resolution (often 4K or 8K). Large
videos require more computing power and resources for decoding. Most systems
have specific limits on maximum video decoding resolutions (for example, many
mobiles are limited to HD or 2K, and older desktops might be limited to 2K or
4K).

## 1\. Video player setup

Import your video into Unity as an [Asset](ImportingAssets.html). To create a
Video Player, drag the video Asset from the Project view to an empty area of
Unity’s Hierarchy view. By default, this sets up the component to play the
video full-screen for the default **Camera** A component which creates an
image of a particular viewpoint in your scene. The output is either drawn to
the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Press **Play** to view this.

You should change this behaviour so that it renders to a Render Texture. That
way, you can control exactly how it is displayed. To do this, go to **Assets**
Any media or data that can be used in your game or project. An asset may come
from a file created outside of Unity, such as a 3D Model, an audio file or an
image. You can also create some asset types in Unity, such as an Animator
Controller, an Audio Mixer or a Render Texture. [More
info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) > **Create** > **Render Texture** A
special type of Texture that is created and updated at runtime. To use them,
first create a new Render Texture and designate one of your Cameras to render
into it. Then you can use the Render Texture in a Material just like a regular
Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture).

Set the Render Texture’s **Size** to match your video exactly. To check the
dimensions of your video, select the video in your Assets folder and view the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. Scroll to the section where
Unity previews your video, select your video’s name in the preview window, and
change it to **Source Info**.

Next, set your Render Texture’s **Depth Buffer** A memory store that holds the
z-value depth of each pixel in an image, where the z-value is the depth for
each rendered pixel from the projection plane. [More info](class-
RenderTexture.html)  
See in [Glossary](Glossary.html#depthbuffer) option to **No depth buffer**.

![Render Texture set to No depth buffer](../uploads/Main/DepthBuffer.jpg)
Render Texture set to **No depth buffer**

Now, open the **Video Player** Inspector and switch the **Render Mode** to
**Render Texture**. Drag your new Render Texture from the Asset view to the
**Target Texture** slot.

Enter Play mode to verify that this is functioning correctly.

The video doesn’t render in the **Game** window, but you can select the Render
Texture Asset to see that its content updating with each video frame.

![](../uploads/Main/RenderTextureAsset.jpg)

## 2\. Create a Skybox Material

You need to replace the default Skybox with your video content to render the
panoramic video as a backdrop to your Scene.

To do this, create a new Material (**Assets** > **Create** > **Material** An
asset that defines how a surface should be rendered. [More info](class-
Material.html)  
See in [Glossary](Glossary.html#Material)). Go to your new Material’s
Inspector and set the Material’s Shader to Skybox/Panoramic (go to **Shader**
A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) > **Skybox** A special type of
Material used to represent skies. Usually six-sided. [More info](sky-
landing.html)  
See in [Glossary](Glossary.html#Skybox) > **Panoramic**).

Drag the Render Texture from the Asset view to the Texture slot in the new
Material’s Inspector.

You must correctly identify the type of content in the video (cubemap or
equirectangular) for the panoramic video to display properly. For cubemap
content (such as a cross and strip layout, as is common for static Skybox
Textures), set **Mapping** to **6 Frames Layout**.

For equirectangular content, set **Mapping** to **Latitude Longitude Layout**
, and then either the **360 degree** or **180 degree** sub-option. Choose the
**360 degree** option if the video covers a full 360-degree view. Choose **180
degree** if the video is just a front-facing 180-degree view.

Look at the **Preview** at the bottom of the Material Inspector. Pan around
and check that the content looks correct.

## 3\. Render the panoramic video to the Skybox

Finally, you must connect your new Skybox Material to the Scene.

  1. Open up the Lighting window (menu: **Window** > **General** > **Lighting**).

  2. Drag and drop the new Skybox Material Asset to the first slot under **Environment**. 

  3. Press Play to show the video as a Scene backdrop on the Skybox.

  4. Change the Scene Camera orientation to show a different portion of the Skybox (and therefore a different portion of the panoramic video).

## 3D panoramic video

Turn on Virtual Reality Support in the **Player** settings (menu: **Edit** >
**Project Settings** A broad collection of settings which allow you to
configure how Physics, Audio, Networking, Graphics, Input and many other areas
of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings), then select the **Player**
category, and open the **XR Settings** panel), especially if your source video
has stereo content. This unlocks an extra **3D Layout** option in the
Skybox/Panoramic Material. The 3D Layout has three options : **Side by Side**
, **Over** **Under** , and **None** (default value).

Use the **Side by Side** settings if the video contains the left eye’s content
on the left and the right eye’s content on the right. Choose **Over Under** if
the left and right content are positioned above and below one another in the
video. Unity detects which eye is currently being rendered and sends this
information to the Skybox/Panoramic shader using [Single Pass Stereo
rendering](https://docs.unity3d.com/Manual/SinglePassStereoRendering.html).
The shader contains the logic to select the correct half of the video based on
this information when Unity renders each eye’s content in VR.

![3D panoramic video](../uploads/Main/3dPanoramicVideo.jpg) 3D panoramic video

For non–360 3D video (where you shouldn’t use a Skybox Material), the same
**3D Layout** is available directly in the Video Player component when using
the Camera **Near/Far** Plane Render Modes.

## Alternate Render Texture type for cubemap videos

When working with cubemap videos, instead of the Video Player rendering to a
2D Render Texture and preserving the exact cube map layout, you can render the
Video Player directly to a Render Texture Cube.

To achieve this, change the Render Texture Asset’s **Dimension** from **2D**
to **Cube and set the Render Texture’s** Size__ to be exactly the dimensions
of the individual faces of the source video.

For example, if you have a 4 x 3 horizontal cross cubemap layout video with
dimensions 4096 x 3072, set the Render Texture’s **Size** to 1024 x 1024 (4096
/ 4 and 3072 / 3).

While rendering to a Cube Target Texture, the Video Player assumes that the
source video contains a cube map in either a cross or a strip layout (which it
determines using the video aspect ratio). The Video Player then fills out the
Render Texture’s faces with the correct cube faces.

Use the resulting Render Texture Cube as a Skybox. To do this, create a
Material and assign **Skybox/Cubemap** as the **Shader**(**Shader** >
**Skybox** > **Cubemap** A collection of six square textures that can
represent the reflections in an environment or the skybox drawn behind your
geometry. The six squares form the faces of an imaginary cube that surrounds
an object; each face represents the view along the directions of the world
axes (up, down, left, right, forward and back). [More info](class-Cubemap-
landing.html)  
See in [Glossary](Glossary.html#Cubemap)) instead of the Skybox/Panoramic
Material described above.

## Video dimensions and transcoding

Including 3D content requires double either the width or the height of the
video (corresponding to **Side-by-Side** or **Over-Under** layouts).

Keep in mind that many desktop hardware video decoders are limited to 4K
resolutions and mobile hardware video decoders are often limited to 2K or less
which limits the resolution of playback in real-time on those platforms.

You can use video transcoding to produce lower resolution versions of
panoramic videos, but take precautions to avoid introducing bleeding at the
edge between left and right 3D content, or, between cube map faces and
adjacent black areas. In general, you should author video in power-of-two
dimensions and transcoding to other power-of-two dimensions to reduce visual
artifacts.

* * *

  * 2017–10–25 Page published 

  * Added 2D and 3D panoramic video support in [2017.3](https://docs.unity3d.com/2017.3/Documentation/Manual/30_search.html?q=newin20173) NewIn20173

[](video-clock.html)

Clock management with the Video Player component

[](profiler-video-profiler-module.html)

Video Profiler module

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

