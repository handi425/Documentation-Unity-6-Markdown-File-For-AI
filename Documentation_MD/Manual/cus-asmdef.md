[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/cus-asmdef.html)
  * [中文](/cn/current/Manual/cus-asmdef.html)
  * [日本語](/ja/current/Manual/cus-asmdef.html)
  * [한국어](/kr/current/Manual/cus-asmdef.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/cus-asmdef.html)
  * [中文](/cn/current/Manual/cus-asmdef.html)
  * [日本語](/ja/current/Manual/cus-asmdef.html)
  * [한국어](/kr/current/Manual/cus-asmdef.html)

  * [Packages and feature sets](PackagesList.html)
  * [Creating custom packages](CustomPackages.html)
  * Assembly definition and packages

[](upm-semver.html)

Versioning

[](cus-legal.html)

Meeting legal requirements

# Assembly definition and packages

You must associate **scripts** A piece of code that allows you to create your
own Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) inside a package to an assembly
definition file (`.asmdef`). Assembly definition files are the Unity
equivalent to a C# project in the .NET ecosystem. You must set explicit
references in the assembly definition file to other assemblies (whether in the
same package or in external packages). Refer to [Assembly
Definitions](assembly-definition-files.html) for more details.

Use these conventions for naming and storing your assembly definition files to
ensure that the compiled assembly filenames follow the [.NET Framework Design
Guidelines](https://docs.microsoft.com/en-us/dotnet/standard/design-
guidelines/):

  * Store Editor-specific code under a root editor assembly definition file:

`Editor/<company-name>.<package-name>.Editor.asmdef`

  * Store runtime-specific code under a root runtime assembly definition file:

`Runtime/<company-name>.<package-name>.asmdef`

  * Configure related test assemblies for your editor and runtime scripts:

`Tests/Editor/<company-name>.<package-name>.Editor.Tests.asmdef`

`Tests/Runtime/<company-name>.<package-name>.Tests.asmdef`

To get a more general view of a recommended package folder layout, refer to
[Package layout](cus-layout.html).

## Example file

In this example, the assembly definition file uses references to its own
assemblies, and an assembly that’s part of a package dependency
([HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-
definition@latest)):

    
    
    {
        "name": "MyCompany.MyPackageName",
        "references": [
            "MyCompany.MyPackageName.Tools",
            "MyCompany.MyPackageName.Planes",
            "Unity.RenderPipelines.HighDefinition.Runtime"
        ],
        "includePlatforms": [],
        "excludePlatforms": [],
        "allowUnsafeCode": false,
        "overrideReferences": false,
        "precompiledReferences": [],
        "autoReferenced": true,
        "defineConstraints": [],
        "versionDefines": [
            {
                "name": "com.unity.render-pipelines.high-definition",
                "expression": "7.1.0",
                "define": "HDRP_7_1_0_OR_NEWER"
            },
            {
                "name": "com.unity.modules.particlesystem",
                "expression": "1.0.0",
                "define": "USING_PARTICLE_SYSTEM"
            }
        ],
        "noEngineReferences": false
    }
    

For details about the structure of an assembly definition file, refer to
[Assembly Definition File Format](assembly-definition-file-format.html).

## Additional resources

  * [Assembly definitions](assembly-definition-files.html)

[](upm-semver.html)

Versioning

[](cus-legal.html)

Meeting legal requirements

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

