[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Android-SinglePassStereoRendering.html)
  * [中文](/cn/current/Manual/Android-SinglePassStereoRendering.html)
  * [日本語](/ja/current/Manual/Android-SinglePassStereoRendering.html)
  * [한국어](/kr/current/Manual/Android-SinglePassStereoRendering.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Android-SinglePassStereoRendering.html)
  * [中文](/cn/current/Manual/Android-SinglePassStereoRendering.html)
  * [日本語](/ja/current/Manual/Android-SinglePassStereoRendering.html)
  * [한국어](/kr/current/Manual/Android-SinglePassStereoRendering.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Graphics for Android](android-graphics.html)
  * Single-pass stereo rendering for Android

[](android-screen-configuration.html)

Screen configuration

[](vulkan-swapchain-pre-rotation.html)

Framebuffer orientation

# Single-pass stereo rendering for Android

Unity supports [single-pass stereo rendering](SinglePassInstancing.html) for
Android devices that support multiview. Multiview consists of the
[GL_OVR_multiview2](https://www.khronos.org/registry/OpenGL/extensions/OVR/OVR_multiview2.txt)
and
[GL_OVR_multiview_multisampled_render_to_texture](https://www.khronos.org/registry/OpenGL/extensions/OVR/OVR_multiview_multisampled_render_to_texture.txt)
OpenGL ES extensions. These extensions require **shaders** A program that runs
on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) to use a 2D texture array that
consists of two slices, one slice per eye.

## Shader code requirements

To use single-pass stereo rendering with custom shaders, you may need to
include additional shader code. You don’t need to include additional code if
your custom shaders are:

  * **Surface Shaders** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) that don’t have custom vertex
processing.

  * Fixed-function pipeline shaders.

**Note** : These shader changes are compatible with multi-pass stereo
rendering.

### Modify your shaders

If you want to use the `unity_StereoEyeIndex` built-in shader variable to know
which eye the GPU is rendering to, you must declare
`UNITY_VERTEX_OUTPUT_STEREO` in any shader stage output structs that you have.
For example:

    
    
    struct v2f {
        float2 uv : TEXCOOR0;
        float4 vertex : SV_POSITION;
        UNITY_VERTEX_OUTPUT_STEREO
    };
    

To initialize the output data, use `UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO()`
in the **vertex shader** A program that runs on each vertex of a 3D model when
the model is being rendered. [More info](writing-shader-writing-shader-
programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader) function. For example:

    
    
    v2f vert (appdata v)
    {
        v2f o;
        UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o);
        o.vertex = UnityObjectToClipPos(v.vertex);
        o.uv = TRANSFORM_TEX(v.uv, _MainTex);
        return o;
    }
    

To initialize `unity_StereoEyeIndex` in subsequent stages, add
`UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX()` at the beginning. For example:

    
    
    fixed4 frag (v2f i) : SV_Target
    {
        UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(i);
        // sample the texture
        fixed4 col = tex2D(_MainTex, i.uv);
        // apply fog
        UNITY_APPLY_FOG(i.fogCoord, col);
        return col;
    }
    

If your shaders use other shader stages, use the
`UNITY_TRANSFER_VERTEX_OUTPUT_STEREO()` macro to transfer the eye index to the
subsequent stages.

**Tip** : To calculate the final position of the object, it’s best practice to
use `UnityObjectToClipPos(IN.vertex)` instead of `mul(UNITY_MATRIX_MVP,
IN.vertex)`.

## Post-Processing Shaders

You must update **post-processing** A process that improves product visuals by
applying filters and effects before the image appears on screen. You can use
post-processing effects to simulate physical camera and film properties, for
example Bloom and Depth of Field. [More info](PostProcessingOverview.html)
post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) shaders to deal with the eye
textures being a 2D texture array. To help with this, Unity includes the
`UNITY_DECLARE_SCREENSPACE_TEXTURE()` macro. To make textures work in both
multi-pass and single-pass modes, wrap each textures in this macro. Also, when
you sample the texture, use the `UNITY_SAMPLE_SCREENSPACE_TEXTURE()` macro.

This macro requires that you call `UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX()`
beforehand when in single-pass mode. Unity also includes similar macros for
depth textures and screen space shadow maps. You can see the full list at the
bottom of `HLSLSupport.cginc`.

[](android-screen-configuration.html)

Screen configuration

[](vulkan-swapchain-pre-rotation.html)

Framebuffer orientation

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

