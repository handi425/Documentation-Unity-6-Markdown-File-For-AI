[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dots-instancing-shaders-macros.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-macros.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-macros.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-macros.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dots-instancing-shaders-macros.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-macros.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-macros.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-macros.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
  * DOTS Instancing shader macros reference for URP

[](dots-instancing-shaders-unity-dots-instanced-prop.html)

Example of using UNITY_DOTS_INSTANCED_PROP macros in a DOTS Instancing shader
in URP

[](dots-instancing-shaders-functions.html)

DOTS Instancing shader functions reference for URP

# DOTS Instancing shader macros reference for URP

Unity provides the following access macros:

**Access macro** | **Description**  
---|---  
`UNITY_ACCESS_DOTS_INSTANCED_PROP(PropertyType, PropertyName)` | Returns the value loaded from `unity_DOTSInstanceData`. Refer to [Declare DOTS Instancing properties in a custom shader](dots-instancing-shaders-declare.html) for more information. **Shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that Unity provides use this version
for DOTS Instanced built-in properties that don’t have a default value to fall
back on.  
`UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_DEFAULT(PropertyType, PropertyName)` | Returns the same as `UNITY_ACCESS_DOTS_INSTANCED_PROP`, except if the most significant bit of the metadata value is zero, it returns a default value. The default value is the value of the regular material property with the same name as the DOTS Instanced property, which is why Shaders that Unity provides use the convention where DOTS Instanced properties have the same name as regular material properties. When using the default value, the access macro doesn’t access `unity_DOTSInstanceData` at all. Shaders that Unity provides use this access macro for DOTS Instanced material properties, so the loads fall back to the value set on the material.  
`UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_CUSTOM_DEFAULT(PropertyType, PropertyName, DefaultValue)` | Returns the same as `UNITY_ACCESS_DOTS_INSTANCED_PROP` unless the most significant bit of the metadata value is zero, in which case this macroreturns `DefaultValue` instead, and doesn’t access `unity_DOTSInstanceData`.  
`UNITY_DOTS_INSTANCED_METADATA_NAME(PropertyType, PropertyName)` | Returns the metadata value directly without accessing anything. This is useful for custom instance data loading schemes.  
  
[](dots-instancing-shaders-unity-dots-instanced-prop.html)

Example of using UNITY_DOTS_INSTANCED_PROP macros in a DOTS Instancing shader
in URP

[](dots-instancing-shaders-functions.html)

DOTS Instancing shader functions reference for URP

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

