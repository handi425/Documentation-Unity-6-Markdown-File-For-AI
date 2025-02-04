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

#  [AssetDatabase](AssetDatabase.html).GetImplicitAssetBundleVariantName

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

public static string GetImplicitAssetBundleVariantName(string assetPath);

### Parameters

assetPath | The asset's path.  
---|---  
  
### Returns

**string** Returns the name of the AssetBundle Variant that a given asset
belongs to. See the method description for more details.

### Description

Returns the name of the AssetBundle Variant that a given asset belongs to.

If the asset has been explicitly assigned to an AssetBundle Variant, then that
value is returned. If the asset doesn't belong to an AssetBundle Variant, its
parent folders are traversed until one that belongs to an AssetBundle Variant
is found. If a folder that matches this condition is found, its AssetBundle
Variant name is returned. If none is found, an empty string is returned.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
     public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
     {
         [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Export Ground Textures")]
         static void ExportGroundTextures()
         {
             var groundTextures4k = new List<string>();
             var groundTextures2k = new List<string>();
             foreach (var guid in [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("l:Ground", new []{"Assets/Textures"}))
             {
                 var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid);
                 if([AssetDatabase.GetImplicitAssetBundleVariantName](AssetDatabase.GetImplicitAssetBundleVariantName.html)(path) == "4k")
                     groundTextures4k.Add(path);
                 else
                     groundTextures2k.Add(path);
             }
             [AssetDatabase.ExportPackage](AssetDatabase.ExportPackage.html)(groundTextures4k.ToArray(), "groundTextures4k.unitypackage");
             [AssetDatabase.ExportPackage](AssetDatabase.ExportPackage.html)(groundTextures2k.ToArray(), "groundTextures2k.unitypackage");
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

