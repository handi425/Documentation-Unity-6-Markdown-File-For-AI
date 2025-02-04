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

#  [AssetDatabase](AssetDatabase.html).GetAssetBundleDependencies

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

public static string[] GetAssetBundleDependencies(string assetBundleName, bool
recursive);

### Parameters

assetBundleName | The name of the AssetBundle for which dependencies are required.  
---|---  
recursive | If false, returns only AssetBundles which are direct dependencies of the input; if true, includes all indirect dependencies of the input.  
  
### Returns

**string[]** The names of all AssetBundles that the input depends on.

### Description

Given an **assetBundleName** , returns the list of AssetBundles that it
depends on.

    
    
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Find Bundles With [Dependencies](Unity.Android.Gradle.Dependencies.html)")]
        static void BundleDependency()
        {
            var allBundleNames = [AssetDatabase.GetAllAssetBundleNames](AssetDatabase.GetAllAssetBundleNames.html)();
            foreach (var bundle in allBundleNames)
            {
                var dependencies = [AssetDatabase.GetAssetBundleDependencies](AssetDatabase.GetAssetBundleDependencies.html)(bundle, true);
                if (dependencies.Length == 0)
                    continue;
                var dependencyString = new StringBuilder();
                foreach (var dependency in dependencies)
                {
                    dependencyString.Append($"\"{dependency}\" ");
                }
                [Debug.Log](Debug.Log.html)($"{bundle} depends on {dependencyString}");
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

