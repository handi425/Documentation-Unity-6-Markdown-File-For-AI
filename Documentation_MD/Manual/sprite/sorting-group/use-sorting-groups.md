[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sorting-group/use-sorting-groups.html)
  * [中文](/cn/current/Manual/sprite/sorting-group/use-sorting-groups.html)
  * [日本語](/ja/current/Manual/sprite/sorting-group/use-sorting-groups.html)
  * [한국어](/kr/current/Manual/sprite/sorting-group/use-sorting-groups.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sorting-group/use-sorting-groups.html)
  * [中文](/cn/current/Manual/sprite/sorting-group/use-sorting-groups.html)
  * [日本語](/ja/current/Manual/sprite/sorting-group/use-sorting-groups.html)
  * [한국어](/kr/current/Manual/sprite/sorting-group/use-sorting-groups.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sorting groups](../../sprite/sorting-group/sorting-group-landing.html)
  * Use sorting groups

[](../../sprite/sorting-group/sort-renderers-within-sorting-group.html)

Sort renderers within a sorting group

[](../../sprite/sorting-group/sorting-group-reference.html)

Sorting group reference

# Use sorting groups

The most common way to create a 2D multi-Sprite character is to arrange and
parent multiple **Sprite** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) Renderers together in the
Hierarchy window to form a character. You can use **Sorting Groups** to help
manage this kind of complex multi-Sprite character.

In the example below, the **Sprite Renderers** A component that lets you
display images as Sprites for use in both 2D and 3D scenes. [More
info](../../sprite/renderer/renderer-landing.html)  
See in [Glossary](../../Glossary.html#SpriteRenderer) belong to the same
**Sorting Layer** , but with different **Order in Layer** values. Unity sorts
the different parts of a character in the order that you want them to appear.

![A character Prefab with its parts in a
hierarchy.](../../../uploads/Main/character_hierarchy.png) A character Prefab
with its parts in a hierarchy.

After you’ve configured the Sorting Groups and Sorting Layers, you can save
your character as a [Prefab](../../Prefabs.html)An asset type that allows you
to store a GameObject complete with components and properties. The prefab acts
as a template from which you can create new object instances in the scene.
[More info](../../Prefabs.html)  
See in [Glossary](../../Glossary.html#Prefab), and clone it as many times as
you need to.

However, Prefab sprites all have the same **Sorting Layer** and **Order in
Layer** values and render to the same layers as other Prefabs, which can cause
different parts of a Prefab character to intersect and layer incorrectly.

![sprites from two Prefabs intersect incorrectly, because Unity is rendering
the sprites on the same layers.](../../../uploads/Main/part_intersect.png)
sprites from two Prefabs intersect incorrectly, because Unity is rendering the
sprites on the same layers.

To make sure Prefabs keep their own render order consistent so they appear
correctly, add the Sorting Group component to the root **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) of each Prefab. Save the
edited Prefab, so that all current and future instances of the Prefab also
have the Sorting Group component.

Each Prefab should have a Sorting Group component with the same **Sorting
Layer** and **Order in Layer** property settings. This might cause Renderers
in the Prefabs that are on the same **Sorting Layer** to render in
inconsistent ways, because they have the same priority in the [Render
Queue](../../SL-SubShaderTags.html).

To prevent this issue, give each Prefab’s Sorting Group component a unique
**Order in Layer** value. Unity renders Sorting Groups with lower **Order in
Layer** values first and those with higher values overlap the Sorting Groups
that are lower. Refer to [Tags and Layers](../../class-TagManager.html) for
more information about editing and reordering **Sorting Layers**.

![](../../../uploads/Main/unique_orderlayer.png)

Each Prefab has a Sorting Group component with a unique **Order in Layer**
value to ensure that Unity renders each character and their parts correctly.

SortingGroup

[](../../sprite/sorting-group/sort-renderers-within-sorting-group.html)

Sort renderers within a sorting group

[](../../sprite/sorting-group/sorting-group-reference.html)

Sorting group reference

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

