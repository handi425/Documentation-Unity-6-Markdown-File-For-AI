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

#  [EditorBuildSettings](EditorBuildSettings.html).scenes

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

public static EditorBuildSettingsScene[] scenes;

### Description

The list of Scenes that should be included in the build.

Exposes the list of Scenes that is shown in the [Build
Settings](../Manual/BuildSettings.html) window. You can modify this list to
set up which Scenes should be included in the build.  
  
Note: When calling [BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html)
directly, [BuildPlayerOptions.scenes](BuildPlayerOptions-scenes.html) can be
used instead of this property.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class ExampleWindow : [EditorWindow](EditorWindow.html)
    {
        List<[SceneAsset](SceneAsset.html)> m_SceneAssets = new List<[SceneAsset](SceneAsset.html)>();  
      
        // Add menu item named "Example Window" to the Window menu
        [[MenuItem](MenuItem.html)("Window/Example Window")]
        public static void ShowWindow()
        {
            //Show existing window instance. If one doesn't exist, make one.
            [EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(ExampleWindow));
        }  
      
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("Scenes to include in build:", [EditorStyles.boldLabel](EditorStyles-boldLabel.html));
            for (int i = 0; i < m_SceneAssets.Count; ++i)
            {
                m_SceneAssets[i] = ([SceneAsset](SceneAsset.html))[EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(m_SceneAssets[i], typeof([SceneAsset](SceneAsset.html)), false);
            }
            if ([GUILayout.Button](GUILayout.Button.html)("Add"))
            {
                m_SceneAssets.Add(null);
            }  
      
            [GUILayout.Space](GUILayout.Space.html)(8);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Apply To Build [Settings](CameraEditor.Settings.html)"))
            {
                SetEditorBuildSettingsScenes();
            }
        }  
      
        public void SetEditorBuildSettingsScenes()
        {
            // Find valid [Scene](SceneManagement.Scene.html) paths and make a list of [EditorBuildSettingsScene](EditorBuildSettingsScene.html)
            List<[EditorBuildSettingsScene](EditorBuildSettingsScene.html)> editorBuildSettingsScenes = new List<[EditorBuildSettingsScene](EditorBuildSettingsScene.html)>();
            foreach (var sceneAsset in m_SceneAssets)
            {
                string scenePath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(sceneAsset);
                if (!string.IsNullOrEmpty(scenePath))
                    editorBuildSettingsScenes.Add(new [EditorBuildSettingsScene](EditorBuildSettingsScene.html)(scenePath, true));
            }  
      
            // Set the Build [Settings](CameraEditor.Settings.html) window [Scene](SceneManagement.Scene.html) list
            [EditorBuildSettings.scenes](EditorBuildSettings-scenes.html) = editorBuildSettingsScenes.ToArray();
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

