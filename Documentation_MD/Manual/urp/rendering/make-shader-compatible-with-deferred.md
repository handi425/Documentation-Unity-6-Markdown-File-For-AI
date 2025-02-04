[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
  * [中文](/cn/current/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
  * [日本語](/ja/current/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
  * [한국어](/kr/current/Manual/urp/rendering/make-shader-compatible-with-deferred.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
  * [中文](/cn/current/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
  * [日本語](/ja/current/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
  * [한국어](/kr/current/Manual/urp/rendering/make-shader-compatible-with-deferred.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Get started with URP](../../urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](../../urp/urp-concepts.html)
  * [Rendering paths in URP](../../urp/rendering-paths-landing.html)
  * [Deferred rendering path in URP](../../urp/rendering/deferred-rendering-path-landing.html)
  * Make a shader compatible with the Deferred rendering path in URP

[](../../urp/rendering/accurate-g-buffer-normals.html)

Enable accurate G-buffer normals in the Deferred rendering path in URP

[](../../urp/rendering/forward-plus-rendering-path-limitations.html)

Troubleshooting the Forward+ rendering path in URP

# Make a shader compatible with the Deferred rendering path in URP

## Use a shader in the Deferred rendering path

To use a **shader** A program that runs on the GPU. [More
info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) in the Deferred **rendering
path** The technique that a render pipeline uses to render graphics. Choosing
a different rendering path affects how lighting and shading are calculated.
Some rendering paths are more suited to different platforms and hardware than
others. [More info](../../RenderingPaths.html)  
See in [Glossary](../../Glossary.html#RenderingPath), add the
`UniversalGBuffer` tag to the Pass in your **ShaderLab** Unity’s language for
defining the structure of Shader objects. [More info](../../SL-Shader.html)  
See in [Glossary](../../Glossary.html#ShaderLab) code. Unity executes the
shader during the G-buffer render pass.

For example:

    
    
    Shader "Examples/ExamplePassFlag"
    {
        SubShader
        {
            Pass
            {    
                  Tags
                  { 
                    "RenderPipeline" = "UniversalPipeline"
                    "LightMode" = "UniversalGBuffer"
                  }
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Use a shader in the forward pass of the Deferred rendering path

To use a shader in the Deferred rendering path, add the `UniversalForwardOnly`
and `DepthNormalsOnly` tags to the Pass in your ShaderLab code. Unity executes
the shader during the G-buffer render pass.

For example:

    
    
    Shader "Examples/ExamplePassFlag"
    {
        SubShader
        {
            Pass
            {    
                  Tags { 
                    "RenderPipeline" = "UniversalPipeline"
                    "LightMode" = "UniversalForwardOnly"
                    "LightMode" = "DepthNormalsOnly"
                  }
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Specify the shader lighting model

To specify the shader lighting model as Lit or Simple Lit, use the
`UniversalMaterialType` tag. For example:

    
    
    Shader "Examples/ExamplePassFlag"
    {
        SubShader
        {
            Pass
            {    
                  Tags
                  { 
                    "RenderPipeline" = "UniversalPipeline"
                    "LightMode" = "UniversalGBuffer"
                    "UniversalMaterialType" = "Lit" 
                  }
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [ShaderLab Pass tags in URP](../urp-shaders/urp-shaderlab-pass-tags.html)
  * [Pass tags in ShaderLab reference](../../SL-PassTags.html)

[](../../urp/rendering/accurate-g-buffer-normals.html)

Enable accurate G-buffer normals in the Deferred rendering path in URP

[](../../urp/rendering/forward-plus-rendering-path-limitations.html)

Troubleshooting the Forward+ rendering path in URP

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

