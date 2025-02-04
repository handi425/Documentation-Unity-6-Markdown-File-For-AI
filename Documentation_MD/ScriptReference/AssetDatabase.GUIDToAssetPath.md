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

#  [AssetDatabase](AssetDatabase.html).GUIDToAssetPath

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

public static string GUIDToAssetPath(string guid);

## Declaration

public static string GUIDToAssetPath(GUID guid);

### Parameters

guid | The GUID of an asset.  
---|---  
  
### Returns

**string** Path of the asset relative to the project folder.

### Description

Gets the corresponding asset path for the supplied GUID, or an empty string if
the GUID can't be found.

Returned paths are relative to the project folder, for example:
"Assets/MyTextures/hello.png".

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class GUIDToAssetPathExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("APIExamples/GUIDToAssetPath")]
        static void MaterialPathsInProject()
        {
            var allMaterials = [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t: [Material](Material.html)");  
      
            foreach (var guid in allMaterials)
            {
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid);
                [Debug.Log](Debug.Log.html)(path);
            }
        }
    }
    

See [AssetDatabase.AssetPathToGUID](AssetDatabase.AssetPathToGUID.html) for a
version that returns a string instead of a UnityEditor.GUID.

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

