[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-tags-set-render-queue.html)
  * [中文](/cn/current/Manual/writing-shader-tags-set-render-queue.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-set-render-queue.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-set-render-queue.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-tags-set-render-queue.html)
  * [中文](/cn/current/Manual/writing-shader-tags-set-render-queue.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-set-render-queue.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-set-render-queue.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Configure when and if Unity uses a shader](writing-shader-tags.html)
  * Set the render queue of a shader

[](writing-shader-tags-require-package.html)

Set a shader to require a package

[](writing-shader-tags-set-pass.html)

Set when Unity runs a shader pass via a LightMode tag

# Set the render queue of a shader

The `Queue` tag tells Unity which render queue to use for geometry that it
renders. The render queue is one of the factors that determines the order that
Unity renders geometry in.

You can use the `Queue` tag in two ways: you can tell Unity to use a named
render queue, or an unnamed render queue that it renders after a named render
queue.

## Examples

This example code creates a SubShader that renders geometry as part of the
Transparent render queue:

    
    
    Shader "ExampleShader" {
        SubShader {
            Tags { "Queue" = "Transparent" }
            Pass {
                …
            }
        }
    }
    

This example code creates a SubShader that renders geometry in an unnamed
queue, after the Geometry queue.

    
    
    Shader "ExampleShader" {
        SubShader {
            Tags { "Queue" = "Geometry+1" }
            Pass {
                …
            }
        }
    }
    

[](writing-shader-tags-require-package.html)

Set a shader to require a package

[](writing-shader-tags-set-pass.html)

Set when Unity runs a shader pass via a LightMode tag

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

