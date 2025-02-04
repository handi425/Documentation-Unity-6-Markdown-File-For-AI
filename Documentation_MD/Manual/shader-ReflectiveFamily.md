[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-ReflectiveFamily.html)
  * [中文](/cn/current/Manual/shader-ReflectiveFamily.html)
  * [日本語](/ja/current/Manual/shader-ReflectiveFamily.html)
  * [한국어](/kr/current/Manual/shader-ReflectiveFamily.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-ReflectiveFamily.html)
  * [中文](/cn/current/Manual/shader-ReflectiveFamily.html)
  * [日本語](/ja/current/Manual/shader-ReflectiveFamily.html)
  * [한국어](/kr/current/Manual/shader-ReflectiveFamily.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * Reflective Shader Family

[](shader-SelfIllumParallaxSpecular.html)

Self-Illuminated Parallax Specular

[](shader-ReflectiveVertexLit.html)

Reflective Vertex-Lit

# Reflective Shader Family

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces these **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

**Reflective** shaders will allow you to use a **Cubemap** A collection of six
square textures that can represent the reflections in an environment or the
skybox drawn behind your geometry. The six squares form the faces of an
imaginary cube that surrounds an object; each face represents the view along
the directions of the world axes (up, down, left, right, forward and back).
[More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) which will be reflected on your
**mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh). You can also define areas of more or
less reflectivity on your object through the alpha channel of the **Base**
texture. High reflectivity is a great effect for glosses, oils, chrome, etc.
Low reflectivity can add effect for metals, liquid surfaces, or video
monitors.

## [Reflective Vertex-Lit](shader-ReflectiveVertexLit.html)

![shader-ReflectiveVertexLit](../uploads/Shaders/Thumb-ReflVertex.jpg) shader-
ReflectiveVertexLit

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map

[» More details](shader-ReflectiveVertexLit.html)

## [Reflective Diffuse](shader-ReflectiveDiffuse.html)

![shader-ReflectiveDiffuse](../uploads/Shaders/Thumb-ReflDiffuse.jpg) shader-
ReflectiveDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map

[» More details](shader-ReflectiveDiffuse.html)

## [Reflective Specular](shader-ReflectiveSpecular.html)

![shader-ReflectiveSpecular](../uploads/Shaders/Thumb-ReflSpec.jpg) shader-
ReflectiveSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas & Specular Map combined
  * One **Reflection** Cubemap for Reflection Map

**Note:** One consideration for this shader is that the **Base** texture’s
alpha channel will double as both the reflective areas and the Specular Map.

[» More details](shader-ReflectiveSpecular.html)

## [Reflective Normal mapped](shader-ReflectiveBumpedDiffuse.html)

![shader-ReflectiveBumpedDiffuse](../uploads/Shaders/Thumb-ReflBump.jpg)
shader-ReflectiveBumpedDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap), no alpha channel required

[» More details](shader-ReflectiveBumpedDiffuse.html)

## [Reflective Normal Mapped Specular](shader-ReflectiveBumpedSpecular.html)

![shader-ReflectiveBumpedSpecular](../uploads/Shaders/Thumb-ReflBumpSpec.jpg)
shader-ReflectiveBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas & Specular Map combined
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required

**Note:** One consideration for this shader is that the **Base** texture’s
alpha channel will double as both the reflective areas and the Specular Map.

[» More details](shader-ReflectiveBumpedSpecular.html)

## [Reflective Parallax](shader-ReflectiveParallaxDiffuse.html)

![shader-ReflectiveParallaxDiffuse](../uploads/Shaders/Thumb-
ReflParallaxBump.jpg) shader-ReflectiveParallaxDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , with alpha channel for Parallax Depth

[» More details](shader-ReflectiveParallaxDiffuse.html)

## [Reflective Parallax Specular](shader-ReflectiveParallaxSpecular.html)

![shader-ReflectiveParallaxSpecular](../uploads/Shaders/Thumb-
ReflParallaxBumpSpec.jpg) shader-ReflectiveParallaxSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas & Specular Map
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , with alpha channel for Parallax Depth

**Note:** One consideration for this shader is that the **Base** texture’s
alpha channel will double as both the reflective areas and the Specular Map.

[» More details](shader-ReflectiveParallaxSpecular.html)

## [Reflective Normal mapped Unlit](shader-ReflectiveBumpedUnlit.html)

![shader-ReflectiveBumpedUnlit](../uploads/Shaders/Thumb-ReflBumpUnlit.jpg)
shader-ReflectiveBumpedUnlit

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required

[» More details](shader-ReflectiveBumpedUnlit.html)

## [Reflective Normal mapped Vertex-Lit](shader-
ReflectiveBumpedVertexLit.html)

![shader-ReflectiveBumpedVertexLit](../uploads/Shaders/Thumb-
ReflBumpVertex.jpg) shader-ReflectiveBumpedVertexLit

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required

[» More details](shader-ReflectiveBumpedVertexLit.html)

ReflectiveFamily

[](shader-SelfIllumParallaxSpecular.html)

Self-Illuminated Parallax Specular

[](shader-ReflectiveVertexLit.html)

Reflective Vertex-Lit

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

