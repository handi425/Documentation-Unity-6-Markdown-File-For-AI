[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-troubleshooting-custom-control-library-compilation.html)
  * [中文](/cn/current/Manual/UIE-troubleshooting-custom-control-library-compilation.html)
  * [日本語](/ja/current/Manual/UIE-troubleshooting-custom-control-library-compilation.html)
  * [한국어](/kr/current/Manual/UIE-troubleshooting-custom-control-library-compilation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-troubleshooting-custom-control-library-compilation.html)
  * [中文](/cn/current/Manual/UIE-troubleshooting-custom-control-library-compilation.html)
  * [日本語](/ja/current/Manual/UIE-troubleshooting-custom-control-library-compilation.html)
  * [한국어](/kr/current/Manual/UIE-troubleshooting-custom-control-library-compilation.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Custom controls](UIE-custom-controls.html)
  * Troubleshooting custom control library compilation

[](UIE-define-a-namespace-prefix.html)

Define a namespace prefix

[](UIE-best-practices-for-managing-elements.html)

Best practices for managing elements

# Troubleshooting custom control library compilation

This troubleshooting guide helps you resolve issues when compiling custom
controls into DLLs.

## Symptoms

When you compile custom controls into DLLs, you might encounter the following
issues:

  * Custom controls don’t appear in the **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder.

  * Custom controls don’t serialize correctly when building libraries (DLLs).

## Cause

UI Toolkit uses the
[UxmlElement](../ScriptReference/UIElements.UxmlElementAttribute.html) code
generator to support UXML serialization. However, when compiling custom
controls into DLLs, the generated serialization code isn’t included by
default, causing issues with element visibility and serialization.

## Resolution

To resolve this issue, run the UI Toolkit source generator
(`Unity.UIToolkit.SourceGenerator.dll`) during the DLL compilation process.

  1. Find the source generator file in your Unity installation. It’s typically located at: `<Unity Installation Path>\Data\Tools\Unity.SourceGenerators\Unity.UIToolkit.SourceGenerator.dll`.

  2. Add the source generator as an analyzer in your library project’s `.csproj` file within an `<ItemGroup>`:
    
        <ItemGroup>
        <Analyzer Include="path\to\Unity.UIToolkit.SourceGenerator.dll" />
    </ItemGroup>
    

  3. Compile your library as usual. This triggers the source generator, which generates the required [UxmlSerializedData](../ScriptReference/UIElements.UxmlSerializedData.html) class for your custom control.

**Tip** : Always rebuild your library against the Unity version you’re using
because the generated code might vary between versions.

## Additional resources

  * [Customize UXML tag names and attributes](UIE-custom-tag-name-and-attributes.html)

[](UIE-define-a-namespace-prefix.html)

Define a namespace prefix

[](UIE-best-practices-for-managing-elements.html)

Best practices for managing elements

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

