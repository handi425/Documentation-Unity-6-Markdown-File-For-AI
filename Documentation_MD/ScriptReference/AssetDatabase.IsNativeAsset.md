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

#  [AssetDatabase](AssetDatabase.html).IsNativeAsset

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

public static bool IsNativeAsset([Object](Object.html) obj);

## Declaration

public static bool IsNativeAsset(int instanceID);

### Description

Determines whether the Asset is a native Asset.

A native Asset is a file produced directly by Unity's serialization system
(for example, a .mat Material file is a native Asset)  
  
Note that scenes, prefabs and assembly definitions are not considered to be
native assets.  
  
Additional resources:
[AssetDatabase.IsForeignAsset](AssetDatabase.IsForeignAsset.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/List All Native Files")]
        static void ListNativeFiles()
        {
            //List all native assets in the project
            foreach (var guid in [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("", new []{"Assets"}))
            {
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid);
                var asset = [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(path);
                if([AssetDatabase.IsNativeAsset](AssetDatabase.IsNativeAsset.html)(asset))
                    [Debug.Log](Debug.Log.html)(asset);
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

