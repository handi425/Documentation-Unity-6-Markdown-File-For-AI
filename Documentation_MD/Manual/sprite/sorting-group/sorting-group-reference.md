[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sorting-group/sorting-group-reference.html)
  * [中文](/cn/current/Manual/sprite/sorting-group/sorting-group-reference.html)
  * [日本語](/ja/current/Manual/sprite/sorting-group/sorting-group-reference.html)
  * [한국어](/kr/current/Manual/sprite/sorting-group/sorting-group-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sorting-group/sorting-group-reference.html)
  * [中文](/cn/current/Manual/sprite/sorting-group/sorting-group-reference.html)
  * [日本語](/ja/current/Manual/sprite/sorting-group/sorting-group-reference.html)
  * [한국어](/kr/current/Manual/sprite/sorting-group/sorting-group-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sorting groups](../../sprite/sorting-group/sorting-group-landing.html)
  * Sorting group reference

[](../../sprite/sorting-group/use-sorting-groups.html)

Use sorting groups

[](../../sprite/9-slice/9-slice-landing.html)

Various image sizes without multiple assets

# Sorting group reference

Unity uses a **Sorting Group** ’s [Sorting
Layer](https://docs.unity3d.com/Manual/class-TagManager.html#SortingLayers)
and **Order in Layer** values to determine its priority in the rendering queue
among other Sorting Groups and **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) in the **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene).

Property | Function  
---|---  
**Sorting Layer** | Select or add a [Sorting Layer](https://docs.unity3d.com/Manual/class-TagManager.html#SortingLayers) from this drop-down menu to determine the Sorting Group’s position in the render queue. Unity determines the Sorting Layer order by its place in the Sorting Layer settings; it renders Sorting Layers in the order they appear in the list. See [Tags and Layers](https://docs.unity3d.com/Manual/class-TagManager.html#SortingLayers) for information on setting up Sorting Layers.  
**Order in Layer** | Set the render order of this Sorting Group within its **Sorting Layer**. Unity queues Renderers with lower values first in the render queue, so they appear before Renderers with higher values.  
**Sort At Root** | Enable this option to ignore all parent Sorting Groups if this Sorting Group is nested. This allows this Sorting Group to be sorted against other Renderers and Sorting Groups at the root level.  
  
See [2D Sorting](../../2d-renderer-sorting.html) for more information on using
Sorting Layers to sort **sprites** A 2D graphic objects. If you are used to
working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](../../sprite/sprite-
landing.html)  
See in [Glossary](../../Glossary.html#Sprite), and Unity’s Renderer sorting
criteria.

[](../../sprite/sorting-group/use-sorting-groups.html)

Use sorting groups

[](../../sprite/9-slice/9-slice-landing.html)

Various image sizes without multiple assets

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

