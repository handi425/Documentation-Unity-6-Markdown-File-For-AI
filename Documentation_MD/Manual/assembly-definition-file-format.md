[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/assembly-definition-file-format.html)
  * [中文](/cn/current/Manual/assembly-definition-file-format.html)
  * [日本語](/ja/current/Manual/assembly-definition-file-format.html)
  * [한국어](/kr/current/Manual/assembly-definition-file-format.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/assembly-definition-file-format.html)
  * [中文](/cn/current/Manual/assembly-definition-file-format.html)
  * [日本語](/ja/current/Manual/assembly-definition-file-format.html)
  * [한국어](/kr/current/Manual/assembly-definition-file-format.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Organizing scripts into assemblies](assembly-definition-files.html)
  * Assembly Definition File Format reference

[](class-AssemblyDefinitionReferenceImporter.html)

Assembly Definition Reference properties reference

[](managed-code-stripping.html)

Managed code stripping

# Assembly Definition File Format reference

Assembly Definition and Assembly Definition Reference assets are JSON files.
You can edit the asset files inside the Unity Editor using the **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, but you can also modify the
JSON content with an external tool.

## Assembly Definition JSON

An Assembly Definition is a JSON object with the following fields:

#### allowUnsafeCode bool

Optional. Defaults to false. See [Allow ‘unsafe’ Code](class-
AssemblyDefinitionImporter.html#general).

    
    
    "allowUnsafeCode" : true
    

#### autoReferenced bool

Optional. Defaults to true. See [Auto Referenced](class-
AssemblyDefinitionImporter.html#general).

    
    
    "autoReferenced": false
    

#### defineConstraints string[]

Optional. The symbols that serve as constraints. Can be empty. See [Define
Constraints](class-AssemblyDefinitionImporter.html#define-constraints).

    
    
    "defineConstraints": [
            "UNITY_2019",
            "UNITY_INCLUDE_TESTS"
        ]
    

#### excludePlatforms string[]

Optional. The platform name strings to exclude or an empty array. The
excludePlatforms array must be empty if includePlatforms contains values. You
can retrieve the platform name strings with the
[CompilationPipeline.GetAssemblyDefinitionPlatforms](ScriptRef:CompilationPipeline.GetAssemblyDefinitionPlatforms.html)
function (support for a platform must be installed for the current Editor when
calling this function.) See [Platforms](class-
AssemblyDefinitionImporter.html#platforms).

    
    
    "includePlatforms": [],
    "excludePlatforms": [
            "iOS",
            "macOSStandalone",
            "tvOS"
    ]
    

#### includePlatforms string[]

Optional. The platform name strings to include or an empty array. The
includePlatforms array must be empty if excludePlatforms contains values. You
can retrieve the platform name strings with the
[CompilationPipeline.GetAssemblyDefinitionPlatforms](ScriptRef:CompilationPipeline.GetAssemblyDefinitionPlatforms.html)
function (support for a platform must be installed for the current Editor when
calling this function.) See [Platforms](class-
AssemblyDefinitionImporter.html#platforms).

    
    
    "includePlatforms": [
            "Android",
            "LinuxStandalone64",
            "WebGL"
    ],
    "excludePlatforms": []
    

#### name string

Required. Any [legal assembly name](https://docs.microsoft.com/en-
us/dotnet/standard/assembly/names).

    
    
    "name" : "MyAssemblyName" 
    

#### noEngineReferences bool

Optional. Defaults to false. See [No Engine References](class-
AssemblyDefinitionImporter.html#general).

    
    
    "noEngineReferences": false
    

#### optionalUnityReferences string[]

Optional. In earlier versions of Unity, this field serialized the **Unity
References : Test Assemblies** option used to designate the assembly as a test
assembly. As of Unity 2019.3, the option is no longer displayed. The field is
still supported, but if the asset is reserialized in a newer version of the
Unity Editor, the field is replaced by the equivalent assembly references.

See [Creating a test assembly](assembly-definition-files.html#create-test-
assembly) for more information about test assemblies.

    
    
    "optionalUnityReferences": [
        "TestAssemblies"
      ]
    

#### overrideReferences bool

Optional. Set to true if precompiledReferences contains values. Defaults to
false.

See [Override References].

    
    
    "overrideReferences": true
    

#### precompiledReferences string[]

Optional. The file names of referenced DLL libraries including extension, but
without other path elements. Can be empty. This array is ignored unless you
set overrideReferences to true.

See [Assembly References](class-AssemblyDefinitionImporter.html#assembly-
references).

    
    
    "overrideReferences": true,
    "precompiledReferences": [
            "Newtonsoft.Json.dll",
            "nunit.framework.dll"
    ]
    

#### references string[]

Optional. References to other assemblies created with Assembly Definition
assets. You can use either the GUID of the Assembly Definition asset file or
the name of the assembly (as defined by the [name](class-
AssemblyDefinitionImporter.html#name) field of the Assembly Definition). You
must use the same form for all references in the list. Can be empty.

You can use the
[AssetDatabase.AssetPathToGUID](ScriptRef:AssetDatabase.AssetPathToGUID.html)
function to retrieve the GUID of an asset. (The GUID is also part of the
metadata associated with every asset.)

Note that the Editor displays a **Use GUIDs** option in the Assembly
Definition Inspector. This option is not serialized in the associated JSON
file. Instead, the choice is inferred from the form of reference found in the
file.

See [Referencing another assembly](assembly-definition-files.html#reference-
another-assembly).

Using GUIDs:

    
    
    "references": [
            "GUID:17b36165d09634a48bf5a0e4bb27f4bd",
            "GUID:b470eee7144904e59a1064b70fa1b086",
            "GUID:2bafac87e7f4b9b418d9448d219b01ab",
            "GUID:27619889b8ba8c24980f49ee34dbb44a",
            "GUID:0acc523941302664db1f4e527237feb3"
    ]
    

Using assembly names:

    
    
    "references": [
            "Unity.CollabProxy.Editor",
            "AssemblyB",
            "UnityEngine.UI",
            "UnityEngine.TestRunner",
            "UnityEditor.TestRunner"
    ]
    

#### versionDefines object[]

Optional. Contains an object for each version define. This object has three
fields:

  * name:string – the name of the resource
  * expression:string – the expression defining the version or range of versions of the resource
  * define:string – the symbol to define

See [Version Defines](class-AssemblyDefinitionImporter.html#version-defines).

    
    
    "versionDefines": [
        {
            "name": "com.unity.ide.vscode",
            "expression": "[1.7,2.4.1]",
            "define": "MY_SYMBOL"
        },
        {
            "name": "com.unity.test-framework",
            "expression": "[2.7.2-preview.8]",
            "define": "TESTS"
        }
    ]
    

### Example Assembly Definition JSON strings

Using assembly names for references to other Assembly Definitions and
_includePlatforms_ :

    
    
    {
        "name": "BeeAssembly",
        "references": [
            "Unity.CollabProxy.Editor",
            "AssemblyB",
            "UnityEngine.UI",
            "UnityEngine.TestRunner",
            "UnityEditor.TestRunner"
        ],
        "includePlatforms": [
            "Android",
            "LinuxStandalone64",
            "WebGL"
        ],
        "excludePlatforms": [],
        "overrideReferences": true,
        "precompiledReferences": [
            "Newtonsoft.Json.dll",
            "nunit.framework.dll"
        ],
        "autoReferenced": false,
        "defineConstraints": [
            "UNITY_2019",
            "UNITY_INCLUDE_TESTS"
        ],
        "versionDefines": [
            {
                "name": "com.unity.ide.vscode",
                "expression": "[1.7,2.4.1]",
                "define": "MY_SYMBOL"
            },
            {
                "name": "com.unity.test-framework",
                "expression": "[2.7.2-preview.8]",
                "define": "TESTS"
            }
        ],
        "noEngineReferences": false
    }
    

Using GUIDS for references to other Assembly Definitions and
_excludePlatforms_ :

    
    
    {
        "name": "BeeAssembly",
        "references": [
            "GUID:17b36165d09634a48bf5a0e4bb27f4bd",
            "GUID:b470eee7144904e59a1064b70fa1b086",
            "GUID:2bafac87e7f4b9b418d9448d219b01ab",
            "GUID:27619889b8ba8c24980f49ee34dbb44a",
            "GUID:0acc523941302664db1f4e527237feb3"
        ],
        "includePlatforms": [],
        "excludePlatforms": [
            "iOS",
            "macOSStandalone",
            "tvOS"
        ],
        "allowUnsafeCode": false,
        "overrideReferences": true,
        "precompiledReferences": [
            "Newtonsoft.Json.dll",
            "nunit.framework.dll"
        ],
        "autoReferenced": false,
        "defineConstraints": [
            "UNITY_2019",
            "UNITY_INCLUDE_TESTS"
        ],
        "versionDefines": [
            {
                "name": "com.unity.ide.vscode",
                "expression": "[1.7,2.4.1]",
                "define": "MY_SYMBOL"
            },
            {
                "name": "com.unity.test-framework",
                "expression": "[2.7.2-preview.8]",
                "define": "TESTS"
            }
        ],
        "noEngineReferences": false
    }
    

## Assembly Definition Reference JSON

An Assembly Definition Reference is a JSON object with the following field:

#### reference string

Required. The assembly definition to reference. See [Assembly Definition
References](class-AssemblyDefinitionReferenceImporter.html).

You can reference an Assembly Definition asset using either the name of the
assembly or the GUID of the asset.You can use the
[AssetDatabase.AssetPathToGUID](ScriptRef:AssetDatabase.AssetPathToGUID.html)
function to retrieve the GUID of an asset. (The GUID is also part of the
metadata associated with every asset.)

Using assembly name:

    
    
    {
        "reference": "AssemblyA"
    }
    

Using Assembly Definition asset GUID

    
    
    {
        "reference": "GUID:f4de40948f4904ecb94b59dd38aab8a1"
    }
    

See [Creating an Assembly Definition Reference asset](assembly-definition-
files.html#create-asmref).

[](class-AssemblyDefinitionReferenceImporter.html)

Assembly Definition Reference properties reference

[](managed-code-stripping.html)

Managed code stripping

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

