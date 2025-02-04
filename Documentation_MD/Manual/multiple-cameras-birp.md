[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/multiple-cameras-birp.html)
  * [中文](/cn/current/Manual/multiple-cameras-birp.html)
  * [日本語](/ja/current/Manual/multiple-cameras-birp.html)
  * [한국어](/kr/current/Manual/multiple-cameras-birp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/multiple-cameras-birp.html)
  * [中文](/cn/current/Manual/multiple-cameras-birp.html)
  * [日本語](/ja/current/Manual/multiple-cameras-birp.html)
  * [한국어](/kr/current/Manual/multiple-cameras-birp.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Using multiple cameras](MultipleCameras-landing.html)
  * Set the order of multiple cameras

[](MultipleCameras.html)

Configure multiple cameras

[](multidisplay.html)

Display camera views on multiple monitors

# Set the order of multiple cameras

You can create multiple Cameras and assign each one to a different depth. Use
the following properties in the **Camera** A component which creates an image
of a particular viewpoint in your scene. The output is either drawn to the
screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window:

  * **Depth** if your project uses the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline).

  * **Priority** if your project uses the Universal Render Pipeline (URP).

Cameras are drawn from low depth to high depth. In other words, a Camera with
a depth of 2 will be drawn on top of a Camera with a depth of 1. You can
adjust the values of the **View Rect** property to resize and position the
Camera’s view onscreen. This can create multiple mini-views like missile cams,
map views, rear-view mirrors, etc.

[](MultipleCameras.html)

Configure multiple cameras

[](multidisplay.html)

Display camera views on multiple monitors

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

