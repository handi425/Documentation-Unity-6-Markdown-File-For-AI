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

#  [AssetImporter](AssetImporter.html).AddRemap

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
AddRemap([AssetImporter.SourceAssetIdentifier](AssetImporter.SourceAssetIdentifier.html)
identifier, [Object](Object.html) externalObject);

### Parameters

identifier | The identifier of the sub-asset.  
---|---  
externalObject | The object to be mapped to the internal object. Can belong to another Prefab or Asset, but not the Asset that is being changed.  
  
### Description

Map a sub-asset from an imported asset (such as an FBX file) to an external
Asset of the same type.

Apply changes by writing the metadata and reimporting the Asset. Instances of
the Asset automatically use the mapped object once you have reimported the
Asset.  
  
If the type of the external asset does not match the type of the sub-asset, or
if the reference is null, instances of the Asset will continue to use the
internal asset without producing an error.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Extractor
    {
        public static void ExtractFromAsset(Object subAsset, string destinationPath)
        {
            string assetPath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(subAsset);  
      
            var clone = [Object.Instantiate](Object.Instantiate.html)(subAsset);
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(clone, destinationPath);  
      
            var assetImporter = [AssetImporter.GetAtPath](AssetImporter.GetAtPath.html)(assetPath);
            assetImporter.AddRemap(new [AssetImporter.SourceAssetIdentifier](AssetImporter.SourceAssetIdentifier.html)(subAsset), clone);  
      
            [AssetDatabase.WriteImportSettingsIfDirty](AssetDatabase.WriteImportSettingsIfDirty.html)(assetPath);
            [AssetDatabase.ImportAsset](AssetDatabase.ImportAsset.html)(assetPath, [ImportAssetOptions.ForceUpdate](ImportAssetOptions.ForceUpdate.html));
        }
    }
    

Additional resources:
[AssetImporter.RemoveRemap](AssetImporter.RemoveRemap.html).

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

