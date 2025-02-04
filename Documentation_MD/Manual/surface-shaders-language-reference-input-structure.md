[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/surface-shaders-language-reference-input-structure.html)
  * [中文](/cn/current/Manual/surface-shaders-language-reference-input-structure.html)
  * [日本語](/ja/current/Manual/surface-shaders-language-reference-input-structure.html)
  * [한국어](/kr/current/Manual/surface-shaders-language-reference-input-structure.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/surface-shaders-language-reference-input-structure.html)
  * [中文](/cn/current/Manual/surface-shaders-language-reference-input-structure.html)
  * [日本語](/ja/current/Manual/surface-shaders-language-reference-input-structure.html)
  * [한국어](/kr/current/Manual/surface-shaders-language-reference-input-structure.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader language reference for the Built-In Render Pipeline](surface-shaders-language-reference.html)
  * Surface Shader input structure reference for the Built-In Render Pipeline

[](surface-shaders-language-reference-optional-directives.html)

Surface Shader optional directives reference for the Built-In Render Pipeline

[](use-built-in-shader-methods-birp.html)

Shader methods in the Built-In Render Pipeline

# Surface Shader input structure reference for the Built-In Render Pipeline

The input structure `Input` generally has any texture coordinates needed by
the **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). Texture coordinates must be named
“`uv`” followed by texture name (or start it with “`uv2`” to use second
texture coordinate set).

Additional values that can be put into Input structure:

  * `float3 viewDir` \- contains view direction, for computing Parallax effects, rim lighting etc.
  * `float4` with `COLOR` semantic - contains interpolated per-vertex color.
  * `float4 screenPos` \- contains screen space position for reflection or screenspace effects. Note that this is not suitable for [GrabPass](SL-GrabPass.html); you need to compute custom UV yourself using `ComputeGrabScreenPos` function.
  * `float3 worldPos` \- contains world space position.
  * `float3 worldRefl` \- contains world reflection vector _if**surface shader** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) does not write to o.Normal_.
See Reflect-Diffuse shader for example.

  * `float3 worldNormal` \- contains world normal vector _if surface shader does not write to o.Normal_.
  * `float3 worldRefl; INTERNAL_DATA` \- contains world reflection vector _if surface shader writes to o.Normal_. To get the reflection vector based on per-pixel **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap), use `WorldReflectionVector (IN,
o.Normal)`. See Reflect-Bumped shader for example.

  * `float3 worldNormal; INTERNAL_DATA` \- contains world normal vector _if surface shader writes to o.Normal_. To get the normal vector based on per-pixel normal map, use `WorldNormalVector (IN, o.Normal)`.

[](surface-shaders-language-reference-optional-directives.html)

Surface Shader optional directives reference for the Built-In Render Pipeline

[](use-built-in-shader-methods-birp.html)

Shader methods in the Built-In Render Pipeline

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

