[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/script-compile-order-folders.html)
  * [中文](/cn/current/Manual/script-compile-order-folders.html)
  * [日本語](/ja/current/Manual/script-compile-order-folders.html)
  * [한국어](/kr/current/Manual/script-compile-order-folders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/script-compile-order-folders.html)
  * [中文](/cn/current/Manual/script-compile-order-folders.html)
  * [日本語](/ja/current/Manual/script-compile-order-folders.html)
  * [한국어](/kr/current/Manual/script-compile-order-folders.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * Special folders and script compilation order

[](script-compilation.html)

Script compilation

[](conditional-compilation.html)

Conditional compilation

# Special folders and script compilation order

Unity reserves some project folder names for specific types of assets. Some of
these folders affect the order of script compilation. For more information
about these folders, refer to [Reserved folder name
reference](SpecialFolders.html)

## Predefined assemblies

Unity compiles **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in four separate phases, based on
where the script file is located within the project folder structure. Unity
creates a separate C# project file (.csproj) and a predefined assembly for
each phase. If there are no scripts eligible for a compilation phase, Unity
doesn’t create the corresponding project file or assembly.

Compilation order is significant when a script references a class compiled in
a different phase and therefore located in a different assembly. The basic
rule is that a script can reference anything compiled in its own compilation
phase or an earlier one, but can’t reference anything compiled in a later
phase.

The phases of compilation are as follows:

**Phase** | **Assembly name** | **Script files**  
---|---|---  
1 | `Assembly-CSharp-firstpass` | Runtime scripts in folders called `Plugins`.  
2 | `Assembly-CSharp-Editor-firstpass` | Editor scripts in folders called `Editor` that are anywhere inside top-level folders called `Plugins`.  
3 | `Assembly-CSharp` | All other scripts that are not inside a folder called `Editor`.  
4 | `Assembly-CSharp-Editor` | All remaining scripts that are inside a folder called `Editor`.  
  
You can create assembly definition files to organize the scripts in your
project with your own assemblies. Defining your own assemblies can reduce the
amount of code that Unity needs to recompile when you make an unrelated code
change, and can provide more control over dependencies to other assemblies.
For more information, refer to [Organizing scripts into assemblies](assembly-
definition-files.html).

## Additional resources

  * [Conditional compilation](conditional-compilation.html)
  * [Assembly definitions](assembly-definition-files.html)

[](script-compilation.html)

Script compilation

[](conditional-compilation.html)

Conditional compilation

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

