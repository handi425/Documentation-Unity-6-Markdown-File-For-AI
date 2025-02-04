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
[EditorSceneManager](SceneManagement.EditorSceneManager.html).playModeStartScene

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

public static [SceneAsset](SceneAsset.html) playModeStartScene;

### Description

Loads this SceneAsset when you start Play Mode.

If this property is set to a SceneAsset, Unity will load this SceneAsset
instead of the Scenes currently open in the Editor when you start Play Mode.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SceneManagement;
    using UnityEngine;  
      
    public class TestWindow : [EditorWindow](EditorWindow.html)
    {
        void OnGUI()
        {
            // Use the Object Picker to select the start [SceneAsset](SceneAsset.html)
            [EditorSceneManager.playModeStartScene](SceneManagement.EditorSceneManager-playModeStartScene.html) = ([SceneAsset](SceneAsset.html))[EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(new [GUIContent](GUIContent.html)("Start [Scene](SceneManagement.Scene.html)"), [EditorSceneManager.playModeStartScene](SceneManagement.EditorSceneManager-playModeStartScene.html), typeof([SceneAsset](SceneAsset.html)), false);  
      
            // Or set the start [Scene](SceneManagement.Scene.html) from code
            var scenePath = "Assets/Scene3.unity";
            if ([GUILayout.Button](GUILayout.Button.html)("Set start [Scene](SceneManagement.Scene.html): " + scenePath))
                SetPlayModeStartScene(scenePath);
        }  
      
        void SetPlayModeStartScene(string scenePath)
        {
            [SceneAsset](SceneAsset.html) myWantedStartScene = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[SceneAsset](SceneAsset.html)>(scenePath);
            if (myWantedStartScene != null)
                [EditorSceneManager.playModeStartScene](SceneManagement.EditorSceneManager-playModeStartScene.html) = myWantedStartScene;
            else
                [Debug.Log](Debug.Log.html)("Could not find [Scene](SceneManagement.Scene.html) " + scenePath);
        }  
      
        [[MenuItem](MenuItem.html)("Test/Open")]
        static void Open()
        {
            GetWindow<TestWindow>();
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

