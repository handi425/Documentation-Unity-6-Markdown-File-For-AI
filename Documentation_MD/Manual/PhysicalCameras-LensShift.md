[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PhysicalCameras-LensShift.html)
  * [中文](/cn/current/Manual/PhysicalCameras-LensShift.html)
  * [日本語](/ja/current/Manual/PhysicalCameras-LensShift.html)
  * [한국어](/kr/current/Manual/PhysicalCameras-LensShift.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PhysicalCameras-LensShift.html)
  * [中文](/cn/current/Manual/PhysicalCameras-LensShift.html)
  * [日本語](/ja/current/Manual/PhysicalCameras-LensShift.html)
  * [한국어](/kr/current/Manual/PhysicalCameras-LensShift.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Simulating real-world cameras with Physical Cameras](PhysicalCameras.html)
  * Widen the view with Lens Shift

[](PhysicalCameras-introduction.html)

Introduction to Physical Cameras

[](PhysicalCameras-GateFit-Landing.html)

Crop or stretch the view with Gate Fit

# Widen the view with Lens Shift

**Lens Shift** offsets the **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)’s lens from its sensor horizontally
and vertically. This allows you to change the focal center, and reposition a
subject in the rendered frame, with little or no distortion.

This technique is common in architectural photography. For example, if you
want to capture a tall building, you could rotate the camera. But that
distorts the image, making parallel lines appear to converge.

![Rotating the camera up to capture the top of the building causes vertical
lines to converge](../uploads/Main/LensShift_VRot.png) Rotating the camera up
to capture the top of the building causes vertical lines to converge

If you shift the lens up instead of rotating the camera, you can change the
composition of the image to include the top of the building, but parallel
lines stay straight.

![Shifting the lens along the Y axis moves the focal center, but keeps
vertical lines straight](../uploads/Main/LensShift_VShift.png) Shifting the
lens along the Y axis moves the focal center, but keeps vertical lines
straight

Similarly, you can use a horizontal lens shift to capture wide objects without
the distortion you might get by rotating the camera.

![](../uploads/Main/LensShift_HRot.png) ![Rotating the camera \(top\) to frame
the building causes horizontal lines to converge. Shifting the lens
horizontally instead \(bottom\) reframes the image, but keeps the horizontal
lines straight.](../uploads/Main/LensShift_HShift.png) Rotating the camera
(top) to frame the building causes horizontal lines to converge. Shifting the
lens horizontally instead (bottom) reframes the image, but keeps the
horizontal lines straight.

### Lens shifts and frustum obliqueness

One side effect of a lens shift is that it makes the camera’s [view
frustum](UnderstandingFrustum.html) oblique. That means the angle between the
camera’s center line and its frustum is smaller on one side than on the other.

![The images above show the camera frustuim before \(left\) and after
\(right\) a Y-axis lens shift. Shifting the lens up makes the frustum
oblique.](../uploads/Main/ObliqueFrustum_LensShift.png) The images above show
the camera frustuim before (left) and after (right) a Y-axis lens shift.
Shifting the lens up makes the frustum oblique.

You can use this to create visual effects based on perspective. For example,
in a racing game, you might want to keep the perspective low to the ground. A
lens shift is a way of achieving an oblique frustum without scripting.

For further information, see documentation on [Using an Oblique
Frustum](ObliqueFrustum.html).

[](PhysicalCameras-introduction.html)

Introduction to Physical Cameras

[](PhysicalCameras-GateFit-Landing.html)

Crop or stretch the view with Gate Fit

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

