[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sorting-group/set-sorting-group.html)
  * [中文](/cn/current/Manual/sprite/sorting-group/set-sorting-group.html)
  * [日本語](/ja/current/Manual/sprite/sorting-group/set-sorting-group.html)
  * [한국어](/kr/current/Manual/sprite/sorting-group/set-sorting-group.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sorting-group/set-sorting-group.html)
  * [中文](/cn/current/Manual/sprite/sorting-group/set-sorting-group.html)
  * [日本語](/ja/current/Manual/sprite/sorting-group/set-sorting-group.html)
  * [한국어](/kr/current/Manual/sprite/sorting-group/set-sorting-group.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sorting groups](../../sprite/sorting-group/sorting-group-landing.html)
  * Set up a sorting group

[](../../sprite/sorting-group/sorting-group-landing.html)

Sorting groups

[](../../sprite/sorting-group/sort-renderers-within-sorting-group.html)

Sort renderers within a sorting group

# Set up a sorting group

To place a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) into a Sorting Group, add
the Sorting Group component to it:

  1. Select the GameObject and go to **Component > Rendering > Sorting Group**, or select the [Add Component](../../UsingComponents.html) button in the Inspector window of the GameObject.

When you add a Sorting Group component to a GameObject, Unity applies the same
[Sorting Group](sorting-group-reference.html) to all child GameObjects of the
GameObject the component is attached to.

Unity uses the Sorting Group’s settings to determine how to sort its Renderers
among other Renderers and Sorting Groups in the **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene). See [2D
sorting](../../2d-renderer-sorting.html) for more information.

To sort Renderers within a Sorting Group, Unity uses the individual sort
settings of the Renderers in the Sorting Group. See [Sorting Renderers within
a Sorting Group](sort-renderers-within-sorting-group.html) for more
information.

SortingGroup

[](../../sprite/sorting-group/sorting-group-landing.html)

Sorting groups

[](../../sprite/sorting-group/sort-renderers-within-sorting-group.html)

Sort renderers within a sorting group

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

