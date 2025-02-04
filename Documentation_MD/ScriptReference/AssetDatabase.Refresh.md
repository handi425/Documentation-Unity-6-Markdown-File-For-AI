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

#  [AssetDatabase](AssetDatabase.html).Refresh

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

public static void Refresh([ImportAssetOptions](ImportAssetOptions.html)
options = ImportAssetOptions.Default);

### Description

Import any changed assets.

This will import any assets that have changed their content modification data
or have been added-removed to the project folder.  
  
This method implicitly triggers an asset garbage collection (see
[Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html)).  
  
Additional resources: [ImportAssetOptions](ImportAssetOptions.html).

    
    
    using System.Collections.Generic;
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Refresh Example")]
        public static void RefreshExample()
        {
            var folderList = new List<string>{"Textures", "Models", "Sounds"};
            foreach (var folder in folderList)
            {
                [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)($"Assets/{folder}");
            }  
      
            foreach (var folder in folderList)
            {
                //Output will be false
                [Debug.Log](Debug.Log.html)([AssetDatabase.IsValidFolder](AssetDatabase.IsValidFolder.html)($"Assets/{folder}"));
            }  
      
            [AssetDatabase.Refresh](AssetDatabase.Refresh.html)();
            foreach (var folder in folderList)
            {
                //Output will be true
                [Debug.Log](Debug.Log.html)([AssetDatabase.IsValidFolder](AssetDatabase.IsValidFolder.html)($"Assets/{folder}"));
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

