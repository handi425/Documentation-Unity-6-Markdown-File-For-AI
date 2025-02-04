[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/material-validator-make-shader-compatible.html)
  * [中文](/cn/current/Manual/material-validator-make-shader-compatible.html)
  * [日本語](/ja/current/Manual/material-validator-make-shader-compatible.html)
  * [한국어](/kr/current/Manual/material-validator-make-shader-compatible.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/material-validator-make-shader-compatible.html)
  * [中文](/cn/current/Manual/material-validator-make-shader-compatible.html)
  * [日本語](/ja/current/Manual/material-validator-make-shader-compatible.html)
  * [한국어](/kr/current/Manual/material-validator-make-shader-compatible.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Materials](Materials.html)
  * [Material Validator in the Built-In Render Pipeline](materials-troubleshooting.html)
  * Make a shader compatible with the Material Validator in the Built-In Render Pipeline

[](material-validator-validate.html)

Validate and correct materials in the Built-In Render Pipeline

[](MaterialValidator.html)

Material Validator window reference for the Built-In Render Pipeline

# Make a shader compatible with the Material Validator in the Built-In Render
Pipeline

The Material Validator works with any Materials that use Unity’s [Standard
shader](shader-StandardShader.html) or [surface shaders](SL-
SurfaceShaders.html)A streamlined way of writing shaders for the Built-in
Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader). However, custom **shaders** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) require a pass named `“META”`. Most
custom shaders that support lightmapping already have this pass defined. See
documentation on [Lightmapping and shaders](MetaPass.html) for more details.

Carry out the following steps to make your custom shader compatible with the
Material Validator:

  1. Add the following pragma to the meta pass: `#pragma shader_feature EDITOR_VISUALIZATION`
  2. In the `UnityMetaInput` structure, assign the **specular color** The color of a specular highlight.  
See in [Glossary](Glossary.html#specularcolor) of the Material to the field
called `SpecularColor`, as shown in the code example below.

Here is an example of a custom meta pass:

    
    
    Pass
    {
        Name "META" 
        Tags { "LightMode"="Meta" }
    
        Cull Off
    
        CGPROGRAM
        #pragma vertex vert_meta
        #pragma fragment frag_meta
    
        #pragma shader_feature _EMISSION
        #pragma shader_feature _METALLICGLOSSMAP
        #pragma shader_feature _ _SMOOTHNESS_TEXTURE_ALBEDO_CHANNEL_A
        #pragma shader_feature ___ _DETAIL_MULX2
        #pragma shader_feature EDITOR_VISUALIZATION
    
        float4 frag_meta(v2f_meta i) : SV_TARGET
        {
            UnityMetaInput input;
            UNITY_INITIALIZE_OUTPUT(UnityMetaInput, input);
            float4 materialSpecularColor = float4(1.0f, 0.0f, 0.0f, 1.0f);
            float4 materialAlbedo = float4(0.0f, 1.0f, 0.0f, 1.0f);
            input.SpecularColor = materialSpecularColor;
            input.Albedo = materialAlbedo;
    
            return UnityMetaFragment(input);
        }  
    }
    

[](material-validator-validate.html)

Validate and correct materials in the Built-In Render Pipeline

[](MaterialValidator.html)

Material Validator window reference for the Built-In Render Pipeline

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

