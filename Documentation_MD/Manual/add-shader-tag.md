[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/add-shader-tag.html)
  * [中文](/cn/current/Manual/add-shader-tag.html)
  * [日本語](/ja/current/Manual/add-shader-tag.html)
  * [한국어](/kr/current/Manual/add-shader-tag.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/add-shader-tag.html)
  * [中文](/cn/current/Manual/add-shader-tag.html)
  * [日本語](/ja/current/Manual/add-shader-tag.html)
  * [한국어](/kr/current/Manual/add-shader-tag.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Configure when and if Unity uses a shader](writing-shader-tags.html)
  * Add a shader tag to a SubShader or Pass

[](writing-shader-tags-introduction.html)

Introduction to shader tags

[](writing-shader-tags-pipeline.html)

Set a shader to require URP or HDRP

# Add a shader tag to a SubShader or Pass

In **ShaderLab** Unity’s language for defining the structure of Shader
objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab), you assign tags to a SubShader or
Pass by placing a `Tags` block inside the block.

Note that both SubShaders and Passes use the `Tags` block, but they work
differently. Assigning SubShader tags to a Pass has no effect, and vice versa.
The difference is where you put the `Tags` block:

  * To define Pass tags, place the `Tags` block inside a `Pass` block.
  * To define SubShader tags, place the `Tags` block inside a `SubShader` block but outside a `Pass` block.

# Example in a Pass block

    
    
    Shader "Examples/ExampleRequireOptions"
    {
        SubShader
        {
            Pass
            {    
                  Tags { "RequireOptions" = "SoftVegetation" }
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [SubShader tags in ShaderLab reference](SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](SL-PassTags.html)

[](writing-shader-tags-introduction.html)

Introduction to shader tags

[](writing-shader-tags-pipeline.html)

Set a shader to require URP or HDRP

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

