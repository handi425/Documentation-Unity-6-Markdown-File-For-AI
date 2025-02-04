[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/analyzer-scope-and-diagnostics.html)
  * [中文](/cn/current/Manual/analyzer-scope-and-diagnostics.html)
  * [日本語](/ja/current/Manual/analyzer-scope-and-diagnostics.html)
  * [한국어](/kr/current/Manual/analyzer-scope-and-diagnostics.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/analyzer-scope-and-diagnostics.html)
  * [中文](/cn/current/Manual/analyzer-scope-and-diagnostics.html)
  * [日本語](/ja/current/Manual/analyzer-scope-and-diagnostics.html)
  * [한국어](/kr/current/Manual/analyzer-scope-and-diagnostics.html)

  * [Scripting](scripting.html)
  * [Debugging and diagnostics](debugging-and-diagnostics.html)
  * [Roslyn analyzers and source generators](roslyn-analyzers.html)
  * Analyzer scope and diagnostics

[](ruleset-files.html)

Create rule set files

[](analysis.html)

Optimization

# Analyzer scope and diagnostics

## Analyzer scope

You can limit the scope of analyzers in your project by using assembly
definitions, so that they only analyze certain portions of your code.

Unity applies analyzers to all assemblies in your project’s Assets folder, or
in any subfolder whose parent folder doesn’t contain an [assembly definition
file](assembly-definition-files.html). If an analyzer is in a folder that
contains an assembly definition, or a subfolder of such a folder, the analyzer
only applies to the assembly generated from that assembly definition, and to
any other assembly that references it.

This means, for example, that a [package](PackagesList.html)A container that
stores various types of features and assets for Unity, including Editor or
Runtime tools and libraries, Asset collections, and project templates.
Packages are self-contained units that the Unity Package Manager can share
across Unity projects. Most of the time these are called _packages_ , but
occasionally they are called **Unity Package Manager (UPM) packages**. [More
info](Packages.html)  
See in [Glossary](Glossary.html#Package) can supply analyzers that only
analyze code related to the package, which can help package users to use the
package API correctly.

## Report analyzer diagnostics

To view information such as the total execution time of your analyzers and
source generators or the relative execution times of each analyzer or source
generator, go to **Preferences** > **Diagnostic Switches** and enable
**EnableDomainReloadTimings**. When enabled, the information is displayed in
the console window.

## Additional resources

  * [Special folders and script compilation order](script-compile-order-folders.html)
  * [Organizing scripts into assemblies](assembly-definition-files.html)

[](ruleset-files.html)

Create rule set files

[](analysis.html)

Optimization

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

