[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-platform-and-mesh.html)
  * [中文](/cn/current/Manual/UIE-platform-and-mesh.html)
  * [日本語](/ja/current/Manual/UIE-platform-and-mesh.html)
  * [한국어](/kr/current/Manual/UIE-platform-and-mesh.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-platform-and-mesh.html)
  * [中文](/cn/current/Manual/UIE-platform-and-mesh.html)
  * [日本語](/ja/current/Manual/UIE-platform-and-mesh.html)
  * [한국어](/kr/current/Manual/UIE-platform-and-mesh.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Support for runtime UI](UIE-support-for-runtime-ui.html)
  * [Performance consideration for runtime UI](UIE-performance-consideration-runtime.html)
  * Platform and mesh considerations

[](UIE-control-textures-of-the-dynamic-atlas.html)

Control textures of the dynamic atlas

[](UIE-work-with-text.html)

Work with text

# Platform and mesh considerations

Things to consider when building **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) for different platforms and **mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) tessellation.

## Consider device capabilities

Some Android devices and the Web platform can’t partially patch index buffers.
If your audience uses such devices or if you target the Web platform, UI
Toolkit rendering is still functional but performance may be degraded. To
avoid performance degradation, don’t animate too many elements at the same
time and [profile on device](profiler-profiling-applications.html).

## Avoid mesh tessellation

It’s computationally expensive to build mesh tessellation for **visual
elements** A node of a visual tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement). Any time the size
(width/height) of the element changes, its geometry re-builds, which can be an
issue with animations or frequent resizing.

Generally speaking, [transforms](UIE-Transform.html) and texture aren’t good
choices in terms of flexibility and re-use. However, when you animate, to get
better performance, do the following:

  * Use [transforms](UIE-Transform.html) instead of width or other layout properties
  * Use textures or 2D **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) instead of rounded corners and borders

## Additional resources

  * [`Transform`](../ScriptReference/Transform.html)
  * [Profiler](profiler-profiling-applications.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler)

[](UIE-control-textures-of-the-dynamic-atlas.html)

Control textures of the dynamic atlas

[](UIE-work-with-text.html)

Work with text

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

