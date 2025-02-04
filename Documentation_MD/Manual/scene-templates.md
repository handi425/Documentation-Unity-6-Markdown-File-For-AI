[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/scene-templates.html)
  * [中文](/cn/current/Manual/scene-templates.html)
  * [日本語](/ja/current/Manual/scene-templates.html)
  * [한국어](/kr/current/Manual/scene-templates.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/scene-templates.html)
  * [中文](/cn/current/Manual/scene-templates.html)
  * [日本語](/ja/current/Manual/scene-templates.html)
  * [한국어](/kr/current/Manual/scene-templates.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * Scene Templates

[](scriptmultiplescenes.html)

Use scripts to edit multiple scenes

[](scene-templates-creating.html)

Creating scene templates

# Scene Templates

To create new scenes, Unity copies **scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) templates. Think of a scene template as
a pre-configured scene that contains all of the content you want to start
with. For example, the default Basic template usually contains a **Camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) and a light.

You can create your own scene templates to customize the types of new scene
you can create in a project. For example, you might create templates for each
level in a game so that everyone working on the project can start their scenes
with the correct assets and configuration.

You can create a template from any Unity scene. After you create a template,
you can create any number of new scenes from it. Like scenes, most scene
templates are assets that are stored in the project.

This page explains important scene template concepts. For more information
about creating, editing, and managing scene templates, see the following
pages:

  * [Creating scene templates](scene-templates-creating.html): Describes the different ways to create a scene template.
  * [Editing scene templates](scene-templates-editing.html): Explains how to edit Scene template properties.
  * [Customizing new scene creation](scene-templates-customizing-scene-instantiation.html): Explains how to attach a script to a scene template so you can run custom code when Unity creates a scene from the template.
  * [Scene template settings](scene-templates-settings.html): Describes **project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) for scene templates. Most of
these settings control how Unity closes and references scene dependencies when
you create a new scene from a template.

## Important concepts

### Built-in templates vs. user-defined templates

Most scene templates are user-defined, meaning you create them from your own
scenes. User-defined scene templates are assets that Unity stores in the
project.

Unity also ships with built-in templates for each project type. For example,
some project types include a Basic template that creates a scene with a Camera
and a light, and an Empty template that creates an empty scene.

Built-in templates are different from other templates because they are not
assets stored in the project, and you cannot modify them.

**Note:**  
---  
Some Unity packages might also include scene templates that they install when
you install the package.  
  
### Templates and scene dependencies

When you create a scene template, you can specify whether Unity clones or
references its dependencies (the assets it includes) when you create a new
scene from it.

To specify which assets Unity clones for a specific template, [edit the
template’s properties](scene-templates-editing.html).

A typical template might contain a mix of cloned and referenced assets. Unity
sets several asset types to clone by default.

To change whether Unity clones or references a given asset type by default,
edit the [Scene template project settings](scene-templates-settings.html).

#### Cloning template assets

Cloned assets are copies of the original assets that the template scene uses.
When Unity creates the new scene from the template, it automatically modifies
the new scene to use any cloned assets. If you modify the cloned assets, it
does not affect the template scene. If you modify the original assets in the
template scene, it does not affect the new scene.

Cloning template assets is useful when you want new scenes to contain a
starting set of assets that users might modify.

#### Referencing template assets

Referenced assets are the original assets that the template scene uses. When
Unity creates the new scene from the template, the new scene points to the
same assets as the template scene. If you modify those assets, it affects both
the new scene and the template scene.

Referencing template assets is useful when you want new scenes to contain a
default set of assets that users build on top of, but do not modify.

* * *

[](scriptmultiplescenes.html)

Use scripts to edit multiple scenes

[](scene-templates-creating.html)

Creating scene templates

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

