[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-tags-disable-dynamic-batching.html)
  * [中文](/cn/current/Manual/writing-shader-tags-disable-dynamic-batching.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-disable-dynamic-batching.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-disable-dynamic-batching.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-tags-disable-dynamic-batching.html)
  * [中文](/cn/current/Manual/writing-shader-tags-disable-dynamic-batching.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-disable-dynamic-batching.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-disable-dynamic-batching.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Configure when and if Unity uses a shader](writing-shader-tags.html)
  * Disable dynamic batching of a shader

[](writing-shader-prioritize-lower-quality-shaders.html)

Prioritize lower quality shaders with the LOD command

[](writing-shader-tags-get-tag-value.html)

Get tag values in a script

# Disable dynamic batching of a shader

The `DisableBatching` SubShader Tag prevents Unity from applying [Dynamic
Batching](DrawCallBatching.html)An automatic Unity process which attempts to
render multiple meshes as if they were a single mesh for optimized graphics
performance. The technique transforms all of the GameObject vertices on the
CPU and groups many similar vertices together. [More
info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) to geometry that uses this
SubShader.

This is useful for **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) programs that perform object space
operations. Dynamic Batching transforms all geometry into world space, meaning
that shader programs can no longer access object space. Shader programs that
rely on object space therefore do not render correctly. To avoid this problem,
use this SubShader Tag to prevent Unity from applying Dynamic Batching.

## Examples

This example code creates a SubShader with a DisableBatching value of `True`:

    
    
    Shader "ExampleShader" {
    
        SubShader {
    
            Tags { "DisableBatching" = "True" }
            Pass {
                …
            }
    
        }
    
    }
    

[](writing-shader-prioritize-lower-quality-shaders.html)

Prioritize lower quality shaders with the LOD command

[](writing-shader-tags-get-tag-value.html)

Get tag values in a script

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

