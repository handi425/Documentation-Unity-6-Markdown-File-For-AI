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

#
[AssetImportContext](AssetImporters.AssetImportContext.html).DependsOnSourceAsset

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

public void DependsOnSourceAsset(string path);

## Declaration

public void DependsOnSourceAsset(GUID guid);

### Parameters

path | The path of the source dependency.  
---|---  
guid | The guid of the source asset dependency.  
  
### Description

Allows you to specify that an Asset depends directly on the source file of
another Asset (as opposed to the import result of another asset).

When you specify that one asset depends on another (eg, Asset A depends on
Assset B), it means if that Asset B is modified, not only will Asset B be
reimported, but also Asset A will be reimported.  
  
Note: This methods sets up a dependency on the Asset source file itself, not
the import result (the artifact) of the Asset. If you want to set up a
dependency on the import result of an asset, use
[DependsOnArtifact](AssetImporters.AssetImportContext.DependsOnArtifact.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;
    using System.IO;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "cube")]
    public class CubeWithTextureImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            var cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));  
      
            ctx.AddObjectToAsset("main obj", cube);
            ctx.SetMainObject(cube);  
      
            var material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));  
      
            var lines = File.ReadAllLines(ctx.assetPath);
            var texturePath = lines[0];
            var texture = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Texture](Texture.html)>(texturePath);
            if (texture != null)
            {
                material.SetTexture("_MainTex", texture);
                // add a dependency on the texture, such that if it changes or moves, we reimport the asset
                ctx.DependsOnSourceAsset(texturePath);
            }  
      
            ctx.AddObjectToAsset("MaterialWithTexture", material);
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

