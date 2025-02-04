[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-MultipleProgramVariants-shortcuts.html)
  * [中文](/cn/current/Manual/SL-MultipleProgramVariants-shortcuts.html)
  * [日本語](/ja/current/Manual/SL-MultipleProgramVariants-shortcuts.html)
  * [한국어](/kr/current/Manual/SL-MultipleProgramVariants-shortcuts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-MultipleProgramVariants-shortcuts.html)
  * [中文](/cn/current/Manual/SL-MultipleProgramVariants-shortcuts.html)
  * [日本語](/ja/current/Manual/SL-MultipleProgramVariants-shortcuts.html)
  * [한국어](/kr/current/Manual/SL-MultipleProgramVariants-shortcuts.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * [Built-in keywords](shaders-keywords-built-in.html)
  * Add built-in keyword sets

[](shader-keywords-default.html)

Default shader keywords

[](writing-shader-tags.html)

Configure when and if Unity uses a shader

# Add built-in keyword sets

You can use Unity **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) directive shortcuts to create sets of
shader keywords and variants. For example, the following example adds
`SHADOWS_DEPTH` and `SHADOWS_CUBE` keywords and variants:

    
    
    #pragma multi_compile_shadowcaster
    

## Shader directive shortcuts

Shortcut | Shader keywords Unity adds | Unity adds a variant with all the keywords off | Shader pass that uses the variants  
---|---|---|---  
`multi_compile_fog` |  `FOG_LINEAR`, `FOG_EXP`, `FOG_EXP2` | Yes | Fog  
`multi_compile_fwdadd` |  `POINT` `DIRECTIONAL` `SPOT` `POINT_COOKIE` `DIRECTIONAL_COOKIE` | No | [`PassType.ForwardAdd`](../ScriptReference/Rendering.PassType.ForwardAdd.html)  
`multi_compile_fwdadd_fullshadows` |  `POINT`, `DIRECTIONAL`, `SPOT`, `POINT_COOKIE`, `DIRECTIONAL_COOKIE`, `SHADOWS_DEPTH SHADOWS_SCREEN` `SHADOWS_CUBE SHADOWS_SOFT SHADOWS_SHADOWMASK`, `LIGHTMAP_SHADOW_MIXING` | No |  [`PassType.ForwardAdd`](../ScriptReference/Rendering.PassType.ForwardAdd.html). Adds the ability for the lights to have real-time shadows.  
`multi_compile_fwdbase` |  `DIRECTIONAL`, `LIGHTMAP_ON`, `DIRLIGHTMAP_COMBINED`, `DYNAMICLIGHTMAP_ON`, `SHADOWS_SCREEN`, `SHADOWS_SHADOWMASK`, `LIGHTMAP_SHADOW_MIXING`, `LIGHTPROBE_SH` | No |  [PassType.ForwardBase](../ScriptReference/Rendering.PassType.ForwardBase.html).  
`multi_compile_fwdbasealpha` |  `DIRECTIONAL`, `LIGHTMAP_ON`, `DIRLIGHTMAP_COMBINED`, `DYNAMICLIGHTMAP_ON`, `LIGHTMAP_SHADOW_MIXING`, `VERTEXLIGHT_ON`, `LIGHTPROBE_SH` | No | [`PassType.ForwardBase`](../ScriptReference/Rendering.PassType.ForwardBase.html)  
`multi_compile_instancing` |  `INSTANCING_ON`. Also adds `PROCEDURAL_ON` if your project uses procedural instancing. | Yes | Instancing  
`multi_compile_lightpass` |  `POINT`, `DIRECTIONAL`, `SPOT`, `POINT_COOKIE`, `DIRECTIONAL_COOKIE`, `SHADOWS_DEPTH`, `SHADOWS_SCREEN`, `SHADOWS_CUBE`, `SHADOWS_SOFT`, `SHADOWS_SHADOWMASK`, `LIGHTMAP_SHADOW_MIXING` | No | All passes that draw real-time light and shadows, except **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe).  
`multi_compile_particles` | `SOFTPARTICLES_ON` | Yes | [Particle System](class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) passes.  
`multi_compile_prepassfinal` |  `LIGHTMAP_ON`, `DIRLIGHTMAP_COMBINED`, `DYNAMICLIGHTMAP_ON`, `UNITY_HDR_ON`, `SHADOWS_SHADOWMASK`, `LIGHTPROBE_SH` | Yes | [`PassType.Deferred`](../ScriptReference/Rendering.PassType.Deferred.html)  
`multi_compile_shadowcaster` |  `SHADOWS_DEPTH`, `SHADOWS_CUBE` | No | [`PassType.ShadowCaster`](../ScriptReference/Rendering.PassType.ShadowCaster.html)  
`multi_compile_shadowcollector` |  `SHADOWS_SPLIT_SPHERES`, `SHADOWS_SINGLE_CASCADE` | Yes | Screen-space shadows.  
  
## Remove variants

You can use the `skip_variants` directive to remove keywords you don’t use.

For example, the following example adds the keywords for the
`multi_compile_fwdadd` set, but removes the `POINT` and `POINT_COOKIES`
variants.

    
    
    #pragma multi_compile_fwdadd
    #pragma skip_variants POINT POINT_COOKIE
    

Refer to [Shader variant stripping](shader-variant-stripping.html) for more
information about removing variants.

[](shader-keywords-default.html)

Default shader keywords

[](writing-shader-tags.html)

Configure when and if Unity uses a shader

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

