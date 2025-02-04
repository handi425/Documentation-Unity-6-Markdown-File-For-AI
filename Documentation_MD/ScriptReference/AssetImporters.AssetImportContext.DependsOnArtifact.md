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
[AssetImportContext](AssetImporters.AssetImportContext.html).DependsOnArtifact

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

public void DependsOnArtifact(string path);

## Declaration

public void DependsOnArtifact(GUID guid);

## Declaration

public void
DependsOnArtifact([Experimental.ArtifactKey](Experimental.ArtifactKey.html)
key);

### Parameters

path | The path of the Asset whose artifact should be the dependency. Note: Although the dependency is the artifact (import result) which is stored in the library folder, this parameter is the path to the Asset in the Assets folder, and _not_ a path to the artifact in the Library folder.  
---|---  
guid | The guid of the artifact dependency.  
key | The artifact key of the artifact dependency.  
  
### Description

Setup artifact dependency to an asset.

An artifact dependency is a dependency where an Asset depends on the import
result (known as an artifact) of another Asset. If you change an Asset that
has been marked as a dependency, all Assets which depend on it will also get
reimported (after the dependency has been imported).  
  
Note: If you specify an Asset as a dependency that doesn't exist or hasn't yet
been imported, the dependency is still registered. It is registered as an un-
imported Asset. When the Asset is later imported, all Assets which depend on
it will also get reimported.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;  
      
    class TextureInfo : [ScriptableObject](ScriptableObject.html)
    {
        public int height;
    }  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "cube")]
    public class CubeWithTextureImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            var assetDependency = "Assets/MyTexture.png";  
      
            ctx.DependsOnArtifact(assetDependency);  
      
            var texture = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Texture](Texture.html)>(assetDependency);  
      
            if (texture != null)
            {
                var textureInfo = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<TextureInfo>();
                textureInfo.height = texture.height;
                ctx.AddObjectToAsset("TextureInfo", textureInfo);
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

