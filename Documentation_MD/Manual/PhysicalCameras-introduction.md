[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PhysicalCameras-introduction.html)
  * [中文](/cn/current/Manual/PhysicalCameras-introduction.html)
  * [日本語](/ja/current/Manual/PhysicalCameras-introduction.html)
  * [한국어](/kr/current/Manual/PhysicalCameras-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PhysicalCameras-introduction.html)
  * [中文](/cn/current/Manual/PhysicalCameras-introduction.html)
  * [日本語](/ja/current/Manual/PhysicalCameras-introduction.html)
  * [한국어](/kr/current/Manual/PhysicalCameras-introduction.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Simulating real-world cameras with Physical Cameras](PhysicalCameras.html)
  * Introduction to Physical Cameras

[](PhysicalCameras.html)

Simulating real-world cameras with Physical Cameras

[](PhysicalCameras-LensShift.html)

Widen the view with Lens Shift

# Introduction to Physical Cameras

The Physical **Camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) properties of the Camera component
simulate real-world camera formats on a Unity camera. This is useful for
importing camera information from 3D modeling applications that also mimic
real-world cameras.

Unity provides the same settings as those in most 3D modeling application’s
physical camera settings. The two main properties that control what the camera
sees are **Focal Length** and **Sensor Size**.

  * **Focal Length:** The distance between the sensor and the camera lens. This determines the vertical field of view. When a Unity camera is in Physical Camera mode, changing the Focal Length also changes the field of view accordingly. Smaller focal lengths result in a larger field of view, and vice versa.

![The relationship between a cameras focal length, field of view, and sensor
size](../uploads/Main/PhysCamAttributes.png) The relationship between a
camera’s focal length, field of view, and sensor size

  * **Sensor Size:** The width and height of the sensor that captures the image. These determine the physical camera’s **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio). You can choose from several
preset sensor sizes that correspond to real-world camera formats, or set a
custom size. When the sensor aspect ratio is different to the rendered aspect
ratio, as set in the Game view, you can control how Unity fits the camera
image to the rendered image (see information on [Gate Fit](PhysicalCameras-
GateFit.html)).

## Additional resources

  * [Camera Inspector windows reference for URP](urp/camera-components-reference-landing.html)
  * [Camera Inspector window reference for the Built-In Render Pipeline](class-Camera.html)

[](PhysicalCameras.html)

Simulating real-world cameras with Physical Cameras

[](PhysicalCameras-LensShift.html)

Widen the view with Lens Shift

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

