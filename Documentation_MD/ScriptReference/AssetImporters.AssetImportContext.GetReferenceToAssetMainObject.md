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
[AssetImportContext](AssetImporters.AssetImportContext.html).GetReferenceToAssetMainObject

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

public Object GetReferenceToAssetMainObject(string path);

### Parameters

path | The location of the asset to get the reference from.  
---|---  
  
### Returns

**Object** Returns the main asset instance if it exists and is already
imported, returns null otherwise.

### Description

Returns the main asset from the given path (if it exists) and automatically
adds a dependency on its path if it is the main asset type.

Calling this method during an import will make the current imported asset re-
import if: \- An asset is added at the given path, \- The type of the asset at
the given path changes, \- An existing asset at the given path is deleted or
moved.  
  
If the returned asset is used for more than referencing, like reading its
content and using its values,
[AssetImportContext.DependsOnArtifact](AssetImporters.AssetImportContext.DependsOnArtifact.html)
or
[AssetImportContext.DependsOnSourceAsset](AssetImporters.AssetImportContext.DependsOnSourceAsset.html)
should be used instead.  
  
For example, this method should be used to reference Textures added to or
created during an import. Since we are only setting a reference to the texture
from the Material, it is not necessary to re-import when the texture itself
changes, only when it is added or removed from the project.

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "customMaterial")]
    public class MaterialCreatorExample : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            var mat = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));
            var texturePath = $"{System.IO.Path.GetDirectoryName(ctx.assetPath)}/{System.IO.Path.GetFileNameWithoutExtension(ctx.assetPath)}_Diffuse.png";
            mat.mainTexture = ctx.GetReferenceToAssetMainObject(texturePath) as [Texture2D](Texture2D.html);
            ctx.AddObjectToAsset("mat", mat);
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

