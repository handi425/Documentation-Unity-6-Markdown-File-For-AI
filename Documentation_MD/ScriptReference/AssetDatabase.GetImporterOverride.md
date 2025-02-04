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

#  [AssetDatabase](AssetDatabase.html).GetImporterOverride

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

public static Type GetImporterOverride(string path);

### Parameters

path | Asset path.  
---|---  
  
### Returns

**Type** Importer type.

### Description

Returns the type of the override importer.

Returns null if there isn't one.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;
    using UnityEngine.Assertions;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Example Importer Actions")]
        static void AllImporterActions()
        {
            //This sets CubeImporter to be used for the asset
            [AssetDatabase.SetImporterOverride](AssetDatabase.SetImporterOverride.html)<CubeImporter>("Assets/CompanionCube.cube");
            [Debug.Log](Debug.Log.html)("New importer: " + [AssetDatabase.GetImporterOverride](AssetDatabase.GetImporterOverride.html)("Assets/CompanionCube.cube"));  
      
            //This clears importer override and sets it to null
            [AssetDatabase.ClearImporterOverride](AssetDatabase.ClearImporterOverride.html)("Assets/CompanionCube.cube");
            [Assert.IsNull](Assertions.Assert.IsNull.html)([AssetDatabase.GetImporterOverride](AssetDatabase.GetImporterOverride.html)("Assets/CompanionCube.cube"));
        }
    }  
      
    //This is Example Importer
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "cube")]
    public class CubeImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public float m_Scale = 1;
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            var cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            var position = new [Vector3](Vector3.html)(0, 0, 0);
            cube.transform.position = position;
            cube.transform.localScale = new [Vector3](Vector3.html)(m_Scale, m_Scale, m_Scale);
            // 'cube' is a [GameObject](GameObject.html) and will be automatically converted into a prefab
            ctx.AddObjectToAsset("main obj", cube);
            ctx.SetMainObject(cube);
            var material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));
            material.color = [Color.red](Color-red.html);
            ctx.AddObjectToAsset("my [Material](Material.html)", material);
            var tempMesh = new [Mesh](Mesh.html)();
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

