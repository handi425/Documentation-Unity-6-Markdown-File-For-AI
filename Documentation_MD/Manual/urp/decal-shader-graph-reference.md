[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/decal-shader-graph-reference.html)
  * [中文](/cn/current/Manual/urp/decal-shader-graph-reference.html)
  * [日本語](/ja/current/Manual/urp/decal-shader-graph-reference.html)
  * [한국어](/kr/current/Manual/urp/decal-shader-graph-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/decal-shader-graph-reference.html)
  * [中文](/cn/current/Manual/urp/decal-shader-graph-reference.html)
  * [日本語](/ja/current/Manual/urp/decal-shader-graph-reference.html)
  * [한국어](/kr/current/Manual/urp/decal-shader-graph-reference.html)

  * [Visual effects](../visual-effects.html)
  * [Decals and projectors](../visual-effects-decals.html)
  * [Decals in URP](../urp/renderer-feature-decal-landing.html)
  * Decal Shader Graph reference for URP

[](../urp/renderer-feature-decal-projector-reference.html)

Decal Projector component reference for URP

[](../decals-birp.html)

Decals in the Built-In Render Pipeline

# Decal Shader Graph reference for URP

You can assign a Material that uses a Decal **Shader** A program that runs on
the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) Graph to a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) directly. For example, you can
[use a Quad as the Decal GameObject](renderer-feature-decal-create.html#decal-
gameobject).

The pre-built Decal Shader has the following properties:

  * **Base Map** : the Base texture of the Material.

  * ****Normal Map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](../Glossary.html#Normalmap)**: the normal texture of the
Material.

  * **Normal Blend** : this property defines the proportion in which the the normal texture selected in the Normal Map property blends with the normal map of the Material that the decal is projected on. 0: the decal does not affect the Material it’s projected on. 1: the normal map of the decal replaces the normal map of the Material it’s projected on.

**Property** | **Description**  
---|---  
**Affect BaseColor** | When enabled, the shader affects the base color. Most decals make use of this option. An exception is a surface damage effect, were you might want to manipulate other properties, such as normals.  
![Decal Color](../../uploads/urp/decal/decal-color.png)  
_From left to right: shader affecting only the color, affecting all
properties, affecting all properties but color._  
**Affect Normal** | When enabled, the shader affects normals. Use cases: adding damage effects to materials, for example, bullet holes or cracks. Use the **Blend** property to blend the normals of the decal with the normals of the surface it’s projected to. If the **Blend** property is disabled, the decal overrides the normals all over the surface it’s projected to.  
![Decal Normal](../../uploads/urp/decal/decal-normal.png)  
_From left to right: Affect Normal is off; Affect Normal is on, Blend is off;
Affect Normal and Blend are on._  
**Affect MAOS** | MOAS stands for Metallic, Ambient Occlusion, and Smoothness. These properties are grouped together to save memory. You can change values of each property separately in the shader, but all properties are blended with a single common alpha value.  
Use cases:  
Override smoothness to highlight puddles or wet paint. Override metallic
values with lower values to render rust. Override AO to give the decal more
depth.  
![Decal MAOS](../../uploads/urp/decal/decal-maos.png)  
_Left: the decal does not affect MAOS. Right: the decal affects MAOS._  
**Affect Emission** | Use cases: you can affect the emission values to make surfaces seem like they are emitting light, or to make surfaces seem like they are being lit by light.  
![Decal Emission](../../uploads/urp/decal/decal-emission.png)  
_Left: Affect Emission is off. Right: Affect Emission is on._  
  
The Decal Material properties above are defined in the pre-built Shader Graph.
Custom decal Material properties depend on a custom Shader Graph.

The following table describes the properties in the **Advanced Options**
section. These properties are common for all decal shaders.

**Property** | **Description**  
---|---  
**Enable GPU Instancing** | Enabling this option lets URP render meshes with the same geometry and Material in one batch, when possible. This makes rendering faster. URP cannot render Meshes in one batch if they have different Materials or if the hardware does not support GPU instancing.  
**Priority** | This property defines the order in which URP draws decals in the scene. URP draws decals with lower Priority values first, and draws decals with higher Priority values on top of those with lower values.   
If there are multiple Decal Materials with the same **Priority** in the scene,
URP renders them in the order in which the Materials were created.  
**Mesh Bias Type** | Select the Mesh bias type. The Mesh bias lets you prevent z-fighting between the Decal GameObject and the GameObject it overlaps. This property is only applicable for GameObjects with a [Decal Material type assigned directly](renderer-feature-decal-create.html#decal-gameobject).  
_View Bias_ | A world-space bias (in meters). When drawing the Decal GameObject, Unity shifts each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) of the GameObject by this value
along the view vector. A positive value shifts pixels closer to the **Camera**
A component which creates an image of a particular viewpoint in your scene.
The output is either drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera), so that Unity draws the Decal
GameObject on top of the overlapping **Mesh** The main graphics primitive of
Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](../mesh.html)  
See in [Glossary](../Glossary.html#Mesh), which prevents z-fighting. Decal
Projectors ignore this property.  
_Depth Bias_ | When drawing the Decal GameObject, Unity changes the depth value of each pixel of the GameObject by this value. A negative value shifts pixels closer to the Camera, so that Unity draws the Decal GameObject on top of the overlapping Mesh, which prevents z-fighting. Decal Projectors ignore this property.  
  
[](../urp/renderer-feature-decal-projector-reference.html)

Decal Projector component reference for URP

[](../decals-birp.html)

Decals in the Built-In Render Pipeline

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

