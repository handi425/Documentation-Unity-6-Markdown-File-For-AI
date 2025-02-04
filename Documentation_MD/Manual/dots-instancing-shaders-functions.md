[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dots-instancing-shaders-functions.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-functions.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-functions.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-functions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dots-instancing-shaders-functions.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-functions.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-functions.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-functions.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
  * DOTS Instancing shader functions reference for URP

[](dots-instancing-shaders-macros.html)

DOTS Instancing shader macros reference for URP

[](urp/features/rendering-debugger.html)

Rendering Debugger in URP

# DOTS Instancing shader functions reference for URP

Alongside the access macros, Unity provides **shader** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) functions that load the values of
constants directly from the draw command data. Shaders that Unity provides use
these functions.

Unity provides the following shader functions:

**Shader function** | **Description**  
---|---  
`LoadDOTSInstancedData_RenderingLayer` | Returns the [renderingLayerMask](../ScriptReference/Rendering.BatchFilterSettings-renderingLayerMask.html) for the draw command.  
`LoadDOTSInstancedData_MotionVectorsParams` | Returns the [motion vector generation mode](../ScriptReference/Rendering.BatchFilterSettings-motionMode.html) for the draw command. This is formatted as a float4, which is what Unity shaders expect.  
`LoadDOTSInstancedData_WorldTransformParams` | Returns whether to draw the instance with a flipped triangle winding. See [FlipWinding](../ScriptReference/Rendering.BatchDrawCommandFlags.FlipWinding.html).  
`LoadDOTSInstancedData_LightData` | Returns whether the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)’s main Directional Light is active for
the instance. The main light can be deactivated for multiple reasons, for
example if the light already included in light maps.  
`LoadDOTSInstancedData_LODFade` | Returns the 8 bit crossfade value you set if the [LODCrossFade flag](../ScriptReference/Rendering.BatchDrawCommandFlags.LODCrossFade.html) is set. If the flag is not set, the return value is undefined.  
  
[](dots-instancing-shaders-macros.html)

DOTS Instancing shader macros reference for URP

[](urp/features/rendering-debugger.html)

Rendering Debugger in URP

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

