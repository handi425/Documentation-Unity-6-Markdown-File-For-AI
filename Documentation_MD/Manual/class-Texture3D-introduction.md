[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-Texture3D-introduction.html)
  * [中文](/cn/current/Manual/class-Texture3D-introduction.html)
  * [日本語](/ja/current/Manual/class-Texture3D-introduction.html)
  * [한국어](/kr/current/Manual/class-Texture3D-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-Texture3D-introduction.html)
  * [中文](/cn/current/Manual/class-Texture3D-introduction.html)
  * [日本語](/ja/current/Manual/class-Texture3D-introduction.html)
  * [한국어](/kr/current/Manual/class-Texture3D-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [3D textures](class-Texture3D.html)
  * Introduction to 3D textures

[](class-Texture3D.html)

3D textures

[](class-Texture3D-import.html)

Create a 3D texture

# Introduction to 3D textures

A 3D texture is a bitmap image that contains information in three dimensions
rather than the standard two. 3D textures are commonly used to simulate
volumetric effects such as fog or smoke, to approximate a volumetric 3D
**mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), or to store animated textures and blend
between them.

The source texture files for **2D Array** and **3D** Textures are divided into
cells; these textures are called flipbook textures. When Unity imports
flipbook textures, it places the contents of each cell into its own 2D array
layer or 3D texture slice.

For example, an image with 8x8 cells of smoke effect frames looks like this as
a default 2D texture:

![Flipbook image as a 2D shape](../uploads/Main/TextureImporter-
Flipbook-2D.jpg) Flipbook image as a 2D shape

But when you correctly import is as a 3D texture with 8 Columns and 8 Rows, it
looks like this:

![Flipbook image as a 3D shape](../uploads/Main/TextureImporter-
Flipbook-3D.jpg) Flipbook image as a 3D shape

[](class-Texture3D.html)

3D textures

[](class-Texture3D-import.html)

Create a 3D texture

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

