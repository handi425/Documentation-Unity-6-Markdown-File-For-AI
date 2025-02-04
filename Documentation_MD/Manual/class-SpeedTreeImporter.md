[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-SpeedTreeImporter.html)
  * [中文](/cn/current/Manual/class-SpeedTreeImporter.html)
  * [日本語](/ja/current/Manual/class-SpeedTreeImporter.html)
  * [한국어](/kr/current/Manual/class-SpeedTreeImporter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-SpeedTreeImporter.html)
  * [中文](/cn/current/Manual/class-SpeedTreeImporter.html)
  * [日本語](/ja/current/Manual/class-SpeedTreeImporter.html)
  * [한국어](/kr/current/Manual/class-SpeedTreeImporter.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Import trees from SpeedTree](SpeedTree-landing.html)
  * SpeedTree Import Settings window

[](SpeedTree.html)

SpeedTree model import

[](SpeedTreeImporter-Model.html)

Model tab

# SpeedTree Import Settings window

[Switch to Scripting](../ScriptReference/SpeedTreeImporter.html "Go to
SpeedTreeImporter page in the Scripting Reference")

When you put SpeedTree files in your Unity project’s Assets folder, Unity
automatically imports and stores them as Unity assets. To view the import
settings in the **Inspector** A Unity window that displays information about
the currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), select the file in the **Project**
In Unity, you use a project to design and develop a game. A project stores all
of the files that are related to a game, such as the asset and Scene files.
[More info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) window. To customize how Unity
imports the selected file, use the properties on the **Model** and
**Materials** tabs on this window. SpeedTree 9 assets imported as .st9 files
also have a **Wind** tab.

**Note:** These settings are for importing models created in
[SpeedTree](SpeedTree.html). For information on models and animation created
in other 3D modeling applications, see the [Model Import Settings](class-
FBXImporter.html) window.

![The SpeedTree Import Settings window](../uploads/Main/class-
SpeedTreeImporter.png) The SpeedTree Import Settings window

Unity recognizes and imports SpeedTree model assets in the same way it handles
other assets. If you’re using SpeedTree Modeler 7, re-save your .spm files
using the Unity version of the Modeler. If you’re using SpeedTree Modeler 8 or
9, save your .st or .st9 files directly into the Unity project folder. The
SpeedTree Importer generates a **prefab** An asset type that allows you to
store a GameObject complete with components and properties. The prefab acts as
a template from which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) with the [LOD Group](class-
LODGroup.html)A component to manage level of detail (LOD) for GameObjects.
[More info](class-LODGroup.html)  
See in [Glossary](Glossary.html#LODGroup) component configured. You can
instantiate the prefab in a **scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as a common prefab instance or select
the prefab as a tree prototype and paint it across the **terrain** The
landscape in your scene. A Terrain GameObject adds a large flat plane to your
scene and you can use the Terrain’s Inspector window to create a detailed
landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain).

Materials come embedded in the imported SpeedTree model as sub-assets. If you
want to make adjustments to the materials, you can extract them to a location
of your choice or re-use existing materials with Material Remapping.

**Topic** | **Description**  
---|---  
**[Model tab](SpeedTreeImporter-Model.html)** | Understand the options in the Model tab of the SpeedTree Import Settings window.  
**[Materials tab](SpeedTreeImporter-Materials.html)** | Understand the options in the Materials tab of the SpeedTree Import Settings window.  
**[Wind tab](SpeedTreeImporter-Wind.html)** | Understand the wind options for SpeedTree 9 assets imported as .st9 files.  
  
[](SpeedTree.html)

SpeedTree model import

[](SpeedTreeImporter-Model.html)

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

