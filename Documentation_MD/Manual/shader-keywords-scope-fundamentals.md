[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-keywords-scope-fundamentals.html)
  * [中文](/cn/current/Manual/shader-keywords-scope-fundamentals.html)
  * [日本語](/ja/current/Manual/shader-keywords-scope-fundamentals.html)
  * [한국어](/kr/current/Manual/shader-keywords-scope-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-keywords-scope-fundamentals.html)
  * [中文](/cn/current/Manual/shader-keywords-scope-fundamentals.html)
  * [日本語](/ja/current/Manual/shader-keywords-scope-fundamentals.html)
  * [한국어](/kr/current/Manual/shader-keywords-scope-fundamentals.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * Shader keyword scope fundamentals

[](shader-keywords.html)

Shader keyword fundamentals

[](shader-conditionals-choose-a-type.html)

Choose which type of keyword to use in shaders

# Shader keyword scope fundamentals

When you declare a set of keywords, you choose whether the keywords in the set
have local or global **scope**. This determines whether you can override the
state of this keyword at runtime using a global **shader** A program that runs
on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) keyword.

By default, you declare keywords with global scope. This means that you can
override the state of this keyword at runtime using a global shader keyword.
If you declare keywords with local scope, this means that you cannot override
the state of this keyword at runtime using a global shader keyword. For more
information and a code example, see [Using shader keywords with C#
scripts](shader-keywords-scripts.html).

**Note:** If a keyword with the same name exists in a shader source file and
its dependencies, the scope of the keyword in the source file overrides the
scope in the dependencies. Dependencies comprise all Shaders that are included
via the [Fallback command](SL-Fallback.html), and Passes that are included via
the [UsePass command](SL-UsePass.html).

To set this value, see the following documentation:

  * In hand-coded shaders, see [Declaring and using shader keywords in HLSL](SL-MultipleProgramVariants.html)
  * In Shader Graph, see [Keywords](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?subfolder=/manual/Keywords.html)

## Shader keywords and C# keywords

### Local and global shader keywords

When Unity represents shader keywords in C#, it uses the concept of **local
shader keywords** and **global shader keywords**.

Local shader keywords comprise all keywords that you declare in shader source
files. Local shader keywords affect an individual shader or compute shader.
Local keywords can have local or global scope, which affects whether they can
be overridden by global shader keywords.

Global shader keywords act as overrides for local shader keywords. You don’t
declare these in shader source files; they exist only in C# code. Global
shader keywords can affect multiple shaders and compute shaders at the same
time.

#### Local shader keywords

When you declare a shader keyword in a shader source file, Unity represents
this in C# with a
[LocalKeyword](../ScriptReference/Rendering.LocalKeyword.html) struct. This is
called a **local shader keyword**.

The [isOverridable](../ScriptReference/Rendering.LocalKeyword-
isOverridable.html) property of a `LocalKeyword` indicates whether the keyword
was declared with a global or local scope in the source file. It is `true` if
the keyword was declared with global scope and can therefore be overridden by
a global shader keyword with the same name. It is `false` if the keyword was
declared with local scope, and therefore cannot be overridden by a global
shader keyword with the same name.

Unity stores all local shader keywords that affect a shader or compute shader
in a [LocalKeywordSpace](../ScriptReference/Rendering.LocalKeywordSpace.html)
struct. For a graphics shader, you can access this with
[Shader.keywordSpace](../ScriptReference/Shader-keywordSpace.html). For a
compute shader, you can access this with [ComputeShader-
keywordSpace](../ScriptReference/ComputeShader-keywordSpace.html).

#### Global shader keywords

In addition to the local shader keywords that you declared in your source
files, Unity maintains a separate list of **global shader keywords**. You
don’t declare these in shader source files; instead, they are runtime
overrides for local shader keywords that you work with in C#. Global shader
keywords can affect multiple shaders and compute shaders at the same time.

Unity represents a global shader keyword with a
[GlobalKeyword](../ScriptReference/Rendering.GlobalKeyword.html) struct.

Setting a global shader keyword can be convenient when you need to enable or
disable the same shader keyword for many materials and compute shaders.
However, it has the following potential downsides:

  * Setting the global state of keywords can lead to unintended consequences if shaders accidentally define a keyword with the same name. You can guard against this by declaring keywords with local scope, or by naming keywords in a way that reduces the likelihood of clashes.
  * When you create a new `GlobalKeyword`, Unity updates its internal mapping between global and local keyword space for all shaders and compute shaders loaded at this point. This can be a CPU-intensive operation. To reduce the impact of this operation, try to create all global keywords shortly after application startup, while your application is loading.

[](shader-keywords.html)

Shader keyword fundamentals

[](shader-conditionals-choose-a-type.html)

Choose which type of keyword to use in shaders

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

