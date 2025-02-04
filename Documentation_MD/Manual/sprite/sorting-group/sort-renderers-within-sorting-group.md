[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sorting-group/sort-renderers-within-sorting-group.html)
  * [中文](/cn/current/Manual/sprite/sorting-group/sort-renderers-within-sorting-group.html)
  * [日本語](/ja/current/Manual/sprite/sorting-group/sort-renderers-within-sorting-group.html)
  * [한국어](/kr/current/Manual/sprite/sorting-group/sort-renderers-within-sorting-group.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sorting-group/sort-renderers-within-sorting-group.html)
  * [中文](/cn/current/Manual/sprite/sorting-group/sort-renderers-within-sorting-group.html)
  * [日本語](/ja/current/Manual/sprite/sorting-group/sort-renderers-within-sorting-group.html)
  * [한국어](/kr/current/Manual/sprite/sorting-group/sort-renderers-within-sorting-group.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sorting groups](../../sprite/sorting-group/sorting-group-landing.html)
  * Sort renderers within a sorting group

[](../../sprite/sorting-group/set-sorting-group.html)

Set up a sorting group

[](../../sprite/sorting-group/use-sorting-groups.html)

Use sorting groups

# Sort renderers within a sorting group

Unity sorts all Renderers within the same Sorting Group by their individual
**Sorting Layer** and **Order in Layer** [Renderer
properties](../renderer/renderer-landing.html). Unity does not consider each
Renderer’s individual **Distance to**Camera** A component which creates an
image of a particular viewpoint in your scene. The output is either drawn to
the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera)** property during this sorting
process. Instead, it sets a Distance to Camera value for the whole Sorting
Group (including all its child Renderers), based on the position of the root
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) that contains the Sorting
Group component.

The Sorting Group’s internal sort order remains constant when Unity sorts the
Sorting Group among other Renderers and Sorting Groups in the **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene).

The following diagram shows the sorting process.

![Internal Sorting Group sorting
process.](../../../uploads/Main/SG_diagram1.png) Internal Sorting Group
sorting process.

Unity treats all Renderers that belong to the same Sorting Group as a single
layer, and sorts non-grouped Renderers based on their **Sorting Layer** and
**Order in Layer** property settings.

### Particle System

The Editor treats a [Particle System](../../class-ParticleSystem.html)A
component that simulates fluid entities such as liquids, clouds and flames by
generating and animating large numbers of small 2D images in the scene. [More
info](../../class-ParticleSystem.html)  
See in [Glossary](../../Glossary.html#particlesystem) that is a child of a
Sorting Group as another Renderer within that Sorting Group, and sorts it
internally among other Renderers based on its **Sorting Layer** and **Order in
Layer** property settings.

When Unity sorts the Particle System with the other Renderers within the
Sorting Group, it ignores the Particle System’s **Sorting Fudge** value.

### Nested Sorting Groups

A nested Sorting Group is a Sorting Group that has a parent Sorting Group.
Unity sorts Renderers within a nested Sorting Group first, before their parent
(refer to [Sorting Renderers within a Sorting Group](sort-renderers-within-
sorting-group.html)).

After Unity determines the internal sort order of the nested Sorting Group, it
sorts the nested Sorting Group with other Renderers or Sorting Groups within
the parent Sorting Group. A nested Sorting Group can have a nested Sorting
Group as a child. Unity sorts the innermost child Groups first, before their
respective parents.

The following diagram gives you an example of the nested Sorting Group sorting
process.

![Nested Sorting Group sorting
process.](../../../uploads/Main/SG_diagram2.png) Nested Sorting Group sorting
process.

### Sort At Root

In certain situations, you may have a nested Sorting Group that is ordered
based on the Scene [Hierarchy](../../Hierarchy.html). However, you may want
this nested Sorting Group to be rendered separately from its parent Sorting
Group without changing its position in the Scene Hierarchy.

You can enable this option to allow this Sorting Group to ignore its parent
Sorting Groups, which allows this Sorting Group to be sorted against other
Renderers and Sorting Groups globally without requiring the GameObject to be
reparented to another Transform. All child Renderers and Sorting Groups (which
have not ignored their parents) will be sorted under this Sorting Group.

![](../../../uploads/Main/SG_diagram3.png)

SortingGroup

[](../../sprite/sorting-group/set-sorting-group.html)

Set up a sorting group

[](../../sprite/sorting-group/use-sorting-groups.html)

Use sorting groups

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

