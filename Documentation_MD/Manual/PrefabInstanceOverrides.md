[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PrefabInstanceOverrides.html)
  * [中文](/cn/current/Manual/PrefabInstanceOverrides.html)
  * [日本語](/ja/current/Manual/PrefabInstanceOverrides.html)
  * [한국어](/kr/current/Manual/PrefabInstanceOverrides.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PrefabInstanceOverrides.html)
  * [中文](/cn/current/Manual/PrefabInstanceOverrides.html)
  * [日本語](/ja/current/Manual/PrefabInstanceOverrides.html)
  * [한국어](/kr/current/Manual/PrefabInstanceOverrides.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Prefabs](Prefabs.html)
  * Instance overrides

[](EditingInPrefabMode.html)

Editing a Prefab in Prefab Mode

[](EditingPrefabViaInstance.html)

Editing a Prefab via its instances

# Instance overrides

**Instance overrides** allow you to create variations between **Prefab** An
asset type that allows you to store a GameObject complete with components and
properties. The prefab acts as a template from which you can create new object
instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) instances, while still linking those
instances to the same Prefab Asset.

When you modify a Prefab Asset, the changes are reflected in all of its
instances. However, you can also make modifications directly to an individual
instance. Doing this creates an **instance override** on that particular
instance.

An example would be if you had a Prefab Asset “Robot”, which you placed in
multiple levels in your game. However, each instance of the “Robot” has a
different speed value, and a different **audio clip** A container for audio
data in Unity. Unity supports mono, stereo and multichannel audio assets (up
to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file
format, and .xm, .mod, .it, and .s3m tracker module formats. [More
info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) assigned.

There are four different types of **instance override** :

  * Overriding the value of a property

  * Adding a component

  * Removing a component

  * Adding a child GameObject

There are some limitations with Prefab instances: you cannot reparent a
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that is part of a Prefab, and you
cannot remove a GameObject that is part of the Prefab. You can, however,
deactivate a GameObject, which is a good substitute for removing a GameObject
(this counts as a property override).

In the **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, instance overrides are
shown with their name label in **bold** , and with a blue line in the left
margin. When you add a new component to a Prefab instance, the blue line in
the margin spans the entire component.

![The inspector windows showing a Prefab instance with overridden Is Trigger
property and a Rigidbody component added as an
override.](../uploads/Main/PrefabsOverridesIndicators1.png) The inspector
windows showing a Prefab instance with overridden “Is Trigger” property and a
Rigidbody component added as an override.

Added and removed components also have plus and minus badges on their icons in
the Inspector, and added GameObjects have a plus badge on their icon in the
Hierarchy.

In the Hierarchy window, Prefab instances with overridden or non-default
values have an override indicator to show that they have been edited, which
Unity displays with a blue line in the left margin with the same appearance as
the lines for instance overrides in the Inspector window. For more
information, see [Hierarchy](Hierarchy.html#OverrideIndicator).

![The Hierarchy window showing a Prefab instance with a child GameObject
called GermOBlaster added as an
override.](../uploads/Main/PrefabsAddedObjectIndicator1.png) The Hierarchy
window showing a Prefab instance with a child GameObject called “GermOBlaster”
added as an override.

## Overrides take precedence

An overridden property value on a Prefab instance always takes precedence over
the value from the Prefab Asset. This means that if you change a property on a
Prefab Asset, it doesn’t have any effect on instances where that property is
overridden.

If you make a change to a Prefab Asset, and it does not update all instances
as expected, you should check whether that property is overridden on the
instance. It is best to only use instance overrides when strictly necessary,
because if you have a large number of instance overrides throughout your
Project, it can be difficult to tell whether your changes to the Prefab Asset
will or won’t have an effect on all of the instances.

## Alignment is specific to Prefab instance

The **alignment** of a Prefab instance is a special case, and is handled
differently to other properties. The **alignment** values are never carried
across from the Prefab Asset to the Prefab instances. This means they can
always differ from the Prefab Asset’s alignment without it being an explicit
instance override. Specifically, the alignment means the **Position** and
**Rotation** properties on the **root Transform** The Transform at the top of
a hierarchy of Transforms. In a Prefab, the Root Transform is the topmost
Transform in the Prefab. In an animated humanoid character, the Root Transform
is a projection on the Y plane of the Body Transform and is computed at run
time. At every frame, a change in the Root Transform is computed, and then
this is applied to the GameObject to make it move. [More
info](RootMotion.html)  
See in [Glossary](Glossary.html#RootTransform) of the Prefab instance, and for
a Rect Transform this also includes the **Width** , **Height** , **Margins** ,
**Anchors** A UI layout tool that fixes a UI element to a parent element.
Anchors are shown as four small triangular handles in the Scene view and
anchor information is also shown in the Inspector. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/UIBasicLayout.html#anchors)  
See in [Glossary](Glossary.html#Anchor) and **Pivot** properties.

This is because it is extremely rare to require multiple instances of a Prefab
to take on the same position and rotation. More commonly, you will want your
prefab instances to be at different positions and rotations, so Unity does not
count these as Prefab overrides.

## Unused Overrides

The data representing the values of your instance overrides can become unused
if the script which declares them is modified or deleted. If this occurs, you
can [remove the unused override data](UnusedOverrides.html).

[](EditingInPrefabMode.html)

Editing a Prefab in Prefab Mode

[](EditingPrefabViaInstance.html)

Editing a Prefab via its instances

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

