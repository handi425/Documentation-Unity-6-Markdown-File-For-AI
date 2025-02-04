[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnpackingPrefabInstances.html)
  * [中文](/cn/current/Manual/UnpackingPrefabInstances.html)
  * [日本語](/ja/current/Manual/UnpackingPrefabInstances.html)
  * [한국어](/kr/current/Manual/UnpackingPrefabInstances.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnpackingPrefabInstances.html)
  * [中文](/cn/current/Manual/UnpackingPrefabInstances.html)
  * [日本語](/ja/current/Manual/UnpackingPrefabInstances.html)
  * [한국어](/kr/current/Manual/UnpackingPrefabInstances.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Prefabs](Prefabs.html)
  * Unpacking Prefab instances

[](UnusedOverrides.html)

Unused Overrides

[](Constraints.html)

Constraints

# Unpacking Prefab instances

To return the contents of a **Prefab** An asset type that allows you to store
a GameObject complete with components and properties. The prefab acts as a
template from which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) instance into a regular **GameObject**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), you unpack the Prefab instance.
This is exactly the reverse operation of creating (packing) a Prefab, except
that it doesn’t destroy the Prefab Asset but only affects the Prefab instance.

You can unpack a Prefab instance by right-clicking on it in the Hierarchy and
selecting **Unpack Prefab**. The resulting GameObject in the **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) no longer has any link to its former
Prefab Asset. The Prefab Asset itself is not affected by this operation and
there may still be other instances of it in your Project.

If you had any overrides on your Prefab instance before you unpacked it, those
will be “baked” onto the resulting GameObjects. That is, the values will stay
the same, but will no longer have status as overrides, since there’s no Prefab
to override.

If you unpack a Prefab that has nested Prefabs inside, the nested Prefabs
remain Prefab instances and still have links to their respective Prefab
Assets. Similarly, if you unpack a Prefab Variant, there will be a new Prefab
instance at the root which is an instance of the base Prefab.

In general, unpacking a Prefab instance will give you the same objects you see
if you go into Prefab Mode for that Prefab. This is because Prefab Mode shows
the contents that is inside of a Prefab, and unpacking a Prefab instance
unpacks the contents of a Prefab.

If you have a Prefab instance that you want to replace with plain GameObjects
and completely remove all links to any Prefab Assets, you can right-click on
it in the Hierarchy and select **Unpack Prefab Completely**. This is
equivalent to unpacking the Prefab, and keeping on unpacking any Prefab
instances that appear as a result because they were nested Prefabs or base
Prefabs.

You can unpack Prefab instances that exist in Scenes, or which exist inside
other Prefabs.

* * *

  * 2018–07–31 Page published 

  * Nested Prefabs and Prefab Variants added in 2018.3

[](UnusedOverrides.html)

Unused Overrides

[](Constraints.html)

Constraints

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

