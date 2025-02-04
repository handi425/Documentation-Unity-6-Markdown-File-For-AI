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
[AssetModificationProcessor](AssetModificationProcessor.html).OnWillMoveAsset(string,string)

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

### Description

Unity calls this method when it is about to move an Asset on disk.

Implement this method to customize the actions Unity performs when moving an
Asset inside the Editor. This method allows you to move the Asset yourself
but, if you do, please remember to return the correct enum. Alternatively, you
can perform some processing and let Unity move the file. The moving of the
asset can be prevented by returning
[AssetMoveResult.FailedMove](AssetMoveResult.FailedMove.html) You should not
call any Unity AssetDatabase API from within this callback, preferably
restrict yourself to the usage of file operations or VCS APIs.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class CustomAssetModificationProcessor : UnityEditor.AssetModificationProcessor
    {
        private static [AssetMoveResult](AssetMoveResult.html) OnWillMoveAsset(string sourcePath, string destinationPath)
        {
            [Debug.Log](Debug.Log.html)("Source path: " + sourcePath + ". Destination path: " + destinationPath + ".");
            [AssetMoveResult](AssetMoveResult.html) assetMoveResult = [AssetMoveResult.DidMove](AssetMoveResult.DidMove.html);  
      
            // Perform operations on the asset and set the value of 'assetMoveResult' accordingly.  
      
            return assetMoveResult;
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

