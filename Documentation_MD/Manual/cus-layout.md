[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/cus-layout.html)
  * [中文](/cn/current/Manual/cus-layout.html)
  * [日本語](/ja/current/Manual/cus-layout.html)
  * [한국어](/kr/current/Manual/cus-layout.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/cus-layout.html)
  * [中文](/cn/current/Manual/cus-layout.html)
  * [日本語](/ja/current/Manual/cus-layout.html)
  * [한국어](/kr/current/Manual/cus-layout.html)

  * [Packages and feature sets](PackagesList.html)
  * [Creating custom packages](CustomPackages.html)
  * Package layout

[](cus-naming.html)

Naming your package

[](cus-tests.html)

Adding tests to a package

# Package layout

This is the package layout recommended for custom packages:

    
    
    <package-root>
      ├── package.json
      ├── README.md
      ├── CHANGELOG.md
      ├── LICENSE.md
      ├── Third Party Notices.md
      ├── Editor
      │   ├── <company-name>.<package-name>.Editor.asmdef
      │   └── EditorExample.cs
      ├── Runtime
      │   ├── <company-name>.<package-name>.asmdef
      │   └── RuntimeExample.cs
      ├── Tests
      │   ├── Editor
      │   │   ├── <company-name>.<package-name>.Editor.Tests.asmdef
      │   │   └── EditorExampleTest.cs
      │   └── Runtime
      │        ├── <company-name>.<package-name>.Tests.asmdef
      │        └── RuntimeExampleTest.cs
      ├── Samples~
      │        ├── SampleFolder1
      │        ├── SampleFolder2
      │        └── ...
      └── Documentation~
           └── <package-name>.md
    
    

Many official Unity packages also implement this structure.

**Location** | **Description**  
---|---  
`package.json` | The [package manifest](upm-manifestPkg.html)Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest), which defines the package
dependencies and other metadata.  
`README.md` | Developer package documentation. This is generally documentation to help developers who want to change the package or push a new change on the package’s main branch.  
`CHANGELOG.md` | Description of package changes in reverse chronological order. It’s good practice to use a standard format, like [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).  
`LICENSE.md` | Contains the [package license text](cus-legal.html). Usually the Package Manager copies the text from the selected [SPDX list website](https://spdx.org/licenses/).  
`Third Party Notices.md` | Contains information that’s required to meet [legal requirements](cus-legal.html).  
`Editor/` | Editor platform-specific Assets folder. Unlike Editor folders under Assets, this is only a convention and doesn’t affect the Asset import pipeline. Refer to [Assembly definition and packages](cus-asmdef.html) to properly configure Editor-specific assemblies in this folder.  
`Runtime/` | Runtime platform-specific Assets folder. This is only a convention and doesn’t affect the Asset import pipeline. Refer to [Assembly definition and packages](cus-asmdef.html) to properly configure runtime assemblies in this folder.  
`Tests/` | Folder to store any [tests included](cus-tests.html) in the package.  
`Tests/Editor/` | Editor platform specific tests folder. Refer to [Assembly definition and packages](cus-asmdef.html) to properly configure Editor-specific test assemblies in this folder.  
`Tests/Runtime/` | Runtime platform specific tests. Refer to [Assembly definition and packages](cus-asmdef.html) to properly configure runtime test assemblies in this folder.  
`Samples~/` | Folder to store any [samples included](cus-samples.html) in the package.  
`Documentation~` | Folder to store any [documentation included](cus-document.html) in the package.  
  
  

Unity ignores the contents of any folder name that ends with the `~`
character, and doesn’t track them with `.meta` files. However, you need to
include `.meta` files for the `Editor`, `Runtime`, and `Tests` folders and
their contents in order for them to work properly. For more information on
`.meta` files and how Unity uses them for tracking, refer to [Asset
workflow](AssetWorkflow.html).

[](cus-naming.html)

Naming your package

[](cus-tests.html)

Adding tests to a package

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

