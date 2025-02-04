[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-tags-set-pass.html)
  * [中文](/cn/current/Manual/writing-shader-tags-set-pass.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-set-pass.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-set-pass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-tags-set-pass.html)
  * [中文](/cn/current/Manual/writing-shader-tags-set-pass.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-set-pass.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-set-pass.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Configure when and if Unity uses a shader](writing-shader-tags.html)
  * Set when Unity runs a shader pass via a LightMode tag

[](writing-shader-tags-set-render-queue.html)

Set the render queue of a shader

[](writing-shader-prioritize-lower-quality-shaders.html)

Prioritize lower quality shaders with the LOD command

# Set when Unity runs a shader pass via a LightMode tag

The `LightMode` tag is a predefined Pass tag that Unity uses to determine
whether to execute the Pass during a given frame, when during the frame Unity
executes the Pass, and what Unity does with the output.

**Note:** The `LightMode` tag is not related to the
[LightMode](../ScriptReference/Experimental.GlobalIllumination.LightMode.html)
enum, which relates to lighting.

Every **render pipeline** A series of operations that take the contents of a
Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) uses the `LightMode` tag, but
the predefined values and their meanings vary. For more information, see
[Syntax and valid values](SL-PassTags.html#lightmode-tag).

In the Built-in Render Pipeline, if you do not set a `LightMode` tag, Unity
renders the Pass without any lighting or shadows; this essentially the same as
having a `LightMode` value of `Always`. In the Scriptable Render Pipeline, you
can use the `SRPDefaultUnlit` value to reference Passes without a LightMode
tag.

## Example in a Shader block

    
    
    Shader "Examples/ExampleLightMode"
    {
        SubShader
        {
            Pass
            {    
                  Tags { "LightMode" = "Always" }
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Example in a SubShader block

    
    
    Shader "Examples/ExampleLightMode"
    {
        SubShader
        {
            Pass
            {
                Tags { "LightMode" = "Always" }
                // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [SubShader tags in ShaderLab reference](SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](SL-PassTags.html)

[](writing-shader-tags-set-render-queue.html)

Set the render queue of a shader

[](writing-shader-prioritize-lower-quality-shaders.html)

Prioritize lower quality shaders with the LOD command

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

