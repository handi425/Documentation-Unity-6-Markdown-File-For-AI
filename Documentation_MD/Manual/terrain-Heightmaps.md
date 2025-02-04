[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-Heightmaps.html)
  * [中文](/cn/current/Manual/terrain-Heightmaps.html)
  * [日本語](/ja/current/Manual/terrain-Heightmaps.html)
  * [한국어](/kr/current/Manual/terrain-Heightmaps.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-Heightmaps.html)
  * [中文](/cn/current/Manual/terrain-Heightmaps.html)
  * [日本語](/ja/current/Manual/terrain-Heightmaps.html)
  * [한국어](/kr/current/Manual/terrain-Heightmaps.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * Working with Heightmaps

[](terrain-Grass.html)

Grass and other details

[](terrain-OtherSettings.html)

Terrain Settings reference

# Working with Heightmaps

Terrain tools that affect height, such as [Raise or Lower Terrain](terrain-
RaiseLowerTerrain.html) and [Set Height](terrain-SetHeight.html), use a
grayscale texture called a heightmap. Unity represents the height of each
point on the **Terrain** The landscape in your scene. A Terrain GameObject
adds a large flat plane to your scene and you can use the Terrain’s Inspector
window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) as a value in a rectangular array. It
represents this array using a grayscale [heightmap](texture-
types.html#TerrainHeightmaps)A greyscale Texture that stores height data for
an object. Each pixel stores the height difference perpendicular to the face
that pixel represents.  
See in [Glossary](Glossary.html#Heightmap). Heightmaps are built into the
Terrain, and the values stored in a heightmap define the height of each point
or vertex on the Terrain.

![Example heightmap](../uploads/Main/1.9-ExampleHeightmap.png) Example
heightmap

## Importing and exporting heightmaps

You can import and export heightmaps into the Unity Editor. This is useful
when you want to use real world height data to replicate a landmark such as
Mount Everest, or work on a heightmap image in an external image editor. You
can also use 3D modelling applications, such as Houdini and World Machine, to
generate Terrain, then import your Terrain into Unity as a heightmap.

It’s good practice to store heightmaps as RAW files. A RAW file uses a 16-bit
grayscale format that’s compatible with most image and landscape editors. The
Unity Editor enables you to import and export RAW heightmap files for a
Terrain.

To access the import and export settings into the Editor, select the Terrain
component in the **Inspector** A Unity window that displays information about
the currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), and click the **Terrain Settings**
button (gear icon in the toolbar).

![Import Raw and Export Raw buttons in the Terrain Settings
Inspector](../uploads/Main/1.9-TerrainSettings_TextureResolutions.png) Import
Raw and Export Raw buttons in the Terrain Settings Inspector

Under **Texture Resolutions (On Terrain Data)** , there are two buttons
labelled **Import Raw** and **Export Raw**.

  * **Import Raw** allows Unity to read a heightmap from the RAW file format, and generate it in the Editor.  
  
![Import Heightmap window](../uploads/Main/1.9-ImportRaw.png)

  * **Export Raw** allows Unity to write a heightmap from the Editor to the RAW file format.  
  
![Export Heightmap window](../uploads/Main/1.9-ExportRaw.png)

### Import and export options

**Property** | **Description**  
---|---  
**Depth** | Determines how many bits Unity uses per pixel in the imported or exported heightmap.  
• Bit 16: Uses 16 bits (2 bytes)  
• Bit 8: Uses 8 bits (1 byte)  
**Resolution** | The texture resolution (width and height) of the imported heightmap.  
**Byte Order** | Determines how Unity orders the bytes for each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) in the imported or exported heightmap.
This mainly applies to bit–16 depth heightmaps, and is platform-dependent.  
**Flip Vertically** | Determines whether Unity flips the exported heightmap vertically across the x-axis.  
**Terrain Size** | The size of Terrain that Unity will apply the imported heightmap to.  
  
* * *

  * 2020–06–30 Page amended 

  * Updated content to reflect new UI and options

[](terrain-Grass.html)

Grass and other details

[](terrain-OtherSettings.html)

Terrain Settings reference

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

