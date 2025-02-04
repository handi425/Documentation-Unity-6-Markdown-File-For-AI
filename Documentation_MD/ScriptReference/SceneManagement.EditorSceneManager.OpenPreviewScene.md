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
[EditorSceneManager](SceneManagement.EditorSceneManager.html).OpenPreviewScene

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

public static [SceneManagement.Scene](SceneManagement.Scene.html)
OpenPreviewScene(string scenePath);

### Parameters

scenePath | Scene file to open.  
---|---  
  
### Returns

**Scene** The created preview Scene.

### Description

Opens a Scene Asset in a preview Scene.

You can use this function for tooling that needs to access GameObjects but
where the scene should not be displayed in the Hierarchy. Make sure to call
[ClosePreviewScene](SceneManagement.EditorSceneManager.ClosePreviewScene.html)
to prevent leaking scenes.  
  
Additional resources:
[NewPreviewScene](SceneManagement.EditorSceneManager.NewPreviewScene.html),
[ClosePreviewScene](SceneManagement.EditorSceneManager.ClosePreviewScene.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SceneManagement;
    using UnityEngine;  
      
    public static class TestOpenAsPreviewScene
    {
        [[MenuItem](MenuItem.html)("Assets/[Scene](SceneManagement.Scene.html) Root Names")]
        static void OpenContextClickedSceneInAPreviewScene()
        {
            [SceneAsset](SceneAsset.html) sceneAsset = [Selection.activeObject](Selection-activeObject.html) as [SceneAsset](SceneAsset.html);
            if (sceneAsset == null)
            {
                [Debug.Log](Debug.Log.html)("Context click on a [Scene](SceneManagement.Scene.html) [Asset](VersionControl.Asset.html) file");
                return;
            }  
      
            var assetPath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(sceneAsset);
            var scene = [EditorSceneManager.OpenPreviewScene](SceneManagement.EditorSceneManager.OpenPreviewScene.html)(assetPath);
            try
            {
                var rootGameObjects = scene.GetRootGameObjects();  
      
                [Debug.Log](Debug.Log.html)($"Root [GameObject](GameObject.html) Names (count: {rootGameObjects.Length})");
                foreach (var gameObject in rootGameObjects)
                    [Debug.Log](Debug.Log.html)(gameObject.name);
            }
            finally
            {
                [EditorSceneManager.ClosePreviewScene](SceneManagement.EditorSceneManager.ClosePreviewScene.html)(scene);
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

