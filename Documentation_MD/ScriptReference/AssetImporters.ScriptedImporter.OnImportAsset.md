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

#  [ScriptedImporter](AssetImporters.ScriptedImporter.html).OnImportAsset

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

public void
OnImportAsset([AssetImporters.AssetImportContext](AssetImporters.AssetImportContext.html)
ctx);

### Parameters

ctx | This argument contains all the contextual information needed to process the import event and is also used by the custom importer to store the resulting Unity Asset.  
---|---  
  
### Description

This method must by overriden by the derived class and is called by the Asset
pipeline to import files.

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;
    using System.IO;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "cube")]
    public class CubeImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public float m_Scale = 1;  
      
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            var cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            var position = [JsonUtility.FromJson](JsonUtility.FromJson.html)<[Vector3](Vector3.html)>(File.ReadAllText(ctx.assetPath));  
      
            cube.transform.position = position;
            cube.transform.localScale = new [Vector3](Vector3.html)(m_Scale, m_Scale, m_Scale);  
      
            // 'cube' is a a [GameObject](GameObject.html) and will be automatically converted into a Prefab
            // (Only the 'Main [Asset](VersionControl.Asset.html)' is elligible to become a Prefab.)
            ctx.AddObjectToAsset("main obj", cube);
            ctx.SetMainObject(cube);  
      
            var material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));
            ctx.DependsOnCustomDependency("StandardShaderDependencyHash");  
      
            material.color = [Color.red](Color-red.html);  
      
            // Assets must be assigned a unique identifier string consistent across imports
            ctx.AddObjectToAsset("my [Material](Material.html)", material);  
      
            // Assets that are not passed into the context as import outputs must be destroyed
            var tempMesh = new [Mesh](Mesh.html)();
            DestroyImmediate(tempMesh);
        }
    }
    

To use the Shader.Find() function in the above example, you need to write a
custom dependency for the shader you want to find and regularly update it.
This prevents the Shader.Find() function from bypassing other means of
dependency checking. The below code is an example of how you might write a
custom dependency for this purpose.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    static class ShaderDependencyUpdater
    {
        [InitializeOnLoadMethod]
        static void ShaderDependencyInit()
        {
            [EditorApplication.update](EditorApplication-update.html) += ShaderDependencyUpdate;
        }
        static void ShaderDependencyUpdate()
        {
            var shader = [Shader.Find](Shader.Find.html)("Standard");
            [AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(shader, out var guid, out long id);
            var hash = new [Hash128](Hash128.html)();
            hash.Append(guid);
            hash.Append(id);
            [AssetDatabase.RegisterCustomDependency](AssetDatabase.RegisterCustomDependency.html)("StandardShaderDependencyHash", hash);
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

