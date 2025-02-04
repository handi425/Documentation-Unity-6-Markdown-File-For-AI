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
[AssetDatabase](AssetDatabase.html).GetAssetPathsFromAssetBundleAndAssetName

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

public static string[] GetAssetPathsFromAssetBundleAndAssetName(string
assetBundleName, string assetName);

### Description

Get the Asset paths for all Assets tagged with assetBundleName and named
assetName.

Get the Asset paths for all Assets tagged with assetBundleName and named
assetName, regardless of extension or path e.g. "Assets/House.prefab",
"Assets/Textures/House.png" and "Assets/Data/House.xml" when assetName is
"House".

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class ExampleScript
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/[Display](Display.html) assets in an [AssetBundle](AssetBundle.html)")]
        static void ExampleScriptCode1()
        {
            string[] assetPaths = [AssetDatabase.GetAssetPathsFromAssetBundleAndAssetName](AssetDatabase.GetAssetPathsFromAssetBundleAndAssetName.html)("assetname", "House");
            foreach (var assetPath in assetPaths)
                [Debug.Log](Debug.Log.html)(assetPath);
        }  
      
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/[AssetBundle](AssetBundle.html) creation")]
        static void ExampleScriptCode2()
        {
            [BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html)("Assets/AssetBundles", [BuildAssetBundleOptions.None](BuildAssetBundleOptions.None.html), [BuildTarget.StandaloneOSX](BuildTarget.StandaloneOSX.html));
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

