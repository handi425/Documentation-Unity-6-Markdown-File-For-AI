[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gpu-instancing-strip-variants.html)
  * [中文](/cn/current/Manual/gpu-instancing-strip-variants.html)
  * [日本語](/ja/current/Manual/gpu-instancing-strip-variants.html)
  * [한국어](/kr/current/Manual/gpu-instancing-strip-variants.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gpu-instancing-strip-variants.html)
  * [中文](/cn/current/Manual/gpu-instancing-strip-variants.html)
  * [日本語](/ja/current/Manual/gpu-instancing-strip-variants.html)
  * [한국어](/kr/current/Manual/gpu-instancing-strip-variants.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in the Built-In Render Pipeline](graphics-performance-birp.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
  * Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline

[](gpu-instancing-change-data.html)

Example of changing per-instance data at runtime in the Built-In Render
Pipeline

[](gpu-instancing-birp-shader-modifications.html)

GPU instancing shader reference for the Built-In Render Pipeline

# Prevent Unity stripping GPU instancing shaders in the Built-In Render
Pipeline

Unity generates Surface **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) with instancing [variants](SL-
MultipleProgramVariants.html) by default, unless you specify `noinstancing` in
the `#pragma` directive. Unity ignores uses of #pragma
multi_compile_instancing in a **surface shader** A streamlined way of writing
shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader).

Unity’s Standard and StandardSpecular shaders have instancing support by
default, but with no per-instance properties other than the transform.

If your **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) contains no **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with GPU instancing enabled, then
Unity strips instancing shader variants. To override the stripping behaviour:

  1. Open Project Settings (menu: **Edit** > **Project Settings**).
  2. Go to **Graphics**.
  3. In the **Shader Stripping** section, set **Instancing Variants** to **Keep All**.

[](gpu-instancing-change-data.html)

Example of changing per-instance data at runtime in the Built-In Render
Pipeline

[](gpu-instancing-birp-shader-modifications.html)

GPU instancing shader reference for the Built-In Render Pipeline

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

