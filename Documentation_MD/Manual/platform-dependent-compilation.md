[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/platform-dependent-compilation.html)
  * [中文](/cn/current/Manual/platform-dependent-compilation.html)
  * [日本語](/ja/current/Manual/platform-dependent-compilation.html)
  * [한국어](/kr/current/Manual/platform-dependent-compilation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/platform-dependent-compilation.html)
  * [中文](/cn/current/Manual/platform-dependent-compilation.html)
  * [日本語](/ja/current/Manual/platform-dependent-compilation.html)
  * [한국어](/kr/current/Manual/platform-dependent-compilation.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Conditional compilation](conditional-compilation.html)
  * Conditional compilation in Unity

[](conditional-compilation.html)

Conditional compilation

[](scripting-symbol-reference.html)

Unity scripting symbol reference

# Conditional compilation in Unity

Unity’s support for the C# language includes the use of **directives** , which
allow you to selectively include or exclude code from compilation, based on
whether certain **scripting symbols** are defined. For more information on how
these directives work in C#, refer to Microsoft’s documentation on [C#
preprocessor directives](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/preprocessor-directives).

Unity has a range of predefined symbols you can use in your **scripts** A
piece of code that allows you to create your own Components, trigger game
events, modify Component properties over time and respond to user input in any
way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) to selectively include or exclude
sections of code from compilation. For example, the symbol that’s defined in
project builds for Windows standalone platform is `UNITY_STANDALONE_WIN`. You
can check whether this symbol is defined using a special type of `if`
statement:

    
    
    #if UNITY_STANDALONE_WIN
    
      Debug.Log("Standalone Windows");
    
    #endif
    

The hash (`#`) character in front of `#if` and `#endif` indicates that these
statements are directives that are handled during the compilation process,
rather than at runtime. In the previous example, the Debug line is only
included for compilation in the Windows standalone build of the project. When
compiled in the Unity Editor or in other target builds, it’s omitted entirely.
This is different to using a regular [if
statements](https://learn.microsoft.com/en-us/dotnet/csharp/language-
reference/statements/selection-statements), which might only bypass the
execution of certain sections of code at runtime.

You can use the `#elif` and `#else` directives to check multiple conditions:

    
    
    #if UNITY_EDITOR
    
        Debug.Log("Unity Editor");
    
    #elif UNITY_IOS
    
        Debug.Log("Unity iOS");
    
    #else
    
        Debug.Log("Any other platform");
    
    #endif
    

There are several predefined symbols which allow you to selectively compile or
omit code based on the selected [Platform](scripting-symbol-
reference.html#Platform), the [Editor Version](scripting-symbol-
reference.html#Editor), and [other](scripting-symbol-reference.html#Other)
system environment scenarios. For the full list of Unity’s predefined symbols,
refer to [Unity scripting symbol reference](scripting-symbol-reference.html).

You can also define your own scripting symbols using the Editor, via
scripting, or via an asset file. For more information, refer to [Custom
scripting symbols](custom-scripting-symbols.html).

**Note:** **Scripting symbols** are also referred to as define symbols,
preprocessor defines, or just defines.

## Alternatives to directives

Preprocessor directives are not always the most appropriate or reliable way to
conditionally include or exclude code. Alternative approaches are listed here.

###  `Conditional` attribute

You can use the C# `Conditional` attribute which is a cleaner, less error-
prone way of stripping out functions. For more information, refer to
[ConditionalAttribute Class](https://msdn.microsoft.com/en-
us/library/system.diagnostics.conditionalattribute\(v=vs.110\).aspx). Common
Unity callbacks such as `Start()`, `Update()`, `LateUpdate()`,
`FixedUpdate()`, `Awake()` aren’t affected by this attribute because they’re
called directly from the engine and, for performance reasons, it doesn’t take
them into account.

### Assembly definition constraints

The recommended approach for conditional compilation at a high level is to
organize your scripts in assemblies with associated [Assembly Definition
files](assembly-definition-files.html). If the code you want to conditionally
include or exclude is in an assembly, you can configure [Define
Constraints](class-AssemblyDefinitionImporter.html#define-constraints) on the
assembly definition to, for example, only compile the code when a given
version of a package is present in the project.

### Conditional execution

Instead of conditional compilation, you can enforce conditional execution of
the compiled code using standard `if` statements. For example, Unity’s
`UNITY_64` scripting symbol is an unreliable test for 64-bit architecture, so
it’s preferable to do the following instead:

    
    
    if (IntPtr.Size == 4)
    {
        // 32 bit code
    }
    else
    {
        // 64-bit code
    }
    

## Additional resources

  * [How to create and use scripts in Unity](creating-scripts.html)
  * [Unity scripting symbol reference](scripting-symbol-reference.html)
  * [Test your conditionally compiled code](test-conditional-compilation.html)
  * [Custom scripting symbols](custom-scripting-symbols.html)

[](conditional-compilation.html)

Conditional compilation

[](scripting-symbol-reference.html)

Unity scripting symbol reference

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

