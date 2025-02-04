[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Prefabs.html)
  * [中文](/cn/current/Manual/Prefabs.html)
  * [日本語](/ja/current/Manual/Prefabs.html)
  * [한국어](/kr/current/Manual/Prefabs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Prefabs.html)
  * [中文](/cn/current/Manual/Prefabs.html)
  * [日本語](/ja/current/Manual/Prefabs.html)
  * [한국어](/kr/current/Manual/Prefabs.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * Prefabs

[](troubleshooting-skinned-mesh-renderer-visibility.html)

Troubleshooting Skinned Mesh Renderer visibility

[](CreatingPrefabs.html)

Creating Prefabs

# Prefabs

![](../uploads/Main/PrefabsIntroScene.png)

Unity’s ****Prefab**** system allows you to create, configure, and store a
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) complete with all its components,
property values, and child GameObjects as a reusable Asset. The Prefab Asset
acts as a template from which you can create new Prefab instances in the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

When you want to reuse a GameObject configured in a particular way – like a
non-player character (NPC), prop or piece of scenery – in multiple places in
your Scene, or across multiple Scenes in your Project, you should convert it
to a Prefab. This is better than simply copying and pasting the GameObject,
because the Prefab system allows you to automatically keep all the copies in
sync.

Any edits that you make to a Prefab Asset are automatically reflected in the
instances of that Prefab, allowing you to easily make broad changes across
your whole Project without having to repeatedly make the same edit to every
copy of the Asset.

You can [nest Prefabs](NestedPrefabs.html) inside other Prefabs to create
complex hierarchies of objects that are easy to edit at multiple levels.

However, this does not mean all Prefab instances have to be identical. You can
[override](PrefabInstanceOverrides.html) settings on individual prefab
instances if you want some instances of a Prefab to differ from others. You
can also create [variants](PrefabVariants.html) of Prefabs which allow you to
group a set of overrides together into a meaningful variation of a Prefab.

You should also use Prefabs when you want to [instantiate GameObjects at
runtime](instantiating-prefabs.html) that did not exist in your Scene at the
start - for example, to make powerups, special effects, projectiles, or NPCs
appear at the right moments during gameplay.

Some common examples of Prefab use include:

  * Environmental Assets - for example a certain type of tree used multiple times around a level (as seen in the screenshot above).

  * Non-player characters (NPCs) - for example a certain type of robot may appear in your game multiple times, across multiple levels. They may differ (using _overrides_) in the speed they move, or the sound they make.

  * Projectiles - for example a pirate’s cannon might instantiate a cannonball Prefab each time it is fired.

  * The player’s main character - the player prefab might be placed at the starting point on each level (separate Scenes) of your game.

## Prefab Inspector previews

When you select a Prefab and view it in the **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), the Asset Preview pane in the
Inspector shows a preview of the Prefab. If the size of the Prefab is less
than 8MB, the Asset Preview pane shows an interactive preview of the Prefab,
which allows you to rotate the Prefab inside the Asset Preview pane.

If the size of the Prefab is greater than 8MB, by default the Asset Preview
shows a static preview of the Prefab. To view an interactive preview of a
Prefab that is greater than 8MB, click anywhere inside the Asset Preview pane.

[](troubleshooting-skinned-mesh-renderer-visibility.html)

Troubleshooting Skinned Mesh Renderer visibility

[](CreatingPrefabs.html)

Creating Prefabs

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

