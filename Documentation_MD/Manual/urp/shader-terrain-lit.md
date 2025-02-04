[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shader-terrain-lit.html)
  * [中文](/cn/current/Manual/urp/shader-terrain-lit.html)
  * [日本語](/ja/current/Manual/urp/shader-terrain-lit.html)
  * [한국어](/kr/current/Manual/urp/shader-terrain-lit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shader-terrain-lit.html)
  * [中文](/cn/current/Manual/urp/shader-terrain-lit.html)
  * [日本語](/ja/current/Manual/urp/shader-terrain-lit.html)
  * [한국어](/kr/current/Manual/urp/shader-terrain-lit.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * [Shader Material Inspector window reference for URP](../urp/shaders-in-universalrp-reference.html)
  * Terrain Lit Shader Material Inspector window reference for URP

[](../urp/unlit-shader.html)

Unlit Shader Material Inspector window reference for URP

[](../urp/particles-lit-shader.html)

Particles Lit Shader Material Inspector window reference for URP

# Terrain Lit Shader Material Inspector window reference for URP

URP uses the **Terrain** The landscape in your scene. A Terrain GameObject
adds a large flat plane to your scene and you can use the Terrain’s Inspector
window to create a detailed landscape. [More info](../terrain-
UsingTerrains.html)  
See in [Glossary](../Glossary.html#Terrain) Lit **shader** A program that runs
on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) for Unity Terrain. This shader is a
simpler version of the [Lit shader](lit-shader.html). A Terrain can use a
Terrain Lit Material with up to eight [Terrain
Layers](https://docs.unity3d.com/Manual/class-TerrainLayer.html).

![A Terrain GameObject rendered with the Terrain Lit
shader.](../../uploads/urp/terrain/terrain-rendered-with-terrain-lit.png)  
_A Terrain GameObject rendered with the Terrain Lit shader._

## Properties

**Property** | **Description**  
---|---  
**Enable Height-based Blend** | Enable to have Unity take the height values from the blue channel of the **Mask Map** Texture.  
  
If you do not enable this property, Unity blends the Terrain Layers based on
the weights painted in the splatmap Textures. When you disable this property
and the Terrain Lit Shader Material is assigned to a Terrain, URP adds an
additional option **Opacity as Density Blend** for each Terrain Layer that is
added to that Terrain in the Paint Texture Tool Inspector.  
  
**Note** : Unity ignores this option when more than four Terrain Layers are on
the Terrain.  
 _Height Transition_ | Select the size in world units of the smooth transition area between Terrain Layers.  
**Enable Per-pixel Normal** | Enable to have Unity sample the normal map Texture on a per-pixel level, preserving more geometry details for distant terrain parts. Unity generates a geometry normal map at runtime from the heightmap, rather than the Mesh geometry. This means you can have high-resolution Mesh normals, even if your Mesh is low resolution.  
  
**Note** : This option only works if you enable **Draw Instanced** on the
Terrain.  
  
## Using the Paint Holes Tool

To use the **Paint Holes** tool on a Terrain, ensure that the **Terrain
Holes** check box in your project’s URP Asset is checked. Otherwise, the
Terrain holes are absent when you build the application.

[](../urp/unlit-shader.html)

Unlit Shader Material Inspector window reference for URP

[](../urp/particles-lit-shader.html)

Particles Lit Shader Material Inspector window reference for URP

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

