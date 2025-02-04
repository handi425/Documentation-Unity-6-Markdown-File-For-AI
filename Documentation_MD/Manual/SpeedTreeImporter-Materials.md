[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SpeedTreeImporter-Materials.html)
  * [中文](/cn/current/Manual/SpeedTreeImporter-Materials.html)
  * [日本語](/ja/current/Manual/SpeedTreeImporter-Materials.html)
  * [한국어](/kr/current/Manual/SpeedTreeImporter-Materials.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SpeedTreeImporter-Materials.html)
  * [中文](/cn/current/Manual/SpeedTreeImporter-Materials.html)
  * [日本語](/ja/current/Manual/SpeedTreeImporter-Materials.html)
  * [한국어](/kr/current/Manual/SpeedTreeImporter-Materials.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Import trees from SpeedTree](SpeedTree-landing.html)
  * [SpeedTree Import Settings window](class-SpeedTreeImporter.html)
  * Materials tab

[](SpeedTreeImporter-Model.html)

Model tab

[](terrain-Tree-LOD.html)

Tree level of detail (LOD)

# Materials tab

Use the **Materials** tab to change how Unity deals with materials for an
imported SpeedTree model. If the model has materials, Unity imports them as
sub-assets.

To change other import settings for the [SpeedTree](SpeedTree.html) model, see
the [Model tab](SpeedTreeImporter-Model.html).

![SpeedTree Importer Materials tab](../uploads/Main/class-SpeedTreeImporter-
Materials.png) SpeedTree Importer Materials tab

The **Materials** tab has these sections:

**(A)** The Location and Materials properties allow you to control how Unity
accesses the materials inside the imported asset.

**(B)** The Remapped Materials section allows you to remap the imported
materials to existing materials in your project.

**(C)** The **Revert** and **Apply** options always appear, but you can only
select them after you make changes to the import settings. If you change
settings in the Remapped Materials section of the **Materials** tab, the
**Apply & Generate Materials** option appears.

**(D)** The properties for the **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) (read-only) appear at the bottom
of the ****Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** view, including a preview of the
SpeedTree model with its material applied.

## Location and Materials

**Property** | **Description**  
---|---  
**Location** | Define how the materials are accessed. These options aren’t available for .st9 files, which only use embedded materials.  
| **Use Embedded Materials** | Import materials as sub-assets inside the SpeedTree model. This is the default and recommended option.  
| **Use External Materials (Legacy)** | Extract materials to a folder with the same name and location as the model. This is a deprecated option for projects created with Unity 2017.1 or earlier and isn’t recommended for use.  
**Materials** | For .st and .spm files, this property is visible only when **Location** is set to **Use Embedded Materials**.  
| **Extract Materials** | Extract the embedded materials from the imported asset and save them to a folder of your choice. Extracted materials populate the Remapped Materials list. Use this option to modify the materials or share them with other SpeedTree assets. This option isn’t available if there are no sub-asset materials to extract from the model.  
  
## Remapped Materials

The Remapped Materials section lists the embedded materials and allows you to
remap them to other materials that are already in the project.

If you already have a set of materials you want to use for this asset, expand
the **On Demand Remap** group, select **Search and Remap** , and give the
location of the materials. Unity remaps the imported materials to existing
materials with the same name. Nothing changes if Unity can’t find any
materials with the same name. You can manually remap materials from the
Remapped Materials list.

![The Remapped Materials section with the On Demand Remap group
expanded](../uploads/Main/class-SpeedTreeImporter-Materials_SearchAndMap.png)
The Remapped Materials section with the On Demand Remap group expanded

To save the imported SpeedTree model with the remapped materials, select
**Apply**.

If you make changes to the material properties through the Model tab’s import
settings or an **LOD** The _Level Of Detail_ (LOD) technique is an
optimization that reduces the number of triangles that Unity has to render for
a GameObject when its distance from the Camera increases. [More
info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) setting override, select **Regenerate
Materials** to re-import the materials in the Remapped Materials list with the
updated settings.

> **Warning:** Re-generating the external materials removes any manual
> modifications you made to the material files.

New imports or changes to the original asset don’t affect extracted materials.
If you want to re-import the materials from the source asset, remove the
references to the extracted materials in the Remapped Materials list. To
remove an item from the list, select it and press the Backspace key on your
keyboard.

[](SpeedTreeImporter-Model.html)

Model tab

[](terrain-Tree-LOD.html)

Tree level of detail (LOD)

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

