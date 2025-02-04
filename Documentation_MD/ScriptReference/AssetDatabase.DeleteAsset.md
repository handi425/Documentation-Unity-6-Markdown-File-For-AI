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

#  [AssetDatabase](AssetDatabase.html).DeleteAsset

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

public static bool DeleteAsset(string path);

### Parameters

path | Project relative path of the asset or folder to be deleted.  
---|---  
  
### Returns

**bool** Returns true if the asset has been successfully removed, false if it
doesn't exist or couldn't be removed.

### Description

Deletes the specified asset or folder.

Paths should be relative to the project folder, for example:
"Assets/MyTextures/hello.png"  
  
Additional resources:
[AssetDatabase.DeleteAssets](AssetDatabase.DeleteAssets.html),
[AssetDatabase.MoveAssetToTrash](AssetDatabase.MoveAssetToTrash.html),
[AssetDatabase.MoveAssetsToTrash](AssetDatabase.MoveAssetsToTrash.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Delete Files In 'Unused' [Folder](WSA.Folder.html)")]
        static void DeleteAllFilesInFolder()
        {
            //"Assets/Unused" folder should exist before running this Method
            string[] unusedFolder = { "Assets/Unused" };
            foreach (var asset in [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("", unusedFolder))
            {
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(asset);
                [AssetDatabase.DeleteAsset](AssetDatabase.DeleteAsset.html)(path);
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

