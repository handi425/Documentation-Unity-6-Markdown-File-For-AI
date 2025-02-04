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

#  [AssetDatabase](AssetDatabase.html).LoadAllAssetsAtPath

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

public static Object[] LoadAllAssetsAtPath(string assetPath);

### Parameters

assetPath | Filesystem path to the asset.  
---|---  
  
### Description

Returns an array of all Assets at `assetPath`.

Some Asset files may contain multiple sub Assets (such as a Maya file which
may contain multiple Meshes and GameObjects).  
All paths are relative to the project folder, for example:
"Assets/MyTextures/hello.png".  
This function returns the [main Asset](AssetDatabase.LoadMainAssetAtPath.html)
and all [sub Assets](AssetDatabase.LoadAllAssetRepresentationsAtPath.html) at
a given path, including those hidden in the Project view.  
  
**Note** : The main asset is not guaranteed to be at index 0 in the array  
  
Additional resources:
[AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html),
[AssetDatabase.LoadAllAssetRepresentationsAtPath](AssetDatabase.LoadAllAssetRepresentationsAtPath.html),
[AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html),
[HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html),
[EditorUtility.UnloadUnusedAssetsImmediate](EditorUtility.UnloadUnusedAssetsImmediate.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/LoadAllAssetsAtPath")]
        private static void PrintAssets()
        {
            Object[] data = [AssetDatabase.LoadAllAssetsAtPath](AssetDatabase.LoadAllAssetsAtPath.html)("Assets/MySpriteTexture.png");  
      
            [Debug.Log](Debug.Log.html)(data.Length + " Assets");  
      
            foreach (Object o in data)
            {
                [Debug.Log](Debug.Log.html)(o);
            }  
      
            // outputs:
            //  5 Assets
            //  MySpriteTexture (UnityEngine.Texture2D)
            //  MyTexture_0 (UnityEngine.Sprite)
            //  MyTexture_1 (UnityEngine.Sprite)
            //  MyTexture_2 (UnityEngine.Sprite)
            //  MyTexture_3 (UnityEngine.Sprite)
        }
    }
    

Additional resources:
[AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html).

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

