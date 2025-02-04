[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-conditionals-choose-a-type.html)
  * [中文](/cn/current/Manual/shader-conditionals-choose-a-type.html)
  * [日本語](/ja/current/Manual/shader-conditionals-choose-a-type.html)
  * [한국어](/kr/current/Manual/shader-conditionals-choose-a-type.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-conditionals-choose-a-type.html)
  * [中文](/cn/current/Manual/shader-conditionals-choose-a-type.html)
  * [日本語](/ja/current/Manual/shader-conditionals-choose-a-type.html)
  * [한국어](/kr/current/Manual/shader-conditionals-choose-a-type.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * Choose which type of keyword to use in shaders

[](shader-keywords-scope-fundamentals.html)

Shader keyword scope fundamentals

[](SL-MultipleProgramVariants-declare.html)

Declare shader keywords

# Choose which type of keyword to use in shaders

When you declare a set of keywords, you choose whether to use them with
[shader variants](shader-variants.html)A verion of a shader program that Unity
generates according to a specific combination of shader keywords and their
status. A Shader object can contain multiple shader variants. [More
info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant) or with [dynamic
branching](shader-branching.html).

  * “dynamic branch”: Use this to create a set of keywords for use with dynamic branching. Internally, Unity uses these keywords to create uniform variables.
  * “multi compile” or “**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) feature”: Use this to create a set of
keywords for use with shader variants. Internally, Unity uses these keyword to
create `#define` preprocessor directives.

    * “multi compile” declares a set of keywords for use with shader variants.  
  
Unity compiles shader variants for all keywords in the set.

    * “shader feature” declares a set of keywords for use with shader variants, and also instructs the compiler to compile variants where none of these keywords are enabled.  
  
Unity examines the state of your project at build time, and only compiles
variants for keywords that are in use. A keyword is in use if a material that
is included in the build has that keyword enabled.

Whether to choose “multi compile” or “shader feature” depends on how you use
the keywords. If you use the keywords to configure materials in your project
and do not change their value from C# **scripts** A piece of code that allows
you to create your own Components, trigger game events, modify Component
properties over time and respond to user input in any way you like. [More
info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) at runtime, then you should use
“shader feature” to reduce the number of shader keywords and variants in your
project. If you enable and disable keywords at runtime using C# scripts, then
you should use “multi compile” to prevent variants being stripped in error.
For more information on shader stripping, see [Shader variant
stripping](shader-variant-stripping.html).

There is no “one size fits all” approach to conditionals in shaders, and you
should consider the advantages and disadvantages of each approach for a given
shader, in a given project.

Which conditional to use depends on when you need the shader to switch to a
different code branch:

  * Only while you’re editing.
  * During runtime.

### Switch code branch while you’re editing

If you don’t need a shader to switch to a different code branch at runtime,
you can use conditionals that Unity only evaluates while you’re editing.

For example you can set up a property in a Material’s **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to make a shader do the
following:

  * Add specular reflections to some instances of a material but not others.
  * Add a different look to certain objects, such as objects that appear in underwater **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

If you use this approach, shader code is simpler to write and maintain, and
less likely to affect build time, file size and performance.

To do this, use one of the following:

  * [Shader variants](shader-variants.html): Use `shader_feature` to [declare keywords](SL-MultipleProgramVariants.html) and evaluate them in `if` statements.
  * [Static branching](shader-branching-use.html#static-branching): Use preprocesser constants and macros.

If you use the `shader_feature` keyword definition, Unity keeps shader
variants used by Materials in your build, and removes (‘strips’) other shader
variants. This keeps build times low and file sizes small.

Avoid using a C# script to enable or disable `shader_feature` keywords at
runtime, because if a Material uses a shader variant that’s missing, Unity
chooses a different available variant instead. If you do need to enable or
disable keywords at runtime, use one of the following approaches to make sure
your build includes all the variants you need:

  * Include a [shader variant collection](shader-variant-collections.html) with the shader variants you need in the list of [preloaded shaders](class-GraphicsSettings.html#shader-loading).
  * Include a Material in your build for every combination of `shader_feature` keywords you want to use.

### Switch code branch at runtime

If you need to use C# scripting to make the shader switch to a different code
branch at runtime, you can use conditionals that Unity evaluates both while
you’re editing and at runtime.

For example you can use a C# script to make a shader do the following:

  * Change a Material dynamically so it has snow on it at certain times.
  * Change a Material when a user changes quality settings, for example to give users dynamic control over whether fog appears.

To do this, use one of the following:

  * [Shader variants](shader-variants.html): Use `multi_compile` to [declare keywords](SL-MultipleProgramVariants.html) and evaluate them in `if` statements.
  * [Dynamic branching](shader-branching-use.html#dynamic-branching).

If you use the `multi_compile` keyword definition, Unity builds a shader
variant for every possible combination of shader code branches, including
combinations that aren’t used by Materials in your build. This means you can
enable and disable keywords at runtime, but it might also greatly increase
build time, file size, load times and memory usage. See [shader
variants](shader-variants.html).

Dynamic branching doesn’t create shader variants, but may mean your shaders
run more slowly on the GPU, especially if any of the following are true:

  * Your shaders run on a less capable GPU.
  * Your conditional code has ‘asymmetric branches’, where one branch is longer or more complex code than the other.

You can [check how many shader variants you have](shader-how-many-
variants.html) to see whether you can use dynamic branching without affecting
GPU performance too much. See [shader branching](shader-branching.html) for
more on the advantages and disadvantages of dynamic branching.

## Additional resources

  * [Shader keywords fundamentals](shader-keywords.html)

[](shader-keywords-scope-fundamentals.html)

Shader keyword scope fundamentals

[](SL-MultipleProgramVariants-declare.html)

Declare shader keywords

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

