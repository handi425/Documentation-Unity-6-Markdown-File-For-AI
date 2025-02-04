[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# BuiltinShaderDefine

enumeration

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Defines set by editor when compiling shaders, based on the target platform and
[GraphicsTier](Rendering.GraphicsTier.html).

Additional resources:
[GraphicsSettings.HasShaderDefine](Rendering.GraphicsSettings.HasShaderDefine.html).

### Properties

[UNITY_NO_DXT5nm](Rendering.BuiltinShaderDefine.UNITY_NO_DXT5nm.html)|
UNITY_NO_DXT5nm is set when compiling shader for platform that do not support
DXT5NM, meaning that normal maps will be encoded in RGB instead.  
---|---  
[UNITY_NO_RGBM](Rendering.BuiltinShaderDefine.UNITY_NO_RGBM.html)|
UNITY_NO_RGBM is set when compiling shader for platform that do not support
RGBM, so dLDR will be used instead.  
[UNITY_ENABLE_REFLECTION_BUFFERS](Rendering.BuiltinShaderDefine.UNITY_ENABLE_REFLECTION_BUFFERS.html)|
UNITY_ENABLE_REFLECTION_BUFFERS is set when deferred shading renders
reflection probes in deferred mode. With this option set reflections are
rendered into a per-pixel buffer. This is similar to the way lights are
rendered into a per-pixel buffer. UNITY_ENABLE_REFLECTION_BUFFERS is on by
default when using deferred shading, but you can turn it off by setting “No
support” for the Deferred Reflections shader option in Graphics Settings. When
the setting is off, reflection probes are rendered per-object, similar to the
way forward rendering works.  
[UNITY_FRAMEBUFFER_FETCH_AVAILABLE](Rendering.BuiltinShaderDefine.UNITY_FRAMEBUFFER_FETCH_AVAILABLE.html)|
UNITY_FRAMEBUFFER_FETCH_AVAILABLE is set when compiling shaders for platforms
where framebuffer fetch is potentially available.  
[UNITY_ENABLE_NATIVE_SHADOW_LOOKUPS](Rendering.BuiltinShaderDefine.UNITY_ENABLE_NATIVE_SHADOW_LOOKUPS.html)|
UNITY_ENABLE_NATIVE_SHADOW_LOOKUPS enables use of built-in shadow comparison
samplers on OpenGL ES 2.0.  
[UNITY_METAL_SHADOWS_USE_POINT_FILTERING](Rendering.BuiltinShaderDefine.UNITY_METAL_SHADOWS_USE_POINT_FILTERING.html)|
UNITY_METAL_SHADOWS_USE_POINT_FILTERING is set if shadow sampler should use
point filtering on iOS Metal.  
[UNITY_NO_SCREENSPACE_SHADOWS](Rendering.BuiltinShaderDefine.UNITY_NO_SCREENSPACE_SHADOWS.html)|
UNITY_NO_SCREENSPACE_SHADOWS is set when screenspace cascaded shadow maps are
disabled.  
[UNITY_USE_DITHER_MASK_FOR_ALPHABLENDED_SHADOWS](Rendering.BuiltinShaderDefine.UNITY_USE_DITHER_MASK_FOR_ALPHABLENDED_SHADOWS.html)|
UNITY_USE_DITHER_MASK_FOR_ALPHABLENDED_SHADOWS is set when Semitransparent
Shadows are enabled.  
[UNITY_PBS_USE_BRDF1](Rendering.BuiltinShaderDefine.UNITY_PBS_USE_BRDF1.html)|
UNITY_PBS_USE_BRDF1 is set if Standard Shader BRDF1 should be used.  
[UNITY_PBS_USE_BRDF2](Rendering.BuiltinShaderDefine.UNITY_PBS_USE_BRDF2.html)|
UNITY_PBS_USE_BRDF2 is set if Standard Shader BRDF2 should be used.  
[UNITY_PBS_USE_BRDF3](Rendering.BuiltinShaderDefine.UNITY_PBS_USE_BRDF3.html)|
UNITY_PBS_USE_BRDF3 is set if Standard Shader BRDF3 should be used.  
[UNITY_SPECCUBE_BOX_PROJECTION](Rendering.BuiltinShaderDefine.UNITY_SPECCUBE_BOX_PROJECTION.html)|
UNITY_SPECCUBE_BLENDING is set if Reflection Probes Box Projection is enabled.  
[UNITY_SPECCUBE_BLENDING](Rendering.BuiltinShaderDefine.UNITY_SPECCUBE_BLENDING.html)|
UNITY_SPECCUBE_BLENDING is set if Reflection Probes Blending is enabled.  
[UNITY_ENABLE_DETAIL_NORMALMAP](Rendering.BuiltinShaderDefine.UNITY_ENABLE_DETAIL_NORMALMAP.html)|
UNITY_ENABLE_DETAIL_NORMALMAP is set if Detail Normal Map should be sampled if
assigned.  
[SHADER_API_MOBILE](Rendering.BuiltinShaderDefine.SHADER_API_MOBILE.html)|
SHADER_API_MOBILE is set when compiling shader for mobile platforms.  
[SHADER_API_DESKTOP](Rendering.BuiltinShaderDefine.SHADER_API_DESKTOP.html)|
SHADER_API_DESKTOP is set when compiling shader for "desktop" platforms.  
[UNITY_HARDWARE_TIER1](Rendering.BuiltinShaderDefine.UNITY_HARDWARE_TIER1.html)|
UNITY_HARDWARE_TIER1 is set when compiling shaders for GraphicsTier.Tier1.  
[UNITY_HARDWARE_TIER2](Rendering.BuiltinShaderDefine.UNITY_HARDWARE_TIER2.html)|
UNITY_HARDWARE_TIER2 is set when compiling shaders for GraphicsTier.Tier2.  
[UNITY_HARDWARE_TIER3](Rendering.BuiltinShaderDefine.UNITY_HARDWARE_TIER3.html)|
UNITY_HARDWARE_TIER3 is set when compiling shaders for GraphicsTier.Tier3.  
[UNITY_COLORSPACE_GAMMA](Rendering.BuiltinShaderDefine.UNITY_COLORSPACE_GAMMA.html)|
UNITY_COLORSPACE_GAMMA is set when compiling shaders for Gamma Color Space.  
[UNITY_LIGHT_PROBE_PROXY_VOLUME](Rendering.BuiltinShaderDefine.UNITY_LIGHT_PROBE_PROXY_VOLUME.html)|
UNITY_LIGHT_PROBE_PROXY_VOLUME is set when Light Probe Proxy Volume feature is
supported by the current graphics API and is enabled in the Graphics Tier
settings. You can only set a Graphics Tier in the Built-in Render Pipeline.  
[UNITY_LIGHTMAP_DLDR_ENCODING](Rendering.BuiltinShaderDefine.UNITY_LIGHTMAP_DLDR_ENCODING.html)|
UNITY_LIGHTMAP_DLDR_ENCODING is set when lightmap textures are using double
LDR encoding to store the values in the texture.  
[UNITY_LIGHTMAP_RGBM_ENCODING](Rendering.BuiltinShaderDefine.UNITY_LIGHTMAP_RGBM_ENCODING.html)|
UNITY_LIGHTMAP_RGBM_ENCODING is set when lightmap textures are using RGBM
encoding to store the values in the texture.  
[UNITY_LIGHTMAP_FULL_HDR](Rendering.BuiltinShaderDefine.UNITY_LIGHTMAP_FULL_HDR.html)|
UNITY_LIGHTMAP_FULL_HDR is set when lightmap textures are not using any
encoding to store the values in the texture.  
[UNITY_VIRTUAL_TEXTURING](Rendering.BuiltinShaderDefine.UNITY_VIRTUAL_TEXTURING.html)|
Is virtual texturing enabled and supported on this platform.  
[UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION](Rendering.BuiltinShaderDefine.UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION.html)|
Unity enables UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION when Vulkan pre-
transform is enabled and supported on the target build platform.  
[UNITY_ASTC_NORMALMAP_ENCODING](Rendering.BuiltinShaderDefine.UNITY_ASTC_NORMALMAP_ENCODING.html)|
Unity enables UNITY_ASTC_NORMALMAP_ENCODING when DXT5nm-style normal maps are
used on Android, iOS or tvOS.  
[SHADER_API_GLES30](Rendering.BuiltinShaderDefine.SHADER_API_GLES30.html)|
SHADER_API_ES30 is set when the Graphics API is OpenGL ES 3 and the minimum
supported OpenGL ES 3 version is OpenGL ES 3.0.  
[UNITY_UNIFIED_SHADER_PRECISION_MODEL](Rendering.BuiltinShaderDefine.UNITY_UNIFIED_SHADER_PRECISION_MODEL.html)|
Unity sets UNITY_UNIFIED_SHADER_PRECISION_MODEL if, in Player Settings, you
set Shader Precision Model to Unified.  
[UNITY_PLATFORM_SUPPORTS_WAVE_32](Rendering.BuiltinShaderDefine.UNITY_PLATFORM_SUPPORTS_WAVE_32.html)|
Unity sets UNITY_PLATFORM_SUPPORTS_WAVE_32 when the target platform is known
to support wave-level shader operations with a wave size of 32.  
[UNITY_PLATFORM_SUPPORTS_WAVE_64](Rendering.BuiltinShaderDefine.UNITY_PLATFORM_SUPPORTS_WAVE_64.html)|
Unity sets UNITY_PLATFORM_SUPPORTS_WAVE_64 when the target platform is known
to support wave-level shader operations with a wave size of 64.  
[UNITY_NEEDS_RENDERPASS_FBFETCH_FALLBACK](Rendering.BuiltinShaderDefine.UNITY_NEEDS_RENDERPASS_FBFETCH_FALLBACK.html)|
UNITY_NEEDS_RENDERPASS_FBFETCH_FALLBACK is set when we need to generate a
fallback for RenderPass due to the possibility of not having framebuffer fetch  
[UNITY_PLATFORM_SUPPORTS_DEPTH_FETCH](Rendering.BuiltinShaderDefine.UNITY_PLATFORM_SUPPORTS_DEPTH_FETCH.html)|
UNITY_PLATFORM_SUPPORTS_DEPTH_FETCH is set if RenderPass can use its depth
attachment as input.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

