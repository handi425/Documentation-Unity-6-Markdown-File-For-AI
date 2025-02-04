[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-FBXImporter.html)
  * [中文](/cn/current/Manual/class-FBXImporter.html)
  * [日本語](/ja/current/Manual/class-FBXImporter.html)
  * [한국어](/kr/current/Manual/class-FBXImporter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-FBXImporter.html)
  * [中文](/cn/current/Manual/class-FBXImporter.html)
  * [日本語](/ja/current/Manual/class-FBXImporter.html)
  * [한국어](/kr/current/Manual/class-FBXImporter.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * Model Import Settings window

[](GenericAnimations.html)

Importing a model with non-humanoid (generic) animations

[](FBXImporter-Model.html)

Model tab

# Model Import Settings window

![The FBX Model Import Settings window](../uploads/Main/classFBXImporter-
Inspector.png) The FBX Model Import Settings window

**Note:** These settings are for importing Models and animations created in
most 3D modeling applications. However, Models created in SketchUp and
SpeedTree use specialized settings. For more information, see [SketchUp
Settings](class-SketchUpImporter.html), and [SpeedTree Import Settings](class-
SpeedTreeImporter.html).

When you put **Model files** A file containing a 3D data, which may include
definitions for meshes, bones, animation, materials and textures. [More
info](3D-formats.html)  
See in [Glossary](Glossary.html#Modelfile) in the Assets folder under your
Unity Project, Unity automatically imports and stores them as Unity Assets. To
view the import settings in the **Inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, click on the file in the
**Project** In Unity, you use a project to design and develop a game. A
project stores all of the files that are related to a game, such as the asset
and Scene files. [More info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) window. You can customize how Unity
imports the selected file by setting the properties on four tabs on this
window:

[![Model tab](../uploads/Main/class-FBXImporter_Model-tab.png)](FBXImporter-
Model.html)  
A 3D [Model](FBXImporter-Model.html)A 3D model representation of an object,
such as a character, a building, or a piece of furniture. [More
info](3D-formats.html)  
See in [Glossary](Glossary.html#Model) can represent a character, a building,
or a piece of furniture. In these cases, Unity creates multiple Assets from a
single model file. In the Project window, the main imported object is a model
**Prefab** An asset type that allows you to store a GameObject complete with
components and properties. The prefab acts as a template from which you can
create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab). Usually there are also several
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) objects that the model Prefab
references.

[![Rig tab](../uploads/Main/class-FBXImporter_Rig-tab.png)](FBXImporter-
Rig.html)  
A [Rig](FBXImporter-Rig.html)A skeletal hierarchy of joints for a mesh. [More
info](FBXImporter-Rig.html)  
See in [Glossary](Glossary.html#Rig) (sometimes called a _skeleton_) comprises
a set of deformers arranged in a hierarchy that animate a Mesh (sometimes
called _skin_) on one or more models created in a 3D modeling application such
as as Autodesk® 3ds Max® or Autodesk® Maya®. For **Humanoid** and **Generic**
(non-humanoid) Models, Unity creates an **Avatar** An interface for
retargeting animation from one rig to another. [More
info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar) to reconcile the imported Rig with the
Unity **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

[![Animation tab](../uploads/Main/class-FBXImporter_Animation-tab.png)](class-
AnimationClip.html)  
You can define any series of different poses occurring over a set of frames,
such as walking, running, or even idling (shifting from one foot to the other)
as an [Animation Clip](class-AnimationClip.html). You can reuse clips for any
Model that has an identical Rig. Often a single file contains several
different actions, each of which you can define as a specific **Animation
Clip** Animation data that can be used for animated characters or simple
animations. It is a simple “unit” piece of motion, such as (one specific
instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip).

[![Materials tab](../uploads/Main/class-FBXImporter_Materials-
tab.png)](FBXImporter-Materials.html)  
You can extract [Materials and Textures](FBXImporter-Materials.html) or leave
them embedded within the model. You can also adjust how Material is mapped in
the Model.

### See also

  * [Model import workflows](ImportingModelFiles.html): Overview of importing Model files
  * [Model file formats](3D-formats.html): Which file formats (both proprietary and generic) that Unity supports, as well as issues specific to various 3D modeling software applications

FBXImporter

[](GenericAnimations.html)

Importing a model with non-humanoid (generic) animations

[](FBXImporter-Model.html)

Model tab

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

