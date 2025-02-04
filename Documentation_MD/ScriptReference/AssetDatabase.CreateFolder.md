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

#  [AssetDatabase](AssetDatabase.html).CreateFolder

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

public static string CreateFolder(string parentFolder, string newFolderName);

### Parameters

parentFolder | The path to the parent folder. Must start with "Assets/".  
---|---  
newFolderName | The name of the new folder.  
  
### Returns

**string** The GUID of the newly created folder, if the folder was created
successfully. Otherwise returns an empty string.

### Description

Creates a new folder, in the specified parent folder.  
  
The parent folder string must start with the "Assets" folder, and all folders
within the parent folder string must already exist. For example, when
specifying "Assets/ParentFolder1/Parentfolder2/", the new folder will be
created in "ParentFolder2" only if ParentFolder1 and ParentFolder2 already
exist.

Note: When Unity attempts to create a folder, if a folder with the same name
exists at the same path, Unity adds a sequential number to the end of the file
name. For example, "My Folder" becomes "My Folder 1".

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CreateFolderExample
    {
        [[MenuItem](MenuItem.html)("[GameObject](GameObject.html)/Create [Folder](WSA.Folder.html) and Some Assets")]
        static void CreateFolder()
        {
            [AssetDatabase.CreateFolder](AssetDatabase.CreateFolder.html)("Assets", "My [Folder](WSA.Folder.html)");
            string guid = [AssetDatabase.CreateFolder](AssetDatabase.CreateFolder.html)("Assets/My [Folder](WSA.Folder.html)", "My Another [Folder](WSA.Folder.html)");
            string newFolderPath = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid);
            [Debug.Log](Debug.Log.html)(newFolderPath);  
      
            // Create a simple material asset in the created folder
            [Material](Material.html) material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Specular"));
            string newAssetPath = newFolderPath + "/MyMaterial.mat";
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(material, newAssetPath);
            [Debug.Log](Debug.Log.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(material));
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

