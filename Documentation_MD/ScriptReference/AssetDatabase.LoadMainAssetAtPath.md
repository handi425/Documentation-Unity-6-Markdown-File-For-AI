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

#  [AssetDatabase](AssetDatabase.html).LoadMainAssetAtPath

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

public static Object LoadMainAssetAtPath(string assetPath);

### Parameters

assetPath | Filesystem path of the asset to load.  
---|---  
  
### Description

Returns the main asset object at `assetPath`.  
  
The "main" Asset is the Asset at the root of a hierarchy (such as a Maya file
which may contain multiples meshes and GameObjects).

All paths are relative to the project folder, for example:
"Assets/MyTextures/hello.png".  
  
Additional resources:
[AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html),
[AssetDatabase.LoadAllAssetsAtPath](AssetDatabase.LoadAllAssetsAtPath.html),
[AssetDatabase.LoadAllAssetRepresentationsAtPath](AssetDatabase.LoadAllAssetRepresentationsAtPath.html).

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MyPlayer : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Assign Materials To Models")]
        static void AssignGunMaterialsToModels()
        {
            var materials = new List<[Material](Material.html)>();
            //Get all the materials that have the name gun in them using LoadMainAssetAtPath
            foreach (var asset in [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:[Material](Material.html) gun"))
            {
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(asset);
                materials.Add(([Material](Material.html))[AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(path));
            }  
      
            var materialID = 0;
            //Assign gun materials to their corresponding models [MeshRenderer](MeshRenderer.html)
            foreach (var asset in [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:Model Gun"))
            {
                if (materialID >= materials.Count) materialID = 0;
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(asset);
                var material = materials[materialID++];
                material.shader = [Shader.Find](Shader.Find.html)("Standard");
                var modelMesh = ([MeshRenderer](MeshRenderer.html)) [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)(path, typeof([MeshRenderer](MeshRenderer.html)));
                modelMesh.sharedMaterial = material;
            }
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

