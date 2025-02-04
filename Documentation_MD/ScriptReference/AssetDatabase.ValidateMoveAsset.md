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

#  [AssetDatabase](AssetDatabase.html).ValidateMoveAsset

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

public static string ValidateMoveAsset(string oldPath, string newPath);

### Parameters

oldPath | The path where the asset currently resides.  
---|---  
newPath | The path which the asset should be moved to.  
  
### Returns

**string** An empty string if the asset can be moved, otherwise an error
message.

### Description

Checks if an asset file can be moved from one folder to another. (Without
actually moving the file).

All paths are relative to the project folder, for example:
"Assets/MyTextures/hello.png".  
  
Additional resources: [AssetDatabase.MoveAsset](AssetDatabase.MoveAsset.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Move With Validate")]
        public static void MoveWithValidate()
        {
            for (var i = 0; i < 5; i++)
            {
                var oldPath = $"Assets/Textures/Building/BuildingTexture{i}.png";
                var newPath = $"Assets/Textures/Construction/BuildingTexture{i}.png";
                var moveResult = [AssetDatabase.ValidateMoveAsset](AssetDatabase.ValidateMoveAsset.html)(oldPath, newPath);  
      
                if (moveResult == "")
                    [AssetDatabase.MoveAsset](AssetDatabase.MoveAsset.html)(oldPath, newPath);
                else
                    [Debug.LogError](Debug.LogError.html)($"Couldn't move {oldPath} because {moveResult}");
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

