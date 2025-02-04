[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SinglePassInstancing.html)
  * [中文](/cn/current/Manual/SinglePassInstancing.html)
  * [日本語](/ja/current/Manual/SinglePassInstancing.html)
  * [한국어](/kr/current/Manual/SinglePassInstancing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SinglePassInstancing.html)
  * [中文](/cn/current/Manual/SinglePassInstancing.html)
  * [日本語](/ja/current/Manual/SinglePassInstancing.html)
  * [한국어](/kr/current/Manual/SinglePassInstancing.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR graphics](xr-graphics.html)
  * [Stereo rendering](SinglePassStereoRendering.html)
  * Single-pass instanced rendering and custom shaders

[](SinglePassStereoRendering.html)

Stereo rendering

[](xr-foveated-rendering.html)

Foveated rendering

# Single-pass instanced rendering and custom shaders

URP, HDRP, ShaderGraph, Surface **shaders** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), and built-in shaders already support
single-pass stereo instanced rendering. However, shaders from the **Asset
Store** A growing library of free and commercial assets created by Unity and
members of the community. Offers a wide variety of assets, from textures,
models and animations to whole project examples, tutorials and Editor
extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore), from other third parties, or
those that you have written yourself might need to be updated.

For more information about supporting instanced rendering in your shaders, see
[GPU Instancing](GPUInstancing.html). The information in this section
specifically talks about stereo rendering and might not include all changes
you need to make to support instanced rendering in general.

## Update the vertex input attributes struct

Add the `UNITY_VERTEX_INPUT_INSTANCE_ID` macro to the `appdata` struct.

Example:

    
    
    struct appdata
    {
        float4 vertex : POSITION;
        float2 uv : TEXCOORD0;
    
        UNITY_VERTEX_INPUT_INSTANCE_ID //Insert
    };
    

## Update the vertex output attributes struct

Add `UNITY_VERTEX_OUTPUT_STEREO` macro to the `v2f` output struct.

Example:

    
    
    struct v2f
    {
        float2 uv : TEXCOORD0;
        float4 vertex : SV_POSITION;
    
        UNITY_VERTEX_OUTPUT_STEREO //Insert
    };
    

## Update the main vertex shader function

Add the following macros to the beginning of your main `vert` method (in
order):

  1. `UNITY_SETUP_INSTANCE_ID()`
  2. `UNITY_INITIALIZE_OUTPUT(v2f, o)`
  3. `UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO()`

`UNITY_SETUP_INSTANCE_ID()` calculates and sets the built-in
`unity_StereoEyeIndex` and `unity_InstanceID` shader variables to the correct
values based on which eye the GPU is currently rendering.

`UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO` tells the GPU which eye in the texture
array it should render to, based on the value of `unity_StereoEyeIndex`. This
macro also transfers the value of `unity_StereoEyeIndex` from the **vertex
shader** A program that runs on each vertex of a 3D model when the model is
being rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader) so that it will be accessible in
the fragment shader only if `UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX` is
called in the fragment shader `frag` method.

`UNITY_INITALIZE_OUTPUT(v2f,o)` initializes all `v2f` values to 0.

Example:

    
    
    v2f vert (appdata v)
    {
        v2f o;
    
        UNITY_SETUP_INSTANCE_ID(v); //Insert
        UNITY_INITIALIZE_OUTPUT(v2f, o); //Insert
        UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o); //Insert
    
        o.vertex = UnityObjectToClipPos(v.vertex);
    
        o.uv = v.uv;
    
        return o;
    }
    

## Post-Processing shaders

If you want your **Post-Processing** A process that improves product visuals
by applying filters and effects before the image appears on screen. You can
use post-processing effects to simulate physical camera and film properties,
for example Bloom and Depth of Field. [More info](PostProcessingOverview.html)
post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) shaders to support single-
pass stereo instancing, follow the steps for custom shaders as well as the
steps below.

**Note:** You can download all Unity base shader **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) from the [Unity
website](https://unity3d.com/get-unity/download/archive).

Do the following for each Post-Processing shader that you want to support
single-pass instancing:

  1. Add the UNITY_DECLARE_SCREENSPACE_TEXTURE(tex) macro outside the frag method (see the example below for placement) in your Shader script, so that when you use a particular stereo rendering method the GPU uses the appropriate texture sampler. For example, if you use multi-pass rendering, the GPU uses a texture 2D sampler. For single-pass instancing or multi-view rendering, the texture sampler is a texture array.

  2. Add `UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(i)` at the beginning of the fragment shader frag method (See the example below for placement). You only need to add this macro if you want to use the `unity_StereoEyeIndex` built-in shader variable to find out which eye the GPU is rendering to. This is useful when testing post-processing effects.

  3. Use the `UNITY_SAMPLE_SCREENSPACE_TEXTURE()` macro when sampling 2D textures (See the example below). Standard shaders use a 2D texture-based back buffer to sample textures. Single-pass stereo instancing does not use this type of back buffer, so if you do not specify a different method for 2D texture sampling, your shader does not render correctly. To prevent rendering issues, the `UNITY_SAMPLE_SCREENSPACE_TEXTURE()` macro detects which stereo **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) you are using and then
automatically samples the texture in the correct manner. See Unity
documentation on [HLSLSupport.cginc](SL-BuiltinIncludes.html) to learn more
about similar macros used for depth textures and screen-space shadow maps.

Example:

    
    
    UNITY_DECLARE_SCREENSPACE_TEXTURE(_MainTex); //Insert
    
    fixed4 frag (v2f i) : SV_Target
    {
        UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(i); //Insert
        
        fixed4 col = UNITY_SAMPLE_SCREENSPACE_TEXTURE(_MainTex, i.uv); //Insert
        
        // just invert the colors
        
        col = 1 - col;
        
        return col;
    }
    

## Full sample shader code

Below is a simple example of the template image effect shader with all of the
previously mentioned changes applied to support single-pass stereo instancing.
The lines added to the shader code are marked with the comment: `//Insert`.

    
    
    struct appdata
    {
        float4 vertex : POSITION;
        float2 uv : TEXCOORD0;
        
        UNITY_VERTEX_INPUT_INSTANCE_ID //Insert
    };
    
    //v2f output struct
    
    struct v2f
    {
    
        float2 uv : TEXCOORD0;
        float4 vertex : SV_POSITION;
        
        UNITY_VERTEX_OUTPUT_STEREO //Insert
    };
    
    v2f vert (appdata v)
    {
        v2f o;
        
        UNITY_SETUP_INSTANCE_ID(v); //Insert
        UNITY_INITIALIZE_OUTPUT(v2f, o); //Insert
        UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o); //Insert
        
        o.vertex = UnityObjectToClipPos(v.vertex);
        o.uv = v.uv;
        return o;
    }
    
    UNITY_DECLARE_SCREENSPACE_TEXTURE(_MainTex); //Insert
    
    fixed4 frag (v2f i) : SV_Target
    {
        UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(i); //Insert
        
        fixed4 col = UNITY_SAMPLE_SCREENSPACE_TEXTURE(_MainTex, i.uv); //Insert
        
        // invert the colors
        
        col = 1 - col;
        
        return col;
    }
    

## Procedural geometry

If you use the
[Graphics.DrawProceduralIndirect()](../ScriptReference/Graphics.DrawProcedural.html)
and
[CommandBuffer.DrawProceduralIndirect()](../ScriptReference/Graphics.DrawProceduralIndirect.html)
methods to draw fully procedural geometry on the GPU, note that both methods
receive their arguments from a compute buffer. This means that it is difficult
to increase the instance count at run time. To increase the instance count,
you must manually double the instance count contained in your compute buffers.

## Debugging your shader

The following shader code renders a **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) as green for a user’s left eye and
red for their right eye. This shader is useful for debugging your stereo
rendering, because it allows you to verify that all stereo graphics work and
are functioning correctly.

    
    
    Shader "XR/StereoEyeIndexColor"
    {
       Properties
       {
           _LeftEyeColor("Left Eye Color", COLOR) = (0,1,0,1)
           _RightEyeColor("Right Eye Color", COLOR) = (1,0,0,1)
       }
    
       SubShader
       {
          Tags { "RenderType" = "Opaque" }
    
          Pass
          {
             CGPROGRAM
    
             #pragma vertex vert
             #pragma fragment frag
    
             float4 _LeftEyeColor;
             float4 _RightEyeColor;
    
             #include "UnityCG.cginc"
    
             struct appdata
             {
                float4 vertex : POSITION;
    
                UNITY_VERTEX_INPUT_INSTANCE_ID
             };
    
             struct v2f
             {
                float4 vertex : SV_POSITION;
    
                UNITY_VERTEX_INPUT_INSTANCE_ID 
                UNITY_VERTEX_OUTPUT_STEREO
             };
    
             v2f vert (appdata v)
             {
                v2f o;
    
                UNITY_SETUP_INSTANCE_ID(v);
                UNITY_INITIALIZE_OUTPUT(v2f, o);
                UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o);
    
                o.vertex = UnityObjectToClipPos(v.vertex);
    
                return o;
             }
    
             fixed4 frag (v2f i) : SV_Target
             {
                UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(i);
    
                return lerp(_LeftEyeColor, _RightEyeColor, unity_StereoEyeIndex);
             }
             ENDCG
          }
       }
    }
    

### ShaderGraph debug shader

ShaderGraph automatically adds the macros required to support single-pass
stereo rendering. To implement the debug shader in ShaderGraph you can use a
[Custom Function
Node](https://docs.unity3d.com/Packages/com.unity.shadergraph@10.10/manual/Custom-
Function-Node.html) that sets the base color based on the eye index.

![](../uploads/Main/xr-debug-shadergraph.png)

Use the `unity_StereoEyeIndex` shader attribute to determine the base color
depending on which eye instance is being rendered. The Custom Function Node in
the example above contains the following code:

    
    
    Out = lerp(LeftColor, RightColor, unity_StereoEyeIndex);
    

[](SinglePassStereoRendering.html)

Stereo rendering

[](xr-foveated-rendering.html)

Foveated rendering

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

