[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/decal-shader.html)
  * [中文](/cn/current/Manual/urp/decal-shader.html)
  * [日本語](/ja/current/Manual/urp/decal-shader.html)
  * [한국어](/kr/current/Manual/urp/decal-shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/decal-shader.html)
  * [中文](/cn/current/Manual/urp/decal-shader.html)
  * [日本語](/ja/current/Manual/urp/decal-shader.html)
  * [한국어](/kr/current/Manual/urp/decal-shader.html)

  * [Visual effects](../visual-effects.html)
  * [Decals and projectors](../visual-effects-decals.html)
  * [Decals in URP](../urp/renderer-feature-decal-landing.html)
  * Create a decal via a Decal Projector in URP

[](../urp/renderer-feature-decal-create.html)

Create a decal via a Decal Renderer Feature in URP

[](../urp/renderer-feature-decal-reference.html)

Decal Renderer Feature reference

# Create a decal via a Decal Projector in URP

The [Decal Projector](renderer-feature-decal-projector-reference.html)
component can project a Material as a decal if the Material uses a **Shader**
A program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) Graph with the Decal Material type.

![Shader Graph with the Decal Material type](../../uploads/urp/decal/decal-
shader-graph-material-type.png)  
_Shader Graph with the Decal Material type_

URP contains the pre-built Decal Shader (`Shader Graphs/Decal`).

![Decal Material properties.](../../uploads/urp/decal/decal-material-
properties.png)  
_Decal Material properties and advanced options._

##  Create custom Decal shaders

The pre-built `Shader Graphs/Decal` shader serves as a simple example. You can
create your own decal shaders that render decals in a way that suits your
project best.

To create a custom decal Shader Graph, select the **Decal** value in Material
property of the shader target.

![Shader Graph, Decal Material](../../uploads/urp/decal/decal-shader-graph-
material-type.png) Shader Graph, Decal Material

Enabling one of the following properties override the equivalent Lit Shader
property on the surface of the Material.

To improve performance, pack data for different surface properties into a
single texture. This way the shader performs fewer samples and Unity stores
fewer textures.

For example, the following Shader Graph uses a **normal map** A type of Bump
Map texture that allows you to add surface detail such as bumps, grooves, and
scratches to a model which catch the light as if they are represented by real
geometry.  
See in [Glossary](../Glossary.html#Normalmap) and a mask map to drive all
properties in the shader. This decal is used for the damaged tarmac effect,
and a hardcoded roughness value of 0 suites the use case.

![Decal Graph](../../uploads/urp/decal/decal-graph.png) Decal Graph

The shader samples the mask and uses the color for setting the Ambient
Occlusion values (Red channel), smoothness values (Green channel), Emission
intensity values (Blue channel), and alpha values for the entire decal. Decals
are often blended using single alpha values for all properties. The following
image shows the mask map for the example tarmac cracks:  
![Decal Mask](../../uploads/urp/decal/decal-mask.png)  
_Example of mask map that packs Ambient Occlusion, Smoothness, Emission, and
alpha values of a decal atlas into a single texture._

[](../urp/renderer-feature-decal-create.html)

Create a decal via a Decal Renderer Feature in URP

[](../urp/renderer-feature-decal-reference.html)

Decal Renderer Feature reference

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

