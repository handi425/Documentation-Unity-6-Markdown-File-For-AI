[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2d-pixelperfect-intro.html)
  * [中文](/cn/current/Manual/urp/2d-pixelperfect-intro.html)
  * [日本語](/ja/current/Manual/urp/2d-pixelperfect-intro.html)
  * [한국어](/kr/current/Manual/urp/2d-pixelperfect-intro.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2d-pixelperfect-intro.html)
  * [中文](/cn/current/Manual/urp/2d-pixelperfect-intro.html)
  * [日本語](/ja/current/Manual/urp/2d-pixelperfect-intro.html)
  * [한국어](/kr/current/Manual/urp/2d-pixelperfect-intro.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [Precise pixel scaling and rotation via the Pixel Perfect Camera in URP](../urp/2d-pixelperfect.html)
  * Introduction to the Pixel Perfect Camera in URP

[](../urp/2d-pixelperfect.html)

Precise pixel scaling and rotation via the Pixel Perfect Camera in URP

[](../urp/2d-pixelperfect-prep-sprites.html)

Prepare your sprites for the 2D Pixel Perfect Camera in URP

# Introduction to the Pixel Perfect Camera in URP

Understand how to use the **Pixel** The smallest unit in a computer image.
Pixel size depends on your screen resolution. Pixel lighting is calculated at
every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) Perfect **Camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) to keep your pixel art crisp and
clear at different resolutions, and stable in motion.

The **2D Pixel Perfect** package contains the **Pixel Perfect Camera**
component. The component calculates what Unity needs to scale the **viewport**
The user’s visible area of an app on their screen.  
See in [Glossary](../Glossary.html#Viewport) with resolution changes to
maintain the pixel perfect visual style, so that you don’t need to calculate
manually. You can use the component settings to adjust the definition of the
rendered pixel art within the camera viewport, and preview any changes made in
the Game view.

![Pixel Perfect Camera Gizmo](../../uploads/urp/2D/2D_Pix_image_0.png) Pixel
Perfect Camera Gizmo

To begin using the component, attach the **Pixel Perfect Camera** component to
the main Camera **GameObject** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) in the **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene). The component is represented by two
green bounding boxes centered on the **Camera** **Gizmo** A graphic overlay
associated with a GameObject in a Scene, and displayed in the Scene View.
Built-in scene tools such as the move tool are Gizmos, and you can create
custom Gizmos using textures or scripting. Some Gizmos are only drawn when the
GameObject is selected, while other Gizmos are drawn by the Editor regardless
of which GameObjects are selected. [More info](../GizmosMenu.html#GizmosIcons)  
See in [Glossary](../Glossary.html#Gizmo) in the **Scene view** An interactive
view into the world you are creating. You use the Scene View to select and
position scenery, characters, cameras, lights, and all other types of Game
Object. [More info](../UsingTheSceneView.html)  
See in [Glossary](../Glossary.html#SceneView). The solid green bounding box
shows the visible area in Game view, while the dotted bounding box shows the
[Reference Resolution](2d-pixelperfect-ref.html#reference-resolution).

[](../urp/2d-pixelperfect.html)

Precise pixel scaling and rotation via the Pixel Perfect Camera in URP

[](../urp/2d-pixelperfect-prep-sprites.html)

Prepare your sprites for the 2D Pixel Perfect Camera in URP

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

