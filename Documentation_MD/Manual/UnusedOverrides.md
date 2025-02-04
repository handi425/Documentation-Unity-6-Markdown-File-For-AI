[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnusedOverrides.html)
  * [中文](/cn/current/Manual/UnusedOverrides.html)
  * [日本語](/ja/current/Manual/UnusedOverrides.html)
  * [한국어](/kr/current/Manual/UnusedOverrides.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnusedOverrides.html)
  * [中文](/cn/current/Manual/UnusedOverrides.html)
  * [日本語](/ja/current/Manual/UnusedOverrides.html)
  * [한국어](/kr/current/Manual/UnusedOverrides.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Prefabs](Prefabs.html)
  * Unused Overrides

[](PrefabOverridesMultiLevel.html)

Overrides at multiple levels

[](UnpackingPrefabInstances.html)

Unpacking Prefab instances

# Unused Overrides

Instance override values are stored as data in the **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) or **prefab** An asset type that allows
you to store a GameObject complete with components and properties. The prefab
acts as a template from which you can create new object instances in the
scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) in which they are defined. However, an
override becomes “unused” if its target object is either invalid or its
[**Property Path**](../ScriptReference/PropertyModification-propertyPath.html)
is unknown. In this case, the data becomes unused. It is still stored in the
scene file, but is redundant.

For example, if you override the values of a [public field](inspecting-
scripts.html) on a [script](creating-scripts.html) attached to a prefab, and
then delete the script, the data that contains the override values becomes
unused because it targets an object that no longer exists.

Override data also becomes unused if you delete the public field definition,
or rename it, because the [**Property
Path**](https://docs.unity3d.com/ScriptReference/PropertyModification-
propertyPath.html) no longer matches the stored data, although the component
object itself still exists.

Because Unity does not automatically delete unused override data, if you
restore the deleted script, or field definition, the override data becomes
used again and is applied as an override as before.

If you do not want to keep unused override data, you can check for and remove
them using the [**Overrides**](PrefabInstanceOverrides.html) menu in the
**inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), or from the context menu in the
**Hierarchy** window. The removal includes all unused overrides, and Unity
writes details of what was removed to the [Editor
log](https://docs.unity3d.com/Manual/log-files.html).

The Unity Editor can’t automatically determine when or whether your unused
data should be cleaned up, because you may have temporarily or accidentally
moved the object or property the data refers to, and you might reinstate it
later. Removing unused override data that you know you no longer need can be
thought of as good practice, because it means your scene file only contains
useful data, which can help make **version control** A system for managing
file changes. You can use Unity in conjunction with most common version
control tools, including Perforce, Git, Mercurial and PlasticSCM. [More
info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) and collaboration simpler.

**Note** : You can rename public fields and preserve the associated overridden
values by using
[**FormerlySerializedAsAttribute**](../ScriptReference/Serialization.FormerlySerializedAsAttribute.html),
which performs name conversion to map the field’s old name to its new name.

## The prefab overrides dropdown

To check for and remove unused overrides using the Inspector:

  1. Select the GameObject(s) that you want to work on.
  2. In the inspector, click the **Overrides** drop-down menu **[A]**. If there are any unused overrides present, the menu will show an “Unused overrides” option **[B]** , otherwise the “Unused overrides” option is not displayed.
  3. Click **Unused Overrides** to open the unused overrides panel.
  4. The unused overrides panel **[C]** lists the unused overrides, and has a **Remove** button.
  5. Click the **Remove** button to remove the unused overrides.

![The unused overrides panel, showing two unused overrides on the selected
prefab.](../uploads/Main/UnusedOverridesInspector.png) The unused overrides
panel, showing two unused overrides on the selected prefab.

**Note:** The unused overrides panel supports multiple selection, and shows
the total number of unused overrides, and the number of instances affected,
however it only shows the field name, **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) name, and value, of up to three of
the unused overrides, as shown in the example below:

![The unused overrides panel, showing 24 unused overrides on 3 separate prefab
instances.](../uploads/Main/UnusedOverridesPanelMultiSelect.png) The unused
overrides panel, showing 24 unused overrides on 3 separate prefab instances.

## The Hierarchy context menu

To check for and remove unused instance overrides from the Hierarchy window:

  1. Select the GameObject(s) that you want to work on.
  2. In the Hierarchy window, right-click on one of the selected objects, and select: **Prefab > Remove Unused Overrides**
  3. Unity displays a dialog box showing the number of unused overrides, if any.
  4. Click the **Remove** button to remove the unused overrides.

![The dialog box shown when removing unused overrides from the Hierarchy
window context menu.](../uploads/Main/UnusedOverridesDialogBox.png) The dialog
box shown when removing unused overrides from the Hierarchy window context
menu.

**Note** : You can remove all unused overrides in an entire scene by right-
clicking the scene’s name in the hierarchy instead of individual GameObjects.

[](PrefabOverridesMultiLevel.html)

Overrides at multiple levels

[](UnpackingPrefabInstances.html)

Unpacking Prefab instances

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

