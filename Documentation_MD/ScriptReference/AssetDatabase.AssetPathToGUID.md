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

#  [AssetDatabase](AssetDatabase.html).AssetPathToGUID

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

public static string AssetPathToGUID(string path);

## Declaration

public static string AssetPathToGUID(string path,
[AssetPathToGUIDOptions](AssetPathToGUIDOptions.html) options =
AssetPathToGUIDOptions.IncludeRecentlyDeletedAssets);

### Parameters

path | Filesystem path for the asset.  
---|---  
options | Specifies whether this method should return a GUID for recently deleted assets. The default value is [AssetPathToGUIDOptions.IncludeRecentlyDeletedAssets](AssetPathToGUIDOptions.IncludeRecentlyDeletedAssets.html).  
  
### Returns

**string** GUID.

### Description

Get the GUID for the asset at `path`.

All paths are relative to the project folder, for example:
"Assets/MyTextures/hello.png".  
  
When you delete an asset, the GUID for that asset remains in Unity's asset
database until you close the Editor. As a result, by default this method will
still return GUIDs for assets that were deleted in the current session of the
Unity Editor.  
  
For assets that do not exist, and were not deleted in the current Editor
session, this method returns an empty string.  
  
If you need it to return an empty string for assets that were deleted in the
current Editor session, pass the value
[AssetPathToGUIDOptions.OnlyExistingAssets](AssetPathToGUIDOptions.OnlyExistingAssets.html)
as the "options" parameter.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/AssetPathToGUID")]
        static void Doit()
        {
            // texture.jpg exists or was recently deleted
            string t = [AssetDatabase.AssetPathToGUID](AssetDatabase.AssetPathToGUID.html)("Assets/texture.jpg");
            [Debug.Log](Debug.Log.html)(t); // t will be not null
        }  
      
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/AssetPathToGUID Existing Assets Only")]
        static void DoitExistingAssetsOnly()
        {
            // texture.jpg does not exist on disk
            string t = [AssetDatabase.AssetPathToGUID](AssetDatabase.AssetPathToGUID.html)("Assets/texture.jpg", [AssetPathToGUIDOptions.OnlyExistingAssets](AssetPathToGUIDOptions.OnlyExistingAssets.html));
            [Debug.Log](Debug.Log.html)(t); // t will be null
        }
    }
    

See [AssetDatabase.GUIDFromAssetPath](AssetDatabase.GUIDFromAssetPath.html)
for a version that returns a UnityEditor.GUID instead of a string.

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

