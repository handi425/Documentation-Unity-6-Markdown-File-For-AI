[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/cus-tests.html)
  * [中文](/cn/current/Manual/cus-tests.html)
  * [日本語](/ja/current/Manual/cus-tests.html)
  * [한국어](/kr/current/Manual/cus-tests.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/cus-tests.html)
  * [中文](/cn/current/Manual/cus-tests.html)
  * [日本語](/ja/current/Manual/cus-tests.html)
  * [한국어](/kr/current/Manual/cus-tests.html)

  * [Packages and feature sets](PackagesList.html)
  * [Creating custom packages](CustomPackages.html)
  * Adding tests to a package

[](cus-layout.html)

Package layout

[](cus-samples.html)

Creating samples for packages

# Adding tests to a package

As with any kind of development, it’s good practice to add tests to your
package. There are three things you must do to set up tests on your package:

  1. Create the C# test files and put them under the Tests folder.
  2. Create asmdef files for your tests.
  3. Enable tests for your package.

## Location of test files

You can add your test files to the Tests folder of your package in the
`Editor` and `Runtime` subfolders. For example, a simple package with tests
might look something like this:

    
    
    <package-root>
      ├── package.json
      ├── Editor
      │     ├── <company-name>.<package-name>.Editor.asmdef
      │     └── EditorExample.cs
      ├── Runtime
      │     ├── <company-name>.<package-name>.asmdef
      │     └── RuntimeExample.cs
      └── Tests
            ├── Editor
            │    ├── <company-name>.<package-name>.Editor.Tests.asmdef
            │    └── EditorExampleTest.cs
            └── Runtime
                 ├── <company-name>.<package-name>.Tests.asmdef
                 └── RuntimeExampleTest.cs
    
    

Each of those subfolders must contain an `.asmdef` file, which provides
references to the Editor and Runtime assemblies. The assembly definition files
also provide a reference to the test assembly files. For more information,
refer to Assembly definition files for tests.

## Assembly definition files for tests

Use the [Test Framework](https://docs.unity3d.com/Packages/com.unity.test-
framework@latest/)The Test Framework package (formerly called the Test Runner)
is a Unity tool that tests your code in both Edit mode and Play mode, and also
on target platforms such as Standalone, Android, or iOS. [More
info](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)  
See in [Glossary](Glossary.html#TestFramework) package to create or edit your
assembly definition files. For more information, refer to [Creating test
assemblies](https://docs.unity3d.com/Packages/com.unity.test-
framework@latest/index.html?subfolder=/manual/workflow-create-test-
assembly.html).

Although you can choose to edit assembly definition files directly, you need
to make sure to add the following references:

**Attribute** | **Type** | **Description**  
---|---|---  
**name** | String | The name of the assembly without the file extension.  
**references** | Array of Strings | References to the Editor and Runtime assemblies. Assembly definition files require different references, depending on the test type:   
\- For Editor tests, add a reference to the package’s Editor and Runtime
assemblies.  
\- For Runtime tests, add a reference to the package’s Runtime assembly only.  
**optionalUnityReferences** | Array of Strings | This list of Unity references must include `"TestAssemblies"` to mark the assembly as a test assembly. This adds references to the `nunit.framework.dll` and `UnityEngine.TestRunner.dll` libraries to the Assembly Definition.  
**includePlatforms** | Array of Strings | For the Editor test, this list of platforms must include the `"Editor"` platform.  
  
**Tip** : You can also edit the assembly definition files in the **Inspector**
A Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). Refer to [Assembly
Definitions](assembly-definition-files.html) for more information.

### Editor file example

The editor test `.asmdef` file looks like this:

    
    
    {
      "name": "MyCompany.MyPackage.Editor.Tests",
      "references": [
        "MyPackage.Editor",
        "MyPackage"
      ],
      "optionalUnityReferences": [
        "TestAssemblies"
      ],
      "includePlatforms": [
        "Editor"
      ],
      "excludePlatforms": []
    }
    
    

### Runtime file example

The runtime test `.asmdef` file looks like this:

    
    
    {
      "name": "MyCompany.MyPackage.Tests",
      "references": [
        "MyPackage"
      ],
      "optionalUnityReferences": [
        "TestAssemblies"
      ],
      "includePlatforms": [],
      "excludePlatforms": []
    }
    
    

## Enabling tests for a package

For **embedded packages** An _embedded_ package is a mutable package that you
store under the `Packages` directory at the root of a Unity project. This
differs from most packages which you download from a package server and are
immutable. [More info](upm-concepts.html#Embedded)  
See in [Glossary](Glossary.html#Embeddedpackage), you don’t need to explicitly
enable tests because embedded packages are in development.

However, for other types of dependencies, you need to add the [testables](upm-
manifestPrj.html#testables) attribute to the **Project manifest** Each Unity
project has a _project manifest_ , which acts as an entry point for the
Package Manager. This file must be available in the `<project>/Packages`
directory. The Package Manager uses it to configure many things, including a
list of dependencies for that project, as well as any package repository to
query for packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest) and add the names of packages
that have tests you want to run. That includes direct and **indirect
dependencies** An **indirect** , or transitive dependency occurs when your
project requests a package which itself “depends on” another package. For
example, if your project depends on the `alembic@1.0.7` package which in turn
depends on the `timeline@1.0.0` package, then your project has an direct
dependency on Alembic and an indirect dependency on Timeline. [More info](upm-
dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency) of the Project. For
example:

    
    
    {
      "dependencies": {
        "com.unity.some-package": "1.0.0",
        "com.unity.other-package": "2.0.0",
        "com.unity.yet-another-package": "3.0.0",
      },
      "testables": ["com.unity.some-package", "com.unity.other-package"]
    }
    
    

This example adds tests for the **com.unity._some-package_** and
**com.unity._other-package_** packages in Unity’s [Test
Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
package.

**Note** : You might need to import the package again, because the test
framework doesn’t always immediately pick up changes to the `testables`
attribute.

[](cus-layout.html)

Package layout

[](cus-samples.html)

Creating samples for packages

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

