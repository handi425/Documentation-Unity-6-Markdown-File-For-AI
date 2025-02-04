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

#  [AssetDatabase](AssetDatabase.html).GetImplicitAssetBundleName

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

public static string GetImplicitAssetBundleName(string assetPath);

### Parameters

assetPath | The asset's path.  
---|---  
  
### Returns

**string** Returns the name of the AssetBundle that a given asset belongs to.
See the method description for more details.

### Description

Returns the name of the AssetBundle that a given asset belongs to.

If the asset has been explicitly assigned to an AssetBundle, then that value
is returned. If the asset doesn't belong to an AssetBundle, its parent folders
are traversed until one that belongs to an AssetBundle is found. If a folder
that matches this condition is found, its AssetBundle name is returned. If
none is found, an empty string is returned.

    
    
    using System.Collections.Generic;
    using System.Linq;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Check [Bundle](Unity.Android.Gradle.Bundle.html) Names")]
        static void CheckBundleNames()
        {
            var assetsWithIncorrectBundle = new List<string>();
            var correctBundleName = "metaltexturebundle";
            //Check if any of the assets have an incorrect bundle set to them
            for (var i = 0; i < 10; i++)
            {
                var texturePath = $"Assets/Textures/Metal/Metal{i}.png";
                if([AssetDatabase.GetImplicitAssetBundleName](AssetDatabase.GetImplicitAssetBundleName.html)(texturePath) != correctBundleName)
                    assetsWithIncorrectBundle.Add(texturePath);
            }  
      
            //If no such assets exist then return
            if (!assetsWithIncorrectBundle.Any())
                return;
            //If there are such assets then print them out
            var incorrectAssetNames = "";
            foreach (var asset in assetsWithIncorrectBundle)
            {
                incorrectAssetNames += $"\"{asset}\" ";
            }
            [Debug.LogWarning](Debug.LogWarning.html)($"Assets with an incorrect [Asset](VersionControl.Asset.html) [Bundle](Unity.Android.Gradle.Bundle.html) {incorrectAssetNames}");
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

