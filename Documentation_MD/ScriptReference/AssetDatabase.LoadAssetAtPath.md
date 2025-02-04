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

#  [AssetDatabase](AssetDatabase.html).LoadAssetAtPath

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

public static Object LoadAssetAtPath(string assetPath, Type type);

### Parameters

assetPath | Path of the asset to load.  
---|---  
type | Data type of the asset.  
  
### Returns

**Object** The asset matching the parameters.

### Description

Returns the first asset object of type **type** at given path **assetPath**.

Some asset files may contain multiple objects. (such as a Maya file which may
contain multiple Meshes and GameObjects). All paths are relative to the
project folder, for example: "Assets/MyTextures/hello.png".  
  
**Note:**  
The **assetPath** parameter is not case sensitive.  
**ALL** asset names and paths in Unity use forward slashes, even on Windows.  
This returns only an asset object that is visible in the Project view. If the
asset is not found `LoadAssetAtPath` returns Null.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MyPlayer : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/LoadAssetExample")]
        static void ImportExample()
        {
            [Texture2D](Texture2D.html) t = ([Texture2D](Texture2D.html))[AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)("Assets/Textures/texture.jpg", typeof([Texture2D](Texture2D.html)));
        }
    }
    

Additional resources:
[AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html),
[AssetDatabase.LoadAllAssetsAtPath](AssetDatabase.LoadAllAssetsAtPath.html).

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

