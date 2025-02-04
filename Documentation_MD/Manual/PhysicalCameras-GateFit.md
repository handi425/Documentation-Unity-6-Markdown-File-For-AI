[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PhysicalCameras-GateFit.html)
  * [中文](/cn/current/Manual/PhysicalCameras-GateFit.html)
  * [日本語](/ja/current/Manual/PhysicalCameras-GateFit.html)
  * [한국어](/kr/current/Manual/PhysicalCameras-GateFit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PhysicalCameras-GateFit.html)
  * [中文](/cn/current/Manual/PhysicalCameras-GateFit.html)
  * [日本語](/ja/current/Manual/PhysicalCameras-GateFit.html)
  * [한국어](/kr/current/Manual/PhysicalCameras-GateFit.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Simulating real-world cameras with Physical Cameras](PhysicalCameras.html)
  * [Crop or stretch the view with Gate Fit](PhysicalCameras-GateFit-Landing.html)
  * Introduction to Gate Fit

[](PhysicalCameras-GateFit-Landing.html)

Crop or stretch the view with Gate Fit

[](PhysicalCameras-GateFit-Configure.html)

Configure Gate Fit

# Introduction to Gate Fit

The **Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) component’s **Gate Fit** property
determines what happens when the Game view and the physical camera sensor have
different **aspect ratios** The relationship of an image’s proportional
dimensions, such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio).

In **Physical Camera** mode, a camera has two “gates.”

  * The area rendered in the Game view, according to the resolution you set in the **Aspect** drop-down menu, is called the “resolution gate”.

  * The area that the camera actually sees, as defined by the **Sensor Size** properties, is called the “film gate”.

![An example of resolution gate vs. film gate when the two gates have
different aspect ratios](../uploads/Main/GateFitGates.png) An example of
resolution gate vs. film gate when the two gates have different aspect ratios

When the two gates have different aspect ratios, Unity “fits” the resolution
gate to the film gate. There are several fit modes, but they all yield one of
three results.

  * **Cropping:** When the film gate exceeds the resolution gate after fitting, the Game view renders as much of the camera image as fits within its aspect ratio, and cuts off the rest.
  * **Overscanning:** When the film gate exceeds the resolution gate after fitting, the Game view still performs rendering calculations for parts of the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that fall outside the camera’s field of
view.

  * **Stretching:** The Game view renders the full camera image, stretched either horizontally or vertically to fit its aspect ratio.

To view the gates in the **Scene view** An interactive view into the world you
are creating. You use the Scene View to select and position scenery,
characters, cameras, lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView), and see how they fit together,
select the camera and look at its view frustum. The resolution gate is the
camera’s far **clipping plane** A plane that limits how far or close a camera
can see from its current position. A camera’s viewable range is between the
far and near clipping planes. See far clipping plane and near clipping plane.
[More info](class-Camera.html)  
See in [Glossary](Glossary.html#clippingplane). The film gate is the second
rectangle at the base of the frustum.

![In the example above, the outer rectangle \(A\) at the base of the camera’s
view frustum is the resolution gate. The inner rectangle \(B\) is the film
gate](../uploads/Main/GateFitUI.png) In the example above, the outer rectangle
(A) at the base of the camera’s view frustum is the resolution gate. The inner
rectangle (B) is the film gate

[](PhysicalCameras-GateFit-Landing.html)

Crop or stretch the view with Gate Fit

[](PhysicalCameras-GateFit-Configure.html)

Configure Gate Fit

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

