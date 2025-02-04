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

#  [AssetDatabase](AssetDatabase.html).ExportPackage

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

## Declaration

public static void ExportPackage(string assetPathName, string fileName);

## Declaration

public static void ExportPackage(string assetPathName, string fileName,
[ExportPackageOptions](ExportPackageOptions.html) flags);

## Declaration

public static void ExportPackage(string[] assetPathNames, string fileName,
[ExportPackageOptions](ExportPackageOptions.html) flags =
ExportPackageOptions.Default);

### Description

Exports the assets identified by **assetPathNames** to a unitypackage file in
**fileName**.

Additional resources: ExportPackageOptions for information on how you can
affect what gets exported.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Export")]
        static void Export()
        {
            var exportedPackageAssetList = new List<string>();
            //Find all shaders that have "Surface" in their names and add them to the list
            foreach (var guid in [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:[Shader](Shader.html) Surface", new []{"Assets/Shaders"}))
            {
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid);
                exportedPackageAssetList.Add(path);
            }  
      
            //Add Prefabs folder into the asset list
            exportedPackageAssetList.Add("Assets/Prefabs");
            //Export Shaders and Prefabs with their dependencies into a .unitypackage
            [AssetDatabase.ExportPackage](AssetDatabase.ExportPackage.html)(exportedPackageAssetList.ToArray(), "ShadersAndPrefabsWithDependencies.unitypackage",
                [ExportPackageOptions.Recurse](ExportPackageOptions.Recurse.html) | [ExportPackageOptions.IncludeDependencies](ExportPackageOptions.IncludeDependencies.html));
        }
    }

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

