[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-branching-introduction.html)
  * [中文](/cn/current/Manual/shader-branching-introduction.html)
  * [日本語](/ja/current/Manual/shader-branching-introduction.html)
  * [한국어](/kr/current/Manual/shader-branching-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-branching-introduction.html)
  * [中文](/cn/current/Manual/shader-branching-introduction.html)
  * [日本語](/ja/current/Manual/shader-branching-introduction.html)
  * [한국어](/kr/current/Manual/shader-branching-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Branching in shaders](shader-branching.html)
  * Introduction to static and dynamic branching

[](shader-branching.html)

Branching in shaders

[](shader-branching-use.html)

Static and dynamic branching in a shader

# Introduction to static and dynamic branching

## Static branching

When a **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) program includes conditionals that are
evaluated at compile time, it uses static branching. The compiler excludes the
code from the unused branch, so it does not appear in the compiled shader
program.

Internally, Unity uses static branching when it creates shader variants.
Static branching on its own does not have any of the performance disadvantages
of shader variants.

### Advantages and disadvantages of static branching

The main advantage of static branching is that it has no negative impact on
runtime performance. The main disadvantage of static branching is that you can
only use it at compile time.

Static branching means that the compiler excludes unneeded code from the
shader program. It results in small, specialized shader programs that contain
only the necessary code. There is no runtime performance cost to static
branching; in fact, the smaller programs are likely to result in quicker load
times and lower runtime memory usage.

To use static branching, the conditions must be constant at compile time. This
means that you can’t use it to execute code for different conditions at
runtime.

## Dynamic branching

When a shader program includes conditionals that are evaluated at runtime, it
uses dynamic branching.

There are two types of dynamic branching: dynamic branching based on uniform
variables, and dynamic branching based on any other runtime value. Uniform-
based branching is usually more efficient, because the uniform value is
constant for the whole draw call.

You can use [shader keywords](shader-keywords.html) for dynamic branching.
This allows you to use C# **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts) and the Material **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) to configure runtime branching
behavior for your shaders. This results is uniform-based branching; when you
do this, Unity compiles the shader keywords as uniforms.

### Advantages and disadvantages of dynamic branching

The main advantage of dynamic branching is that it allows you to use
conditionals at runtime without increasing the number of shader variants in
your project. The main disadvantage of dynamic branching is that it impacts
GPU performance.

The GPU performance impact varies by hardware, and by shader code. The reasons
are:

  * Branching based on non-uniform variables means that the GPU must either perform different operations at the same time (and therefore break parallelism), or “flatten the branch” and maintain parallelism by performing the operations for both branches and then discarding one result. Branching based on uniform variables means that the GPU must flatten the branch. Both of these approaches result in reduced GPU performance.
  * For any type of dynamic branching, the GPU must allocate register space for the worst case. If one branch is much more costly than the other, this means that the GPU wastes register space. This can lead to fewer invocations of the shader program in parallel, which reduces performance.

In general, if your code branches on uniform values and both branches have
roughly similar workloads, then the impact on GPU performance is likely to be
small. However, you should always profile your application and consider the
advantages and disadvantages case-by-case.

**Note:** Dynamic branching can also lead to large shader programs, because
the code for all conditions is compiled into the same shader program. However,
the effect of these larger files on load times and memory usage is usually
less significant than the impact of shader variants.

For information about other ways of using conditionals in shaders, and how to
decide which technique is right for your use case, see [Conditionals in
shaders](shader-conditionals-choose-a-type.html).

[](shader-branching.html)

Branching in shaders

[](shader-branching-use.html)

Static and dynamic branching in a shader

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

