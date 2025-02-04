[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-Material.html)
  * [中文](/cn/current/Manual/class-Material.html)
  * [日本語](/ja/current/Manual/class-Material.html)
  * [한국어](/kr/current/Manual/class-Material.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-Material.html)
  * [中文](/cn/current/Manual/class-Material.html)
  * [日本語](/ja/current/Manual/class-Material.html)
  * [한국어](/kr/current/Manual/class-Material.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Materials](Materials.html)
  * Material Inspector window reference

[](MaterialValidator.html)

Material Validator window reference for the Built-In Render Pipeline

[](visual-effects.html)

Visual effects

# Material Inspector window reference

[Switch to Scripting](../ScriptReference/Material.html "Go to Material page in
the Scripting Reference")

You can view and edit a Material asset in the ****Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window.

The Material Inspector makes it possible to do the following things:

  * Modify a Material or Material Variant’s Properties
  * Identify and change its relationships with other Materials and Material Variant
  * Copy and paste its Property settings
  * Associate it with a **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) or **lightmap** A pre-rendered texture
that contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) atlas

See [Materials introduction](materials-introduction.html) to learn more about
Materials.

![](../uploads/Main/material-inspector-controls.png) Material controls in the
Inspector

A: Inspector Controls  
B: Material Controls  
C: Material Hierarchy  

## Settings

Click Material Controls to open the selected Material’s Settings menu.

**Setting** | **Function**  
---|---  
**Select Shader** | Move focus to this shader asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow). This can aid navigation in a
Project with many Assets.  
**Edit Shader** | Open the source file for the shader asset that this Material uses.  
**Select Material** | Move focus to this Material asset in the Project window. This can aid navigation in a Project with many Assets.  
**Flatten Material Variant** | Convert this Material Variant to a Material and retain its Property values. Only available when the selected Material is a Variant.  
**Copy Material Properties** | Copy Material Property values so that you can copy them to other Materials.  
**Paste Material Properties** | Paste Material Property values into this Material from the computer’s clipboard. Only available when there are Property Values in the clipboard.  
**Create Material Preset** | Create a duplicate of this Material’s Property settings. See [Presets](https://docs.unity3d.com/Manual/Presets.html) for more information. By default, Unity creates the duplicate in the same asset directory as this Material.  
**Copy Atlas** | Copy the font atlas to the keyboard. Only for [Text Mesh Pro](https://docs.unity3d.com/Packages/com.unity.textmeshpro@4.0/manual/index.html) Materials.  
**Paste Atlas** | Paste a Text **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Pro font atlas into this Material.  
**Reset** | Reset all Material properties to the default values specified by the shader associated with this Material.  
  
## Advanced Options

The properties the Unity Editor displays for a Material depend on the Material
Properties defined by the shader that this Material uses. However, all
Materials share three **Advanced Options**.

**Advanced Options** | **Function**  
---|---  
**Render Queue** | Select a Render Queue. The Material’s shader determines the default Render Queue value. Corresponds to the [Material.renderQueue](../ScriptReference/Material-renderQueue.html) property.  
**Enable GPU Instancing** | Optimize draw calls for meshes that use this Material. See [GPU Instancing](GPUInstancing.html) for more information.  
**Double Sided Global Illumination** | Instruct the Progressive Lightmappers to consider backfaces in [global illumination](LightingInUnity.html)A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) calculations. When this
option is active, back-facing polygons bounce light using the same emission
and albedo values as front-facing polygons.  
  
**Note** : The appearance of back-facing polygons does not change when you
enable this option because this option does not cause Unity to render back-
facing polygons or add them to lightmaps.  
  
Corresponds to the [Material.doubleSidedGI](../ScriptReference/Material-
doubleSidedGI.html) property.  
  
### Additional resources

  * [Standard Shader](https://docs.unity3d.com/2022.1/Documentation/Manual/shader-StandardShader.html)
  * [Standard shader Material Properties](https://docs.unity3d.com/2022.1/Documentation/Manual/StandardShaderMaterialParameters.html)
  * [Shader introduction](https://docs.unity3d.com/2022.1/Documentation/Manual/shader-introduction.html)
  * [Render queue](https://docs.unity3d.com/2022.1/Documentation/ScriptReference/Rendering.RenderQueue.html)
  * [ShaderLab: SubShader tags](https://docs.unity3d.com/2022.1/Documentation/Manual/SL-SubShaderTags.html)
  * [ShaderLab: defining material properties](https://docs.unity3d.com/2022.1/Documentation/Manual/SL-Properties.html)
  * [Legacy shaders](https://docs.unity3d.com/2022.1/Documentation/Manual/Built-inShaderGuide.html)

Material

[](MaterialValidator.html)

Material Validator window reference for the Built-In Render Pipeline

[](visual-effects.html)

Visual effects

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

