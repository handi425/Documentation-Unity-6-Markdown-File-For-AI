[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-keywords.html)
  * [中文](/cn/current/Manual/shader-keywords.html)
  * [日本語](/ja/current/Manual/shader-keywords.html)
  * [한국어](/kr/current/Manual/shader-keywords.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-keywords.html)
  * [中文](/cn/current/Manual/shader-keywords.html)
  * [日本語](/ja/current/Manual/shader-keywords.html)
  * [한국어](/kr/current/Manual/shader-keywords.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * Shader keyword fundamentals

[](shader-keywords-landing.html)

Shader keywords

[](shader-keywords-scope-fundamentals.html)

Shader keyword scope fundamentals

# Shader keyword fundamentals

Shader keywords allow you to use [conditional behavior](shader-conditionals-
choose-a-type.html) in your **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code. You can create shaders that
share some common code, but have different functionality when a given
**keyword** is enabled or disabled.

You can use shader keywords with [dynamic branching](shader-branching-
introduction.html#dynamic-branching), or with [Shader variants](shader-
variants.html)A verion of a shader program that Unity generates according to a
specific combination of shader keywords and their status. A Shader object can
contain multiple shader variants. [More info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant). Before you use shader
keywords, it is important to understand how these techniques work, and which
one is right for your project.

**Note:** In Shader Graph, the terminology is different: a set of keywords is
called a **Keyword** , and the keywords in a set are called **states**.
Internally, the functionality is the same: Unity compiles them in the same
way, you work with them the same way with C# **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), and so on.

## Declaring shader keywords

You declare shader keywords in sets. A set contains mutually exclusive
keywords.

  * In hand-coded shaders, see [Declaring and using shader keywords in HLSL](SL-MultipleProgramVariants.html)
  * In Shader Graph, see [Keywords](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?subfolder=/manual/Keywords.html). **Note:** The “dynamic branch” option is not available in Shader Graph. You can only use shader keywords with shader variants in Shader Graph.

For example, the following set contains three keywords:

  * COLOR_RED
  * COLOR_GREEN
  * COLOR_BLUE

The way that you declare shader keywords affects a number of things:

  * The type affects whether and how Unity uses the keywords to generate shader variants, or whether it uses them for dynamic branching.
  * The [scope](shader-keywords-scope-fundamentals.html) affects whether the keywords are local or global. This determines their behavior at runtime.
  * The [stage](shader-branching-pass.html) affects which shader stage the keywords affect (where applicable).

## Definition type: multi compile, shader feature, or dynamic branch

When you declare a set of keywords, you choose whether to use them with
[shader variants](shader-variants.html) or with [dynamic branching](shader-
branching.html). If you choose shader variants, you must also choose how Unity
defines the keywords internally; this affects the number of variants that
Unity compiles.

Refer to [Choose which type of conditional to use in shaders](shader-
conditionals-choose-a-type.html) for more information.

## Managing sets of keywords at runtime

When you author your shader, you declare keywords in sets. A set contains
mutually-exclusive keywords.

At runtime, Unity has no concept of these sets. It allows you to enable or
disable any keyword independently, and enabling or disabling a keyword has no
effect on the state of any other keyword. This means that it is possible to
enable multiple keywords from the same set, or disable all the keywords in a
set.

If you use keywords with shader variants, when more than one keyword in a set
is enabled or no keywords in a set are enabled, Unity chooses a variant that
it considers a “good enough” match. There is no guarantee about what exactly
happens, and it can lead to unintended results. It is best to avoid this
situation by managing keyword state carefully.

If you use keywords with dynamic branching, when more than one keyword in a
set is enabled or no keywords in a set are enabled, the conditional branches
execute accordingly. For example, if both `KEYWORD_A` and `KEYWORD_B` are
enabled, the branches for `if (KEYWORD_A)` and `if (KEYWORD_B)` will both
execute.

## Shader keyword limits

Unity can use up to 4,294,967,294 global shader keywords. Individual shaders
and compute shaders can use up to 65,534 local shader keywords. These totals
include keywords used for variants, and keywords used for dynamic branching.

Every keyword declared in the shader source file and its dependencies count
towards this limit. Dependencies include [Passes](SL-Pass.html) that the
shader includes with [UsePass](SL-UsePass.html), and [fallbacks](SL-
Fallback.html).

If Unity encounters a shader keyword with the same name multiple times, it
only counts towards the limit once.

If a shader uses more than 128 keywords in total, it incurs a small runtime
performance penalty; therefore, it is best to keep the number of keywords low.
Unity always reserves 4 keywords per shader.

[](shader-keywords-landing.html)

Shader keywords

[](shader-keywords-scope-fundamentals.html)

Shader keyword scope fundamentals

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

