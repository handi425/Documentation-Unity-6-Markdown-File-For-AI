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

#  [AssetDatabase](AssetDatabase.html).RemoveAssetBundleName

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

public static bool RemoveAssetBundleName(string assetBundleName, bool
forceRemove);

### Parameters

assetBundleName | The assetBundle name you want to remove.  
---|---  
forceRemove | Flag to indicate if you want to remove the assetBundle name even it's in use.  
  
### Description

Remove the assetBundle name from the asset database. The forceRemove flag is
used to indicate if you want to remove it even it's in use.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Remove [Bundle](Unity.Android.Gradle.Bundle.html) Name")]
        static void RemoveAssetBundleNameExample()
        {
            //Remove [Asset](VersionControl.Asset.html) [Bundle](Unity.Android.Gradle.Bundle.html) name that is on Cube.prefab and it's dependencies
            var prefabPath = "Assets/Prefabs/Cube.prefab";
            var assetBundleName = [AssetDatabase.GetImplicitAssetBundleName](AssetDatabase.GetImplicitAssetBundleName.html)(prefabPath);
            var assetBundleDependencies = [AssetDatabase.GetAssetBundleDependencies](AssetDatabase.GetAssetBundleDependencies.html)(assetBundleName, true);
            [AssetDatabase.RemoveAssetBundleName](AssetDatabase.RemoveAssetBundleName.html)(assetBundleName, true);
            foreach (var bundleName in assetBundleDependencies)
            {
                [AssetDatabase.RemoveAssetBundleName](AssetDatabase.RemoveAssetBundleName.html)(bundleName, true);
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

