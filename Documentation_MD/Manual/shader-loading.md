[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-loading.html)
  * [中文](/cn/current/Manual/shader-loading.html)
  * [日本語](/ja/current/Manual/shader-loading.html)
  * [한국어](/kr/current/Manual/shader-loading.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-loading.html)
  * [中文](/cn/current/Manual/shader-loading.html)
  * [日本語](/ja/current/Manual/shader-loading.html)
  * [한국어](/kr/current/Manual/shader-loading.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Troubleshooting shaders](shader-troubleshooting.html)
  * [Fixing hitches or stalls](shader-reduce-stalling.html)
  * Shader loading

[](shader-reduce-stalling.html)

Fixing hitches or stalls

[](shader-prewarm.html)

Prewarm shaders

# Shader loading

Unity loads [compiled shaders](shader-compilation.html) from your built
application in the following way:

  1. When Unity loads a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) or a [runtime
resource](LoadingResourcesatRuntime.html), it loads all the compiled
**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) variants for the scene or resource
into CPU memory.

  2. By default, Unity decompresses all the shader variants into another area of CPU memory. You can [control how much memory shaders use on different platforms](shader-memory.html).
  3. The first time Unity needs to render geometry using a shader variant, Unity passes the shader variant and its data to the graphics API and the graphics driver.
  4. The graphics driver creates a GPU-specific version of the shader variant and uploads it to the GPU.

This approach ensures that Unity and the graphics driver avoid processing and
storing all the shader variants on the GPU before Unity needs them. But there
might be a visible stall when the graphics driver creates a GPU-specific
shader variant for the first time.

Unity caches each GPU-specific shader variant, to avoid another stall when
Unity needs the shader variant again.

Unity removes the shader variant completely from CPU and GPU memory when there
are no longer any objects that reference the shader variant.

## Which shaders Unity loads

Unity only loads compiled shaders that are compatible with the platform’s
graphics API, hardware and [graphics tier](graphics-tiers.html).

If Unity can’t find the shader variant it needs because you or Unity [stripped
the shader variant](shader-variant-stripping.html) from your built
application, Unity tries to select a similar shader variant. If Unity can’t
find a similar shader variant, it uses the magenta [error shader](shader-
error.html).

You can [enable strict shader variant matching](shader-how-many-
variants.html#highlight-missing-shaders) to stop Unity trying to select a
similar shader variant.

##  How Unity selects a subshader

If a shader variant contains multiple [subshaders](shader-
objects.html#subshaders), Unity tries to select and use a single subshader
that’s compatible with all of the following:

  * The platform’s hardware.
  * The current [ShaderLab level of detail (LOD)](SL-ShaderLOD.html).
  * The active **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline).

Unity searches for the first compatible subshader among the following elements
in the following order:

  1. The subshaders in the order they appear in the shader.
  2. The subshaders in any fallback **shader objects** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject), in the order they appear in the
shader objects.

If Unity can’t find a compatible subshader, it uses the magenta error shader.

You can set which subshaders are compatible with which hardware using
**ShaderLab** Unity’s language for defining the structure of Shader objects.
[More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) tags. See [ShaderLab: assigning
tags to a SubShader](SL-SubShaderTags.html).

## Check when Unity loads shaders

To check when a shader loads from serialized data, search for the following
**profiler markers** Placed in code to describe a CPU or GPU event that is
then displayed in the Unity Profiler window. Added to Unity code by default,
or you can use [ProfilerMarker
API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-
guide.html) to add your own custom markers. [More info](profiler-markers.html)  
See in [Glossary](Glossary.html#Profilermarker) in the
[Profiler](Profiler.html)A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler):

  * `Shader.ParseThreaded`
  * `Shader.ParseMainThread`

To check when a shader unloads shader variants, search for the
`Shader.MainThreadCleanup` profiler marker.

## Additional resources

  * [How Unity loads and uses shaders](shader-loading.html)
  * [Optimizing shader runtime performance](SL-ShaderPerformance.html)

[](shader-reduce-stalling.html)

Fixing hitches or stalls

[](shader-prewarm.html)

Prewarm shaders

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

