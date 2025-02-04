[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/scene-templates-editing.html)
  * [中文](/cn/current/Manual/scene-templates-editing.html)
  * [日本語](/ja/current/Manual/scene-templates-editing.html)
  * [한국어](/kr/current/Manual/scene-templates-editing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/scene-templates-editing.html)
  * [中文](/cn/current/Manual/scene-templates-editing.html)
  * [日本語](/ja/current/Manual/scene-templates-editing.html)
  * [한국어](/kr/current/Manual/scene-templates-editing.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * [Scene Templates](scene-templates.html)
  * Editing scene templates

[](scene-templates-creating.html)

Creating scene templates

[](scene-templates-customizing-scene-instantiation.html)

Customizing new scene creation

# Editing scene templates

To edit a **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) template, select it in the [Project
window](https://docs.unity3d.com/Manual/ProjectView.html)A window that shows
the contents of your `Assets` folder (Project tab) [More
info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), then open it in an [Inspector
window](https://docs.unity3d.com/Manual/UsingTheInspector.html).

**Note:**  
---  
When you first create an [empty scene template](scene-templates-
creating.html#creating-an-empty-scene-template), you must edit its properties
to associate it with a scene before you can use it. Templates that you create
from the active scene, or an existing scene asset, have some properties set by
default.  
  
![The scene template Inspector](../uploads/Main/scene-template-inspector.png)  
_The scene template Inspector_

The scene template **Inspector** A Unity window that displays information
about the currently selected GameObject, asset or project settings, allowing
you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) has the following sections:

  1. **Details** : Specifies which scene the template uses, and contains the template description that appears in the New Scene dialog.
  2. **Thumbnail** : Provides options for creating a preview image for the template.
  3. **Scene Template Pipeline** : Specifies an optional custom script to run when Unity creates a new scene from the template.
  4. **Dependencies** : Lists the template scene’s dependencies, and specifies whether Unity clones them when it creates a new scene from the template.

### Details

Use the Details section to specify which scene to use for a template, and
control how the template appears in the [New Scene
dialog](CreatingScenes.html#new-scene-dialog).

![](../uploads/Main/scene-template-inspector-details.png)  

**Property:** | **Description:**  
---|---  
**Template Scene** |  | Specifies the scene to use as a template. This can be any scene in the Project.  
**Title** |  | The template name. The name you enter here appears in the [New Scene dialog](CreatingScenes.html#new-scene-dialog).  
**Description** |  | The template description. The description you enter here appears in the [New Scene dialog](CreatingScenes.html#new-scene-dialog).  
**Pin in New Scene Dialog** |  | Controls whether this template is pinned in the [New Scene dialog](CreatingScenes.html#new-scene-dialog).  
  
Pinned templates always appear at the top of the **Scene Templates in
Project** list.  
  
### Thumbnail

The Thumbnail section contains options for creating a preview image for the
template. The preview image appears in the New Scene dialog.

![The scene template Inspector](../uploads/Main/scene-template-inspector-
thumbnail.png)  

**Property:** | **Description:**  
---|---  
**Texture** |  | Specifies a Texture asset to use as a thumbnail for this template. You can use any Texture asset in the Project.   
  
If you don’t assign a Texture, the template uses the default scene template
asset icon.  
**_[Thumbnail Preview]_** |  | Displays the template’s thumbnail texture, if it has one.  
**Snapshot** |  | Provides options for capturing a thumbnail image for this template.  
| View | Specifies whether to capture the **Main**Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)** view or the **Game View**.  
| Take Snapshot | Click this button to capture the selected **View**.  
  
### Scene Template Pipeline

Use these properties to add a **Scene Template Pipeline** script to this
template.

![](../uploads/Main/scene-template-inspector-pipeline.png)  

A Scene Template Pipeline script lets you execute custom code when you create
a new scene from the template. See [Customizing new scene creation](scene-
templates-customizing-scene-instantiation.html).

### Dependencies

This section lists all of the template scene’s **Dependencies**. You can
specify whether or not to **Clone** each dependency when you [create a new
scene from the template](scenes-working-with.html).

To search for a dependency by name, enter text in the search bar.

To sort the **Dependencies** list:

  * Click the **Dependencies** heading to sort by the name of the dependency in alphabetical order.
  * Click the **Type** heading to sort by the dependency Type.
  * Click the **Clone** heading to sort by dependencies that are cloned and not cloned.

![](../uploads/Main/Scene-template-inspector-dependencies.png)  

For each dependency in the list, toggle the **Clone** option on to clone the
dependency, or off to reference the dependency. When you clone a dependency,
you create a copy. When you reference a dependency, all changes made to the
original will affect the dependency.

When you create a new scene from the template, Unity checks whether the
template scene has cloneable dependencies. If it does, Unity creates a folder
with the same name as the new scene, and puts any cloned dependencies in that
folder.

For more information about cloned and referenced dependencies, see [Templates
and scene dependencies](scene-templates.html#templates-and-scene-
dependencies).

To specify which types of asset Unity clones by default, edit the [scene
template Project settings](scene-templates-settings.html).

* * *

[](scene-templates-creating.html)

Creating scene templates

[](scene-templates-customizing-scene-instantiation.html)

Customizing new scene creation

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

