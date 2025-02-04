[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/materials-introduction.html)
  * [中文](/cn/current/Manual/materials-introduction.html)
  * [日本語](/ja/current/Manual/materials-introduction.html)
  * [한국어](/kr/current/Manual/materials-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/materials-introduction.html)
  * [中文](/cn/current/Manual/materials-introduction.html)
  * [日本語](/ja/current/Manual/materials-introduction.html)
  * [한국어](/kr/current/Manual/materials-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Materials](Materials.html)
  * Introduction to materials

[](Materials.html)

Materials

[](create-material.html)

Create and assign a material

# Introduction to materials

To draw something in Unity, you must provide information that describes its
shape, and information that describes the appearance of its surface. You use
[meshes](class-Mesh.html) to describe shapes, and materials to describe the
appearance of surfaces.

Materials and **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) are closely linked; you always use
materials with shaders.

## Render pipeline compatibility

Feature | Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP) | High Definition Render Pipeline (HDRP) | Custom Scriptable Render Pipeline (SRP) | Built-in Render Pipeline  
---|---|---|---|---  
Materials | Yes | Yes | Yes | Yes  
  
## Material fundamentals

A material contains a reference to a [Shader object](shader-objects.html)An
instance of the Shader class, a Shader object is container for shader programs
and GPU instructions, and information that tells Unity how to use them. Use
them with materials to determine the appearance of your scene. [More
info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject). If that Shader object defines
[material properties](SL-Properties.html), then the material can also contain
data such as colors or references to textures.

The [Material](../ScriptReference/Material.html)An asset that defines how a
surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) class represents a material in C#
code. For information, see [Using Materials with C#
scripts](MaterialsAccessingViaScript.html).

A material asset is a file with the `.mat` extension. It represents a material
in your Unity project. For information on viewing and editing a material asset
using the **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, see [Material Inspector
reference](class-Material.html).

## Material Variants

Unity supports functionality for creating variants of Materials. To learn more
about this functionality, see [Material Variants](materialvariant-
landingpage.html).

[](Materials.html)

Materials

[](create-material.html)

Create and assign a material

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

