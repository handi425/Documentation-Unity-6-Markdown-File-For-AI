[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StandardShaderMaterialParameterSmoothness.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterSmoothness.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterSmoothness.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterSmoothness.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StandardShaderMaterialParameterSmoothness.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterSmoothness.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterSmoothness.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterSmoothness.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](shader-built-in-birp.html)
  * [Standard Shader in the Built-In Render Pipeline](shader-StandardShader-landing.html)
  * [Configuring material properties in the Standard Shader in the Built-In Render Pipeline](StandardShaderChangeProperties.html)
  * Configure smoothness with the Standard Shader

[](StandardShaderMaterialParameterSpecular.html)

Configure specular reflections in the Standard Shader

[](StandardShaderMaterialParameterRenderingMode.html)

Set the Rendering Mode in the Standard Shader using a script

# Configure smoothness with the Standard Shader

The concept of Smoothness applies to both the Specular workflow and the
Metallic workflow, and works in very much the same way in both. By default,
without a [Metallic](StandardShaderMaterialParameterMetallic.html) or
[Specular](StandardShaderMaterialParameterSpecular.html) texture map assigned,
the smoothness of the material is controlled by a slider. This slider allows
you to control the “microsurface detail” or smoothness across a surface.

Both **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) modes are shown above, because if you
choose to use a texture map for the **Metallic** or **Specular** Property, the
smoothness values are taken from that same map. This is explained in further
detail down the page.

![A range of smoothness values from 0 to
1](../uploads/Main/StandardShaderSmoothnessGraduationTable.svg) A range of
smoothness values from 0 to 1

The “microsurface detail” is not something directly visible in Unity. It is a
concept used in the lighting calculations. You can, however, see the effect of
this microsurface detail represented by the amount the light that is diffused
as it bounces off the object. With a smooth surface, all light rays tend to
bounce off at predictable and consistent angles. Taken to its extreme, a
perfectly smooth surface reflects light like a mirror. Less smooth surfaces
reflect light over a wider range of angles (as the light hits the bumps in the
microsurface), and therefore the reflections have less detail and are spread
across the surface in a more diffuse way.

![A comparison of low, medium and high values for smoothness \(left to
right\), as a diagram of the theoretical microsurface detail of a material.
The yellow lines represent light rays hitting the surface and reflecting off
the angles encountered at varying levels of
smoothness.](../uploads/Main/StandardShaderMicrosurfaceDiagram.svg) A
comparison of low, medium and high values for smoothness (left to right), as a
diagram of the theoretical microsurface detail of a material. The yellow lines
represent light rays hitting the surface and reflecting off the angles
encountered at varying levels of smoothness.

A smooth surface has very low microsurface detail, or none at all, so light
bounces off in uniform ways, creating clear reflections. A rough surface has
high peaks and troughs in its microsurface detail, so light bounces off in a
wide range of angles which, when averaged out, create a diffuse colour with no
clear reflections.

![A comparison of low, medium and high values for smoothness \(top to
bottom\).](../uploads/Main/StandardShaderEnergyConservation.jpg) A comparison
of low, medium and high values for smoothness (top to bottom).

At low smoothness levels, the reflected light at each point on the surface
comes from a wide area, because the microsurface detail is bumpy and scatters
light. At high values of smoothness, the light at each point comes from a
narrowly focused area, giving a much clearer reflection of the object’s
environment.

## Use a Smoothness Texture Map

In a similar way to many of the other Properties, you can assign a texture map
instead of using a single slider value. This allows you greater control over
the strength and colour of the specular light reflections across the surface
of the material.

Using a map instead of a slider means you can create materials which include a
variety of smoothness levels across the surface (usually designed to match
what is shown in the albedo texture).

Smoother surfaces are more reflective and have smaller, more tightly-focused
specular highlights. Less smooth surfaces do not reflect as much, so specular
highlights are less noticable and spread wider across the surface. By matching
the specular and smoothness maps to the content in your albedo map, you can
begin to create very realistic-looking textures.

[](StandardShaderMaterialParameterSpecular.html)

Configure specular reflections in the Standard Shader

[](StandardShaderMaterialParameterRenderingMode.html)

Set the Rendering Mode in the Standard Shader using a script

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

