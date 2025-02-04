[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# CollectImportedDependenciesAttribute

class in UnityEditor.AssetImporters

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Use this method attribute to specify which methods declare dependancies on
imported assets. The methods are called by [AssetDatabase](AssetDatabase.html)
during import.

The AssetDatabase imports the dependencies declared in methods with this
attribute before importing the dependent assets. This also re-imports the
dependent asset whenever the dependency asset changes. Use this declared
dependency to safely load dependancies in
[AssetPostprocessor](AssetPostprocessor.html) callbacks.  
  
This example shows how you can declare a dependency between two prefabs
imported by the [ModelImporter](ModelImporter.html) and use them in an
AssetPostprocessor.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;
    using UnityEngine;  
      
    public class ProceduralParentPostprocessor : [AssetPostprocessor](AssetPostprocessor.html)
    {
        private const string s_DependentPath = "Assets/ProceduralPrefab.fbx";
        private const string s_DependencyPath = "Assets/DependencyPrefab.fbx";  
      
        [CollectImportedDependencies(typeof([ModelImporter](ModelImporter.html)), 1)]
        public static string[] CollectImportedDependenciesForModelImporter(string assetPath)
        {
            if (assetPath.Equals(s_DependentPath))
                return new[] { s_DependencyPath };  
      
            return null;
        }  
      
        void OnPostprocessMeshHierarchy([GameObject](GameObject.html) root)
        {
            if (root.name == "ProceduralPrefabRoot")
            {
                // Add a new child game object
                var go = [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(s_DependencyPath) as [GameObject](GameObject.html);
                [Object.Instantiate](Object.Instantiate.html)(go, root.transform, true);
            }
        }
    }
    

**Note:** The attribute supports only native importer types with
[AssetPostprocessor](AssetPostprocessor.html) callbacks:
[ModelImporter](ModelImporter.html), [TextureImporter](TextureImporter.html),
[AudioImporter](AudioImporter.html), and
[SpeedTreeImporter](SpeedTreeImporter.html).

### Properties

[importerType](AssetImporters.CollectImportedDependenciesAttribute-
importerType.html)| The type of the importer for which the imported dependency
getter is declared.  
---|---  
[version](AssetImporters.CollectImportedDependenciesAttribute-version.html)|
The version of the imported dependency getter.  
  
### Constructors

[CollectImportedDependenciesAttribute](AssetImporters.CollectImportedDependenciesAttribute-
ctor.html)| Use the CollectImportedDependencies attribute to declare getters
for imported dependencies.  
---|---  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

