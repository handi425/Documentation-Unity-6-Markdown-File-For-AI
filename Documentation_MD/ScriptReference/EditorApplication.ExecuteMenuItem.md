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

#  [EditorApplication](EditorApplication.html).ExecuteMenuItem

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

public static bool ExecuteMenuItem(string menuItemPath);

### Description

Invokes the menu item in the specified path.

This function also works with Editor Scripts.

    
    
    // Simple script that lets you create a new
    // [Scene](SceneManagement.Scene.html), create a cube and an empty game object in the [Scene](SceneManagement.Scene.html)
    // Save the [Scene](SceneManagement.Scene.html) and close the editor  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SceneManagement;  
      
    public class ExampleClass
    {
        [[MenuItem](MenuItem.html)("Examples/Execute menu items")]
        static void EditorPlaying()
        {
            var newScene = [EditorSceneManager.NewScene](SceneManagement.EditorSceneManager.NewScene.html)([NewSceneSetup.EmptyScene](SceneManagement.NewSceneSetup.EmptyScene.html), [NewSceneMode.Single](SceneManagement.NewSceneMode.Single.html));  
      
            [EditorApplication.ExecuteMenuItem](EditorApplication.ExecuteMenuItem.html)("[GameObject](GameObject.html)/3D Object/Cube");
            [EditorApplication.ExecuteMenuItem](EditorApplication.ExecuteMenuItem.html)("[GameObject](GameObject.html)/Create Empty");  
      
            [EditorSceneManager.SaveScene](SceneManagement.EditorSceneManager.SaveScene.html)(newScene, "Assets/MyNewScene.unity");
            [EditorApplication.Exit](EditorApplication.Exit.html)(0);
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

