[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PhysicalCameras-GateFit-Configure.html)
  * [中文](/cn/current/Manual/PhysicalCameras-GateFit-Configure.html)
  * [日本語](/ja/current/Manual/PhysicalCameras-GateFit-Configure.html)
  * [한국어](/kr/current/Manual/PhysicalCameras-GateFit-Configure.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PhysicalCameras-GateFit-Configure.html)
  * [中文](/cn/current/Manual/PhysicalCameras-GateFit-Configure.html)
  * [日本語](/ja/current/Manual/PhysicalCameras-GateFit-Configure.html)
  * [한국어](/kr/current/Manual/PhysicalCameras-GateFit-Configure.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Simulating real-world cameras with Physical Cameras](PhysicalCameras.html)
  * [Crop or stretch the view with Gate Fit](PhysicalCameras-GateFit-Landing.html)
  * Configure Gate Fit

[](PhysicalCameras-GateFit.html)

Introduction to Gate Fit

[](CameraOutput.html)

Camera output

# Configure Gate Fit

The **Gate Fit** mode you choose determines how Unity resizes the resolution
gate (and consequently, the camera’s view frustum). The film gate always stays
the same size.

The following sections provide more details on each Gate Fit mode.

### Vertical

When **Gate Fit** is set to **Vertical** , Unity fits the resolution gate to
the height (Y axis) of the film gate. Any change you make to the sensor width
(**Sensor Size > X**) has no effect on the rendered image.

If the sensor **aspect ratio** The relationship of an image’s proportional
dimensions, such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio) is larger than the game view
aspect ratio, Unity crops the rendered image at the sides:

![Gate Fit set to Vertical: Resolution gate aspect ratio is 0.66:1 \(600 x 900
px\). Film gate aspect ratio is 1.37:1 \(16mm\). The red areas indicate where
Unity crops the image in the Game
view.](../uploads/Main/GateFitV_600x900_16mm.png) **Gate Fit** set to
**Vertical** : Resolution gate aspect ratio is 0.66:1 (600 x 900 px). Film
gate aspect ratio is 1.37:1 (16mm). The red areas indicate where Unity crops
the image in the Game view.

If the sensor aspect ratio is smaller than the game view aspect ratio, Unity
overscans the rendered image at the sides:

![Gate Fit set to Vertical: Resolution gate aspect ratio is 16:9. Film gate
aspect ratio is 1.37:1 \(16mm\). The green areas indicate where Unity
overscans the image in the Game view.](../uploads/Main/GateFitV_16-9_16mm.png)
**Gate Fit** set to **Vertical** : Resolution gate aspect ratio is 16:9. Film
gate aspect ratio is 1.37:1 (16mm). The green areas indicate where Unity
overscans the image in the Game view.

### Horizontal

When **Gate Fit** is set to **Horizontal** , Unity fits the resolution gate to
the width (X axis) of the film gate. Any change you make to the sensor height
(Sensor Size > Y) has no effect on the rendered image.

If the sensor aspect ratio is larger than the Game view aspect ratio, Unity
overscans the rendered image on the top and bottom:

![Gate Fit is set to Horizontal: Resolution gate aspect ratio is 0.66:1 \(600
x 900 px\). Film gate aspect ratio is 1.37:1 \(16mm\). The green areas
indicate where Unity overscans the image in the Game
view.](../uploads/Main/GateFitH_600x900_16mm.png) **Gate Fit** is set to
**Horizontal** : Resolution gate aspect ratio is 0.66:1 (600 x 900 px). Film
gate aspect ratio is 1.37:1 (16mm). The green areas indicate where Unity
overscans the image in the Game view.

If the sensor aspect ratio is smaller than the game view aspect ratio, the
rendered image is cropped on the top and bottom.

![Gate Fit set to Horizontal: Resolution gate aspect ratio is 16:9. Film gate
aspect ratio is 1.37:1 \(16mm\). The red areas indicate where Unity crops the
image in the Game view.](../uploads/Main/GateFitH_16-9_16mm.png) **Gate Fit**
set to **Horizontal** : Resolution gate aspect ratio is 16:9. Film gate aspect
ratio is 1.37:1 (16mm). The red areas indicate where Unity crops the image in
the Game view.

### None

When Gate Fit is set to None, Unity fits the resolution gate to the width and
height (X and Y axes) of the film gate. Unity stretches the rendered image to
fit the Game view aspect ratio.

![No gate fit. The camera uses the film gate aspect ratio of 1.37:1 \(16mm\),
and stretches the image horizontally to fit a Game view aspect ratio of 16:9
\(left\) and vertically to fit a game view aspect ratio of 0.66:1
\(right\)](../uploads/Main/GateFitF_16mm.png) No gate fit. The camera uses the
film gate aspect ratio of 1.37:1 (16mm), and stretches the image horizontally
to fit a Game view aspect ratio of 16:9 (left) and vertically to fit a game
view aspect ratio of 0.66:1 (right)

### Fill and Overscan

When **Gate Fit** is set to **Fill** or **Overscan** , Unity automatically
performs either a vertical or horizontal fit, depending on the resolution gate
and film gate aspect ratios.

  * **Fill** fits the resolution gate to the film gate’s smaller axis, and crops the rest of the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) image.

  * **Overscan** fits the resolution gate to the film gate’s larger axis and overscans the area outside of the camera image’s boundaries.

[](PhysicalCameras-GateFit.html)

Introduction to Gate Fit

[](CameraOutput.html)

Camera output

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

