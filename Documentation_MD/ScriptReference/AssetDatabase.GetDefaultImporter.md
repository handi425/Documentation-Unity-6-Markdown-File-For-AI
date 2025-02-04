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

#  [AssetDatabase](AssetDatabase.html).GetDefaultImporter

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

public static Type GetDefaultImporter(string path);

### Parameters

path | Asset path.  
---|---  
  
### Returns

**Type** Importer type.

### Description

Returns the Default Importer associated with the asset located at the supplied
path. When no Importer override is set, then the default importer is used.
Additional resources:
[AssetDatabase.GetImporterOverride](AssetDatabase.GetImporterOverride.html),
[AssetDatabase.ClearImporterOverride](AssetDatabase.ClearImporterOverride.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Available Importer Types for cube")]
        static void AvailableImporterTypeCube()
        {
            var path = "Assets/CompanionCube.fbx";
            [AssetDatabase.GetDefaultImporter](AssetDatabase.GetDefaultImporter.html)(path);
            // returns [ModelImporter](ModelImporter.html).
            [AssetDatabase.GetImporterOverride](AssetDatabase.GetImporterOverride.html)(path);
            // returns null because no Override Importer is set.
            [AssetDatabase.GetAvailableImporters](AssetDatabase.GetAvailableImporters.html)(path);
            // returns [CubeImporter].
            [AssetDatabase.SetImporterOverride](AssetDatabase.SetImporterOverride.html)<CubeImporter>(path);
            // sets CubeImporter as Override Importer.
            [AssetDatabase.ClearImporterOverride](AssetDatabase.ClearImporterOverride.html)(path);
            // removes the Override Importer.
            [AssetDatabase.GetImporterOverride](AssetDatabase.GetImporterOverride.html)(path);
            // returns null because no Override Importer is set.
        }  
      
        //This is Example Importer for cube
        [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, new []{"cube" }, new[] { "fbx" })]
        public class CubeImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
        {
            public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
            {
                var cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                cube.transform.position = new [Vector3](Vector3.html)(0, 0, 0);
                // 'cube' is a [GameObject](GameObject.html) and will be automatically converted into a prefab
                ctx.AddObjectToAsset("main obj", cube);
                ctx.SetMainObject(cube);
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

