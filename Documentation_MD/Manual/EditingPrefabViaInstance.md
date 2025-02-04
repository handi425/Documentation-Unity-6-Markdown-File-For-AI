[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/EditingPrefabViaInstance.html)
  * [中文](/cn/current/Manual/EditingPrefabViaInstance.html)
  * [日本語](/ja/current/Manual/EditingPrefabViaInstance.html)
  * [한국어](/kr/current/Manual/EditingPrefabViaInstance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/EditingPrefabViaInstance.html)
  * [中文](/cn/current/Manual/EditingPrefabViaInstance.html)
  * [日本語](/ja/current/Manual/EditingPrefabViaInstance.html)
  * [한국어](/kr/current/Manual/EditingPrefabViaInstance.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Prefabs](Prefabs.html)
  * Editing a Prefab via its instances

[](PrefabInstanceOverrides.html)

Instance overrides

[](NestedPrefabs.html)

Nested Prefabs

# Editing a Prefab via its instances

The **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) for the root of a **Prefab** An
asset type that allows you to store a GameObject complete with components and
properties. The prefab acts as a template from which you can create new object
instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) instance has three more controls than
a normal **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject): **Open** , **Select** and
**Overrides**.

![The three Prefab controls in the Inspector window for a Prefab
instance](../uploads/Main/PrefabsInspectorControls1.png) The three Prefab
controls in the Inspector window for a Prefab instance

The **Open** button opens the Prefab Asset that the instance is from in Prefab
Mode, allowing you to edit the Prefab Asset and thereby change all of its
instances. The **Select** button selects the Prefab Asset that this instance
is from in the **Project window** A window that shows the contents of your
`Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow). The **Overrides** button opens
the overrides drop-down window.

## Overrides dropdown

The **Overrides** drop-down window shows all the overrides on the Prefab
instance. It also lets you apply overrides from the instance to the Prefab
Asset, or revert overrides on the instance back to the values on the Prefab
Asset. The **Overrides** drop-down button only appears for the root Prefab
instance, not for Prefabs that are inside other Prefabs.

The **Overrides** drop-down window allows you to apply or revert prefab
overrides individually, or apply or revert all the prefab overrides in one go.

  * **Applying** an override modifies the Prefab Asset. This puts the override (which is currently only on your Prefab instance) onto the Asset. This means the Prefab Asset now has that modification, and the Prefab instance no longer has that modification as an override.

  * **Reverting** an override modifies the Prefab instance. This essentially discards your override and reverts it back to the state of the Prefab Asset.

The drop-down window shows a list of changes on the instance in the form of
modified, added and removed components, and added GameObjects (including other
Prefabs).

![The Overrides dropdown in the Inspector window when viewing a Prefab
instance](../uploads/Main/PrefabsOverridesDropdown1.png) The Overrides
dropdown in the Inspector window when viewing a Prefab instance

To inspect an entry, click it. This displays a floating view that shows the
change and allows you to revert or apply that change.

![The overrides dropdown window with an added component override
selected](../uploads/Main/PrefabsOverridesDropdownAddedComponent1.png) The
overrides dropdown window with an added component override selected

For components with modified values, the view displays a side-by-side
comparison of the component’s values on the Prefab Asset and the modified
component on the Prefab instance. This allows you to compare the original
Prefab Asset values with the current overrides, so that you can decide whether
you would like to revert or apply those values.

In the example below, the “GermOBlaster” child GameObject exists on both the
Prefab Asset and the Prefab instance, however its scale has been increased on
the instance. This increase in scale is an instance override, and can be seen
as a side-by-side comparison in the **Overrides** drop-down window.

![The Overrides dropdown with comparison view, showing modified values in the
Transform component of a child GameObject of the prefab
instance](../uploads/Main/PrefabsOverridesDropdownCompareComponent1.png) The
Overrides dropdown with comparison view, showing modified values in the
Transform component of a child GameObject of the prefab instance

The **Overrides** drop-down window also has **Revert All** and **Apply All**
buttons for reverting or applying all changes at once. If you have Prefabs
inside other Prefabs, the **Apply All** button always applies to the outermost
Prefab, which is the one that has the **Overrides** drop-down button on its
root GameObject.

If you select multiple entries at once, the Revert All and Apply All buttons
are replaced by **Revert Selected** and **Apply Selected** buttons. You can
use these to revert or apply multiple overrides at once. Similar to the
**Apply All** button, the **Apply Selected** button always applies to the
outermost Prefab.

If there are [unused overrides](UnusedOverrides.html) on any selected objects,
the Overrides drop down displays an option that allows you to remove them.

## Context menus

You can also **revert** and **apply** individual overrides using the context
menu in the Inspector, instead of using the Overrides drop-down window.

Overridden properties are shown in bold. They can be reverted or applied via a
context menu:

![Context menu for a single
property](../uploads/Main/PrefabsContextSingleProperty1.png) Context menu for
a single property

Modified components can be reverted or applied via the cog drop-down button or
context menu of the component header:

![Context menu for modified
component](../uploads/Main/PrefabsContextModifiedComponent1.png) Context menu
for modified component

Added components have a plus badge that overlays the icon. They can be
reverted or applied via the cog drop-down button or context menu of the
component header:

![Context menu for added
component](../uploads/Main/PrefabsContextAddedComponent1.png) Context menu for
added component

Removed components have a minus badge that overlays the icon. The removal can
be reverted or applied via the cog drop-down button or context menu of the
component header. Reverting the removal puts the component back, and applying
the removal deletes it from the Prefab Asset as well:

![Context menu for removed
component](../uploads/Main/PrefabsContextRemovedComponent1.png) Context menu
for removed component

GameObjects (including other Prefabs) that are added as children to a Prefab
instance have a plus badge that overlays the icon in the Hierarchy. They can
be reverted or applied via the context menu on the object in the Hierarchy:

![Context menu for added GameObject
child](../uploads/Main/PrefabsContextAddedGameObject1.png) Context menu for
added GameObject child

* * *

  * 2018–07–31 Page published 

  * Nested Prefabs and Prefab Variants added in 2018.3

[](PrefabInstanceOverrides.html)

Instance overrides

[](NestedPrefabs.html)

Nested Prefabs

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

