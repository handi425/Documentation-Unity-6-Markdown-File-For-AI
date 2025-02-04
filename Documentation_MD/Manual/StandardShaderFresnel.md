[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StandardShaderFresnel.html)
  * [中文](/cn/current/Manual/StandardShaderFresnel.html)
  * [日本語](/ja/current/Manual/StandardShaderFresnel.html)
  * [한국어](/kr/current/Manual/StandardShaderFresnel.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StandardShaderFresnel.html)
  * [中文](/cn/current/Manual/StandardShaderFresnel.html)
  * [日本語](/ja/current/Manual/StandardShaderFresnel.html)
  * [한국어](/kr/current/Manual/StandardShaderFresnel.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](shader-built-in-birp.html)
  * [Standard Shader in the Built-In Render Pipeline](shader-StandardShader-landing.html)
  * [Configuring material properties in the Standard Shader in the Built-In Render Pipeline](StandardShaderChangeProperties.html)
  * Configure edge reflections (Fresnel effect)

[](StandardShaderMaterialParameterMetallic.html)

Configure reflections with the Standard Shader

[](StandardShaderMaterialParameterSpecular.html)

Configure specular reflections in the Standard Shader

# Configure edge reflections (Fresnel effect)

One important visual cue of objects in the real world has to do with how they
become more reflective at grazing angles (illustrated below). This is called
the **Fresnel effect** An effect representing the increase in reflectivity on
objects when light hits at grazing angles.  
See in [Glossary](Glossary.html#FresnelEffect).

![The fresnel effect visible at grazing angles in relation to the viewer is
increasingly apparent as the surface of a material becomes
smoother](../uploads/Main/StandardShaderFresnelGraduationTable.jpg) The
fresnel effect visible at grazing angles in relation to the viewer is
increasingly apparent as the surface of a material becomes smoother

There are two things to note in this example; firstly, these reflections only
appear around the edges of the sphere (that’s when its surface is at a grazing
angle), and also that they become more visible and sharper as the smoothness
of the material goes up.

In the Standard **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) there is no direct control over the
Fresnel effect. Instead it is indirectly controlled through the smoothness of
the material. Smooth surfaces will present a stronger Fresnel, totally rough
surfaces will have no Fresnel.

[](StandardShaderMaterialParameterMetallic.html)

Configure reflections with the Standard Shader

[](StandardShaderMaterialParameterSpecular.html)

Configure specular reflections in the Standard Shader

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

